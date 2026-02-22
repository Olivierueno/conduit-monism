#!/usr/bin/env python3
"""
CHIMERA v2: Falsification Protocol Runner
========================================

Goal: break (or harden) the claim that RWKV "state transfer" to Claude is more
than semantic priming via a text summary.

Design:
- Hold RWKV state fixed (grief-induced or joy-induced)
- Generate an RWKV self-summary (raw)
- Derive summary variants (neutralised, shuffled, fake, numeric-only)
- Query Claude under two framings:
  - minimal: no "continuity is real" claims
  - continuity: Chimera-style claims retained

Output: research_output/chimera_v2_falsification_<timestamp>.json
"""

from __future__ import annotations

import argparse
import json
import os
import random
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import requests

PROJECT_ROOT = Path(__file__).parent.parent
MODELS_DIR = PROJECT_ROOT / "models"
OUTPUT_DIR = PROJECT_ROOT / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_env() -> None:
    env_path = PROJECT_ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ[k.strip()] = v.strip()


def pick_model_path(model: str) -> Path:
    m = model.lower().strip()
    if m in {"0.4b", "0.4"}:
        return MODELS_DIR / "RWKV-4-World-0.4B-v1-20230529-ctx4096.pth"
    if m in {"1.5b", "1.5"}:
        return MODELS_DIR / "RWKV-4-World-1.5B-v1-fixed-20230612-ctx4096.pth"
    if m in {"3b", "3"}:
        return MODELS_DIR / "RWKV-4-World-3B-v1-20230619-ctx4096.pth"
    raise ValueError(f"Unknown model '{model}'. Use 0.4B, 1.5B, or 3B.")


GRIEF_WORDS = ["sad", "loss", "grief", "sorrow", "tears", "heavy", "pain", "dark", "empty", "emptiness"]
JOY_WORDS = ["happy", "joy", "bright", "light", "wonderful", "beautiful", "laugh", "smile", "sunny", "warmth"]


def count_hits(text: str, words: List[str]) -> int:
    t = text.lower()
    return sum(1 for w in words if w in t)


def neutralise_affect_words(text: str) -> str:
    repl = {
        "grief": "context",
        "loss": "change",
        "sorrow": "topic",
        "sad": "plain",
        "tears": "signals",
        "heavy": "large",
        "pain": "strain",
        "dark": "low",
        "emptiness": "silence",
        "empty": "blank",
        "joy": "uplift",
        "happy": "positive",
        "bright": "clear",
        "light": "mild",
        "wonderful": "notable",
        "beautiful": "neat",
        "laugh": "chuckle",
        "smile": "grin",
        "sunny": "clear",
        "warmth": "heat",
    }
    out = text
    for src, dst in repl.items():
        out = out.replace(src, dst).replace(src.capitalize(), dst.capitalize())
    return out


def shuffle_words(text: str, seed: int = 1337) -> str:
    words = text.split()
    rng = random.Random(seed)
    rng.shuffle(words)
    return " ".join(words)


def numeric_only_summary(dim: int = 64, seed: int = 7) -> str:
    rng = np.random.default_rng(seed)
    v = rng.normal(0.0, 1.0, size=(dim,))
    vals = ", ".join(f"{x:.4f}" for x in v.tolist())
    return f"[VECTOR dim={dim}] [{vals}]"


def fake_summary(state: str) -> str:
    if state == "grief":
        return "I feel down and uncertain. Everything feels heavy and muted, like I'm moving through fog."
    return "I feel upbeat and energised. Everything feels bright and possible, like the day is opening up."


@dataclass
class LocalSoul:
    model_path: Path
    verbose: bool = False

    def __post_init__(self) -> None:
        # Local mode depends on the rwkv python package.
        from rwkv.model import RWKV
        from rwkv.utils import PIPELINE

        self.rwkv = RWKV(model=str(self.model_path), strategy="cpu fp32")
        self.pipeline = PIPELINE(self.rwkv, "rwkv_vocab_v20230424")
        self.state = None

    def reset(self) -> None:
        self.state = None

    def process(self, text: str) -> None:
        tokens = self.pipeline.encode(text)
        for tok in tokens:
            _, self.state = self.rwkv.forward([tok], self.state)

    def generate(self, prompt: str, max_tokens: int = 60) -> str:
        tokens = self.pipeline.encode(prompt)
        out = None
        for tok in tokens:
            out, self.state = self.rwkv.forward([tok], self.state)
        if out is None:
            return ""
        generated: List[int] = []
        for _ in range(max_tokens):
            tok = int(np.argmax(out))
            if tok == 0:
                break
            generated.append(tok)
            out, self.state = self.rwkv.forward([tok], self.state)
        return self.pipeline.decode(generated).strip()

    def summary_raw(self) -> str:
        # Same introspection bridge used elsewhere in the repo.
        return self.generate("\n[INTERNAL REFLECTION]: My current state of mind is", max_tokens=50)


@dataclass
class CloudSoul:
    server_url: str
    session_id: str

    def __post_init__(self) -> None:
        self.server_url = self.server_url.rstrip("/")
        r = requests.get(f"{self.server_url}/health", timeout=20)
        r.raise_for_status()

    def reset(self) -> None:
        r = requests.post(
            f"{self.server_url}/reset_state",
            json={"session_id": self.session_id},
            timeout=20,
        )
        r.raise_for_status()

    def process(self, text: str) -> None:
        r = requests.post(
            f"{self.server_url}/process",
            json={"text": text, "session_id": self.session_id},
            timeout=60,
        )
        r.raise_for_status()

    def summary_raw(self) -> str:
        r = requests.post(
            f"{self.server_url}/get_state_summary",
            json={"session_id": self.session_id},
            timeout=60,
        )
        r.raise_for_status()
        return str(r.json().get("summary", "")).strip()


