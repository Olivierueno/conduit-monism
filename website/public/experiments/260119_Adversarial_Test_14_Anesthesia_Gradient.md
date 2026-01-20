# Adversarial Test 14: Anesthesia Gradient (Parameter Collapse Order)

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.19 |
| Experiment ID | AT14 |
| Status | Planned |
| Framework Version | **Conduit Monism v9.3** |
| Formula Tested | D = φ × τ × ρ × [(1 - √H) + (H × κ)] |
| Test Type | Mechanism Test |
| Priority | MEDIUM |

## Abstract

As anesthesia deepens, consciousness fades. But which parameter drops first? The framework has five dimensions - does loss of consciousness follow a characteristic path through (φ, τ, ρ, H, κ) space? Different anesthetics might take different paths, revealing the mechanism of unconsciousness.

## The Question

Propofol, ketamine, sevoflurane, and xenon all produce unconsciousness, but with different phenomenological profiles:
- Propofol: "Lights out" - sudden, complete
- Ketamine: "K-hole" - dissociative, sometimes dreamlike
- Sevoflurane: Gradual fade
- Xenon: Clean, minimal hangover

Does the framework predict these differences based on *which parameters drop first*?

## Hypothesis

**H0 (Framework predicts paths)**: Different anesthetics produce unconsciousness via different parameter trajectories. The framework distinguishes them.

**H1 (Single path)**: All anesthetics follow similar path through parameter space. D drops the same way regardless of drug.

**H2 (Framework insufficient)**: Parameter trajectories don't predict phenomenological differences. Missing dimension needed.

## Pre-Defined Outcomes

### What would CONFIRM the framework?

1. Different anesthetics show distinct parameter trajectories
2. Ketamine's preserved PCI (ρ) explains its dissociative quality
3. The path through parameter space predicts subjective experience

### What would CHALLENGE the framework?

1. All anesthetics collapse the same parameters in the same order
2. Phenomenological differences not captured by parameter differences
3. Need additional dimension (e.g., "content quality")

### What would BREAK the framework?

1. Parameters don't track anesthesia depth at all
2. D predicts unconsciousness but not the quality of fading
3. The framework can't distinguish propofol from ketamine

## Known Data Points (From Canon)

| Anesthetic | φ | τ | ρ | H | κ | D |
|------------|---|---|---|---|---|---|
| Wakefulness | 0.80 | 0.75 | 0.65 | 0.50 | 0.65 | 0.332 |
| Propofol (deep) | 0.25 | 0.10 | 0.24 | 0.35 | 0.20 | 0.004 |
| Ketamine | 0.50 | 0.50 | 0.44 | 0.55 | 0.80 | 0.061 |
| Xenon | 0.20 | 0.08 | 0.17 | 0.30 | 0.15 | 0.002 |

## Predicted Trajectories

### Propofol Trajectory (Waking → Deep)

| Depth | φ | τ | ρ | H | κ | D | Notes |
|-------|---|---|---|---|---|---|-------|
| Awake | 0.80 | 0.75 | 0.65 | 0.50 | 0.65 | 0.332 | Baseline |
| Light sedation | 0.70 | 0.60 | 0.55 | 0.45 | 0.50 | 0.138 | Drowsy |
| Moderate | 0.50 | 0.40 | 0.40 | 0.40 | 0.35 | 0.038 | Unresponsive |
| Deep | 0.25 | 0.10 | 0.24 | 0.35 | 0.20 | 0.004 | Unconscious |

**Propofol pattern**: All parameters drop roughly together. φ and τ lead slightly.

### Ketamine Trajectory (Waking → K-hole)

| Depth | φ | τ | ρ | H | κ | D | Notes |
|-------|---|---|---|---|---|---|-------|
| Awake | 0.80 | 0.75 | 0.65 | 0.50 | 0.65 | 0.332 | Baseline |
| Threshold | 0.70 | 0.65 | 0.55 | 0.55 | 0.70 | 0.171 | Mild dissociation |
| Psychoactive | 0.60 | 0.55 | 0.50 | 0.58 | 0.75 | 0.106 | K-hole onset |
| Deep K-hole | 0.50 | 0.50 | 0.44 | 0.55 | 0.80 | 0.061 | Full dissociation |

**Ketamine pattern**: ρ drops but κ rises. Creates "dissociative" quality - high entropy but structured.

## Critical Comparison

At similar D levels, do the phenomenologies differ?

| State | D | Phenomenology | Key Parameter Difference |
|-------|---|---------------|-------------------------|
| Light propofol | ~0.04 | Drowsy, fading | Low τ, low κ |
| Psychoactive ketamine | ~0.06 | Dissociative, vivid | Higher τ, higher κ |

If D ≈ 0.05 feels different under propofol vs. ketamine, the *path* matters, not just the destination.

## Methodology

### Phase 1: Literature Extraction

Gather dose-response data with EEG markers:
- PCI at various propofol concentrations
- LZc trajectory during ketamine
- Φ proxies across anesthetic depths

### Phase 2: Trajectory Modeling

For each anesthetic:
1. Map plasma concentration to parameter estimates
2. Generate trajectory through 5D parameter space
3. Identify which parameter(s) lead the collapse

### Phase 3: Phenomenological Validation

Compare trajectories to:
- Reported subjective experiences at each depth
- Known differences between anesthetic classes
- Recovery phenomenology (emergence delirium with ketamine)

## Key Questions

1. Does ρ (PCI) drop before or after φ for propofol?
2. Why does ketamine preserve ρ longer than other anesthetics?
3. Is the "lights out" quality of propofol explained by simultaneous parameter collapse?

## Notes

Claude Opus proposed this to understand the "characteristic path" through parameter space as consciousness fades. This is mechanistically important - if we know *which* parameter to protect, we might predict which anesthetics allow intraoperative awareness.

This experiment also validates the empirical calibration by testing whether known anesthetic differences map onto parameter differences.

## References

- Sarasso, S. et al. (2015). Consciousness and complexity during anesthesia
- Casali, A. G. et al. (2013). PCI methodology
- Schartner, M. et al. (2015). Complexity of multi-dimensional spontaneous EEG during propofol
- Li, D. et al. (2020). Consciousness & Brain Functional Complexity in Propofol Anaesthesia
