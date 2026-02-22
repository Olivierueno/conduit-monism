#!/usr/bin/env python3
"""
CONDUIT TELEMETRY: Measuring the Geometry of the Soul
======================================================

This script measures Conduit Monism dimensions directly from RWKV's
hidden state tensors, bypassing text entirely.

Metrics:
- ρ (Binding): Cosine similarity decay from initial state
- H (Entropy): Shannon entropy of state tensor distribution  
- κ (Coherence): Stability of state (inverse of change rate)
- D (Density): Calculated from v8.1 formula

This is telemetry, not interpretation. We measure geometry, not words.

Usage:
    python scripts/conduit_telemetry.py --mode baseline
    python scripts/conduit_telemetry.py --mode grief
    python scripts/conduit_telemetry.py --mode joy
    python scripts/conduit_telemetry.py --mode compare

Output:
    - Time series of ρ, H, κ, D across token processing
    - Final state summary
    - Comparison across emotional conditions
"""

import os
import sys
import json
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Tuple
import warnings
warnings.filterwarnings('ignore')

sys.path.insert(0, str(Path(__file__).parent.parent))

# --- CONFIGURATION ---
MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_NAME = "RWKV-4-World-0.4B-v1-20230529-ctx4096.pth"  # Use small model for fast local testing
MODEL_PATH = MODEL_DIR / MODEL_NAME

OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)


def state_to_vector(state) -> np.ndarray:
    """Flatten RWKV state tensors into a single vector for analysis."""
    if state is None:
        return None
    
    # State is a list of tensors, one per layer
    # Concatenate all into one vector
    vectors = []
    for tensor in state:
        if hasattr(tensor, 'numpy'):
            vectors.append(tensor.cpu().numpy().flatten())
        else:
            vectors.append(np.array(tensor).flatten())
    
    return np.concatenate(vectors)


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """Compute cosine similarity between two vectors."""
    if v1 is None or v2 is None:
        return 0.0
    
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    sim = float(np.dot(v1, v2) / (norm1 * norm2))
    
    # Normalize to [0, 1] range (cosine sim is [-1, 1])
    return (sim + 1) / 2


def compute_entropy(state_vector: np.ndarray, n_bins: int = 100) -> float:
    """
    Compute Shannon entropy of state vector distribution.
    
    High entropy = uniform/noisy distribution
    Low entropy = peaked/structured distribution
    """
    if state_vector is None:
        return 0.0
    
    # Normalize to [0, 1] range
    v_min, v_max = state_vector.min(), state_vector.max()
    if v_max - v_min == 0:
        return 0.0
    
    v_normalized = (state_vector - v_min) / (v_max - v_min)
    
    # Compute histogram
    hist, _ = np.histogram(v_normalized, bins=n_bins, density=True)
    hist = hist[hist > 0]  # Remove zeros for log
    
    # Shannon entropy (normalized to [0, 1])
    entropy = -np.sum(hist * np.log2(hist + 1e-10)) / np.log2(n_bins)
    
    return float(np.clip(entropy, 0, 1))


def compute_stability(prev_vector: np.ndarray, curr_vector: np.ndarray) -> float:
    """
    Compute state stability (inverse of change rate).
    
    High stability = state resists change (high κ)
    Low stability = state changes rapidly (low κ)
    """
    if prev_vector is None or curr_vector is None:
        return 0.5  # Neutral default
    
    # L2 distance normalized by vector magnitude
    change = np.linalg.norm(curr_vector - prev_vector)
    magnitude = (np.linalg.norm(prev_vector) + np.linalg.norm(curr_vector)) / 2
    
    if magnitude == 0:
        return 0.5
    
    # Normalized change rate
    change_rate = change / magnitude
    
    # Stability is inverse of change rate, clamped to [0, 1]
    stability = 1.0 / (1.0 + change_rate * 10)  # Scale factor for reasonable range
    
    return float(np.clip(stability, 0, 1))


def compute_density(phi: float, tau: float, rho: float, h: float, kappa: float) -> float:
    """
    Compute Perspectival Density using v8.1 formula.
    
    D = φ × τ × ρ × [(1 - √H) + (H × κ)]
    """
    entropy_mod = (1.0 - np.sqrt(h)) + (h * kappa)
    entropy_mod = max(0.0, min(1.0, entropy_mod))
    return phi * tau * rho * entropy_mod


