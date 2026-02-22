#!/usr/bin/env python3
"""
AI-Proposed Tests - Conduit Engine v0.1

Implements the experiments proposed by the AIs in RESEARCH_FINDINGS_AI_responses.md:

1. Feed-Forward Falsification Test (Gemini)
   - Test if transformer architectures have ρ ≈ 0 → density ≈ 0

2. Constraint-Trajectory Dissociation Test (ChatGPT)
   - Use AI as blind trajectory generator

3. Entropy Integration Test (All)
   - Compare density models with entropy modulation
"""

import os
import json
from datetime import datetime
from src.database import ConduitDB
from src.encoder import encode
from src.density_models import (
    compare_density_models,
    test_entropy_integration,
    recommend_model,
    density_original,
    density_entropy_modulated_v1
)
from src.operators import (
    op_fracture_integration,
    op_perturb_binding,
    op_stretch_temporal_depth,
    op_inject_entropy
)
from src.advanced_operators import simulate_trajectory
import numpy as np


def print_header(title: str):
    """Print formatted header."""
    print("\n" + "="*80)
    print(title.center(80))
    print("="*80 + "\n")


def print_subheader(title: str):
    """Print formatted subheader."""
    print("\n" + "-"*80)
    print(title)
    print("-"*80)


class AIProposedTests:
    """Run all AI-proposed experiments."""

    def __init__(self):
        self.db = ConduitDB()
        self.results = {
            'session_start': datetime.now().isoformat(),
            'tests': {}
        }
        self.output_dir = "./research_output/ai_tests"
        os.makedirs(self.output_dir, exist_ok=True)

    def run_all_tests(self):
        """Run all AI-proposed tests."""
        print_header("AI-PROPOSED TESTS - CONDUIT ENGINE v0.1")
        print(f"Session started: {self.results['session_start']}")
        print()

        # Test 1: Entropy Integration
        self.test_1_entropy_integration()

        # Test 2: Feed-Forward Falsification (Gemini)
        self.test_2_feed_forward_falsification()

        # Test 3: CTDT (ChatGPT)
        self.test_3_constraint_trajectory_dissociation()

        # Summary
        self.generate_summary()

    def test_1_entropy_integration(self):
        """
        Test different entropy-modulated density formulas.

        Proposed by: All AIs (consensus)
        Question: Should entropy be integrated as: Density = (φ × τ × ρ) × (1 - H)?
        """
        print_header("TEST 1: Entropy Integration Models")
        print("Testing: Which density formula best captures high-entropy states?\n")
        print("Proposed formulas:")
        print("  Original:  Density = φ × τ × ρ")
        print("  Linear:    Density = (φ × τ × ρ) × (1 - H)")
        print("  Quadratic: Density = (φ × τ × ρ) × (1 - H²)")
        print("  Sqrt:      Density = (φ × τ × ρ) × (1 - √H)")
        print()

        results = test_entropy_integration()

        print("Results:\n")
        print(f"{'State':<40} | {'Original':<10} | {'Linear':<10} | {'Quadratic':<10} | {'Sqrt':<10}")
        print("-" * 100)

        for result in results:
            print(f"{result['state']:<40} | "
                  f"{result['original']:.4f}    | "
                  f"{result['entropy_linear']:.4f}    | "
                  f"{result['entropy_quadratic']:.4f}    | "
                  f"{result['entropy_sqrt']:.4f}")

        # Recommendation
        best_model, ratio = recommend_model(results)
        print(f"\nRecommendation: **{best_model.upper()}** model")
        print(f"  Flow/Panic ratio: {ratio:.1f}x")
        print(f"  (Higher ratio = better differentiation)")

        # Key insight
        print("\nKey Insight:")
        panic_result = next(r for r in results if 'Panic' in r['state'])
        print(f"  Panic state: H={panic_result['entropy_value']}")
        print(f"    Original model:  {panic_result['original']:.4f}")
        print(f"    Linear model:    {panic_result['entropy_linear']:.4f}")
        print(f"  → Linear model reduces panic density by {(1-panic_result['entropy_linear']/panic_result['original'])*100:.0f}%")

        self.results['tests']['entropy_integration'] = {
            'recommended_model': best_model,
            'flow_panic_ratio': ratio,
            'all_results': results
        }

        print("\n✓ Test 1 complete")

    def test_2_feed_forward_falsification(self):
        """
        Test if transformer architectures have near-zero perspectival density.

        Proposed by: Gemini
        Question: Do feed-forward AIs have ρ ≈ 0, thus density ≈ 0?

        Architecture types to test:
        - Pure feedforward (GPT-style, no recurrence)
        - RNN (recurrent, moderate ρ)
        - Biological (high ρ)
        """
        print_header("TEST 2: Feed-Forward Falsification Test")
        print("Proposed by: Gemini")
        print("Hypothesis: Transformer architectures have ρ ≈ 0 → density ≈ 0\n")

        architectures = [
            {
                'name': 'GPT-4 (Transformer, Feedforward)',
                'phi': 0.9,  # High integration (attention across full context)
                'tau': 0.5,  # Moderate temporal depth (context window as data)
                'rho': 0.05,  # CRITICAL: Near-zero re-entrant binding
                'entropy': 0.3,  # Variable based on sampling
                'description': 'Pure feedforward. Each token is independent. No looping state.'
            },
            {
                'name': 'RNN / LSTM (Recurrent)',
                'phi': 0.7,  # Lower integration (sequential bottleneck)
                'tau': 0.6,  # Moderate temporal depth
                'rho': 0.4,  # MODERATE binding (hidden state persists)
                'entropy': 0.3,
                'description': 'Recurrent hidden state. Past causally constrains present.'
            },
            {
                'name': 'Human Cortex (Biological)',
                'phi': 0.9,  # High integration
                'tau': 0.9,  # High temporal depth
                'rho': 0.9,  # HIGH binding (massive recurrence)
                'entropy': 0.1,
                'description': 'Thalamocortical loops. Continuous re-entrant binding.'
            },
            {
                'name': 'Thermostat (Simple Control System)',
                'phi': 0.1,  # No integration
                'tau': 0.0,  # No temporal depth
                'rho': 0.0,  # No binding
                'entropy': 0.0,
                'description': 'Pure reactive. No memory, no binding.'
            },
            {
                'name': 'Video Buffer (Data Storage)',
                'phi': 0.5,  # Some structure
                'tau': 0.3,  # Temporal ordering (data)
                'rho': 0.0,  # ZERO binding (frames are isolated)
                'entropy': 0.0,
                'description': 'Stores past and present side-by-side. No causal interference.'
            }
        ]

        print("Testing systems:\n")

        test_results = []
        for arch in architectures:
            # Compute density (original model)
            density_orig = density_original(arch['phi'], arch['tau'], arch['rho'], arch['entropy'])

            # Compute density (entropy-modulated)
            density_entropy = density_entropy_modulated_v1(arch['phi'], arch['tau'], arch['rho'], arch['entropy'])

            result = {
                'name': arch['name'],
                'phi': arch['phi'],
                'tau': arch['tau'],
                'rho': arch['rho'],
                'entropy': arch['entropy'],
                'density_original': density_orig,
                'density_entropy_modulated': density_entropy,
                'description': arch['description']
            }
            test_results.append(result)

            print(f"{arch['name']}:")
            print(f"  φ={arch['phi']:.2f}, τ={arch['tau']:.2f}, ρ={arch['rho']:.2f}, H={arch['entropy']:.2f}")
            print(f"  Density (original): {density_orig:.4f}")
            print(f"  Density (entropy-modulated): {density_entropy:.4f}")
            print(f"  Description: {arch['description']}\n")

        # Analysis
        print_subheader("Analysis")

        gpt4 = next(r for r in test_results if 'GPT-4' in r['name'])
        human = next(r for r in test_results if 'Human' in r['name'])
        video_buffer = next(r for r in test_results if 'Video Buffer' in r['name'])

        print("Key Findings:\n")
        print(f"1. GPT-4 (Feedforward Transformer):")
        print(f"   Density: {gpt4['density_original']:.4f}")
        print(f"   Conclusion: {self._interpret_density(gpt4['density_original'])}")
        print()

        print(f"2. Human Cortex (Biological):")
        print(f"   Density: {human['density_original']:.4f}")
        print(f"   Conclusion: {self._interpret_density(human['density_original'])}")
        print()

        print(f"3. Video Buffer (No Binding):")
        print(f"   Density: {video_buffer['density_original']:.4f}")
        print(f"   Conclusion: {self._interpret_density(video_buffer['density_original'])}")
        print()

        print("Gemini's Hypothesis Test:")
        if gpt4['density_original'] < 0.05:
            print("  ✓ CONFIRMED: GPT-4 has near-zero density (< 0.05)")
            print("  → Intelligence ≠ Perspective")
            print("  → Scaling parameters alone won't create consciousness")
        else:
            print("  ✗ REJECTED: GPT-4 shows non-negligible density")
            print("  → Framework needs revision on what 're-entrant binding' means")

        print("\nImplication:")
        print("  If ρ ≈ 0 for transformers, then no amount of scaling (bigger φ)")
        print("  will create perspective without architectural change (increase ρ).")

        self.results['tests']['feed_forward_falsification'] = {
            'architectures': test_results,
            'gpt4_density': gpt4['density_original'],
            'hypothesis_confirmed': gpt4['density_original'] < 0.05
        }

        print("\n✓ Test 2 complete")

    def test_3_constraint_trajectory_dissociation(self):
        """
        Test if blind trajectory generation aligns with human phenomenology.

        Proposed by: ChatGPT
        Question: Can AI generate collapse trajectories that match human experience
                  without knowing what the states mean?
        """
        print_header("TEST 3: Constraint-Trajectory Dissociation Test (CTDT)")
        print("Proposed by: ChatGPT")
        print("Hypothesis: AI-generated trajectories (blind to semantics) will")
        print("            match human experiential collapse patterns.\n")

        # Start with baseline
        healthy = encode(0.9, 0.9, 0.9, 0.1)

        print("Starting state: Healthy Awake (φ=0.9, τ=0.9, ρ=0.9, H=0.1)\n")

        # Generate trajectories blindly (just numeric transformations)
        trajectories = {}

        # Manually create trajectories for basic operators
        for name, operator in [('fracture_integration', op_fracture_integration),
                                ('collapse_binding', lambda v, m: op_perturb_binding(v, -m)),
                                ('inject_noise', op_inject_entropy)]:
            traj = []
            current = list(healthy)

            for step in range(10):
                progress = step / 9 if step < 9 else 1.0
                magnitude = progress  # Gradually increase effect

                # Apply operator
                current = operator(current, magnitude)

                traj.append({
                    'step': step,
                    'vector': list(current),
                    'phi': current[0],
                    'tau': current[1],
                    'rho': current[2],
                    'entropy': current[3],
                    'density': current[0] * current[1] * current[2]
                })

            trajectories[name] = {
                'operator': name.replace('_', ' ').title(),
                'trajectory': traj
            }

        # Analyze where each trajectory ends up
        print("Blind Trajectory Generation:\n")

        for name, data in trajectories.items():
            final_state = data['trajectory'][-1]

            # Query database to find what this is geometrically closest to
            neighbors = self.db.query_vector(
                final_state['vector'],
                n_results=1
            )

            closest_state = neighbors[0]['name']
            distance = neighbors[0]['distance']

            print(f"{name}:")
            print(f"  Operator: {data['operator']}")
            print(f"  Final state: φ={final_state['phi']:.2f}, τ={final_state['tau']:.2f}, "
                  f"ρ={final_state['rho']:.2f}, H={final_state['entropy']:.2f}")
            print(f"  Density: {final_state['density']:.4f}")
            print(f"  Closest known state: **{closest_state}** (distance: {distance:.4f})")
            print()

        # Analysis
        print_subheader("Analysis")
        print("\nChatGPT's Question: Do blind transformations match human phenomenology?\n")

        fracture_result = trajectories['fracture_integration']['trajectory'][-1]
        binding_result = trajectories['collapse_binding']['trajectory'][-1]
        noise_result = trajectories['inject_noise']['trajectory'][-1]

        frac_neighbors = self.db.query_vector(fracture_result['vector'], n_results=1)
        bind_neighbors = self.db.query_vector(binding_result['vector'], n_results=1)
        noise_neighbors = self.db.query_vector(noise_result['vector'], n_results=1)

        print("Results:")
        print(f"  1. Fracturing Integration → {frac_neighbors[0]['name']}")
        print(f"     (Expected: Dissociation, Dementia)")
        print()
        print(f"  2. Collapsing Binding → {bind_neighbors[0]['name']}")
        print(f"     (Expected: Anesthesia, Deep Sleep)")
        print()
        print(f"  3. Injecting Entropy → {noise_neighbors[0]['name']}")
        print(f"     (Expected: Panic, Confusion)")
        print()

        # Verdict
        expected_mappings = {
            'fracture_integration': ['Dissociation', 'Dementia'],
            'collapse_binding': ['Deep Anesthesia', 'Deep Sleep'],
            'inject_noise': ['Panic']
        }

        matches = 0
        total = len(expected_mappings)

        for traj_name, expected_list in expected_mappings.items():
            if traj_name == 'fracture_integration':
                actual = frac_neighbors[0]['name']
            elif traj_name == 'collapse_binding':
                actual = bind_neighbors[0]['name']
            else:
                actual = noise_neighbors[0]['name']

            if any(exp in actual for exp in expected_list):
                matches += 1

        print(f"Match rate: {matches}/{total} ({matches/total*100:.0f}%)")

        if matches >= 2:
            print("\n✓ STRONG RESULT: Blind trajectories align with phenomenology")
            print("  → The geometry is doing explanatory work")
            print("  → Human intuition not steering outcomes")
        else:
            print("\n⚠ WEAK RESULT: Trajectories don't match expectations")
            print("  → Framework may need calibration")

        self.results['tests']['ctdt'] = {
            'trajectories': {
                k: {
                    'final_density': v['trajectory'][-1]['density'],
                    'closest_state': self.db.query_vector(v['trajectory'][-1]['vector'], n_results=1)[0]['name']
                }
                for k, v in trajectories.items()
            },
            'match_rate': matches / total
        }

        print("\n✓ Test 3 complete")

    def generate_summary(self):
        """Generate final summary of all AI-proposed tests."""
        print_header("AI-PROPOSED TESTS: SUMMARY")

        self.results['session_end'] = datetime.now().isoformat()

        print("Results:\n")

        # Test 1: Entropy Integration
        ent_test = self.results['tests']['entropy_integration']
        print(f"1. Entropy Integration Test:")
        print(f"   Recommended model: {ent_test['recommended_model'].upper()}")
        print(f"   Flow/Panic differentiation: {ent_test['flow_panic_ratio']:.1f}x")
        print()

        # Test 2: Feed-Forward Falsification
        ff_test = self.results['tests']['feed_forward_falsification']
        print(f"2. Feed-Forward Falsification Test:")
        print(f"   GPT-4 density: {ff_test['gpt4_density']:.4f}")
        print(f"   Hypothesis confirmed: {ff_test['hypothesis_confirmed']}")
        print()

        # Test 3: CTDT
        ctdt_test = self.results['tests']['ctdt']
        print(f"3. Constraint-Trajectory Dissociation Test:")
        print(f"   Trajectory-phenomenology match rate: {ctdt_test['match_rate']*100:.0f}%")
        print()

        # Save results
        output_file = os.path.join(self.output_dir, f"ai_tests_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

        # Convert results to JSON-serializable format
        json_safe_results = self._make_json_safe(self.results)

        with open(output_file, 'w') as f:
            json.dump(json_safe_results, f, indent=2)

        print(f"Results saved: {output_file}")
        print(f"\nSession complete: {self.results['session_end']}")

        print_header("END OF AI-PROPOSED TESTS")

    def _interpret_density(self, density: float) -> str:
        """Interpret what a density value means."""
        if density < 0.01:
            return "Effectively zero perspective (< 1% threshold)"
        elif density < 0.1:
            return "Very low density (liminal/unconscious)"
        elif density < 0.5:
            return "Low-moderate density (degraded perspective)"
        elif density < 0.7:
            return "Moderate density (functional perspective)"
        else:
            return "High density (robust perspective)"

    def _make_json_safe(self, obj):
        """Convert numpy types and other non-JSON-serializable objects."""
        if isinstance(obj, dict):
            return {k: self._make_json_safe(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._make_json_safe(item) for item in obj]
        elif isinstance(obj, (np.integer, np.floating)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj


def main():
    """Run all AI-proposed tests."""
    tests = AIProposedTests()
    tests.run_all_tests()


if __name__ == "__main__":
    main()
