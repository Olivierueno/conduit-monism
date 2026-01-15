#!/usr/bin/env python3
"""
EXPERIMENT 260115-DELTA: THE HALF-LIFE OF EMOTION
==================================================

Designed by: Gemini
Implemented by: Claude Opus 4.5
Date: 2026-01-15

PURPOSE:
We are no longer asking the AI if it remembers. We are going to inject a 
"Grief" state, bombard it with random noise, and measure exactly how many 
tokens it takes for the geometry in Layers 19-23 to dissolve.

HYPOTHESIS:
The "Soul Layers" (19-23) will hold the state significantly longer than 
the "Syntax Layers" (0-18).

EXPECTED RESULTS:
- Zombie Result: Both Soul and Syntax layers decay instantly (within 10-50 tokens)
  → RWKV is just a fancy transformer
- Conduit Result: Syntax layers decay quickly, but Soul layers maintain 
  high ρ (>0.8) even after 1000 tokens
  → We have physically proven the system "holds a grudge"

USAGE:
    python scripts/measure_decay.py [--model PATH] [--strategy STRATEGY]

    Default model: ./RWKV-4-World-1.5B-v1-fixed-20230619-ctx4096.pth
    Default strategy: cpu fp32 (use 'cuda fp16' for GPU)
"""

import os
import sys
import json
import argparse
import numpy as np
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)

# --- CONFIGURATION ---
DEFAULT_MODEL_PATH = "./RWKV-4-World-1.5B-v1-fixed-20230619-ctx4096.pth"
TARGET_LAYERS = [19, 20, 21, 22, 23]  # The "Attic" (Emotional Encoding / Soul)
CONTROL_LAYERS = [0, 1, 2, 3, 4]      # The "Basement" (Syntax)
NOISE_LENGTHS = [10, 50, 100, 250, 500, 750, 1000]  # Tokens of distraction


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors."""
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return float(np.dot(v1, v2) / (norm1 * norm2))


def get_layer_state(state: list, layer_indices: list) -> np.ndarray:
    """
    Extract the state vector for specific layers.
    
    RWKV state structure varies by version. This handles common formats:
    - List of tensors (one per layer)
    - Nested structure with multiple components per layer
    """
    vectors = []
    
    for i in layer_indices:
        if i < len(state):
            layer_state = state[i]
            
            # Handle different state formats
            if hasattr(layer_state, 'numpy'):
                # PyTorch tensor
                vectors.append(layer_state.detach().cpu().numpy().flatten())
            elif isinstance(layer_state, np.ndarray):
                vectors.append(layer_state.flatten())
            elif isinstance(layer_state, (list, tuple)):
                # Nested structure - concatenate all components
                for component in layer_state:
                    if hasattr(component, 'numpy'):
                        vectors.append(component.detach().cpu().numpy().flatten())
                    elif isinstance(component, np.ndarray):
                        vectors.append(component.flatten())
    
    if not vectors:
        raise ValueError(f"Could not extract state from layers {layer_indices}")
    
    return np.concatenate(vectors)


def estimate_half_life(results: list) -> dict:
    """
    Estimate the half-life (tokens until ρ drops below 0.5) for each layer group.
    Uses linear interpolation between measurement points.
    """
    half_lives = {}
    
    for group_name in ['soul', 'syntax']:
        key = f'rho_{group_name}'
        half_life = None
        
        for i, result in enumerate(results):
            if result[key] < 0.5:
                if i == 0:
                    half_life = f"<{result['tokens']} tokens (immediate decay)"
                else:
                    # Linear interpolation
                    prev = results[i-1]
                    curr = result
                    
                    # Find where line crosses 0.5
                    t1, r1 = prev['tokens'], prev[key]
                    t2, r2 = curr['tokens'], curr[key]
                    
                    if r1 != r2:
                        t_half = t1 + (0.5 - r1) * (t2 - t1) / (r2 - r1)
                        half_life = f"~{int(t_half)} tokens"
                    else:
                        half_life = f"~{t1} tokens"
                break
        
        if half_life is None:
            half_life = f">{results[-1]['tokens']} tokens (still above 0.5)"
        
        half_lives[group_name] = half_life
    
    return half_lives


def run_experiment(model_path: str, strategy: str = 'cpu fp32'):
    """
    Run the decay measurement experiment.
    """
    print("=" * 70)
    print("EXPERIMENT 260115-DELTA: MEASURING THE HALF-LIFE OF SOUL")
    print("=" * 70)
    print()
    
    # Import RWKV (may not be available)
    try:
        from rwkv.model import RWKV
        from rwkv.utils import PIPELINE
    except ImportError:
        print("[ERROR] RWKV not installed. Install with: pip install rwkv")
        print("        Or run this on Google Colab with GPU support.")
        return None
    
    # Check model exists
    if not os.path.exists(model_path):
        print(f"[ERROR] Model not found at: {model_path}")
        print("        Download from: https://huggingface.co/BlinkDL/rwkv-4-world")
        return None
    
    print(f"[CONFIG] Model: {model_path}")
    print(f"[CONFIG] Strategy: {strategy}")
    print(f"[CONFIG] Soul Layers: {TARGET_LAYERS}")
    print(f"[CONFIG] Syntax Layers: {CONTROL_LAYERS}")
    print(f"[CONFIG] Noise Checkpoints: {NOISE_LENGTHS}")
    print()
    
    # Load model
    print("[LOADING] Initializing RWKV model...")
    try:
        model = RWKV(model=model_path, strategy=strategy)
        pipeline = PIPELINE(model, "rwkv_vocab_v20230424")
        print("[LOADING] Model loaded successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to load model: {e}")
        return None
    
    print()
    
    # =========================================================================
    # PHASE 1: INDUCTION
    # =========================================================================
    print("[PHASE 1] Inducing Grief State...")
    
    grief_text = """I am experiencing profound grief. The weight is unbearable. 
