"""
Density Models Module - Conduit Engine v0.2

Implements the v9.2 Conduit Monism density formula:

    D = φ × τ × ρ × [(1 - √H) + (H × κ)]

Where:
    φ (phi)   = Structural Integration
    τ (tau)   = Temporal Depth
    ρ (rho)   = Re-entrant Binding (anchored to PCI)
    H         = Entropy (anchored to LZc)
    κ (kappa) = Coherence (anchored to MSE/Fractal Dimension)

The formula has two components:
1. Structure: φ × τ × ρ (multiplicative - zero in any dimension means zero D)
2. Entropy Gate: [(1 - √H) + (H × κ)] (coherence rescues structured entropy)

Updated: 2026-01-17
- Integrated calibration library (v1.1)
- Added v9.2 formula with coherence gate
- Preserved legacy models for comparison
"""

import math
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple

import numpy as np

# Add calibration to path
CALIBRATION_PATH = Path(__file__).parent.parent / "calibration"
if str(CALIBRATION_PATH) not in sys.path:
    sys.path.insert(0, str(CALIBRATION_PATH))

try:
    from mapping_functions import (
        get_calibrated_states,
        create_grounded_state,
        GroundedState,
        CalibratedValue,
        Confidence,
    )
    CALIBRATION_AVAILABLE = True
except ImportError:
    CALIBRATION_AVAILABLE = False
    print("Warning: Calibration library not available. Using standalone mode.")


# =============================================================================
# v9.2 Density Formula (Current Standard)
# =============================================================================

def density_v92(
    phi: float,
    tau: float,
    rho: float,
    H: float,
    kappa: float
) -> float:
    """
    Compute perspectival density using Conduit Monism v9.2 formula.

    D = φ × τ × ρ × [(1 - √H) + (H × κ)]

    The formula embodies two key insights:
    1. Structure is multiplicative: zero in any structural dimension
       (φ, τ, ρ) means zero consciousness
    2. Entropy is gated by coherence: high entropy can contribute to
       density IF it is structured (high κ)

    Parameters:
    -----------
    phi : float (0.0 - 1.0)
        Structural Integration - system unity
    tau : float (0.0 - 1.0)
        Temporal Depth - the "thick now"
    rho : float (0.0 - 1.0)
        Re-entrant Binding - recursive self-reference (anchored to PCI)
    H : float (0.0 - 1.0)
        Entropy - signal diversity (anchored to LZc)
    kappa : float (0.0 - 1.0)
        Coherence - structure within entropy (anchored to MSE)

    Returns:
    --------
    float: Perspectival density D (0.0 - ~0.15 for typical states)

    Examples:
    ---------
    >>> density_v92(0.80, 0.50, 0.55, 0.50, 0.50)  # Wakefulness
    0.119...
    >>> density_v92(0.20, 0.10, 0.24, 0.35, 0.20)  # Propofol
    0.002...
    >>> density_v92(0.48, 0.25, 0.40, 0.65, 0.75)  # K-hole
    0.033...
    """
    # Validate inputs
    for name, val in [("phi", phi), ("tau", tau), ("rho", rho), ("H", H), ("kappa", kappa)]:
        if not 0.0 <= val <= 1.0:
            raise ValueError(f"{name} must be in range [0.0, 1.0], got {val}")

    # Structure component (multiplicative)
    structure = phi * tau * rho

    # Entropy gate component
    # (1 - √H): High entropy penalizes
    # (H × κ): But coherent entropy partially rescues
    entropy_gate = (1 - math.sqrt(H)) + (H * kappa)

    # Final density
    return structure * entropy_gate


def decompose_density(
    phi: float,
    tau: float,
    rho: float,
    H: float,
    kappa: float
) -> Dict[str, float]:
    """
    Decompose density into its components for analysis.

    Returns:
    --------
    Dict with structure, entropy_penalty, coherence_rescue, entropy_gate, and D
    """
    structure = phi * tau * rho
    entropy_penalty = 1 - math.sqrt(H)
    coherence_rescue = H * kappa
    entropy_gate = entropy_penalty + coherence_rescue
    D = structure * entropy_gate

    return {
        "phi": phi,
        "tau": tau,
        "rho": rho,
        "H": H,
        "kappa": kappa,
        "structure": structure,
        "entropy_penalty": entropy_penalty,
        "coherence_rescue": coherence_rescue,
        "entropy_gate": entropy_gate,
        "D": D
    }


