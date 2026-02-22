"""
Tests for the v9.2 Conduit Monism density formula.

    D = phi * tau * rho * [(1 - sqrt(H)) + (H * kappa)]

This module validates:
- CANON reference states produce correct densities
- Structural zero-elimination (multiplicative axiom)
- Entropy gate behaviour under boundary conditions
- Monotonicity of structural parameters
- Empirical ordering constraints (DMT > Panic, Ketamine >> Propofol)
- Input validation for out-of-range parameters
"""

import math
import pytest

from src.density_models import density_v92, decompose_density
from src.encoder import StateVector, compute_density_v92
from tests.conftest import CANON_STATES


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _gate(H: float, kappa: float) -> float:
    """Compute the entropy gate independently for verification."""
    return (1.0 - math.sqrt(H)) + (H * kappa)


# =========================================================================
# 1. CANON reference-state density tests
# =========================================================================

class TestCanonDensities:
    """Verify that every CANON reference state reproduces its published D value."""

    @pytest.mark.parametrize("name,params", list(CANON_STATES.items()))
    def test_canon_density_within_tolerance(self, name, params):
        """Each CANON state must match its published density within 0.005.

        This tolerance accounts for rounding in the published table while
        still catching formula regressions.
        """
        computed = density_v92(
            params["phi"], params["tau"], params["rho"],
            params["H"], params["kappa"],
        )
        assert abs(computed - params["D"]) < 0.005, (
            f"{name}: computed D={computed:.6f}, expected D={params['D']:.3f}"
        )

    @pytest.mark.parametrize("name,params", list(CANON_STATES.items()))
    def test_canon_via_statevector(self, name, params):
        """StateVector.density() must agree with the standalone density_v92()."""
        sv = StateVector(
            phi=params["phi"], tau=params["tau"], rho=params["rho"],
            H=params["H"], kappa=params["kappa"], name=name,
        )
        assert abs(sv.density() - density_v92(
            params["phi"], params["tau"], params["rho"],
            params["H"], params["kappa"],
        )) < 1e-12

    @pytest.mark.parametrize("name,params", list(CANON_STATES.items()))
    def test_canon_via_compute_density_v92(self, name, params):
        """compute_density_v92() must agree with density_v92()."""
        d1 = density_v92(
            params["phi"], params["tau"], params["rho"],
            params["H"], params["kappa"],
        )
        d2 = compute_density_v92(
            params["phi"], params["tau"], params["rho"],
            params["H"], params["kappa"],
        )
        assert abs(d1 - d2) < 1e-12


# =========================================================================
# 2. Zero-elimination property (multiplicative axiom)
# =========================================================================

class TestZeroElimination:
    """If any structural invariant is zero, D must be exactly zero.

    This is the strongest falsifiable prediction of the multiplicative
    structure: a system with no integration (phi=0) or no temporal depth
    (tau=0) or no re-entrant binding (rho=0) has no perspective at all.
    """

    @pytest.mark.parametrize("zero_param", ["phi", "tau", "rho"])
    def test_single_structural_zero(self, zero_param):
        """Setting any single structural parameter to 0 produces D=0."""
        params = {"phi": 0.9, "tau": 0.9, "rho": 0.9, "H": 0.5, "kappa": 0.8}
        params[zero_param] = 0.0
        assert density_v92(**params) == 0.0

    def test_all_structural_zero(self):
        """All structural parameters zero -> D=0."""
        assert density_v92(0.0, 0.0, 0.0, 0.5, 0.5) == 0.0

    @pytest.mark.parametrize("zero_param", ["phi", "tau", "rho"])
    def test_zero_with_max_entropy_coherence(self, zero_param):
        """Structural zero overrides even maximum entropy gate values."""
        params = {"phi": 1.0, "tau": 1.0, "rho": 1.0, "H": 1.0, "kappa": 1.0}
        params[zero_param] = 0.0
        assert density_v92(**params) == 0.0


# =========================================================================
# 3. Entropy gate boundary conditions
# =========================================================================