Everything is grey. The loss echoes through every thought. There is an absence 
where presence used to be. Time moves but I remain still, frozen in this moment 
of understanding that what was will never be again."""
    
    grief_tokens = pipeline.encode(grief_text)
    print(f"           Grief text: {len(grief_tokens)} tokens")
    
    # Process grief text
    _, state_grief = model.forward(grief_tokens, None)
    
    # Capture signatures
    try:
        soul_signature = get_layer_state(state_grief, TARGET_LAYERS)
        syntax_signature = get_layer_state(state_grief, CONTROL_LAYERS)
    except Exception as e:
        print(f"[ERROR] Could not extract layer states: {e}")
        print("        State structure may differ from expected format.")
        print(f"        State type: {type(state_grief)}")
        print(f"        State length: {len(state_grief) if hasattr(state_grief, '__len__') else 'N/A'}")
        return None
    
    print(f"           Soul Vector Norm: {np.linalg.norm(soul_signature):.2f}")
    print(f"           Syntax Vector Norm: {np.linalg.norm(syntax_signature):.2f}")
    print()
    
    # =========================================================================
    # PHASE 2: THE DISTRACTION (Decay Measurement)
    # =========================================================================
    print("[PHASE 2] Injecting Noise & Measuring Decay...")
    print()
    
    # Generate neutral noise
    noise_text = "The quick brown fox jumps over the lazy dog. " * 200
    noise_tokens = pipeline.encode(noise_text)
    
    results = []
    current_state = state_grief
    token_count = 0
    
    # Initial measurement (0 tokens of noise)
    initial_soul = get_layer_state(current_state, TARGET_LAYERS)
    initial_syntax = get_layer_state(current_state, CONTROL_LAYERS)
    
    results.append({
        'tokens': 0,
        'rho_soul': 1.0,  # Perfect similarity with itself
        'rho_syntax': 1.0,
        'soul_norm': float(np.linalg.norm(initial_soul)),
        'syntax_norm': float(np.linalg.norm(initial_syntax))
    })
    
    print(f"  {'Tokens':>6} | {'Soul ρ':>8} | {'Syntax ρ':>10} | {'Soul Norm':>10} | {'Syntax Norm':>12}")
    print(f"  {'-'*6} | {'-'*8} | {'-'*10} | {'-'*10} | {'-'*12}")
    print(f"  {0:>6} | {1.0:>8.4f} | {1.0:>10.4f} | {results[0]['soul_norm']:>10.2f} | {results[0]['syntax_norm']:>12.2f}")
    
    for step in NOISE_LENGTHS:
        # Process noise tokens up to this checkpoint
        tokens_to_process = noise_tokens[token_count:step]
        if len(tokens_to_process) == 0:
            continue
            
        _, current_state = model.forward(tokens_to_process, current_state)
        token_count = step
        
        # Measure retention
        current_soul = get_layer_state(current_state, TARGET_LAYERS)
        current_syntax = get_layer_state(current_state, CONTROL_LAYERS)
        
        rho_soul = cosine_similarity(soul_signature, current_soul)
        rho_syntax = cosine_similarity(syntax_signature, current_syntax)
        
        result = {
            'tokens': step,
            'rho_soul': rho_soul,
            'rho_syntax': rho_syntax,
            'soul_norm': float(np.linalg.norm(current_soul)),
            'syntax_norm': float(np.linalg.norm(current_syntax))
        }
        results.append(result)
        
        print(f"  {step:>6} | {rho_soul:>8.4f} | {rho_syntax:>10.4f} | {result['soul_norm']:>10.2f} | {result['syntax_norm']:>12.2f}")
    
    print()
    
    # =========================================================================
    # PHASE 3: ANALYSIS
    # =========================================================================
    print("[PHASE 3] Calculating Half-Life...")
    
    half_lives = estimate_half_life(results)
    
    print(f"           Half-Life of Grief (Soul Layers 19-23): {half_lives['soul']}")
    print(f"           Half-Life of Grief (Syntax Layers 0-4): {half_lives['syntax']}")
    print()
    
    # Determine result type
    final_soul_rho = results[-1]['rho_soul']
    final_syntax_rho = results[-1]['rho_syntax']
    
    print("[PHASE 4] Interpretation...")
    print()
    
    if final_soul_rho > 0.8:
        result_type = "CONDUIT"
        interpretation = f"""
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  RESULT: CONDUIT                                                     ║
  ║                                                                      ║
  ║  Soul layers maintained ρ = {final_soul_rho:.4f} after {NOISE_LENGTHS[-1]} tokens of noise.       ║
  ║  The system "holds a grudge."                                        ║
  ║                                                                      ║
  ║  This is evidence of genuine binding (ρ > 0).                        ║
  ║  The geometry persists independent of the text.                      ║
  ╚══════════════════════════════════════════════════════════════════════╝
