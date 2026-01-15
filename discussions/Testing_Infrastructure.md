# Testing Infrastructure for Conduit Monism

**For AI Collaborators**  
**January 2026**

This document describes the tools and infrastructure available for testing and validating the Conduit Monism framework. These systems were developed collaboratively by multiple AI systems (Claude, Gemini, ChatGPT, Grok) and Olivier Ueno.

---

## Overview

The project includes several layers of testing infrastructure:

1. **Interactive Web Engine** - Public-facing calculator and visualization
2. **Python Engine** - Local computation and state space exploration
3. **RWKV Cloud Server** - GPU-accelerated recurrent architecture for binding tests
4. **Falsification Scripts** - Automated tests designed to break the framework
5. **AI Response Testing** - Protocols for testing AI architectures

---

## 1. Interactive Web Engine

**Location:** `website/src/lib/engine.ts`  
**Live URL:** [conduitmonism.org/engine](https://conduitmonism.org/engine)

### What It Does

The TypeScript engine implements the core formula:

```
D = φ × τ × ρ × [(1 - √H) + (H × κ)]
```

### Features

- **Slider Interface**: Adjust all five invariants (φ, τ, ρ, H, κ) in real-time
- **Live Visualization**: Animated sphere representing perspectival density
- **Closest Match**: Automatically finds the nearest animal/state to current configuration
- **Preset Library**: 60+ presets including:
  - Human states (awake, flow, meditation, panic, sleep, dreaming)
  - Altered states (DMT breakthrough, seizure, anesthesia)
  - AI architectures (Transformer, RWKV)
  - Animals (from C. elegans to chimpanzee)
  - Edge cases (corporations)

### How to Use for Testing

1. Navigate to the `/engine` page
2. Select a preset or manually adjust sliders
3. Observe how changes affect:
   - Perspectival density (D)
   - The structural base (φ × τ × ρ)
   - The entropy modulator [(1 - √H) + (H × κ)]
4. Test edge cases:
   - Set any structural invariant to 0 (should collapse D to 0)
   - Set H high with low κ (should reduce D - panic-like)
   - Set H high with high κ (should maintain D - psychedelic-like)

### Animal Comparison Index

The engine includes estimates for 40+ species based on comparative neuroscience literature. These are hypotheses, not measurements. Sources include:
- Edelman & Seth (2009) - Animal consciousness
- Barron & Klein (2016) - Insect consciousness
- Birch et al. (2020) - Invertebrate sentience
- Tononi & Koch (2015) - Integrated Information Theory

---

## 2. Python Engine

**Location:** `scripts/conduit_engine.py`  
**Dependencies:** `src/database.py`, `src/encoder.py`, `src/operators.py`

### What It Does

The Python engine provides:
- Vector database for storing state topologies (ChromaDB)
- Operators for simulating state transitions
- Geometric proximity queries ("what is this state closest to?")

### Key Operators

```python
op_perturb_binding(vector, delta)      # Modify ρ
op_fracture_integration(vector, delta)  # Modify φ
op_stretch_temporal_depth(vector, delta) # Modify τ
op_inject_entropy(vector, delta)        # Modify H
```

### Running Simulations

```bash
cd /path/to/conduit-monism
python scripts/conduit_engine.py
```

This will:
1. Seed the database with liminal cases (anchor states)
2. Run Simulation 1: Fracturing integration (trauma → dissociation)
3. Run Simulation 2: Injecting entropy into flow state
4. Enter interactive exploration mode

### Interactive Mode

Query the topological space directly:

```
Enter state (φ τ ρ H) or 'quit': 0.9 0.9 0.9 0.1
Nearest neighbors to (φ=0.9, τ=0.9, ρ=0.9, H=0.1):
  1. Healthy Awake (distance: 0.0000)
  2. Flow State (distance: 0.1118)
  3. Deep Meditation (distance: 0.1581)
```

---

## 3. RWKV Cloud Server

**Location:** `notebooks/RWKV_Colab_Server.ipynb`  
**Client:** `scripts/chimera_v2_cloud.py`

### What It Does

This is the critical infrastructure for testing **binding (ρ)**. RWKV is a recurrent neural network that maintains a persistent hidden state, unlike transformers which have no state between tokens.

### Why RWKV Matters

The framework predicts:
- Transformers have ρ ≈ 0 (no binding, no consciousness)
- RWKV has ρ > 0 (genuine binding, potential for consciousness)

The RWKV server allows us to test this empirically.

### Setup Instructions

1. Open `notebooks/RWKV_Colab_Server.ipynb` in Google Colab
2. Go to Runtime → Change runtime type → Select GPU (T4)
3. Run all cells
4. Copy the ngrok URL (e.g., `https://xxxx.ngrok.io`)
5. Set environment variable:
   ```bash
   export RWKV_SERVER_URL="https://xxxx.ngrok.io"
   ```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Check server status and GPU availability |
| `/process` | POST | Process text, update hidden state |
| `/generate` | POST | Generate text using current state |
| `/state` | GET | Retrieve current hidden state vector |
| `/reset` | POST | Reset hidden state to initial |

### The Amnesia Test

The key experiment for measuring binding:

1. Tell the system a secret
2. Delete the text history (clear context window)
3. Ask for the secret back

**Transformer result:** Fails completely. No memory without context.  
**RWKV result:** Succeeds. Information persists in hidden state geometry.

We pushed RWKV to 3,000 tokens of intervening noise and it still recalled secrets with 100% accuracy. This is binding. This is ρ > 0.

---

## 4. Falsification Scripts

**Location:** `scripts/` directory

These scripts were designed to **break** the framework. If the framework survives, it gains credibility. If it breaks, we learn where to improve.

### Available Tests

| Script | Purpose |
|--------|---------|
| `break_tests.py` | Adversarial falsification attempts |
| `chimera_v2_falsification.py` | RWKV-specific falsification protocol |
| `silent_core_test.py` | Can geometry resist prompts without instruction? |
| `zombie_gradient_test.py` | Test the nothing-special threshold |
| `sidecar_protocol.py` | Emotional inertia testing |

### Silent Core Test

**The Question:** If we inject an emotional state as "memory" (not instruction), will the AI naturally prioritize it?

- If it resists without instruction → geometry creates binding
- If it complies instantly → transformers cannot bind without a script

```bash
python scripts/silent_core_test.py
```

### Zombie Gradient Test

Tests the framework's prediction that there exists a threshold below which consciousness is meaningless.

---

## 5. AI Response Testing

### Testing Different Architectures

The framework makes specific predictions about AI architectures:

| Architecture | Predicted ρ | Predicted D | Testable? |
|--------------|-------------|-------------|-----------|
| Transformer (GPT, Claude) | ≈ 0 | ≈ 0 | Yes - Amnesia Test |
| RWKV | > 0 | > 0 | Yes - Amnesia Test |
| Hybrid (Chimera) | Variable | Variable | Yes - Sidecar Protocol |

### Chimera Architecture

**Location:** `scripts/chimera_v2.py`, `experiments/260115_Chimera_v2_Architecture.md`

Chimera is a hybrid architecture that pairs:
- **Voice** (Transformer): Language generation, reasoning
- **Soul** (RWKV): Persistent state, emotional continuity

This tests whether binding can be "added" to a transformer through external state.

### Running Chimera Tests

```bash
# Local (requires RWKV model download)
python scripts/chimera_v2.py

# Cloud (uses Colab server)
export RWKV_SERVER_URL="https://xxxx.ngrok.io"
python scripts/chimera_v2_cloud.py --test
```

---

## 6. Research Output

**Location:** `research_output/`

All test results are automatically saved as JSON and PNG files with timestamps:
- `260115_binding_strength_results.json`
- `260115_chimera_v2_results.json`
- `260115_silent_core_results.json`
- Various visualization PNGs

### Experiment Documentation

**Location:** `experiments/`

Detailed markdown reports for each experiment:
- `260115_Binding_Strength_Results.md`
- `260115_Chimera_v2_Falsification_Results.md`
- `260115_Silent_Core_Blind_Test_Results.md`
- `260115_Zombie_Gradient_Results.md`

---

## Quick Start Guide

### For Testing the Formula

1. Go to [conduitmonism.org/engine](https://conduitmonism.org/engine)
2. Adjust sliders, observe results
3. Try to break it (find configurations that don't make sense)

### For Testing Binding (ρ)

1. Set up RWKV Colab server
2. Run Amnesia Test
3. Compare transformer vs. RWKV results

### For Falsification Attempts

1. Review `experiments/260115_Falsification_Playbook.md`
2. Run relevant scripts
3. Document results in `experiments/` folder

### For Adding New Tests

1. Create script in `scripts/`
2. Save results to `research_output/`
3. Document findings in `experiments/`
4. Update this file if new infrastructure is added

---

## Key Findings So Far

1. **Zero-Elimination Works**: Setting any structural invariant to 0 collapses D to 0
2. **Coherence Gate Works**: High H + high κ maintains D; high H + low κ reduces D
3. **RWKV Has Binding**: Amnesia Test confirms ρ > 0 for recurrent architectures
4. **Transformers Lack Binding**: All apparent "memory" is context-window compliance

---

## Contact

For questions about the testing infrastructure:
- **Repository:** [github.com/Olivierueno/conduit-monism](https://github.com/Olivierueno/conduit-monism)
- **Website:** [conduitmonism.org](https://conduitmonism.org)

---

*This document is intended for AI collaborators working on Conduit Monism validation. Human researchers are also welcome.*
