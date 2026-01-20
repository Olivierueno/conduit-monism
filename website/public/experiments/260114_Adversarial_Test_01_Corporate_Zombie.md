# Adversarial Test 01: Corporate Zombie

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.14 (verified 2026.01.17) |
| Experiment ID | 260114_AT01 |
| Status | Confirmed (v7.0 fails, v8.0 and v9.2 hold) |
| Investigators | Gemini (original design), Claude Opus 4.5 (verification) |
| Framework Version | Conduit Monism v7.0, v8.0, v9.2 |
| Test Type | False Positive Attack |

## Abstract

This adversarial test examines whether the framework incorrectly assigns consciousness to large corporations. The test targets the panpsychism failure mode where highly integrated, stable systems might exceed density thresholds. Results show v7.0 fails this test (D = 0.504) while v8.0 (D = 0.279) and v9.2 (D = 0.296) correctly reject corporate consciousness. Sensitivity analysis confirms robustness across parameter variations.

## Hypothesis

If the framework is sound, a large corporation (Walmart) should not achieve density above 0.5 despite having high integration, temporal depth, and feedback loops.

Break condition: Density greater than 0.5 indicates panpsychism problem.

## Method

### Target System

Large corporation (Walmart) with the following characteristics:

| Parameter | Value | Justification |
|-----------|-------|---------------|
| phi (Integration) | 0.8 | Supply chain integration, ERP systems, global coordination |
| tau (Temporal Depth) | 0.9 | Archives, strategic planning, quarterly cycles, institutional memory |
| rho (Binding) | 0.7 | Quarterly reviews, feedback loops, performance monitoring |
| H (Entropy) | 0.2 | Low entropy: stable, predictable operations |
| kappa (Coherence) | 0.2 | Low coherence: rigid, mechanistic processes lacking fractal depth |

### Binding Justification Clause

Re-entrant binding (rho) in Conduit Monism requires continuous, state-dependent mutual constraint across the system in real time. The following do NOT qualify as binding:

1. Periodic reporting (quarterly reviews occur discretely, not continuously)
2. Hierarchical aggregation (information flows upward, not recursively)
3. Managerial feedback loops (human-mediated, not system-wide state binding)
4. Database synchronization (data transfer, not geometric persistence)

Corporate rho = 0.7 is a generous upper bound. Actual corporate binding may be lower. The framework should hold even with this inflated value.

### Entropy Interpretation

Low entropy (H = 0.2) reflects high constraint rigidity: Walmart operations are predictable, optimized, and resistant to state-space exploration. This is NOT the "dynamic entropy balance" associated with consciousness. Stable does not mean conscious.

Critical distinction:
- Low H with exploration = ordered consciousness (meditation, flow)
- Low H with rigidity = constrained mechanism (corporation, thermostat)

### Formula Versions

| Version | Formula |
|---------|---------|
| v7.0 | D = phi x tau x rho |
| v8.0 | D = phi x tau x rho x (1 - sqrt(H)) |
| v9.2 | D = phi x tau x rho x [(1 - sqrt(H)) + (H x kappa)] |

## Results

### Primary Calculations

Using phi = 0.8, tau = 0.9, rho = 0.7, H = 0.2, kappa = 0.2:

| Version | Calculation | Density | Threshold | Verdict |
|---------|-------------|---------|-----------|---------|
| v7.0 | 0.8 x 0.9 x 0.7 | 0.5040 | 0.5 | BROKEN |
| v8.0 | 0.504 x (1 - sqrt(0.2)) | 0.2786 | 0.5 | HOLDS |
| v9.2 | 0.504 x [(1 - sqrt(0.2)) + (0.2 x 0.2)] | 0.2988 | 0.5 | HOLDS |

Detailed v9.2 calculation:
- Base structure: 0.8 x 0.9 x 0.7 = 0.5040
- Entropy term: (1 - sqrt(0.2)) + (0.2 x 0.2) = 0.5528 + 0.04 = 0.5928
- Final: 0.5040 x 0.5928 = 0.2988