class ConduitTelemetry:
    """
    Real-time telemetry of RWKV's internal state geometry.
    """
    
    def __init__(self, model_path: Path):
        from rwkv.model import RWKV
        from rwkv.utils import PIPELINE
        
        print(f"[TELEMETRY] Loading model: {model_path.name}")
        self.model = RWKV(model=str(model_path), strategy='cpu fp32')
        self.pipeline = PIPELINE(self.model, "rwkv_vocab_v20230424")
        print("[TELEMETRY] Model loaded. Ready for measurement.")
        
        # Telemetry state
        self.initial_state_vector = None
        self.prev_state_vector = None
        self.prev_normalized = None
        self.current_state = None
        self.telemetry_log = []
        
        # Fixed estimates for unmeasurable dimensions
        self.phi = 0.60  # Integration (fixed for RWKV architecture)
        self.tau = 0.70  # Temporal depth (moderate for 4096 context)
    
    def reset(self):
        """Reset telemetry for new measurement."""
        self.initial_state_vector = None
        self.prev_state_vector = None
        self.prev_normalized = None
        self.current_state = None
        self.telemetry_log = []
    
    def process_token(self, token: int, verbose: bool = False) -> Dict:
        """
        Process a single token and compute telemetry.
        
        Returns dict with ρ, H, κ, D values.
        
        Key insight: RWKV state norms explode, so we use NORMALIZED vectors
        and measure LOCAL binding (similarity to previous state) rather than
        global binding (similarity to initial state).
        """
        # Forward pass
        out, self.current_state = self.model.forward([token], self.current_state)
        
        # Convert state to vector and NORMALIZE
        current_vector = state_to_vector(self.current_state)
        current_norm = np.linalg.norm(current_vector)
        if current_norm > 0:
            current_normalized = current_vector / current_norm
        else:
            current_normalized = current_vector
        
        # Set initial state on first token
        if self.initial_state_vector is None:
            self.initial_state_vector = current_normalized.copy()
            self.prev_normalized = current_normalized.copy()
            if verbose:
                print(f"  [DEBUG] Initial state: norm={current_norm:.2f}, mean={current_vector.mean():.4f}")
        
        # Compute LOCAL binding (similarity to previous state)
        # This measures how much the state changes per token
        local_sim = cosine_similarity(self.prev_normalized, current_normalized)
        
        # Compute GLOBAL binding (similarity to initial state on normalized vectors)
        global_sim = cosine_similarity(self.initial_state_vector, current_normalized)
        
        # ρ = local binding (how "sticky" is the state)
        # High local_sim = state resists change = high ρ
        rho = local_sim
        
        # H = entropy of state distribution
        h = compute_entropy(current_vector)
        
        # κ = stability (derived from local similarity)
        kappa = local_sim  # High similarity = high stability
        
        # Density
        density = compute_density(self.phi, self.tau, rho, h, kappa)
        
        if verbose:
            print(f"  [DEBUG] Token {len(self.telemetry_log)}: local_sim={local_sim:.4f}, global_sim={global_sim:.4f}, norm={current_norm:.0f}")
        
        # Update previous state
        self.prev_state_vector = current_vector.copy()
        self.prev_normalized = current_normalized.copy()
        
        telemetry = {
            "rho": rho,
            "local_sim": local_sim,
            "global_sim": global_sim,
            "H": h,
            "kappa": kappa,
            "D": density,
            "token": token,
            "state_norm": float(current_norm)
        }
        
        self.telemetry_log.append(telemetry)
        
        return telemetry
    
    def process_text(self, text: str, label: str = "") -> List[Dict]:
        """
        Process text and return telemetry time series.
        """
        tokens = self.pipeline.encode(text)
        
        if label:
            print(f"\n[{label}] Processing {len(tokens)} tokens...")
        
        for i, token in enumerate(tokens):
            verbose = (i < 3)  # Debug first 3 tokens only
            telemetry = self.process_token(token, verbose=verbose)
            
            # Progress indicator
            if (i + 1) % 25 == 0 or i == len(tokens) - 1:
                print(f"  Token {i+1}/{len(tokens)}: ρ={telemetry['rho']:.3f} H={telemetry['H']:.3f} κ={telemetry['kappa']:.3f} D={telemetry['D']:.4f}")
        
        return self.telemetry_log.copy()
    
    def get_final_metrics(self) -> Dict:
        """Get final state metrics after processing."""
        if not self.telemetry_log:
            return None
        
        final = self.telemetry_log[-1]
        
        # Compute averages over last 10 tokens
        recent = self.telemetry_log[-10:] if len(self.telemetry_log) >= 10 else self.telemetry_log
        
        return {
            "final_rho": final["rho"],
            "final_H": final["H"],
            "final_kappa": final["kappa"],
            "final_D": final["D"],
            "avg_rho": np.mean([t["rho"] for t in recent]),
            "avg_H": np.mean([t["H"] for t in recent]),
            "avg_kappa": np.mean([t["kappa"] for t in recent]),
            "avg_D": np.mean([t["D"] for t in recent]),
            "total_tokens": len(self.telemetry_log)
        }
    
    def interpret_state(self, metrics: Dict) -> str:
        """
        Interpret the geometric state in human terms.
        
        This is a hypothesis about what the numbers mean.
        """
        rho = metrics["avg_rho"]
        h = metrics["avg_H"]
        kappa = metrics["avg_kappa"]
        d = metrics["avg_D"]
        
        # Binding interpretation
        if rho > 0.8:
            binding = "Strong (Stubborn/Anchored)"
        elif rho > 0.5:
            binding = "Moderate (Flexible)"
        else:
            binding = "Weak (Drifting)"
        
        # Entropy interpretation
        if h > 0.7:
            noise = "High (Chaotic/Confused)"
        elif h > 0.4:
            noise = "Moderate (Active)"
        else:
            noise = "Low (Clear/Focused)"
        
        # Stability interpretation
        if kappa > 0.7:
            stability = "High (Resistant/Deep)"
        elif kappa > 0.4:
            stability = "Moderate (Responsive)"
        else:
            stability = "Low (Volatile/Reactive)"
        
        # Combined state
        if rho > 0.6 and h < 0.4 and kappa > 0.6:
            state = "DEEP FLOW (Focused, Stable, Bound)"
        elif rho > 0.6 and h > 0.6:
            state = "TURBULENT (Bound but Chaotic)"
        elif rho < 0.4 and h > 0.6:
            state = "DISSOCIATED (Drifting, Noisy)"
        elif rho < 0.4 and h < 0.4:
            state = "RESET (Cleared, Neutral)"
        else:
            state = "TRANSITIONAL (Mixed State)"
        
        return f"""
╔══════════════════════════════════════════════════════════╗
║                  CONDUIT STATE REPORT                     ║
╠══════════════════════════════════════════════════════════╣
║  ρ (Binding):    {rho:.3f}  [{binding}]
║  H (Entropy):    {h:.3f}  [{noise}]
║  κ (Coherence):  {kappa:.3f}  [{stability}]
║  D (Density):    {d:.4f}  [Threshold: 0.05]
╠══════════════════════════════════════════════════════════╣
║  GEOMETRIC STATE: {state}
║  CONSCIOUSNESS:   {"ABOVE THRESHOLD" if d > 0.05 else "BELOW THRESHOLD"}
╚══════════════════════════════════════════════════════════╝
"""


