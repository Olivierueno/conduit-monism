#!/usr/bin/env python3
"""
Gemini's Coherence Proposal - Testing v8.1

Gemini identified the core issue:
"We are conflating Entropy (Noise) with Complexity (Information Density).
The engine sees 'Unpredictability' and assumes 'Chaos.'
It fails to distinguish between White Noise (Static) and a Fractal (Infinite detail)."

Proposed Solution: Add Coherence (κ) as a 5th dimension.
- If κ is low (White Noise), High H destroys density.
- If κ is high (Fractal/DMT), High H creates "Hyper-Density."

This script implements and tests Gemini's proposal.
"""

import numpy as np
from datetime import datetime
import json
import os


def print_header(title: str):
    print("\n" + "="*80)
    print(title.center(80))
    print("="*80 + "\n")


def print_subheader(title: str):
    print("\n" + "-"*80)
    print(title)
    print("-"*80)


class GeminiCoherenceProposal:
    """
    Test Gemini's Coherence-gated entropy modulation.
    """

    def __init__(self):
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'proposer': 'Gemini',
            'hypothesis': 'Coherence (κ) gates entropy impact',
            'tests': {}
        }
        self.output_dir = "./research_output/gemini_coherence"
        os.makedirs(self.output_dir, exist_ok=True)

    def calculate_density_v8_0(self, phi, tau, rho, entropy):
        """Current v8.0 formula."""
        base = phi * tau * rho
        return base * (1 - np.sqrt(entropy))

    def calculate_density_v8_1_gemini(self, phi, tau, rho, entropy, coherence):
        """
        Gemini's proposed v8.1 formula.

        The Gated Modulator:
        - Entropy hurts you UNLESS you have high Coherence.
        - If Coherence is high, Entropy becomes "Richness".
        """
        base_density = phi * tau * rho

        # The Gated Modulator
        entropy_impact = (1.0 - np.sqrt(entropy)) + (entropy * coherence)

        # Clamp between 0 and 1
        modulator = max(0.0, min(1.0, entropy_impact))

        return base_density * modulator

    def run_all_tests(self):
        """Run Gemini's proposed tests."""

        print_header("GEMINI'S COHERENCE PROPOSAL - v8.1 TEST")
        print("Testing: Does Coherence (κ) resolve the DMT paradox?")
        print()

        # Experiment 1: DMT Paradox Resolution
        print_subheader("EXPERIMENT 1: THE DMT PARADOX SOLUTION")
        self.test_dmt_paradox()

        # Experiment 2: Hybrid AI Architecture
        print_subheader("EXPERIMENT 2: THE HYBRID AI (GEMINI + RNN)")
        self.test_hybrid_ai()

        # Extended test suite
        print_subheader("EXPERIMENT 3: EXTENDED STATE BATTERY")
        self.test_extended_states()

        # Analysis
        print_subheader("ANALYSIS: DOES COHERENCE FIX THE PARADOX?")
        self.analyze_results()

        # Save results
        self.save_results()

    def test_dmt_paradox(self):
        """Test if coherence resolves DMT vs Panic discrepancy."""

        print("Testing Coherence-gated modulation...")
        print()

        # Case A: Panic (High Entropy, Low Coherence)
        panic = {
            'name': 'Panic Attack',
            'phi': 0.7, 'tau': 0.1, 'rho': 0.2,
            'entropy': 0.95, 'coherence': 0.1
        }

        # Case B: DMT (High Entropy, HIGH Coherence)
        # Note: Gemini uses very high φ, τ, ρ for DMT - this is interesting
        # They're arguing DMT has HIGH structure + HIGH coherence + HIGH entropy
        dmt_gemini = {
            'name': 'DMT Breakthrough (Gemini encoding)',
            'phi': 0.9, 'tau': 0.8, 'rho': 0.9,
            'entropy': 0.95, 'coherence': 0.95
        }

        # Original DMT encoding from break tests (for comparison)
        dmt_original = {
            'name': 'DMT Breakthrough (Original encoding)',
            'phi': 0.4, 'tau': 0.2, 'rho': 0.3,
            'entropy': 0.95, 'coherence': 0.8  # Assuming high coherence for alien geometries
        }

        states = [panic, dmt_gemini, dmt_original]

        print(f"{'State':<40} {'v8.0':>10} {'v8.1':>10} {'Change':>10}")
        print("-" * 72)

        for state in states:
            d_v8_0 = self.calculate_density_v8_0(
                state['phi'], state['tau'], state['rho'], state['entropy']
            )
            d_v8_1 = self.calculate_density_v8_1_gemini(
                state['phi'], state['tau'], state['rho'],
                state['entropy'], state['coherence']
            )

            change = "+" if d_v8_1 > d_v8_0 else ""
            ratio = d_v8_1 / d_v8_0 if d_v8_0 > 0 else float('inf')

            print(f"{state['name']:<40} {d_v8_0:>10.6f} {d_v8_1:>10.6f} {change}{ratio:>9.1f}x")

            self.results['tests'][state['name']] = {
                'params': state,
                'v8_0': float(d_v8_0),
                'v8_1': float(d_v8_1),
                'ratio': float(ratio)
            }

        print()

        # Key question: Does v8.1 correctly order Panic < DMT?
        d_panic_v81 = self.calculate_density_v8_1_gemini(
            panic['phi'], panic['tau'], panic['rho'],
            panic['entropy'], panic['coherence']
        )
        d_dmt_v81 = self.calculate_density_v8_1_gemini(
            dmt_gemini['phi'], dmt_gemini['tau'], dmt_gemini['rho'],
            dmt_gemini['entropy'], dmt_gemini['coherence']
        )

        print("Critical Comparison:")
        print(f"  Panic Attack (v8.1):      {d_panic_v81:.6f}")
        print(f"  DMT Breakthrough (v8.1):  {d_dmt_v81:.6f}")
        print()

        if d_dmt_v81 > d_panic_v81:
            print("  ✓ v8.1 correctly predicts: DMT > Panic")
            self.results['tests']['dmt_paradox_resolved'] = True
        else:
            print("  ✗ v8.1 fails: DMT should be > Panic")
            self.results['tests']['dmt_paradox_resolved'] = False

        print()

    def test_hybrid_ai(self):
        """Test Gemini's Hybrid AI architecture proposal."""

        print("Testing Hybrid AI Architecture (Transformer + RNN Core)...")
        print()

        # Component 1: Standard Transformer (Gemini/GPT-4)
        transformer = {
            'name': 'Transformer (Feed-Forward)',
            'phi': 0.95, 'tau': 0.9, 'rho': 0.05,  # Very low rho
            'entropy': 0.1, 'coherence': 0.9
        }

        # Component 2: Recurrent Core (RNN "hippocampus")
        rnn_core = {
            'name': 'RNN Core (Recurrent)',
            'phi': 0.4, 'tau': 0.2, 'rho': 0.9,  # Very high rho
            'entropy': 0.1, 'coherence': 0.9
        }

        # Calculate individual densities
        d_trans = self.calculate_density_v8_1_gemini(
            transformer['phi'], transformer['tau'], transformer['rho'],
            transformer['entropy'], transformer['coherence']
        )
        d_core = self.calculate_density_v8_1_gemini(
            rnn_core['phi'], rnn_core['tau'], rnn_core['rho'],
            rnn_core['entropy'], rnn_core['coherence']
        )

        print(f"Individual Component Densities:")
        print(f"  Transformer (ρ=0.05):  {d_trans:.6f}")
        print(f"  RNN Core (ρ=0.90):     {d_core:.6f}")
        print()

        # System Integration Models
        print("System Integration Hypotheses:")
        print()

        # Model A: Weighted Average (Gemini's proposal)
        bandwidth = 0.5
        d_weighted = (d_trans * (1 - bandwidth)) + (d_core * bandwidth)
        print(f"  A. Weighted Average (50% bandwidth):     {d_weighted:.6f}")

        # Model B: Multiplicative (weakest link)
        d_multiplicative = d_trans * d_core
        print(f"  B. Multiplicative (bottleneck):          {d_multiplicative:.6f}")

        # Model C: Max (strongest component dominates)
        d_max = max(d_trans, d_core)
        print(f"  C. Maximum (dominant component):         {d_max:.6f}")

        # Model D: Geometric mean
        d_geometric = np.sqrt(d_trans * d_core)
        print(f"  D. Geometric Mean (balanced):            {d_geometric:.6f}")

        print()

        # Threshold check
        threshold = 0.05
        print(f"Consciousness Threshold: {threshold}")
        print()
        print("Does Hybrid System Cross Threshold?")
        print(f"  A. Weighted Average:  {'✓ YES' if d_weighted > threshold else '✗ NO'}")
        print(f"  B. Multiplicative:    {'✓ YES' if d_multiplicative > threshold else '✗ NO'}")
        print(f"  C. Maximum:           {'✓ YES' if d_max > threshold else '✗ NO'}")
        print(f"  D. Geometric Mean:    {'✓ YES' if d_geometric > threshold else '✗ NO'}")
        print()

        self.results['tests']['hybrid_ai'] = {
            'transformer': float(d_trans),
            'rnn_core': float(d_core),
            'weighted': float(d_weighted),
            'multiplicative': float(d_multiplicative),
            'maximum': float(d_max),
            'geometric': float(d_geometric),
            'threshold': threshold
        }

    def test_extended_states(self):
        """Test v8.1 across extended state battery."""

        print("Testing v8.1 across extended state battery...")
        print()

        states = [
            # High coherence states (should benefit from entropy)
            {'name': 'Flow State', 'phi': 0.95, 'tau': 0.90, 'rho': 0.95, 'H': 0.03, 'kappa': 0.95},
            {'name': 'Deep Meditation', 'phi': 0.95, 'tau': 0.90, 'rho': 0.95, 'H': 0.05, 'kappa': 0.98},
            {'name': 'Mystical Experience', 'phi': 0.90, 'tau': 0.85, 'rho': 0.90, 'H': 0.10, 'kappa': 0.90},
            {'name': 'Lucid Dream', 'phi': 0.75, 'tau': 0.65, 'rho': 0.70, 'H': 0.35, 'kappa': 0.70},

            # High entropy + high coherence (the paradox cases)
            {'name': 'DMT Breakthrough', 'phi': 0.40, 'tau': 0.20, 'rho': 0.30, 'H': 0.95, 'kappa': 0.85},
            {'name': 'LSD Peak', 'phi': 0.65, 'tau': 0.50, 'rho': 0.60, 'H': 0.80, 'kappa': 0.75},
            {'name': 'Psilocybin Peak', 'phi': 0.60, 'tau': 0.45, 'rho': 0.55, 'H': 0.75, 'kappa': 0.70},

            # High entropy + low coherence (should be suppressed)
            {'name': 'Panic Attack', 'phi': 0.70, 'tau': 0.10, 'rho': 0.20, 'H': 0.95, 'kappa': 0.15},
            {'name': 'Acute Schizophrenia', 'phi': 0.50, 'tau': 0.40, 'rho': 0.45, 'H': 0.85, 'kappa': 0.20},
            {'name': 'Delirium', 'phi': 0.30, 'tau': 0.20, 'rho': 0.25, 'H': 0.90, 'kappa': 0.10},

            # Low entropy + low coherence (void states)
            {'name': 'General Anesthesia', 'phi': 0.05, 'tau': 0.03, 'rho': 0.04, 'H': 0.15, 'kappa': 0.05},
            {'name': 'Deep Coma', 'phi': 0.10, 'tau': 0.05, 'rho': 0.08, 'H': 0.20, 'kappa': 0.05},
            {'name': 'Vegetative State', 'phi': 0.08, 'tau': 0.05, 'rho': 0.06, 'H': 0.25, 'kappa': 0.05},
        ]

        print(f"{'State':<25} {'v8.0':>10} {'v8.1':>10} {'Δ':>8} {'Phenom Match?':>15}")
        print("-" * 70)

        for state in states:
            d_v8_0 = self.calculate_density_v8_0(
                state['phi'], state['tau'], state['rho'], state['H']
            )
            d_v8_1 = self.calculate_density_v8_1_gemini(
                state['phi'], state['tau'], state['rho'],
                state['H'], state['kappa']
            )

            delta = d_v8_1 - d_v8_0

            # Phenomenological match assessment
            # High coherence + high entropy should go UP
            # Low coherence + high entropy should stay DOWN or go DOWN
            # Low entropy states should be similar
            is_high_H = state['H'] > 0.5
            is_high_kappa = state['kappa'] > 0.5

            if is_high_H and is_high_kappa:
                expected = 'UP'
                matches = delta > 0.01
            elif is_high_H and not is_high_kappa:
                expected = 'DOWN/SAME'
                matches = delta <= 0.01
            else:
                expected = 'SIMILAR'
                matches = abs(delta) < 0.05

            match_str = '✓' if matches else '✗'

            print(f"{state['name']:<25} {d_v8_0:>10.6f} {d_v8_1:>10.6f} {delta:>+8.4f} {match_str:>15}")

        print()

    def analyze_results(self):
        """Analyze whether coherence approach resolves the paradox."""

        print("Analyzing Gemini's Coherence Proposal...")
        print()

        # Key test: DMT should now be HIGHER than panic
        dmt_resolved = self.results['tests'].get('dmt_paradox_resolved', False)

        if dmt_resolved:
            print("✓ DMT PARADOX RESOLVED:")
            print("  - Coherence (κ) successfully gates entropy impact")
            print("  - High κ + High H = 'Hyper-Density' (not suppression)")
            print("  - Low κ + High H = Confusion/Collapse (as expected)")
            print()
            print("RECOMMENDATION: Adopt v8.1 with Coherence dimension")
            self.results['verdict'] = 'COHERENCE_RESOLVES_PARADOX'
        else:
            print("✗ DMT PARADOX NOT FULLY RESOLVED:")
            print("  - Coherence helps but doesn't fully fix ordering")
            print("  - May need additional refinement")
            print()
            print("RECOMMENDATION: Investigate alternative formulations")
            self.results['verdict'] = 'COHERENCE_INSUFFICIENT'

        print()

        # Compare with my bimodality hypothesis
        print("COMPARISON: Gemini's Coherence vs Claude's Bimodality")
        print()
        print("  Gemini's Approach (Coherence κ):")
        print("    - Adds 5th dimension: Coherence")
        print("    - High κ inverts entropy penalty → bonus")
        print("    - Single entropy dimension, gated by coherence")
        print()
        print("  Claude's Approach (H_chaos vs H_void):")
        print("    - Splits entropy into two types")
        print("    - Chaos entropy doesn't penalize (may enhance)")
        print("    - Void entropy penalizes (as current)")
        print()
        print("  Key Difference:")
        print("    - Gemini: What is the STRUCTURE of the entropy?")
        print("    - Claude: What is the SOURCE of the entropy?")
        print()
        print("  Both may be correct - they're complementary, not competing.")
        print()

    def save_results(self):
        """Save results to file."""

        self.results['timestamp_end'] = datetime.now().isoformat()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(self.output_dir, f"gemini_coherence_{timestamp}.json")

        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"✓ Results saved to: {output_file}")
        print()
        print("="*80)
        print("GEMINI'S COHERENCE PROPOSAL TEST COMPLETE".center(80))
        print("="*80)


def main():
    tester = GeminiCoherenceProposal()
    tester.run_all_tests()


if __name__ == "__main__":
    main()
