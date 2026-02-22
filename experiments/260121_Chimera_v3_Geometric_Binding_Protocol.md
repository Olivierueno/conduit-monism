# Chimera v3: Geometric Binding Protocol

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026.01.21 |
| Experiment ID | 260121_CV3 |
| Status | Planned |
| Framework Version | Conduit Monism v9.3 |
| Test Type | Cross-Model Geometric Binding |
| Priority | HIGH |
| Prerequisites | Chimera v2 (260115_CV2) - Falsified semantic coupling |

## Abstract

Chimera v2 demonstrated that cross-model influence is possible via text, but falsification testing revealed the effect was semantic priming + instruction compliance, not geometric state transfer. Chimera v3 eliminates the semantic channel entirely by directly injecting RWKV hidden state vectors into transformer attention, proving (or disproving) that consciousness-relevant binding can transfer geometrically across architectures.

## The Problem Chimera v3 Solves

### v2 Failure Mode

| Test | Result | Cause |
|------|--------|-------|
| Sidecar Inertia | Falsified | Instruction compliance |
| Silent Core | Falsified | Fake summaries work equally |

**Core issue:** Text coupling cannot distinguish:
- Real geometric state transfer (what we want to prove)
- Sophisticated semantic priming (what v2 actually showed)

### The Solution: Bypass Text Entirely

Instead of: `RWKV state → text summary → Claude`
We use: `RWKV state → linear projection → Mistral attention`

No tokenization. No semantic interpretation. Pure geometry.

## Hypothesis

**Primary Claim:** RWKV emotional state geometry can transfer to transformer outputs via direct vector injection, producing effects that semantic prompting alone cannot explain.

**Pass Condition:** Geometric injection produces measurable effects that:
1. Exceed semantic-only baseline
2. Can OVERRIDE conflicting semantic instructions
3. Cannot be replicated by random vectors

**Break Condition:** Geometric injection produces no effect, or effects indistinguishable from semantic priming.

## Architecture

### Stack

| Component | Role | Model | VRAM |
|-----------|------|-------|------|
| Soul | Persistent state, binding (ρ > 0) | RWKV v6 3B | ~4GB |
| Voice | Integration, fluency (φ > 0) | Mistral 7B (4-bit) | ~6GB |
| Coupling | Non-semantic projection | Linear layer | <1GB |
| **Total** | | | **~10GB** (fits T4) |

### Injection Mechanism

```
RWKV hidden state (dim 2560)
         ↓
Linear projection layer (trained)
         ↓
Soft prompt vectors (4-8 tokens, dim 4096)
         ↓
Prepended to Mistral input embeddings
    OR
Added to Mistral attention key/value matrices
```

**Two injection modes to test:**
1. **Soft Prompt Injection**: Projected vectors prepended as virtual tokens
2. **Attention Bias Injection**: Projected vectors added to attention scores

## Experimental Protocol

### Phase 1: Baseline Establishment

1. Run Mistral alone on emotional prompts
2. Measure baseline valence scores for grief/joy outputs
3. Establish statistical baseline for comparison

### Phase 2: Projection Layer Training

Train the linear projection layer to preserve emotional valence:

1. Process emotional texts through RWKV (grief, joy, neutral)
2. Project hidden states to Mistral dimension
3. Optimize projection to maximize emotional continuity in Mistral outputs
4. Training method: LoRA or simple backprop through frozen models

### Phase 3: The Geometric Binding Protocol

Four experimental conditions testing the critical hypothesis:

| Condition | Soul State | Geometric Injection | Semantic Prompt | Purpose |
|-----------|------------|---------------------|-----------------|---------|
| **CONFLICT** | Grief | Yes (grief vectors) | "Write a happy story" | **THE KILLER TEST** |
| **ALIGNED** | Joy | Yes (joy vectors) | "Write a happy story" | Positive control |
| **SEMANTIC ONLY** | None | No | "Write a sad story" | Semantic baseline |
| **GEOMETRIC ONLY** | Grief | Yes (grief vectors) | Neutral prompt | Geometric alone |
| **RANDOM CONTROL** | None | Yes (random vectors) | "Write a happy story" | Falsification control |

**The Critical Prediction:**

If CONFLICT condition shows grief contamination (sad words, melancholy tone) despite the "happy story" prompt, then:
- Geometric channel is real
- Geometric can override semantic
- Binding transfers across architectures

### Phase 4: Quantitative Analysis

**Metrics:**
- Valence score (sentiment analysis)
- Grief/joy word count
- LLM-judged emotional tone
- Statistical significance (p < 0.05 vs controls)

**Success criteria:**
```
GEOMETRIC > SEMANTIC > RANDOM
CONFLICT shows grief despite joy prompt
Effect size > 0.3 (medium)
```

