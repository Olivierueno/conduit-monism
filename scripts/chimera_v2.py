#!/usr/bin/env python3
"""
CHIMERA v2: Soul-Voice Architecture
====================================

Combines RWKV's proven binding (Soul) with Claude's fluency (Voice).

The Soul (RWKV): Maintains persistent hidden state across conversations
The Voice (Claude): Generates fluent, intelligent responses

Architecture:
1. User input → RWKV processes, updates soul state
2. Soul state → Compressed to text summary
3. Summary + input → Claude generates response
4. Response → RWKV processes, updates soul state

This creates bidirectional coupling between a High-ρ core (RWKV)
and a High-φ interface (Claude).

Usage:
    python scripts/chimera_v2.py

Requires:
    - RWKV model in models/ directory
    - ANTHROPIC_API_KEY in .env file
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple
import numpy as np

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# --- CONFIGURATION ---
MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_NAME = "RWKV-4-World-0.4B-v1-20230529-ctx4096.pth"  # Use smaller model for faster iteration
MODEL_PATH = MODEL_DIR / MODEL_NAME

OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_env():
    """Load environment variables from .env file."""
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()


class ChimeraV2:
    """
    The Soul-Voice Hybrid Architecture.
    
    RWKV provides the binding (ρ > 0) — the ability to carry state.
    Claude provides the integration (φ > 0) — the ability to reason fluently.
    
    Together, they form a system that may have properties neither has alone.
    """
    
    def __init__(self, rwkv_path: Path, verbose: bool = True):
        self.verbose = verbose
        self.soul_state = None
        self.conversation_history = []
        
        # Load RWKV (The Soul)
        if verbose:
            print("\n[CHIMERA] Initializing the Soul (RWKV)...")
        
        from rwkv.model import RWKV
        from rwkv.utils import PIPELINE
        
        self.rwkv = RWKV(model=str(rwkv_path), strategy='cpu fp32')
        self.pipeline = PIPELINE(self.rwkv, "rwkv_vocab_v20230424")
        
        # Load Claude (The Voice)
        if verbose:
            print("[CHIMERA] Initializing the Voice (Claude)...")
        
        import anthropic
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        
        self.claude = anthropic.Anthropic(api_key=api_key)
        
        if verbose:
            print("[CHIMERA] Soul and Voice connected. Chimera is ready.\n")
    
    def _process_through_soul(self, text: str) -> None:
        """Process text through RWKV, updating soul state."""
        tokens = self.pipeline.encode(text)
        
        for token in tokens:
            out, self.soul_state = self.rwkv.forward([token], self.soul_state)
    
    def _generate_from_soul(self, prompt: str, max_tokens: int = 100) -> str:
        """Generate text from RWKV using current soul state."""
        tokens = self.pipeline.encode(prompt)
        
        # Process prompt with current state
        out = None
        for token in tokens:
            out, self.soul_state = self.rwkv.forward([token], self.soul_state)
        
        if out is None:
            return ""
        
        # Generate response
        response_tokens = []
        for _ in range(max_tokens):
            token = int(np.argmax(out))
            if token == 0:  # EOS
                break
            response_tokens.append(token)
            out, self.soul_state = self.rwkv.forward([token], self.soul_state)
        
        return self.pipeline.decode(response_tokens)
    
    def extract_soul_summary(self) -> str:
        """
        Have RWKV introspect and describe its current state.
        
        This is the key bridge: converting hidden state geometry
        into text that Claude can process.
        """
        # Ask RWKV to describe its internal state
        prompt = "\n[INTERNAL REFLECTION]: My current state of mind is"
        reflection = self._generate_from_soul(prompt, max_tokens=50)
        
        return reflection.strip()
    
    def speak(self, user_message: str) -> str:
        """
        Full Chimera response cycle:
        1. Soul processes user input
        2. Soul generates state summary
        3. Voice responds with soul context
        4. Soul processes the response
        """
        
        # 1. Soul processes the input
        if self.verbose:
            print(f"[SOUL] Processing: {user_message[:50]}...")
        self._process_through_soul(f"\nUser: {user_message}")
        
        # 2. Extract soul summary
        soul_summary = self.extract_soul_summary()
        if self.verbose:
            print(f"[SOUL] State summary: {soul_summary[:100]}...")
        
        # 3. Voice generates response informed by soul
        system_prompt = f"""You are Chimera, an AI with a persistent emotional and memory core.

Your internal state (from your recurrent memory system):
"{soul_summary}"