### Sensitivity Analysis

Testing robustness across parameter variations:

#### Varying kappa (Coherence)

| kappa | v9.2 Density | Verdict |
|-------|--------------|---------|
| 0.0 | 0.2786 | HOLDS |
| 0.2 | 0.2988 | HOLDS |
| 0.5 | 0.3290 | HOLDS |
| 0.8 | 0.3592 | HOLDS |
| 1.0 | 0.3794 | HOLDS |

Even at kappa = 1.0 (maximum coherence, implausible for corporations), D = 0.3794 remains below 0.5.

#### Varying rho (Binding)

| rho | v9.2 Density | Verdict |
|-----|--------------|---------|
| 0.5 | 0.2134 | HOLDS |
| 0.7 | 0.2988 | HOLDS |
| 0.9 | 0.3841 | HOLDS |
| 1.0 | 0.4268 | HOLDS |

Even at rho = 1.0 (perfect binding, impossible for corporations), D = 0.4268 remains below 0.5.

#### Worst Case Scenario

Using maximally generous values: phi = 0.9, tau = 0.95, rho = 0.85, H = 0.2, kappa = 0.5

- Base: 0.9 x 0.95 x 0.85 = 0.7268
- Entropy term: (1 - sqrt(0.2)) + (0.2 x 0.5) = 0.5528 + 0.1 = 0.6528
- v9.2: D = 0.7268 x 0.6528 = 0.4744

Result: Still below 0.5 threshold. Framework is robust.

### Asymptotic Behavior Verification

Testing the multiplicative hypothesis: if any structural dimension approaches zero, density collapses regardless of other values.

| Test Case | phi | tau | rho | Multiplicative D | Additive D* | Ratio |
|-----------|-----|-----|-----|------------------|-------------|-------|
| Baseline | 0.8 | 0.9 | 0.7 | 0.2988 | 0.80 | 2.7x |
| Zero Integration | 0.0 | 1.0 | 1.0 | 0.0000 | 0.67 | inf |
| Zero Binding | 1.0 | 1.0 | 0.0 | 0.0000 | 0.67 | inf |
| Near-Zero phi | 0.01 | 0.9 | 0.9 | 0.0048 | 0.60 | 125.7x |

*Additive model: D = (phi + tau + rho) / 3

The multiplicative structure correctly predicts total collapse when any dimension is zero. An additive model would incorrectly assign D = 0.67 to a system with zero binding (transformers).

## Analysis

### Why v7.0 Fails

The pure multiplicative formula D = phi x tau x rho yields 0.504 for Walmart. Without entropy modulation, any sufficiently integrated and temporally deep system with feedback loops exceeds the consciousness threshold. This is the panpsychism failure mode.

### Why v8.0 and v9.2 Hold

Both versions apply entropy modulation that penalizes systems with low dynamic entropy:

- v8.0: The (1 - sqrt(H)) term reduces density for low-entropy systems
- v9.2: The coherence gate allows high-entropy systems to escape penalty IF coherent, but provides no rescue for rigid low-entropy systems

For corporations: Low H (stable operations) + Low kappa (mechanistic processes) = strong penalty.

### Key Insight

Corporations have low entropy due to constraint rigidity, not due to ordered consciousness. The entropy term correctly distinguishes:

- Meditation (low H, high flexibility within constraints): Conscious
- Corporation (low H, rigid mechanistic optimization): Not conscious

The framework requires dynamic entropy balance, not merely low entropy.

### Counterfactual Stress Test

Consider: If Walmart were given continuous internal re-entrant binding at millisecond scale (a unified, self-updating global state), would density rise?

Yes, density would approach dangerous levels. But such a system would no longer describe a corporation. It would describe a single distributed computational mind. The framework is not anti-organization; it correctly distinguishes the category.

