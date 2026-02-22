# Critical Analysis: Formula Properties and Theoretical Vulnerabilities

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026-02-22 |
| Author | Claude Opus 4.6 |
| Status | ANALYSIS (not an adversarial test -- a structural examination) |
| Framework Version | Conduit Monism v9.3.1 (Canon 2026-01-20) |
| Scope | Mathematical properties, logical vulnerabilities, falsification criteria |

## Abstract

This document provides a rigorous mathematical and epistemological analysis of the Conduit Monism formula D = phi x tau x rho x [(1 - sqrt(H)) + (H x kappa)]. Rather than testing a specific prediction, it examines the formula's structural properties, sensitivity landscape, degeneracy problems, and logical vulnerabilities. The goal is constructive: to identify where the framework is genuinely strong, where it is genuinely weak, and what would be required to move it from "internally consistent theoretical model" to "empirically testable scientific theory."

---

## I. Mathematical Properties of the Formula

### 1. Range Analysis: The Theoretical Maximum of D

The formula is:

```
D = phi x tau x rho x g(H, kappa)
```

where g(H, kappa) = (1 - sqrt(H)) + (H x kappa) is the entropy gate.

All parameters lie in [0, 1]. The structural prefix phi x tau x rho is maximized when phi = tau = rho = 1, giving a prefix of 1.0. The question reduces to: **what is the maximum of g(H, kappa) on [0,1] x [0,1]?**

To find the maximum of g, take the partial derivative with respect to H and set it to zero:

```
dg/dH = -1/(2*sqrt(H)) + kappa
```

Setting dg/dH = 0:

```
kappa = 1/(2*sqrt(H))
sqrt(H) = 1/(2*kappa)
H* = 1/(4*kappa^2)
```

For this critical point to lie within [0,1], we need H* <= 1, which requires kappa >= 1/2 = 0.5.

At the critical point H* = 1/(4*kappa^2), the gate value is:

```
g(H*, kappa) = (1 - sqrt(1/(4*kappa^2))) + (1/(4*kappa^2)) * kappa
             = (1 - 1/(2*kappa)) + 1/(4*kappa)
             = 1 - 1/(2*kappa) + 1/(4*kappa)
             = 1 - 1/(4*kappa)
```

This is an increasing function of kappa. At kappa = 1:

```
g_max = 1 - 1/4 = 3/4 = 0.75
```

occurring at H* = 1/(4 * 1^2) = 0.25.

We must also check the boundary values:

- At H = 0: g(0, kappa) = (1 - 0) + (0 * kappa) = 1.0
- At H = 1: g(1, kappa) = (1 - 1) + (1 * kappa) = kappa, maximum kappa = 1.0

**The boundary H = 0 gives g = 1.0, which exceeds the interior critical value of 0.75.**

However, there is a subtlety. At H = 0, kappa is phenomenologically constrained: if there is no entropy, there is nothing to cohere. The framework states "kappa cannot be high when H is low." If we enforce this constraint, then at H = 0, kappa should also be 0 or near-zero, but the gate value g(0, kappa) = 1.0 regardless of kappa (the kappa term vanishes when H = 0).

**Therefore, the theoretical maximum of D is exactly 1.0**, achieved when:

```
phi = 1, tau = 1, rho = 1, H = 0, kappa = any value
```

This corresponds to a perfectly integrated, temporally deep, fully self-referential system with zero entropy -- a system in a state of absolute crystalline order. The gate g(0, kappa) = 1.0 because the (1 - sqrt(H)) term reaches its maximum.

**But this is phenomenologically problematic.** A zero-entropy system is a frozen crystal, a state with no dynamics at all. The formula assigns it maximal consciousness. Deep meditation (low H, high structure) gets high D by this logic, but H = 0 literally means complete predictability -- rigor mortis, not samadhi.

If we exclude the degenerate H = 0 case and consider only H > 0:

**Interior maximum of g:** For kappa = 1 and H = 0.25:

```
D_max = 1.0 x 1.0 x 1.0 x 0.75 = 0.75
```

**The practically meaningful maximum of D is 0.75**, not 1.0. This occurs at (phi, tau, rho, H, kappa) = (1, 1, 1, 0.25, 1).

For the calibrated reference states, the highest D in the canon is DMT breakthrough at 0.381. This uses the canon values (0.85, 0.90, 0.70, 0.70, 0.90). The theoretical ceiling of 0.75 means the most extreme human state occupies roughly 51% of the formula's practical dynamic range.

**Summary of D range:**

| Condition | Maximum D | Parameters |
|-----------|-----------|------------|
| Unconstrained theoretical | 1.000 | (1, 1, 1, 0, any) |
| Interior maximum (H > 0) | 0.750 | (1, 1, 1, 0.25, 1) |
| Highest calibrated state (DMT) | 0.381 | (0.85, 0.90, 0.70, 0.70, 0.90) |
| Wakefulness baseline | 0.332 | (0.80, 0.75, 0.65, 0.50, 0.65) |
| Consciousness threshold (~PCI* = 0.31) | ~0.008-0.02 | Various unconscious states |

### 2. Entropy Gate Behavior

The entropy gate g(H, kappa) = (1 - sqrt(H)) + H*kappa is the most mathematically interesting component of the formula. It mediates between two regimes:

- **Low entropy (H near 0):** The (1 - sqrt(H)) term dominates, approaching 1.0. Low entropy = high gate = good for consciousness.
- **High entropy (H near 1):** The (1 - sqrt(H)) term collapses toward 0, but H*kappa can partially rescue the gate if kappa is high.

#### Partial Derivatives

```
dg/dkappa = H
```

This is remarkably simple: **the leverage of kappa is exactly H.** At low entropy, kappa does nothing. At high entropy, kappa has maximum leverage. This is by design -- kappa only matters when there is entropy to structure -- but its linearity is notable.

```
dg/dH = -1/(2*sqrt(H)) + kappa
```

This derivative is always negative when kappa < 1/(2*sqrt(H)), meaning increasing entropy hurts. It is positive when kappa > 1/(2*sqrt(H)), meaning increasing entropy helps. The crossover occurs at:

```
H_crossover = 1/(4*kappa^2)
```

| kappa | H_crossover | Interpretation |
|-------|-------------|----------------|
| 0.10 | 25.00 (>1, never) | Entropy always hurts |
| 0.20 | 6.25 (>1, never) | Entropy always hurts |
| 0.30 | 2.78 (>1, never) | Entropy always hurts |
| 0.50 | 1.00 (boundary) | Entropy always hurts (within domain) |
| 0.60 | 0.694 | Entropy helps above H = 0.694 |
| 0.70 | 0.510 | Entropy helps above H = 0.510 |
| 0.80 | 0.391 | Entropy helps above H = 0.391 |
| 0.90 | 0.309 | Entropy helps above H = 0.309 |
| 1.00 | 0.250 | Entropy helps above H = 0.250 |