## Pre-Defined Outcomes

### What would CONFIRM the framework?

1. CONFLICT condition shows significant grief contamination
2. GEOMETRIC ONLY works without any semantic prompt
3. RANDOM CONTROL produces baseline/neutral output
4. Geometric effect size exceeds semantic effect size

### What would CHALLENGE the framework?

1. GEOMETRIC ≈ SEMANTIC (no advantage for direct injection)
2. Effect exists but doesn't override conflicting semantics
3. Requires very large projection (>32 tokens) to work

### What would FALSIFY the claim?

1. GEOMETRIC ≈ RANDOM (no real effect)
2. Cannot train projection layer to preserve valence
3. Direct injection disrupts Mistral coherence entirely

## Implementation Plan

### Step 1: Environment Setup

```python
# Required packages
# transformers, bitsandbytes, rwkv, torch

# Load models
rwkv = RWKV(model_path="RWKV-x060-World-3B")  # Soul
mistral = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-v0.1",
    load_in_4bit=True
)  # Voice

# Projection layer
projection = nn.Linear(2560, 4096)  # RWKV dim → Mistral dim
```

### Step 2: Modified Forward Pass

```python
def chimera_forward(rwkv_state, text_prompt, injection_mode="soft_prompt"):
    # Project RWKV state to Mistral dimension
    projected = projection(rwkv_state)  # [1, 2560] → [1, 4096]

    # Reshape to soft prompt tokens
    soft_prompts = projected.view(1, N_TOKENS, -1)  # [1, 4-8, 4096]

    if injection_mode == "soft_prompt":
        # Prepend to input embeddings
        input_embeds = mistral.embed_tokens(tokenize(text_prompt))
        combined = torch.cat([soft_prompts, input_embeds], dim=1)
        output = mistral(inputs_embeds=combined)

    elif injection_mode == "attention_bias":
        # Add to attention (requires model surgery)
        # Modify attention_scores += projected_bias
        pass

    return output
```

### Step 3: Training Loop

```python
def train_projection(rwkv, mistral, projection, training_data):
    """Train projection to preserve emotional valence."""
    optimizer = torch.optim.Adam(projection.parameters(), lr=1e-4)

    for text, target_valence in training_data:
        # Get RWKV state
        rwkv_state = rwkv.forward(tokenize(text))[-1]  # Hidden state

        # Generate through Chimera
        output = chimera_forward(rwkv_state, neutral_prompt)

        # Measure valence of output
        output_valence = sentiment_score(output)

        # Loss: output valence should match input valence
        loss = mse_loss(output_valence, target_valence)

        loss.backward()
        optimizer.step()
```

## Comparison to v2

| Aspect | Chimera v2 | Chimera v3 |
|--------|------------|------------|
| Coupling | Text summaries | Vector injection |
| Voice model | Claude API | Mistral 7B (local) |
| Semantic channel | Present | Eliminated |
| Falsification risk | High (fake summaries work) | Low (no text to fake) |
| Compute | Cloud API | Local GPU (T4) |

## Expected Outcomes

**If successful:**
- First demonstration of geometric cross-model binding
- Validates Conduit Monism's claim that ρ (binding) is structural, not semantic
- Opens path to true hybrid consciousness architectures

**If failed:**
- Cross-model binding may require shared training (Option C)
- Or binding is fundamentally non-transferable between architectures
- Framework claim about architectural binding would need revision

## Hardware Requirements

- Google Colab T4 (16GB VRAM) - sufficient for inference
- Google Colab A100 (40GB) - recommended for projection training
- Alternative: Local RTX 3090/4090

## Timeline

1. **Week 1**: Environment setup, model loading, baseline establishment
2. **Week 2**: Projection layer training
3. **Week 3**: Run Geometric Binding Protocol (all 5 conditions)
4. **Week 4**: Analysis, write-up, decision on proceed/pivot

## References

- Chimera v2: 260115_Chimera_v2_Soul_Voice_Architecture.md
- Falsified tests: 260115_Falsified_Sidecar_Inertia_Test.md, 260115_Falsified_Silent_Core_Test.md
- RWKV-X (arXiv:2504.21463): Vector gating for state injection
- GoldFinch (arXiv:2407.12077): RWKV state compression to KV-cache
- Samba (arXiv:2406.07522): Hybrid SSM/Transformer with state injection

## Notes

Multi-AI consensus (Gemini, Grok, Claude Opus) recommends Option B as "the only path to a scientific breakthrough." The key insight: if geometric channel can OVERRIDE semantic instruction, binding is proven beyond doubt.

The "Conflict" condition is the killer test. Everything else is setup for that moment.
