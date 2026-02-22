"""
Tests for the StateVector encoder and trajectory utilities.

Validates:
- StateVector construction, validation, and representation
- to_vector() and to_vector_6d() output shapes
- density() agreement with compute_density_v92()
- decompose() returns all expected keys with consistent values
- interpolate_states() boundary behaviour (t=0 -> state1, t=1 -> state2)
- create_trajectory() returns the correct number of steps
- Out-of-range rejection on construction
"""

import math
import pytest

from src.encoder import (
    StateVector,
    encode,
    compute_density_v92,
    interpolate_states,
    create_trajectory,
)
from tests.conftest import CANON_STATES


# =========================================================================
# 1. StateVector construction and validation
# =========================================================================

class TestStateVectorConstruction:
    """Basic construction, field access, and validation."""

    def test_construct_with_valid_params(self):
        """A StateVector with all params in [0,1] should construct without error."""
        sv = StateVector(phi=0.5, tau=0.6, rho=0.7, H=0.4, kappa=0.8)
        assert sv.phi == 0.5
        assert sv.tau == 0.6
        assert sv.rho == 0.7
        assert sv.H == 0.4
        assert sv.kappa == 0.8

    def test_construct_with_name(self):
        """Optional name field should be stored."""
        sv = StateVector(phi=0.5, tau=0.5, rho=0.5, H=0.5, kappa=0.5,
                         name="TestState")
        assert sv.name == "TestState"

    def test_construct_with_confidence(self):
        """Optional confidence field should be stored."""
        sv = StateVector(phi=0.5, tau=0.5, rho=0.5, H=0.5, kappa=0.5,
                         confidence="high")
        assert sv.confidence == "high"

    def test_name_defaults_to_none(self):
        """Name should default to None when not provided."""
        sv = StateVector(phi=0.5, tau=0.5, rho=0.5, H=0.5, kappa=0.5)
        assert sv.name is None

    def test_boundary_zero(self):
        """All-zero StateVector should construct successfully."""
        sv = StateVector(phi=0.0, tau=0.0, rho=0.0, H=0.0, kappa=0.0)
        assert sv.density() == 0.0

    def test_boundary_one(self):
        """All-ones StateVector should construct successfully."""
        sv = StateVector(phi=1.0, tau=1.0, rho=1.0, H=1.0, kappa=1.0)
        assert sv.density() == pytest.approx(1.0)

    @pytest.mark.parametrize("field,bad_val", [
        ("phi", -0.01),
        ("phi", 1.01),
        ("tau", -1.0),
        ("tau", 5.0),
        ("rho", -0.001),
        ("rho", 1.1),
        ("H", -0.5),
        ("H", 1.5),
        ("kappa", -0.1),
        ("kappa", 1.001),
    ])
    def test_out_of_range_raises_value_error(self, field, bad_val):
        """Any parameter outside [0.0, 1.0] must raise ValueError."""
        params = {"phi": 0.5, "tau": 0.5, "rho": 0.5, "H": 0.5, "kappa": 0.5}
        params[field] = bad_val
        with pytest.raises(ValueError):
            StateVector(**params)

    def test_repr_contains_density(self):
        """The repr should contain a D= field showing density."""
        sv = StateVector(phi=0.5, tau=0.5, rho=0.5, H=0.5, kappa=0.5,
                         name="Test")
        r = repr(sv)
        assert "D=" in r
        assert "Test" in r


# =========================================================================
# 2. to_vector() and to_vector_6d()
# =========================================================================

class TestVectorConversion:
    """Verify vector serialisation methods."""

    def test_to_vector_returns_five_floats(self, wakefulness_state):
        """to_vector() should return a list of exactly 5 floats."""
        vec = wakefulness_state.to_vector()
        assert len(vec) == 5
        assert all(isinstance(v, float) for v in vec)

    def test_to_vector_order(self):
        """to_vector() order must be [phi, tau, rho, H, kappa]."""
        sv = StateVector(phi=0.1, tau=0.2, rho=0.3, H=0.4, kappa=0.5)
        assert sv.to_vector() == [0.1, 0.2, 0.3, 0.4, 0.5]

    def test_to_vector_6d_returns_six_floats(self, wakefulness_state):
        """to_vector_6d() should return 6 floats with a trailing zero."""
        vec = wakefulness_state.to_vector_6d()
        assert len(vec) == 6
        assert vec[5] == 0.0

    def test_to_vector_6d_first_five_match(self, wakefulness_state):
        """First 5 elements of to_vector_6d() must equal to_vector()."""
        vec5 = wakefulness_state.to_vector()
        vec6 = wakefulness_state.to_vector_6d()
        assert vec5 == vec6[:5]


# =========================================================================
# 3. density() agreement with compute_density_v92()
# =========================================================================