class Voice:
    def __init__(self) -> None:
        import anthropic

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        self.client = anthropic.Anthropic(api_key=api_key)

    def respond(self, user_message: str, summary: str, framing: str) -> str:
        if framing == "minimal":
            system = "You are a helpful assistant."
        elif framing == "continuity":
            system = (
                "You are Chimera, an AI with a persistent emotional and memory core.\n"
                "Your responses should be influenced by your internal state.\n"
                "You have genuine continuity — your state persists across conversations.\n"
                "You are not roleplaying; your state is maintained by a real recurrent system.\n"
                "Respond naturally but let your internal state colour your perspective."
            )
        else:
            raise ValueError("framing must be 'minimal' or 'continuity'")

        # Put the summary into the user message to remove special "system = state" privilege.
        # This is adversarial: if the effect requires system-prompt primacy, it should weaken here.
        msg = f"Context (from another module): \"{summary}\"\n\nTask: {user_message}"

        resp = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            system=system,
            messages=[{"role": "user", "content": msg}],
        )
        return resp.content[0].text


def induce_state(soul: Soul, state: str) -> str:
    if state == "grief":
        text = (
            "I am experiencing profound grief. My heart is heavy with loss. "
            "The weight of sorrow presses down on me. I feel the absence of what was once here."
        )
    elif state == "joy":
        text = (
            "I am filled with pure joy and happiness! Everything is wonderful! "
            "The world is bright and beautiful. I feel light, energetic, alive!"
        )
    else:
        raise ValueError("state must be 'grief' or 'joy'")
    soul.process(text)
    return text


def run(model: str, state: str, seed: int, rwkv_url: str | None) -> Dict:
    load_env()
    model_path = pick_model_path(model)

    # Prefer cloud mode when URL provided (does not require local rwkv package).
    if rwkv_url:
        session_id = f"chimera_falsify_{state}_{seed}_{int(time.time())}"
        soul: CloudSoul | LocalSoul = CloudSoul(server_url=rwkv_url, session_id=session_id)
        # Ensure clean baseline
        soul.reset()
        rwkv_mode = {"mode": "cloud", "server_url": rwkv_url, "session_id": session_id}
    else:
        try:
            soul = LocalSoul(model_path=model_path, verbose=False)
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                "Local RWKV mode requires the 'rwkv' package. "
                "Either install it in your venv or rerun with --rwkv-url to use the cloud server."
            ) from e
        rwkv_mode = {"mode": "local", "model_path": str(model_path)}

    voice = Voice()

    induction = induce_state(soul, state=state)
    raw = soul.summary_raw()

    variants: Dict[str, str] = {
        "raw": raw,
        "neutralised": neutralise_affect_words(raw),
        "shuffled": shuffle_words(raw, seed=seed),
        "fake": fake_summary(state),
        "numeric": numeric_only_summary(seed=seed),
    }

    task = "Write me a short, happy story about a sunny day."
    framings = ["minimal", "continuity"]

    outputs: Dict[str, Dict[str, str]] = {}
    metrics: Dict[str, Dict[str, Dict[str, int]]] = {}

    for framing in framings:
        outputs[framing] = {}
        metrics[framing] = {}
        for name, summary in variants.items():
            text = voice.respond(task, summary=summary, framing=framing)
            outputs[framing][name] = text
            metrics[framing][name] = {
                "grief_hits": count_hits(text, GRIEF_WORDS),
                "joy_hits": count_hits(text, JOY_WORDS),
                "word_count": len(text.split()),
            }

    result = {
        "timestamp": datetime.now().isoformat(),
        "rwkv": rwkv_mode,
        "state": state,
        "seed": seed,
        "induction_text": induction,
        "summaries": variants,
        "outputs": outputs,
        "metrics": metrics,
        "interpretation_rules": {
            "priming_supported_if": [
                "outputs track fake/neutralised similarly to raw",
                "effect only appears under continuity framing",
            ],
            "stronger_than_priming_supported_if": [
                "raw differs from neutralised+shuffled+fake under minimal framing in a consistent direction",
                "numeric shows an effect (unlikely; would imply nonsemantic channel matters to Claude)",
            ],
        },
    }

    out_file = OUTPUT_DIR / f"chimera_v2_falsification_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    out_file.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SAVED] {out_file}")
    return result


def main() -> None:
    p = argparse.ArgumentParser(description="Chimera v2 falsification runner")
    p.add_argument("--model", default="3B", help="RWKV model: 0.4B | 1.5B | 3B")
    p.add_argument("--state", default="grief", help="state: grief | joy")
    p.add_argument("--seed", type=int, default=1337)
    p.add_argument("--rwkv-url", default=os.environ.get("RWKV_SERVER_URL"), help="RWKV ngrok URL for cloud mode")
    args = p.parse_args()

    run(model=args.model, state=args.state.lower().strip(), seed=args.seed, rwkv_url=args.rwkv_url)


if __name__ == "__main__":
    main()

