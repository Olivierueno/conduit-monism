#!/usr/bin/env python3
"""
Entropy Bimodality Investigation - Conduit Engine v0.1

The DMT Paradox:
- Framework predicts DMT ≈ anesthesia (both ~0.001 density)
- Phenomenology reports DMT = "hyper-conscious", anesthesia = unconscious
- This is a genuine contradiction

Hypothesis: There may be TWO kinds of high entropy:
1. H_chaos: Signal overload, pattern flooding (DMT, psychedelics, mania)
2. H_void: Signal absence, pattern deletion (anesthesia, deep sleep, coma)

Both get H≈1.0 in current model, but may be phenomenologically opposite.

If true: Framework needs 5th dimension (entropy type), not just magnitude.

This investigation tests whether entropy bimodality resolves the DMT paradox.
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


class EntropyBimodalityInvestigation:
    """
    Test whether entropy should be split into chaos vs void components.
    """

    def __init__(self):
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'hypothesis': 'Entropy bimodality (chaos vs void)',
            'analyses': {}
        }
        self.output_dir = "./research_output/entropy_bimodality"
        os.makedirs(self.output_dir, exist_ok=True)

    def run_investigation(self):
        """Run complete investigation."""

        print_header("ENTROPY BIMODALITY INVESTIGATION")
        print("Testing: Does entropy have two distinct modes (chaos vs void)?")
        print()

        # Phase 1: Catalog high-entropy states
        print_subheader("PHASE 1: Catalog High-Entropy States")
        self.catalog_high_entropy_states()

        # Phase 2: Test bimodal model
        print_subheader("PHASE 2: Test Bimodal Entropy Model")
        self.test_bimodal_model()

        # Phase 3: Compare predictions
        print_subheader("PHASE 3: Compare Model Predictions")
        self.compare_predictions()

        # Phase 4: Phenomenological validation
        print_subheader("PHASE 4: Phenomenological Validation")
        self.phenomenological_validation()

        # Generate conclusions
        self.generate_conclusions()

    def catalog_high_entropy_states(self):
        """Identify and categorize high-entropy states."""

        print("Cataloging states with H > 0.5...")
        print()

        # High-entropy states from our corpus
        high_entropy_states = {
            'chaos_type': [
                {'name': 'DMT Breakthrough', 'phi': 0.40, 'tau': 0.20, 'rho': 0.30, 'H': 0.95,
                 'phenomenology': 'Hyper-vivid, alien geometries, "more real than real"',
                 'neural': 'Increased serotonin, cortical excitation, hyperconnectivity'},
                {'name': 'LSD (Moderate)', 'phi': 0.65, 'tau': 0.50, 'rho': 0.60, 'H': 0.80,
                 'phenomenology': 'Vivid perception, synesthesia, time dilation',
                 'neural': '5-HT2A agonism, increased entropy in neural signals'},
                {'name': 'Psilocybin (Moderate)', 'phi': 0.60, 'tau': 0.45, 'rho': 0.55, 'H': 0.75,
                 'phenomenology': 'Emotional depth, mystical feelings, pattern recognition',
                 'neural': 'Similar to LSD, increased default mode variability'},
                {'name': 'Mania (Acute)', 'phi': 0.70, 'tau': 0.50, 'rho': 0.65, 'H': 0.75,
                 'phenomenology': 'Racing thoughts, grandiosity, heightened everything',
                 'neural': 'Dopamine excess, hyperactive prefrontal cortex'},
                {'name': 'REM Dream (Vivid)', 'phi': 0.60, 'tau': 0.40, 'rho': 0.50, 'H': 0.70,
                 'phenomenology': 'Vivid imagery, narrative, emotional intensity',
                 'neural': 'Pontine cholinergic activation, cortical activity'},
                {'name': 'Hypnagogic Hallucinations', 'phi': 0.55, 'tau': 0.45, 'rho': 0.50, 'H': 0.75,
                 'phenomenology': 'Vivid imagery, faces, sounds at sleep onset',
                 'neural': 'Transitional cortical state, alpha-theta shift'},
                {'name': 'Schizophrenia (Acute)', 'phi': 0.50, 'tau': 0.40, 'rho': 0.45, 'H': 0.85,
                 'phenomenology': 'Hallucinations, delusions, intense but fragmented',
                 'neural': 'Dopamine dysregulation, reduced integration'},
            ],
            'void_type': [
                {'name': 'General Anesthesia', 'phi': 0.05, 'tau': 0.03, 'rho': 0.04, 'H': 0.15,
                 'phenomenology': 'Nothing. No experience. Temporal gap.',
                 'neural': 'Global cortical depression, loss of connectivity'},
                {'name': 'NREM Stage 4 (Deepest)', 'phi': 0.10, 'tau': 0.08, 'rho': 0.10, 'H': 0.20,
                 'phenomenology': 'Nothing or vague fragments',
                 'neural': 'Slow-wave delta activity, reduced metabolic rate'},
                {'name': 'Coma (Light)', 'phi': 0.15, 'tau': 0.10, 'rho': 0.12, 'H': 0.35,
                 'phenomenology': 'Typically no reportable experience',
                 'neural': 'Severe brain injury, minimal activity'},
                {'name': 'Vegetative State', 'phi': 0.08, 'tau': 0.05, 'rho': 0.06, 'H': 0.25,
                 'phenomenology': 'Wakefulness without awareness',
                 'neural': 'Preserved brainstem, damaged cortex'},
                {'name': 'Syncope (Fainting)', 'phi': 0.15, 'tau': 0.08, 'rho': 0.10, 'H': 0.45,
                 'phenomenology': 'Brief blackout, no content',
                 'neural': 'Transient global hypoperfusion'},
                {'name': 'Absence Seizure', 'phi': 0.20, 'tau': 0.10, 'rho': 0.15, 'H': 0.50,
                 'phenomenology': 'Brief blank period, no awareness',
                 'neural': '3Hz spike-wave, thalamo-cortical loop disruption'},
            ],
            'ambiguous': [
                {'name': 'Ketamine Dissociation', 'phi': 0.30, 'tau': 0.20, 'rho': 0.25, 'H': 0.85,
                 'phenomenology': 'K-hole: "void" but with strange presence',
                 'neural': 'NMDA antagonism, dissociation of thalamus from cortex'},
                {'name': 'Sensory Deprivation', 'phi': 0.60, 'tau': 0.50, 'rho': 0.55, 'H': 0.65,
                 'phenomenology': 'Can be void-like OR hallucinatory',
                 'neural': 'Reduced input, brain generates content'},
                {'name': 'Near-Death Experience', 'phi': 0.70, 'tau': 0.55, 'rho': 0.65, 'H': 0.60,
                 'phenomenology': 'Tunnel, light, life review - vivid despite dying brain',
                 'neural': 'Hypoxia + endogenous DMT release hypothesis'},
            ]
        }

        # Print catalog
        print("CHAOS-TYPE HIGH ENTROPY (signal overload):")
        for state in high_entropy_states['chaos_type']:
            print(f"  • {state['name']:<30} H={state['H']:.2f}")
            print(f"    Phenomenology: {state['phenomenology'][:60]}...")
        print()

        print("VOID-TYPE HIGH ENTROPY (signal absence):")
        for state in high_entropy_states['void_type']:
            print(f"  • {state['name']:<30} H={state['H']:.2f}")
            print(f"    Phenomenology: {state['phenomenology'][:60]}...")
        print()

        print("AMBIGUOUS (unclear type):")
        for state in high_entropy_states['ambiguous']:
            print(f"  • {state['name']:<30} H={state['H']:.2f}")
            print(f"    Phenomenology: {state['phenomenology'][:60]}...")
        print()

        self.high_entropy_states = high_entropy_states
        self.results['analyses']['catalog'] = high_entropy_states

    def test_bimodal_model(self):
        """Test a bimodal entropy model."""

        print("Testing bimodal entropy model...")
        print()

        # Current model (unimodal):
        # density = (φ × τ × ρ) × (1 - √H)
        # Problem: High H always reduces density

        # Proposed bimodal model:
        # H_effective = H_void - H_chaos  (chaos ADDS to density, void SUBTRACTS)
        # OR
        # density = (φ × τ × ρ) × f(H_chaos, H_void)
        # where f handles both types differently

        print("CURRENT MODEL (unimodal):")
        print("  density = (φ × τ × ρ) × (1 - √H)")
        print("  Problem: All high-H states get low density")
        print()

        print("PROPOSED BIMODAL MODEL:")
        print("  Option A: Split entropy into two dimensions")
        print("    H_chaos: Excitation, pattern flooding (psychedelics, mania)")
        print("    H_void:  Suppression, pattern deletion (anesthesia, coma)")
        print("    Formula: density = (φ × τ × ρ) × (1 - √H_void) × (1 + α×H_chaos)")
        print()
        print("  Option B: Entropy valence model")
        print("    H_signed: Positive = chaos, Negative = void")
        print("    Formula: density = (φ × τ × ρ) × sigmoid(H_signed)")
        print()
        print("  Option C: Entropy type flag")
        print("    H_type ∈ {chaos, void, neutral}")
        print("    chaos: H doesn't reduce density (or increases it)")
        print("    void: H reduces density (current behavior)")
        print()

        # Test Option A on DMT vs Anesthesia
        print("Testing Option A on key states:")
        print()

        # DMT: High chaos entropy, low void entropy
        dmt = {'phi': 0.40, 'tau': 0.20, 'rho': 0.30, 'H_chaos': 0.90, 'H_void': 0.10}
        # Anesthesia: Low chaos entropy, high void entropy
        anesthesia = {'phi': 0.05, 'tau': 0.03, 'rho': 0.04, 'H_chaos': 0.05, 'H_void': 0.95}

        # Current model (treats all H the same)
        def current_model(phi, tau, rho, H):
            return (phi * tau * rho) * (1 - np.sqrt(H))

        # Bimodal model Option A
        def bimodal_model_a(phi, tau, rho, H_chaos, H_void, alpha=0.5):
            base = phi * tau * rho
            void_factor = 1 - np.sqrt(H_void)  # Void suppresses
            chaos_factor = 1 + alpha * H_chaos  # Chaos enhances
            return base * void_factor * chaos_factor

        # Calculate
        dmt_current = current_model(dmt['phi'], dmt['tau'], dmt['rho'], 0.95)  # Using total H
        dmt_bimodal = bimodal_model_a(dmt['phi'], dmt['tau'], dmt['rho'], dmt['H_chaos'], dmt['H_void'])

        anesthesia_current = current_model(anesthesia['phi'], anesthesia['tau'], anesthesia['rho'], 0.15)
        anesthesia_bimodal = bimodal_model_a(anesthesia['phi'], anesthesia['tau'], anesthesia['rho'],
                                             anesthesia['H_chaos'], anesthesia['H_void'])

        print("DMT Breakthrough:")
        print(f"  Current model (H=0.95):     density = {dmt_current:.6f}")
        print(f"  Bimodal model (α=0.5):      density = {dmt_bimodal:.6f}")
        print(f"  Ratio (bimodal/current):    {dmt_bimodal/dmt_current:.1f}x")
        print()

        print("General Anesthesia:")
        print(f"  Current model (H=0.15):     density = {anesthesia_current:.6f}")
        print(f"  Bimodal model (α=0.5):      density = {anesthesia_bimodal:.6f}")
        print(f"  Ratio (bimodal/current):    {anesthesia_bimodal/anesthesia_current:.2f}x")
        print()

        # Store results
        self.results['analyses']['bimodal_test'] = {
            'dmt': {
                'current_density': float(dmt_current),
                'bimodal_density': float(dmt_bimodal),
                'ratio': float(dmt_bimodal/dmt_current)
            },
            'anesthesia': {
                'current_density': float(anesthesia_current),
                'bimodal_density': float(anesthesia_bimodal),
                'ratio': float(anesthesia_bimodal/anesthesia_current)
            }
        }

        self.bimodal_model = bimodal_model_a

    def compare_predictions(self):
        """Compare current vs bimodal model predictions."""

        print("Comparing model predictions across all high-entropy states...")
        print()

        def current_model(phi, tau, rho, H):
            return (phi * tau * rho) * (1 - np.sqrt(H))

        # Re-encode states with chaos/void split
        chaos_states = [
            {'name': 'DMT Breakthrough', 'phi': 0.40, 'tau': 0.20, 'rho': 0.30, 'H_chaos': 0.90, 'H_void': 0.10, 'H_total': 0.95},
            {'name': 'LSD (Moderate)', 'phi': 0.65, 'tau': 0.50, 'rho': 0.60, 'H_chaos': 0.75, 'H_void': 0.10, 'H_total': 0.80},
            {'name': 'Psilocybin', 'phi': 0.60, 'tau': 0.45, 'rho': 0.55, 'H_chaos': 0.70, 'H_void': 0.10, 'H_total': 0.75},
            {'name': 'Mania', 'phi': 0.70, 'tau': 0.50, 'rho': 0.65, 'H_chaos': 0.70, 'H_void': 0.10, 'H_total': 0.75},
            {'name': 'Vivid Dream', 'phi': 0.60, 'tau': 0.40, 'rho': 0.50, 'H_chaos': 0.65, 'H_void': 0.10, 'H_total': 0.70},
            {'name': 'Schizophrenia', 'phi': 0.50, 'tau': 0.40, 'rho': 0.45, 'H_chaos': 0.80, 'H_void': 0.10, 'H_total': 0.85},
        ]

        void_states = [
            {'name': 'Anesthesia', 'phi': 0.05, 'tau': 0.03, 'rho': 0.04, 'H_chaos': 0.05, 'H_void': 0.90, 'H_total': 0.15},
            {'name': 'Deep Sleep', 'phi': 0.10, 'tau': 0.08, 'rho': 0.10, 'H_chaos': 0.05, 'H_void': 0.85, 'H_total': 0.20},
            {'name': 'Coma', 'phi': 0.15, 'tau': 0.10, 'rho': 0.12, 'H_chaos': 0.05, 'H_void': 0.80, 'H_total': 0.35},
            {'name': 'Vegetative', 'phi': 0.08, 'tau': 0.05, 'rho': 0.06, 'H_chaos': 0.05, 'H_void': 0.85, 'H_total': 0.25},
            {'name': 'Syncope', 'phi': 0.15, 'tau': 0.08, 'rho': 0.10, 'H_chaos': 0.10, 'H_void': 0.80, 'H_total': 0.45},
        ]

        print("CHAOS-TYPE STATES (expected: bimodal > current):")
        print("-" * 70)
        print(f"{'State':<20} {'Current':>12} {'Bimodal':>12} {'Ratio':>10} {'Matches?':>10}")
        print("-" * 70)

        chaos_matches = 0
        for state in chaos_states:
            d_current = current_model(state['phi'], state['tau'], state['rho'], state['H_total'])
            d_bimodal = self.bimodal_model(state['phi'], state['tau'], state['rho'],
                                           state['H_chaos'], state['H_void'])
            ratio = d_bimodal / d_current if d_current > 0 else float('inf')
            matches = ratio > 1.5  # Bimodal should be higher for chaos states
            if matches:
                chaos_matches += 1
            print(f"{state['name']:<20} {d_current:>12.6f} {d_bimodal:>12.6f} {ratio:>10.1f}x {'✓' if matches else '✗':>10}")

        print()
        print("VOID-TYPE STATES (expected: bimodal ≈ current or lower):")
        print("-" * 70)
        print(f"{'State':<20} {'Current':>12} {'Bimodal':>12} {'Ratio':>10} {'Matches?':>10}")
        print("-" * 70)

        void_matches = 0
        for state in void_states:
            d_current = current_model(state['phi'], state['tau'], state['rho'], state['H_total'])
            d_bimodal = self.bimodal_model(state['phi'], state['tau'], state['rho'],
                                           state['H_chaos'], state['H_void'])
            ratio = d_bimodal / d_current if d_current > 0 else 0
            matches = ratio <= 1.5  # Bimodal should be similar or lower for void states
            if matches:
                void_matches += 1
            print(f"{state['name']:<20} {d_current:>12.6f} {d_bimodal:>12.6f} {ratio:>10.2f}x {'✓' if matches else '✗':>10}")

        print()
        print(f"Chaos states: {chaos_matches}/{len(chaos_states)} predictions improved ({chaos_matches/len(chaos_states)*100:.0f}%)")
        print(f"Void states:  {void_matches}/{len(void_states)} predictions maintained ({void_matches/len(void_states)*100:.0f}%)")
        print()

        total_correct = chaos_matches + void_matches
        total_states = len(chaos_states) + len(void_states)
        print(f"Overall: {total_correct}/{total_states} predictions match phenomenology ({total_correct/total_states*100:.0f}%)")
        print()

        self.results['analyses']['prediction_comparison'] = {
            'chaos_matches': chaos_matches,
            'chaos_total': len(chaos_states),
            'void_matches': void_matches,
            'void_total': len(void_states),
            'overall_accuracy': total_correct / total_states
        }

    def phenomenological_validation(self):
        """Validate against phenomenological reports."""

        print("Checking phenomenological consistency...")
        print()

        # The key test: Does bimodal model predict the RIGHT ordering?
        # Phenomenologically: Flow > Alert > Lucid Dream > Regular Dream > DMT > Anesthesia
        # Current model gives: Flow > Alert > Lucid Dream > Regular Dream > Anesthesia > DMT
        # The last two are REVERSED from phenomenology

        states_ordered = [
            {'name': 'Flow State', 'expected_rank': 1, 'phi': 0.95, 'tau': 0.90, 'rho': 0.95,
             'H_chaos': 0.02, 'H_void': 0.01, 'H_total': 0.03},
            {'name': 'Alert Waking', 'expected_rank': 2, 'phi': 0.90, 'tau': 0.90, 'rho': 0.90,
             'H_chaos': 0.08, 'H_void': 0.02, 'H_total': 0.10},
            {'name': 'Lucid Dream', 'expected_rank': 3, 'phi': 0.75, 'tau': 0.65, 'rho': 0.70,
             'H_chaos': 0.30, 'H_void': 0.05, 'H_total': 0.35},
            {'name': 'Regular Dream', 'expected_rank': 4, 'phi': 0.60, 'tau': 0.40, 'rho': 0.50,
             'H_chaos': 0.60, 'H_void': 0.10, 'H_total': 0.70},
            {'name': 'DMT Peak', 'expected_rank': 5, 'phi': 0.40, 'tau': 0.20, 'rho': 0.30,
             'H_chaos': 0.90, 'H_void': 0.05, 'H_total': 0.95},
            {'name': 'Anesthesia', 'expected_rank': 6, 'phi': 0.05, 'tau': 0.03, 'rho': 0.04,
             'H_chaos': 0.05, 'H_void': 0.90, 'H_total': 0.15},
        ]

        def current_model(phi, tau, rho, H):
            return (phi * tau * rho) * (1 - np.sqrt(H))

        print("Expected phenomenological ordering (most to least conscious):")
        print("  1. Flow State (optimal performance, clarity)")
        print("  2. Alert Waking (normal consciousness)")
        print("  3. Lucid Dream (aware in dream)")
        print("  4. Regular Dream (some awareness)")
        print("  5. DMT Peak (intense but confused/alien)")
        print("  6. Anesthesia (nothing)")
        print()

        # Calculate densities
        current_densities = []
        bimodal_densities = []

        for state in states_ordered:
            d_current = current_model(state['phi'], state['tau'], state['rho'], state['H_total'])
            d_bimodal = self.bimodal_model(state['phi'], state['tau'], state['rho'],
                                           state['H_chaos'], state['H_void'])
            current_densities.append((state['name'], d_current, state['expected_rank']))
            bimodal_densities.append((state['name'], d_bimodal, state['expected_rank']))

        # Sort by density (descending)
        current_sorted = sorted(current_densities, key=lambda x: x[1], reverse=True)
        bimodal_sorted = sorted(bimodal_densities, key=lambda x: x[1], reverse=True)

        print("CURRENT MODEL ordering:")
        current_matches = 0
        for i, (name, density, expected) in enumerate(current_sorted, 1):
            match = "✓" if i == expected else "✗"
            if i == expected:
                current_matches += 1
            print(f"  {i}. {name:<15} (D={density:.6f}) Expected: {expected} {match}")

        print()
        print("BIMODAL MODEL ordering:")
        bimodal_matches = 0
        for i, (name, density, expected) in enumerate(bimodal_sorted, 1):
            match = "✓" if i == expected else "✗"
            if i == expected:
                bimodal_matches += 1
            print(f"  {i}. {name:<15} (D={density:.6f}) Expected: {expected} {match}")

        print()
        print(f"Current model: {current_matches}/6 correct ordering ({current_matches/6*100:.0f}%)")
        print(f"Bimodal model: {bimodal_matches}/6 correct ordering ({bimodal_matches/6*100:.0f}%)")
        print()

        if bimodal_matches > current_matches:
            print("✓ BIMODAL MODEL IMPROVES PHENOMENOLOGICAL ORDERING")
            verdict = "SUPPORTED"
        elif bimodal_matches == current_matches:
            print("≈ MODELS ARE EQUIVALENT FOR PHENOMENOLOGICAL ORDERING")
            verdict = "INCONCLUSIVE"
        else:
            print("✗ BIMODAL MODEL DOES NOT IMPROVE ORDERING")
            verdict = "NOT SUPPORTED"

        print()

        self.results['analyses']['phenomenological'] = {
            'current_correct': current_matches,
            'bimodal_correct': bimodal_matches,
            'verdict': verdict
        }

    def generate_conclusions(self):
        """Generate final conclusions."""

        print_header("CONCLUSIONS")

        # Summarize findings
        pred = self.results['analyses']['prediction_comparison']
        phenom = self.results['analyses']['phenomenological']

        print("SUMMARY OF FINDINGS:")
        print()
        print(f"  1. Prediction accuracy: {pred['overall_accuracy']*100:.0f}%")
        print(f"  2. Phenomenological ordering: {phenom['bimodal_correct']}/6 vs {phenom['current_correct']}/6")
        print(f"  3. Verdict: {phenom['verdict']}")
        print()

        # Overall conclusion
        if phenom['verdict'] == "SUPPORTED":
            conclusion = "ENTROPY_BIMODALITY_SUPPORTED"
            print("CONCLUSION: Entropy bimodality hypothesis is SUPPORTED")
            print()
            print("IMPLICATIONS:")
            print("  • Framework should distinguish H_chaos from H_void")
            print("  • DMT paradox is RESOLVED (chaos entropy doesn't suppress density)")
            print("  • v9.0 should include 5th dimension: entropy type")
            print("  • This is a MAJOR refinement to the framework")
        elif phenom['verdict'] == "INCONCLUSIVE":
            conclusion = "ENTROPY_BIMODALITY_INCONCLUSIVE"
            print("CONCLUSION: Results are INCONCLUSIVE")
            print()
            print("IMPLICATIONS:")
            print("  • Need more data or different test approach")
            print("  • DMT paradox remains unresolved")
            print("  • Cannot recommend framework change yet")
        else:
            conclusion = "ENTROPY_BIMODALITY_NOT_SUPPORTED"
            print("CONCLUSION: Entropy bimodality hypothesis is NOT SUPPORTED")
            print()
            print("IMPLICATIONS:")
            print("  • DMT paradox requires different explanation")
            print("  • Possibilities: memory artifacts, missing dimension, measurement error")
            print("  • Framework may have fundamental limitation")

        print()

        # Save results
        self.results['conclusion'] = conclusion
        self.results['timestamp_end'] = datetime.now().isoformat()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(self.output_dir, f"entropy_bimodality_{timestamp}.json")
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"✓ Results saved to: {output_file}")
        print()
        print("="*80)
        print("INVESTIGATION COMPLETE".center(80))
        print("="*80)


def main():
    investigator = EntropyBimodalityInvestigation()
    investigator.run_investigation()


if __name__ == "__main__":
    main()