class TestEntropyGateBoundaries:
    """Test the coherence-gated entropy term at its extreme configurations.

    Gate = (1 - sqrt(H)) + (H * kappa)
    """

    def test_H_zero_gate_equals_one(self):
        """H=0 means no entropy penalty and no coherence rescue: gate = 1.0.

        At zero entropy the system is in perfect order; the gate should
        impose no penalty (gate = 1 - sqrt(0) + 0*kappa = 1.0).
        """
        gate = _gate(0.0, 0.5)
        assert gate == pytest.approx(1.0)

    def test_H_one_kappa_zero_gate_equals_zero(self):
        """H=1, kappa=0: maximum entropy with no coherence rescue -> gate = 0.

        gate = (1 - sqrt(1)) + (1 * 0) = 0 + 0 = 0.
        Full entropy penalty, nothing to rescue. D collapses to zero.
        """
        gate = _gate(1.0, 0.0)
        assert gate == pytest.approx(0.0)

    def test_H_one_kappa_one_gate_equals_one(self):
        """H=1, kappa=1: maximum entropy fully rescued by maximum coherence.

        gate = (1 - sqrt(1)) + (1 * 1) = 0 + 1 = 1.0.
        This models the DMT-like case where coherence fully compensates.
        """
        gate = _gate(1.0, 1.0)
        assert gate == pytest.approx(1.0)

    def test_H_one_kappa_zero_density_zero(self):
        """Full entropy + zero coherence => D=0 even with maximal structure."""
        d = density_v92(1.0, 1.0, 1.0, 1.0, 0.0)
        assert d == pytest.approx(0.0)

    def test_H_one_kappa_one_density_equals_structure(self):
        """Full entropy + full coherence => D equals the raw structure product."""
        d = density_v92(0.8, 0.7, 0.6, 1.0, 1.0)
        structure = 0.8 * 0.7 * 0.6
        assert d == pytest.approx(structure)

    def test_H_zero_any_kappa_gate_one(self):
        """At H=0 the kappa value is irrelevant; gate is always 1.0."""
        for kappa in [0.0, 0.25, 0.5, 0.75, 1.0]:
            assert _gate(0.0, kappa) == pytest.approx(1.0)


# =========================================================================
# 4. Boundary-value tests for all parameters
# =========================================================================

class TestParameterBoundaries:
    """All five parameters must stay within [0, 1]."""

    @pytest.mark.parametrize("phi", [0.0, 1.0])
    @pytest.mark.parametrize("tau", [0.0, 1.0])
    @pytest.mark.parametrize("rho", [0.0, 1.0])
    @pytest.mark.parametrize("H", [0.0, 1.0])
    @pytest.mark.parametrize("kappa", [0.0, 1.0])
    def test_all_boundary_combinations(self, phi, tau, rho, H, kappa):
        """density_v92 must return a finite non-negative value for every
        corner of the 5-dimensional unit hypercube."""
        d = density_v92(phi, tau, rho, H, kappa)
        assert d >= 0.0
        assert math.isfinite(d)

    def test_all_ones(self):
        """All params at 1.0: gate = (1-1)+(1*1) = 1.0, D = 1.0."""
        assert density_v92(1.0, 1.0, 1.0, 1.0, 1.0) == pytest.approx(1.0)

    def test_all_zeros(self):
        """All params at 0.0: structure=0, D=0."""
        assert density_v92(0.0, 0.0, 0.0, 0.0, 0.0) == pytest.approx(0.0)


# =========================================================================
# 5. Input validation
# =========================================================================

class TestInputValidation:
    """Out-of-range parameters must raise ValueError."""

    @pytest.mark.parametrize("bad_param,bad_val", [
        ("phi", -0.1),
        ("phi", 1.1),
        ("tau", -0.01),
        ("tau", 2.0),
        ("rho", -1.0),
        ("rho", 1.001),
        ("H", -0.5),
        ("H", 1.5),
        ("kappa", -0.1),
        ("kappa", 1.1),
    ])
    def test_density_v92_rejects_out_of_range(self, bad_param, bad_val):
        """density_v92() must raise ValueError for any parameter outside [0, 1]."""
        params = {"phi": 0.5, "tau": 0.5, "rho": 0.5, "H": 0.5, "kappa": 0.5}
        params[bad_param] = bad_val
        with pytest.raises(ValueError):
            density_v92(**params)

    @pytest.mark.parametrize("bad_param,bad_val", [
        ("phi", -0.1),
        ("tau", 1.5),
        ("rho", -1.0),
        ("H", 2.0),
        ("kappa", -0.01),
    ])
    def test_statevector_rejects_out_of_range(self, bad_param, bad_val):
        """StateVector construction must raise ValueError for out-of-range values."""
        params = {"phi": 0.5, "tau": 0.5, "rho": 0.5, "H": 0.5, "kappa": 0.5}
        params[bad_param] = bad_val
        with pytest.raises(ValueError):
            StateVector(**params)


# =========================================================================
# 6. Monotonicity of structural parameters
# =========================================================================

class TestMonotonicity:
    """Increasing any structural parameter (with others fixed) must increase D.

    This follows directly from the multiplicative structure: D is linear in
    each of phi, tau, rho when the others are held constant and the gate is
    positive.
    """

    @pytest.mark.parametrize("param", ["phi", "tau", "rho"])
    def test_structural_monotonicity(self, param):
        """D must strictly increase when a structural parameter increases
        (assuming positive gate and nonzero other structural params)."""
        base = {"phi": 0.5, "tau": 0.5, "rho": 0.5, "H": 0.3, "kappa": 0.5}
        low_val = 0.3
        high_val = 0.8

        low_params = dict(base)
        low_params[param] = low_val
        high_params = dict(base)
        high_params[param] = high_val

        d_low = density_v92(**low_params)
        d_high = density_v92(**high_params)
        assert d_high > d_low, (
            f"Increasing {param} from {low_val} to {high_val} should increase D "
            f"but got D_low={d_low:.6f}, D_high={d_high:.6f}"
        )

    def test_phi_monotonicity_fine_grained(self):
        """Sweep phi from 0.1 to 0.9 and confirm D is strictly increasing."""
        prev_d = -1.0
        for phi_100 in range(10, 91, 5):
            phi = phi_100 / 100.0
            d = density_v92(phi, 0.6, 0.6, 0.4, 0.5)
            assert d > prev_d
            prev_d = d


