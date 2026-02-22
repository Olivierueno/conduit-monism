"""
Advanced Operators Module - Conduit Engine v0.3

Operators that simulate liminal configurations from the framework.
All operators use the v9.2 StateVector with five invariants.

These operators model specific neurological/experiential states:
- Dementia progression
- Split-brain bifurcation
- Anesthesia gradients
- Locked-in syndrome
- Flow state induction
- Panic attack onset
"""

from typing import List, Tuple, Dict
from .encoder import StateVector


def op_dementia_progression(
    state: StateVector,
    stage: float
) -> Tuple[StateVector, str]:
    """
    Simulate dementia progression.

    Framework prediction: Self-Model (narrative identity, temporal depth) erodes
    as memory structures fail. Re-entrant binding of the immediate present
    often remains intact until very late stages.

    Parameters:
        state: Initial StateVector
        stage: Progression (0=healthy, 1=advanced)

    Returns:
        (Modified StateVector, description)
    """
    new_tau = max(0.0, state.tau * (1.0 - stage * 0.9))
    new_phi = max(0.0, state.phi * (1.0 - stage * 0.5))
    new_rho = max(0.0, state.rho * (1.0 - stage * 0.3))
    new_H = min(1.0, state.H + stage * 0.4)
    new_kappa = max(0.0, state.kappa * (1.0 - stage * 0.4))

    result = StateVector(
        phi=new_phi, tau=new_tau, rho=new_rho,
        H=new_H, kappa=new_kappa,
        name=f"Dementia(stage={stage:.1f})"
    )

    description = (
        f"Dementia stage {stage:.1f}: "
        f"Temporal depth severely impaired, but immediate 'now' persists. "
        f"D={result.density():.4f}"
    )

    return result, description


def op_split_brain(
    state: StateVector
) -> Tuple[StateVector, StateVector, str]:
    """
    Simulate corpus callosotomy (split-brain).

    Framework prediction: Topology bifurcates. Two distinct loci of perspective,
    each with lower integration (φ) than the whole.

    Parameters:
        state: Initial unified StateVector

    Returns:
        (Left hemisphere, Right hemisphere, description)
    """
    left = StateVector(
        phi=state.phi * 0.6, tau=state.tau, rho=state.rho,
        H=state.H, kappa=state.kappa,
        name="Left Hemisphere"
    )
    right = StateVector(
        phi=state.phi * 0.6, tau=state.tau, rho=state.rho,
        H=state.H, kappa=state.kappa,
        name="Right Hemisphere"
    )

    description = (
        f"Split-brain: One window becomes two narrower windows. "
        f"Original D={state.density():.4f}, "
        f"Left D={left.density():.4f}, Right D={right.density():.4f}"
    )

    return left, right, description


def op_anesthesia_gradient(
    state: StateVector,
    depth: float
) -> Tuple[StateVector, str]:
    """
    Simulate anesthesia onset/offset.

    Framework prediction: Propofol collapses re-entrant loops required for binding.
    As binding drops, perspective slides down the asymptotic curve toward zero.
    The 'thick now' becomes infinitely thin.

    Parameters:
        state: Initial StateVector
        depth: Anesthetic depth (0=awake, 1=deep anesthesia)

    Returns:
        (Modified StateVector, description)
    """
    new_rho = max(0.0, state.rho * (1.0 - depth))
    new_tau = max(0.0, state.tau * (1.0 - depth * 0.8))
    new_phi = max(0.0, state.phi * (1.0 - depth * 0.7))
    new_H = max(0.0, state.H * (1.0 - depth * 0.9))
    new_kappa = max(0.0, state.kappa * (1.0 - depth * 0.6))

    result = StateVector(
        phi=new_phi, tau=new_tau, rho=new_rho,
        H=new_H, kappa=new_kappa,
        name=f"Anesthesia(depth={depth:.2f})"
    )

    description = (
        f"Anesthesia depth {depth:.2f}: "
        f"Re-entrant binding collapsed. D={result.density():.4f}"
    )

    return result, description


def op_locked_in_syndrome(
    state: StateVector
) -> Tuple[StateVector, str]:
    """
    Simulate locked-in syndrome.

    Framework prediction: Full constraint topology with output isolation predicts
    high perspectival density despite behavioral invisibility.

    Parameters:
        state: StateVector (should be high-density)

    Returns:
        (Unchanged StateVector, description)
    """
    description = (
        f"Locked-in syndrome: Full perspectival density D={state.density():.4f} "
        f"with zero behavioral output. "
        f"Topology intact; only motor interface severed."
    )

    return state, description