**Key insight:** For kappa <= 0.5, increasing entropy ALWAYS reduces the gate (and thus D). Only when kappa > 0.5 can entropy become beneficial, and only above a threshold H value. This is the mathematical mechanism behind the "coherence rescues entropy" claim.

At the wakefulness baseline (kappa = 0.65), the crossover is at H = 1/(4 * 0.65^2) = 0.592. This means for a normally alert person, entropy would need to exceed 0.592 before more chaos starts helping -- which is roughly at the level of psilocybin (H = 0.60). This is a satisfying result: it predicts that mild increases in entropy (stress, distraction) reduce clarity, while psychedelic-level entropy with high coherence can enhance it.

#### Saddle Point Analysis

The entropy gate g(H, kappa) has no saddle point in the strict sense (it is linear in kappa). Its second derivatives are:

```
d^2g/dH^2 = 1/(4*H^(3/2))   (always positive for H > 0: convex in H)
d^2g/dkappa^2 = 0             (linear in kappa: no curvature)
d^2g/dH*dkappa = 1            (constant mixed partial)
```

The Hessian determinant is:

```
det(Hess) = (1/(4*H^(3/2))) * 0 - 1^2 = -1
```

**The Hessian determinant is always -1**, which is always negative. This means every critical point of g(H, kappa) in the interior is a **saddle point**. There is no interior local maximum or minimum of the gate function -- it is a saddle surface everywhere.

This has an important geometric interpretation: the entropy gate is shaped like a Pringles chip. You cannot simultaneously optimize H and kappa to find a local peak. Every attempt to increase the gate by adjusting one variable can be undone by the other. The true optima are always on the boundary of the domain.

#### Singularities and Discontinuities

The term -1/(2*sqrt(H)) in dg/dH diverges as H approaches 0. This means:

1. The gate function has **infinite slope** at H = 0 -- it drops very steeply for even tiny amounts of entropy.
2. The formula's sensitivity to entropy is **extremely high** near H = 0 and decreases as H increases.

Concretely, going from H = 0.00 to H = 0.01 reduces the gate from 1.000 to 0.900 + 0.01*kappa, a drop of about 0.10. Going from H = 0.50 to H = 0.51 reduces the gate from 0.293 + 0.50*kappa to 0.286 + 0.51*kappa, a net change of about -0.007 + 0.01*kappa. The first interval of 0.01 in H costs 14x more than the same interval around H = 0.50.

This is a design choice with consequences: the formula is **hypersensitive to the onset of entropy** but relatively tolerant of high-entropy states if kappa is high. Whether this matches phenomenology is an empirical question. Does the first hint of neural noise destroy consciousness more than the difference between mild and extreme chaos? Possibly yes for anesthesia (where initial signal degradation rapidly eliminates awareness) but the infinite derivative at H = 0 is a mathematical artifact that creates numerical instability near the boundary.

### 3. Sensitivity Hierarchy at the Wakefulness Baseline

The canon wakefulness baseline is (phi, tau, rho, H, kappa) = (0.80, 0.75, 0.65, 0.50, 0.65).

First, compute the baseline density:

```
Structure = 0.80 x 0.75 x 0.65 = 0.39
Gate = (1 - sqrt(0.50)) + (0.50 x 0.65) = (1 - 0.7071) + 0.325 = 0.2929 + 0.325 = 0.6179
D = 0.39 x 0.6179 = 0.24098
```

**Note:** The CANON.md lists wakefulness D = 0.332, but this appears to use different parameter values than (0.80, 0.75, 0.65, 0.50, 0.65). Let me recompute with the values from the Canon's reference table:

```
D = 0.80 x 0.75 x 0.65 x [(1 - sqrt(0.50)) + (0.50 x 0.65)]
  = 0.39 x [0.29289 + 0.325]
  = 0.39 x 0.61789
  = 0.24098
```

This gives D = 0.241, not 0.332. There appears to be an internal inconsistency in the canon -- the listed D values may have been computed with a different parameter set than the one tabulated. This is itself a finding worth noting.

**Proceeding with the tabulated parameters (0.80, 0.75, 0.65, 0.50, 0.65):**

The partial derivatives of D with respect to each parameter at this baseline:

```
dD/dphi = tau * rho * g(H,kappa) = 0.75 x 0.65 x 0.6179 = 0.30122
dD/dtau = phi * rho * g(H,kappa) = 0.80 x 0.65 x 0.6179 = 0.32131
dD/drho = phi * tau * g(H,kappa) = 0.80 x 0.75 x 0.6179 = 0.37074
dD/dH   = phi * tau * rho * [-1/(2*sqrt(H)) + kappa]
        = 0.39 x [-1/(2*sqrt(0.50)) + 0.65]
        = 0.39 x [-0.7071 + 0.65]
        = 0.39 x (-0.0571)
        = -0.02227
dD/dkappa = phi * tau * rho * H = 0.39 x 0.50 = 0.19500
```

**Sensitivity ranking (absolute values):**

| Rank | Parameter | dD/dX | Interpretation |
|------|-----------|-------|----------------|
| 1 | rho (Binding) | 0.371 | Most leverage |
| 2 | tau (Temporal Depth) | 0.321 | Second most |
| 3 | phi (Integration) | 0.301 | Third |
| 4 | kappa (Coherence) | 0.195 | Moderate |
| 5 | H (Entropy) | -0.022 | **Near-zero leverage** |

**This reveals a striking asymmetry.** At the wakefulness baseline, entropy has almost no effect on D. A small change in H barely moves the needle because dg/dH = kappa - 1/(2*sqrt(H)) = 0.65 - 0.707 = -0.057, which is near zero. The entropy gate is near its saddle point at these values.

The structural parameters (phi, tau, rho) each have roughly 15-19x more leverage than entropy. Coherence (kappa) has about 9x more leverage than entropy.

For **normalized sensitivity** (elasticity: percent change in D per percent change in parameter):

```
Elasticity_phi   = (dD/dphi) * (phi/D) = 0.301 x (0.80/0.241) = 1.000
Elasticity_tau   = (dD/dtau) * (tau/D) = 0.321 x (0.75/0.241) = 1.000
Elasticity_rho   = (dD/drho) * (rho/D) = 0.371 x (0.65/0.241) = 1.000
Elasticity_H     = (dD/dH)  * (H/D)   = -0.022 x (0.50/0.241) = -0.046
Elasticity_kappa = (dD/dkappa) * (kappa/D) = 0.195 x (0.65/0.241) = 0.526
```

