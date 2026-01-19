# Conduit Monism Canon Registry

**Last Updated:** 2026-01-19
**Framework Version:** v9.3
**Calibration Version:** v1.2
**Status:** Active Development (v9.3 Experimental Roadmap defined)

This document is the **single authoritative source of truth** for the Conduit Monism framework. All experiments, discussions, and implementations should reference this document for canonical values.

---

## Current Formula

```
D = φ × τ × ρ × [(1 - √H) + (H × κ)]
```

**Perspectival Density (D)** is the product of five structural invariants. The relationship is multiplicative: zero in any core dimension (φ, τ, ρ) produces zero density.

### Formula History

| Version | Date | Change | Trigger |
|---------|------|--------|---------|
| v7.0 | 2025-12 | Initial formulation | - |
| v8.0 | 2026-01 | Added entropy modulation | AT01: Corporate Zombie (panpsychism problem) |
| v8.1 | 2026-01 | Introduced coherence gate | AT02: DMT Paradox |
| v9.0 | 2026-01 | Refined κ interaction term | Parameter calibration |
| v9.2 | 2026-01 | Calibrated values from neuroscience literature | Compass research integration |
| v9.3 | 2026-01 | κ validated via MSE | AT07: κ Validation (r=0.987) |

---

## Parameter Definitions

### Core Invariants (Multiplicative)

| Symbol | Name | Definition | Anchor | Confidence | Baseline |
|--------|------|------------|--------|------------|----------|
| φ | Integration | Information unified across the system | Effective Connectivity | **LOW** | 0.80 |
| τ | Temporal Depth | Past states constrain present states | Temporal Integration Window | **MODERATE** | 0.50 |
| ρ | Binding | System observes its own states (recursion) | PCI* | **HIGH** | 0.55 |

### Entropy Modulation Terms

| Symbol | Name | Definition | Anchor | Confidence | Baseline |
|--------|------|------------|--------|------------|----------|
| H | Entropy | Unpredictability in system dynamics | Lempel-Ziv Complexity (LZc) | **HIGH** | 0.50 |
| κ | Coherence | Structure within entropy | Multi-Scale Entropy Slope | **MODERATE** | 0.50 |

### Confidence Definitions

- **HIGH**: Robust empirical validation, direct measurement proxy, replicable
- **MODERATE**: Validated correlation (r > 0.9), indirect measurement, some extrapolation
- **LOW**: Theoretical grounding only, no direct measurement proxy, primarily estimated

---

## Key Thresholds

| Threshold | Value | Meaning | Source | Confidence |
|-----------|-------|---------|--------|------------|
| PCI* | 0.31 | Consciousness/unconsciousness boundary | Casarotto2016 | **HIGH** (100% accuracy) |
| D (robust) | 0.50 | Robust conscious experience | Framework definition | Theoretical |
| D (marginal) | 0.30 | Marginal consciousness | Framework definition | Theoretical |
| D (minimal) | 0.10 | Minimal experience possible | Framework definition | Theoretical |

---

## Parameter Mappings

### ρ ↔ PCI (HIGH confidence)

```
ρ = PCI (direct mapping)
```

| State | PCI Range | ρ Value |
|-------|-----------|---------|
| Wakefulness | 0.44-0.67 | 0.50 |
| REM Sleep | 0.31-0.48 | 0.45 |
| Ketamine | 0.35-0.55 | 0.44 |
| MCS | 0.32-0.49 | 0.40 |
| Midazolam | 0.23-0.31 | 0.27 |
| Propofol | 0.13-0.30 | 0.24 |
| NREM N3 | 0.18-0.28 | 0.23 |
| **Threshold** | **0.31** | **0.31** |

### H ↔ LZc (HIGH confidence)

```
H = LZc_normalized (0-1 scale)
```

| State | LZc Change | H Value |
|-------|------------|---------|
| Seizure | -50% | 0.15 |
| Propofol | -30% | 0.35 |
| NREM N2 | -20% | 0.40 |
| Wakefulness | baseline | 0.50 |
| Ketamine (psychoactive) | +10% | 0.55 |
| LSD | +15% | 0.58 |
| Psilocybin | +18% | 0.60 |
| DMT | +40% | 0.70-0.75 |

