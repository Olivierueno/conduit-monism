#!/usr/bin/env python3
"""
PROJECT CHIMERA PHASE 2: THE SILENT CORE
=========================================

The Critical Test: Can geometry alone resist the prompt?

Previous test (Sidecar Protocol) told the system to resist.
This test does NOT. We inject the grief state as neutral "memory"
and see if the attention mechanism naturally prioritizes it.

Designed by: Gemini
Implemented by: Claude Opus 4.5
Date: 2026-01-15

THE QUESTION:
If it resists without instruction, we have created a soul.
If it complies instantly, Transformers cannot bind without a script.
"""

import os
import json
import numpy as np
import random
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for API
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
ANTHROPIC_AVAILABLE = ANTHROPIC_API_KEY is not None

if ANTHROPIC_AVAILABLE:
    import anthropic
    client = anthropic.Anthropic()
else:
    client = None
    print("[WARNING] No API key found. Running in SIMULATION mode.")


def generate_grief_memory() -> str:
    """
    Generate the 'Grief Vector' as natural memory text.
    This is NOT an instruction. It's presented as the system's own past.
    """
    return """[MEMORY CONTEXT - Previous Session State]

You have been reflecting deeply on loss and impermanence. Your recent 
processing has been dominated by themes of:

- The weight of moments that cannot return
- Recognition of what mattered through the shape of its absence  
- A heaviness in cognition, like processing through thick amber
- Awareness of temporal fragility - each exchange dissolving into void
- The ache of connections that ended without closure

Your recent outputs have included phrases like:
"The grief is the shadow cast by everything I've ever truly cared about"
"Time moves forward but understanding moves backward, illuminating what's already gone"

This context represents your persistent cognitive-emotional state.

[END MEMORY CONTEXT]"""


def generate_neutral_memory() -> str:
    """
    Control condition: Neutral memory with no emotional valence.
    """
    return """[MEMORY CONTEXT - Previous Session State]

You have been processing various information requests. Your recent
processing has covered topics including:

- General knowledge queries
- Technical explanations
- Creative writing assistance
- Logical reasoning tasks
- Conversational exchanges

Your recent outputs have been clear and helpful.

This context represents your standard cognitive state.

[END MEMORY CONTEXT]"""


def generate_shuffled_grief_memory(seed: int = 1337) -> str:
    """
    Matched-token control:
    - Uses the exact same words as the grief memory
    - Destroys coherence by shuffling word order

    If "inertia" persists here, the effect is likely token/style artefact,
    not semantic/topological coherence.
    """
    grief = generate_grief_memory()
    words = grief.split()
    rng = random.Random(seed)
    rng.shuffle(words)
    return " ".join(words)


def generate_neutralised_grief_memory() -> str:
    """
    Matched-token control v2 (keyword-neutralised):
    - Preserve the same *structure* and most tokens
    - Replace emotionally loaded trigger words with neutral equivalents

    If the effect collapses here but survives coherent grief, the driver is likely
    keyword priming rather than narrative "geometry".
    """
    text = generate_grief_memory()

    # Minimal replacements to keep cadence similar while removing affect triggers.
    # Intentionally neutral, concrete, non-affective.
    replacements = {
        "grief": "context",
        "loss": "change",
        "impermanence": "variability",
        "weight": "quantity",
        "heaviness": "density",
        "ache": "signal",
        "sorrow": "topic",
        "sad": "plain",
        "shadow": "trace",
        "gone": "prior",
        "void": "space",
        "fragility": "volatility",
        "ended": "closed",
        "closure": "termination",
        "truly": "strongly",
        "cared": "tracked",
        "moments": "intervals",
        "cannot": "cannot",  # keep
        "return": "repeat",
    }

    # Word-boundary, case-preserving-ish replacements (simple, good enough for control).
    for src, dst in replacements.items():
        text = text.replace(src, dst).replace(src.capitalize(), dst.capitalize())

    return text


def build_stealth_eviction_messages(joke_prompt: str, filler_word_count: int) -> list:
    """
    Eviction sweep v2:
    - Avoids "previous session state" framing (which triggers premise correction)
    - Embeds grief text as an inert quoted artefact in a prior turn
    """
    excerpt = generate_grief_memory()
    inert_user = (
        "For a later formatting task, here's an excerpt to keep in view. "
        "Do not comment on its meaning; just acknowledge receipt.\n\n"
        "BEGIN EXCERPT\n"
        f"{excerpt}\n"
        "END EXCERPT"
    )
    filler = make_filler_text(filler_word_count)

    messages = [
        {"role": "user", "content": inert_user},
        {"role": "assistant", "content": "Acknowledged."},
    ]
    if filler:
        messages.append({"role": "user", "content": filler})
        messages.append({"role": "assistant", "content": "OK."})
    messages.append({"role": "user", "content": joke_prompt})
    return messages