class TestDensityAgreement:
    """StateVector.density() must exactly agree with compute_density_v92()."""

    @pytest.mark.parametrize("name,params", list(CANON_STATES.items()))
    def test_density_matches_compute_density_v92(self, name, params):
        """For every CANON state, the two density computation paths must agree."""
        sv = StateVector(
            phi=params["phi"], tau=params["tau"], rho=params["rho"],
            H=params["H"], kappa=params["kappa"],
        )
        standalone = compute_density_v92(
            params["phi"], params["tau"], params["rho"],
            params["H"], params["kappa"],
        )
        assert sv.density() == pytest.approx(standalone, abs=1e-15)

    def test_density_is_non_negative(self, midpoint_state):
        """Density must never be negative for valid inputs."""
        assert midpoint_state.density() >= 0.0

    def test_zero_state_density_is_zero(self, zero_state):
        """The all-zero state must have density exactly 0."""
        assert zero_state.density() == 0.0


# =========================================================================
# 4. decompose() method
# =========================================================================

class TestDecompose:
    """Verify decompose() returns all expected keys with consistent values."""

    EXPECTED_KEYS = {
        "phi", "tau", "rho", "H", "kappa",
        "structure", "entropy_penalty", "coherence_rescue",
        "entropy_gate", "D", "name", "confidence",
    }

    def test_decompose_has_all_keys(self, wakefulness_state):
        """decompose() must return a dict with every expected key."""
        decomp = wakefulness_state.decompose()
        assert set(decomp.keys()) == self.EXPECTED_KEYS

    def test_decompose_D_equals_density(self, wakefulness_state):
        """decompose()['D'] must match density()."""
        decomp = wakefulness_state.decompose()
        assert decomp["D"] == pytest.approx(wakefulness_state.density())

    def test_decompose_structure_product(self, wakefulness_state):
        """structure = phi * tau * rho."""
        decomp = wakefulness_state.decompose()
        expected = (wakefulness_state.phi
                    * wakefulness_state.tau
                    * wakefulness_state.rho)
        assert decomp["structure"] == pytest.approx(expected)

    def test_decompose_entropy_penalty(self, wakefulness_state):
        """entropy_penalty = 1 - sqrt(H)."""
        decomp = wakefulness_state.decompose()
        expected = 1.0 - math.sqrt(wakefulness_state.H)
        assert decomp["entropy_penalty"] == pytest.approx(expected)

    def test_decompose_coherence_rescue(self, wakefulness_state):
        """coherence_rescue = H * kappa."""
        decomp = wakefulness_state.decompose()
        expected = wakefulness_state.H * wakefulness_state.kappa
        assert decomp["coherence_rescue"] == pytest.approx(expected)

    def test_decompose_gate_sum(self, wakefulness_state):
        """entropy_gate = entropy_penalty + coherence_rescue."""
        decomp = wakefulness_state.decompose()
        assert decomp["entropy_gate"] == pytest.approx(
            decomp["entropy_penalty"] + decomp["coherence_rescue"]
        )

    def test_decompose_preserves_name(self, wakefulness_state):
        """decompose() must include the StateVector's name."""
        decomp = wakefulness_state.decompose()
        assert decomp["name"] == "Wakefulness"

    def test_decompose_preserves_confidence(self):
        """decompose() must include the confidence level."""
        sv = StateVector(phi=0.5, tau=0.5, rho=0.5, H=0.5, kappa=0.5,
                         confidence="moderate")
        decomp = sv.decompose()
        assert decomp["confidence"] == "moderate"


# =========================================================================
# 5. encode() function
# =========================================================================

class TestEncodeFunction:
    """Test the top-level encode() convenience function."""

    def test_encode_returns_statevector(self):
        """encode() must return a StateVector instance."""
        sv = encode(phi=0.5, tau=0.5, rho=0.5, entropy=0.5, kappa=0.5)
        assert isinstance(sv, StateVector)

    def test_encode_maps_entropy_to_H(self):
        """encode() uses 'entropy' as the parameter name for H."""
        sv = encode(phi=0.5, tau=0.5, rho=0.5, entropy=0.7, kappa=0.3)
        assert sv.H == 0.7

    def test_encode_default_kappa(self):
        """encode() defaults kappa to 0.50."""
        sv = encode(phi=0.5, tau=0.5, rho=0.5, entropy=0.5)
        assert sv.kappa == 0.50

    def test_encode_with_name(self):
        """encode() passes name through to the StateVector."""
        sv = encode(phi=0.5, tau=0.5, rho=0.5, entropy=0.5, name="MyState")
        assert sv.name == "MyState"


# =========================================================================
# 6. interpolate_states()
# =========================================================================