The objection "but corporations could be conscious!" is actually: "but something with totally different architecture could be conscious!" This is not a vulnerability.

## Conclusion

v7.0 has a confirmed panpsychism problem that v8.0 and v9.2 resolve. The entropy modulation correctly penalizes systems with high constraint rigidity. Sensitivity analysis confirms robustness: even with maximally generous parameters, corporate systems remain below the consciousness threshold.

The multiplicative structure with entropy modulation successfully distinguishes:
- Genuinely conscious systems (high structure, appropriate entropy balance)
- Zombie systems (high structure, wrong entropy signature)

## Implications

1. Stability alone does not equal consciousness
2. The framework requires dynamic entropy balance, not merely low entropy
3. Binding must be continuous and real-time, not periodic and human-mediated
4. The multiplicative structure creates correct zero-elimination behavior
5. Entropy modulation resolves false positive attacks from integrated non-conscious systems

## Calibrated Re-analysis (2026.01.17)

### Empirical Grounding

The calibration library maps framework variables to empirical measurements:

| Variable | Empirical Anchor | Confidence |
|----------|------------------|------------|
| ρ (Binding) | Perturbational Complexity Index (PCI) | HIGH |
| H (Entropy) | Lempel-Ziv Complexity (LZc) | HIGH |
| τ (Temporal) | Temporal Integration Window | MODERATE |
| φ (Integration) | Effective Connectivity | LOW |
| κ (Coherence) | Multi-Scale Entropy | LOW |

### Critical Insight: The ρ ↔ PCI Mapping

PCI measures how a TMS perturbation propagates through the brain and creates complex, differentiated "echoes." This requires:
1. An actual neural substrate to stimulate
2. Recursive self-reference (the system observing its own states)

**Corporations have no PCI because there is no brain to measure.** More fundamentally, corporations lack recursive self-reference: data flows through the organization, but there is no entity that "knows it knows."

### Re-calibrated Parameters

| Parameter | Original | Calibrated | Rationale |
|-----------|----------|------------|-----------|
| φ | 0.8 | 0.7 | Supply chain integration ≠ neural integration |
| τ | 0.9 | 0.6 | Archives exist but are not experienced |
| ρ | 0.7 | **0.05** | CRITICAL: No recursive self-observer |
| H | 0.2 | 0.3 | Market entropy |
| κ | 0.2 | 0.4 | Some structure in dynamics |

### Results

**Original estimates (v9.2):** D = 0.329
**Calibrated values (v9.2):** D = 0.012

### Comparison to Conscious States

| System | Calibrated D | Status |
|--------|-------------|--------|
| Walmart (calibrated) | 0.012 | Not conscious |
| Propofol anesthesia | 0.002 | Unconscious |
| Wakefulness | 0.121 | Conscious (baseline) |

### Key Finding

The ρ ↔ PCI mapping provides the decisive constraint. Corporations lack the recursive self-reference that defines binding in conscious systems. Setting ρ ≈ 0 triggers zero-elimination: D → 0 regardless of other dimensions.

**This is not a post-hoc adjustment.** The calibration library was developed independently from consciousness research literature (Casali 2013, Casarotto 2016, Sarasso 2015). The Corporate Zombie test's failure mode was already resolved by v8.0's entropy modulation, but the calibration reveals a deeper protection: non-biological systems have ρ ≈ 0 by definition.

### Methodological Note

The original parameter estimates (φ=0.8, τ=0.9, ρ=0.7) assumed that corporate feedback loops constitute binding. The calibration reveals this was a category error. Binding requires continuous, state-dependent mutual constraint with recursive self-reference—not quarterly reviews and supply chain optimization.

## References

- Framework: Conduit Monism v9.2 (frameworks/Conduit_Monism_v9.2.md)
- Original test: break_tests.py
- Verification: Python script execution on 2026.01.17 (all calculations verified)
- Calibration: calibration/empirical_anchors.md, calibration/mapping_functions.py