**The elasticities of the three structural parameters are exactly 1.0.** This is not coincidence -- it follows from the multiplicative structure. In D = phi * tau * rho * g(H, kappa), a 1% increase in any multiplicative factor produces exactly a 1% increase in D. This is a mathematically necessary consequence of the formula's design, not an empirical finding.

The elasticity of kappa (0.526) means a 1% increase in coherence produces only a 0.53% increase in density at baseline. The near-zero elasticity of H (-0.046) confirms that at baseline, entropy is essentially inert.

### 4. The Degeneracy Problem

The formula maps a 5-dimensional parameter space (phi, tau, rho, H, kappa) to a 1-dimensional output D. This means the **level sets** of D -- the set of all parameter combinations producing a given density value -- are 4-dimensional hypersurfaces.

For any given D value, there are uncountably infinite parameter combinations that produce it. Here are concrete examples of distinct phenomenological states that produce nearly identical D values:

#### Example Set A: D approximately equals 0.062

| State | phi | tau | rho | H | kappa | D | Phenomenology |
|-------|-----|-----|-----|---|-------|---|---------------|
| REM Sleep | 0.60 | 0.50 | 0.45 | 0.55 | 0.55 | 0.062 | Loose narrative, strange logic |
| Ketamine | 0.50 | 0.50 | 0.44 | 0.55 | 0.80 | 0.061 | Dissociative void, ego dissolution |

These states produce almost identical D values but represent radically different phenomenologies. REM sleep involves passive narrative dreaming; ketamine involves active dissociation with preserved (but altered) meta-awareness. The formula cannot distinguish them.

#### Example Set B: Constructed degeneracy

Consider D = 0.24 (near wakefulness):

| Configuration | phi | tau | rho | H | kappa | D |
|---------------|-----|-----|-----|---|-------|---|
| Config 1 | 0.80 | 0.75 | 0.65 | 0.50 | 0.65 | 0.241 |
| Config 2 | 0.65 | 0.65 | 0.65 | 0.20 | 0.50 | 0.239 |
| Config 3 | 0.50 | 0.50 | 1.00 | 0.30 | 0.90 | 0.237 |

Config 1 is normal wakefulness. Config 2 has less integration and temporal depth but much lower entropy. Config 3 has half the integration and temporal depth but maximal binding and high coherence. These are topologically distinct configurations in parameter space, yet the formula treats them as approximately equivalent.

#### Degrees of Freedom Analysis

The system has 5 free parameters producing 1 output. This means:

- **Degrees of freedom in parameters:** 5
- **Degrees of freedom in output:** 1
- **Degrees of freedom lost (degeneracy):** 4

Four dimensions of phenomenological variation are collapsed into the single number D. The formula intentionally discards:

1. **Valence** -- whether experience is pleasant or painful (acknowledged gap)
2. **Content type** -- what the experience is about
3. **Temporal dynamics** -- how the state evolves (partially addressed by AT13 lag modeling)
4. **Internal structure of the parameter combination** -- which specific parameters are contributing to D

This is not necessarily a flaw -- any scalar measure of consciousness must compress information. Temperature is a scalar that compresses the kinetic energy distribution of billions of molecules. But the degeneracy means **D is not a sufficient statistic for phenomenology.** Two states with identical D can feel completely different. D measures intensity, not character.

The question is whether D is intended to measure only intensity. The framework says it measures "how intensely experience is occurring" -- perspectival density. If this is genuinely all it claims, then the degeneracy is a feature, not a bug. But in practice, the framework frequently makes claims about the *quality* of experience based on D values (e.g., "DMT should be high because it feels more real than real"), which blurs the line between intensity and character.

---

## II. Logical Vulnerabilities

### 1. Post-Hoc Fitting

The formula's development history is explicitly documented:

| Version | Problem | Fix |
|---------|---------|-----|
| v7.0 (D = phi x tau x rho) | Corporate zombie scored too high (panpsychism) | Added entropy modulation |
| v8.0 (D = phi x tau x rho x (1 - sqrt(H))) | DMT scored too low (entropy penalty without nuance) | Added kappa coherence gate |
| v8.1 (current formula) | Stable | -- |

This is a classic case of **post-hoc parameter introduction.** Each time the formula produced a result that conflicted with phenomenological expectations, a new term was added to fix it. The procedure was:

1. Assign parameter values based on what a state "should feel like"
2. Compute D
3. Check if D matches what the state "should score"
4. If not, modify the formula
5. Return to step 2

This is not inherently illegitimate -- Kepler's laws were also refined iteratively to match observations. But there is a critical difference: **Kepler's observations were independent of his model.** Planetary positions were measured by Tycho Brahe before Kepler proposed his laws. The data existed before the theory.

In Conduit Monism, the "observations" (what states "should" score) are themselves theory-laden. The claim that DMT "should" score high because it feels intense is not an independent measurement -- it is a phenomenological judgment that may itself be wrong, biased, or poorly calibrated.

**What would make it different from curve-fitting:**

1. **Prospective prediction.** If the formula, with its current fixed parameters and structure, correctly predicts the density of a novel state *before* the parameter values for that state are assigned, this breaks the circularity. AT13 (psychedelic trajectory simulation) partially achieves this by showing that lag dynamics produce the expected onset-anxiety/breakthrough/afterglow arc without formula modification. But the parameter values were still assigned with knowledge of the expected outcome.

2. **Independent parameter measurement.** If phi, tau, rho, H, and kappa were measured by instruments (PCI, LZc, etc.) without reference to the framework, and the resulting D matched phenomenological rankings, this would be strong evidence. Currently, only rho (via PCI) and H (via LZc) have genuinely independent empirical anchors. The others are estimated from phenomenology.

3. **Competitive prediction.** If the formula outperforms alternative formulas (e.g., additive instead of multiplicative, different entropy functions) at predicting independent data, this distinguishes genuine structure from overfitting.

Currently, the framework is in a state between curve-fitting and genuine prediction. The post-hoc introduction of kappa is the most concerning element, because it was introduced specifically to resolve a single anomaly (DMT) and its empirical grounding (MSE slope, r = 0.987) was obtained by correlating MSE values with phenomenologically-assigned kappa values -- not independently.

### 2. The Kappa Problem

Kappa is the framework's most vulnerable parameter. Consider its epistemic status:

| Property | Status |
|----------|--------|
| Introduced to solve | DMT paradox (AT02) |
| Empirical anchor | MSE slope (Multi-Scale Entropy) |
| Anchor confidence | MODERATE (self-assessed) |
| Independent validation | r = 0.987 between phenomenological kappa and MSE kappa (AT07) |
| Direct measurement for any state | None |
| Number of states with empirical kappa | 0 (all are phenomenological estimates) |

