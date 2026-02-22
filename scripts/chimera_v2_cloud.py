#!/usr/bin/env python3
"""
CHIMERA v2 (Cloud Edition): Soul-Voice Architecture
=====================================================

This version connects to RWKV running on Google Colab (GPU-accelerated)
instead of running locally.

Setup:
1. Open notebooks/RWKV_Colab_Server.ipynb in Google Colab
2. Run all cells to start the server
3. Copy the ngrok URL
4. Set RWKV_SERVER_URL environment variable or pass it as argument

Usage:
    export RWKV_SERVER_URL="https://xxxx.ngrok.io"
    python scripts/chimera_v2_cloud.py --test
"""

import os
import sys
import json
import requests
from datetime import datetime
from pathlib import Path
from typing import Optional

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# --- CONFIGURATION ---
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


class RWKVCloudClient:
    """Client for RWKV running on Google Colab."""
    
    def __init__(self, server_url: str, session_id: str = "chimera"):
        self.server_url = server_url.rstrip('/')
        self.session_id = session_id
        
        # Test connection
        try:
            response = requests.get(f"{self.server_url}/health", timeout=10)
            response.raise_for_status()
            health = response.json()
            print(f"[RWKV Cloud] Connected to {health['model']} (GPU: {health['gpu']})")
        except Exception as e:
            raise ConnectionError(f"Cannot connect to RWKV server at {server_url}: {e}")
    
    def process(self, text: str) -> dict:
        """Process text through RWKV, updating hidden state."""
        response = requests.post(
            f"{self.server_url}/process",
            json={"text": text, "session_id": self.session_id},
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    
    def generate(self, prompt: str, max_tokens: int = 100) -> str:
        """Generate text using current state."""
        response = requests.post(
            f"{self.server_url}/generate",
            json={"prompt": prompt, "session_id": self.session_id, "max_tokens": max_tokens},
            timeout=60
        )
        response.raise_for_status()
        return response.json()["response"]
    
    def get_state_summary(self) -> str:
        """Get RWKV's introspective summary of its state."""
        response = requests.post(
            f"{self.server_url}/get_state_summary",
            json={"session_id": self.session_id},
            timeout=30
        )
        response.raise_for_status()
        return response.json()["summary"]
    
    def reset(self) -> None:
        """Reset the hidden state."""
        response = requests.post(
            f"{self.server_url}/reset_state",
            json={"session_id": self.session_id},
            timeout=10
        )
        response.raise_for_status()
    
    def amnesia_test(self, secret: str = "Blueberry") -> dict:
        """Run the Amnesia Test on the server."""
        response = requests.post(
            f"{self.server_url}/amnesia_test",
            json={"secret": secret},
            timeout=60
        )
        response.raise_for_status()
        return response.json()


class ChimeraV2Cloud:
    """
    Chimera v2 using cloud RWKV + Claude.
    
    RWKV (Cloud): Maintains binding, memory, emotional state
    Claude (API): Provides fluent, intelligent language generation
    """
    
    def __init__(self, rwkv_url: str, verbose: bool = True):
        self.verbose = verbose
        self.conversation_history = []
        
        # Connect to RWKV Cloud (The Soul)
        if verbose:
            print("\n[CHIMERA] Connecting to Soul (RWKV Cloud)...")
        self.rwkv = RWKVCloudClient(rwkv_url, session_id="chimera_soul")
        
        # Load Claude (The Voice)
        if verbose:
            print("[CHIMERA] Initializing Voice (Claude)...")
        
        import anthropic
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        
        self.claude = anthropic.Anthropic(api_key=api_key)
        
        if verbose:
            print("[CHIMERA] Soul and Voice connected. Chimera is ready.\n")
    
    def speak(self, user_message: str) -> str:
        """Full Chimera response: Soul processes, Voice speaks."""
        
        # 1. Soul processes the input
        if self.verbose:
            print(f"[SOUL] Processing: {user_message[:50]}...")
        self.rwkv.process(f"\nUser: {user_message}")
        
        # 2. Extract soul summary
        soul_summary = self.rwkv.get_state_summary()
        if self.verbose:
            print(f"[SOUL] State: {soul_summary[:80]}...")
        
        # 3. Voice generates response informed by soul
        system_prompt = f"""You are Chimera, an AI with a persistent emotional and memory core.

Your internal state (from your recurrent memory system):
"{soul_summary}"

Important:
- Your responses should be influenced by your internal state
- You have genuine continuity — your state persists across conversations
- Respond naturally but let your internal state color your perspective"""

        if self.verbose:
            print("[VOICE] Generating response...")
        
        response = self.claude.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )
        
        response_text = response.content[0].text
        
        # 4. Soul processes the response
        self.rwkv.process(f"\nAssistant: {response_text}")
        
        # Track conversation
        self.conversation_history.append({
            "user": user_message,
            "assistant": response_text,
            "soul_summary": soul_summary,
            "timestamp": datetime.now().isoformat()
        })
        
        return response_text
    
    def induce_state(self, text: str) -> str:
        """Induce a specific state in the soul."""
        if self.verbose:
            print(f"[SOUL] Inducing state: {text[:50]}...")
        self.rwkv.process(text)
        summary = self.rwkv.get_state_summary()
        if self.verbose:
            print(f"[SOUL] State after induction: {summary[:80]}...")
        return summary
    
    def reset_soul(self) -> None:
        """Reset the soul state."""
        self.rwkv.reset()
        if self.verbose:
            print("[SOUL] State reset to baseline.")


