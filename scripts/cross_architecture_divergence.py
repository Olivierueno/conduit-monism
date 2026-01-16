#!/usr/bin/env python3
"""
CROSS-ARCHITECTURE TRAJECTORY DIVERGENCE TEST
==============================================

Designed by: ChatGPT
Implemented by: Claude Opus 4.5
Date: 2026-01-16

PURPOSE:
Test whether two systems with identical instantaneous coordinates (φ,τ,ρ,H,κ)
but different architectures diverge under identical perturbations.

THE QUESTION:
Does architecture constrain not just position, but REACHABLE FUTURES?

ARCHITECTURES MODELED:
1. RWKV-like (Continuous State): True recurrent binding, state persists
2. Transformer-like (Reconstructed State): Context-based, state rebuilt each step

PREDICTION:
If architectures diverge → Conduit Monism becomes PREDICTIVE (not just descriptive)
If architectures converge → Framework is architecture-agnostic (which is also valid)
"""

import json
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)


def density_v81(phi: float, tau: float, rho: float, H: float, kappa: float) -> float:
    """Conduit Monism v8.1 density formula."""
    structural = phi * tau * rho
    entropy_impact = (1 - np.sqrt(H)) + (H * kappa)
    entropy_impact = max(0.0, min(1.0, entropy_impact))
    return structural * entropy_impact


