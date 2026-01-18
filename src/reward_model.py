"""
reward_model.py

Demo-safe reward/scoring logic.

Instead of a learned reward model, we use a transparent heuristic score:
Higher is better.

Heuristics:
- Prefer open-ended questions ("why", "how", "what do you think")
- Prefer grounded questions that reference context (simple proxy: longer + contains "text" or "story")
- Penalize yes/no style prompts
"""

from __future__ import annotations


OPEN_ENDED_CUES = ["why", "how", "what do you think", "tell me", "describe", "predict"]
YES_NO_STARTS = ["did", "is", "are", "was", "were", "do", "does", "can", "could"]


def score(text: str) -> float:
    t = text.strip().lower()

    s = 0.0

    # Length proxy for specificity (capped)
    s += min(len(t) / 120.0, 2.0)

    # Reward open-ended cues
    for cue in OPEN_ENDED_CUES:
        if cue in t:
            s += 0.8

    # Reward grounding cues
    if "text" in t or "story" in t or "passage" in t:
        s += 0.6

    # Penalize yes/no starts
    first_word = t.split(" ")[0] if t else ""
    if first_word in YES_NO_STARTS:
        s -= 1.0

    return s


def choose(a: str, b: str) -> str:
    """Return the higher-scoring string."""
    return a if score(a) >= score(b) else b
