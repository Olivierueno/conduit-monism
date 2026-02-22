"""
Tests for basic and advanced operators.

Operators transform StateVectors in the topological space to model
neurological and experiential transitions (anaesthesia onset,
dissociation, flow induction, etc.).

Validates:
- Every operator returns a valid StateVector (all params in [0, 1])
- Zero-magnitude perturbation is identity
- Extreme magnitudes stay within range bounds
- op_split_brain produces two hemispheres each with lower phi
- op_anesthesia_gradient at depth=1 produces near-zero density
- Advanced operators return (StateVector, str) tuples
"""

import pytest

from src.encoder import StateVector
from src.operators import (
    op_perturb_binding,
    op_fracture_integration,
    op_stretch_temporal_depth,
    op_inject_entropy,
    op_modulate_coherence,
)
from src.advanced_operators import (
    op_dementia_progression,
    op_split_brain,
    op_anesthesia_gradient,
    op_locked_in_syndrome,
    op_flow_state_induction,
    op_panic_induction,
    op_psychedelic_onset,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def assert_valid_state(sv: StateVector):
    """Assert that a StateVector has all parameters within [0, 1]."""
    assert isinstance(sv, StateVector), f"Expected StateVector, got {type(sv)}"
    assert 0.0 <= sv.phi <= 1.0, f"phi={sv.phi} out of range"
    assert 0.0 <= sv.tau <= 1.0, f"tau={sv.tau} out of range"
    assert 0.0 <= sv.rho <= 1.0, f"rho={sv.rho} out of range"
    assert 0.0 <= sv.H <= 1.0, f"H={sv.H} out of range"
    assert 0.0 <= sv.kappa <= 1.0, f"kappa={sv.kappa} out of range"


# =========================================================================
# 1. Basic operators -- valid output
# =========================================================================

BASIC_OPERATORS = [
    ("op_perturb_binding", op_perturb_binding),
    ("op_fracture_integration", op_fracture_integration),
    ("op_stretch_temporal_depth", op_stretch_temporal_depth),
    ("op_inject_entropy", op_inject_entropy),
    ("op_modulate_coherence", op_modulate_coherence),
]


class TestBasicOperatorsValidOutput:
    """Every basic operator must return a valid StateVector for typical inputs."""

    @pytest.mark.parametrize("name,op_func", BASIC_OPERATORS)
    def test_positive_magnitude_returns_valid_state(self, name, op_func,
                                                     midpoint_state):
        """Positive magnitude on a midpoint state should produce valid output."""
        result = op_func(midpoint_state, 0.2)
        assert_valid_state(result)

    @pytest.mark.parametrize("name,op_func", BASIC_OPERATORS)
    def test_negative_magnitude_returns_valid_state(self, name, op_func,
                                                     midpoint_state):
        """Negative magnitude on a midpoint state should produce valid output."""
        result = op_func(midpoint_state, -0.2)
        assert_valid_state(result)

    @pytest.mark.parametrize("name,op_func", BASIC_OPERATORS)
    def test_extreme_positive_magnitude_clamped(self, name, op_func,
                                                 midpoint_state):
        """Extreme positive magnitude should clamp to [0, 1], not overflow."""
        result = op_func(midpoint_state, 10.0)
        assert_valid_state(result)

    @pytest.mark.parametrize("name,op_func", BASIC_OPERATORS)
    def test_extreme_negative_magnitude_clamped(self, name, op_func,
                                                 midpoint_state):
        """Extreme negative magnitude should clamp to [0, 1], not underflow."""
        result = op_func(midpoint_state, -10.0)
        assert_valid_state(result)


# =========================================================================
# 2. Zero-magnitude identity
# =========================================================================

class TestZeroMagnitudeIdentity:
    """Applying an operator with magnitude=0 should return the same state."""

    def test_perturb_binding_zero(self, wakefulness_state):
        """op_perturb_binding(state, 0) should preserve rho."""
        result = op_perturb_binding(wakefulness_state, 0.0)
        assert result.rho == pytest.approx(wakefulness_state.rho)
        assert result.phi == pytest.approx(wakefulness_state.phi)
        assert result.tau == pytest.approx(wakefulness_state.tau)
        assert result.H == pytest.approx(wakefulness_state.H)
        assert result.kappa == pytest.approx(wakefulness_state.kappa)

    def test_fracture_integration_zero(self, wakefulness_state):
        """op_fracture_integration(state, 0) should preserve phi."""
        result = op_fracture_integration(wakefulness_state, 0.0)
        assert result.phi == pytest.approx(wakefulness_state.phi)

    def test_stretch_temporal_zero(self, wakefulness_state):
        """op_stretch_temporal_depth(state, 0) should preserve tau."""
        result = op_stretch_temporal_depth(wakefulness_state, 0.0)
        assert result.tau == pytest.approx(wakefulness_state.tau)

    def test_inject_entropy_zero(self, wakefulness_state):
        """op_inject_entropy(state, 0) should preserve H."""
        result = op_inject_entropy(wakefulness_state, 0.0)
        assert result.H == pytest.approx(wakefulness_state.H)

    def test_modulate_coherence_zero(self, wakefulness_state):
        """op_modulate_coherence(state, 0) should preserve kappa."""
        result = op_modulate_coherence(wakefulness_state, 0.0)
        assert result.kappa == pytest.approx(wakefulness_state.kappa)

    def test_zero_magnitude_preserves_density(self, wakefulness_state):
        """All operators at magnitude=0 should preserve density exactly."""
        for _, op_func in BASIC_OPERATORS:
            result = op_func(wakefulness_state, 0.0)
            assert result.density() == pytest.approx(
                wakefulness_state.density()
            )


# =========================================================================
# 3. Directional correctness of basic operators
# =========================================================================

class TestDirectionalEffects:
    """Verify that operators move parameters in the expected direction."""

    def test_perturb_binding_positive_increases_rho(self, midpoint_state):
        """Positive magnitude should increase rho."""
        result = op_perturb_binding(midpoint_state, 0.1)
        assert result.rho > midpoint_state.rho

    def test_perturb_binding_negative_decreases_rho(self, midpoint_state):
        """Negative magnitude should decrease rho."""
        result = op_perturb_binding(midpoint_state, -0.1)
        assert result.rho < midpoint_state.rho

    def test_fracture_integration_reduces_phi(self, midpoint_state):
        """Positive magnitude should reduce phi (fracturing integration)."""
        result = op_fracture_integration(midpoint_state, 0.1)
        assert result.phi < midpoint_state.phi

    def test_stretch_temporal_positive_increases_tau(self, midpoint_state):
        """Positive magnitude should increase tau."""
        result = op_stretch_temporal_depth(midpoint_state, 0.1)
        assert result.tau > midpoint_state.tau

    def test_inject_entropy_positive_increases_H(self, midpoint_state):
        """Positive magnitude should increase H."""
        result = op_inject_entropy(midpoint_state, 0.1)
        assert result.H > midpoint_state.H

    def test_modulate_coherence_positive_increases_kappa(self, midpoint_state):
        """Positive magnitude should increase kappa."""
        result = op_modulate_coherence(midpoint_state, 0.1)
        assert result.kappa > midpoint_state.kappa


# =========================================================================
# 4. Operators only modify their target parameter
# =========================================================================

class TestOperatorIsolation:
    """Each basic operator should only modify its target parameter."""

    def test_perturb_binding_only_changes_rho(self, midpoint_state):
        """op_perturb_binding should only change rho, leaving others intact."""
        result = op_perturb_binding(midpoint_state, 0.2)
        assert result.phi == midpoint_state.phi
        assert result.tau == midpoint_state.tau
        assert result.H == midpoint_state.H
        assert result.kappa == midpoint_state.kappa
        assert result.rho != midpoint_state.rho

    def test_fracture_integration_only_changes_phi(self, midpoint_state):
        """op_fracture_integration should only change phi."""
        result = op_fracture_integration(midpoint_state, 0.2)
        assert result.tau == midpoint_state.tau
        assert result.rho == midpoint_state.rho
        assert result.H == midpoint_state.H
        assert result.kappa == midpoint_state.kappa

    def test_stretch_temporal_only_changes_tau(self, midpoint_state):
        """op_stretch_temporal_depth should only change tau."""
        result = op_stretch_temporal_depth(midpoint_state, 0.2)
        assert result.phi == midpoint_state.phi
        assert result.rho == midpoint_state.rho
        assert result.H == midpoint_state.H
        assert result.kappa == midpoint_state.kappa

    def test_inject_entropy_only_changes_H(self, midpoint_state):
        """op_inject_entropy should only change H."""
        result = op_inject_entropy(midpoint_state, 0.2)
        assert result.phi == midpoint_state.phi
        assert result.tau == midpoint_state.tau
        assert result.rho == midpoint_state.rho
        assert result.kappa == midpoint_state.kappa

    def test_modulate_coherence_only_changes_kappa(self, midpoint_state):
        """op_modulate_coherence should only change kappa."""
        result = op_modulate_coherence(midpoint_state, 0.2)
        assert result.phi == midpoint_state.phi
        assert result.tau == midpoint_state.tau
        assert result.rho == midpoint_state.rho
        assert result.H == midpoint_state.H


# =========================================================================
# 5. Boundary preservation under extreme inputs
# =========================================================================

class TestBoundaryPreservation:
    """Operators must clamp outputs to [0, 1] even at extreme inputs."""

    @pytest.mark.parametrize("name,op_func", BASIC_OPERATORS)
    def test_from_max_state(self, name, op_func, max_state):
        """From all-ones state, any magnitude should stay in bounds."""
        for mag in [-5.0, -1.0, -0.5, 0.0, 0.5, 1.0, 5.0]:
            result = op_func(max_state, mag)
            assert_valid_state(result)

    @pytest.mark.parametrize("name,op_func", BASIC_OPERATORS)
    def test_from_zero_state(self, name, op_func, zero_state):
        """From all-zeros state, any magnitude should stay in bounds."""
        for mag in [-5.0, -1.0, -0.5, 0.0, 0.5, 1.0, 5.0]:
            result = op_func(zero_state, mag)
            assert_valid_state(result)


# =========================================================================
# 6. Advanced operator: op_split_brain
# =========================================================================

class TestSplitBrain:
    """op_split_brain models corpus callosotomy.

    Framework prediction: topology bifurcates into two distinct loci,
    each with lower integration (phi) than the unified whole.
    """

    def test_returns_two_states_and_description(self, wakefulness_state):
        """op_split_brain should return (left, right, description)."""
        result = op_split_brain(wakefulness_state)
        assert len(result) == 3
        left, right, desc = result
        assert isinstance(left, StateVector)
        assert isinstance(right, StateVector)
        assert isinstance(desc, str)

    def test_both_hemispheres_have_lower_phi(self, wakefulness_state):
        """Both hemispheres must have strictly lower phi than the input."""
        left, right, _ = op_split_brain(wakefulness_state)
        assert left.phi < wakefulness_state.phi
        assert right.phi < wakefulness_state.phi

    def test_both_hemispheres_valid(self, wakefulness_state):
        """Both hemispheres must be valid StateVectors."""
        left, right, _ = op_split_brain(wakefulness_state)
        assert_valid_state(left)
        assert_valid_state(right)

    def test_both_hemispheres_lower_density(self, wakefulness_state):
        """Split hemispheres should each have lower density than the unified state."""
        left, right, _ = op_split_brain(wakefulness_state)
        original_d = wakefulness_state.density()
        assert left.density() < original_d
        assert right.density() < original_d

    def test_hemispheres_preserve_non_phi_params(self, wakefulness_state):
        """Split should preserve tau, rho, H, kappa (only phi changes)."""
        left, right, _ = op_split_brain(wakefulness_state)
        for hemi in [left, right]:
            assert hemi.tau == wakefulness_state.tau
            assert hemi.rho == wakefulness_state.rho
            assert hemi.H == wakefulness_state.H
            assert hemi.kappa == wakefulness_state.kappa


# =========================================================================
# 7. Advanced operator: op_anesthesia_gradient
# =========================================================================

class TestAnesthesiaGradient:
    """op_anesthesia_gradient models propofol-like anaesthesia.

    Framework prediction: at depth=1 (deep anaesthesia) all binding
    collapses, producing near-zero perspectival density.
    """

    def test_returns_state_and_description(self, wakefulness_state):
        """Should return (StateVector, str)."""
        result, desc = op_anesthesia_gradient(wakefulness_state, depth=0.5)
        assert isinstance(result, StateVector)
        assert isinstance(desc, str)

    def test_depth_zero_preserves_state(self, wakefulness_state):
        """At depth=0 (awake), the state should be unchanged."""
        result, _ = op_anesthesia_gradient(wakefulness_state, depth=0.0)
        assert result.phi == pytest.approx(wakefulness_state.phi)
        assert result.tau == pytest.approx(wakefulness_state.tau)
        assert result.rho == pytest.approx(wakefulness_state.rho)
        assert result.H == pytest.approx(wakefulness_state.H)
        assert result.kappa == pytest.approx(wakefulness_state.kappa)

    def test_depth_one_near_zero_density(self, wakefulness_state):
        """At depth=1 (deep anaesthesia), density should be near zero.

        The formula multiplies each param by (1 - depth*factor), so at
        depth=1 rho=0 (factor=1.0), guaranteeing D=0 via zero-elimination.
        """
        result, _ = op_anesthesia_gradient(wakefulness_state, depth=1.0)
        assert result.density() < 0.001, (
            f"Deep anaesthesia density should be near zero, got {result.density():.6f}"
        )

    def test_depth_one_produces_zero_rho(self, wakefulness_state):
        """At depth=1 the re-entrant binding (rho) should collapse to zero."""
        result, _ = op_anesthesia_gradient(wakefulness_state, depth=1.0)
        assert result.rho == pytest.approx(0.0)

    def test_increasing_depth_decreases_density(self, wakefulness_state):
        """Density must monotonically decrease as anaesthesia deepens."""
        prev_d = wakefulness_state.density()
        for depth_10 in range(1, 11):
            depth = depth_10 / 10.0
            result, _ = op_anesthesia_gradient(wakefulness_state, depth=depth)
            assert result.density() <= prev_d + 1e-10, (
                f"Density increased at depth={depth:.1f}: "
                f"{result.density():.6f} > {prev_d:.6f}"
            )
            prev_d = result.density()

    def test_valid_output_across_gradient(self, wakefulness_state):
        """Every point along the gradient should be a valid StateVector."""
        for depth_10 in range(0, 11):
            depth = depth_10 / 10.0
            result, _ = op_anesthesia_gradient(wakefulness_state, depth=depth)
            assert_valid_state(result)


# =========================================================================
# 8. Advanced operator: op_dementia_progression
# =========================================================================

class TestDementiaProgression:
    """op_dementia_progression models cognitive decline.

    Framework prediction: temporal depth (tau) is the first casualty
    as memory systems fail. Re-entrant binding of the immediate present
    persists until late stages.
    """

    def test_returns_state_and_description(self, wakefulness_state):
        """Should return (StateVector, str)."""
        result, desc = op_dementia_progression(wakefulness_state, stage=0.5)
        assert isinstance(result, StateVector)
        assert isinstance(desc, str)

    def test_stage_zero_preserves_state(self, wakefulness_state):
        """At stage=0 (healthy), the state should be unchanged."""
        result, _ = op_dementia_progression(wakefulness_state, stage=0.0)
        assert result.phi == pytest.approx(wakefulness_state.phi)
        assert result.tau == pytest.approx(wakefulness_state.tau)

    def test_advanced_stage_severely_reduces_tau(self, wakefulness_state):
        """At advanced stages, temporal depth should be severely reduced."""
        result, _ = op_dementia_progression(wakefulness_state, stage=1.0)
        assert result.tau < wakefulness_state.tau * 0.2

    def test_valid_output_across_progression(self, wakefulness_state):
        """Every stage should produce a valid StateVector."""
        for stage_10 in range(0, 11):
            stage = stage_10 / 10.0
            result, _ = op_dementia_progression(wakefulness_state, stage=stage)
            assert_valid_state(result)


# =========================================================================
# 9. Advanced operator: op_flow_state_induction
# =========================================================================

class TestFlowStateInduction:
    """op_flow_state_induction models the transition into flow.

    Flow states should increase density by boosting structure and
    coherence while reducing entropy.
    """

    def test_returns_state_and_description(self, wakefulness_state):
        """Should return (StateVector, str)."""
        result, desc = op_flow_state_induction(wakefulness_state, intensity=0.5)
        assert isinstance(result, StateVector)
        assert isinstance(desc, str)

    def test_flow_increases_density(self, midpoint_state):
        """Flow induction should increase density relative to baseline."""
        result, _ = op_flow_state_induction(midpoint_state, intensity=0.5)
        assert result.density() > midpoint_state.density()

    def test_flow_increases_phi_and_kappa(self, midpoint_state):
        """Flow should increase integration (phi) and coherence (kappa)."""
        result, _ = op_flow_state_induction(midpoint_state, intensity=0.5)
        assert result.phi > midpoint_state.phi
        assert result.kappa > midpoint_state.kappa

    def test_flow_reduces_entropy(self, midpoint_state):
        """Flow should reduce entropy (H)."""
        result, _ = op_flow_state_induction(midpoint_state, intensity=0.5)
        assert result.H < midpoint_state.H

    def test_valid_across_intensities(self, midpoint_state):
        """Every intensity level should produce a valid StateVector."""
        for intensity_10 in range(0, 11):
            intensity = intensity_10 / 10.0
            result, _ = op_flow_state_induction(midpoint_state, intensity=intensity)
            assert_valid_state(result)


# =========================================================================
# 10. Advanced operator: op_panic_induction
# =========================================================================

class TestPanicInduction:
    """op_panic_induction models onset of a panic attack.

    Panic should increase entropy with low coherence, producing
    a characteristic high-H, low-kappa signature.
    """

    def test_returns_state_and_description(self, wakefulness_state):
        """Should return (StateVector, str)."""
        result, desc = op_panic_induction(wakefulness_state, severity=0.5)
        assert isinstance(result, StateVector)
        assert isinstance(desc, str)

    def test_panic_increases_entropy(self, midpoint_state):
        """Panic should increase entropy (H)."""
        result, _ = op_panic_induction(midpoint_state, severity=0.5)
        assert result.H > midpoint_state.H

    def test_panic_decreases_coherence(self, midpoint_state):
        """Panic should decrease coherence (kappa)."""
        result, _ = op_panic_induction(midpoint_state, severity=0.5)
        assert result.kappa < midpoint_state.kappa

    def test_valid_across_severities(self, midpoint_state):
        """Every severity level should produce a valid StateVector."""
        for sev_10 in range(0, 11):
            severity = sev_10 / 10.0
            result, _ = op_panic_induction(midpoint_state, severity=severity)
            assert_valid_state(result)


# =========================================================================
# 11. Advanced operator: op_locked_in_syndrome
# =========================================================================

class TestLockedInSyndrome:
    """op_locked_in_syndrome models locked-in syndrome.

    Framework prediction: full perspectival density with zero motor output.
    The StateVector should be returned unchanged.
    """

    def test_returns_state_and_description(self, wakefulness_state):
        """Should return (StateVector, str)."""
        result, desc = op_locked_in_syndrome(wakefulness_state)
        assert isinstance(result, StateVector)
        assert isinstance(desc, str)

    def test_preserves_state_unchanged(self, wakefulness_state):
        """Locked-in should not alter the StateVector (topology intact)."""
        result, _ = op_locked_in_syndrome(wakefulness_state)
        assert result.phi == wakefulness_state.phi
        assert result.tau == wakefulness_state.tau
        assert result.rho == wakefulness_state.rho
        assert result.H == wakefulness_state.H
        assert result.kappa == wakefulness_state.kappa

    def test_preserves_density(self, wakefulness_state):
        """Density should be identical before and after."""
        result, _ = op_locked_in_syndrome(wakefulness_state)
        assert result.density() == pytest.approx(wakefulness_state.density())


# =========================================================================
# 12. Advanced operator: op_psychedelic_onset
# =========================================================================

class TestPsychedelicOnset:
    """op_psychedelic_onset models psychedelic drug effects with lag dynamics.

    Key insight: kappa lags behind H during onset, producing transient
    anxiety before coherence catches up.
    """

    def test_returns_state_and_description(self, wakefulness_state):
        """Should return (StateVector, str)."""
        result, desc = op_psychedelic_onset(wakefulness_state, intensity=0.5)
        assert isinstance(result, StateVector)
        assert isinstance(desc, str)

    def test_increases_entropy(self, midpoint_state):
        """Psychedelic onset should increase entropy (H)."""
        result, _ = op_psychedelic_onset(midpoint_state, intensity=0.5)
        assert result.H > midpoint_state.H

    def test_valid_across_intensities(self, midpoint_state):
        """Every intensity level should produce a valid StateVector."""
        for int_10 in range(0, 11):
            intensity = int_10 / 10.0
            result, _ = op_psychedelic_onset(midpoint_state, intensity=intensity)
            assert_valid_state(result)
