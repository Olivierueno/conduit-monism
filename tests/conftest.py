"""
Shared fixtures for Conduit Monism test suite.

Provides canonical consciousness states from CANON.md as reusable
pytest fixtures. All values are empirically grounded reference points
for the v9.2 density formula:

    D = phi * tau * rho * [(1 - sqrt(H)) + (H * kappa)]
"""

import pytest
from src.encoder import StateVector


# ---------------------------------------------------------------------------
# CANON reference states (from CANON.md)
# ---------------------------------------------------------------------------

# D values below are the exact outputs of the v9.2 formula
# D = phi * tau * rho * [(1 - sqrt(H)) + (H * kappa)]
# applied to the CANON parameter vectors.  The published CANON.md table
# may show rounded or independently-calibrated D values; the tests use
# the formula-derived values so they validate the code, not the table.
CANON_STATES = {
    "Wakefulness":  {"phi": 0.80, "tau": 0.75, "rho": 0.65, "H": 0.50, "kappa": 0.65, "D": 0.240978},
    "Propofol":     {"phi": 0.25, "tau": 0.10, "rho": 0.24, "H": 0.35, "kappa": 0.20, "D": 0.002870},
    "Ketamine":     {"phi": 0.50, "tau": 0.50, "rho": 0.44, "H": 0.55, "kappa": 0.80, "D": 0.076822},
    "Flow":         {"phi": 0.90, "tau": 0.70, "rho": 0.65, "H": 0.55, "kappa": 0.75, "D": 0.274725},
    "DMT":          {"phi": 0.85, "tau": 0.90, "rho": 0.70, "H": 0.70, "kappa": 0.90, "D": 0.424834},
    "Meditation":   {"phi": 0.85, "tau": 0.80, "rho": 0.70, "H": 0.40, "kappa": 0.80, "D": 0.327271},
}


@pytest.fixture
def canon_states():
    """Return the full dictionary of CANON reference states."""
    return CANON_STATES


@pytest.fixture
def wakefulness_state():
    """Normal wakefulness -- the default baseline consciousness state."""
    s = CANON_STATES["Wakefulness"]
    return StateVector(phi=s["phi"], tau=s["tau"], rho=s["rho"],
                       H=s["H"], kappa=s["kappa"], name="Wakefulness")


@pytest.fixture
def propofol_state():
    """Propofol anaesthesia -- near-total suppression of binding and integration."""
    s = CANON_STATES["Propofol"]
    return StateVector(phi=s["phi"], tau=s["tau"], rho=s["rho"],
                       H=s["H"], kappa=s["kappa"], name="Propofol")


@pytest.fixture
def ketamine_state():
    """Ketamine anaesthesia -- dissociative state with residual coherence."""
    s = CANON_STATES["Ketamine"]
    return StateVector(phi=s["phi"], tau=s["tau"], rho=s["rho"],
                       H=s["H"], kappa=s["kappa"], name="Ketamine")


@pytest.fixture
def flow_state():
    """Flow state -- high-density topology with extended temporal binding."""
    s = CANON_STATES["Flow"]
    return StateVector(phi=s["phi"], tau=s["tau"], rho=s["rho"],
                       H=s["H"], kappa=s["kappa"], name="Flow")


@pytest.fixture
def dmt_state():
    """DMT experience -- maximal structured entropy; coherence gate resolves the paradox."""
    s = CANON_STATES["DMT"]
    return StateVector(phi=s["phi"], tau=s["tau"], rho=s["rho"],
                       H=s["H"], kappa=s["kappa"], name="DMT")


@pytest.fixture
def meditation_state():
    """Deep meditation -- high integration, moderate entropy, high coherence."""
    s = CANON_STATES["Meditation"]
    return StateVector(phi=s["phi"], tau=s["tau"], rho=s["rho"],
                       H=s["H"], kappa=s["kappa"], name="Meditation")


@pytest.fixture
def zero_state():
    """All-zero state -- the null topology with zero perspectival density."""
    return StateVector(phi=0.0, tau=0.0, rho=0.0, H=0.0, kappa=0.0,
                       name="Zero")


@pytest.fixture
def max_state():
    """All-ones state -- theoretical maximum of every parameter."""
    return StateVector(phi=1.0, tau=1.0, rho=1.0, H=1.0, kappa=1.0,
                       name="Maximum")


@pytest.fixture
def midpoint_state():
    """All parameters at 0.5 -- useful as a neutral perturbation baseline."""
    return StateVector(phi=0.5, tau=0.5, rho=0.5, H=0.5, kappa=0.5,
                       name="Midpoint")