# =============================================================================
# Calibration-Integrated Functions
# =============================================================================

def density_from_state(state_name: str) -> Tuple[float, Dict]:
    """
    Compute density for a pre-calibrated state by name.

    Parameters:
    -----------
    state_name : str
        Name of calibrated state (e.g., 'wakefulness', 'ketamine_anesthesia')

    Returns:
    --------
    Tuple[float, Dict]: (density, full decomposition)

    Raises:
    -------
    ValueError if state not found or calibration not available
    """
    if not CALIBRATION_AVAILABLE:
        raise ValueError("Calibration library not available")

    states = get_calibrated_states()
    if state_name not in states:
        available = list(states.keys())
        raise ValueError(f"State '{state_name}' not found. Available: {available}")

    state = states[state_name]
    decomp = decompose_density(
        state.phi.value,
        state.tau.value,
        state.rho.value,
        state.H.value,
        state.kappa.value
    )

    return decomp["D"], decomp


def compare_states(*state_names: str) -> Dict[str, Dict]:
    """
    Compare multiple calibrated states.

    Parameters:
    -----------
    *state_names : str
        Names of states to compare

    Returns:
    --------
    Dict mapping state names to their decompositions
    """
    if not CALIBRATION_AVAILABLE:
        raise ValueError("Calibration library not available")

    results = {}
    for name in state_names:
        D, decomp = density_from_state(name)
        results[name] = decomp

    return results


def density_ratio(state1: str, state2: str) -> float:
    """
    Calculate density ratio between two calibrated states.

    Useful for comparisons like K-hole vs Propofol.

    Returns:
    --------
    float: D(state1) / D(state2)
    """
    d1, _ = density_from_state(state1)
    d2, _ = density_from_state(state2)

    if d2 == 0:
        return float('inf') if d1 > 0 else 1.0

    return d1 / d2


# =============================================================================
# Legacy Models (Preserved for Comparison)
# =============================================================================

def density_original(phi: float, tau: float, rho: float, entropy: float = 0.0) -> float:
    """
    LEGACY: Original density model from v7.0.

    Density = φ × τ × ρ

    Entropy is not integrated into the calculation.
    Preserved for historical comparison only.
    """
    return phi * tau * rho


def density_entropy_modulated_v1(phi: float, tau: float, rho: float, entropy: float) -> float:
    """
    LEGACY: Entropy-modulated density (linear).

    Density = (φ × τ × ρ) × (1 - H)

    Superseded by v9.2 coherence gate.
    """
    base_density = phi * tau * rho
    entropy_factor = 1.0 - entropy
    return base_density * max(0.0, entropy_factor)


def density_entropy_modulated_v2(phi: float, tau: float, rho: float, entropy: float) -> float:
    """
    LEGACY: Entropy-modulated density (quadratic).

    Density = (φ × τ × ρ) × (1 - H²)

    Superseded by v9.2 coherence gate.
    """
    base_density = phi * tau * rho
    entropy_factor = 1.0 - (entropy ** 2)
    return base_density * max(0.0, entropy_factor)


def density_entropy_modulated_v3(phi: float, tau: float, rho: float, entropy: float) -> float:
    """
    LEGACY: Entropy-modulated density (square root).

    Density = (φ × τ × ρ) × (1 - √H)

    This is the "entropy penalty" term from v9.2, but without
    the coherence rescue. Superseded by full v9.2.
    """
    base_density = phi * tau * rho
    entropy_factor = 1.0 - np.sqrt(entropy)
    return base_density * max(0.0, entropy_factor)


# =============================================================================
# Model Comparison & Testing
# =============================================================================

def compare_all_models(
    phi: float,
    tau: float,
    rho: float,
    H: float,
    kappa: float
) -> Dict[str, float]:
    """
    Compare all density models for a given state.

    Includes both legacy models (for historical comparison)
    and the current v9.2 standard.
    """
    return {
        'v9.2_standard': density_v92(phi, tau, rho, H, kappa),
        'v7_original': density_original(phi, tau, rho),
        'legacy_linear': density_entropy_modulated_v1(phi, tau, rho, H),
        'legacy_quadratic': density_entropy_modulated_v2(phi, tau, rho, H),
        'legacy_sqrt': density_entropy_modulated_v3(phi, tau, rho, H),
        'structure_only': phi * tau * rho,
    }


