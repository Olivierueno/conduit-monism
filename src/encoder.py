"""
Encoder Module - Conduit Engine v0.2

Strictly structural encoding following Conduit Monism v9.2 principles.
Encodes the five sanctioned invariants: φ, τ, ρ, H, κ

NON-NEGOTIABLE: No semantic primitives (valence, self-model, emotion labels)
These must emerge from the geometry, not be hard-coded.

Updated: 2026-01-17
- Added κ (kappa) for coherence (v9.2)
- Integrated with calibration library
- Added v9.2 density computation
"""

import math
import sys
from pathlib import Path
from typing import List, Optional, Dict, Tuple
from dataclasses import dataclass

# Add calibration to path
CALIBRATION_PATH = Path(__file__).parent.parent / "calibration"
if str(CALIBRATION_PATH) not in sys.path:
    sys.path.insert(0, str(CALIBRATION_PATH))

try:
    from mapping_functions import get_calibrated_states, GroundedState
    CALIBRATION_AVAILABLE = True
except ImportError:
    CALIBRATION_AVAILABLE = False


@dataclass
class StateVector:
    """
    A v9.2 consciousness state encoded as structural topology.

    Attributes:
        phi: Structural Integration (0-1)
        tau: Temporal Depth (0-1)
        rho: Re-entrant Binding (0-1, anchored to PCI)
        H: Entropy (0-1, anchored to LZc)
        kappa: Coherence (0-1, anchored to MSE)
        name: Optional state name
        confidence: Optional confidence level
    """
    phi: float
    tau: float
    rho: float
    H: float
    kappa: float
    name: Optional[str] = None
    confidence: Optional[str] = None

    def __post_init__(self):
        """Validate all parameters are in range."""
        for name, val in [("phi", self.phi), ("tau", self.tau),
                          ("rho", self.rho), ("H", self.H), ("kappa", self.kappa)]:
            if not 0.0 <= val <= 1.0:
                raise ValueError(f"{name} must be in range [0.0, 1.0], got {val}")

    def to_vector(self) -> List[float]:
        """Convert to 5D vector for database storage."""
        return [self.phi, self.tau, self.rho, self.H, self.kappa]

    def to_vector_6d(self) -> List[float]:
        """Convert to 6D vector with latent dimension for future expansion."""
        return [self.phi, self.tau, self.rho, self.H, self.kappa, 0.0]

    def density(self) -> float:
        """Compute v9.2 perspectival density."""
        structure = self.phi * self.tau * self.rho
        entropy_gate = (1 - math.sqrt(self.H)) + (self.H * self.kappa)
        return structure * entropy_gate

    def decompose(self) -> Dict[str, float]:
        """Full decomposition of density components."""
        structure = self.phi * self.tau * self.rho
        entropy_penalty = 1 - math.sqrt(self.H)
        coherence_rescue = self.H * self.kappa
        entropy_gate = entropy_penalty + coherence_rescue
        D = structure * entropy_gate

        return {
            "phi": self.phi,
            "tau": self.tau,
            "rho": self.rho,
            "H": self.H,
            "kappa": self.kappa,
            "structure": structure,
            "entropy_penalty": entropy_penalty,
            "coherence_rescue": coherence_rescue,
            "entropy_gate": entropy_gate,
            "D": D,
            "name": self.name,
            "confidence": self.confidence
        }

    def __repr__(self) -> str:
        name_str = f"'{self.name}'" if self.name else "unnamed"
        return f"StateVector({name_str}: φ={self.phi:.2f}, τ={self.tau:.2f}, ρ={self.rho:.2f}, H={self.H:.2f}, κ={self.kappa:.2f}, D={self.density():.4f})"


def encode(
    phi: float,
    tau: float,
    rho: float,
    entropy: float,
    kappa: float = 0.50,
    name: Optional[str] = None
) -> StateVector:
    """
    Encode a topological state using v9.2 licensed variables.

    Parameters:
    -----------
    phi : float (0.0 - 1.0)
        Structural Integration - how unified/coherent the system is
    tau : float (0.0 - 1.0)
        Temporal Depth - the reach of temporal binding
    rho : float (0.0 - 1.0)
        Re-entrant Binding - recursive feedback strength (anchored to PCI)
    entropy : float (0.0 - 1.0)
        System Surprise/Noise - unpredictability (anchored to LZc)
    kappa : float (0.0 - 1.0)
        Coherence - structure within entropy (anchored to MSE)
        Default 0.50 for baseline
    name : str, optional
        State name for identification

    Returns:
    --------
    StateVector with all components and computed density
    """
    return StateVector(
        phi=phi,
        tau=tau,
        rho=rho,
        H=entropy,
        kappa=kappa,
        name=name
    )


def encode_legacy(phi: float, tau: float, rho: float, entropy: float) -> List[float]:
    """
    LEGACY: Encode a state as 6D vector for backward compatibility.

    Returns [φ, τ, ρ, H, latent_1, latent_2]

    Note: This format is deprecated. Use encode() for new code.
    """
    assert 0.0 <= phi <= 1.0, "phi must be in range [0.0, 1.0]"
    assert 0.0 <= tau <= 1.0, "tau must be in range [0.0, 1.0]"
    assert 0.0 <= rho <= 1.0, "rho must be in range [0.0, 1.0]"
    assert 0.0 <= entropy <= 1.0, "entropy must be in range [0.0, 1.0]"

    return [float(phi), float(tau), float(rho), float(entropy), 0.0, 0.0]


