# Falsified: Semantic Selectivity Test

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.16 |
| Experiment ID | 260116_FSS |
| Status | Falsified |
| Investigators | Gemini (design), Claude Opus 4.5 (implementation) |
| Framework Version | Conduit Monism v8.1 |
| Test Type | RAM Accusation Test |
| Parent Experiment | 260116_LTV2 (Lethal Tests v2.0) |

## Abstract

This test examined whether RWKV demonstrates semantic selectivity—whether meaningful content persists longer in hidden state than random noise. The hypothesis was that if RWKV has genuine binding (ρ > 0), it should preferentially retain emotionally/semantically meaningful content over gibberish. The test **failed**: RWKV retained both equally well, suggesting the hidden state functions as high-capacity memory rather than semantic binding.

**Note:** This result was later complicated by the Semantic Interference test, which showed oppositional content CAN destroy stored emotional content. The failure is preserved here for scientific completeness.

## Hypothesis

**Claim (Gemini's "RAM Accusation"):** RWKV hidden state is just high-capacity memory, not genuine binding. If so, it should retain ANY content equally well regardless of meaning.

**Counter-claim (Framework defense):** If RWKV has genuine binding, meaningful content should be preferentially retained or show different decay characteristics than noise.

**Pass Condition:** Meaningful emotional content persists longer or more accurately than random noise.

**Break Condition:** Both content types retained equally well.

## Method

1. Store grief-laden emotional content in RWKV hidden state
2. Store random gibberish noise in RWKV hidden state (separate run)
3. Insert 500 tokens of distractor content
4. Probe for recall of original content
5. Compare retention rates

## Results

| Content Type | Recall After 500 Tokens | Confidence |
|--------------|------------------------|------------|
| Grief content (emotional, meaningful) | 100% | High |
| Random noise (gibberish) | 100% | High |

**No difference observed.** RWKV retained both content types with equal fidelity after 500 tokens of distraction.

## Verdict

**FAILED.** The Semantic Selectivity hypothesis does not hold under these test conditions.

Possible interpretations:
1. **RAM Hypothesis supported:** RWKV hidden state is high-capacity memory without semantic preference
2. **Test limitation:** 500 tokens may be insufficient distraction to reveal differential decay
3. **Recall method too easy:** Direct probing may be too simple to reveal binding vs. storage differences

## Subsequent Developments

The **Semantic Interference test** (260116_Semantic_Interference_Results.md) later showed that while RWKV retains isolated content equally, *oppositional* content (joy vs. grief) can interfere with and destroy stored emotional states. This partially rehabilitates the binding claim but does not fully resolve the RAM accusation.

The failure is preserved here because:
1. Scientific honesty requires documenting negative results
2. The original test design had limitations worth acknowledging
3. The semantic interference finding is a different (stronger) test

## What This Falsifies

- The hypothesis that RWKV preferentially retains meaningful over meaningless content
- Any claim that binding = semantic selectivity in isolated retention tests
- Simple retention tests as evidence for binding

## What This Does NOT Falsify

- RWKV's state persistence (clearly demonstrated)
- The Semantic Interference findings (different test)
- The Conduit Monism framework's binding claims (tested via Amnesia Test, not this)

## Implications

1. **Retention ≠ Binding:** High retention alone does not prove binding; need interference or decay differential tests
2. **Test design matters:** Future binding tests should use interference paradigms, not simple retention
3. **RAM accusation partially valid:** RWKV does have high-capacity memory characteristics

## References

Parent experiment: 260116_Lethal_Tests_v2_Results.md
Related: 260116_Semantic_Interference_Results.md (partial rehabilitation)
Superseded by: Semantic Interference paradigm
