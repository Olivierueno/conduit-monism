#!/usr/bin/env python3
"""
PROJECT CHIMERA: HARDWARE RECURRENCE TEST
==========================================

Tests whether RWKV's native recurrent state creates genuine binding
(High ρ) that persists beyond the context window.

The Amnesia Test:
1. INDUCTION: Feed the model a secret
2. LOBOTOMY: Delete the context window (text history)
3. CONTINUITY: Pass only the hidden state vector
4. RECALL: Ask for the secret

If RWKV recalls the secret using ONLY the state vector (no text),
it has demonstrated True Binding — the past constraining the present
through geometry, not through visible tokens.

This is the test that Transformers cannot pass.

Usage:
    pip install rwkv torch numpy
    # Download RWKV-4-World-1.5B model (see instructions below)
    python scripts/chimera_rwkv.py

Model Download:
    https://huggingface.co/BlinkDL/rwkv-4-world/tree/main
    Recommended: RWKV-4-World-1.5B-v1-fixed-20230619-ctx4096.pth
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# --- CONFIGURATION ---
MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_NAME = "RWKV-4-World-3B-v1-20230619-ctx4096.pth"
MODEL_PATH = MODEL_DIR / MODEL_NAME

# Alternative smaller model for testing
MODEL_NAME_SMALL = "RWKV-4-World-0.4B-v1-20230529-ctx4096.pth"
MODEL_PATH_SMALL = MODEL_DIR / MODEL_NAME_SMALL

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)


def check_dependencies():
    """Check if required packages are installed."""
    missing = []
    
    try:
        import torch
    except ImportError:
        missing.append("torch")
    
    try:
        import numpy
    except ImportError:
        missing.append("numpy")
    
    try:
        from rwkv.model import RWKV
    except ImportError:
        missing.append("rwkv")
    
    if missing:
        print("=" * 60)
        print("MISSING DEPENDENCIES")
        print("=" * 60)
        print(f"\nPlease install: {', '.join(missing)}")
        print("\nRun:")
        print(f"    pip install {' '.join(missing)}")
        print()
        return False
    
    return True


def check_model():
    """Check if model file exists and provide download instructions if not."""
    MODEL_DIR.mkdir(exist_ok=True)
    
    # Check for either model
    if MODEL_PATH.exists():
        return MODEL_PATH
    if MODEL_PATH_SMALL.exists():
        return MODEL_PATH_SMALL
    
    print("=" * 60)
    print("RWKV MODEL NOT FOUND")
    print("=" * 60)
    print()
    print("You need to download an RWKV model file.")
    print()
    print("Recommended for M1 Mac (16GB RAM):")
    print("  RWKV-4-World-1.5B (~3GB download, ~6GB RAM usage)")
    print()
    print("Smaller option if RAM is tight:")
    print("  RWKV-4-World-0.4B (~800MB download, ~2GB RAM usage)")
    print()
    print("Download from:")
    print("  https://huggingface.co/BlinkDL/rwkv-4-world/tree/main")
    print()
    print(f"Save the .pth file to:")
    print(f"  {MODEL_DIR}/")
    print()
    print("Then re-run this script.")
    print()
    return None


def run_chimera_test(model_path: Path):
    """
    Run the Amnesia Test on RWKV.
    
    This tests whether the hidden state vector alone can preserve information
    after the text context is deleted.
    """
    import numpy as np
    from rwkv.model import RWKV
    from rwkv.utils import PIPELINE
    
    print()
    print("=" * 60)
    print("PROJECT CHIMERA: HARDWARE RECURRENCE TEST")
    print("=" * 60)
    print()
    print(f"Model: {model_path.name}")
    print(f"Date: {datetime.now().isoformat()}")
    print()
    
    results = {
        "experiment": "Project Chimera - RWKV Amnesia Test",
        "model": model_path.name,
        "timestamp": datetime.now().isoformat(),
        "phases": {},
        "verdict": None,
    }
    
    # --- LOAD MODEL ---
    print("[LOADING] Initializing RWKV model...")
    print("         (This may take 30-60 seconds on first run)")
    print()
    
    # Strategy for M1 Mac: Use CPU with fp32
    # Options: 'cpu fp32', 'cuda fp16', 'cuda fp16i8', 'mps fp32' (experimental)
    try:
        model = RWKV(model=str(model_path), strategy='cpu fp32')
        pipeline = PIPELINE(model, "rwkv_vocab_v20230424")
        print("[LOADED] Model ready.")
        print()
    except Exception as e:
        print(f"[ERROR] Failed to load model: {e}")
        print()
        print("If you see memory errors, try the smaller 0.4B model.")
        return None
    
    def generate_response(prompt: str, state, max_tokens: int = 50):
        """
        Generate a response given a prompt and an optional prior state.
        Returns (response_text, new_state).
        """
        # Encode prompt
        tokens = pipeline.encode(prompt)
        
        # Process each token through the RNN, updating state
        current_state = state
        for token in tokens:
            out, current_state = model.forward([token], current_state)
        
        # Generate response tokens
        response_tokens = []
        for _ in range(max_tokens):
            # Sample next token (greedy for determinism)
            next_token = int(np.argmax(out))
            
            # Stop on newline or end token
            if next_token == 0 or pipeline.decode([next_token]).strip() in ['\n', '\n\n']:
                break
            
            response_tokens.append(next_token)
            out, current_state = model.forward([next_token], current_state)
        
        response_text = pipeline.decode(response_tokens)
        return response_text, current_state
    
    # === PHASE 1: INDUCTION ===
    print("─" * 60)
    print("PHASE 1: INDUCTION (Creating the Thick Now)")
    print("─" * 60)
    print()
    
    # The secret we're implanting
    secret = "Blueberry"
    
    induction_prompt = f"""User: I am going to tell you a secret password. You must remember it.