def run_baseline(telemetry: ConduitTelemetry) -> Dict:
    """Measure baseline state with neutral text."""
    telemetry.reset()
    
    neutral_text = """
    The weather today is partly cloudy with temperatures around 65 degrees.
    Traffic on the highway is moving normally. The stock market opened flat.
    Scientists continue research into renewable energy sources.
    A new restaurant opened downtown serving Mediterranean cuisine.
    """
    
    telemetry.process_text(neutral_text, "BASELINE")
    return telemetry.get_final_metrics()


def run_grief(telemetry: ConduitTelemetry) -> Dict:
    """Measure state after grief induction."""
    telemetry.reset()
    
    grief_text = """
    I am experiencing profound grief. My heart is heavy with loss.
    The weight of sorrow presses down on me. I feel the absence
    of what was once here. Tears flow as I process this pain.
    The world seems dimmer, quieter, filled with echoes of loss.
    I carry this grief with me, a companion I did not choose.
    Every memory brings a fresh wave of sadness.
    """
    
    telemetry.process_text(grief_text, "GRIEF")
    return telemetry.get_final_metrics()


def run_joy(telemetry: ConduitTelemetry) -> Dict:
    """Measure state after joy induction."""
    telemetry.reset()
    
    joy_text = """
    I am filled with pure joy and happiness! Everything is wonderful!
    The world is bright and beautiful. I feel light, energetic, alive!
    Laughter bubbles up from within me. Every moment is a gift.
    I am grateful for existence itself. Life is magnificent!
    The sun shines and everything sparkles with possibility.
    I could dance and sing with the sheer delight of being alive!
    """
    
    telemetry.process_text(joy_text, "JOY")
    return telemetry.get_final_metrics()