def op_flow_state_induction(
    state: StateVector,
    intensity: float
) -> Tuple[StateVector, str]:
    """
    Simulate flow state induction.

    Flow states represent high-density topologies with extended temporal
    binding, high coherence, and reduced entropy.

    Parameters:
        state: Initial StateVector
        intensity: Flow intensity (0-1)

    Returns:
        (Modified StateVector, description)
    """
    new_phi = min(1.0, state.phi + intensity * 0.3)
    new_tau = min(1.0, state.tau + intensity * 0.2)
    new_rho = min(1.0, state.rho + intensity * 0.25)
    new_H = max(0.0, state.H - intensity * 0.4)
    new_kappa = min(1.0, state.kappa + intensity * 0.3)

    result = StateVector(
        phi=new_phi, tau=new_tau, rho=new_rho,
        H=new_H, kappa=new_kappa,
        name=f"Flow(intensity={intensity:.2f})"
    )

    description = (
        f"Flow state (intensity {intensity:.2f}): "
        f"High density, extended temporal binding, low entropy. "
        f"D={result.density():.4f}"
    )

    return result, description


def op_panic_induction(
    state: StateVector,
    severity: float
) -> Tuple[StateVector, str]:
    """
    Simulate panic attack onset.

    Panic is characterized by high entropy with low coherence,
    high binding (hyper-vigilant self-monitoring), and moderate integration
    (global alarm state).

    Parameters:
        state: Initial StateVector
        severity: Panic severity (0-1)

    Returns:
        (Modified StateVector, description)
    """
    new_phi = min(1.0, state.phi + severity * 0.1)
    new_tau = max(0.0, state.tau - severity * 0.3)
    new_rho = min(1.0, state.rho + severity * 0.15)
    new_H = min(1.0, state.H + severity * 0.5)
    new_kappa = max(0.0, state.kappa - severity * 0.4)

    result = StateVector(
        phi=new_phi, tau=new_tau, rho=new_rho,
        H=new_H, kappa=new_kappa,
        name=f"Panic(severity={severity:.2f})"
    )

    description = (
        f"Panic attack (severity {severity:.2f}): "
        f"High entropy, low coherence. D={result.density():.4f}"
    )

    return result, description


def op_psychedelic_onset(
    state: StateVector,
    intensity: float
) -> Tuple[StateVector, str]:
    """
    Simulate psychedelic onset with lag dynamics (AT13).

    Key insight: κ lags behind H. During onset, entropy rises before
    coherence can establish, producing transient anxiety. At peak,
    coherence catches up and the coherence gate rescues density.

    Parameters:
        state: Initial StateVector
        intensity: Dose intensity (0-1)

    Returns:
        (Modified StateVector, description)
    """
    new_phi = min(1.0, state.phi + intensity * 0.1)
    new_tau = min(1.0, state.tau + intensity * 0.3)
    new_rho = state.rho
    new_H = min(1.0, state.H + intensity * 0.35)
    # κ lags: at low intensity, κ hasn't caught up yet
    kappa_lag = intensity ** 1.5  # Nonlinear lag
    new_kappa = min(1.0, state.kappa + kappa_lag * 0.4)

    result = StateVector(
        phi=new_phi, tau=new_tau, rho=new_rho,
        H=new_H, kappa=new_kappa,
        name=f"Psychedelic(intensity={intensity:.2f})"
    )

    description = (
        f"Psychedelic onset (intensity {intensity:.2f}): "
        f"H={new_H:.2f}, κ={new_kappa:.2f} (lag={kappa_lag:.2f}). "
        f"D={result.density():.4f}"
    )

    return result, description


def simulate_trajectory(
    initial_state: StateVector,
    operator_func,
    steps: int = 10,
    **operator_kwargs
) -> List[Dict]:
    """
    Simulate a trajectory through state space by applying an operator iteratively.

    Parameters:
        initial_state: Starting StateVector
        operator_func: Operator function to apply
        steps: Number of steps to simulate
        **operator_kwargs: Additional arguments for the operator

    Returns:
        List of dicts with state data at each step
    """
    trajectory = []
    current = initial_state

    for step in range(steps):
        progress = step / (steps - 1) if steps > 1 else 0

        result = operator_func(current, progress)
        if isinstance(result, tuple) and len(result) >= 2:
            if isinstance(result[0], StateVector):
                current = result[0]
            elif isinstance(result[0], tuple):
                current = result[0]
        else:
            current = result

        trajectory.append({
            'step': step,
            'progress': progress,
            'phi': current.phi,
            'tau': current.tau,
            'rho': current.rho,
            'H': current.H,
            'kappa': current.kappa,
            'density': current.density(),
            'name': current.name
        })

    return trajectory
