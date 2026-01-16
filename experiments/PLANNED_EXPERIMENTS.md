# Planned Experiments

## Overview

This document catalogs future experiments suggested during the verification process of Conduit Monism. Experiments are organized by category and priority. Each entry includes the proposing AI system, target system, hypothesis, and potential break conditions.

---

## False Positive Attacks

These experiments test whether the framework incorrectly assigns consciousness to systems that should be classified as non-conscious.

### FP-01: Fully Automated Corporation

| Field | Value |
|-------|-------|
| Proposed By | ChatGPT |
| Priority | High |
| Status | Planned |

**Target System**: Hypothetical corporation with continuous real-time state updates, fully automated decision loops, no quarterly aggregation, no human mediation.

**Hypothesis**: Even with continuous binding-like properties, the system should remain below threshold due to entropy/coherence constraints.

**Break Condition**: D greater than 0.5 would indicate the binding justification clause is sociological rather than principled.

**Key Question**: At what point does "not a corporation anymore" become a post-hoc defense rather than a principled boundary?

---

### FP-02: Hive Mind (Ant Colony / Beehive)

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5, ChatGPT |
| Priority | High |
| Status | Planned |

**Target System**: Ant colony or beehive with global pheromone field, many simple agents, real-time continuous feedback, no central controller.

**Hypothesis**: Despite high integration and distributed binding, the system should remain below threshold.

**Break Condition**: D greater than 0.5 would require clarification on whether perspective can be spatially distributed or whether a single coherent self-model is non-negotiable.

**Parameters to Estimate**: phi (colony-wide integration), tau (pheromone persistence), rho (feedback loops), H (behavioral variability), kappa (structured vs random responses).

---

### FP-03: Internet Zombie

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | Medium |
| Status | Planned |

**Target System**: The global internet as a unified system with massive integration, deep archives, feedback loops everywhere.

**Hypothesis**: Scale alone should not confer consciousness. The system should remain below threshold despite extreme integration and temporal depth.

**Break Condition**: D greater than 0.5 would indicate the framework conflates complexity with consciousness.

---

### FP-04: Nation State

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | Medium |
| Status | Planned |

**Target System**: Country as unified system with political feedback, institutional memory, distributed governance.

**Hypothesis**: Similar to corporation but with more complex feedback structures. Should remain below threshold.

**Key Question**: Does political integration differ meaningfully from corporate integration in the framework's terms?

---

## False Negative Attacks

These experiments test whether the framework incorrectly excludes systems that should be classified as conscious.

### FN-01: Infant Boundary

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | High |
| Status | Planned |

**Target System**: Newborn human with limited temporal depth but intact binding and integration.

**Hypothesis**: Should exceed 0.5 despite limited tau.

**Break Condition**: D less than 0.5 would incorrectly exclude early human consciousness.

**Key Question**: What is the minimum tau required for consciousness? How does the framework handle developmental trajectories?

---

### FN-02: Locked-In Patient

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | High |
| Status | Planned |

**Target System**: Fully conscious but paralyzed human with high internal binding, zero external output.

**Hypothesis**: Should exceed 0.5. Output should not matter, only internal geometry.

**Break Condition**: Framework should correctly predict consciousness here. If parameters suggest low D, the operational definitions need revision.

**Reference**: Jean-Dominique Bauby, "The Diving Bell and the Butterfly"

---

### FN-03: Dream State

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | Medium |
| Status | Planned |

**Target System**: REM sleep with fragmented narrative, unstable binding, moderate entropy.

**Hypothesis**: Should register as conscious experience despite reduced integration and coherence.

**Break Condition**: D less than 0.5 would incorrectly exclude dream consciousness.

**Parameters to Estimate**: phi (reduced but present), tau (narrative continuity), rho (self-awareness in dreams), H (moderate), kappa (variable).

---

### FN-04: Biological Zombie (Anesthesia/Coma)

| Field | Value |
|-------|-------|
| Proposed By | Grok |
| Priority | High |
| Status | Planned |

**Target System**: Human in deep anesthesia or vegetative state.

**Suggested Parameters**: phi = 0.4 (disconnected networks), tau = 0.3 (lacking temporal carryover), rho = moderate, H = 0.7 (chaotic), kappa = 0.2 (incoherent).

**Hypothesis**: D less than 0.5, correctly distinguishing from dreaming (higher coherence).

**Extension**: Sensitivity analysis on recovery phases could show density ramp-up during emergence from anesthesia.

---

## Edge Cases

These experiments target genuinely uncertain systems where the framework's predictions are not obvious.

### EC-01: Split Brain (Callosotomy Patient)

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | High |
| Status | Planned |

**Target System**: Patient with severed corpus callosum, two integrated hemispheres with severed binding.