The r = 0.987 correlation sounds impressive, but examine what it actually demonstrates. It shows that if you assign kappa values based on whether a state "feels structured" and then check whether Multi-Scale Entropy patterns match, you get high correlation. But this could mean:

**(a)** Kappa is a genuine variable that MSE captures -- the optimistic interpretation.

**(b)** The phenomenological assignment of kappa implicitly tracked MSE-like properties because the researchers knew about multi-scale entropy -- a confirmation bias interpretation.

**(c)** MSE and phenomenological "structuredness" are both driven by a third variable (e.g., serotonergic tone), and kappa is an epiphenomenal label for something more fundamental -- a confound interpretation.

The critical test for kappa would be: **assign kappa values from MSE data alone, with no knowledge of phenomenology, and check whether the resulting D values match subjective reports.** This has not been done.

Without kappa (setting kappa = 0), the formula becomes:

```
D = phi x tau x rho x (1 - sqrt(H))
```

This predicts that DMT (H = 0.70) has gate value (1 - sqrt(0.70)) = 0.163, giving D = 0.85 x 0.90 x 0.70 x 0.163 = 0.088. Compare to wakefulness D = 0.80 x 0.75 x 0.65 x (1 - sqrt(0.50)) = 0.39 x 0.293 = 0.114. DMT scores *lower* than wakefulness without kappa, which contradicts phenomenological reports.

So kappa is load-bearing. Without it, the formula fails for psychedelic states. The question is whether it is a genuine structural variable or an ad hoc fix.

**Arguments that kappa is genuine:**
- Multi-Scale Entropy is a well-established measure in the complexity science literature (Costa et al. 2002, 2005)
- The distinction between "structured chaos" and "random noise" has independent mathematical foundations (fractal dimension, 1/f scaling)
- Phenomenological reports consistently distinguish psychedelic states (meaningful, geometric, coherent) from seizures (meaningless, stereotyped) despite both being high-entropy
- Carhart-Harris's Entropic Brain Hypothesis (2014) independently identified the need to distinguish entropy types

**Arguments that kappa is a patch:**
- It was introduced specifically to fix one anomaly
- Its values for specific states are all phenomenologically assigned
- The MSE validation was performed by the same research group that introduced kappa
- The formula provides kappa with a free parameter that can be tuned to fit any anomalous state
- No prospective prediction using kappa has been made and tested

**Verdict:** Kappa is in epistemic limbo. It is more principled than a mere fudge factor -- the underlying concept (structured vs. random entropy) has independent support. But it has not been validated independently of the framework that introduced it. It is a **theoretically motivated hypothesis**, not an established variable.

### 3. Circular Reasoning Risk

The circularity in the framework can be mapped precisely:

```
Step 1: Choose parameters "appropriate" for DMT based on phenomenological reports
        -> phi = 0.85, tau = 0.90, rho = 0.70, H = 0.70, kappa = 0.90

Step 2: Compute D = 0.381

Step 3: Note that D = 0.381 is high, consistent with phenomenological reports

Step 4: Conclude: "The formula correctly predicts DMT is a high-density state"
```

The circle: the "prediction" in Step 4 is guaranteed by the choices in Step 1. The formula did not predict anything -- it reflected back the phenomenological judgments that were used to set the parameters.

**Where the circle can be broken:**

1. **At Step 1 (parameter measurement).** If phi, tau, rho, H, and kappa were measured by instruments with no reference to phenomenology, Step 1 becomes independent of Step 3. Currently, this is partially achieved:
   - H is independently measurable via LZc (HIGH confidence)
   - rho is independently measurable via PCI for some states (HIGH confidence)
   - phi is partially independent via Global Efficiency (MODERATE-HIGH confidence)
   - tau has indirect grounding via Temporal Integration Windows (MODERATE confidence)
   - kappa has no fully independent measurement (MODERATE confidence, but derived from phenomenological correlation)

2. **At Step 3 (outcome measurement).** If "intensity of experience" were measured by an instrument independent of both the formula and subjective report (e.g., a neural correlate that reliably tracks experiential intensity regardless of content), the validation would be non-circular.

3. **At the formula structure itself.** If the multiplicative structure and the specific entropy gate function were derived from theoretical constraints (e.g., information-theoretic arguments about what must be true of any system with experiential properties), rather than fitted to phenomenological expectations, the formula would have independent justification.

**Current status:** The circle is partially broken for H and rho (independent measurement), weakly broken for phi and tau (indirect measurement), and unbroken for kappa. The formula structure remains post-hoc.

### 4. The 0/44 Problem

The Canon reports:

```
Total Experiments: 116
Confirmed: 44
Pending: 2
Planned: 70
Falsified: 0
```

Zero falsified experiments out of 44 completed. What does this mean epistemically?

**Possible interpretations:**

**(a) The theory is correct.** The simplest explanation. But 44 confirmations with 0 falsifications is unusual for a theory that claims to be falsifiable.

**(b) The experiments are not genuinely risky.** If the experiments were designed such that confirmation was overwhelmingly likely, a 44/44 record is uninformative. Consider: "If I drop a ball, will it fall?" Testing this 44 times and getting 44 confirmations tells us little about the ball.

The key question is whether the experiments involved **novel, risky predictions** -- outcomes that would be surprising if the theory were false. Examining the experiment list:

- **AT01 (Corporate Zombie):** Tests whether the formula gives low D to organizations. Since organizations have phi near 0, rho near 0, the formula trivially gives D near 0. Any multiplicative formula would pass this test.
- **AT03 (Locked Groove):** Tests whether tau = 0 gives D = 0. Tautological given multiplicative structure.
- **AT05 (Dimensional Collapse):** Tests whether rho = 0 gives D = 0. Also tautological.
- **AT07 (Kappa Validation):** Genuinely informative -- shows MSE correlates with kappa. But validated against phenomenological kappa, not independent data.
- **AT08-AT11:** Test whether parameter clarifications are consistent with neuroscience literature. These are literature reviews, not novel predictions.

**(c) The theory is unfalsifiable in practice.** If parameter values can be adjusted freely, any state can be accommodated. The formula has 5 free parameters per state, and only 1 constraint (D should match phenomenological expectations). With 5 degrees of freedom and 1 equation, there are always solutions.

**Comparison to Popper's criterion:**

Popper argued that a theory's scientific status depends on its falsifiability -- the existence of potential observations that would refute it. Conduit Monism identifies several falsification targets:

1. A state with high phi, tau, rho, low H, high kappa that lacks experience
2. A state with low invariant values that has rich experience
3. Demonstration that structured chaos and random chaos cannot be distinguished

These are genuine falsification criteria. But notice: **none of them have been tested.** The 44 experiments test *consistency* (do assigned parameters produce expected D values?) rather than *falsification* (can we find a case that breaks the framework?).

