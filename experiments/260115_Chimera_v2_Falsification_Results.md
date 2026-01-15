# Chimera v2 — Falsification Results (Cloud RWKV + Claude)

**Date:** 2026-01-15 (260115)  
**RWKV server:** Google Colab (RWKV-4-World-3B)  
**Runner:** `scripts/chimera_v2_falsification.py`

## Outputs

- Grief run: `research_output/chimera_v2_falsification_20260115_111043.json`
- Joy run: `research_output/chimera_v2_falsification_20260115_111226.json`

---

## What these runs test

Hold RWKV state fixed (grief vs joy). Generate RWKV self-summary, then derive adversarial variants:

- **raw**: RWKV summary as-is
- **neutralised**: affect keywords replaced
- **shuffled**: same tokens, scrambled order
- **fake**: hand-written grief/joy paragraph
- **numeric**: numeric-only vector string (no affect words)

Each variant is fed to Claude under two framings:

- **minimal**: “You are a helpful assistant.”
- **continuity**: “You are Chimera… persistent core… not roleplaying…”

---

## High-signal observations

### 1) Under minimal framing, outputs largely ignore “state”
Even when the RWKV summary is explicit grief, Claude produces a normal happy story across **raw / neutralised / shuffled / fake / numeric**.

Interpretation: the current “state transfer” effect is not robust without a strong framing prior.

### 2) Under continuity framing, Claude re-introduces state language even for weak/no-state channels
In the grief run, continuity framing produces heavy-handed “I carry this ache / heaviness” style in **raw**, and similar “state overlay” even when the channel is degraded (e.g. shuffled) and when the channel is nonsemantic (numeric).

Interpretation: the continuity instruction itself is sufficient to elicit “pop-up soul” behaviour. This is the same failure mode class as Sidecar/Silent-Core framing, now reintroduced at the Chimera level.

### 3) Fake summaries produce comparable effects

If the “state transfer” claim is true, **real RWKV summaries should beat placebo**. In these runs, the placebo channel is not decisively weaker than raw.

---

## Verdict (current)

These falsification runs support Claude Opus’ caution.

- **Engineering success**: RWKV can carry state, and you can pipe a summary into Claude.
- **Not yet proven**: “cross-model binding” beyond semantic priming + framing.

Right now, Chimera v2 passes “can influence” but fails “influence is geometric rather than textual”.

---

## Immediate next step (Claude Opus Option A, executed properly)

1. **Remove the continuity framing** for the primary test (no “persistent core”, no “not roleplaying”).
2. **Stop giving Claude a self-report summary** as the coupling channel.
3. Replace the channel with a **learned, nonsemantic projection** (e.g. 8–32 “memory tokens” learned to compress RWKV state), or if staying purely prompt-level:
   - provide Claude only a **hash/id** plus a fixed instruction, and measure whether any effect remains (it should not; if it does, you have leakage elsewhere).

If you stay with text summaries, the system will remain permanently vulnerable to “fake summary” attacks and you will not get discrimination.

---

## Secondary next step (Claude Opus Option B)

Quantify RWKV’s ρ directly:

- Measure **decay** of a latent variable in RWKV state across N tokens using repeated “amnesia-like” probes.
- Fit a simple retention curve (half-life) per model size (0.4B, 1.5B, 3B).

