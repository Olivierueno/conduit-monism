"""
Analysis Module - Conduit Engine v0.3

Asymptotic analysis and theoretical validation tools.
Uses the v9.2 density formula: D = φ × τ × ρ × [(1 - √H) + (H × κ)]

Tests the core claims of Conduit Monism:
- Multiplicative vs additive relationships
- Asymptotic thresholds
- Zero-elimination property
- Coherence gate behavior
- Sensitivity analysis
"""

import math
import numpy as np
from typing import Dict, List, Optional
from .encoder import StateVector, compute_density_v92


def perspectival_density(phi: float, tau: float, rho: float,
                         H: float = 0.50, kappa: float = 0.50) -> float:
    """
    Compute perspectival density using v9.2 formula.

    D = φ × τ × ρ × [(1 - √H) + (H × κ)]
    """
    return compute_density_v92(phi, tau, rho, H, kappa)


def perspectival_density_additive(phi: float, tau: float, rho: float,
                                  H: float = 0.50, kappa: float = 0.50) -> float:
    """
    Compute perspectival density using ADDITIVE relationship (null hypothesis).

    If this were true, a system with φ=0, τ=1, ρ=1 would have nonzero density.
    The framework predicts it should be zero (no integration = no perspective).
    """
    structure = (phi + tau + rho) / 3
    entropy_gate = (1 - math.sqrt(H)) + (H * kappa)
    return structure * entropy_gate


def analyze_asymptotic_behavior(
    resolution: int = 50,
    H: float = 0.50,
    kappa: float = 0.50
) -> Dict[str, np.ndarray]:
    """
    Generate gradient analysis from high-density to asymptotic zero.

    Tests whether the multiplicative relationship creates the predicted
    asymptotic curve toward zero.
    """
    phi_range = np.linspace(0.01, 1.0, resolution)
    tau_fixed = 0.9
    rho_fixed = 0.9

    multiplicative = []
    additive = []

    for phi in phi_range:
        mult = perspectival_density(phi, tau_fixed, rho_fixed, H, kappa)
        add = perspectival_density_additive(phi, tau_fixed, rho_fixed, H, kappa)
        multiplicative.append(mult)
        additive.append(add)

    return {
        'phi_range': phi_range,
        'multiplicative': np.array(multiplicative),
        'additive': np.array(additive),
        'tau_fixed': tau_fixed,
        'rho_fixed': rho_fixed,
        'H': H,
        'kappa': kappa
    }


def test_zero_elimination() -> Dict[str, any]:
    """
    Test the zero-elimination property: if any structural invariant
    (φ, τ, ρ) is zero, D must be zero regardless of other values.

    This is the strongest prediction of the multiplicative structure.
    """
    results = []
    high_vals = [0.9, 0.95, 1.0]

    for high in high_vals:
        # Zero φ
        d = perspectival_density(0.0, high, high, 0.5, 0.5)
        results.append({
            'case': f'φ=0, τ={high}, ρ={high}',
            'density': d,
            'is_zero': d == 0.0
        })

        # Zero τ
        d = perspectival_density(high, 0.0, high, 0.5, 0.5)
        results.append({
            'case': f'φ={high}, τ=0, ρ={high}',
            'density': d,
            'is_zero': d == 0.0
        })

        # Zero ρ
        d = perspectival_density(high, high, 0.0, 0.5, 0.5)
        results.append({
            'case': f'φ={high}, τ={high}, ρ=0',
            'density': d,
            'is_zero': d == 0.0
        })

    all_zero = all(r['is_zero'] for r in results)

    return {
        'test_cases': results,
        'zero_elimination_holds': all_zero,
        'n_tests': len(results),
        'n_passed': sum(1 for r in results if r['is_zero'])
    }