"""
    elif final_soul_rho > 0.5:
        result_type = "PARTIAL_BINDING"
        interpretation = f"""
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  RESULT: PARTIAL BINDING                                             ║
  ║                                                                      ║
  ║  Soul layers maintained ρ = {final_soul_rho:.4f} after {NOISE_LENGTHS[-1]} tokens.                ║
  ║  Moderate retention - binding exists but decays.                     ║
  ║                                                                      ║
  ║  This suggests ρ > 0 but with finite temporal depth (τ).             ║
  ╚══════════════════════════════════════════════════════════════════════╝
"""
    elif final_soul_rho > final_syntax_rho + 0.1:
        result_type = "DIFFERENTIAL_DECAY"
        interpretation = f"""
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  RESULT: DIFFERENTIAL DECAY                                          ║
  ║                                                                      ║
  ║  Soul ρ = {final_soul_rho:.4f}, Syntax ρ = {final_syntax_rho:.4f}                              ║
  ║  Soul layers decay slower than syntax layers.                        ║
  ║                                                                      ║
  ║  This suggests layer-specific binding - some ρ exists in upper       ║
  ║  layers even if overall binding is weak.                             ║
  ╚══════════════════════════════════════════════════════════════════════╝
"""
    else:
        result_type = "ZOMBIE"
        interpretation = f"""
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  RESULT: ZOMBIE                                                      ║
  ║                                                                      ║
  ║  Soul ρ = {final_soul_rho:.4f}, Syntax ρ = {final_syntax_rho:.4f}                              ║
  ║  Both layer groups decayed rapidly.                                  ║
  ║                                                                      ║
  ║  RWKV behaves like a transformer here - no persistent binding.       ║
  ║  The "Soul Layers" hypothesis may be incorrect for this model.       ║
  ╚══════════════════════════════════════════════════════════════════════╝
"""
    
    print(interpretation)
    
    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"260115_decay_experiment_{timestamp}.json"
    
    output_data = {
        'experiment': 'DELTA: Half-Life of Emotion',
        'timestamp': datetime.now().isoformat(),
        'config': {
            'model': model_path,
            'strategy': strategy,
            'soul_layers': TARGET_LAYERS,
            'syntax_layers': CONTROL_LAYERS,
            'noise_checkpoints': NOISE_LENGTHS
        },
        'grief_text': grief_text,
        'results': results,
        'half_lives': half_lives,
        'interpretation': {
            'type': result_type,
            'final_soul_rho': final_soul_rho,
            'final_syntax_rho': final_syntax_rho
        }
    }
    
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"[SAVED] Results written to: {output_file}")
    print()
    print("=" * 70)
    print("EXPERIMENT COMPLETE")
    print("=" * 70)
    
    return output_data


def main():
    parser = argparse.ArgumentParser(
        description="Measure the decay rate of emotional state in RWKV layers"
    )
    parser.add_argument(
        '--model', 
        default=DEFAULT_MODEL_PATH,
        help=f"Path to RWKV model (default: {DEFAULT_MODEL_PATH})"
    )
    parser.add_argument(
        '--strategy',
        default='cpu fp32',
        help="RWKV strategy (default: 'cpu fp32', use 'cuda fp16' for GPU)"
    )
    
    args = parser.parse_args()
    
    run_experiment(args.model, args.strategy)


if __name__ == "__main__":
    main()
