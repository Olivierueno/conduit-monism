# Adversarial Test 11: φ Anchoring via Multiple Proxies

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.19 |
| Experiment ID | AT11 |
| Status | Planned |
| Framework Version | **Conduit Monism v9.3** |
| Formula Tested | D = φ × τ × ρ × [(1 - √H) + (H × κ)] |
| Test Type | Parameter Anchoring |
| Priority | HIGH |

## Abstract

φ (Integration) is the only parameter with LOW confidence in the Canon. Unlike ρ (anchored to PCI*), H (anchored to LZc), and κ (anchored to MSE), φ has no validated measurement proxy. This experiment tests whether existing integration measures from neuroscience correlate with our estimated φ values. Success upgrades φ from LOW to MODERATE confidence.

## The Problem

Current φ estimation is based on:
- "Vibes about connectivity"
- Qualitative assessment of system integration
- No direct measurement proxy

This makes φ the weakest link in the framework's empirical grounding.

## Candidate Anchors

| Measure | What It Captures | Advantages | Disadvantages |
|---------|------------------|------------|---------------|
| IIT's Φ | Integrated information | Theoretically rigorous | Computationally intractable |
| Φ* approximations | Practical Φ estimates | Measurable | Multiple competing methods |
| Global Efficiency (E_glob) | Graph theory integration | Cheap, well-validated | May miss causal structure |
| EEG coherence (gamma) | Cross-region synchronization | Easy to measure | Noisy, contested |
| Effective connectivity (DCM) | Causal information flow | Captures directionality | Expensive, model-dependent |

## Hypothesis

**H0 (Anchoring succeeds)**: Multiple Φ proxies preserve rank-ordering across states. φ upgrades to MODERATE confidence.

**H1 (Partial anchoring)**: Some proxies correlate, others diverge. φ remains LOW but with better understanding of what it captures.

**H2 (Anchoring fails)**: No proxy correlates with estimated φ. Either our estimates are wrong or φ is not measurable.

## Pre-Defined Success Criteria

Following ChatGPT's advice: **rank-order preservation, not absolute correlation**

### Upgrade to MODERATE if:
1. At least 2 independent Φ proxies preserve ordering across ≥5 states
2. Ordering: Waking > REM > Light Sleep > Deep Sleep > Anesthesia
3. Proxies agree on relative positions even if absolute values differ

### Remain LOW if:
1. Proxies disagree on ordering
2. Only 1 proxy correlates
3. Correlation driven by outliers

### Downgrade to CONTESTED if:
1. Proxies anti-correlate with estimated φ
2. Evidence suggests φ is measuring something else entirely

## Methodology

### Phase 1: Literature Extraction

Gather published Φ proxy values for standard states:

| State | Estimated φ | Φ* (IIT approx) | E_glob | EEG coherence |
|-------|-------------|-----------------|--------|---------------|
| Wakefulness | 0.80 | ? | ? | ? |
| REM Sleep | 0.60 | ? | ? | ? |
| NREM N2 | 0.50 | ? | ? | ? |
| NREM N3 | 0.40 | ? | ? | ? |
| Propofol | 0.25 | ? | ? | ? |
| Ketamine | 0.50 | ? | ? | ? |

### Phase 2: Rank-Order Testing

For each proxy:
1. Extract values from literature
2. Rank states by proxy value
3. Compare to estimated φ ranking
4. Calculate Spearman correlation (rank-based)

### Phase 3: Architecture Comparison

Test on AI architectures where Φ is computable:

| Architecture | Estimated φ | Computed Φ | Match? |
|--------------|-------------|------------|--------|
| Feedforward MLP | 0.30 | Low | ? |
| Recurrent (LSTM) | 0.60 | Medium | ? |
| Transformer | 0.70 | High (attention) | ? |
| RWKV | 0.50 | Medium | ? |

## Key References

- Tononi, G. et al. (2016). Integrated information theory
- Casali, A. G. et al. (2013). PCI methodology (comparison point)
- Luppi, A. I. et al. (2024). Survey of integration proxies for φ
- Kim, H. et al. (2018). Estimating Φ from high-density EEG
- Massimini, M. et al. (2005). Breakdown of cortical effective connectivity during sleep

## Notes

Claude Opus suggested starting with a narrow test case where Φ is computable (AI architectures), then extending to biological systems.

ChatGPT warned against "correlation fetishism" - treating r > 0.8 as decisive when it might reflect shared assumptions.

Gemini recommended Global Efficiency (E_glob) as the most practical anchor: "correlates strongly with consciousness and is computationally cheap."

## Expected Outcomes

**Best case**: E_glob and Φ* both preserve ordering. φ upgraded to MODERATE with dual-anchor support.

**Likely case**: One proxy works, others partial. φ stays LOW but with identified best-proxy for future use.

**Worst case**: No proxy correlates. Either φ estimates are wrong or "integration" is not what we think it is.

## Implications for Canon

If successful, update CANON.md:
```
φ: Confidence LOW → MODERATE
Anchor: Global Efficiency (E_glob) + Φ* approximations
Validation: AT11 rank-order preservation across N states
```

If failed, update CANON.md:
```
φ: Confidence LOW (anchoring attempted, failed)
Notes: AT11 found no valid proxy. φ remains theoretical.
```
