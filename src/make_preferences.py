"""
make_preferences.py

Creates (prompt, chosen, rejected) preference pairs for demo purposes.

We generate two candidate questions per prompt:
- a "chosen" example (more specific, open-ended, grounded)
- a "rejected" example (vague or yes/no)

Outputs: data/preferences.jsonl
"""

from __future__ import annotations

import json
from pathlib import Path


def load_prompts(path: Path) -> list[dict]:
    items = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            items.append(json.loads(line))
    return items


def build_pair(item: dict) -> dict:
    context = item["context"]
    prompt = item["prompt"]

    # Chosen: open-ended, specific, grounded in context
    chosen = (
        f"{prompt} In this story/passage: {context} "
        "What do you think will happen next, and what in the text makes you think that?"
    )

    # Rejected: vague, yes/no, not grounded
    rejected = "Did you like the story?"

    return {
        "id": item["id"],
        "context": context,
        "prompt": prompt,
        "chosen": chosen,
        "rejected": rejected,
    }


def main() -> None:
    data_dir = Path("data")
    prompts_path = data_dir / "prompts.jsonl"
    out_path = data_dir / "preferences.jsonl"

    prompts = load_prompts(prompts_path)
    pairs = [build_pair(p) for p in prompts]

    with out_path.open("w", encoding="utf-8") as f:
        for ex in pairs:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")

    print(f"Wrote {len(pairs)} preference pairs to {out_path}")


if __name__ == "__main__":
    main()