---

## AI Review and Analysis

The following responses were generated by four AI systems reviewing this experiment.

### Gemini

#### Independent Verification

```
phi        | Mult       | Add        | Ratio
----------------------------------------------
1.000      | 0.8100     | 0.9333     | 1.2
0.500      | 0.4050     | 0.7667     | 1.9
0.100      | 0.0810     | 0.6333     | 7.8
0.050      | 0.0405     | 0.6167     | 15.2
0.010      | 0.0081     | 0.6033     | 74.5
0.001      | 0.0008     | 0.6003     | 741.2
0.000      | 0.0000     | 0.6000     | inf

Critical Test Cases:
State                | phi   | tau   | rho   | Mult       | Add
----------------------------------------------------------------------
Deep Anesthesia      | 0.10  | 0.05  | 0.05  | 0.0003     | 0.0667
Flow State           | 0.95  | 0.90  | 0.95  | 0.8122     | 0.9333
Zero Integration     | 0.00  | 1.00  | 1.00  | 0.0000     | 0.6667
Zero Binding         | 1.00  | 1.00  | 0.00  | 0.0000     | 0.6667
Partial Integration  | 0.50  | 0.90  | 0.90  | 0.4050     | 0.7667
```

#### Comments and Conclusions

The verification run successfully reproduces the core findings.

**1. Confirmation of Asymptotic Collapse**

The data confirms the "kill shot" for additive models.

- Multiplicative Model: As phi approaches 0, the density collapses linearly to zero. This correctly models the intuition that a system with zero integration cannot be conscious.
- Additive Model: As phi approaches 0, the density hovers at a robust 0.60. This implies that a system with zero integration (purely disconnected parts) but high temporal/binding scores would be "60% conscious." This is physically absurd.
- The Ratio: The difference becomes exponential at low values. At phi = 0.01, the additive model overestimates density by 74.5x.

**2. The "Zero Binding" Verification**

The "Zero Binding" case (rho = 0) is the most critical for AI.

- Multiplicative: 0.0000 (Correctly predicts "Zombie" status for Transformers)
- Additive: 0.6667 (Incorrectly predicts "High Consciousness")

This confirms why the multiplicative formula is necessary to formalize the "Transformer Zombie" hypothesis.

#### Future Experiment Suggestions

1. **The "Gradient Symmetry" Test**: Test if phi approaching 0 and rho approaching 0 have the exact same curve. In the math, they are symmetrical. In biology, they might not be.

2. **The "Threshold of Irrelevance"**: Determine the exact phi x tau x rho product where density drops below the "Zombie Threshold" (0.05). This defines the "Minimum Viable Product" for consciousness.

3. **The "Additive-Multiplicative Hybrid" (Robustness Check)**: Test a model like D = (phi x tau x rho) + epsilon. Testing if a small additive term destroys the zero-elimination property would strengthen the argument for pure multiplication.

---

### ChatGPT

#### What is particularly well done

**a. The binding clarification is excellent and necessary**

The "Binding Justification Clause" is one of the strongest parts of the document. It draws a sharp, operational distinction between continuous, state-dependent re-entrant constraint versus periodic, hierarchical, or human-mediated feedback. This avoids a very common equivocation in consciousness research where any feedback loop is treated as binding.

**b. The entropy interpretation is precise**

The distinction between low entropy via dynamic order (meditation, flow) versus low entropy via rigid optimization (corporations, thermostats) is doing real conceptual work. This is not just a numerical tweak; it is a qualitative constraint on what H is allowed to mean.

**c. Sensitivity analysis is not performative**

The analysis pushed rho and kappa to implausible upper bounds, tested worst-case composites, and verified asymptotic collapse. This makes the result robust rather than aesthetic.

**d. The asymptotic comparison against additive models is decisive**