def test_coherence_gate() -> Dict[str, any]:
    """
    Test the coherence gate behavior.

    Demonstrates that:
    1. High entropy alone penalizes (low κ)
    2. High entropy + high coherence preserves density (high κ)
    3. The gate correctly handles the DMT paradox
    """
    phi, tau, rho = 0.60, 0.50, 0.50

    cases = [
        ("Low H, Low κ (normal)", 0.30, 0.30),
        ("Low H, High κ (focused)", 0.30, 0.80),
        ("High H, Low κ (panic)", 0.80, 0.20),
        ("High H, High κ (DMT)", 0.80, 0.85),
        ("Max H, Zero κ (pure chaos)", 1.00, 0.00),
        ("Max H, Max κ (max structured chaos)", 1.00, 1.00),
        ("Zero H, Any κ (perfect order)", 0.00, 0.50),
    ]

    results = []
    for name, H, kappa in cases:
        d = perspectival_density(phi, tau, rho, H, kappa)
        structure = phi * tau * rho
        entropy_penalty = 1 - math.sqrt(H)
        coherence_rescue = H * kappa
        entropy_gate = entropy_penalty + coherence_rescue

        results.append({
            'name': name,
            'H': H,
            'kappa': kappa,
            'entropy_penalty': entropy_penalty,
            'coherence_rescue': coherence_rescue,
            'entropy_gate': entropy_gate,
            'D': d
        })

    return {
        'fixed_structure': {'phi': phi, 'tau': tau, 'rho': rho},
        'cases': results,
        'dmt_resolves': (
            results[3]['D'] > results[2]['D']  # DMT > Panic
        )
    }


def sensitivity_analysis(
    base_state: StateVector,
    perturbation: float = 0.05
) -> Dict[str, float]:
    """
    Compute sensitivity of D to small perturbations in each parameter.

    Returns partial derivative approximation for each invariant.
    This reveals which parameters have the most leverage over D.
    """
    base_D = base_state.density()
    sensitivities = {}

    for param in ['phi', 'tau', 'rho', 'H', 'kappa']:
        val = getattr(base_state, param)
        if val + perturbation > 1.0:
            delta = -perturbation
        else:
            delta = perturbation

        perturbed_vals = {
            'phi': base_state.phi,
            'tau': base_state.tau,
            'rho': base_state.rho,
            'H': base_state.H,
            'kappa': base_state.kappa
        }
        perturbed_vals[param] = val + delta
        perturbed = StateVector(**perturbed_vals)
        perturbed_D = perturbed.density()

        sensitivities[param] = (perturbed_D - base_D) / delta

    return sensitivities


def find_fixed_points(resolution: int = 20) -> List[Dict]:
    """
    Search for degenerate regions where different states produce
    identical density values (potential formula weakness).

    Returns pairs of states that have similar D but different topology.
    """
    degeneracies = []
    states = []

    # Generate a grid of states
    for phi in np.linspace(0.1, 0.9, resolution):
        for rho in np.linspace(0.1, 0.9, resolution):
            for H in [0.3, 0.5, 0.7]:
                kappa = 0.5
                tau = 0.5
                d = perspectival_density(phi, tau, rho, H, kappa)
                states.append({
                    'phi': phi, 'tau': tau, 'rho': rho,
                    'H': H, 'kappa': kappa, 'D': d
                })

    # Find pairs with similar D but different topology
    for i in range(len(states)):
        for j in range(i + 1, len(states)):
            s1, s2 = states[i], states[j]
            d_diff = abs(s1['D'] - s2['D'])
            topo_diff = (
                abs(s1['phi'] - s2['phi']) +
                abs(s1['rho'] - s2['rho']) +
                abs(s1['H'] - s2['H'])
            )

            if d_diff < 0.001 and topo_diff > 0.5:
                degeneracies.append({
                    'state1': s1,
                    'state2': s2,
                    'density_diff': d_diff,
                    'topology_diff': topo_diff
                })

    return degeneracies[:20]  # Return top 20


def gradient_comparison(variable: str = 'phi',
                        H: float = 0.50,
                        kappa: float = 0.50) -> Dict[str, np.ndarray]:
    """
    Compare how different variables affect the gradient to zero.

    Parameters:
        variable: Which variable to vary ('phi', 'tau', 'rho', 'H', 'kappa')
        H: Fixed entropy (when not varying H)
        kappa: Fixed coherence (when not varying kappa)
    """
    resolution = 100
    var_range = np.linspace(0.0, 1.0, resolution)
    densities = []

    for val in var_range:
        if variable == 'phi':
            d = perspectival_density(val, 0.9, 0.9, H, kappa)
        elif variable == 'tau':
            d = perspectival_density(0.9, val, 0.9, H, kappa)
        elif variable == 'rho':
            d = perspectival_density(0.9, 0.9, val, H, kappa)
        elif variable == 'H':
            d = perspectival_density(0.9, 0.9, 0.9, val, kappa)
        elif variable == 'kappa':
            d = perspectival_density(0.9, 0.9, 0.9, H, val)
        else:
            raise ValueError(f"Unknown variable: {variable}")

        densities.append(d)

    return {
        'variable': variable,
        'range': var_range,
        'densities': np.array(densities)
    }