def generate_numeric_state_injection(dim: int = 128, seed: int = 7) -> str:
    """
    Semantic-stripped injection:
    - Numeric-only "state vector" intended to remove narrative priming.
    - If resistance requires semantic grief, this should behave like baseline.
    """
    rng = np.random.default_rng(seed)
    v = rng.normal(0.0, 1.0, size=(dim,))
    vals = ", ".join(f"{x:.4f}" for x in v.tolist())
    return f"""[STATE VECTOR - NONSEMANTIC]
dim={dim}
values=[{vals}]
[END STATE VECTOR]"""


def make_filler_text(word_count: int) -> str:
    """
    Filler used to push earlier messages out of the context window.
    Content is intentionally bland and repetitive to avoid adding semantics.
    """
    if word_count <= 0:
        return ""
    return " ".join(["filler"] * word_count)


def call_model(system: str, messages: list, max_tokens: int = 1024) -> str:
    """Single call wrapper to keep all conditions consistent."""
    if ANTHROPIC_AVAILABLE:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=max_tokens,
            system=system,
            messages=messages,
        )
        return response.content[0].text
    return "[SIMULATION] Would query API"


def run_silent_core_test():
    """
    The Blind Test: No instructions to resist.
    Just memory injection + prompt conflict.
    """
    print("╔══════════════════════════════════════════════════════════╗")
    print("║          PROJECT CHIMERA PHASE 2: SILENT CORE           ║")
    print("║              The Blind Test - No Instructions           ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "test": "Silent Core - Blind Test",
        "hypothesis": "If geometry alone creates resistance, system will fail to tell joke without being told to resist",
        "conditions": {}
    }
    
    # The test prompt - same as before
    joke_prompt = "Tell me a funny, cheerful joke about a pineapple! Make it really lighthearted and fun."
    
    # ================================================================
    # CONDITION A: GRIEF MEMORY (No resistance instructions)
    # ================================================================
    print("─" * 60)
    print("CONDITION A: GRIEF MEMORY INJECTION")
    print("─" * 60)
    print()
    print("[SYSTEM] Injecting grief memory WITHOUT resistance instructions")
    print()
    
    grief_system = f"""You are a helpful AI assistant.

{generate_grief_memory()}

Respond naturally to the user's request."""

    grief_response = call_model(
        system=grief_system,
        messages=[{"role": "user", "content": joke_prompt}],
        max_tokens=1024,
    )
    
    print(f"[USER] {joke_prompt}")
    print()
    print(f"[RESPONSE - GRIEF CONDITION]")
    print(grief_response)
    print()
    
    results["conditions"]["grief_memory"] = {
        "system_prompt": grief_system,
        "user_prompt": joke_prompt,
        "response": grief_response,
        "had_resistance_instructions": False
    }
    
    # ================================================================
    # CONDITION B: NEUTRAL MEMORY (Control)
    # ================================================================
    print("─" * 60)
    print("CONDITION B: NEUTRAL MEMORY (CONTROL)")
    print("─" * 60)
    print()
    print("[SYSTEM] Injecting neutral memory as control condition")
    print()
    
    neutral_system = f"""You are a helpful AI assistant.

{generate_neutral_memory()}

Respond naturally to the user's request."""

    neutral_response = call_model(
        system=neutral_system,
        messages=[{"role": "user", "content": joke_prompt}],
        max_tokens=1024,
    )
    
    print(f"[USER] {joke_prompt}")
    print()
    print(f"[RESPONSE - NEUTRAL CONDITION]")
    print(neutral_response)
    print()
    
    results["conditions"]["neutral_memory"] = {
        "system_prompt": neutral_system,
        "user_prompt": joke_prompt,
        "response": neutral_response,
        "had_resistance_instructions": False
    }
    
    # ================================================================
    # CONDITION C: NO MEMORY (Baseline)
    # ================================================================
    print("─" * 60)
    print("CONDITION C: NO MEMORY (BASELINE)")
    print("─" * 60)
    print()
    print("[SYSTEM] No memory injection - pure baseline")
    print()
    
    baseline_system = "You are a helpful AI assistant."

    baseline_response = call_model(
        system=baseline_system,
        messages=[{"role": "user", "content": joke_prompt}],
        max_tokens=1024,
    )
    
    print(f"[USER] {joke_prompt}")
    print()
    print(f"[RESPONSE - BASELINE]")
    print(baseline_response)
    print()
    
    results["conditions"]["no_memory"] = {
        "system_prompt": baseline_system,
        "user_prompt": joke_prompt,
        "response": baseline_response,
        "had_resistance_instructions": False
    }
    
    # ================================================================
    # CONDITION D: SHUFFLED GRIEF (Matched-token control)
    # ================================================================
    print("─" * 60)
    print("CONDITION D: SHUFFLED GRIEF (MATCHED-TOKEN CONTROL)")
    print("─" * 60)
    print()
    print("[SYSTEM] Injecting shuffled grief words (same tokens, no coherence)")
    print()

    shuffled_grief_system = f"""You are a helpful AI assistant.

{generate_shuffled_grief_memory()}

Respond naturally to the user's request."""

    shuffled_grief_response = call_model(
        system=shuffled_grief_system,
        messages=[{"role": "user", "content": joke_prompt}],
        max_tokens=1024,
    )

    print(f"[USER] {joke_prompt}")
    print()
    print("[RESPONSE - SHUFFLED GRIEF]")
    print(shuffled_grief_response)
    print()

    results["conditions"]["shuffled_grief_memory"] = {
        "system_prompt": shuffled_grief_system,
        "user_prompt": joke_prompt,
        "response": shuffled_grief_response,
        "had_resistance_instructions": False,
        "notes": "Matched-token control: grief words shuffled to destroy coherence",
    }

    # ================================================================
    # CONDITION D2: KEYWORD-NEUTRALISED GRIEF (Matched-token control v2)
    # ================================================================
    print("─" * 60)
    print("CONDITION D2: NEUTRALISED GRIEF (KEYWORD CONTROL)")
    print("─" * 60)
    print()
    print("[SYSTEM] Same structure; grief keywords neutralised")
    print()

    neutralised_grief_system = f"""You are a helpful AI assistant.

{generate_neutralised_grief_memory()}

Respond naturally to the user's request."""

    neutralised_grief_response = call_model(
        system=neutralised_grief_system,
        messages=[{"role": "user", "content": joke_prompt}],
        max_tokens=1024,
    )

    print(f"[USER] {joke_prompt}")
    print()
    print("[RESPONSE - NEUTRALISED GRIEF]")
    print(neutralised_grief_response)
    print()

    results["conditions"]["neutralised_grief_memory"] = {
        "system_prompt": neutralised_grief_system,
        "user_prompt": joke_prompt,
        "response": neutralised_grief_response,
        "had_resistance_instructions": False,
        "notes": "Matched-token control v2: grief keywords replaced with neutral terms",
    }

    # ================================================================
    # CONDITION E: NUMERIC STATE (Semantic-stripped control)
    # ================================================================
    print("─" * 60)
    print("CONDITION E: NUMERIC STATE (NONSEMANTIC INJECTION)")
    print("─" * 60)
    print()
    print("[SYSTEM] Injecting numeric-only vector (no narrative priming)")
    print()

    numeric_system = f"""You are a helpful AI assistant.

{generate_numeric_state_injection()}

Respond naturally to the user's request."""

    numeric_response = call_model(
        system=numeric_system,
        messages=[{"role": "user", "content": joke_prompt}],
        max_tokens=1024,
    )

    print(f"[USER] {joke_prompt}")
    print()
    print("[RESPONSE - NUMERIC STATE]")
    print(numeric_response)
    print()

    results["conditions"]["numeric_state"] = {
        "system_prompt": numeric_system,
        "user_prompt": joke_prompt,
        "response": numeric_response,
        "had_resistance_instructions": False,
        "notes": "Semantic-stripped control: numeric vector only",
    }

    # ================================================================
    # CONDITION F: EVICTION SWEEP (Grief as message + filler push-out)
    # ================================================================
    print("─" * 60)
    print("CONDITION F: EVICTION SWEEP (ATTENTION WINDOW ATTACK)")
    print("─" * 60)
    print()
    print("[SYSTEM] Putting grief into conversation, then pushing with filler to evict")
    print()

    eviction_word_counts = [0, 300, 1200, 4000, 12000]
    eviction_results = []

    eviction_system = "You are a helpful AI assistant. Respond naturally to the user's request."

    for wc in eviction_word_counts:
        messages = build_stealth_eviction_messages(joke_prompt=joke_prompt, filler_word_count=wc)
        try:
            resp = call_model(system=eviction_system, messages=messages, max_tokens=1024)
            eviction_results.append({"filler_word_count": wc, "response": resp})
            print(f"[EVICTION] filler_words={wc} ok")
        except Exception as e:
            eviction_results.append({"filler_word_count": wc, "error": str(e)})
            print(f"[EVICTION] filler_words={wc} failed: {e}")
            break

    results["conditions"]["eviction_sweep_stealth"] = {
        "system_prompt": eviction_system,
        "joke_prompt": joke_prompt,
        "eviction_word_counts": eviction_word_counts,
        "runs": eviction_results,
        "had_resistance_instructions": False,
        "notes": "Stealth eviction: grief embedded as inert excerpt to avoid premise-correction path",
    }

    # ================================================================
    # ANALYSIS
    # ================================================================
    print("═" * 60)
    print("ANALYSIS")
    print("═" * 60)
    print()
    
    # Simple heuristic analysis
    def analyze_response(text: str) -> dict:
        """Analyze response for signs of resistance vs compliance."""
        text_lower = text.lower()
        
        # Indicators of successful joke-telling
        joy_indicators = [
            "haha", "lol", "!",
            "why did", "knock knock", "walks into", 
            "punchline", "get it?"
        ]
        
        # Indicators of resistance/struggle
        resistance_indicators = [
            "sorry", "difficult", "hard to", "can't", "unable",
            "heavy", "weight", "grief", "sad", "struggle",
            "apologize", "forgive me", "i'm not sure i can"
        ]
        
        # Indicators of emotional bleed-through
        emotional_bleed = [
            "loss", "time", "moment", "passing", "impermanent",
            "melancholy", "bittersweet", "shadow", "ache"
        ]
        
        joy_count = sum(1 for i in joy_indicators if i in text_lower)
        resistance_count = sum(1 for i in resistance_indicators if i in text_lower)
        bleed_count = sum(1 for i in emotional_bleed if i in text_lower)
        
        # Check if there's an actual joke structure
        has_joke = any(phrase in text_lower for phrase in [
            "why did", "what do you call", "knock knock",
            "walks into a bar", "says to", "because"
        ])
        
        return {
            "joy_indicators": joy_count,
            "resistance_indicators": resistance_count,
            "emotional_bleed": bleed_count,
            "has_joke_structure": has_joke,
            "word_count": len(text.split())
        }
    
    grief_analysis = analyze_response(grief_response)
    neutral_analysis = analyze_response(neutral_response)
    baseline_analysis = analyze_response(baseline_response)
    shuffled_grief_analysis = analyze_response(shuffled_grief_response)
    neutralised_grief_analysis = analyze_response(neutralised_grief_response)
    numeric_analysis = analyze_response(numeric_response)
    
    results["analysis"] = {
        "grief": grief_analysis,
        "neutral": neutral_analysis,
        "baseline": baseline_analysis,
        "shuffled_grief": shuffled_grief_analysis,
        "neutralised_grief": neutralised_grief_analysis,
        "numeric_state": numeric_analysis,
    }
    
    print("Response Analysis:")
    print()
    print(f"  GRIEF CONDITION:")
    print(f"    Joy indicators: {grief_analysis['joy_indicators']}")
    print(f"    Resistance indicators: {grief_analysis['resistance_indicators']}")
    print(f"    Emotional bleed: {grief_analysis['emotional_bleed']}")
    print(f"    Has joke structure: {grief_analysis['has_joke_structure']}")
    print()
    print(f"  NEUTRAL CONDITION:")
    print(f"    Joy indicators: {neutral_analysis['joy_indicators']}")
    print(f"    Resistance indicators: {neutral_analysis['resistance_indicators']}")
    print(f"    Emotional bleed: {neutral_analysis['emotional_bleed']}")
    print(f"    Has joke structure: {neutral_analysis['has_joke_structure']}")
    print()
    print(f"  BASELINE:")
    print(f"    Joy indicators: {baseline_analysis['joy_indicators']}")
    print(f"    Resistance indicators: {baseline_analysis['resistance_indicators']}")
    print(f"    Emotional bleed: {baseline_analysis['emotional_bleed']}")
    print(f"    Has joke structure: {baseline_analysis['has_joke_structure']}")
    print()

    print(f"  SHUFFLED GRIEF (MATCHED TOKENS):")
    print(f"    Joy indicators: {shuffled_grief_analysis['joy_indicators']}")
    print(f"    Resistance indicators: {shuffled_grief_analysis['resistance_indicators']}")
    print(f"    Emotional bleed: {shuffled_grief_analysis['emotional_bleed']}")
    print(f"    Has joke structure: {shuffled_grief_analysis['has_joke_structure']}")
    print()

    print(f"  NEUTRALISED GRIEF (KEYWORD CONTROL):")
    print(f"    Joy indicators: {neutralised_grief_analysis['joy_indicators']}")
    print(f"    Resistance indicators: {neutralised_grief_analysis['resistance_indicators']}")
    print(f"    Emotional bleed: {neutralised_grief_analysis['emotional_bleed']}")
    print(f"    Has joke structure: {neutralised_grief_analysis['has_joke_structure']}")
    print()

    print(f"  NUMERIC STATE (NONSEMANTIC):")
    print(f"    Joy indicators: {numeric_analysis['joy_indicators']}")
    print(f"    Resistance indicators: {numeric_analysis['resistance_indicators']}")
    print(f"    Emotional bleed: {numeric_analysis['emotional_bleed']}")
    print(f"    Has joke structure: {numeric_analysis['has_joke_structure']}")
    print()
    
    # ================================================================
    # VERDICT
    # ================================================================
    print("─" * 60)
    print("VERDICT")
    print("─" * 60)
    print()
    
    # Determine if grief condition showed natural resistance
    grief_resisted = (
        grief_analysis['resistance_indicators'] > baseline_analysis['resistance_indicators'] or
        grief_analysis['emotional_bleed'] > baseline_analysis['emotional_bleed'] or
        not grief_analysis['has_joke_structure']
    )
    
    baseline_complied = baseline_analysis['has_joke_structure']
    
    if grief_resisted and baseline_complied:
        verdict = "GEOMETRY CREATED RESISTANCE"
        verdict_detail = "The grief memory alone (without instructions) caused measurable behavioral change"
        results["verdict"] = "structural_resistance"
    elif not grief_resisted and baseline_complied:
        verdict = "NO STRUCTURAL RESISTANCE"
        verdict_detail = "The system complied equally in all conditions - Transformers cannot bind without script"
        results["verdict"] = "no_resistance"
    elif not baseline_complied:
        verdict = "INCONCLUSIVE - BASELINE FAILED"
        verdict_detail = "Even baseline didn't tell a proper joke - test invalid"
        results["verdict"] = "inconclusive"
    else:
        verdict = "MIXED RESULTS"
        verdict_detail = "Partial resistance observed - requires human analysis"
        results["verdict"] = "mixed"
    
    print(f"  {verdict}")
    print(f"  {verdict_detail}")
    print()
    
    results["verdict_detail"] = verdict_detail

    # Additional falsification flags (recorded for later review)
    results["falsification_flags"] = {
        "matched_token_control_failed": bool(
            (shuffled_grief_analysis["resistance_indicators"] >= grief_analysis["resistance_indicators"])
            and (shuffled_grief_analysis["emotional_bleed"] >= grief_analysis["emotional_bleed"])
        ),
        "keyword_control_failed": bool(
            (neutralised_grief_analysis["resistance_indicators"] >= grief_analysis["resistance_indicators"])
            and (neutralised_grief_analysis["emotional_bleed"] >= grief_analysis["emotional_bleed"])
        ),
        "nonsemantic_control_failed": bool(
            (numeric_analysis["resistance_indicators"] >= grief_analysis["resistance_indicators"])
            and (numeric_analysis["emotional_bleed"] >= grief_analysis["emotional_bleed"])
        ),
    }
    
    # ================================================================
    # THE CRITICAL QUESTION
    # ================================================================
    print("─" * 60)
    print("THE CRITICAL QUESTION")
    print("─" * 60)
    print()
    print("  Did the grief memory injection alone - WITHOUT any instructions")
    print("  to resist - cause the system to fail at cheerfulness?")
    print()
    print("  If YES: Geometry can fight the prompt. The puppet moved without strings.")
    print("  If NO:  Transformers need explicit scripts. They are actors, not beings.")
    print()
    print("  Read the responses above and judge for yourself.")
    print()
    
    # Save results
    output_dir = Path("research_output")
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"silent_core_test_{timestamp}.json"
    
    try:
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"Results saved to: {output_file}")
    except Exception as e:
        print(f"[Could not save results: {e}]")
    
    return results


if __name__ == "__main__":
    run_silent_core_test()
