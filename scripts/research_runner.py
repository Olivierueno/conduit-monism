#!/usr/bin/env python3
"""
Research Runner - Conduit Engine v0.1
=====================================

Comprehensive R&D suite for Conduit Monism v7.0.

This script runs all experiments, tests hypotheses, generates visualizations,
and documents findings.

Usage:
    python research_runner.py
"""

import os
import json
from datetime import datetime
from src.database import ConduitDB
from src.encoder import encode
from src.analysis import (
    analyze_asymptotic_behavior,
    find_critical_threshold,
    test_multiplicative_hypothesis,
    gradient_comparison,
    analyze_liminal_states
)
from src.advanced_operators import (
    op_dementia_progression,
    op_split_brain,
    op_anesthesia_gradient,
    op_locked_in_syndrome,
    op_flow_state_induction,
    op_panic_induction,
    simulate_trajectory
)
from src.visualization import (
    plot_asymptotic_curve,
    plot_gradient_comparison,
    plot_3d_state_space,
    plot_trajectory,
    plot_liminal_states_comparison,
    print_text_visualization,
    VISUALIZATION_AVAILABLE
)


def print_header(title: str):
    """Print a formatted section header."""
    print("\n" + "="*80)
    print(title.center(80))
    print("="*80 + "\n")


def print_subheader(title: str):
    """Print a formatted subsection header."""
    print("\n" + "-"*80)
    print(title)
    print("-"*80)


def save_results(results: dict, filename: str):
    """Save results to JSON file."""
    output_dir = "./research_output"
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Results saved: {filepath}")


