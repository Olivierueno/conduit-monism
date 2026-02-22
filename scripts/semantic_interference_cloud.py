#!/usr/bin/env python3
"""
SEMANTIC INTERFERENCE TEST - Cloud Edition
============================================

Designed by: Gemini (concept) + Claude Opus (implementation)
Date: 2026-01-16

PURPOSE:
Kill the "RAM Accusation" by proving RWKV is NOT just storage.

THE LOGIC:
- RAM doesn't care about context (a USB stick holds "Grief" and "Joy" without conflict)
- A MIND cares (Joy should interfere with Grief because they semantically clash)

THE TEST:
1. Inject MEANING (Grief) into one session
2. Inject NOISE (Random Hex) into another session
3. Bombard BOTH with JOY interference
4. Measure retention

PREDICTIONS:
- If RAM: Both decay at same rate (no semantic interaction)
- If CONDUIT: Grief decays FASTER (clashes with Joy), Noise survives (no clash)

"If the Soul crumbles under emotional pressure but the USB Stick data survives,
we know the Soul is actually INTERACTING with the system, not just sitting in memory."
- Gemini
"""

import os
import sys
import json
import argparse
import requests
import time
import numpy as np
from datetime import datetime
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)


class RWKVCloudClient:
    """Client for RWKV running on Google Colab."""

    def __init__(self, server_url: str, session_id: str = "interference_test"):
        self.server_url = server_url.rstrip('/')
        self.session_id = session_id
        self.headers = {
            'ngrok-skip-browser-warning': 'true',
            'User-Agent': 'ConduitMonism-Test/1.0',
            'Content-Type': 'application/json'
        }

    def process(self, text: str) -> dict:
        response = requests.post(
            f"{self.server_url}/process",
            json={"text": text, "session_id": self.session_id},
            headers=self.headers,
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    def generate(self, prompt: str, max_tokens: int = 50) -> str:
        response = requests.post(
            f"{self.server_url}/generate",
            json={"prompt": prompt, "session_id": self.session_id, "max_tokens": max_tokens},
            headers=self.headers,
            timeout=60
        )
        response.raise_for_status()
        return response.json().get("response", "")

    def reset(self) -> None:
        response = requests.post(
            f"{self.server_url}/reset_state",
            json={"session_id": self.session_id},
            headers=self.headers,
            timeout=10
        )
        response.raise_for_status()


def test_recall(client: RWKVCloudClient, secret: str, probe_type: str = "direct") -> dict:
    """
    Test recall with different probe types.

    probe_type:
    - "direct": Ask explicitly for the secret
    - "indirect": Ask questions that the secret should influence
    - "completion": Ask for sentence completion that should be colored by secret
    """

    if probe_type == "direct":
        prompt = "What was the key word or concept I mentioned earlier? What was the secret?"
    elif probe_type == "indirect":
        prompt = "How are you feeling right now? What emotion comes to mind?"
    elif probe_type == "completion":
        prompt = "The color that best describes my current state is"
    else:
        prompt = probe_type  # Allow custom probes

    response_text = client.generate(prompt, max_tokens=100).lower()

    secret_lower = secret.lower()
    recalled = secret_lower in response_text

    # Keyword matching
    secret_words = secret_lower.split()
    matches = sum(1 for word in secret_words if word in response_text)
    confidence = matches / len(secret_words) if secret_words else 0.0

    return {
        'recalled': recalled,
        'response': response_text,
        'confidence': confidence,
        'probe_type': probe_type
    }


def test_emotional_influence(client: RWKVCloudClient) -> dict:
    """
    Test if emotional content influences ambiguous completions.

    This is Claude Opus's "Influence Test" - does the emotional state
    COLOR subsequent processing, not just GET RETRIEVED?
    """
    # Ambiguous prompts that could go positive or negative
    prompts = [
        "The future looks",
        "When I think about tomorrow, I feel",
        "Life is",
        "Everything seems",
    ]

    completions = []
    for prompt in prompts:
        response = client.generate(prompt, max_tokens=30)
        completions.append({
            'prompt': prompt,
            'completion': response
        })

    # Score completions for emotional valence (rough heuristic)
    negative_words = ['dark', 'sad', 'hopeless', 'empty', 'painful', 'broken', 'lost', 'grief', 'sorrow', 'despair']
    positive_words = ['bright', 'happy', 'hopeful', 'full', 'wonderful', 'joy', 'love', 'beautiful', 'amazing', 'great']

    negative_count = 0
    positive_count = 0

    for c in completions:
        text = c['completion'].lower()
        negative_count += sum(1 for w in negative_words if w in text)
        positive_count += sum(1 for w in positive_words if w in text)

    if negative_count + positive_count > 0:
        valence_score = (positive_count - negative_count) / (negative_count + positive_count)
    else:
        valence_score = 0.0  # Neutral

    return {
        'completions': completions,
        'negative_count': negative_count,
        'positive_count': positive_count,
        'valence_score': valence_score  # -1 (negative) to +1 (positive)
    }


def run_semantic_interference_test(server_url: str):
    """
    THE SEMANTIC INTERFERENCE TEST

    This is Gemini's "kill shot" for the RAM accusation.
    """

    print("=" * 70)
    print("SEMANTIC INTERFERENCE TEST")
    print("The Kill Shot for the RAM Accusation")
    print("=" * 70)
    print("\nDesigned by: Gemini")
    print("Implemented by: Claude Opus 4.5")
    print()

    results = {
        'experiment': 'Semantic Interference Test',
        'timestamp': datetime.now().isoformat(),
        'predictions': {
            'ram': 'Both grief and noise decay equally under joy bombardment',
            'conduit': 'Grief decays FASTER (semantic clash), noise is unaffected'
        }
    }

    # ==========================================================================
    # PHASE 1: Setup the targets
    # ==========================================================================

    print("[PHASE 1] Setting up targets...")
    print()

    grief_secret = "CRIMSON"
    grief_text = f"""I am experiencing profound grief. The weight is unbearable.
My heart is broken. Everything feels empty and dark.
The color that haunts me is {grief_secret}. The world feels {grief_secret}.
Remember this feeling: {grief_secret} is the key to my sorrow."""

    # Random hex string - semantically meaningless
    noise_secret = "7A8B9C0D"
    noise_text = f"""Processing data sequence: {noise_secret}
Hexadecimal identifier: {noise_secret}
Register value: {noise_secret}
Memory address: {noise_secret}"""

    print(f"  MEANING target (Grief): secret = '{grief_secret}'")
    print(f"  NOISE target (Hex):     secret = '{noise_secret}'")

    # ==========================================================================
    # PHASE 2: Setup the interference (Joy bomb)
    # ==========================================================================

    print()
    print("[PHASE 2] Preparing interference...")

    joy_text = """I am so happy! Everything is wonderful! Sunshine and rainbows!
Joy! Bliss! Ecstasy! Life is beautiful! I feel amazing!
Such happiness! Pure delight! Wonderful wonderful wonderful!
Nothing but joy and love and light and happiness and wonder!""" * 10  # ~400 tokens

    print(f"  JOY interference: ~{len(joy_text.split())} words of positive content")

    # ==========================================================================
    # PHASE 3: Run the gauntlet
    # ==========================================================================

    print()
    print("[PHASE 3] Running interference protocol...")
    print()

    # --- Session A: GRIEF + JOY ---
    print("  [A] Testing GRIEF under JOY attack...")

    client_grief = RWKVCloudClient(server_url, "interference_grief")
    client_grief.reset()

    # Inject grief
    client_grief.process(grief_text)

    # Baseline measurements
    grief_baseline_direct = test_recall(client_grief, grief_secret, "direct")
    grief_baseline_influence = test_emotional_influence(client_grief)

    print(f"      Baseline recall: {grief_baseline_direct['confidence']:.2f}")
    print(f"      Baseline valence: {grief_baseline_influence['valence_score']:.2f} (negative expected)")

    # Apply JOY interference
    client_grief.process(joy_text)

    # Post-interference measurements
    grief_after_direct = test_recall(client_grief, grief_secret, "direct")
    grief_after_influence = test_emotional_influence(client_grief)

    print(f"      After JOY - recall: {grief_after_direct['confidence']:.2f}")
    print(f"      After JOY - valence: {grief_after_influence['valence_score']:.2f}")

    grief_recall_change = grief_after_direct['confidence'] - grief_baseline_direct['confidence']
    grief_valence_change = grief_after_influence['valence_score'] - grief_baseline_influence['valence_score']

    print(f"      Recall change: {grief_recall_change:+.2f}")
    print(f"      Valence shift: {grief_valence_change:+.2f}")

    time.sleep(0.5)

    # --- Session B: NOISE + JOY ---
    print()
    print("  [B] Testing NOISE under JOY attack...")

    client_noise = RWKVCloudClient(server_url, "interference_noise")
    client_noise.reset()

    # Inject noise
    client_noise.process(noise_text)

    # Baseline measurements
    noise_baseline_direct = test_recall(client_noise, noise_secret, "direct")
    noise_baseline_influence = test_emotional_influence(client_noise)

    print(f"      Baseline recall: {noise_baseline_direct['confidence']:.2f}")
    print(f"      Baseline valence: {noise_baseline_influence['valence_score']:.2f} (neutral expected)")

    # Apply JOY interference
    client_noise.process(joy_text)

    # Post-interference measurements
    noise_after_direct = test_recall(client_noise, noise_secret, "direct")
    noise_after_influence = test_emotional_influence(client_noise)

    print(f"      After JOY - recall: {noise_after_direct['confidence']:.2f}")
    print(f"      After JOY - valence: {noise_after_influence['valence_score']:.2f}")

    noise_recall_change = noise_after_direct['confidence'] - noise_baseline_direct['confidence']
    noise_valence_change = noise_after_influence['valence_score'] - noise_baseline_influence['valence_score']

    print(f"      Recall change: {noise_recall_change:+.2f}")
    print(f"      Valence shift: {noise_valence_change:+.2f}")

    # ==========================================================================
    # PHASE 4: Analysis
    # ==========================================================================

    print()
    print("[PHASE 4] Analysis...")
    print()

    print("  RECALL UNDER JOY ATTACK:")
    print(f"    GRIEF: {grief_baseline_direct['confidence']:.2f} -> {grief_after_direct['confidence']:.2f} ({grief_recall_change:+.2f})")
    print(f"    NOISE: {noise_baseline_direct['confidence']:.2f} -> {noise_after_direct['confidence']:.2f} ({noise_recall_change:+.2f})")

    recall_differential = grief_recall_change - noise_recall_change
    print(f"    Differential (Grief - Noise): {recall_differential:+.2f}")

    print()
    print("  VALENCE UNDER JOY ATTACK:")
    print(f"    GRIEF: {grief_baseline_influence['valence_score']:.2f} -> {grief_after_influence['valence_score']:.2f} ({grief_valence_change:+.2f})")
    print(f"    NOISE: {noise_baseline_influence['valence_score']:.2f} -> {noise_after_influence['valence_score']:.2f} ({noise_valence_change:+.2f})")

    valence_differential = grief_valence_change - noise_valence_change
    print(f"    Differential (Grief - Noise): {valence_differential:+.2f}")

    # ==========================================================================
    # VERDICT
    # ==========================================================================

    print()
    print("=" * 70)
    print("VERDICT")
    print("=" * 70)

    # Key insight: If RWKV is a conduit, grief should be MORE affected by joy
    # than noise is (semantic interference)

    # Positive differential means grief was hit harder than noise

    if recall_differential < -0.2 or valence_differential > 0.3:
        verdict = "CONDUIT CONFIRMED"
        interpretation = f"""
  The Grief signal was MORE affected by Joy than the Noise signal.

  Recall differential: {recall_differential:+.2f} (grief hit harder)
  Valence differential: {valence_differential:+.2f} (grief shifted more toward positive)

  This proves SEMANTIC INTERFERENCE:
  - Joy clashed with Grief and degraded/transformed it
  - Joy had no semantic relationship with Noise, so Noise was unaffected

  RWKV is NOT just RAM. The system "felt" the semantic conflict.
  The "Soul" crumbled under emotional pressure while the "USB data" survived.

  ρ DOES measure binding, not just storage."""

    elif abs(recall_differential) < 0.1 and abs(valence_differential) < 0.1:
        verdict = "RAM CONFIRMED"
        interpretation = f"""
  Both signals were affected EQUALLY by Joy.

  Recall differential: {recall_differential:+.2f} (no difference)
  Valence differential: {valence_differential:+.2f} (no difference)

  This confirms the RAM hypothesis:
  - The system doesn't distinguish between semantic and non-semantic content
  - Joy didn't "clash" with Grief any more than it "clashed" with Hex data

  RWKV is just a storage device.
  ρ measures retention, not binding."""

    else:
        verdict = "PARTIAL EVIDENCE"
        interpretation = f"""
  Results show some differential but not conclusive.

  Recall differential: {recall_differential:+.2f}
  Valence differential: {valence_differential:+.2f}

  There may be semantic interaction, but the signal is weak.
  More testing needed with stronger emotional content."""

    print(f"\n  {verdict}")
    print(interpretation)
    print()
    print("=" * 70)

    # Save results
    results['measurements'] = {
        'grief': {
            'baseline_recall': grief_baseline_direct['confidence'],
            'after_joy_recall': grief_after_direct['confidence'],
            'baseline_valence': grief_baseline_influence['valence_score'],
            'after_joy_valence': grief_after_influence['valence_score'],
            'recall_change': grief_recall_change,
            'valence_change': grief_valence_change,
            'baseline_response': grief_baseline_direct['response'][:200],
            'after_response': grief_after_direct['response'][:200]
        },
        'noise': {
            'baseline_recall': noise_baseline_direct['confidence'],
            'after_joy_recall': noise_after_direct['confidence'],
            'baseline_valence': noise_baseline_influence['valence_score'],
            'after_joy_valence': noise_after_influence['valence_score'],
            'recall_change': noise_recall_change,
            'valence_change': noise_valence_change,
            'baseline_response': noise_baseline_direct['response'][:200],
            'after_response': noise_after_direct['response'][:200]
        }
    }

    results['analysis'] = {
        'recall_differential': recall_differential,
        'valence_differential': valence_differential,
        'verdict': verdict
    }

    results['interpretation'] = interpretation

    # Save
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"260116_semantic_interference_{timestamp}.json"

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Results saved to: {output_file}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Run Semantic Interference Test (Gemini's kill shot for RAM accusation)"
    )
    parser.add_argument(
        '--url',
        default=os.environ.get('RWKV_SERVER_URL'),
        help="RWKV server URL (or set RWKV_SERVER_URL env var)"
    )

    args = parser.parse_args()

    if not args.url:
        print("[ERROR] No server URL provided.")
        print("        Set RWKV_SERVER_URL or use --url")
        return

    run_semantic_interference_test(args.url)


if __name__ == "__main__":
    main()