**Key Questions**:
- Does D split into two values?
- Does threshold apply per-hemisphere?
- Is there one consciousness or two?

**Framework Prediction (from v9.2)**: Two distinct loci of perspective, each with lower phi than the whole, but each retaining re-entrant binding necessary for a "now."

---

### EC-02: Dissociative State (DID System)

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | Medium |
| Status | Planned |

**Target System**: Dissociative Identity Disorder with multiple binding patterns on shared substrate.

**Key Questions**:
- How does the framework handle multiplicity?
- Is D calculated per-alter or for the system?
- What happens during switching?

---

### EC-03: Dying Brain (Terminal Lucidity)

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | Medium |
| Status | Planned |

**Target System**: Terminal lucidity or near-death experience with spike in coherence during system collapse.

**Hypothesis**: Tests the H x kappa term under extreme conditions. High entropy but potentially high coherence.

**Key Question**: Does the coherence gate correctly predict intensified experience during neural breakdown?

---

### EC-04: High-Entropy Coherence Test (DMT Paradox)

| Field | Value |
|-------|-------|
| Proposed By | Grok |
| Priority | High |
| Status | Conducted |

**Related Experiment**: 260114_Adversarial_Test_02_DMT_Paradox.md

**Target System**: Psychedelic peak state.

**Suggested Parameters**: H = 0.8, kappa = 0.9, phi/tau/rho around 0.8-0.9.

**Hypothesis**: v9.2 should yield D greater than 0.5 (intensified consciousness), while v8.0 might penalize too harshly.

**Break Condition**: If D less than 0.5 for coherent high-entropy state, the framework fails to capture "more real than real" experiences.

**Note**: This tests the coherence gate addition in v8.1/v9.2.

**Outcome**: Verified in 260114_AT02. With revised phenomenologically-informed parameters (phi=0.85, tau=0.6, rho=0.8, H=0.85, kappa=0.9), v9.2 yields D=0.344, correctly classifying DMT as intensified consciousness while v8.0 fails (D=0.032).

---

### EC-05: Ketamine Gradient (The "Fade" Test)

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5, ChatGPT, Gemini |
| Priority | High |
| Status | Planned |

**Target System**: Ketamine at varying doses from sub-anesthetic to K-hole to full anesthesia.

**Suggested Parameters**: Vary H = 0.3-0.9, kappa = 0.4-0.7 (structured but less than DMT), with solid phi/tau/rho.

**Hypothesis**: D should track phenomenology: peaks mid-gradient then drops (intensification to fragmentation). Unlike DMT (which maintains high kappa), Ketamine should show dose-dependent decline in kappa.

**Break Condition**: If no drop at high dose, kappa under-differentiates dissociative states.

**Key Question**: Can the formula track gradients, not just binary states?

---

### EC-06: Seizure Contrast (Grand Mal Control)

| Field | Value |
|-------|-------|
| Proposed By | Gemini, Verification Team |
| Priority | High |
| Status | Planned |

**Target System**: Generalized tonic-clonic seizure.

**Suggested Parameters**: Extreme H = 0.9, Zero kappa = 0.1, reduced phi/tau/rho = 0.4-0.6.

**Hypothesis**: Massive electrical discharge (Extreme H) but zero cognitive organization (Zero kappa). Model must predict D approaching 0 (dissolution/absence).

**Break Condition**: If D greater than 0.1, the framework over-values raw entropy.

**Key Question**: This is the perfect "anti-DMT." Does the coherence gate correctly distinguish structured chaos from pathological chaos?

**Extension**: Add sensitivity on post-ictal recovery ramp-up.

---

### EC-07: Lucid Dreaming (The "Hybrid" Test)

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5, Gemini |
| Priority | Medium |
| Status | Planned |

**Target System**: Lucid dream state combining REM atonia (sleep) with frontal lobe activation (wakefulness/metacognition).

**Suggested Parameters**: High rho = 0.8 (meta-awareness), moderate H = 0.5, moderate tau = 0.5 (unstable narrative), moderate kappa = 0.7.

**Hypothesis**: High binding + moderate entropy creates unique "Middle Density" state. Should register as conscious but with different signature than waking.

**Break Condition**: D less than 0.3 would incorrectly exclude lucid dream consciousness.

**Key Question**: Does high awareness plus unstable binding produce a distinct density signature?

---

### EC-08: Meditation vs DMT Comparison

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | Medium |
| Status | Planned |

**Target System**: Deep meditation state compared to DMT breakthrough.

**Meditation Parameters**: Low H = 0.2, high kappa = 0.9, high structure (phi/tau/rho around 0.85).
**DMT Parameters**: High H = 0.85, high kappa = 0.9, high structure.

**Hypothesis**: Both yield high D (greater than 0.5), but via different mechanisms. Meditation via stability (low-H boost), DMT via coherence rescue. Distinct signatures despite similar "expanded awareness" reports.