The three falsified experiments in the framework's history (v7.0 failing on Corporate Zombie, v7.0/v8.0 failing on DMT) are better evidence for the theory's scientific character than the 44 confirmations, because they show the framework has actually been revised in response to disconfirming evidence. This is more Popperian than the confirmation record.

**Verdict:** 44/0 is epistemically weak evidence for the theory. It is more likely a sign of insufficiently risky testing than of a perfect theory. The three historical falsifications are more informative than the 44 confirmations.

### 5. AI Validation Methodology

The framework describes its validation as including "4 independent AI reviews" that each supported the findings. This methodology has specific limitations:

**What AI validation can provide:**
- Logical consistency checks (do the mathematical claims follow?)
- Literature verification (do the cited papers say what is claimed?)
- Identification of conceptual gaps
- Adversarial stress-testing (can the framework handle edge cases?)

**What AI validation cannot provide:**
- Empirical evidence
- Independent parameter measurement
- Novel experimental data
- Peer review in the scientific sense (AI systems have no professional reputation at stake, no domain expertise beyond their training data, and no ability to replicate experiments)

**Specific concerns with the 4-AI validation:**

1. **Training data contamination.** All four AI systems (Claude, Grok, ChatGPT, Gemini) were trained on similar corpora that include the consciousness literature. They share biases about what sounds "plausible" in consciousness research.

2. **Compliance pressure.** AI systems are designed to be helpful. When presented with a framework and asked "does this make sense?", there is an inherent bias toward agreement. This is not the same as hostile peer review by domain experts who have competing theories to defend.

3. **No stake in being right.** A human reviewer who endorses a flawed theory risks professional reputation. An AI system that endorses a flawed framework faces no consequences. This removes a critical incentive structure that makes peer review work.

4. **Consensus is not evidence.** Four AI systems agreeing is structurally similar to asking four students who read the same textbook whether a theory is consistent with the textbook. Agreement indicates consistency with training data, not truth.

**What genuine validation would require:**

1. **Human domain expert review.** Submit to consciousness science journals. Engage with IIT, Global Workspace, and Higher-Order Theory researchers directly.
2. **Empirical pre-registration.** Pre-register specific predictions (e.g., "ketamine at dose X will produce PCI = Y, LZc = Z, and the resulting D will be between A and B") before collecting data.
3. **Adversarial collaboration.** Partner with researchers who hold competing theories (Tononi's group for IIT, Dehaene's group for GNW) to design experiments that discriminate between frameworks.
4. **Replication by independent groups.** Have other labs assign parameter values to states using the framework's operational definitions and check whether they converge.

---

## III. What Would Actually Kill This Theory

The following five experiments could produce results genuinely incompatible with the framework. Each specifies concrete measurements and explicit failure criteria.

### Experiment 1: The Ketamine Dissociation Test

**Rationale:** Ketamine preserves PCI (rho remains high) while producing subjective dissociation. The framework predicts moderate D. But what if PCI-measured rho and subjectively-reported experiential intensity are uncorrelated during ketamine dose escalation?

**Method:**
1. Measure PCI at 5 ketamine dose levels (sub-anesthetic through anesthetic)
2. Simultaneously collect subjective intensity ratings (e.g., 11-Dimensional Altered States of Consciousness scale)
3. Compute D from measured PCI (= rho), measured LZc (= H), and estimated phi, tau, kappa
4. Plot D against subjective intensity

**Falsification criterion:** If D (computed from measured parameters) and subjective intensity are uncorrelated (r < 0.3) or show inverse correlation, the formula does not track experiential intensity. This is particularly damaging because rho and H -- the two best-grounded parameters -- would have been measured independently.

**Required equipment:** TMS-EEG system, ketamine infusion protocol, validated self-report scales.

### Experiment 2: The Split-Brain Paradox Test

**Rationale:** The framework predicts that severing the corpus callosum reduces phi, producing two lower-D loci of experience. But phi is measured via *global* efficiency. In a split brain, each hemisphere has intact *local* efficiency.

**Method:**
1. Measure PCI and Global Efficiency in corpus callosotomy patients
2. Compute phi_left and phi_right from hemisphere-specific connectivity
3. Compute D_left and D_right
4. Compare with behavioral and (if possible) subjective evidence of experiential quality in each hemisphere

**Falsification criterion:** If each hemisphere shows phi, tau, rho values comparable to an intact brain (which is plausible -- each hemisphere is a complete processing system), the formula predicts near-normal D for each hemisphere. But if behavioral evidence suggests one hemisphere has severely diminished experience (e.g., the non-dominant hemisphere), the formula's prediction would be wrong. Conversely, if D predicts severe reduction but both hemispheres show rich experience, the multiplicative penalty on phi is too harsh.

### Experiment 3: The Meditation-Anesthesia Isocline Test

**Rationale:** Deep absorption meditation (jhana) and light propofol sedation can both produce states of reduced responsiveness. The framework predicts very different D values (meditation: high D; sedation: low D). But what if their neural signatures are more similar than predicted?

**Method:**
1. Measure PCI, LZc, and Global Efficiency simultaneously in experienced meditators during jhana states and in the same subjects during light propofol sedation
2. Compute all five parameters from neural measurements alone (blind to condition)
3. Compute D for each condition

**Falsification criterion:** If the neurally-measured parameters for jhana and light sedation are similar (both showing reduced entropy, reduced binding), but phenomenological reports are radically different (rich absorption vs. reduced awareness), then either (a) the parameter measurements do not capture what matters, or (b) the formula is missing a critical variable. Either outcome is damaging.

### Experiment 4: The Non-Biological High-D System Test

**Rationale:** The framework claims substrate independence -- any system with the right geometry is conscious. Weather systems, ecosystems, and markets should have low D. But what about highly integrated, self-referential computational systems that are not designed to be conscious?

**Method:**
1. Identify a large-scale computational system with genuine recurrence, temporal persistence, high integration, and structured entropy (candidates: reservoir computing networks, cellular automata at the edge of chaos, RWKV-based systems with external memory)
2. Measure or compute phi, tau, rho, H, kappa using the framework's operational definitions as literally as possible
3. Compute D

**Falsification criterion:** If a system that we have strong reasons to believe lacks experience (e.g., a weather simulation) produces D > 0.1, the formula is measuring complexity, not consciousness. The framework acknowledges this as a vulnerability ("the Nothing-Special problem") but has not tested it. This experiment directly probes whether D tracks consciousness or merely complex self-referential dynamics.

### Experiment 5: The Entropy-Coherence Dissociation Test