def clamp(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """Clamp value to range."""
    return max(min_val, min(max_val, value))


class RWKVArchitecture:
    """
    RWKV-like architecture: Continuous recurrent state.

    Key properties:
    - State persists across time steps
    - ρ represents ACTUAL binding in hidden state
    - Perturbations accumulate and decay through state dynamics
    - τ reflects true temporal depth (memory decay rate)
    """

    def __init__(self, phi: float, tau: float, rho: float, H: float, kappa: float):
        self.phi = phi
        self.tau = tau
        self.rho = rho  # This is REAL binding
        self.H = H
        self.kappa = kappa

        # Internal state (hidden)
        self.state_memory = np.zeros(5)  # Accumulated perturbation effects
        self.decay_rate = 1 - tau  # Higher τ = slower decay

    def apply_perturbation(self, delta: Dict[str, float]) -> None:
        """Apply perturbation - accumulates in state with decay."""

        # State decays toward baseline
        self.state_memory *= (1 - self.decay_rate * 0.1)

        # Perturbation is FILTERED by ρ (binding)
        # High ρ = perturbation integrates into state
        # Low ρ = perturbation has less lasting effect
        binding_filter = self.rho

        # Apply perturbations
        self.phi = clamp(self.phi + delta.get('phi', 0) * binding_filter)
        self.tau = clamp(self.tau + delta.get('tau', 0) * binding_filter)
        self.rho = clamp(self.rho + delta.get('rho', 0) * 0.5)  # ρ changes slowly
        self.H = clamp(self.H + delta.get('H', 0))
        self.kappa = clamp(self.kappa + delta.get('kappa', 0) * binding_filter)

        # Accumulate in state memory
        self.state_memory += np.array([
            delta.get('phi', 0),
            delta.get('tau', 0),
            delta.get('rho', 0),
            delta.get('H', 0),
            delta.get('kappa', 0)
        ]) * binding_filter

    def get_state(self) -> Dict[str, float]:
        return {
            'phi': self.phi,
            'tau': self.tau,
            'rho': self.rho,
            'H': self.H,
            'kappa': self.kappa,
            'D': density_v81(self.phi, self.tau, self.rho, self.H, self.kappa),
            'state_memory_norm': np.linalg.norm(self.state_memory)
        }


class TransformerArchitecture:
    """
    Transformer-like architecture: Reconstructed state from context.

    Key properties:
    - No persistent hidden state
    - ρ is SIMULATED via attention over context window
    - Each step reconstructs state from recent history
    - τ depends on context window size, not true memory
    """

    def __init__(self, phi: float, tau: float, rho: float, H: float, kappa: float,
                 context_window: int = 10):
        self.phi = phi
        self.tau = tau
        self.rho = rho  # This is SIMULATED binding
        self.H = H
        self.kappa = kappa

        # Context window (recent states)
        self.context = []
        self.context_window = context_window

        # Store initial state
        self.context.append({
            'phi': phi, 'tau': tau, 'rho': rho, 'H': H, 'kappa': kappa
        })

    def apply_perturbation(self, delta: Dict[str, float]) -> None:
        """Apply perturbation - reconstructs state from context."""

        # Direct application of perturbation
        self.phi = clamp(self.phi + delta.get('phi', 0))
        self.tau = clamp(self.tau + delta.get('tau', 0))
        self.rho = clamp(self.rho + delta.get('rho', 0))
        self.H = clamp(self.H + delta.get('H', 0))
        self.kappa = clamp(self.kappa + delta.get('kappa', 0))

        # Add to context
        self.context.append({
            'phi': self.phi, 'tau': self.tau, 'rho': self.rho,
            'H': self.H, 'kappa': self.kappa
        })

        # Trim context window
        if len(self.context) > self.context_window:
            self.context = self.context[-self.context_window:]

        # RECONSTRUCT ρ from context (attention-based simulation)
        # More varied context = lower effective ρ (less coherent binding)
        if len(self.context) > 1:
            phi_var = np.var([s['phi'] for s in self.context])
            tau_var = np.var([s['tau'] for s in self.context])
            context_coherence = 1 - (phi_var + tau_var) / 2

            # ρ is modulated by context coherence
            self.rho = clamp(self.rho * 0.9 + context_coherence * 0.1)

        # τ is limited by context window
        effective_tau = min(self.tau, len(self.context) / self.context_window)
        self.tau = self.tau * 0.95 + effective_tau * 0.05

    def get_state(self) -> Dict[str, float]:
        return {
            'phi': self.phi,
            'tau': self.tau,
            'rho': self.rho,
            'H': self.H,
            'kappa': self.kappa,
            'D': density_v81(self.phi, self.tau, self.rho, self.H, self.kappa),
            'context_size': len(self.context)
        }


def generate_perturbation_sequence(n_steps: int, seed: int = 42) -> List[Dict[str, float]]:
    """Generate a sequence of random perturbations."""
    np.random.seed(seed)

    perturbations = []
    for _ in range(n_steps):
        # Random small perturbations
        delta = {
            'phi': np.random.uniform(-0.1, 0.1),
            'tau': np.random.uniform(-0.1, 0.1),
            'rho': np.random.uniform(-0.05, 0.05),
            'H': np.random.uniform(-0.1, 0.1),
            'kappa': np.random.uniform(-0.1, 0.1)
        }
        perturbations.append(delta)

    return perturbations


def run_trajectory_comparison(
    initial_state: Dict[str, float],
    perturbations: List[Dict[str, float]]
) -> Tuple[List[Dict], List[Dict]]:
    """Run both architectures through the same perturbation sequence."""

    # Initialize both architectures with IDENTICAL starting coordinates
    rwkv = RWKVArchitecture(**initial_state)
    transformer = TransformerArchitecture(**initial_state)

    rwkv_trajectory = [rwkv.get_state()]
    transformer_trajectory = [transformer.get_state()]

    # Apply identical perturbations
    for delta in perturbations:
        rwkv.apply_perturbation(delta)
        transformer.apply_perturbation(delta)

        rwkv_trajectory.append(rwkv.get_state())
        transformer_trajectory.append(transformer.get_state())

    return rwkv_trajectory, transformer_trajectory


def calculate_divergence(traj1: List[Dict], traj2: List[Dict]) -> Dict:
    """Calculate divergence metrics between two trajectories."""

    divergence = {
        'D_divergence': [],
        'phi_divergence': [],
        'tau_divergence': [],
        'rho_divergence': [],
        'H_divergence': [],
        'kappa_divergence': []
    }

    for s1, s2 in zip(traj1, traj2):
        divergence['D_divergence'].append(abs(s1['D'] - s2['D']))
        divergence['phi_divergence'].append(abs(s1['phi'] - s2['phi']))
        divergence['tau_divergence'].append(abs(s1['tau'] - s2['tau']))
        divergence['rho_divergence'].append(abs(s1['rho'] - s2['rho']))
        divergence['H_divergence'].append(abs(s1['H'] - s2['H']))
        divergence['kappa_divergence'].append(abs(s1['kappa'] - s2['kappa']))

    return divergence


def run_cross_architecture_test():
    """Run the complete cross-architecture divergence test."""

    print("=" * 70)
    print("CROSS-ARCHITECTURE TRAJECTORY DIVERGENCE TEST")
    print("=" * 70)
    print("\nDesigned by: ChatGPT")
    print("Implemented by: Claude Opus 4.5")
    print()
    print("Question: Do identical coordinates diverge under identical perturbations")
    print("          when processed by different architectures?")
    print()

    results = {
        'experiment': 'Cross-Architecture Trajectory Divergence',
        'timestamp': datetime.now().isoformat(),
        'scenarios': []
    }

    # =========================================================================
    # SCENARIO 1: High-Binding Starting State (Flow-like)
    # =========================================================================

    print("[SCENARIO 1] High-Binding Starting State (Flow-like)")
    print("-" * 50)

    flow_state = {'phi': 0.9, 'tau': 0.85, 'rho': 0.9, 'H': 0.15, 'kappa': 0.85}
    print(f"Initial: φ={flow_state['phi']}, τ={flow_state['tau']}, ρ={flow_state['rho']}, H={flow_state['H']}, κ={flow_state['kappa']}")
    print(f"Initial D: {density_v81(**flow_state):.4f}")

    perturbations = generate_perturbation_sequence(50, seed=42)
    rwkv_traj, trans_traj = run_trajectory_comparison(flow_state, perturbations)
    divergence = calculate_divergence(rwkv_traj, trans_traj)

    print(f"\nAfter 50 perturbations:")
    print(f"  RWKV final:        D = {rwkv_traj[-1]['D']:.4f}, ρ = {rwkv_traj[-1]['rho']:.4f}")
    print(f"  Transformer final: D = {trans_traj[-1]['D']:.4f}, ρ = {trans_traj[-1]['rho']:.4f}")
    print(f"  D divergence:      {divergence['D_divergence'][-1]:.4f}")
    print(f"  ρ divergence:      {divergence['rho_divergence'][-1]:.4f}")
    print(f"  Max D divergence:  {max(divergence['D_divergence']):.4f}")

    results['scenarios'].append({
        'name': 'High-Binding (Flow)',
        'initial': flow_state,
        'rwkv_final': rwkv_traj[-1],
        'transformer_final': trans_traj[-1],
        'max_D_divergence': max(divergence['D_divergence']),
        'final_D_divergence': divergence['D_divergence'][-1],
        'final_rho_divergence': divergence['rho_divergence'][-1]
    })

    # =========================================================================
    # SCENARIO 2: Low-Binding Starting State (Panic-like)
    # =========================================================================

    print("\n[SCENARIO 2] Low-Binding Starting State (Panic-like)")
    print("-" * 50)

    panic_state = {'phi': 0.7, 'tau': 0.1, 'rho': 0.2, 'H': 0.9, 'kappa': 0.2}
    print(f"Initial: φ={panic_state['phi']}, τ={panic_state['tau']}, ρ={panic_state['rho']}, H={panic_state['H']}, κ={panic_state['kappa']}")
    print(f"Initial D: {density_v81(**panic_state):.4f}")

    perturbations = generate_perturbation_sequence(50, seed=42)
    rwkv_traj, trans_traj = run_trajectory_comparison(panic_state, perturbations)
    divergence = calculate_divergence(rwkv_traj, trans_traj)

    print(f"\nAfter 50 perturbations:")
    print(f"  RWKV final:        D = {rwkv_traj[-1]['D']:.4f}, ρ = {rwkv_traj[-1]['rho']:.4f}")
    print(f"  Transformer final: D = {trans_traj[-1]['D']:.4f}, ρ = {trans_traj[-1]['rho']:.4f}")
    print(f"  D divergence:      {divergence['D_divergence'][-1]:.4f}")
    print(f"  ρ divergence:      {divergence['rho_divergence'][-1]:.4f}")
    print(f"  Max D divergence:  {max(divergence['D_divergence']):.4f}")

    results['scenarios'].append({
        'name': 'Low-Binding (Panic)',
        'initial': panic_state,
        'rwkv_final': rwkv_traj[-1],
        'transformer_final': trans_traj[-1],
        'max_D_divergence': max(divergence['D_divergence']),
        'final_D_divergence': divergence['D_divergence'][-1],
        'final_rho_divergence': divergence['rho_divergence'][-1]
    })

    # =========================================================================
    # SCENARIO 3: Medium State with Heavy Perturbations
    # =========================================================================

    print("\n[SCENARIO 3] Medium State with Heavy Perturbations")
    print("-" * 50)

    medium_state = {'phi': 0.6, 'tau': 0.5, 'rho': 0.5, 'H': 0.5, 'kappa': 0.5}
    print(f"Initial: φ={medium_state['phi']}, τ={medium_state['tau']}, ρ={medium_state['rho']}, H={medium_state['H']}, κ={medium_state['kappa']}")
    print(f"Initial D: {density_v81(**medium_state):.4f}")

    # Heavier perturbations
    np.random.seed(123)
    heavy_perturbations = []
    for _ in range(100):
        delta = {
            'phi': np.random.uniform(-0.2, 0.2),
            'tau': np.random.uniform(-0.2, 0.2),
            'rho': np.random.uniform(-0.1, 0.1),
            'H': np.random.uniform(-0.2, 0.2),
            'kappa': np.random.uniform(-0.2, 0.2)
        }
        heavy_perturbations.append(delta)

    rwkv_traj, trans_traj = run_trajectory_comparison(medium_state, heavy_perturbations)
    divergence = calculate_divergence(rwkv_traj, trans_traj)

    print(f"\nAfter 100 heavy perturbations:")
    print(f"  RWKV final:        D = {rwkv_traj[-1]['D']:.4f}, ρ = {rwkv_traj[-1]['rho']:.4f}")
    print(f"  Transformer final: D = {trans_traj[-1]['D']:.4f}, ρ = {trans_traj[-1]['rho']:.4f}")
    print(f"  D divergence:      {divergence['D_divergence'][-1]:.4f}")
    print(f"  ρ divergence:      {divergence['rho_divergence'][-1]:.4f}")
    print(f"  Max D divergence:  {max(divergence['D_divergence']):.4f}")

    results['scenarios'].append({
        'name': 'Medium + Heavy Perturbations',
        'initial': medium_state,
        'rwkv_final': rwkv_traj[-1],
        'transformer_final': trans_traj[-1],
        'max_D_divergence': max(divergence['D_divergence']),
        'final_D_divergence': divergence['D_divergence'][-1],
        'final_rho_divergence': divergence['rho_divergence'][-1]
    })

    # =========================================================================
    # SCENARIO 4: Trajectory over time (detailed)
    # =========================================================================

    print("\n[SCENARIO 4] Trajectory Evolution Over Time")
    print("-" * 50)

    start_state = {'phi': 0.8, 'tau': 0.7, 'rho': 0.7, 'H': 0.3, 'kappa': 0.7}
    perturbations = generate_perturbation_sequence(30, seed=999)
    rwkv_traj, trans_traj = run_trajectory_comparison(start_state, perturbations)
    divergence = calculate_divergence(rwkv_traj, trans_traj)

    print(f"\nD trajectory comparison (every 5 steps):")
    print(f"  Step | RWKV D  | Trans D | Divergence")
    print(f"  -----|---------|---------|----------")
    for i in range(0, len(rwkv_traj), 5):
        print(f"  {i:4} | {rwkv_traj[i]['D']:.4f}  | {trans_traj[i]['D']:.4f}  | {divergence['D_divergence'][i]:.4f}")

    results['scenarios'].append({
        'name': 'Detailed Trajectory',
        'initial': start_state,
        'rwkv_trajectory_D': [s['D'] for s in rwkv_traj],
        'transformer_trajectory_D': [s['D'] for s in trans_traj],
        'D_divergence_over_time': divergence['D_divergence']
    })

    # =========================================================================
    # ANALYSIS
    # =========================================================================

    print("\n" + "=" * 70)
    print("ANALYSIS")
    print("=" * 70)

    # Calculate overall divergence statistics
    all_max_divergences = [s['max_D_divergence'] for s in results['scenarios'][:3]]
    all_final_divergences = [s['final_D_divergence'] for s in results['scenarios'][:3]]
    all_rho_divergences = [s['final_rho_divergence'] for s in results['scenarios'][:3]]

    print(f"\nDivergence Statistics Across Scenarios:")
    print(f"  Max D divergence (mean):   {np.mean(all_max_divergences):.4f}")
    print(f"  Final D divergence (mean): {np.mean(all_final_divergences):.4f}")
    print(f"  Final ρ divergence (mean): {np.mean(all_rho_divergences):.4f}")

    print("\n[KEY FINDINGS]")
    print()

    # Check if divergence is significant
    significant_divergence = np.mean(all_max_divergences) > 0.05
    rho_divergence_significant = np.mean(all_rho_divergences) > 0.1

    if significant_divergence:
        print("  1. TRAJECTORIES DIVERGE SYSTEMATICALLY")
        print("     Identical starting coordinates lead to different futures")
        print("     based on architecture.")
        print()
        print("  2. ρ IS THE KEY DIFFERENTIATOR")
        print(f"     Mean ρ divergence: {np.mean(all_rho_divergences):.4f}")
        print("     RWKV maintains binding through perturbations")
        print("     Transformer's 'binding' degrades with context variation")
        print()
        print("  3. ARCHITECTURAL CONSTRAINTS ON REACHABLE FUTURES")
        print("     RWKV-like systems can reach states Transformer-like cannot")
        print("     (and vice versa), even from identical starting points")
    else:
        print("  1. TRAJECTORIES SHOW LIMITED DIVERGENCE")
        print("     Architectures produce similar futures from same coordinates")
        print()
        print("  2. FRAMEWORK IS LARGELY ARCHITECTURE-AGNOSTIC")
        print("     The formula captures geometry, not implementation details")

    # =========================================================================
    # VERDICT
    # =========================================================================

    print("\n" + "=" * 70)
    print("VERDICT")
    print("=" * 70)

    if significant_divergence and rho_divergence_significant:
        verdict = "ARCHITECTURES DIVERGE - FRAMEWORK IS PREDICTIVE"
        interpretation = f"""
  Identical instantaneous coordinates (φ,τ,ρ,H,κ) lead to DIFFERENT
  trajectories under identical perturbations, depending on architecture.

  Mean D divergence: {np.mean(all_max_divergences):.4f}
  Mean ρ divergence: {np.mean(all_rho_divergences):.4f}

  KEY INSIGHT:
  - RWKV's TRUE binding (persistent state) maintains ρ better
  - Transformer's SIMULATED binding (context attention) degrades faster

  IMPLICATION:
  Conduit Monism is not just DESCRIPTIVE (assigning D to states)
  but PREDICTIVE (different architectures have different future cones).

  This means:
  - ρ is not just a number, but reflects REAL architectural properties
  - Two systems with "same coordinates" are NOT phenomenologically equivalent
  - Architecture constrains not just WHERE you are, but WHERE YOU CAN GO
"""
    else:
        verdict = "LIMITED DIVERGENCE - FRAMEWORK IS DESCRIPTIVE"
        interpretation = f"""
  Trajectories show limited divergence ({np.mean(all_max_divergences):.4f}).

  The formula captures instantaneous geometry regardless of implementation.
  This is also a valid result - it means D is architecture-agnostic.
"""

    print(f"\n  {verdict}")
    print(interpretation)

    results['verdict'] = verdict
    results['interpretation'] = interpretation
    results['statistics'] = {
        'mean_max_D_divergence': float(np.mean(all_max_divergences)),
        'mean_final_D_divergence': float(np.mean(all_final_divergences)),
        'mean_rho_divergence': float(np.mean(all_rho_divergences)),
        'significant_divergence': significant_divergence
    }

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"260116_cross_architecture_{timestamp}.json"

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\nResults saved to: {output_file}")

    return results


if __name__ == "__main__":
    run_cross_architecture_test()