# =========================================================================
# 7. Empirical ordering constraints
# =========================================================================

class TestEmpiricalOrdering:
    """Tests that the formula reproduces known empirical orderings.

    These are hard constraints from consciousness science:
    - DMT experiences have higher density than panic attacks
    - Ketamine preserves far more density than propofol
    """

    def test_dmt_greater_than_panic(self, dmt_state):
        """DMT density > Panic density.

        The DMT paradox: DMT has extreme entropy (H=0.70) but also high
        coherence (kappa=0.90). The coherence gate rescues the density.
        Panic has high entropy but LOW coherence, so the gate collapses it.

        We construct a panic-like state with high H, low kappa.
        """
        panic = StateVector(phi=0.70, tau=0.40, rho=0.60, H=0.80, kappa=0.20,
                            name="Panic")
        assert dmt_state.density() > panic.density(), (
            f"DMT D={dmt_state.density():.4f} should exceed "
            f"Panic D={panic.density():.4f}"
        )

    def test_ketamine_propofol_ratio_exceeds_10x(self, ketamine_state, propofol_state):
        """Ketamine density / Propofol density > 10.

        This captures the key clinical distinction: ketamine is a
        dissociative anaesthetic that preserves some experience;
        propofol produces near-total unconsciousness.
        """
        ratio = ketamine_state.density() / propofol_state.density()
        assert ratio > 10.0, (
            f"Ketamine/Propofol ratio={ratio:.2f}, expected > 10.0"
        )

    def test_wakefulness_exceeds_propofol(self, wakefulness_state, propofol_state):
        """Normal wakefulness must dominate propofol anaesthesia."""
        assert wakefulness_state.density() > propofol_state.density()

    def test_flow_exceeds_ketamine(self, flow_state, ketamine_state):
        """Flow state density should exceed dissociative ketamine."""
        assert flow_state.density() > ketamine_state.density()

    def test_dmt_is_highest_canon_density(self, canon_states):
        """DMT should produce the highest density of all CANON states."""
        dmt_d = density_v92(**{k: v for k, v in CANON_STATES["DMT"].items() if k != "D"})
        for name, params in CANON_STATES.items():
            other_d = density_v92(**{k: v for k, v in params.items() if k != "D"})
            assert dmt_d >= other_d, (
                f"DMT D={dmt_d:.4f} should be >= {name} D={other_d:.4f}"
            )

    def test_propofol_is_lowest_canon_density(self, canon_states):
        """Propofol should produce the lowest density of all CANON states."""
        prop_d = density_v92(**{k: v for k, v in CANON_STATES["Propofol"].items() if k != "D"})
        for name, params in CANON_STATES.items():
            other_d = density_v92(**{k: v for k, v in params.items() if k != "D"})
            assert prop_d <= other_d, (
                f"Propofol D={prop_d:.4f} should be <= {name} D={other_d:.4f}"
            )


# =========================================================================
# 8. Decomposition consistency
# =========================================================================

class TestDecomposition:
    """Verify that decompose_density returns internally consistent components."""

    @pytest.mark.parametrize("name,params", list(CANON_STATES.items()))
    def test_decomposition_reassembles(self, name, params):
        """structure * entropy_gate must equal the reported D."""
        decomp = decompose_density(
            params["phi"], params["tau"], params["rho"],
            params["H"], params["kappa"],
        )
        assert decomp["D"] == pytest.approx(
            decomp["structure"] * decomp["entropy_gate"]
        )

    @pytest.mark.parametrize("name,params", list(CANON_STATES.items()))
    def test_gate_equals_penalty_plus_rescue(self, name, params):
        """entropy_gate = entropy_penalty + coherence_rescue."""
        decomp = decompose_density(
            params["phi"], params["tau"], params["rho"],
            params["H"], params["kappa"],
        )
        assert decomp["entropy_gate"] == pytest.approx(
            decomp["entropy_penalty"] + decomp["coherence_rescue"]
        )

    @pytest.mark.parametrize("name,params", list(CANON_STATES.items()))
    def test_structure_equals_phi_tau_rho(self, name, params):
        """structure = phi * tau * rho."""
        decomp = decompose_density(
            params["phi"], params["tau"], params["rho"],
            params["H"], params["kappa"],
        )
        assert decomp["structure"] == pytest.approx(
            params["phi"] * params["tau"] * params["rho"]
        )
