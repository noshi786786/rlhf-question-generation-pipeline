"""
build_dataset.py

Demo-scale dataset builder for question generation.

Creates a small JSONL file of prompts from public-safe, synthetic examples.
Outputs: data/prompts.jsonl
"""

from __future__ import annotations

import json
from pathlib import Path


PROMPTS = [
    {
        "id": "p001",
        "context": "A short story about a child learning to share toys with a friend.",
        "prompt": "Write one dialogic reading question that encourages the child to predict what happens next.",
    },
    {
        "id": "p002",
        "context": "A story where a dog gets lost and finds its way home.",
        "prompt": "Write one dialogic reading question that asks about the character’s feelings and why.",
    },
    {
        "id": "p003",
        "context": "A nonfiction passage about how plants grow from seeds.",
        "prompt": "Write one dialogic reading question that connects the text to the reader’s own experience.",
    },
    {
        "id": "p004",
        "context": "A story where two siblings solve a problem together.",
        "prompt": "Write one dialogic reading question that encourages reasoning (how/why).",
    },
    {
        "id": "p005",
        "context": "A story about a rainy day and finding fun indoors.",
        "prompt": "Write one dialogic reading question that invites descriptive language.",
    },
    {
        "id": "p006",
        "context": "A story where a character makes a mistake and apologizes.",
        "prompt": "Write one dialogic reading question about consequences and choices.",
    },
    {
        "id": "p007",
        "context": "A nonfiction passage about the water cycle.",
        "prompt": "Write one dialogic reading question that checks understanding of a key concept.",
    },
    {
        "id": "p008",
        "context": "A story where a character tries something new and feels nervous.",
        "prompt": "Write one dialogic reading question that supports empathy and perspective-taking.",
    },
]


def main() -> None:
    out_dir = Path("data")
    out_dir.mkdir(exist_ok=True)

    out_path = out_dir / "prompts.jsonl"
    with out_path.open("w", encoding="utf-8") as f:
        for item in PROMPTS:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"Wrote {len(PROMPTS)} prompts to {out_path}")


if __name__ == "__main__":
    main()