def encode_from_calibration(state_name: str) -> StateVector:
    """
    Create a StateVector from a pre-calibrated state.

    Parameters:
    -----------
    state_name : str
        Name of calibrated state (e.g., 'wakefulness', 'ketamine_anesthesia')

    Returns:
    --------
    StateVector with empirically grounded values

    Raises:
    -------
    ValueError if calibration not available or state not found
    """
    if not CALIBRATION_AVAILABLE:
        raise ValueError("Calibration library not available")

    states = get_calibrated_states()
    if state_name not in states:
        available = list(states.keys())
        raise ValueError(f"State '{state_name}' not found. Available: {available}")

    state = states[state_name]

    return StateVector(
        phi=state.phi.value,
        tau=state.tau.value,
        rho=state.rho.value,
        H=state.H.value,
        kappa=state.kappa.value,
        name=state.name,
        confidence=state.overall_confidence().value
    )


def get_all_calibrated_states() -> Dict[str, StateVector]:
    """
    Get all pre-calibrated states as StateVectors.

    Returns:
    --------
    Dict mapping state names to StateVectors
    """
    if not CALIBRATION_AVAILABLE:
        raise ValueError("Calibration library not available")

    states = get_calibrated_states()
    return {
        name: encode_from_calibration(name)
        for name in states.keys()
    }


def compute_density(phi: float, tau: float, rho: float) -> float:
    """
    LEGACY: Compute density as φ × τ × ρ only.

    This is the v7.0 formula. Use StateVector.density() for v9.2.
    """
    return phi * tau * rho


def compute_density_v92(
    phi: float,
    tau: float,
    rho: float,
    H: float,
    kappa: float
) -> float:
    """
    Compute v9.2 perspectival density.

    D = φ × τ × ρ × [(1 - √H) + (H × κ)]

    Parameters:
    -----------
    All parameters in range [0.0, 1.0]

    Returns:
    --------
    float: Perspectival density D
    """
    structure = phi * tau * rho
    entropy_gate = (1 - math.sqrt(H)) + (H * kappa)
    return structure * entropy_gate


# =============================================================================
# State Transition Utilities
# =============================================================================

def interpolate_states(
    state1: StateVector,
    state2: StateVector,
    t: float
) -> StateVector:
    """
    Linear interpolation between two states.

    Useful for modeling gradual transitions (e.g., anesthesia onset).

    Parameters:
    -----------
    state1: Starting state
    state2: Ending state
    t: Interpolation factor (0.0 = state1, 1.0 = state2)

    Returns:
    --------
    Interpolated StateVector
    """
    if not 0.0 <= t <= 1.0:
        raise ValueError(f"t must be in [0, 1], got {t}")

    return StateVector(
        phi=state1.phi + t * (state2.phi - state1.phi),
        tau=state1.tau + t * (state2.tau - state1.tau),
        rho=state1.rho + t * (state2.rho - state1.rho),
        H=state1.H + t * (state2.H - state1.H),
        kappa=state1.kappa + t * (state2.kappa - state1.kappa),
        name=f"Interpolated({t:.2f})"
    )


def create_trajectory(
    state1: StateVector,
    state2: StateVector,
    steps: int = 10
) -> List[StateVector]:
    """
    Create a trajectory of states between two endpoints.

    Useful for modeling gradients (e.g., psychedelic onset → peak).

    Parameters:
    -----------
    state1: Starting state
    state2: Ending state
    steps: Number of intermediate states

    Returns:
    --------
    List of StateVectors from state1 to state2
    """
    trajectory = []
    for i in range(steps + 1):
        t = i / steps
        trajectory.append(interpolate_states(state1, state2, t))
    return trajectory


# =============================================================================
# Main Execution
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("CONDUIT MONISM v9.2 - STATE ENCODER")
    print("=" * 60)
    print()

    # Demo: Create a state manually
    print("Manual state creation:")
    wake = encode(phi=0.80, tau=0.50, rho=0.55, entropy=0.50, kappa=0.50, name="Wakefulness")
    print(f"  {wake}")
    print(f"  Decomposition: {wake.decompose()}")
    print()

    # Demo: Load from calibration
    if CALIBRATION_AVAILABLE:
        print("Loading from calibration library:")
        all_states = get_all_calibrated_states()
        print(f"  Available states: {len(all_states)}")
        print()

        # Show a few key states
        key_states = ["wakefulness", "ketamine_anesthesia", "propofol_anesthesia", "flow_state"]
        print("Key states:")
        for name in key_states:
            if name in all_states:
                state = all_states[name]
                print(f"  {state}")
        print()

        # Demo: Create trajectory
        if "wakefulness" in all_states and "propofol_anesthesia" in all_states:
            print("Trajectory: Wakefulness → Propofol Anesthesia (5 steps)")
            trajectory = create_trajectory(
                all_states["wakefulness"],
                all_states["propofol_anesthesia"],
                steps=5
            )
            for state in trajectory:
                print(f"  D={state.density():.4f}")
    else:
        print("Calibration library not available.")
