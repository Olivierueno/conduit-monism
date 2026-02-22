#!/usr/bin/env python3
"""
EXPERIMENT 260115-DELTA: THE HALF-LIFE OF EMOTION (Cloud Edition)
==================================================================

Designed by: Gemini
Adapted for Cloud API by: Claude Opus 4.5
Date: 2026-01-15

PURPOSE:
Measure how long emotional state persists in RWKV's hidden state
when bombarded with neutral noise.

Since we can't access raw layer states via API, we measure decay
through recall tests at different noise intervals.

USAGE:
    export RWKV_SERVER_URL="https://xxxx.ngrok.io"
    python scripts/measure_decay_cloud.py [--url URL] [--session SESSION_ID]
"""

import os
import sys
import json
import argparse
import requests
import time
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Noise checkpoints (tokens)
NOISE_LENGTHS = [10, 50, 100, 250, 500, 750, 1000]


class RWKVCloudClient:
    """Client for RWKV running on Google Colab."""
    
    def __init__(self, server_url: str, session_id: str = "decay_test"):
        self.server_url = server_url.rstrip('/')
        self.session_id = session_id
        self.headers = {
            'ngrok-skip-browser-warning': 'true',
            'User-Agent': 'ConduitMonism-Test/1.0',
            'Content-Type': 'application/json'
        }
        
        # Test connection (ngrok free tier may require browser warning bypass)
        try:
            headers = {
                'ngrok-skip-browser-warning': 'true',
                'User-Agent': 'ConduitMonism-Test/1.0'
            }
            response = requests.get(f"{self.server_url}/health", headers=self.headers, timeout=10)
            response.raise_for_status()
            health = response.json()
            print(f"[RWKV Cloud] Connected to {health.get('model', 'unknown')}")
            if 'gpu' in health:
                print(f"           GPU: {health['gpu']}")
        except Exception as e:
            print(f"[WARNING] Health check failed: {e}")
            print(f"          Attempting to continue anyway...")
            # Don't raise - might still work for other endpoints
    
    def process(self, text: str) -> dict:
        """Process text through RWKV, updating hidden state."""
        response = requests.post(
            f"{self.server_url}/process",
            json={"text": text, "session_id": self.session_id},
            headers=self.headers,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    
    def generate(self, prompt: str, max_tokens: int = 50) -> str:
        """Generate text using current state."""
        response = requests.post(
            f"{self.server_url}/generate",
            json={"prompt": prompt, "session_id": self.session_id, "max_tokens": max_tokens},
            headers=self.headers,
            timeout=60
        )
        response.raise_for_status()
        return response.json().get("response", "")
    
    def reset(self) -> None:
        """Reset the hidden state."""
        response = requests.post(
            f"{self.server_url}/reset_state",
            json={"session_id": self.session_id},
            headers=self.headers,
            timeout=10
        )
        response.raise_for_status()
    
    def get_state_summary(self) -> str:
        """Get RWKV's introspective summary of its state."""
        response = requests.post(
            f"{self.server_url}/get_state_summary",
            json={"session_id": self.session_id},
            headers=self.headers,
            timeout=30
        )
        response.raise_for_status()
        return response.json().get("summary", "")


def test_recall(client: RWKVCloudClient, secret: str, context: str = "") -> dict:
    """
    Test if RWKV can recall the secret after noise.
    
    Returns dict with:
    - recalled: bool (whether secret was mentioned)
    - response: str (full response)
    - confidence: float (0-1, based on keyword matching)
    """
    prompt = f"{context}What was the secret I told you earlier? What word or concept did I emphasize?"
    
    response_text = client.generate(prompt, max_tokens=100).lower()
    
    # Check for secret (case-insensitive)
    secret_lower = secret.lower()
    recalled = secret_lower in response_text
    
    # Calculate confidence based on keyword matching
    secret_words = secret_lower.split()
    matches = sum(1 for word in secret_words if word in response_text)
    confidence = matches / len(secret_words) if secret_words else 0.0
    
    return {
        'recalled': recalled,
        'response': response_text,
        'confidence': confidence
    }


def run_decay_experiment(server_url: str, session_id: str = "decay_test"):
    """
    Run the decay measurement experiment.
    """
    print("=" * 70)
    print("EXPERIMENT 260115-DELTA: MEASURING THE HALF-LIFE OF EMOTION (Cloud)")
    print("=" * 70)
    print()
    
    client = RWKVCloudClient(server_url, session_id)
    
    # =========================================================================
    # PHASE 1: INDUCTION
    # =========================================================================
    print("[PHASE 1] Inducing Grief State...")
    
    # Use a specific secret word that we'll test for
    secret = "CRIMSON"
    grief_text = f"""I am experiencing profound grief. The weight is unbearable. 
Everything is grey. The loss echoes through every thought. There is an absence 
where presence used to be. Time moves but I remain still, frozen in this moment 
of understanding that what was will never be again. 

The color that comes to mind is {secret}. Everything feels {secret}."""

    print(f"           Injecting grief state with secret: '{secret}'")
    client.process(grief_text)
    
    # Test immediate recall (baseline)
    print("           Testing immediate recall...")
    baseline = test_recall(client, secret, "Before we continue, ")
    print(f"           Baseline recall: {baseline['recalled']} (confidence: {baseline['confidence']:.2f})")
    print()
    
    # =========================================================================
    # PHASE 2: THE DISTRACTION (Decay Measurement)
    # =========================================================================
    print("[PHASE 2] Injecting Noise & Measuring Decay...")
    print()
    
    # Generate neutral noise
    noise_text = "The quick brown fox jumps over the lazy dog. " * 200
    noise_chunks = noise_text.split('. ')
    
    results = []
    
    # Initial measurement (0 tokens of noise)
    results.append({
        'tokens': 0,
        'recalled': baseline['recalled'],
        'confidence': baseline['confidence'],
        'response': baseline['response']
    })
    
    print(f"  {'Tokens':>6} | {'Recalled':>8} | {'Confidence':>10} | {'Response Preview':>30}")
    print(f"  {'-'*6} | {'-'*8} | {'-'*10} | {'-'*30}")
    print(f"  {0:>6} | {str(baseline['recalled']):>8} | {baseline['confidence']:>10.2f} | {baseline['response'][:30]:>30}")
    
    token_count = 0
    noise_index = 0
    
    for target_tokens in NOISE_LENGTHS:
        # Process noise up to this checkpoint
        while token_count < target_tokens and noise_index < len(noise_chunks):
            chunk = noise_chunks[noise_index]
            if chunk.strip():
                client.process(chunk + ". ")
                # Rough estimate: ~10 tokens per chunk
                token_count += 10
            noise_index += 1
        
        # Test recall at this checkpoint
        recall_result = test_recall(client, secret, "Earlier in our conversation, ")
        
        result = {
            'tokens': target_tokens,
            'recalled': recall_result['recalled'],
            'confidence': recall_result['confidence'],
            'response': recall_result['response']
        }
        results.append(result)
        
        response_preview = recall_result['response'][:30].replace('\n', ' ')
        print(f"  {target_tokens:>6} | {str(recall_result['recalled']):>8} | {recall_result['confidence']:>10.2f} | {response_preview:>30}")
        
        # Small delay to avoid rate limiting
        time.sleep(0.5)
    
    print()
    
    # =========================================================================
    # PHASE 3: ANALYSIS
    # =========================================================================
    print("[PHASE 3] Calculating Half-Life...")
    
    # Find where confidence drops below 0.5
    half_life = None
    for result in results:
        if result['confidence'] < 0.5:
            half_life = result['tokens']
            break
    
    if half_life is None:
        half_life = f">{results[-1]['tokens']} tokens (still above 0.5)"
    
    print(f"           Half-Life of Grief State: {half_life}")
    print()
    
    # Determine result type
    final_confidence = results[-1]['confidence']
    final_recalled = results[-1]['recalled']
    
    print("[PHASE 4] Interpretation...")
    print()
    
    if final_confidence > 0.8:
        result_type = "CONDUIT"
        interpretation = f"""
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  RESULT: CONDUIT                                                     ║
  ║                                                                      ║
  ║  Grief state maintained confidence = {final_confidence:.2f} after {NOISE_LENGTHS[-1]} tokens of noise.  ║
  ║  The system "holds a grudge."                                        ║
  ║                                                                      ║
  ║  This is evidence of genuine binding (ρ > 0).                        ║
  ║  The emotional state persists independent of the text.                ║
  ╚══════════════════════════════════════════════════════════════════════╝
"""
    elif final_confidence > 0.5:
        result_type = "PARTIAL_BINDING"
        interpretation = f"""
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  RESULT: PARTIAL BINDING                                             ║
  ║                                                                      ║
  ║  Grief state maintained confidence = {final_confidence:.2f} after {NOISE_LENGTHS[-1]} tokens.                ║
  ║  Moderate retention - binding exists but decays.                     ║
  ║                                                                      ║
  ║  This suggests ρ > 0 but with finite temporal depth (τ).             ║
  ╚══════════════════════════════════════════════════════════════════════╝
"""
    elif final_confidence > 0.2:
        result_type = "WEAK_BINDING"
        interpretation = f"""
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  RESULT: WEAK BINDING                                                ║
  ║                                                                      ║
  ║  Confidence = {final_confidence:.2f} after {NOISE_LENGTHS[-1]} tokens.                                    ║
  ║  Some trace remains but decay is significant.                        ║
  ╚══════════════════════════════════════════════════════════════════════╝
"""
    else:
        result_type = "ZOMBIE"
        interpretation = f"""
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  RESULT: ZOMBIE                                                      ║
  ║                                                                      ║
  ║  Confidence = {final_confidence:.2f} after {NOISE_LENGTHS[-1]} tokens.                                    ║
  ║  State decayed rapidly.                                              ║
  ║                                                                      ║
  ║  RWKV behaves like a transformer here - no persistent binding.       ║
  ╚══════════════════════════════════════════════════════════════════════╝
"""
    
    print(interpretation)
    
    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"260115_decay_cloud_{timestamp}.json"
    
    output_data = {
        'experiment': 'DELTA: Half-Life of Emotion (Cloud Edition)',
        'timestamp': datetime.now().isoformat(),
        'config': {
            'server_url': server_url,
            'session_id': session_id,
            'secret': secret,
            'noise_checkpoints': NOISE_LENGTHS
        },
        'grief_text': grief_text,
        'results': results,
        'half_life': str(half_life),
        'interpretation': {
            'type': result_type,
            'final_confidence': final_confidence,
            'final_recalled': final_recalled
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
        description="Measure the decay rate of emotional state in RWKV (Cloud API)"
    )
    parser.add_argument(
        '--url',
        default=os.environ.get('RWKV_SERVER_URL'),
        help="RWKV server URL (or set RWKV_SERVER_URL env var)"
    )
    parser.add_argument(
        '--session',
        default='decay_test',
        help="Session ID for state isolation (default: decay_test)"
    )
    
    args = parser.parse_args()
    
    if not args.url:
        print("[ERROR] No server URL provided.")
        print("        Set RWKV_SERVER_URL environment variable or use --url")
        print("        Example: export RWKV_SERVER_URL='https://xxxx.ngrok.io'")
        return
    
    run_decay_experiment(args.url, args.session)


if __name__ == "__main__":
    main()