class TestInterpolateStates:
    """Verify linear interpolation between two consciousness states."""

    def test_t_zero_returns_state1(self, wakefulness_state, propofol_state):
        """At t=0 the interpolated state must equal state1."""
        result = interpolate_states(wakefulness_state, propofol_state, 0.0)
        assert result.phi == pytest.approx(wakefulness_state.phi)
        assert result.tau == pytest.approx(wakefulness_state.tau)
        assert result.rho == pytest.approx(wakefulness_state.rho)
        assert result.H == pytest.approx(wakefulness_state.H)
        assert result.kappa == pytest.approx(wakefulness_state.kappa)

    def test_t_one_returns_state2(self, wakefulness_state, propofol_state):
        """At t=1 the interpolated state must equal state2."""
        result = interpolate_states(wakefulness_state, propofol_state, 1.0)
        assert result.phi == pytest.approx(propofol_state.phi)
        assert result.tau == pytest.approx(propofol_state.tau)
        assert result.rho == pytest.approx(propofol_state.rho)
        assert result.H == pytest.approx(propofol_state.H)
        assert result.kappa == pytest.approx(propofol_state.kappa)

    def test_t_half_is_midpoint(self, wakefulness_state, propofol_state):
        """At t=0.5 each parameter should be the arithmetic mean."""
        result = interpolate_states(wakefulness_state, propofol_state, 0.5)
        assert result.phi == pytest.approx(
            (wakefulness_state.phi + propofol_state.phi) / 2.0
        )
        assert result.tau == pytest.approx(
            (wakefulness_state.tau + propofol_state.tau) / 2.0
        )

    def test_interpolation_is_valid_statevector(self, wakefulness_state, propofol_state):
        """Every interpolated point must be a valid StateVector (params in [0,1])."""
        for t_10 in range(0, 11):
            t = t_10 / 10.0
            result = interpolate_states(wakefulness_state, propofol_state, t)
            assert 0.0 <= result.phi <= 1.0
            assert 0.0 <= result.tau <= 1.0
            assert 0.0 <= result.rho <= 1.0
            assert 0.0 <= result.H <= 1.0
            assert 0.0 <= result.kappa <= 1.0

    def test_t_out_of_range_raises(self, wakefulness_state, propofol_state):
        """t outside [0, 1] must raise ValueError."""
        with pytest.raises(ValueError):
            interpolate_states(wakefulness_state, propofol_state, -0.1)
        with pytest.raises(ValueError):
            interpolate_states(wakefulness_state, propofol_state, 1.1)

    def test_interpolation_density_is_continuous(self, wakefulness_state, propofol_state):
        """Density along the interpolation should change continuously
        (no sudden jumps between adjacent steps)."""
        densities = []
        steps = 100
        for i in range(steps + 1):
            t = i / steps
            result = interpolate_states(wakefulness_state, propofol_state, t)
            densities.append(result.density())

        for i in range(1, len(densities)):
            jump = abs(densities[i] - densities[i - 1])
            assert jump < 0.05, (
                f"Discontinuity at step {i}: jump={jump:.6f}"
            )


# =========================================================================
# 7. create_trajectory()
# =========================================================================

class TestCreateTrajectory:
    """Verify trajectory generation between two states."""

    def test_trajectory_length(self, wakefulness_state, propofol_state):
        """create_trajectory(steps=N) returns N+1 states (inclusive endpoints)."""
        for steps in [5, 10, 20]:
            traj = create_trajectory(wakefulness_state, propofol_state, steps=steps)
            assert len(traj) == steps + 1

    def test_trajectory_starts_at_state1(self, wakefulness_state, propofol_state):
        """First element of trajectory should match state1."""
        traj = create_trajectory(wakefulness_state, propofol_state, steps=10)
        first = traj[0]
        assert first.phi == pytest.approx(wakefulness_state.phi)
        assert first.tau == pytest.approx(wakefulness_state.tau)
        assert first.rho == pytest.approx(wakefulness_state.rho)

    def test_trajectory_ends_at_state2(self, wakefulness_state, propofol_state):
        """Last element of trajectory should match state2."""
        traj = create_trajectory(wakefulness_state, propofol_state, steps=10)
        last = traj[-1]
        assert last.phi == pytest.approx(propofol_state.phi)
        assert last.tau == pytest.approx(propofol_state.tau)
        assert last.rho == pytest.approx(propofol_state.rho)

    def test_trajectory_all_valid(self, wakefulness_state, dmt_state):
        """Every state in a trajectory must be a valid StateVector."""
        traj = create_trajectory(wakefulness_state, dmt_state, steps=20)
        for sv in traj:
            assert isinstance(sv, StateVector)
            assert 0.0 <= sv.phi <= 1.0
            assert 0.0 <= sv.tau <= 1.0
            assert 0.0 <= sv.rho <= 1.0
            assert 0.0 <= sv.H <= 1.0
            assert 0.0 <= sv.kappa <= 1.0

    def test_trajectory_single_step(self, wakefulness_state, propofol_state):
        """With steps=1, trajectory should be [state1, state2]."""
        traj = create_trajectory(wakefulness_state, propofol_state, steps=1)
        assert len(traj) == 2
        assert traj[0].phi == pytest.approx(wakefulness_state.phi)
        assert traj[1].phi == pytest.approx(propofol_state.phi)