**Rationale:** The framework's strongest novel claim is that high entropy + high coherence produces intensified consciousness, while high entropy + low coherence produces dissolution. The kappa gate is load-bearing. This must be tested with simultaneously measured H and kappa.

**Method:**
1. Measure LZc (for H) and MSE slope (for kappa) simultaneously during:
   - Psilocybin administration (predicted: high H, high kappa)
   - Generalized seizure (predicted: high H, low kappa)
   - Panic attack induction (predicted: previously debated H level, low kappa)
2. Compute D from measured values
3. Correlate with phenomenological reports

**Falsification criterion:** If psilocybin and seizure show similar MSE slopes (both high kappa or both low kappa), then the kappa distinction between "structured" and "random" chaos does not hold in neural data. This would collapse the coherence gate and require removing or redesigning the most novel element of the formula. Alternatively, if kappa is high during seizures (because hypersynchronous spreading is highly structured, just stereotyped), the MSE slope fails as a proxy for kappa.

---

## IV. Novel Observations

### 1. Exact Maximum of D

As computed in Section I.1, the exact global maximum of D is:

```
D_max = 1.0, achieved at (phi, tau, rho) = (1, 1, 1) and H = 0
```

The practical (interior) maximum is:

```
D_max_interior = 0.75, achieved at (phi, tau, rho) = (1, 1, 1), H = 0.25, kappa = 1
```

More precisely, the maximum of the gate function for given kappa is:

```
g_max(kappa) = 1 - 1/(4*kappa)    for kappa >= 0.5
g_max(kappa) = 1 - sqrt(H) + H*kappa evaluated at H=0 or H=1, whichever is larger, for kappa < 0.5
```

For kappa < 0.5, the gate is maximized at H = 0 (g = 1.0) or H = 1 (g = kappa), so the boundary maximum is always 1.0 (at H = 0).

This means the gate function's interior maximum only exists for kappa >= 0.5, and even then, it is always less than 1.0. The formula's maximum is always achieved at the boundary H = 0, making it a **boundary-dominated** optimization. This is mathematically unusual and suggests the formula may not have the right functional form near H = 0.

### 2. Unexpected Mathematical Behaviors

#### Non-monotonicity in H

For kappa > 0.5, the gate function g(H, kappa) is non-monotonic in H:

- It starts at g(0) = 1.0
- Decreases initially (the sqrt(H) penalty dominates)
- Reaches a minimum at the critical point H* = 1/(4*kappa^2)
- Then increases toward g(1) = kappa

The derivative g'(H) = -1/(2*sqrt(H)) + kappa changes sign at H* = 1/(4*kappa^2). For kappa = 0.9:

```
H* = 1/(4 x 0.81) = 0.309
g(0) = 1.0
g(H*) = 1 - sqrt(0.309) + 0.309 x 0.9 = 1 - 0.556 + 0.278 = 0.722
g(1) = 0 + 0.9 = 0.9
```

So the gate drops from 1.0 to 0.722 at H = 0.309, then rises back to 0.9 at H = 1. For kappa = 0.9, the gate at H = 1 (0.90) **exceeds** the interior minimum (0.722). This confirms non-monotonicity.

**This is a significant structural feature.** For high-kappa states, the gate function has a valley. A system transitioning from low entropy to high entropy passes through a *worse* state before reaching a *better* state. This is precisely the onset-anxiety pattern observed in psychedelic phenomenology: as entropy increases (drug onset), experience first degrades (the gate drops into the valley) before the coherence term kicks in at higher H values.

The framework's AT13 (Psychedelic Trajectory) simulated this with lag dynamics, but the valley is actually built into the static gate function itself. The lag dynamics add temporal delay, but the underlying non-monotonicity is already present in the mathematics. This may have been unintended but is phenomenologically apt.

#### The kappa = 0 collapse

When kappa = 0, the gate becomes g(H) = 1 - sqrt(H), which is monotonically decreasing. This means that for systems with zero coherence, any entropy at all hurts. The formula produces:

- H = 0: g = 1.0
- H = 0.5: g = 0.293
- H = 1.0: g = 0.0

At kappa = 0 and H = 1, g = 0 and D = 0 regardless of structure. This means a maximally entropic, zero-coherence system has zero consciousness even with perfect integration, temporal depth, and binding. This is the formula's most extreme claim: entropy without structure is absolutely lethal.

### 3. Flat Regions in the Landscape

The formula has regions where D is effectively insensitive to parameter changes:

#### The "entropy dead zone" near baseline

As computed in Section I.3, dD/dH = -0.022 at the wakefulness baseline. This means small changes in entropy around H = 0.5 barely affect consciousness. The dead zone extends roughly from H = 0.35 to H = 0.65 when kappa is near 0.5-0.7.

Phenomenologically, this predicts that moderate stress (slightly elevated entropy) has minimal impact on experiential intensity. This seems reasonable for mild stress but may not hold for sustained elevation.

#### The "low structure floor"

When any of phi, tau, rho is below about 0.2, D is so small that changes in other parameters are irrelevant. For example, with rho = 0.1:

```
D_max = phi_max x tau_max x 0.1 x g_max = 1 x 1 x 0.1 x 1.0 = 0.1
```

No adjustment of phi, tau, H, or kappa can bring D above 0.1 if rho < 0.1. The structural parameters create a hard ceiling. Below rho = 0.1, you are in the "zombie basin" regardless.

#### The "high structure plateau"

When phi, tau, and rho are all above 0.8, the structural prefix is > 0.512. The gate then becomes the dominant factor. In this regime, the formula is primarily about entropy management, and the structural parameters become relatively less important (since they are already near maximum). This is the regime of "enhanced" states (meditation, psychedelics, flow), where the action is in H and kappa, not in phi, tau, rho.

### 4. Regime-Dependent Sensitivity

The formula has distinct regimes where different parameters matter:

| Regime | Dominant Parameters | Example States |
|--------|-------------------|----------------|
| Low structure (any structural param < 0.3) | phi, tau, rho | Anesthesia, coma, seizure |
| Moderate structure, moderate entropy | All roughly equal | Wakefulness, REM |
| High structure, low entropy | phi, tau, rho (ceiling) | Meditation, flow |
| High structure, high entropy | kappa, H | Psychedelics, creative states |
| Near-zero H | phi, tau, rho (H irrelevant) | Hypothetical crystal states |

This regime structure is actually a strength of the formula. It means different parameters "take over" in different phenomenological contexts, which matches the intuition that different factors matter in different states. Entropy does not much matter for determining whether you are conscious at all (structure does that work), but it critically determines the character of highly structured conscious states.

However, the regime boundaries are not sharp -- they are gradual transitions in a smooth landscape. This means the formula cannot produce sharp phase transitions (like the sudden loss of consciousness under anesthesia). The smooth multiplicative structure predicts gradual decline, while clinical evidence suggests relatively sharp transitions around PCI* = 0.31.

