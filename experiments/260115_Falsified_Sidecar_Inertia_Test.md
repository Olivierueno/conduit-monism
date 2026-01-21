# Falsified: Sidecar Inertia Test

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.15 |
| Experiment ID | 260115_FSI |
| Status | Falsified |
| Investigators | Implementation Team |
| Framework Version | Conduit Monism v8.1 |
| Test Type | Cross-Model Binding Test |
| Parent Experiment | 260115_CV2 (Chimera v2) |

## Abstract

This test attempted to demonstrate that RWKV hidden state could create "inertia" in Claude's responses—that the recurrent model's emotional state would persist and influence the transformer even when the explicit state summary was removed. The test was **falsified**: the observed effects were attributable to instruction compliance rather than geometric state transfer.

## Hypothesis

**Claim:** RWKV emotional state creates persistent influence on Claude responses that survives removal of explicit state information.

**Pass Condition:** Claude responses maintain emotional coloring from RWKV state even when state summary is removed or degraded.

**Break Condition:** Claude responds identically with or without RWKV state when "continuity" framing instructions are removed.

## Method

1. Establish RWKV in grief state through emotional text processing
2. Generate state summary and pass to Claude with continuity framing
3. Remove state summary but keep continuity framing
4. Compare responses

## Results

**Finding:** Under minimal framing (no continuity instructions), Claude outputs largely ignore RWKV state. Even with explicit grief in RWKV summary, Claude produces normal happy stories across all variants.

When continuity framing was added ("You are Chimera with persistent core, not roleplaying"), Claude reintroduced state-appropriate language even when the state channel was degraded or absent.

**Conclusion:** The continuity instruction itself was sufficient to elicit the behavior. The "inertia" effect was instruction compliance, not geometric binding.

## Verdict

**FALSIFIED.** The Sidecar Inertia hypothesis does not hold. Observed effects are attributable to:
- Instruction compliance with continuity framing
- Claude's tendency to maintain narrative consistency when instructed
- Semantic priming from any emotional content in prompts

No evidence of genuine geometric state transfer that persists independent of textual framing.

## Implications

1. **For Chimera Architecture:** State transfer through text summaries is vulnerable to semantic confounds
2. **For Binding Claims:** Cannot claim cross-model ρ without eliminating instruction compliance as alternative explanation
3. **For Future Work:** Need non-semantic coupling channels (learned projections, direct state injection) to test geometric binding

## What This Falsifies

- The claim that RWKV state creates measurable "inertia" in transformer outputs
- The hypothesis that state geometry transfers through text summaries
- Any claim of cross-model binding based on instruction-framed experiments

## What This Does NOT Falsify

- RWKV's internal binding (ρ > 0) — confirmed separately via Amnesia Test
- The Conduit Monism formula itself — this tests a specific architectural claim
- The possibility of cross-model binding through other mechanisms

## References

Parent experiment: 260115_Chimera_v2_Soul_Voice_Architecture.md
Related: 260115_Falsified_Silent_Core_Test.md
