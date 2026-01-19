# Adversarial Test 10: κ Edge Cases

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.19 |
| Experiment ID | AT10 |
| Status | Planned |
| Framework Version | **Conduit Monism v9.3** |
| Formula Tested | D = φ × τ × ρ × [(1 - √H) + (H × κ)] |
| Test Type | Stress Test |
| Priority | HIGH |

## Abstract

The coherence gate [(1 - √H) + (H × κ)] was introduced in v8.1 to resolve the DMT Paradox (AT02). It rescued high-entropy states by allowing structured chaos (high κ) to intensify rather than dissolve experience. But the gate is the newest and least-tested component. This experiment actively seeks failure modes where high H + high κ should produce dissolution, not intensification.

## The Threat

The coherence gate claims:
- High H + Low κ → dissolution (panic, seizure)
- High H + High κ → intensification (DMT, psilocybin)

But what if:
- High H + High κ sometimes produces dissolution?
- The gate has no ceiling - can D grow unboundedly with structured chaos?
- κ is doing too much work, masking other problems?

## Hypothesis

**H0 (Gate holds)**: No high H + high κ state produces dissolution. The gate correctly distinguishes structured from random chaos.

**H1 (Gate has limits)**: Above some threshold, even structured chaos overwhelms integration capacity. A ceiling term is needed.

**H2 (Gate is broken)**: The H-κ interaction is too simple. States exist where the phenomenology contradicts the prediction.

## Pre-Defined Outcomes

### What would CONFIRM the framework?

1. All high H + high κ states produce intensification (or at least not dissolution)
2. No counterexamples found despite systematic search
3. The gate's predictions match phenomenological reports across diverse states

### What would CHALLENGE the framework?

1. Some high H + high κ states produce overwhelm/shutdown, not intensification
2. The gate needs a ceiling: beyond H > 0.9, even high κ can't rescue
3. Individual variation is so large that the gate is predictively weak

### What would BREAK the framework?

1. Multiple verified high H + high κ states with dissolution phenomenology
2. The correlation between (H, κ) and phenomenology is weak or absent
3. κ is shown to be post-hoc fitting, not a genuine structural invariant

## Candidate States to Test

| State | H (est) | κ (est) | Predicted | Phenomenology | Match? |
|-------|---------|---------|-----------|---------------|--------|
| DMT breakthrough | 0.75 | 0.90 | Intensification | Vivid, structured | ✓ |
| Psilocybin peak | 0.60 | 0.85 | Intensification | Meaningful chaos | ✓ |
| Fever delirium | 0.80 | 0.50 | Borderline | Confusion | ? |
| Seizure (partial) | 0.90 | 0.70? | Intensification? | Altered but aware | ? |
| Sensory overload | 0.85 | 0.60 | Intensification? | Overwhelm, shutdown | **Mismatch?** |
| Panic attack | 0.70 | 0.20 | Dissolution | Fragmentation | ✓ |
| Creative mania | 0.75 | 0.85 | Intensification | Racing, productive | ✓ |
| Psychotic break | 0.85 | 0.75? | Intensification? | Dissolution? | **Test** |

## Critical Test Cases

### Case 1: Sensory Overload

- Loud noise + bright lights + crowds + information flood
- H should be high (unpredictable bombardment)
- κ might be moderate (some structure in the chaos)
- Phenomenology: shutdown, withdrawal, overwhelm
- **If D is high but experience is "dissolution"** → gate fails

### Case 2: Psychotic Break

- Racing thoughts, loose associations, meaning everywhere
- H is high (unpredictable ideation)
- κ might be high (everything feels connected, meaningful)
- Phenomenology: varies - some report intensification, some dissolution
- **If κ-high predicts intensification but patient reports dissolution** → gate fails

### Case 3: Near-Death Under Stress

- Extreme danger, time dilation, life flashing
- H might be high (chaos of situation)
- κ might be high (meaningful, structured memories)
- Phenomenology: hyper-clarity or dissociation?
- **Test both predictions**

## Methodology

### Phase 1: Literature Search

Find empirical data on entropy/complexity measures in:
- Psychotic states (EEG, fMRI)
- Sensory overload paradigms
- Stress-induced dissociation
- Compare to DMT/psilocybin baselines

### Phase 2: MSE Analysis

For candidate states where data exists:
- Compute MSE slope (κ proxy)
- Compute LZc (H proxy)
- Plot H × κ against phenomenological reports

### Phase 3: Threshold Search

Systematically vary H and κ in model:
- At what H does even κ = 0.95 produce D < 0.1?
- Is there a natural ceiling, or does D grow unboundedly?
- Should the formula have: min(1.0, H × κ)?

## Sensitivity Analysis

| H | κ | Entropy Term | With φτρ = 0.5 | Interpretation |
|---|---|--------------|----------------|----------------|
| 0.50 | 0.50 | 0.54 | 0.27 | Normal waking |
| 0.70 | 0.90 | 0.80 | 0.40 | DMT-like |
| 0.90 | 0.90 | 0.86 | 0.43 | Extreme structured chaos |
| 0.95 | 0.95 | 0.93 | 0.46 | Near-maximum |
| 0.99 | 0.99 | 0.99 | 0.50 | Theoretical limit |

**Observation**: The gate approaches but never exceeds 1.0. No ceiling needed mathematically. But does phenomenology track this?

## Notes

Claude Opus noted: "The gate might need a ceiling—at some point, even structured chaos overwhelms the system's capacity to integrate it."

ChatGPT emphasized: "Dissolution needs operational definition. Is it reduced τ? Reduced ρ? Loss of stable attractors?"

The key insight is that "dissolution" might not be about the entropy term at all - it might be about φ, τ, or ρ collapsing under high entropy, regardless of κ.

## References

- Schartner, M. et al. (2017). Increased spontaneous MEG signal diversity for psychedelic doses
- Carhart-Harris, R. L. (2018). The entropic brain - revisited
- Costa, M. et al. (2002). Multiscale entropy analysis of complex physiologic time series
- AT02: DMT Paradox (260114)
- AT07: κ Validation via MSE (260118)
