# Adversarial Test 13: Psychedelic Trajectory (Dynamics Test)

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.19 |
| Experiment ID | AT13 |
| Status | Planned |
| Framework Version | **Conduit Monism v9.3** |
| Formula Tested | D = φ × τ × ρ × [(1 - √H) + (H × κ)] |
| Test Type | Dynamics Test |
| Priority | MEDIUM |

## Abstract

Previous experiments tested "peaks" (AT02: DMT) and "plateaus" (AT06: Ketamine Gradient). This experiment tests **transitions** - how parameters evolve over time during a psychedelic experience. The framework currently captures instantaneous geometry; this tests whether the dynamics reveal additional structure.

## The Gap

The framework is **stateless** (acknowledged in Falsification Suite Test 4). Two systems at identical coordinates have identical D regardless of trajectory.

But phenomenology suggests trajectory matters:
- "Onset anxiety" when H spikes before κ catches up
- "Afterglow" when structure persists after entropy drops
- "Bad trip" when κ fails to rise with H

## Hypothesis

**H0 (Framework sufficient)**: Trajectory effects are fully captured by tracking D(t). No additional dynamics needed.

**H1 (Trajectory reveals structure)**: The *order* of parameter changes predicts phenomenology beyond instantaneous D.

**H2 (Framework needs dynamics)**: A derivative term or hysteresis is needed to capture trajectory-dependent effects.

## Pre-Defined Outcomes

### What would CONFIRM the framework?

1. Tracking D(t) fully explains onset/peak/comedown phenomenology
2. "Onset anxiety" is explained by D being low (H up, κ not yet up)
3. No path-dependent effects beyond what D captures

### What would CHALLENGE the framework?

1. Same D(t) curve produces different phenomenology depending on trajectory
2. Rate of change (dD/dt) is predictively important
3. Hysteresis observed: ascending D feels different from descending D

### What would BREAK the framework?

1. Trajectory effects are large and unaccounted
2. D(t) alone is poor predictor of moment-to-moment experience
3. The stateless limitation is not just acknowledged but critical

## Predicted Trajectory

Based on phenomenological reports and neuroscience:

### Typical Psilocybin Trajectory (4-6 hours)

| Time | H | κ | φ | τ | ρ | D | Phenomenology |
|------|---|---|---|---|---|---|---------------|
| T+0 (baseline) | 0.50 | 0.50 | 0.80 | 0.75 | 0.65 | 0.332 | Normal |
| T+30min (onset) | 0.60 | 0.55 | 0.75 | 0.70 | 0.60 | 0.222 | Unease, anticipation |
| T+60min (rising) | 0.70 | 0.70 | 0.70 | 0.75 | 0.55 | 0.210 | Visual distortion |
| T+90min (peak) | 0.75 | 0.85 | 0.65 | 0.80 | 0.55 | 0.229 | Full effects |
| T+3hr (plateau) | 0.65 | 0.80 | 0.70 | 0.80 | 0.60 | 0.245 | Integration |
| T+5hr (descent) | 0.55 | 0.70 | 0.75 | 0.75 | 0.65 | 0.274 | Grounding |
| T+6hr (afterglow) | 0.50 | 0.65 | 0.80 | 0.80 | 0.70 | 0.337 | Clarity |

### Critical Prediction: Onset Anxiety

**Framework prediction**: At T+30min, if H rises (0.50→0.60) but κ hasn't caught up (0.50→0.55), the entropy term shifts unfavorably:
- Entropy term at baseline: (1 - √0.50) + (0.50 × 0.50) = 0.54
- Entropy term at T+30min: (1 - √0.60) + (0.60 × 0.55) = 0.56

This is only slightly changed. The anxiety might come from:
1. **φ dropping** (losing integration)
2. **ρ dropping** (losing self-model stability)
3. **The framework missing something about transition rate**

## Methodology

### Phase 1: Model Building

Create a time-series model of parameter evolution:
- Use published pharmacokinetics (plasma levels)
- Map to parameter trajectories (assumptions documented)
- Generate D(t) curves

### Phase 2: Phenomenological Comparison

Compare D(t) predictions to:
- Trip reports with timestamps
- Subjective rating scales (if available in literature)
- Known inflection points (onset, peak, return)

### Phase 3: Hysteresis Test

Check for path dependence:
- Does D = 0.25 at T+60min (ascending) feel same as D = 0.25 at T+4hr (descending)?
- If different, what parameter captures this?

## Key Questions

1. Is "onset anxiety" explained by instantaneous D, or by dD/dt?
2. Does the framework need a "momentum" term?
3. Are there phase transitions (sudden shifts in phenomenology) at specific D thresholds?

## Failure Mode to Watch

Gemini's prediction: "If H spikes *before* κ rises, the subject should experience 'Onset Anxiety' (Panic). The framework should predict this delay."

If the framework *cannot* predict onset anxiety from instantaneous parameters alone, this suggests:
- Either we're estimating parameters wrong at onset
- Or the framework needs trajectory terms

## Notes

This experiment addresses the "stateless limitation" acknowledged in the Falsification Suite (Test 4). The current framework treats consciousness as a snapshot. This tests whether that's sufficient or whether we need video.

ChatGPT suggested "Threshold Hysteresis" (AT17 in their list) - does density show path dependence? This is related but focuses specifically on psychedelic transitions.

## References

- Carhart-Harris, R. L. et al. (2016). Neural correlates of the psychedelic state
- Roseman, L. et al. (2018). Quality of acute psychedelic experience predicts therapeutic efficacy
- Barrett, F. S. et al. (2017). Emotions and brain function are altered up to one month after a single high dose of psilocybin
- Falsification Suite (260115) - Test 4: Silent Trajectory