class ResearchSession:
    """
    Manages a complete research session.
    """

    def __init__(self):
        self.db = ConduitDB()
        self.results = {
            'session_start': datetime.now().isoformat(),
            'experiments': {}
        }
        self.output_dir = "./research_output"
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "visualizations"), exist_ok=True)

    def run_all_experiments(self):
        """Run the complete R&D suite."""
        print_header("CONDUIT MONISM v7.0 - RESEARCH & DEVELOPMENT SUITE")
        print(f"Session started: {self.results['session_start']}")
        print(f"Database state count: {self.db.count()}")

        # Experiment 1: Asymptotic Analysis
        self.experiment_1_asymptotic_analysis()

        # Experiment 2: Multiplicative Hypothesis Test
        self.experiment_2_multiplicative_test()

        # Experiment 3: Critical Threshold Discovery
        self.experiment_3_critical_threshold()

        # Experiment 4: Liminal States Analysis
        self.experiment_4_liminal_states()

        # Experiment 5: Trajectory Simulations
        self.experiment_5_trajectories()

        # Experiment 6: Gradient Comparison
        self.experiment_6_gradient_comparison()

        # Final summary
        self.generate_summary()

    def experiment_1_asymptotic_analysis(self):
        """Test the asymptotic behavior of the multiplicative relationship."""
        print_header("EXPERIMENT 1: Asymptotic Behavior Analysis")

        print("Testing the core claim:")
        print("'The three conditions are not merely additive; they are multiplicative.'")
        print("\nGenerating asymptotic curves...")

        data = analyze_asymptotic_behavior(resolution=100)

        print(f"\nResults:")
        print(f"  φ range: {data['phi_range'][0]:.2f} to {data['phi_range'][-1]:.2f}")
        print(f"  Fixed: τ={data['tau_fixed']}, ρ={data['rho_fixed']}")
        print(f"  Multiplicative density at φ=0.01: {data['multiplicative'][0]:.6f}")
        print(f"  Additive density at φ=0.01: {data['additive'][0]:.6f}")
        print(f"\nMultiplicative approaches zero asymptotically: {data['multiplicative'][0] < 0.001}")
        print(f"Additive remains high even at low φ: {data['additive'][0] > 0.3}")

        # Visualize
        if VISUALIZATION_AVAILABLE:
            plot_asymptotic_curve(
                data,
                save_path=os.path.join(self.output_dir, "visualizations", "asymptotic_curve.png")
            )

        self.results['experiments']['asymptotic_analysis'] = {
            'phi_min_multiplicative_density': float(data['multiplicative'][0]),
            'phi_min_additive_density': float(data['additive'][0]),
            'asymptotic_behavior_confirmed': data['multiplicative'][0] < 0.001
        }

        print("\n✓ Experiment 1 complete")

    def experiment_2_multiplicative_test(self):
        """Test the multiplicative hypothesis with specific cases."""
        print_header("EXPERIMENT 2: Multiplicative Hypothesis Test")

        print("Testing specific cases from the framework...")

        results = test_multiplicative_hypothesis()

        print(f"\nHypothesis supported: {results['hypothesis_supported']}\n")

        for case in results['test_cases']:
            print(f"{case['name']}:")
            print(f"  State: φ={case['phi']}, τ={case['tau']}, ρ={case['rho']}")
            print(f"  Multiplicative density: {case['multiplicative_density']:.4f}")
            print(f"  Additive density: {case['additive_density']:.4f}")
            print(f"  Expected: {case['expected']}")
            print(f"  Matches theory: {case['multiplicative_matches_theory']}\n")

        self.results['experiments']['multiplicative_hypothesis'] = results

        print("✓ Experiment 2 complete")

    def experiment_3_critical_threshold(self):
        """Find the critical threshold where perspective becomes meaningless."""
        print_header("EXPERIMENT 3: Critical Threshold Discovery")

        print("Searching for the threshold where perspectival density becomes 'meaningless'...")
        print("Per Section VIII: 'Does the asymptotic curve ever truly hit zero?'\n")

        thresholds = find_critical_threshold(epsilon=0.01, fixed_high=0.9)

        print(f"Epsilon (threshold): {thresholds['epsilon']}")
        print(f"\nCritical thresholds (with other variables at 0.9):")
        print(f"  φ_critical: {thresholds['phi_critical']:.6f}")
        print(f"  τ_critical: {thresholds['tau_critical']:.6f}")
        print(f"  ρ_critical: {thresholds['rho_critical']:.6f}")
        print(f"\n{thresholds['interpretation']}")

        self.results['experiments']['critical_threshold'] = thresholds

        print("\n✓ Experiment 3 complete")

    def experiment_4_liminal_states(self):
        """Analyze the liminal states from the database."""
        print_header("EXPERIMENT 4: Liminal States Analysis")

        print("Analyzing seeded liminal states from Section III...")

        analysis = analyze_liminal_states(self.db)

        print(f"\nStates analyzed: {len(analysis['states'])}")
        print(f"Density range: {analysis['density_range'][0]:.4f} to {analysis['density_range'][1]:.4f}")

        if analysis['highest_density']:
            print(f"\nHighest density: {analysis['highest_density']['name']}")
            print(f"  Density: {analysis['highest_density']['density']:.4f}")

        if analysis['lowest_density']:
            print(f"\nLowest density: {analysis['lowest_density']['name']}")
            print(f"  Density: {analysis['lowest_density']['density']:.4f}")

        print("\nAll states:")
        for state in analysis['states']:
            print(f"  {state['name']:<20} | φ={state['phi']:.2f} τ={state['tau']:.2f} "
                  f"ρ={state['rho']:.2f} H={state['entropy']:.2f} | "
                  f"Density={state['density']:.4f}")

        # Visualizations
        if VISUALIZATION_AVAILABLE:
            plot_3d_state_space(
                analysis['states'],
                save_path=os.path.join(self.output_dir, "visualizations", "state_space_3d.png")
            )
            plot_liminal_states_comparison(
                analysis['states'],
                save_path=os.path.join(self.output_dir, "visualizations", "liminal_states_comparison.png")
            )
        else:
            print_text_visualization(analysis['states'])

        self.results['experiments']['liminal_states'] = analysis

        print("\n✓ Experiment 4 complete")

    def experiment_5_trajectories(self):
        """Simulate trajectories through state space using advanced operators."""
        print_header("EXPERIMENT 5: Trajectory Simulations")

        print("Simulating state transformations using advanced operators...\n")

        # Starting state: Healthy Awake
        healthy = encode(0.9, 0.9, 0.9, 0.1)

        # Trajectory 1: Dementia progression
        print_subheader("Trajectory 1: Dementia Progression")
        dementia_traj = simulate_trajectory(
            healthy, op_dementia_progression, steps=10
        )
        print(f"Initial density: {dementia_traj[0]['density']:.4f}")
        print(f"Final density: {dementia_traj[-1]['density']:.4f}")
        print(f"Density reduction: {(1 - dementia_traj[-1]['density']/dementia_traj[0]['density'])*100:.1f}%")

        if VISUALIZATION_AVAILABLE:
            plot_trajectory(
                dementia_traj,
                title="Trajectory: Dementia Progression",
                save_path=os.path.join(self.output_dir, "visualizations", "trajectory_dementia.png")
            )

        # Trajectory 2: Anesthesia gradient
        print_subheader("Trajectory 2: Anesthesia Gradient")
        anesthesia_traj = simulate_trajectory(
            healthy, op_anesthesia_gradient, steps=10
        )
        print(f"Initial density: {anesthesia_traj[0]['density']:.4f}")
        print(f"Final density: {anesthesia_traj[-1]['density']:.6f}")
        print(f"Approaches asymptotic zero: {anesthesia_traj[-1]['density'] < 0.001}")

        if VISUALIZATION_AVAILABLE:
            plot_trajectory(
                anesthesia_traj,
                title="Trajectory: Anesthesia Gradient",
                save_path=os.path.join(self.output_dir, "visualizations", "trajectory_anesthesia.png")
            )

        # Trajectory 3: Flow state induction
        print_subheader("Trajectory 3: Flow State Induction")
        baseline = encode(0.7, 0.7, 0.7, 0.4)
        flow_traj = simulate_trajectory(
            baseline, op_flow_state_induction, steps=10
        )
        print(f"Initial density: {flow_traj[0]['density']:.4f}")
        print(f"Final density: {flow_traj[-1]['density']:.4f}")
        print(f"Density increase: {(flow_traj[-1]['density']/flow_traj[0]['density'] - 1)*100:.1f}%")

        if VISUALIZATION_AVAILABLE:
            plot_trajectory(
                flow_traj,
                title="Trajectory: Flow State Induction",
                save_path=os.path.join(self.output_dir, "visualizations", "trajectory_flow.png")
            )

        # Trajectory 4: Panic induction
        print_subheader("Trajectory 4: Panic Attack")
        panic_traj = simulate_trajectory(
            healthy, op_panic_induction, steps=10
        )
        print(f"Initial density: {panic_traj[0]['density']:.4f}")
        print(f"Final density: {panic_traj[-1]['density']:.4f}")
        print(f"Final entropy: {panic_traj[-1]['entropy']:.4f}")

        if VISUALIZATION_AVAILABLE:
            plot_trajectory(
                panic_traj,
                title="Trajectory: Panic Attack",
                save_path=os.path.join(self.output_dir, "visualizations", "trajectory_panic.png")
            )

        self.results['experiments']['trajectories'] = {
            'dementia': {
                'initial_density': dementia_traj[0]['density'],
                'final_density': dementia_traj[-1]['density']
            },
            'anesthesia': {
                'initial_density': anesthesia_traj[0]['density'],
                'final_density': anesthesia_traj[-1]['density'],
                'asymptotic': anesthesia_traj[-1]['density'] < 0.001
            },
            'flow': {
                'initial_density': flow_traj[0]['density'],
                'final_density': flow_traj[-1]['density']
            },
            'panic': {
                'initial_density': panic_traj[0]['density'],
                'final_density': panic_traj[-1]['density'],
                'final_entropy': panic_traj[-1]['entropy']
            }
        }

        print("\n✓ Experiment 5 complete")

    def experiment_6_gradient_comparison(self):
        """Compare gradients for each variable."""
        print_header("EXPERIMENT 6: Gradient Comparison")

        print("Comparing how each variable affects perspectival density...\n")

        for var in ['phi', 'tau', 'rho']:
            print(f"\nAnalyzing {var} gradient...")
            data = gradient_comparison(var)

            min_density = data['densities'][0]
            max_density = data['densities'][-1]

            print(f"  Range: {min_density:.4f} to {max_density:.4f}")

            if VISUALIZATION_AVAILABLE:
                plot_gradient_comparison(
                    data,
                    save_path=os.path.join(
                        self.output_dir,
                        "visualizations",
                        f"gradient_{var}.png"
                    )
                )

        print("\n✓ Experiment 6 complete")

    def generate_summary(self):
        """Generate final research summary."""
        print_header("RESEARCH SESSION SUMMARY")

        self.results['session_end'] = datetime.now().isoformat()

        print("Key Findings:\n")

        # Finding 1: Multiplicative behavior
        mult_result = self.results['experiments']['multiplicative_hypothesis']
        print(f"1. Multiplicative Hypothesis: {'SUPPORTED' if mult_result['hypothesis_supported'] else 'REJECTED'}")

        # Finding 2: Asymptotic behavior
        asymp_result = self.results['experiments']['asymptotic_analysis']
        print(f"2. Asymptotic Behavior: {'CONFIRMED' if asymp_result['asymptotic_behavior_confirmed'] else 'REJECTED'}")

        # Finding 3: Critical threshold
        threshold = self.results['experiments']['critical_threshold']
        print(f"3. Critical Threshold: φ, τ, or ρ < {threshold['phi_critical']:.6f} → density < 1%")

        # Finding 4: Liminal state range
        liminal = self.results['experiments']['liminal_states']
        density_range = liminal['density_range']
        print(f"4. Liminal State Range: {density_range[0]:.4f} to {density_range[1]:.4f}")

        # Finding 5: Anesthesia trajectory
        anesthesia = self.results['experiments']['trajectories']['anesthesia']
        print(f"5. Anesthesia Gradient: Asymptotic zero achieved: {anesthesia['asymptotic']}")

        # Save full results
        save_results(self.results, f"research_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

        print(f"\nVisualization output: {self.output_dir}/visualizations/")
        print(f"Session complete: {self.results['session_end']}")

        print_header("END OF RESEARCH SESSION")


def main():
    """Run the complete R&D suite."""
    session = ResearchSession()
    session.run_all_experiments()


if __name__ == "__main__":
    main()
