"""
Operators Module - Conduit Engine v0.3

Operators transform StateVectors in the topological space.
All operators work on the five v9.2 invariants: φ, τ, ρ, H, κ.

Operators are the "mechanics of thought" -- they model how states transition
under perturbation (anesthesia onset, attentional shift, neurochemical change).
"""

from .encoder import StateVector


def op_perturb_binding(state: StateVector, magnitude: float) -> StateVector:
    """
    Perturb Re-entrant Binding (ρ).

    Simulates: drifting focus, anesthesia onset, degradation of recursive feedback.

    Parameters:
        state: Input StateVector
        magnitude: Amount to modulate ρ (positive increases, negative decreases)

    Returns:
        New StateVector with modified ρ
    """
    new_rho = max(0.0, min(1.0, state.rho + magnitude))
    return StateVector(
        phi=state.phi, tau=state.tau, rho=new_rho,
        H=state.H, kappa=state.kappa, name=state.name
    )


def op_fracture_integration(state: StateVector, magnitude: float) -> StateVector:
    """
    Fracture Structural Integration (φ).

    Simulates: dissociation, cognitive lesion, system fragmentation.

    Parameters:
        state: Input StateVector
        magnitude: Amount to reduce φ (positive values reduce integration)

    Returns:
        New StateVector with reduced φ
    """
    new_phi = max(0.0, min(1.0, state.phi - magnitude))
    return StateVector(
        phi=new_phi, tau=state.tau, rho=state.rho,
        H=state.H, kappa=state.kappa, name=state.name
    )


def op_stretch_temporal_depth(state: StateVector, magnitude: float) -> StateVector:
    """
    Stretch or compress Temporal Depth (τ).

    Simulates: time dilation/compression, extended present (flow), temporal fragmentation.

    Parameters:
        state: Input StateVector
        magnitude: Amount to modulate τ (positive extends, negative compresses)

    Returns:
        New StateVector with modified τ
    """
    new_tau = max(0.0, min(1.0, state.tau + magnitude))
    return StateVector(
        phi=state.phi, tau=new_tau, rho=state.rho,
        H=state.H, kappa=state.kappa, name=state.name
    )


def op_inject_entropy(state: StateVector, magnitude: float) -> StateVector:
    """
    Inject Entropy/Noise (H).

    Simulates: surprise, sensory overload, system perturbation.

    Parameters:
        state: Input StateVector
        magnitude: Amount to increase entropy (positive adds noise)

    Returns:
        New StateVector with modified H
    """
    new_H = max(0.0, min(1.0, state.H + magnitude))
    return StateVector(
        phi=state.phi, tau=state.tau, rho=state.rho,
        H=new_H, kappa=state.kappa, name=state.name
    )


def op_modulate_coherence(state: StateVector, magnitude: float) -> StateVector:
    """
    Modulate Coherence (κ).

    Simulates: onset of structured thought, fractal dynamics, loss of meaning.

    Parameters:
        state: Input StateVector
        magnitude: Amount to modulate κ (positive increases structure in entropy)

    Returns:
        New StateVector with modified κ
    """
    new_kappa = max(0.0, min(1.0, state.kappa + magnitude))
    return StateVector(
        phi=state.phi, tau=state.tau, rho=state.rho,
        H=state.H, kappa=new_kappa, name=state.name
    )