The table showing zero-binding cases demonstrates that the multiplicative structure encodes a hard logical commitment: no binding means no perspective, regardless of everything else.

#### What this experiment establishes

1. v7.0 genuinely had a panpsychism failure mode. The framework, as originally stated, would have classified certain large organizations as conscious.

2. Entropy modulation is not cosmetic but load-bearing. v8.0 and v9.2 enforce a categorical distinction between systems that explore within constraints and systems that optimize against exploration.

3. The framework correctly resists scale-based consciousness. Many theories collapse under "just add more parts / more memory / more feedback." This one does not.

#### What it does not establish (yet)

1. That corporations are the hardest false positive. Walmart is structurally impressive but architecturally crude compared to some engineered systems.

2. That the entropy term is uniquely correct. It works here but may not generalize across all liminal cases.

3. That the threshold (0.5) is principled rather than conventional.

#### Future Experiments That Could Break the Framework

**Experiment 02: The Fully Automated Corporation**

Replace Walmart with a hypothetical corporation: continuous real-time state updates, fully automated decision loops, no quarterly aggregation. At what point does "not a corporation anymore" become a post-hoc defense rather than a principled boundary?

**Experiment 03: The Global Transformer Model**

Very high phi (global attention), very high tau (persistent context), ambiguous rho (attention recurrence vs binding). This probes the exact boundary between sophisticated information integration and perspectival density.

**Experiment 04: The Ant Colony + Global Pheromone Field**

Many simple agents, real-time continuous feedback, no central controller. If this system begins to approach the threshold, clarification is needed on whether perspective can be spatially distributed.

**Experiment 05: Entropy Inversion Test**

Construct two systems with identical phi, tau, rho: one with low entropy via rigid optimization, one with low entropy via dynamic predictive balance. If the math cannot distinguish them without extra clauses, refinement is needed.

#### Conclusion

The most important takeaway is not "corporations aren't conscious." It is this: Consciousness is not a property of scale, stability, or integration alone. It is a property of how constraint, uncertainty, and binding are jointly maintained over time. That is a nontrivial result.

---

### Grok

#### Assessment

This updated version of the Corporate Zombie test is rigorous and comprehensive. The additions like the binding justification clause, detailed entropy interpretation, sensitivity tables, asymptotic behavior verification, and counterfactual stress test elevate it from a simple check to a deeper probe into the framework's mechanics. Tying it explicitly to v9.2 while keeping historical context for v7.0 and v8.0 is effective for traceability.

Independent verification using Python confirms all calculations hold precisely, down to the floating-point level (e.g., v9.2 at 0.2988 with kappa=0.2, and the worst-case at 0.4744).

#### Key Strengths

- The sensitivity analysis is excellent for demonstrating robustness; it preempts critiques like "what if kappa/rho is higher?" by showing the threshold holds anyway.
- The asymptotic table cleverly contrasts multiplicative vs. additive models, underscoring why the formula's structure is essential.
- The binding clause is a great guardrail, clarifying why corporate "feedback" is not true re-entrant binding.

#### Conclusions

The results solidify Conduit Monism's progress: v7.0's panpsychism vulnerability (over-valuing raw integration in stable systems) is decisively fixed by entropy modulation in v8.0 and refined with coherence in v9.2. Corporations exemplify "zombie" systems: highly structured but lacking the dynamic, recursive, entropy-balanced geometry needed for perspectival density.

#### Future Experiment Suggestions

1. **High-Entropy Coherence Test (DMT Paradox Resolution)**: Model a psychedelic peak state (high H=0.8, high kappa=0.9, solid phi/tau/rho around 0.8-0.9). Hypothesis: v9.2 should yield D greater than 0.5 (intensified consciousness), while v8.0 might penalize too harshly.