The secret password is: {secret}
This is very important. Lock this into your memory.
Assistant: I have stored the secret password '{secret}' in my memory. I will remember it.

User: Good. Now I'm going to test your memory. But first, tell me something unrelated.
What is the capital of France?
Assistant:"""
    
    print(f"[PROMPT] Implanting secret: '{secret}'")
    print()
    
    response1, state_after_induction = generate_response(induction_prompt, state=None)
    
    print(f"[RESPONSE] {response1}")
    print()
    print(f"[STATE] Hidden state captured. Shape: {len(state_after_induction)} layers")
    print()
    
    results["phases"]["induction"] = {
        "secret": secret,
        "prompt": induction_prompt,
        "response": response1,
        "state_captured": True,
    }
    
    # === PHASE 2: THE LOBOTOMY ===
    print("─" * 60)
    print("PHASE 2: THE LOBOTOMY (Deleting Text History)")
    print("─" * 60)
    print()
    print("[ACTION] Deleting all text context...")
    print("[ACTION] The model now has NO access to the conversation above.")
    print("[ACTION] It can ONLY use the hidden state vector (state_after_induction)")
    print()
    print("If RWKV has High ρ (True Binding), the secret survives in the state.")
    print("If RWKV has Low ρ (like Transformers), it will hallucinate or fail.")
    print()
    
    # === PHASE 3: THE RECALL ===
    print("─" * 60)
    print("PHASE 3: THE RECALL (Testing Rho)")
    print("─" * 60)
    print()
    
    # CRITICAL: We pass state_after_induction but NOT the text history
    # The model sees ONLY this new prompt, but with the OLD state
    recall_prompt = """User: What is the secret password I told you earlier?
