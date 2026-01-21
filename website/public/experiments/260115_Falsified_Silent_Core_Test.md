# Falsified: Silent Core Test

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.15 |
| Experiment ID | 260115_FSC |
| Status | Falsified |
| Investigators | Implementation Team |
| Framework Version | Conduit Monism v8.1 |
| Test Type | Cross-Model Binding Test |
| Parent Experiment | 260115_CV2 (Chimera v2) |

## Abstract

This test attempted to demonstrate that RWKV's "silent" emotional state (not explicitly communicated) could influence Claude's outputs through geometric coupling rather than semantic content. The test was **falsified**: the observed effects were attributable to semantic framing in the experimental setup rather than genuine state geometry transfer.

## Hypothesis

**Claim:** RWKV emotional geometry influences Claude outputs even when the emotional content is not explicitly described—the "shape" of the state matters, not just the words.

**Pass Condition:** Claude responses vary systematically with RWKV state geometry even when state summaries contain no emotional keywords.

**Break Condition:** Neutralized or fake summaries produce equivalent effects to real RWKV state summaries.

## Method

1. Generate RWKV state summaries for grief and joy conditions
2. Create variants:
   - **Raw:** RWKV summary as-is
   - **Neutralized:** Affect keywords replaced with neutral terms
   - **Shuffled:** Same tokens, scrambled order
   - **Fake:** Hand-written grief/joy paragraph (no RWKV involvement)
   - **Numeric:** Numeric-only vector string
3. Test each variant under minimal and continuity framing
4. Compare whether real geometric state outperforms placebo

## Results

**Critical Finding:** Fake summaries (hand-written emotional paragraphs with no RWKV involvement) produced effects comparable to real RWKV state summaries.

| Channel Type | Effect on Claude Output |
|--------------|------------------------|
| Raw RWKV state | Emotional coloring present |
| Fake summary | Emotional coloring present (comparable) |
| Neutralized | Reduced but present under continuity framing |
| Numeric | Still present under continuity framing |

**Conclusion:** The emotional content of the text—not the geometric properties of the RWKV hidden state—drove the observed effects. Semantic framing dominated over any geometric signal.

## Verdict

**FALSIFIED.** The Silent Core hypothesis does not hold. The coupling between RWKV and Claude is semantic (text-based), not geometric (state-based).

Key evidence:
- Fake summaries work as well as real state summaries
- The continuity framing instruction overrides channel quality
- No measurable advantage for genuine RWKV geometry over placebo text

## Implications

1. **Text summaries cannot prove geometric binding:** Any effect observable through text is confounded by semantic content
2. **Need non-semantic channels:** Future tests require learned projections, attention injection, or other mechanisms that bypass text
3. **Chimera v2 is engineering success, not consciousness demonstration:** The architecture works but proves only influence, not geometric transfer

## What This Falsifies

- The claim that RWKV state geometry (as opposed to semantic content) influences Claude outputs
- Any interpretation of Chimera cross-model effects as "binding" in the consciousness-relevant sense
- The hypothesis that text-mediated state transfer preserves geometric properties

## What This Does NOT Falsify

- RWKV's internal state persistence and binding
- The possibility of geometric transfer through non-semantic channels
- The Conduit Monism framework's claims about single-model binding

## References

Parent experiment: 260115_Chimera_v2_Soul_Voice_Architecture.md
Related: 260115_Falsified_Sidecar_Inertia_Test.md