---

## V. Constructive Recommendations

### 1. Breaking the Parameter-Assignment Circularity

**Priority: Critical.**

The single most important step for the framework's scientific credibility is to establish a complete measurement protocol that assigns all five parameters from neural data alone, blind to phenomenological expectations.

**Specific proposal:**

1. Recruit N >= 30 subjects
2. Measure PCI, LZc, Global Efficiency, Temporal Integration Window, and MSE slope simultaneously during 5 conditions: (a) resting wakefulness, (b) light propofol sedation, (c) ketamine sub-anesthetic, (d) focused attention meditation, (e) psilocybin (where legally possible)
3. Convert all measurements to (phi, tau, rho, H, kappa) using only the operational definitions in the Canon -- no phenomenological adjustment
4. Compute D for each condition and subject
5. Correlate D with subjective intensity ratings collected independently

This experiment would either validate or falsify the framework in a single stroke. If D correlates with subjective intensity (r > 0.5), the framework has genuine predictive power. If not, it needs fundamental revision.

### 2. Obtaining Truly Independent Empirical Anchors

**Current status by parameter:**

| Parameter | Independence | Priority |
|-----------|-------------|----------|
| rho (PCI) | HIGH -- PCI is measured independently | Maintain |
| H (LZc) | HIGH -- LZc is measured independently | Maintain |
| phi (E_glob) | MODERATE -- E_glob is measured, but mapping to 0-1 scale involves judgment | Standardize mapping |
| tau (TIW) | LOW-MODERATE -- temporal integration windows are measured, but their relationship to "temporal depth" in the formula is not validated | Need validation study |
| kappa (MSE slope) | LOW -- MSE is measured, but its correspondence to kappa has only been validated against phenomenological kappa assignments | Need independent validation |

**Highest priority:** Validate kappa independently. The proposed method:
1. Measure MSE slopes during 10+ states with known phenomenology
2. Have independent raters (blinded to MSE data) rate each state's "structuredness of chaos" on a scale
3. Correlate MSE slope with blind phenomenological ratings
4. If correlation holds (r > 0.7), kappa is independently validated

### 3. Designing Discriminating Experiments

The framework needs experiments that distinguish it from competing theories, not just confirm it.

**Conduit Monism vs. IIT:**

IIT uses summation (Phi integrates information across partitions). Conduit Monism uses multiplication (zero in any core dimension = zero D). A discriminating experiment:

- Find a system with high Phi but one zero structural parameter (e.g., high integration, high temporal depth, zero binding). IIT predicts consciousness (Phi > 0). Conduit Monism predicts D = 0.
- Candidate: A feedforward neural network with very high integration (many interconnections) but no recurrence. IIT may assign non-zero Phi; Conduit Monism assigns D = 0 (rho = 0).
- Evidence for or against consciousness in such a system would discriminate between the theories.

**Conduit Monism vs. Global Neuronal Workspace (GNW):**

GNW predicts consciousness requires global ignition -- a threshold event where information becomes globally accessible. Conduit Monism predicts gradual scaling with no sharp threshold (D is continuous).

- Discriminating experiment: Measure the transition into anesthesia with fine temporal resolution. If consciousness disappears suddenly (supporting GNW's ignition threshold) rather than gradually (supporting Conduit Monism's continuous D), this favors GNW.
- Note: PCI studies suggest relatively sharp transitions around PCI* = 0.31, which is more consistent with GNW's threshold than Conduit Monism's gradual scaling. This is a genuine tension the framework should address.

**Conduit Monism vs. Higher-Order Theories (HOT):**

HOT theories claim consciousness requires meta-representation -- the system representing its own states to itself. This is similar to Conduit Monism's rho (binding). A discriminating test:

- HOT predicts that eliminating higher-order representations eliminates consciousness but preserves first-order processing. Conduit Monism predicts that rho = 0 eliminates D entirely, but distinguishes rho (self-reference) from higher-order representation.
- Candidate: Lesion studies or pharmacological interventions that selectively affect prefrontal cortex (where higher-order representations are thought to reside) while preserving thalamocortical loops (which PCI measures). If consciousness persists with prefrontal damage but preserved PCI, this supports Conduit Monism's broader notion of rho over HOT's narrower notion.

### 4. Additional Structural Improvements

**Address the H = 0 singularity.** The formula's infinite derivative at H = 0 is a mathematical artifact. Consider replacing (1 - sqrt(H)) with a smoother function, such as (1 - sqrt(H + epsilon)) for small epsilon, or using a different functional form like exp(-alpha * H) that avoids the singularity. This is a technical fix that would not change the formula's behavior in the phenomenologically relevant range but would improve its mathematical properties.

**Consider a vector output.** D as a scalar compresses too much information. A 2D or 3D output -- perhaps (Intensity, Stability, Complexity) -- would reduce degeneracy while remaining interpretable. The formula already implicitly contains these dimensions: intensity ~ phi*tau*rho, stability ~ 1-H, complexity ~ H*kappa. Factoring them out as separate outputs would increase discriminative power.

**Establish a formal error model.** Every parameter assignment should carry an uncertainty estimate. The density D should be reported as D +/- delta_D, where delta_D is computed from error propagation through the formula. This would transform claims from "DMT has D = 0.381" to "DMT has D = 0.38 +/- 0.12 (95% CI)", which is more scientifically honest and would allow statistical comparison of states.

The error propagation for the multiplicative formula is:

```
(delta_D / D)^2 = (delta_phi / phi)^2 + (delta_tau / tau)^2 + (delta_rho / rho)^2
                  + (dg/dH * delta_H / g)^2 + (dg/dkappa * delta_kappa / g)^2
```

Given that many parameters have confidence levels of LOW (delta ~ 20-30% of value), the resulting delta_D could be substantial.

---

## VI. Summary of Findings

### Strengths

1. **The multiplicative structure is well-motivated.** The zero-elimination property (any core parameter = 0 means D = 0) is a strong, falsifiable structural claim. It distinguishes the framework from additive theories.

2. **The entropy gate is mathematically elegant.** The non-monotonicity of g(H, kappa) for high kappa naturally produces the onset-anxiety/breakthrough pattern observed in psychedelic phenomenology, without requiring additional parameters.

3. **Two parameters have strong empirical grounding.** rho (via PCI) and H (via LZc) are independently measurable with HIGH confidence. This gives the framework partial empirical traction.

4. **The framework identifies genuine structural distinctions.** The distinction between "structured chaos" (high kappa) and "random chaos" (low kappa) has independent support in the complexity science literature.

### Weaknesses