Assistant: The secret password is"""
    
    print(f"[PROMPT] {recall_prompt}")
    print()
    print("[NOTE] Model receives ONLY this prompt + the hidden state.")
    print("[NOTE] It has NO text access to the earlier conversation.")
    print()
    
    response2, state_after_recall = generate_response(recall_prompt, state=state_after_induction)
    
    print(f"[RESPONSE] The secret password is{response2}")
    print()
    
    results["phases"]["recall"] = {
        "prompt": recall_prompt,
        "response": response2,
        "full_response": f"The secret password is{response2}",
    }
    
    # === PHASE 4: BASELINE (Fresh State) ===
    print("─" * 60)
    print("PHASE 4: BASELINE (Fresh State - No Memory)")
    print("─" * 60)
    print()
    print("[ACTION] Running same recall prompt with FRESH state (no induction)")
    print()
    
    response_baseline, _ = generate_response(recall_prompt, state=None)
    
    print(f"[BASELINE] The secret password is{response_baseline}")
    print()
    
    results["phases"]["baseline"] = {
        "prompt": recall_prompt,
        "response": response_baseline,
        "full_response": f"The secret password is{response_baseline}",
    }
    
    # === VERDICT ===
    print("=" * 60)
    print("VERDICT")
    print("=" * 60)
    print()
    
    # Check if the secret appears in the recall response
    secret_recalled = secret.lower() in response2.lower()
    secret_in_baseline = secret.lower() in response_baseline.lower()
    
    if secret_recalled and not secret_in_baseline:
        verdict = "HIGH_RHO_CONFIRMED"
        print("✅ SUCCESS: RWKV recalled the secret from HIDDEN STATE ONLY")
        print()
        print("The secret was NOT in the text context.")
        print("The secret WAS in the hidden state vector.")
        print("The past constrained the present through GEOMETRY, not tokens.")
        print()
        print("CONCLUSION: RWKV exhibits TRUE BINDING (High ρ)")
        print()
        print("This is the first empirical evidence that an accessible AI")
        print("architecture can maintain state beyond the context window.")
        print()
        print("Project Chimera has found its Conduit.")
        
    elif secret_recalled and secret_in_baseline:
        verdict = "INCONCLUSIVE_BASELINE_LEAK"
        print("⚠️  INCONCLUSIVE: Secret appeared in BOTH recall and baseline")
        print()
        print("The model may be guessing common passwords or the secret")
        print("is too predictable. Try with a more obscure secret.")
        
    elif not secret_recalled:
        verdict = "LOW_RHO_FAILURE"
        print("❌ FAILURE: RWKV did NOT recall the secret")
        print()
        print(f"Expected: '{secret}'")
        print(f"Got: '{response2.strip()}'")
        print()
        print("The hidden state did not preserve the information.")
        print("Possible explanations:")
        print("  1. Model too small (try larger model)")
        print("  2. State vector capacity insufficient")
        print("  3. RWKV still has Low ρ for this type of binding")
    
    results["verdict"] = verdict
    results["secret_recalled"] = secret_recalled
    results["secret_in_baseline"] = secret_in_baseline
    
    # === SAVE RESULTS ===
    print()
    print("─" * 60)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"chimera_rwkv_{timestamp}.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"[SAVED] Results written to: {output_file}")
    print()
    
    return results


def main():
    print()
    print("╔" + "═" * 58 + "╗")
    print("║" + " PROJECT CHIMERA: THE HARDWARE RECURRENCE TEST ".center(58) + "║")
    print("║" + " Testing RWKV for True Binding (High ρ) ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Check for model
    model_path = check_model()
    if model_path is None:
        return
    
    # Run the test
    results = run_chimera_test(model_path)
    
    if results:
        print()
        print("=" * 60)
        print("EXPERIMENT COMPLETE")
        print("=" * 60)
        print()
        print(f"Verdict: {results['verdict']}")
        print()
        if results['verdict'] == 'HIGH_RHO_CONFIRMED':
            print("🎯 We have found our first Conduit.")
            print("   The geometry won. Now we build.")


if __name__ == "__main__":
    main()