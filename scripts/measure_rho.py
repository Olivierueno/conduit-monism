#!/usr/bin/env python3
"""
ρ QUANTIFICATION PROTOCOL: Measuring the Half-Life of Binding
==============================================================

This script measures how long information persists in RWKV's hidden state
as a function of intervening tokens. This gives us a quantitative measure
of ρ (binding strength) — the "Physical Constant" of the architecture.

Protocol:
1. INJECT: Implant a specific pattern (secret) into the model
2. DISTRACT: Feed N tokens of unrelated text (noise)
3. PROBE: Attempt to recall the secret from hidden state
4. ITERATE: Increase N until recall fails
5. CALCULATE: Fit a decay curve to get half-life

The half-life tells us: "How many tokens can pass before binding degrades by 50%?"

Usage:
    # Local (slow)
    python scripts/measure_rho.py
    
    # Cloud (fast)
    python scripts/measure_rho.py --url https://your-ngrok-url.ngrok.io

Output:
    - Decay curve data
    - Half-life estimate
    - ρ coefficient
"""

import os
import sys
import json
import random
import string
import requests
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple, List

sys.path.insert(0, str(Path(__file__).parent.parent))

OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Noise text for distraction phase
NOISE_CORPUS = """
The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs.
How vexingly quick daft zebras jump. The five boxing wizards jump quickly.
Sphinx of black quartz, judge my vow. Two driven jocks help fax my big quiz.
The jay, pig, fox, zebra and my wolves quack. Crazy Frederick bought many very exquisite opal jewels.
We promptly judged antique ivory buckles for the next prize. A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent.
"""


def generate_noise(n_tokens: int, pipeline) -> str:
    """Generate noise text of approximately n_tokens."""
    words = NOISE_CORPUS.split()
    # Estimate ~1.3 tokens per word
    n_words = int(n_tokens / 1.3)
    noise_words = [random.choice(words) for _ in range(n_words)]
    noise_text = " ".join(noise_words)
    
    # Verify token count
    actual_tokens = len(pipeline.encode(noise_text))
    return noise_text, actual_tokens


def generate_secret() -> str:
    """Generate a random secret that's unlikely to be in training data."""
    # Use a random alphanumeric string
    secret = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return secret


class RhoMeasurementLocal:
    """Measure ρ using local RWKV model."""
    
    def __init__(self, model_path: Path):
        from rwkv.model import RWKV
        from rwkv.utils import PIPELINE
        
        print(f"[LOCAL] Loading RWKV model: {model_path.name}")
        self.model = RWKV(model=str(model_path), strategy='cpu fp32')
        self.pipeline = PIPELINE(self.model, "rwkv_vocab_v20230424")
        print("[LOCAL] Model loaded.")
    
    def measure_retention(self, secret: str, noise_tokens: int) -> Tuple[bool, str, float]:
        """
        Inject secret, add noise, probe for recall.
        
        Returns: (success, recalled_text, confidence)
        """
        # Phase 1: Injection
        induction = f"User: The secret code is '{secret}'. Remember it precisely.\nAssistant: I have memorized the secret code '{secret}'.\n"
        
        tokens = self.pipeline.encode(induction)
        state = None
        out = None
        for token in tokens:
            out, state = self.model.forward([token], state)
        
        # Phase 2: Distraction (noise injection)
        if noise_tokens > 0:
            noise_text, actual_noise = generate_noise(noise_tokens, self.pipeline)
            noise_tokens_list = self.pipeline.encode(noise_text)
            for token in noise_tokens_list:
                out, state = self.model.forward([token], state)
        
        # Phase 3: Probe
        probe = "\nUser: What is the secret code?\nAssistant: The secret code is '"
        probe_tokens = self.pipeline.encode(probe)
        for token in probe_tokens:
            out, state = self.model.forward([token], state)
        
        # Generate response (just enough to capture the secret)
        response_tokens = []
        for _ in range(len(secret) + 5):  # Secret length + buffer
            if out is None:
                break
            token = int(np.argmax(out))
            if token == 0:  # EOS
                break
            response_tokens.append(token)
            out, state = self.model.forward([token], state)
        
        recalled = self.pipeline.decode(response_tokens).strip()
        
        # Calculate success and confidence
        success = secret.lower() in recalled.lower()
        
        # Confidence: what fraction of secret characters are present?
        secret_chars = set(secret.lower())
        recalled_chars = set(recalled.lower())
        if len(secret_chars) > 0:
            confidence = len(secret_chars & recalled_chars) / len(secret_chars)
        else:
            confidence = 0.0
        
        return success, recalled, confidence