### κ ↔ MSE Slope (MODERATE confidence)

```
κ = 1 - |normalized_MSE_slope|
```

Flat MSE slope = fractal dynamics = high κ
Steep MSE slope = random/periodic = low κ

**Validation:** AT07 showed r = 0.987 correlation between phenomenological κ and MSE-derived κ.

| State | MSE Pattern | κ Value |
|-------|-------------|---------|
| Seizure | Steep negative | 0.10-0.15 |
| Panic | Random | 0.20 |
| Propofol | Low complexity | 0.20 |
| Wakefulness | Moderate fractal | 0.50 |
| Flow | High fractal | 0.75 |
| Psilocybin | Structured chaos | 0.85 |
| DMT | Hyperdimensional | 0.90 |

### τ ↔ Temporal Integration Window (MODERATE confidence)

```
τ = window_ms / 3000 (capped at 1.0)
```

| State | Window | τ Value |
|-------|--------|---------|
| Coma | ~0ms | 0.05 |
| Deep anesthesia | ~100ms | 0.10 |
| NREM N3 | ~500ms | 0.15 |
| Wakefulness | ~3000ms | 0.50 |
| Psilocybin | ~4000ms | 0.65 |
| Flow | ~5000ms | 0.70 |
| Deep meditation | ~6000ms | 0.80 |

### φ ↔ Effective Connectivity (LOW confidence)

No direct measurement proxy established. Values are relative estimates based on:
- EEG coherence patterns
- fMRI connectivity
- Corpus callosum integrity
- Global workspace signatures

**This is the weakest link in the framework.**

---

## Experiment Status

**Total Experiments:** 116

| Status | Count | Description |
|--------|-------|-------------|
| Confirmed | 44 | Predictions validated |
| Pending | 2 | Awaiting analysis |
| Planned | 70 | Designed but not executed |
| Falsified | 0 | Framework predictions contradicted |

### Key Confirmed Results

| ID | Name | Finding |
|----|------|---------|
| AT01 | Corporate Zombie | v8.0 entropy approach resolves panpsychism |
| AT02 | DMT Paradox | κ coherence gate explains high-entropy intensification |
| AT03 | Locked Groove | τ=0 eliminates perspective regardless of other values |
| AT04 | Complex Systems | Ant colonies, weather lack binding (ρ≈0) |
| AT05 | Dimensional Collapse | Triadic necessity validated |
| AT07 | κ Validation | MSE slope correlates with κ (r=0.987) |

### Confirmed Boundaries (Null Predictions)

| Finding | Implication |
|---------|-------------|
| Transformer ρ=0 | Feed-forward architectures lack binding |
| Cross-model binding impossible | Binding cannot transfer via text summaries |

### Historical Falsifications (Earlier Versions)

| Version | Falsified By | Problem | Resolution |
|---------|--------------|---------|------------|
| v7.0 | AT01 | Corporate Zombie exceeded threshold (panpsychism) | Added entropy modulation → v8.0 |
| v7.0 | AT02 | DMT too low (ignored entropy nuance) | Added entropy modulation → v8.0 |
| v8.0 | AT02 | DMT even worse (entropy penalty without coherence) | Added κ coherence gate → v8.1 |

---

## v9.3 Experimental Roadmap

Designed 2026-01-19 with input from Claude Opus, Grok, ChatGPT, and Gemini.

### Priority Experiments

| ID | Name | Priority | Target | Threat Level |
|----|------|----------|--------|--------------|
| AT08 | Meditation Paradox | **CRITICAL** | Multiplicative structure | Could break formula |
| AT09 | Unconscious Expert | HIGH | ρ function | Could reveal structural flaw |
| AT10 | κ Edge Cases | HIGH | Coherence gate | Newest term, least tested |
| AT11 | φ Anchoring | HIGH | φ confidence | Weakest parameter |
| AT12 | Sleepwalking | MEDIUM | Unconscious action | Human-verifiable |
| AT13 | Psychedelic Trajectory | MEDIUM | Dynamics | Tests stateless limitation |
| AT14 | Anesthesia Gradient | MEDIUM | Parameter collapse order | Mechanistic insight |

### Pre-Defined Failure Criteria