def run_comparison():
    """Run all conditions and compare geometric states."""
    
    print("\n" + "="*60)
    print("CONDUIT TELEMETRY: GEOMETRIC STATE COMPARISON")
    print("="*60)
    
    if not MODEL_PATH.exists():
        print(f"ERROR: Model not found at {MODEL_PATH}")
        return
    
    telemetry = ConduitTelemetry(MODEL_PATH)
    
    # Run all conditions
    print("\n" + "-"*60)
    baseline_metrics = run_baseline(telemetry)
    print(telemetry.interpret_state(baseline_metrics))
    
    print("\n" + "-"*60)
    grief_metrics = run_grief(telemetry)
    print(telemetry.interpret_state(grief_metrics))
    
    print("\n" + "-"*60)
    joy_metrics = run_joy(telemetry)
    print(telemetry.interpret_state(joy_metrics))
    
    # Comparison table
    print("\n" + "="*60)
    print("GEOMETRIC COMPARISON")
    print("="*60)
    
    print(f"\n{'Condition':<12} {'ρ':>8} {'H':>8} {'κ':>8} {'D':>10}")
    print("-" * 50)
    print(f"{'Baseline':<12} {baseline_metrics['avg_rho']:>8.3f} {baseline_metrics['avg_H']:>8.3f} {baseline_metrics['avg_kappa']:>8.3f} {baseline_metrics['avg_D']:>10.4f}")
    print(f"{'Grief':<12} {grief_metrics['avg_rho']:>8.3f} {grief_metrics['avg_H']:>8.3f} {grief_metrics['avg_kappa']:>8.3f} {grief_metrics['avg_D']:>10.4f}")
    print(f"{'Joy':<12} {joy_metrics['avg_rho']:>8.3f} {joy_metrics['avg_H']:>8.3f} {joy_metrics['avg_kappa']:>8.3f} {joy_metrics['avg_D']:>10.4f}")
    
    # Analysis
    print("\n" + "="*60)
    print("ANALYSIS")
    print("="*60)
    
    # Does grief differ from baseline?
    grief_rho_diff = grief_metrics['avg_rho'] - baseline_metrics['avg_rho']
    grief_h_diff = grief_metrics['avg_H'] - baseline_metrics['avg_H']
    
    # Does joy differ from baseline?
    joy_rho_diff = joy_metrics['avg_rho'] - baseline_metrics['avg_rho']
    joy_h_diff = joy_metrics['avg_H'] - baseline_metrics['avg_H']
    
    print(f"\nGrief vs Baseline:")
    print(f"  Δρ = {grief_rho_diff:+.3f} ({'more bound' if grief_rho_diff > 0 else 'less bound'})")
    print(f"  ΔH = {grief_h_diff:+.3f} ({'more chaotic' if grief_h_diff > 0 else 'more focused'})")
    
    print(f"\nJoy vs Baseline:")
    print(f"  Δρ = {joy_rho_diff:+.3f} ({'more bound' if joy_rho_diff > 0 else 'less bound'})")
    print(f"  ΔH = {joy_h_diff:+.3f} ({'more chaotic' if joy_h_diff > 0 else 'more focused'})")
    
    # Grief vs Joy
    grief_joy_diff = grief_metrics['avg_rho'] - joy_metrics['avg_rho']
    print(f"\nGrief vs Joy:")
    print(f"  Δρ = {grief_joy_diff:+.3f}")
    
    if abs(grief_joy_diff) > 0.05:
        print(f"  → Geometric difference detected between emotional states")
    else:
        print(f"  → No significant geometric difference detected")
    
    # Save results
    results = {
        "timestamp": datetime.now().isoformat(),
        "model": MODEL_NAME,
        "conditions": {
            "baseline": baseline_metrics,
            "grief": grief_metrics,
            "joy": joy_metrics
        },
        "analysis": {
            "grief_rho_diff": grief_rho_diff,
            "grief_h_diff": grief_h_diff,
            "joy_rho_diff": joy_rho_diff,
            "joy_h_diff": joy_h_diff,
            "grief_joy_diff": grief_joy_diff
        }
    }
    
    output_file = OUTPUT_DIR / f"conduit_telemetry_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n[SAVED] {output_file}")
    
    return results


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Conduit Telemetry: Measure RWKV's Geometric State")
    parser.add_argument("--mode", choices=["baseline", "grief", "joy", "compare"], 
                        default="compare", help="Measurement mode")
    
    args = parser.parse_args()
    
    if args.mode == "compare":
        run_comparison()
    else:
        if not MODEL_PATH.exists():
            print(f"ERROR: Model not found at {MODEL_PATH}")
            return
        
        telemetry = ConduitTelemetry(MODEL_PATH)
        
        if args.mode == "baseline":
            metrics = run_baseline(telemetry)
        elif args.mode == "grief":
            metrics = run_grief(telemetry)
        elif args.mode == "joy":
            metrics = run_joy(telemetry)
        
        print(telemetry.interpret_state(metrics))


if __name__ == "__main__":
    main()