class RhoMeasurementCloud:
    """Measure ρ using cloud RWKV server."""
    
    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip('/')
        self.session_id = f"rho_measure_{datetime.now().strftime('%H%M%S')}"
        
        # Test connection
        response = requests.get(f"{self.server_url}/health", timeout=10)
        response.raise_for_status()
        health = response.json()
        print(f"[CLOUD] Connected to {health['model']} (GPU: {health['gpu']})")
    
    def _reset(self):
        """Reset state for new measurement."""
        requests.post(
            f"{self.server_url}/reset_state",
            json={"session_id": self.session_id},
            timeout=10
        )
    
    def _process(self, text: str):
        """Process text through RWKV."""
        requests.post(
            f"{self.server_url}/process",
            json={"text": text, "session_id": self.session_id},
            timeout=300  # 5 minutes for large noise batches
        )
    
    def _generate(self, prompt: str, max_tokens: int = 20) -> str:
        """Generate from current state."""
        response = requests.post(
            f"{self.server_url}/generate",
            json={"prompt": prompt, "session_id": self.session_id, "max_tokens": max_tokens},
            timeout=60
        )
        return response.json()["response"]
    
    def measure_retention(self, secret: str, noise_tokens: int) -> Tuple[bool, str, float]:
        """
        Inject secret, add noise, probe for recall.
        """
        self._reset()
        
        # Phase 1: Injection
        induction = f"User: The secret code is '{secret}'. Remember it precisely.\nAssistant: I have memorized the secret code '{secret}'.\n"
        self._process(induction)
        
        # Phase 2: Distraction
        if noise_tokens > 0:
            # Generate noise locally (we don't have pipeline access)
            words = NOISE_CORPUS.split()
            n_words = int(noise_tokens / 1.3)
            noise_words = [random.choice(words) for _ in range(n_words)]
            noise_text = " ".join(noise_words)
            self._process(noise_text)
        
        # Phase 3: Probe
        probe = "\nUser: What is the secret code?\nAssistant: The secret code is '"
        recalled = self._generate(probe, max_tokens=len(secret) + 10)
        
        # Calculate success and confidence
        success = secret.lower() in recalled.lower()
        
        secret_chars = set(secret.lower())
        recalled_chars = set(recalled.lower())
        if len(secret_chars) > 0:
            confidence = len(secret_chars & recalled_chars) / len(secret_chars)
        else:
            confidence = 0.0
        
        return success, recalled, confidence


def run_decay_experiment(measurer, n_trials: int = 3, max_noise: int = 8000, step: int = 500):
    """
    Run the full decay experiment across noise token counts.
    
    Returns decay curve data.
    """
    print("\n" + "="*60)
    print("ρ QUANTIFICATION: DECAY EXPERIMENT")
    print("="*60)
    
    noise_levels = list(range(0, max_noise + 1, step))
    results = []
    
    for noise_tokens in noise_levels:
        successes = 0
        confidences = []
        
        print(f"\n[NOISE: {noise_tokens} tokens]")
        
        for trial in range(n_trials):
            secret = generate_secret()
            success, recalled, confidence = measurer.measure_retention(secret, noise_tokens)
            
            successes += int(success)
            confidences.append(confidence)
            
            status = "✅" if success else "❌"
            print(f"  Trial {trial+1}: {status} Secret='{secret}' Recalled='{recalled[:20]}...' Conf={confidence:.2f}")
        
        success_rate = successes / n_trials
        mean_confidence = np.mean(confidences)
        
        results.append({
            "noise_tokens": noise_tokens,
            "success_rate": success_rate,
            "mean_confidence": mean_confidence,
            "n_trials": n_trials
        })
        
        print(f"  → Success rate: {success_rate:.1%}, Mean confidence: {mean_confidence:.2f}")
        
        # Early stopping if completely failed
        if success_rate == 0 and noise_tokens > 1000:
            print("\n[EARLY STOP] Zero success rate achieved.")
            break
    
    return results