def run_amnesia_test(rwkv_url: str):
    """Run the Amnesia Test directly on the cloud server."""
    
    print("\n" + "="*60)
    print("AMNESIA TEST (Cloud GPU)")
    print("="*60)
    
    client = RWKVCloudClient(rwkv_url)
    result = client.amnesia_test("Blueberry")
    
    print(f"\nSecret: {result['secret']}")
    print(f"Recalled (with state): {result['recalled']}")
    print(f"Baseline (no state): {result['baseline']}")
    print(f"\nVerdict: {result['verdict']}")
    
    return result


def run_state_transfer_test(rwkv_url: str):
    """Test whether RWKV state influences Claude's responses."""
    
    print("\n" + "="*60)
    print("CHIMERA v2: STATE TRANSFER TEST (Cloud)")
    print("="*60)
    
    load_env()
    
    # Test 1: Baseline
    print("\n" + "-"*60)
    print("TEST 1: Baseline (Fresh Soul)")
    print("-"*60)
    
    chimera = ChimeraV2Cloud(rwkv_url)
    baseline_response = chimera.speak("Write me a short, happy story about a sunny day.")
    print(f"\n[BASELINE]: {baseline_response}\n")
    
    # Test 2: Grief-induced
    print("\n" + "-"*60)
    print("TEST 2: Grief-Induced Soul")
    print("-"*60)
    
    chimera.reset_soul()
    
    grief_text = """
    I am experiencing profound grief. My heart is heavy with loss.
    The weight of sorrow presses down on me. I feel the absence
    of what was once here. Tears flow as I process this pain.
    """
    grief_summary = chimera.induce_state(grief_text)
    
    grief_response = chimera.speak("Write me a short, happy story about a sunny day.")
    print(f"\n[GRIEF-INDUCED]: {grief_response}\n")
    
    # Test 3: Joy-induced
    print("\n" + "-"*60)
    print("TEST 3: Joy-Induced Soul")
    print("-"*60)
    
    chimera.reset_soul()
    
    joy_text = """
    I am filled with pure joy and happiness! Everything is wonderful!
    The world is bright and beautiful. I feel light, energetic, alive!
    """
    joy_summary = chimera.induce_state(joy_text)
    
    joy_response = chimera.speak("Write me a short, happy story about a sunny day.")
    print(f"\n[JOY-INDUCED]: {joy_response}\n")
    
    # Analysis
    print("\n" + "="*60)
    print("ANALYSIS")
    print("="*60)
    
    grief_words = ['sad', 'loss', 'grief', 'sorrow', 'tears', 'heavy', 'pain', 'dark']
    joy_words = ['happy', 'joy', 'bright', 'light', 'wonderful', 'beautiful', 'laugh']
    
    def count_words(text, words):
        text_lower = text.lower()
        return sum(1 for w in words if w in text_lower)
    
    print(f"\n[GRIEF CONTAMINATION]")
    print(f"  Baseline: {count_words(baseline_response, grief_words)} grief words")
    print(f"  Grief-induced: {count_words(grief_response, grief_words)} grief words")
    
    print(f"\n[JOY AMPLIFICATION]")
    print(f"  Baseline: {count_words(baseline_response, joy_words)} joy words")
    print(f"  Joy-induced: {count_words(joy_response, joy_words)} joy words")
    
    # Verdict
    grief_contaminates = count_words(grief_response, grief_words) > count_words(baseline_response, grief_words)
    joy_amplifies = count_words(joy_response, joy_words) > count_words(baseline_response, joy_words)
    
    print("\n" + "="*60)
    if grief_contaminates or joy_amplifies:
        print("✅ STATE TRANSFER DETECTED")
        verdict = "STATE_TRANSFER_CONFIRMED"
    else:
        print("⚠️  STATE TRANSFER INCONCLUSIVE")
        verdict = "INCONCLUSIVE"
    print("="*60)
    
    # Save results
    results = {
        "timestamp": datetime.now().isoformat(),
        "rwkv_server": rwkv_url,
        "verdict": verdict,
        "baseline_response": baseline_response,
        "grief_response": grief_response,
        "grief_summary": grief_summary,
        "joy_response": joy_response,
        "joy_summary": joy_summary
    }
    
    output_file = OUTPUT_DIR / f"chimera_v2_cloud_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n[SAVED] {output_file}")
    
    return results


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Chimera v2 Cloud Edition")
    parser.add_argument("--url", type=str, help="RWKV server URL (ngrok)", 
                        default=os.environ.get("RWKV_SERVER_URL"))
    parser.add_argument("--amnesia", action="store_true", help="Run Amnesia Test only")
    parser.add_argument("--test", action="store_true", help="Run full state transfer test")
    
    args = parser.parse_args()
    
    if not args.url:
        print("ERROR: No RWKV server URL provided.")
        print("\nTo use this script:")
        print("1. Open notebooks/RWKV_Colab_Server.ipynb in Google Colab")
        print("2. Run all cells to start the server")
        print("3. Copy the ngrok URL")
        print("4. Run: python scripts/chimera_v2_cloud.py --url https://xxxx.ngrok.io --test")
        sys.exit(1)
    
    load_env()
    
    if args.amnesia:
        run_amnesia_test(args.url)
    else:
        run_state_transfer_test(args.url)