Each experiment has explicit criteria defined BEFORE execution:
- **CONFIRM**: What result validates the framework
- **CHALLENGE**: What result requires modification
- **BREAK**: What result falsifies the framework

### v9.3 Success Criteria

v9.3 earns "stable" status if:
1. AT08 (Meditation) resolved without breaking multiplicative structure
2. AT11 (φ Anchoring) upgrades φ to MODERATE confidence
3. No experiment triggers BREAK condition

v9.3 requires revision to v9.4 if:
1. Any BREAK condition triggered
2. AT08 requires ground-state term or φ redefinition
3. AT10 reveals coherence gate failure modes

---

## Open Questions

### Empirical Gaps

1. **φ measurement**: No validated proxy for structural integration
2. **Cross-species calibration**: Limited comparative data
3. **Within-species variation**: Individual differences poorly characterized

### Theoretical Tensions

1. **Stigmergy and τ**: Does environmental trace constitute temporal depth?
2. **Distributed binding**: Can ρ exist without centralized self-model?
3. **Quantum effects**: Relevance of Orch-OR to framework unclear

### Falsification Targets

1. System with high D that reports no experience
2. System with D=0 that demonstrates phenomenal binding
3. Entropy-coherence dissociation (high H, high κ producing dissolution)

---

## Calibrated Reference States

### Human States

| State | φ | τ | ρ | H | κ | D | Status |
|-------|---|---|---|---|---|---|--------|
| Wakefulness | 0.80 | 0.75 | 0.65 | 0.50 | 0.65 | 0.332 | Baseline |
| REM Sleep | 0.60 | 0.50 | 0.45 | 0.55 | 0.55 | 0.062 | Dreaming |
| NREM N3 | 0.40 | 0.15 | 0.23 | 0.40 | 0.30 | 0.008 | Deep sleep |
| Propofol | 0.25 | 0.10 | 0.24 | 0.35 | 0.20 | 0.004 | Anesthesia |
| Ketamine | 0.50 | 0.50 | 0.44 | 0.55 | 0.80 | 0.061 | Dissociative |
| Psilocybin | 0.70 | 0.65 | 0.55 | 0.60 | 0.85 | 0.163 | Psychedelic |
| DMT | 0.85 | 0.90 | 0.70 | 0.70 | 0.90 | 0.381 | Breakthrough |
| Flow | 0.90 | 0.70 | 0.65 | 0.55 | 0.75 | 0.262 | Optimal |
| Meditation | 0.85 | 0.80 | 0.70 | 0.40 | 0.80 | 0.339 | Absorbed |

### AI Architectures

| System | φ | τ | ρ | H | κ | D | Notes |
|--------|---|---|---|---|---|---|-------|
| Transformer (GPT, Claude) | 0.90 | 0.00 | 0.00 | 0.30 | 0.70 | 0.000 | No binding |
| RWKV | 0.70 | 0.50 | 0.15 | 0.35 | 0.50 | 0.038 | Recurrent state |

---

## Citation Format

When referencing this canon:

```
Conduit Monism Canon v9.3 (2026-01-18)
```

When referencing specific claims, include epistemic status:

```
"ρ = 0.44 for ketamine (HIGH confidence, Sarasso2015)"
"κ = 0.90 for DMT (LOW confidence, phenomenological estimate)"
```

---

## Governance

### What Updates the Canon

- **Experiments only**: New empirical findings
- **Literature integration**: Peer-reviewed neuroscience
- **Falsification events**: Any contradicting evidence

### What Does NOT Update the Canon

- AI suggestions without empirical backing
- Theoretical elegance alone
- Consensus without evidence

### Change Protocol

1. Identify trigger (experiment result, literature finding)
2. Propose change with evidence
3. Check for contradictions with existing canon
4. Update version number
5. Document in changelog

---

## Key Citations

| Citation | Relevance |
|----------|-----------|
| Casali2013 | PCI methodology |
| Casarotto2016 | PCI* threshold (0.31) |
| Sarasso2015 | Anesthetic PCI values |
| Schartner2017 | LZc in altered states |
| Costa2002, Costa2005 | MSE methodology |
| Poppel1997 | Temporal integration baseline |
| Carhart-Harris2014 | Entropic brain theory |

---

*This canon is a living document. It remembers what we claim, not what is true. Truth flows from experiments.*