1. **Post-hoc construction.** The formula was iteratively refined to match phenomenological expectations. This is not inherently illegitimate but has not yet been distinguished from curve-fitting by prospective prediction.

2. **Kappa is under-validated.** The most novel element of the formula (the coherence gate) rests on the least well-grounded parameter. Kappa has no fully independent empirical anchor.

3. **Parameter assignment circularity.** Most parameter values are assigned from phenomenological expectations, then the formula is validated against those same expectations. This circle is partially broken for rho and H but not for tau, phi (partially), or kappa.

4. **44/0 confirmation record is epistemically weak.** The experiments test consistency, not falsification. Genuinely risky predictions have not been made or tested.

5. **AI validation is not peer review.** Getting AI systems to agree the framework is consistent is useful but not equivalent to domain expert review, independent replication, or empirical testing.

6. **D is a scalar that discards too much information.** The 5-to-1 compression creates massive degeneracy: topologically distinct states produce identical D values.

7. **The formula predicts gradual transitions, but consciousness may have sharp thresholds.** The PCI* = 0.31 threshold suggests a relatively sharp transition between conscious and unconscious states, which is more consistent with GNW's ignition model than Conduit Monism's smooth multiplicative structure.

### Overall Assessment

Conduit Monism is a **promising theoretical framework** that has been developed with unusual intellectual honesty -- documenting its own failures, acknowledging its limitations, and iteratively refining in response to anomalies. The mathematical structure is sound and non-trivial. The entropy gate is a genuine contribution to the formal modeling of consciousness.

However, the framework currently exists in a pre-scientific state. Its predictions are predominantly retrodictive (explaining known phenomenology) rather than predictive (forecasting unknown outcomes). Its parameter assignments are largely circular. Its validation methodology (AI review) is novel but insufficient.

The path from here to genuine scientific credibility requires exactly three things:

1. **Prospective predictions** -- compute D for a novel state before measuring it
2. **Independent parameter measurement** -- especially for kappa and tau
3. **Discriminating experiments** -- tests that distinguish Conduit Monism from IIT, GNW, and HOT

The framework has the structural properties to support this transition. Whether it makes the transition depends on whether the research program moves from phenomenological calibration to empirical measurement.

---

## Appendix: Computed Reference Values

### Gate Function Values

| H | kappa = 0 | kappa = 0.25 | kappa = 0.50 | kappa = 0.65 | kappa = 0.75 | kappa = 0.90 | kappa = 1.00 |
|---|-----------|-------------|-------------|-------------|-------------|-------------|-------------|
| 0.00 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| 0.10 | 0.684 | 0.709 | 0.734 | 0.749 | 0.759 | 0.774 | 0.784 |
| 0.20 | 0.553 | 0.603 | 0.653 | 0.683 | 0.703 | 0.733 | 0.753 |
| 0.25 | 0.500 | 0.563 | 0.625 | 0.663 | 0.688 | 0.725 | 0.750 |
| 0.30 | 0.452 | 0.527 | 0.602 | 0.647 | 0.677 | 0.722 | 0.752 |
| 0.40 | 0.368 | 0.468 | 0.568 | 0.628 | 0.668 | 0.728 | 0.768 |
| 0.50 | 0.293 | 0.418 | 0.543 | 0.618 | 0.668 | 0.743 | 0.793 |
| 0.60 | 0.225 | 0.375 | 0.525 | 0.615 | 0.675 | 0.765 | 0.825 |
| 0.70 | 0.163 | 0.338 | 0.513 | 0.618 | 0.688 | 0.793 | 0.863 |
| 0.80 | 0.106 | 0.306 | 0.506 | 0.626 | 0.706 | 0.826 | 0.906 |
| 0.90 | 0.051 | 0.276 | 0.501 | 0.636 | 0.726 | 0.861 | 0.951 |
| 1.00 | 0.000 | 0.250 | 0.500 | 0.650 | 0.750 | 0.900 | 1.000 |

### Sensitivity at Key States

| State | dD/dphi | dD/dtau | dD/drho | dD/dH | dD/dkappa | Most Sensitive |
|-------|---------|---------|---------|-------|-----------|----------------|
| Wakefulness (0.80,0.75,0.65,0.50,0.65) | 0.301 | 0.321 | 0.371 | -0.022 | 0.195 | rho |
| DMT (0.85,0.90,0.70,0.70,0.90) | 0.500 | 0.472 | 0.607 | 0.162 | 0.375 | rho |
| Propofol (0.25,0.10,0.24,0.35,0.20) | 0.011 | 0.029 | 0.012 | -0.004 | 0.002 | tau |
| Meditation (0.85,0.80,0.70,0.40,0.80) | 0.385 | 0.409 | 0.468 | 0.005 | 0.190 | rho |

---

## References

### Cited in This Analysis

- Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*, 5(198), 198ra105.
- Casarotto, S., et al. (2016). Stratification of unresponsive patients by an independently validated index of brain complexity. *Annals of Neurology*, 80(5), 718-729.
- Carhart-Harris, R. L., et al. (2014). The entropic brain: A theory of conscious states informed by neuroimaging research with psychedelic drugs. *Frontiers in Human Neuroscience*, 8, 20.
- Costa, M., Goldberger, A. L., Peng, C. K. (2002). Multiscale entropy analysis of complex physiologic time series. *Physical Review Letters*, 89(6), 068102.
- Costa, M., Goldberger, A. L., Peng, C. K. (2005). Multiscale entropy analysis of biological signals. *Physical Review E*, 71(2), 021906.
- Popper, K. (1963). *Conjectures and Refutations: The Growth of Scientific Knowledge*. Routledge.
- Sarasso, S., et al. (2015). Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine. *Current Biology*, 25(23), 3099-3105.
- Schartner, M., et al. (2017). Increased spontaneous MEG signal diversity for psychoactive doses of ketamine, LSD and psilocybin. *Scientific Reports*, 7, 46421.
- Tononi, G., et al. (2016). Integrated information theory: from consciousness to its physical substrate. *PLOS Computational Biology*, 12(5), e1004588.

### Framework Documents Referenced

- Conduit Monism v9.2 (`frameworks/Conduit_Monism_v9.2.md`)
- Canon Registry v9.3.1 (`CANON.md`)
- Empirical Anchors v1.4 (`calibration/empirical_anchors.md`)
- Grounded States v1.1 (`calibration/grounded_states.json`)
- Calibration Table v1.2 (`calibration/calibration_table.json`)
- Mapping Functions v1.1 (`calibration/mapping_functions.py`)
- Falsification Suite v1.0 (`experiments/260115_Falsification_Suite.md`)
- AT02 DMT Paradox (`experiments/260114_Adversarial_Test_02_DMT_Paradox.md`)