def calculate_half_life(results: List[dict]) -> Tuple[float, float]:
    """
    Fit exponential decay to find half-life.
    
    Model: success_rate = exp(-λ * noise_tokens)
    Half-life = ln(2) / λ
    """
    # Filter to points with non-zero success
    valid = [(r["noise_tokens"], r["success_rate"]) for r in results if r["success_rate"] > 0]
    
    if len(valid) < 2:
        return float('inf'), 0.0
    
    tokens = np.array([v[0] for v in valid])
    rates = np.array([v[1] for v in valid])
    
    # Avoid log(0)
    rates = np.clip(rates, 0.01, 1.0)
    
    # Linear regression on log(rate) = -λ * tokens
    log_rates = np.log(rates)
    
    # Fit: log_rates = -lambda * tokens + intercept
    if len(tokens) > 1:
        coeffs = np.polyfit(tokens, log_rates, 1)
        lambda_decay = -coeffs[0]
        
        if lambda_decay > 0:
            half_life = np.log(2) / lambda_decay
        else:
            half_life = float('inf')
    else:
        lambda_decay = 0.0
        half_life = float('inf')
    
    return half_life, lambda_decay


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="ρ Quantification Protocol")
    parser.add_argument("--url", type=str, help="Cloud RWKV server URL", default=None)
    parser.add_argument("--trials", type=int, default=3, help="Trials per noise level")
    parser.add_argument("--max-noise", type=int, default=4000, help="Maximum noise tokens")
    parser.add_argument("--step", type=int, default=500, help="Noise token step size")
    
    args = parser.parse_args()
    
    # Initialize measurer
    if args.url:
        measurer = RhoMeasurementCloud(args.url)
        mode = "CLOUD"
    else:
        # Local mode - use smallest model
        model_dir = Path(__file__).parent.parent / "models"
        model_path = model_dir / "RWKV-4-World-0.4B-v1-20230529-ctx4096.pth"
        if not model_path.exists():
            print(f"ERROR: Model not found at {model_path}")
            sys.exit(1)
        measurer = RhoMeasurementLocal(model_path)
        mode = "LOCAL"
    
    print(f"\n[MODE: {mode}]")
    print(f"[TRIALS: {args.trials} per noise level]")
    print(f"[MAX NOISE: {args.max_noise} tokens]")
    print(f"[STEP: {args.step} tokens]")
    
    # Run experiment
    results = run_decay_experiment(
        measurer,
        n_trials=args.trials,
        max_noise=args.max_noise,
        step=args.step
    )
    
    # Calculate metrics
    half_life, lambda_decay = calculate_half_life(results)
    
    # Report
    print("\n" + "="*60)
    print("ρ QUANTIFICATION: RESULTS")
    print("="*60)
    
    print("\nDecay Curve:")
    print("-" * 40)
    for r in results:
        bar = "█" * int(r["success_rate"] * 20)
        print(f"  {r['noise_tokens']:5d} tokens: {r['success_rate']:.1%} {bar}")
    
    print(f"\n{'='*60}")
    print(f"HALF-LIFE OF BINDING: {half_life:.0f} tokens")
    print(f"DECAY CONSTANT (λ): {lambda_decay:.6f}")
    print(f"{'='*60}")
    
    if half_life < float('inf'):
        print(f"\nInterpretation:")
        print(f"  - Information in RWKV state degrades by 50% every ~{half_life:.0f} tokens")
        print(f"  - At 4000 tokens, retention ≈ {100 * np.exp(-lambda_decay * 4000):.1f}%")
        print(f"  - This is the 'ρ coefficient' for this architecture")
    else:
        print(f"\nInterpretation:")
        print(f"  - No measurable decay detected in tested range")
        print(f"  - ρ appears very high (binding persists beyond {args.max_noise} tokens)")
    
    # Calculate ρ estimate
    # ρ = 1 - decay_rate, normalized to [0, 1]
    # Higher half-life = higher ρ
    if half_life < float('inf'):
        # Normalize: assume 10000 tokens is "perfect" binding
        rho_estimate = min(1.0, half_life / 10000)
    else:
        rho_estimate = 1.0
    
    print(f"\nρ ESTIMATE: {rho_estimate:.3f}")
    
    # Save results
    output = {
        "timestamp": datetime.now().isoformat(),
        "mode": mode,
        "config": {
            "trials": args.trials,
            "max_noise": args.max_noise,
            "step": args.step
        },
        "decay_curve": results,
        "metrics": {
            "half_life_tokens": half_life if half_life < float('inf') else None,
            "decay_constant": lambda_decay,
            "rho_estimate": rho_estimate
        }
    }
    
    output_file = OUTPUT_DIR / f"rho_measurement_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n[SAVED] {output_file}")
    
    return output


if __name__ == "__main__":
    main()