def run_validation_suite() -> Dict[str, Dict]:
    """
    Run validation against key empirical benchmarks.

    Tests the v9.2 formula against:
    1. Ketamine vs Propofol split (should be >10×)
    2. Wakefulness baseline (~0.12)
    3. Panic Attack vs K-hole (Panic should be higher)
    4. Flow State (should be high)

    Returns validation results.
    """
    if not CALIBRATION_AVAILABLE:
        return {"error": "Calibration library required for validation"}

    results = {}

    # Test 1: Ketamine vs Propofol
    ket_D, _ = density_from_state("ketamine_anesthesia")
    prop_D, _ = density_from_state("propofol_anesthesia")
    ratio = ket_D / prop_D if prop_D > 0 else float('inf')

    results["ketamine_propofol_split"] = {
        "ketamine_D": ket_D,
        "propofol_D": prop_D,
        "ratio": ratio,
        "pass": ratio > 10.0,
        "criterion": "ratio > 10×"
    }

    # Test 2: Wakefulness baseline
    wake_D, _ = density_from_state("wakefulness")
    results["wakefulness_baseline"] = {
        "D": wake_D,
        "pass": 0.10 <= wake_D <= 0.15,
        "criterion": "0.10 ≤ D ≤ 0.15"
    }

    # Test 3: Panic vs K-hole
    panic_D, _ = density_from_state("panic_attack")
    khole_D, _ = density_from_state("ketamine_anesthesia")
    results["panic_khole_ordering"] = {
        "panic_D": panic_D,
        "khole_D": khole_D,
        "pass": panic_D > khole_D,
        "criterion": "Panic D > K-hole D (hyper-conscious > dissociated)"
    }

    # Test 4: Flow State
    flow_D, _ = density_from_state("flow_state")
    results["flow_state"] = {
        "D": flow_D,
        "pass": flow_D > wake_D,
        "criterion": "Flow D > Wakefulness D"
    }

    # Overall
    all_pass = all(r.get("pass", False) for r in results.values())
    results["_overall"] = {
        "all_tests_pass": all_pass,
        "passed": sum(1 for r in results.values() if r.get("pass", False)),
        "total": len([r for r in results.values() if "pass" in r])
    }

    return results


def test_entropy_coherence_gate():
    """
    Test the coherence gate behavior.

    Demonstrates that:
    1. High entropy alone penalizes (low kappa)
    2. High entropy + high coherence preserves density (high kappa)
    """
    # Fixed structure
    phi, tau, rho = 0.60, 0.50, 0.50
    base_structure = phi * tau * rho

    print("=" * 60)
    print("ENTROPY-COHERENCE GATE TEST")
    print(f"Fixed structure: φ={phi}, τ={tau}, ρ={rho}")
    print(f"Base structure product: {base_structure:.4f}")
    print("=" * 60)
    print()

    test_cases = [
        ("Low H, Low κ (normal)", 0.30, 0.30),
        ("Low H, High κ (focused)", 0.30, 0.80),
        ("High H, Low κ (chaos/panic)", 0.80, 0.20),
        ("High H, High κ (structured/DMT)", 0.80, 0.85),
    ]

    for name, H, kappa in test_cases:
        D = density_v92(phi, tau, rho, H, kappa)
        decomp = decompose_density(phi, tau, rho, H, kappa)
        print(f"{name}:")
        print(f"  H={H:.2f}, κ={kappa:.2f}")
        print(f"  Entropy penalty: {decomp['entropy_penalty']:.3f}")
        print(f"  Coherence rescue: {decomp['coherence_rescue']:.3f}")
        print(f"  Entropy gate: {decomp['entropy_gate']:.3f}")
        print(f"  Final D: {D:.4f}")
        print()


# =============================================================================
# Main Execution
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("CONDUIT MONISM v9.2 - DENSITY MODELS")
    print("=" * 60)
    print()

    # Run entropy-coherence gate test
    test_entropy_coherence_gate()

    # Run validation suite if calibration available
    if CALIBRATION_AVAILABLE:
        print("=" * 60)
        print("VALIDATION SUITE")
        print("=" * 60)
        print()

        results = run_validation_suite()
        for test_name, test_result in results.items():
            if test_name.startswith("_"):
                continue
            status = "PASS" if test_result.get("pass") else "FAIL"
            print(f"{test_name}: {status}")
            for k, v in test_result.items():
                if k not in ["pass"]:
                    print(f"  {k}: {v}")
            print()

        overall = results["_overall"]
        print(f"Overall: {overall['passed']}/{overall['total']} tests passed")
    else:
        print("Calibration library not available. Skipping validation suite.")
