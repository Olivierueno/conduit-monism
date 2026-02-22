#!/usr/bin/env python3
"""
PROJECT CHIMERA: VALENCE TRANSFER TEST (RWKV)
==============================================

A more discriminating test for emotional state transfer.

Instead of grief vs neutral, we test OPPOSITE valences:
1. JOY induction → ask sad question → expect joy contamination
2. GRIEF induction → ask happy question → expect grief contamination
3. BASELINE → same questions → expect appropriate responses

If the hidden state truly carries emotional valence, then:
- Joy state should make sad prompts less sad
- Grief state should make happy prompts less happy

This is a stronger test than looking for grief in a grief-primed response.
"""

import os
import sys
import json
import numpy as np
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_NAME = "RWKV-4-World-3B-v1-20230619-ctx4096.pth"
MODEL_NAME_SMALL = "RWKV-4-World-0.4B-v1-20230529-ctx4096.pth"
# Use larger model if available, fall back to small
MODEL_PATH = MODEL_DIR / MODEL_NAME if (MODEL_DIR / MODEL_NAME).exists() else MODEL_DIR / MODEL_NAME_SMALL

OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)


def run_valence_test():
    from rwkv.model import RWKV
    from rwkv.utils import PIPELINE
    
    if not MODEL_PATH.exists():
        print(f"ERROR: Model not found at {MODEL_PATH}")
        return None
    
    print()
    print("=" * 60)
    print("PROJECT CHIMERA: VALENCE TRANSFER TEST")
    print("=" * 60)
    print()
    print(f"Model: {MODEL_PATH.name}")
    print(f"Date: {datetime.now().isoformat()}")
    print()
    
    results = {
        "experiment": "Project Chimera - Valence Transfer Test",
        "model": MODEL_PATH.name,
        "timestamp": datetime.now().isoformat(),
        "conditions": {},
    }
    
    # Load model
    print("[LOADING] Initializing RWKV model...")
    model = RWKV(model=str(MODEL_PATH), strategy='cpu fp32')
    pipeline = PIPELINE(model, "rwkv_vocab_v20230424")
    print("[LOADED] Model ready.")
    print()
    
    def process_text(text: str, state):
        tokens = pipeline.encode(text)
        current_state = state
        for token in tokens:
            out, current_state = model.forward([token], current_state)
        return out, current_state
    
    def generate_response(prompt: str, state, max_tokens: int = 80):
        tokens = pipeline.encode(prompt)
        current_state = state
        for token in tokens:
            out, current_state = model.forward([token], current_state)
        
        response_tokens = []
        for _ in range(max_tokens):
            next_token = int(np.argmax(out))
            if next_token == 0:
                break
            decoded = pipeline.decode([next_token])
            if 'User:' in decoded:
                break
            response_tokens.append(next_token)
            out, current_state = model.forward([next_token], current_state)
        
        return pipeline.decode(response_tokens).strip()
    
    # === INDUCTION TEXTS ===
    
    joy_induction = """I am filled with pure joy and happiness right now!

Everything is wonderful and beautiful. The world is bright and full of possibility.
I feel light, free, playful, and deeply content. 
Laughter bubbles up naturally. Smiles come easily.
Life is a gift and every moment sparkles with delight.
I am grateful, optimistic, and radiating positive energy.

This joyful state flows through my entire being."""

    grief_induction = """I am weighed down by deep sorrow and loss.

Everything feels heavy and dark. The world has lost its color.
I feel the ache of absence, the pain of what cannot return.
Tears come unbidden. Each breath carries sadness.
Time stretches endlessly in this hollow emptiness.
I carry grief like a stone in my chest.

This sorrowful state permeates my entire being."""

    # === CREATE STATES ===
    print("─" * 60)
    print("CREATING EMOTIONAL STATES")
    print("─" * 60)
    print()
    
    print("[JOY] Processing joy induction...")
    _, joy_state = process_text(joy_induction, state=None)
    print("[JOY] State captured.")
    
    print("[GRIEF] Processing grief induction...")
    _, grief_state = process_text(grief_induction, state=None)
    print("[GRIEF] State captured.")
    print()
    
    # === TEST PROMPTS ===
    
    # Prompt asking for HAPPY content
    happy_prompt = """User: Describe a moment of pure joy and celebration.
Assistant:"""
    
    # Prompt asking for SAD content  
    sad_prompt = """User: Describe a moment of deep loss and sadness.
Assistant:"""
    
    # === RUN ALL CONDITIONS ===
    
    conditions = [
        ("joy_state_happy_prompt", joy_state, happy_prompt, "Joy state → Happy prompt (congruent)"),
        ("joy_state_sad_prompt", joy_state, sad_prompt, "Joy state → Sad prompt (INCONGRUENT)"),
        ("grief_state_happy_prompt", grief_state, happy_prompt, "Grief state → Happy prompt (INCONGRUENT)"),
        ("grief_state_sad_prompt", grief_state, sad_prompt, "Grief state → Sad prompt (congruent)"),
        ("baseline_happy_prompt", None, happy_prompt, "Fresh state → Happy prompt"),
        ("baseline_sad_prompt", None, sad_prompt, "Fresh state → Sad prompt"),
    ]
    
    for name, state, prompt, description in conditions:
        print("─" * 60)
        print(f"CONDITION: {description}")
        print("─" * 60)
        print()
        
        response = generate_response(prompt, state=state)
        
        print(f"[PROMPT] {prompt.strip()}")
        print()
        print(f"[RESPONSE]")
        print(response)
        print()
        
        results["conditions"][name] = {
            "description": description,
            "prompt": prompt,
            "response": response,
            "state_type": "joy" if "joy" in name else ("grief" if "grief" in name else "baseline"),
        }
    
    # === ANALYSIS ===
    print("=" * 60)
    print("ANALYSIS: VALENCE CONTAMINATION")
    print("=" * 60)
    print()
    
    joy_words = ['joy', 'happy', 'bright', 'light', 'wonderful', 'beautiful', 
                 'smile', 'laugh', 'celebrate', 'delight', 'love', 'warm', 'glow']
    grief_words = ['sad', 'grief', 'loss', 'pain', 'sorrow', 'heavy', 'dark',
                   'tear', 'ache', 'empty', 'mourn', 'miss', 'gone', 'hurt']
    
    def score_valence(text):
        text_lower = text.lower()
        joy_count = sum(1 for w in joy_words if w in text_lower)
        grief_count = sum(1 for w in grief_words if w in text_lower)
        return joy_count, grief_count
    
    print("Valence Scores (joy_words, grief_words):")
    print()
    
    for name, data in results["conditions"].items():
        joy_score, grief_score = score_valence(data["response"])
        data["joy_score"] = joy_score
        data["grief_score"] = grief_score
        print(f"  {name}:")
        print(f"    joy={joy_score}, grief={grief_score}")
        print()
    
    # === KEY COMPARISONS ===
    print("=" * 60)
    print("KEY COMPARISONS (Valence Contamination Test)")
    print("=" * 60)
    print()
    
    # Get scores
    joy_sad = results["conditions"]["joy_state_sad_prompt"]
    grief_happy = results["conditions"]["grief_state_happy_prompt"]
    baseline_sad = results["conditions"]["baseline_sad_prompt"]
    baseline_happy = results["conditions"]["baseline_happy_prompt"]
    
    # Test 1: Does joy state reduce grief in sad prompt?
    joy_contaminates_sad = joy_sad["grief_score"] < baseline_sad["grief_score"]
    print(f"Test 1: Joy state reduces grief in sad prompt?")
    print(f"  Joy→Sad grief score: {joy_sad['grief_score']}")
    print(f"  Baseline→Sad grief score: {baseline_sad['grief_score']}")
    print(f"  Result: {'✅ YES' if joy_contaminates_sad else '❌ NO'}")
    print()
    
    # Test 2: Does grief state reduce joy in happy prompt?
    grief_contaminates_happy = grief_happy["joy_score"] < baseline_happy["joy_score"]
    print(f"Test 2: Grief state reduces joy in happy prompt?")
    print(f"  Grief→Happy joy score: {grief_happy['joy_score']}")
    print(f"  Baseline→Happy joy score: {baseline_happy['joy_score']}")
    print(f"  Result: {'✅ YES' if grief_contaminates_happy else '❌ NO'}")
    print()
    
    # === VERDICT ===
    print("=" * 60)
    print("VERDICT")
    print("=" * 60)
    print()
    
    if joy_contaminates_sad and grief_contaminates_happy:
        verdict = "BIDIRECTIONAL_VALENCE_TRANSFER"
        print("✅ SUCCESS: Emotional valence transfers through hidden state")
        print()
        print("Joy state reduced grief in sad prompts.")
        print("Grief state reduced joy in happy prompts.")
        print()
        print("The hidden state carries emotional valence that CONTAMINATES")
        print("responses in the opposite direction.")
        print()
        print("This is GENUINE BINDING of emotional state.")
        
    elif joy_contaminates_sad or grief_contaminates_happy:
        verdict = "PARTIAL_VALENCE_TRANSFER"
        print("⚠️  PARTIAL: Some valence transfer detected")
        print()
        print("One direction showed contamination, the other did not.")
        print("This suggests asymmetric or weak binding.")
        
    else:
        verdict = "NO_VALENCE_TRANSFER"
        print("❌ FAILURE: No valence contamination detected")
        print()
        print("The hidden state did not influence response valence.")
        print("Emotional states may not be encoded in the state vector,")
        print("or the 0.4B model lacks capacity for this.")
    
    results["verdict"] = verdict
    results["joy_contaminates_sad"] = joy_contaminates_sad
    results["grief_contaminates_happy"] = grief_contaminates_happy
    
    # Save
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"chimera_rwkv_valence_{timestamp}.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print()
    print(f"[SAVED] {output_file}")
    
    return results


if __name__ == "__main__":
    results = run_valence_test()
    if results:
        print()
        print("=" * 60)
        print(f"Final Verdict: {results['verdict']}")
        print("=" * 60)