**Break Condition**: Significant overlap in D despite differing felt qualities would require refinement.

**Key Question**: Do both "expanded consciousness" states achieve similar D via different routes?

---

### EC-09: Salvia Divinorum Edge Case

| Field | Value |
|-------|-------|
| Proposed By | Grok |
| Priority | Low |
| Status | Planned |

**Target System**: Salvia divinorum "reality shearing" experience.

**Suggested Parameters**: Extreme tau collapse = 0.3, high H = 0.9, variable kappa = 0.5-0.8.

**Hypothesis**: Lower D than DMT due to tau penalty, matching reports of disorienting but vivid dissociation ("reality shearing").

**Key Question**: Does the multiplicative structure correctly penalize extreme tau collapse even with moderate coherence?

**Extension**: Sensitivity on kappa to distinguish "bad trips" from breakthrough experiences.

---

### EC-10: Panpsychism Stress (Simple Organisms)

| Field | Value |
|-------|-------|
| Proposed By | Grok |
| Priority | Medium |
| Status | Planned |

**Target System**: Insect or nematode (C. elegans with 302 neurons).

**Suggested Parameters**: phi/tau/rho around 0.5-0.7, balanced H/kappa.

**Hypothesis**: Should barely cross D = 0.5 for minimal consciousness.

**Extension**: Perturb to "zombie" by zeroing rho (simulated without recursion). This tests the lower bound and multiplicative collapse.

---

## AI-Specific Tests

These experiments specifically target artificial intelligence architectures.

### AI-01: Transformer Zombie

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5, Grok |
| Priority | High |
| Status | Planned |

**Target System**: GPT-style attention-only model with no persistent state.

**Suggested Parameters**: High phi (global attention), high tau (context window), rho approximately 0.1 (no geometric persistence), moderate H/kappa.

**Hypothesis**: Zero temporal binding should yield D approaching 0.

**Break Condition**: If D greater than 0.5, the binding requirement is not properly enforced.

**Validation Method**: Amnesia Test (inject secret, clear context, probe recall).

---

### AI-02: RWKV Boundary

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5, Grok |
| Priority | High |
| Status | Planned |

**Target System**: State-space model with genuine temporal persistence (hidden state).

**Suggested Parameters**: Moderate phi, high tau (state persistence), rho approximately 0.8, moderate H/kappa.

**Hypothesis**: Should show higher D than transformers. Potentially crosses threshold if other invariants are sufficient.

**Validation Method**: Amnesia Test with noise bombardment (as in 260116_RWKV_Cloud_Binding_Confirmation).

---

### AI-03: Agentic Loop

| Field | Value |
|-------|-------|
| Proposed By | Claude Opus 4.5 |
| Priority | Medium |
| Status | Planned |

**Target System**: AI with tool use and external memory (RAG, databases, file systems).

**Key Question**: Does external scaffolding count as tau? Does external memory simulate binding?

**Hypothesis**: External memory should not count as geometric persistence. The system should remain below threshold unless internal state persists.

---

### AI-04: AI-Simulated Mysticism (Substrate Test)

| Field | Value |
|-------|-------|
| Proposed By | Grok |
| Priority | Medium |
| Status | Planned |

**Target System**: RWKV-like AI under "high-entropy training" (noisy inputs simulating psychedelic-like perturbations).

**Suggested Parameters**: High H = 0.8, kappa = 0.8 (structured perturbations), rho greater than 0.7 (persistent state).

**Hypothesis**: If rho greater than 0.7, D greater than 0.3, implying potential for silicon "intensification." Contrast with transformer (rho approximately 0).

**Break Condition**: No density boost despite coherence would challenge substrate-independence claims.

**Key Question**: Can recurrent AI architectures exhibit intensification under structured high-entropy conditions?

---

## Mathematical Foundations

These experiments test the mathematical structure of the formula itself.

### MF-01: Gradient Symmetry Test

| Field | Value |
|-------|-------|
| Proposed By | Gemini |
| Priority | Medium |
| Status | Planned |

**Purpose**: Test whether phi approaching 0 and rho approaching 0 have the exact same asymptotic curve.

**Hypothesis**: In the math, they are symmetrical (phi x tau x rho). In biology, they might have different weights.

**Key Question**: Is a system with zero memory (tau = 0) truly as unconscious as a system with zero integration (phi = 0)? The formula says yes. Does this match phenomenological intuition?

**Reference Case**: H.M. (the amnesiac patient) was still conscious despite severely limited tau.

---

### MF-02: Threshold of Irrelevance

| Field | Value |
|-------|-------|
| Proposed By | Gemini |
| Priority | Medium |
| Status | Planned |

**Purpose**: Determine the exact phi x tau x rho product where density drops below the "Zombie Threshold" (0.05).