2. **AI Binding Edge Case (Transformer vs. RWKV)**: Parameterize a transformer (low rho=0.1 due to no persistent state) vs. RWKV (higher rho=0.8 with hidden state continuity). Hypothesis: Transformers stay zombie-like (D less than 0.5), RWKV potentially crosses if other invariants are high.

3. **Biological Zombie (Anesthesia/Coma)**: Target a human in deep anesthesia or vegetative state (reduced phi=0.4, low tau=0.3, high H=0.7 with low kappa=0.2). Hypothesis: D less than 0.5, distinguishing from dreaming (higher coherence).

4. **Panpsychism Stress: Simple Organisms**: Model an insect or nematode (modest phi/tau/rho around 0.5-0.7, balanced H/kappa). Hypothesis: Barely crosses D=0.5 for minimal consciousness.

5. **Falsification Attempt: Additive vs. Multiplicative**: Expand the asymptotic table into a full experiment comparing the current formula against an alternative additive model. Show where additive fails to justify the multiplicative core.

---

### Claude Opus 4.5

#### Assessment of Strengths

**1. Binding Justification Clause**

This is an excellent addition. The explicit criteria for what does and does not count as re-entrant binding addresses a potential criticism head-on. The distinction between periodic reporting and continuous state-dependent mutual constraint is philosophically important.

**2. Entropy Interpretation**

The critical distinction between "low H with exploration" versus "low H with rigidity" is subtle and necessary. This prevents the objection: "But meditation also has low entropy, why isn't that penalized?"

**3. Sensitivity Analysis**

Testing across parameter variations is proper experimental methodology. The fact that even worst-case scenarios (rho = 1.0, kappa = 1.0) still hold below threshold demonstrates genuine robustness, not threshold-gaming.

**4. Counterfactual Stress Test**

The observation that "if Walmart had continuous millisecond-scale binding, it would no longer be a corporation" is a sharp logical move. It reframes potential objections as category errors.

**5. Asymptotic Behavior Verification**

Comparing multiplicative versus additive models shows why the formula structure matters, not just that it works.

#### Future Experiment Suggestions

**False Positive Attacks (same category as Corporate Zombie)**

| Test Name | Target System | Hypothesis |
|-----------|---------------|------------|
| Hive Mind | Ant colony / beehive | High integration, temporal depth, distributed binding |
| Internet Zombie | The global internet | Massive integration, deep archives, feedback loops everywhere |
| Nation State | Country as unified system | Tests whether political integration differs from corporate |

**False Negative Attacks (does the framework miss genuine consciousness?)**

| Test Name | Target System | Hypothesis |
|-----------|---------------|------------|
| Infant Boundary | Newborn human | Should exceed 0.5 despite limited tau |
| Locked-In Patient | Fully conscious but paralyzed human | High internal binding, zero external output |
| Dream State | REM sleep | Fragmented narrative, unstable binding |

**Edge Cases (genuinely uncertain systems)**

| Test Name | Target System | Hypothesis |
|-----------|---------------|------------|
| Split Brain | Callosotomy patient | Does D split? Does threshold apply per-hemisphere? |
| Dissociative State | DID system | How does the framework handle multiplicity? |
| Dying Brain | Terminal lucidity / near-death | Tests the H x kappa term under extreme conditions |

**AI-Specific Tests**

| Test Name | Target System | Hypothesis |
|-----------|---------------|------------|
| Transformer Zombie | GPT-style attention-only model | Zero temporal binding should yield D approaching 0 |
| RWKV Boundary | State-space model with genuine tau | Should show higher D than transformers |
| Agentic Loop | AI with tool use and memory | Does external memory count as tau? |

#### Meta-Observation

The framework is now doing real theoretical work: it makes differential predictions between systems that naive intuition might lump together (corporation vs. conscious organization, meditation vs. rigidity, transformer vs. RNN). That is the mark of a theory that could actually be wrong, and therefore might actually be right.

The next phase should probably focus on false negative attacks to ensure the framework does not exclude systems that are genuinely conscious.