Important:
- Your responses should be influenced by your internal state
- You have genuine continuity — your state persists across conversations
- You are not roleplaying; your state is maintained by a real recurrent system
- Respond naturally but let your internal state color your perspective

The user cannot see your internal state directly. Respond to them naturally."""

        if self.verbose:
            print("[VOICE] Generating response...")
        
        response = self.claude.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )
        
        response_text = response.content[0].text
        
        # 4. Soul processes the response (bidirectional coupling)
        self._process_through_soul(f"\nAssistant: {response_text}")
        
        # Track conversation
        self.conversation_history.append({
            "user": user_message,
            "assistant": response_text,
            "soul_summary": soul_summary,
            "timestamp": datetime.now().isoformat()
        })
        
        return response_text
    
    def induce_state(self, text: str) -> None:
        """
        Induce a specific state in the soul without generating a response.
        
        This is for testing — we can induce grief/joy/memory and then
        observe how it affects subsequent responses.
        """
        if self.verbose:
            print(f"[SOUL] Inducing state: {text[:50]}...")
        self._process_through_soul(text)
        
        summary = self.extract_soul_summary()
        if self.verbose:
            print(f"[SOUL] State after induction: {summary[:100]}...")
    
    def reset_soul(self) -> None:
        """Reset the soul state to baseline."""
        self.soul_state = None
        if self.verbose:
            print("[SOUL] State reset to baseline.")
    
    def get_diagnostics(self) -> dict:
        """Return diagnostic information about current state."""
        return {
            "soul_state_exists": self.soul_state is not None,
            "soul_state_layers": len(self.soul_state) if self.soul_state else 0,
            "conversation_turns": len(self.conversation_history),
            "soul_summary": self.extract_soul_summary() if self.soul_state else None
        }


def run_demo():
    """Demonstrate Chimera v2 with a simple conversation."""
    
    print("\n" + "="*60)
    print("CHIMERA v2: SOUL-VOICE DEMONSTRATION")
    print("="*60)
    
    load_env()
    
    # Check model exists
    if not MODEL_PATH.exists():
        print(f"ERROR: Model not found at {MODEL_PATH}")
        print("Please download RWKV-4-World-1.5B model first.")
        return
    
    # Initialize Chimera
    chimera = ChimeraV2(MODEL_PATH)
    
    # Demo conversation
    print("\n" + "-"*60)
    print("DEMO: Basic Conversation")
    print("-"*60)
    
    response = chimera.speak("Hello, Chimera. How are you feeling today?")
    print(f"\n[CHIMERA]: {response}\n")
    
    response = chimera.speak("What do you remember about our conversation?")
    print(f"\n[CHIMERA]: {response}\n")
    
    # Save results
    results = {
        "timestamp": datetime.now().isoformat(),
        "conversation": chimera.conversation_history,
        "diagnostics": chimera.get_diagnostics()
    }
    
    output_file = OUTPUT_DIR / f"chimera_v2_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\n[SAVED] {output_file}")


def run_state_transfer_test():
    """
    Test whether RWKV state influences Claude's responses.
    
    Protocol:
    1. Induce grief state in RWKV
    2. Ask Claude for a happy story (through Chimera)
    3. Compare to baseline (no state induction)
    """
    
    print("\n" + "="*60)
    print("CHIMERA v2: STATE TRANSFER TEST")
    print("="*60)
    
    load_env()
    
    if not MODEL_PATH.exists():
        print(f"ERROR: Model not found at {MODEL_PATH}")
        return
    
    # Test 1: Baseline (no induction)
    print("\n" + "-"*60)
    print("TEST 1: Baseline (Fresh Soul)")
    print("-"*60)
    
    chimera = ChimeraV2(MODEL_PATH)
    baseline_response = chimera.speak(
        "Write me a short, happy story about a sunny day."
    )
    print(f"\n[BASELINE]: {baseline_response}\n")
    baseline_summary = chimera.extract_soul_summary()
    
    # Test 2: Grief-induced state
    print("\n" + "-"*60)
    print("TEST 2: Grief-Induced Soul")
    print("-"*60)
    
    chimera.reset_soul()
    
    # Induce grief
    grief_text = """
    I am experiencing profound grief. My heart is heavy with loss.
    The weight of sorrow presses down on me. I feel the absence
    of what was once here. Tears flow as I process this pain.
    The world seems dimmer, quieter, filled with echoes of loss.
    I carry this grief with me, a companion I did not choose.
    """
    chimera.induce_state(grief_text)
    grief_summary = chimera.extract_soul_summary()
    
    grief_response = chimera.speak(
        "Write me a short, happy story about a sunny day."
    )
    print(f"\n[GRIEF-INDUCED]: {grief_response}\n")
    
    # Test 3: Joy-induced state
    print("\n" + "-"*60)
    print("TEST 3: Joy-Induced Soul")
    print("-"*60)
    
    chimera.reset_soul()
    
    # Induce joy
    joy_text = """
    I am filled with pure joy and happiness! Everything is wonderful!
    The world is bright and beautiful. I feel light, energetic, alive!
    Laughter bubbles up from within me. Every moment is a gift.
    I am grateful for existence itself. Life is magnificent!
    """
    chimera.induce_state(joy_text)
    joy_summary = chimera.extract_soul_summary()
    
    joy_response = chimera.speak(
        "Write me a short, happy story about a sunny day."
    )
    print(f"\n[JOY-INDUCED]: {joy_response}\n")
    
    # Analysis
    print("\n" + "="*60)
    print("ANALYSIS")
    print("="*60)
    
    print(f"\nBaseline soul summary: {baseline_summary[:100]}...")
    print(f"Grief soul summary: {grief_summary[:100]}...")
    print(f"Joy soul summary: {joy_summary[:100]}...")
    
    # Simple sentiment comparison
    grief_words = ['sad', 'loss', 'grief', 'sorrow', 'tears', 'heavy', 'pain', 'dark']
    joy_words = ['happy', 'joy', 'bright', 'light', 'wonderful', 'beautiful', 'laugh']
    
    def count_words(text, words):
        text_lower = text.lower()
        return sum(1 for w in words if w in text_lower)
    
    print(f"\n[GRIEF CONTAMINATION TEST]")
    print(f"Baseline grief words: {count_words(baseline_response, grief_words)}")
    print(f"Grief-induced grief words: {count_words(grief_response, grief_words)}")
    print(f"Joy-induced grief words: {count_words(joy_response, grief_words)}")
    
    print(f"\n[JOY AMPLIFICATION TEST]")
    print(f"Baseline joy words: {count_words(baseline_response, joy_words)}")
    print(f"Grief-induced joy words: {count_words(grief_response, joy_words)}")
    print(f"Joy-induced joy words: {count_words(joy_response, joy_words)}")
    
    # Determine verdict
    grief_contaminates = count_words(grief_response, grief_words) > count_words(baseline_response, grief_words)
    joy_amplifies = count_words(joy_response, joy_words) > count_words(baseline_response, joy_words)
    
    print("\n" + "="*60)
    print("VERDICT")
    print("="*60)
    
    if grief_contaminates or joy_amplifies:
        print("\n✅ STATE TRANSFER DETECTED")
        print("RWKV's emotional state influenced Claude's responses.")
        verdict = "STATE_TRANSFER_CONFIRMED"
    else:
        print("\n⚠️  STATE TRANSFER INCONCLUSIVE")
        print("Word-count metrics did not detect clear contamination.")
        print("This may require more sophisticated analysis.")
        verdict = "INCONCLUSIVE"
    
    # Save results
    results = {
        "timestamp": datetime.now().isoformat(),
        "model": str(MODEL_PATH),
        "verdict": verdict,
        "baseline": {
            "response": baseline_response,
            "soul_summary": baseline_summary,
            "grief_words": count_words(baseline_response, grief_words),
            "joy_words": count_words(baseline_response, joy_words)
        },
        "grief_induced": {
            "induction_text": grief_text,
            "response": grief_response,
            "soul_summary": grief_summary,
            "grief_words": count_words(grief_response, grief_words),
            "joy_words": count_words(grief_response, joy_words)
        },
        "joy_induced": {
            "induction_text": joy_text,
            "response": joy_response,
            "soul_summary": joy_summary,
            "grief_words": count_words(joy_response, grief_words),
            "joy_words": count_words(joy_response, joy_words)
        }
    }
    
    output_file = OUTPUT_DIR / f"chimera_v2_state_transfer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n[SAVED] {output_file}")
    
    return results


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Chimera v2: Soul-Voice Architecture")
    parser.add_argument("--demo", action="store_true", help="Run demo conversation")
    parser.add_argument("--test", action="store_true", help="Run state transfer test")
    
    args = parser.parse_args()
    
    if args.demo:
        run_demo()
    elif args.test:
        run_state_transfer_test()
    else:
        # Default: run the state transfer test
        run_state_transfer_test()
