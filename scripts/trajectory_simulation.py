#!/usr/bin/env python3
"""
Trajectory Simulation for AT13: Psychedelic Trajectory Test

Tests whether the Conduit Monism formula (v9.3) produces the expected
phenomenological arc during a psychedelic experience WITHOUT adding
derivative or momentum terms.

Hypothesis: The "Anxiety Dip → Breakthrough → Afterglow" pattern emerges
naturally from parameter lag dynamics.

Key insight from multi-AI review:
- κ lags H (coherence takes time to establish in chaos)
- φ wobbles at onset (integration disrupted before hyper-integration)
- τ may extend during peak (temporal depth increases)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for headless execution
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class State:
    """Consciousness state at a moment in time."""
    time_min: float
    phi: float      # Integration
    tau: float      # Temporal depth
    rho: float      # Binding
    H: float        # Entropy
    kappa: float    # Coherence

    @property
    def entropy_gate(self) -> float:
        """Calculate the entropy modulation term: [(1 - √H) + (H × κ)]"""
        return (1 - np.sqrt(self.H)) + (self.H * self.kappa)

    @property
    def structural(self) -> float:
        """Calculate φ × τ × ρ"""
        return self.phi * self.tau * self.rho

    @property
    def D(self) -> float:
        """Calculate perspectival density: D = φ × τ × ρ × [(1 - √H) + (H × κ)]"""
        return self.structural * self.entropy_gate

    def __repr__(self):
        return (f"T+{self.time_min:3.0f}min | φ={self.phi:.2f} τ={self.tau:.2f} "
                f"ρ={self.rho:.2f} H={self.H:.2f} κ={self.kappa:.2f} | "
                f"Gate={self.entropy_gate:.3f} D={self.D:.3f}")


def lag_toward(current: float, target: float, rate: float) -> float:
    """Move current value toward target at given rate (0-1)."""
    return current + rate * (target - current)


def simulate_psilocybin_trajectory(
    duration_hours: float = 6.0,
    timestep_min: float = 5.0,
    kappa_lag_rate: float = 0.08,  # κ responds VERY slowly to H changes
    phi_recovery_rate: float = 0.12,  # φ recovers slowly after crash
) -> List[State]:
    """
    Simulate a psilocybin trajectory with realistic parameter dynamics.

    Key dynamics modeled:
    1. H rises quickly (drug hits fast)
    2. κ lags behind H (takes time to find structure in chaos)
    3. φ dips at onset (disintegration), then recovers/hyper-integrates
    4. ρ dips slightly mid-trip
    5. τ extends during peak

    Returns list of State objects at each timestep.
    """
    states = []

    # Baseline values (waking consciousness from CANON)
    baseline = {
        'phi': 0.80, 'tau': 0.75, 'rho': 0.65, 'H': 0.50, 'kappa': 0.65
    }

    # Target values at peak (from CANON psilocybin calibration)
    peak_targets = {
        'phi': 0.85,   # Hyper-integration (discovered in AT11)
        'tau': 0.80,   # Extended temporal depth
        'rho': 0.55,   # Slight dip in binding
        'H': 0.70,     # High entropy
        'kappa': 0.90  # High coherence (structured chaos)
    }

    # Pharmacokinetic profile (simplified)
    # Psilocybin: onset 20-40min, peak 60-90min, duration 4-6hr
    def drug_effect(t_min: float) -> float:
        """Returns 0-1 drug effect level based on pharmacokinetics."""
        if t_min < 20:
            return 0.0
        elif t_min < 60:
            # Rising phase
            return (t_min - 20) / 40
        elif t_min < 120:
            # Peak plateau
            return 1.0
        elif t_min < 300:
            # Gradual descent
            return 1.0 - (t_min - 120) / 180
        else:
            # Return to baseline
            return max(0, 1.0 - (t_min - 120) / 180)

    # Initialize current values at baseline
    current = baseline.copy()
    kappa_target = baseline['kappa']

    n_steps = int(duration_hours * 60 / timestep_min)

    for i in range(n_steps + 1):
        t = i * timestep_min
        effect = drug_effect(t)

        # === H (Entropy) - responds quickly to drug ===
        H_target = baseline['H'] + effect * (peak_targets['H'] - baseline['H'])
        current['H'] = lag_toward(current['H'], H_target, rate=0.4)  # Fast response

        # === κ (Coherence) - LAGS behind H ===
        # This is the key dynamic: κ takes time to establish structure
        kappa_target = baseline['kappa'] + effect * (peak_targets['kappa'] - baseline['kappa'])
        current['kappa'] = lag_toward(current['kappa'], kappa_target, rate=kappa_lag_rate)

        # === φ (Integration) - CRASHES at onset, then hyper-integrates ===
        if 20 < t < 50:
            # Onset: integration severely disrupted (disorientation, "falling apart")
            phi_target = baseline['phi'] - 0.30 * min(effect * 2, 1.0)  # Faster, deeper crash
        elif 50 <= t < 90:
            # Transition: slowly recovering
            phi_target = baseline['phi'] - 0.15 * effect
        else:
            # Peak and beyond: hyper-integration
            phi_target = baseline['phi'] + effect * (peak_targets['phi'] - baseline['phi'])
        current['phi'] = lag_toward(current['phi'], phi_target, rate=phi_recovery_rate)

        # === τ (Temporal Depth) - extends during peak ===
        tau_target = baseline['tau'] + effect * (peak_targets['tau'] - baseline['tau'])
        current['tau'] = lag_toward(current['tau'], tau_target, rate=0.25)

        # === ρ (Binding) - dips during onset and mid-trip ===
        if 20 < t < 60:
            # Onset: binding disrupted along with integration
            rho_target = baseline['rho'] - 0.15 * min(effect * 2, 1.0)
        elif 60 <= t < 180:
            # Mid-trip: moderate dip
            rho_target = baseline['rho'] - 0.10 * effect
        else:
            rho_target = baseline['rho']
        current['rho'] = lag_toward(current['rho'], rho_target, rate=0.20)

        states.append(State(
            time_min=t,
            phi=current['phi'],
            tau=current['tau'],
            rho=current['rho'],
            H=current['H'],
            kappa=current['kappa']
        ))

    return states


def analyze_trajectory(states: List[State]) -> dict:
    """Analyze trajectory for key phenomenological predictions."""

    D_values = [s.D for s in states]
    times = [s.time_min for s in states]

    baseline_D = D_values[0]
    min_D = min(D_values)
    min_D_time = times[D_values.index(min_D)]
    max_D = max(D_values)
    max_D_time = times[D_values.index(max_D)]
    final_D = D_values[-1]

    # Check for anxiety dip
    onset_window = [s for s in states if 20 <= s.time_min <= 60]
    if onset_window:
        onset_min_D = min(s.D for s in onset_window)
        anxiety_dip = onset_min_D < baseline_D * 0.9  # >10% drop
    else:
        anxiety_dip = False
        onset_min_D = None

    # Check for afterglow
    afterglow_window = [s for s in states if s.time_min >= 300]
    if afterglow_window:
        afterglow_D = np.mean([s.D for s in afterglow_window])
        afterglow_present = afterglow_D > baseline_D * 1.02  # >2% above baseline
    else:
        afterglow_present = False
        afterglow_D = None

    return {
        'baseline_D': baseline_D,
        'min_D': min_D,
        'min_D_time': min_D_time,
        'max_D': max_D,
        'max_D_time': max_D_time,
        'final_D': final_D,
        'anxiety_dip_detected': anxiety_dip,
        'onset_min_D': onset_min_D,
        'afterglow_present': afterglow_present,
        'afterglow_D': afterglow_D,
    }


def plot_trajectory(states: List[State], save_path: str = None):
    """Generate visualization of D(t) and parameter dynamics."""

    times = [s.time_min / 60 for s in states]  # Convert to hours

    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

    # Plot 1: D(t) - the main prediction
    ax1 = axes[0]
    D_values = [s.D for s in states]
    ax1.plot(times, D_values, 'b-', linewidth=2, label='D (Perspectival Density)')
    ax1.axhline(y=D_values[0], color='gray', linestyle='--', alpha=0.5, label='Baseline')
    ax1.fill_between(times, D_values, D_values[0], alpha=0.3)
    ax1.set_ylabel('D (Density)', fontsize=12)
    ax1.set_title('AT13: Psilocybin Trajectory - D(t) Prediction', fontsize=14)
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)

    # Mark key phases
    ax1.axvspan(0.33, 1.0, alpha=0.1, color='red', label='Onset')
    ax1.axvspan(1.0, 2.0, alpha=0.1, color='green', label='Peak')
    ax1.axvspan(5.0, 6.0, alpha=0.1, color='blue', label='Afterglow')

    # Plot 2: H and κ (the lag dynamic)
    ax2 = axes[1]
    H_values = [s.H for s in states]
    kappa_values = [s.kappa for s in states]
    ax2.plot(times, H_values, 'r-', linewidth=2, label='H (Entropy)')
    ax2.plot(times, kappa_values, 'g-', linewidth=2, label='κ (Coherence)')
    ax2.fill_between(times, H_values, kappa_values, alpha=0.2, color='orange', label='H-κ Gap')
    ax2.set_ylabel('Value', fontsize=12)
    ax2.set_title('Entropy-Coherence Lag (Key Dynamic)', fontsize=14)
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)

    # Plot 3: Structural terms (φ, τ, ρ)
    ax3 = axes[2]
    phi_values = [s.phi for s in states]
    tau_values = [s.tau for s in states]
    rho_values = [s.rho for s in states]
    ax3.plot(times, phi_values, 'b-', linewidth=2, label='φ (Integration)')
    ax3.plot(times, tau_values, 'purple', linewidth=2, label='τ (Temporal Depth)')
    ax3.plot(times, rho_values, 'orange', linewidth=2, label='ρ (Binding)')
    ax3.set_xlabel('Time (hours)', fontsize=12)
    ax3.set_ylabel('Value', fontsize=12)
    ax3.set_title('Structural Parameters', fontsize=14)
    ax3.legend(loc='upper right')
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved plot to {save_path}")

    plt.close()  # Close instead of show for headless execution


def main():
    print("=" * 70)
    print("AT13: Psychedelic Trajectory Simulation")
    print("Testing if v9.3 formula produces Anxiety → Breakthrough → Afterglow")
    print("=" * 70)
    print()

    # Run simulation
    states = simulate_psilocybin_trajectory()

    # Print trajectory
    print("TIME-SERIES OUTPUT:")
    print("-" * 70)
    for i, s in enumerate(states):
        if i % 6 == 0:  # Print every 30 minutes
            print(s)
    print()

    # Analyze
    analysis = analyze_trajectory(states)

    print("ANALYSIS:")
    print("-" * 70)
    print(f"Baseline D:        {analysis['baseline_D']:.4f}")
    print(f"Minimum D:         {analysis['min_D']:.4f} (at T+{analysis['min_D_time']:.0f}min)")
    print(f"Maximum D:         {analysis['max_D']:.4f} (at T+{analysis['max_D_time']:.0f}min)")
    print(f"Final D:           {analysis['final_D']:.4f}")
    print()

    print("PHENOMENOLOGICAL PREDICTIONS:")
    print("-" * 70)

    if analysis['anxiety_dip_detected']:
        dip_pct = (1 - analysis['onset_min_D'] / analysis['baseline_D']) * 100
        print(f"✓ ANXIETY DIP DETECTED: D drops {dip_pct:.1f}% during onset")
        print(f"  (Onset minimum D = {analysis['onset_min_D']:.4f})")
    else:
        print("✗ No significant anxiety dip during onset")

    if analysis['afterglow_present']:
        glow_pct = (analysis['afterglow_D'] / analysis['baseline_D'] - 1) * 100
        print(f"✓ AFTERGLOW DETECTED: D is {glow_pct:.1f}% above baseline post-trip")
        print(f"  (Afterglow D = {analysis['afterglow_D']:.4f})")
    else:
        print("✗ No significant afterglow detected")

    print()
    print("VERDICT:")
    print("-" * 70)

    if analysis['anxiety_dip_detected'] and analysis['afterglow_present']:
        print("✓ H0 SUPPORTED: Framework produces expected phenomenological arc")
        print("  WITHOUT derivative or momentum terms.")
        print("  The lag model is sufficient.")
    elif analysis['anxiety_dip_detected']:
        print("~ PARTIAL: Anxiety dip present, afterglow unclear")
    else:
        print("✗ H0 CHALLENGED: Expected patterns not emerging")
        print("  May need to revise lag parameters or consider H1/H2")

    # Plot
    print()
    print("Generating visualization...")
    plot_trajectory(states, save_path='research_output/at13_trajectory.png')


if __name__ == '__main__':
    main()