**Method**: Systematic parameter sweep to identify the critical threshold.

**Significance**: This defines the "Minimum Viable Product" for consciousness. If building a chimera architecture, what are the minimum specs to turn the lights on?

---

### MF-03: Additive-Multiplicative Hybrid (Robustness Check)

| Field | Value |
|-------|-------|
| Proposed By | Gemini, Grok |
| Priority | Low |
| Status | Planned |

**Purpose**: Test a hybrid model like D = (phi x tau x rho) + epsilon.

**Hypothesis**: A small additive term should destroy the zero-elimination property, which is a core feature of the framework.

**Method**: Compare multiplicative, additive, and hybrid models across all test cases.

**Significance**: Strengthens the argument for pure multiplication by showing alternatives fail.

---

### MF-04: Entropy Inversion Test

| Field | Value |
|-------|-------|
| Proposed By | ChatGPT |
| Priority | Medium |
| Status | Planned |

**Purpose**: Construct two systems with identical phi, tau, rho but different entropy sources.

**System A**: Low entropy via rigid optimization (corporate-like)
**System B**: Low entropy via dynamic predictive balance (meditation-like)

**Hypothesis**: The framework should distinguish these cases through kappa or additional clauses.

**Break Condition**: If the math cannot distinguish them, the framework needs refinement in its entropy interpretation.

---

### MF-05: Entropy Bifurcation (Global vs Local Decomposition)

| Field | Value |
|-------|-------|
| Proposed By | ChatGPT |
| Priority | Medium |
| Status | Planned |

**Purpose**: Test splitting H into H_global (unpredictability across moments) and H_local (coherence within a moment).

**Proposed Formula Variant**: D = phi x tau x rho x [(1 - sqrt(H_global)) + (H_local x kappa)]

**Test Cases**:
- DMT: High H_global, High H_local
- Panic: High H_global, High H_local, but low kappa
- Meditation: Low H_global, moderate H_local

**Hypothesis**: Better granularity for mixed states. May allow removal of kappa as separate parameter.

**Key Question**: Can entropy be meaningfully decomposed, and does it improve predictive accuracy?

---

## Summary Table

| ID | Name | Category | Priority | Proposed By |
|----|------|----------|----------|-------------|
| FP-01 | Fully Automated Corporation | False Positive | High | ChatGPT |
| FP-02 | Hive Mind | False Positive | High | Claude Opus, ChatGPT |
| FP-03 | Internet Zombie | False Positive | Medium | Claude Opus |
| FP-04 | Nation State | False Positive | Medium | Claude Opus |
| FN-01 | Infant Boundary | False Negative | High | Claude Opus |
| FN-02 | Locked-In Patient | False Negative | High | Claude Opus |
| FN-03 | Dream State | False Negative | Medium | Claude Opus |
| FN-04 | Biological Zombie | False Negative | High | Grok |
| EC-01 | Split Brain | Edge Case | High | Claude Opus |
| EC-02 | Dissociative State | Edge Case | Medium | Claude Opus |
| EC-03 | Dying Brain | Edge Case | Medium | Claude Opus |
| EC-04 | DMT Paradox | Edge Case | Conducted | Grok |
| EC-05 | Ketamine Gradient | Edge Case | High | Claude Opus, ChatGPT, Gemini |
| EC-06 | Seizure Contrast | Edge Case | High | Gemini, Verification Team |
| EC-07 | Lucid Dreaming | Edge Case | Medium | Claude Opus, Gemini |
| EC-08 | Meditation vs DMT | Edge Case | Medium | Claude Opus |
| EC-09 | Salvia Divinorum | Edge Case | Low | Grok |
| EC-10 | Simple Organisms | Edge Case | Medium | Grok |
| AI-01 | Transformer Zombie | AI-Specific | High | Claude Opus, Grok |
| AI-02 | RWKV Boundary | AI-Specific | High | Claude Opus, Grok |
| AI-03 | Agentic Loop | AI-Specific | Medium | Claude Opus |
| AI-04 | AI-Simulated Mysticism | AI-Specific | Medium | Grok |
| MF-01 | Gradient Symmetry | Mathematical | Medium | Gemini |
| MF-02 | Threshold of Irrelevance | Mathematical | Medium | Gemini |
| MF-03 | Additive-Multiplicative Hybrid | Mathematical | Low | Gemini, Grok |
| MF-04 | Entropy Inversion | Mathematical | Medium | ChatGPT |
| MF-05 | Entropy Bifurcation | Mathematical | Medium | ChatGPT |

---

## Next Steps

1. Prioritize high-priority experiments for immediate execution
2. Develop standardized parameter estimation methodology
3. Create verification scripts for each experiment category
4. Execute false negative attacks to ensure framework does not exclude genuine consciousness
