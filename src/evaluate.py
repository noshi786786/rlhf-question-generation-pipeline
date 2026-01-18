"""
evaluate.py

Offline evaluation for the demo RLHF pipeline.

We compute a simple win-rate:
- For each preference example, the "chosen" response is preferred.
- Our policy chooses between (chosen, rejected) using heuristic reward.
- Win-rate = fraction where policy picks the chosen response.
"""

from __future__ import annotations

import json
from pathlib import Path

from src.reward_model import choose


def load_preferences(path: Path) -> list[dict]:
    items = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            items.append(json.loads(line))
    return items


def main() -> None:
    prefs_path = Path("data") / "preferences.jsonl"
    prefs = load_preferences(prefs_path)

    wins = 0
    for ex in prefs:
        picked = choose(ex["chosen"], ex["rejected"])
        if picked == ex["chosen"]:
            wins += 1

    win_rate = wins / max(len(prefs), 1)

    print(f"Examples evaluated: {len(prefs)}")
    print(f"Policy win-rate:   {win_rate:.3f}")

    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)
    (out_dir / "metrics.json").write_text(json.dumps({"win_rate": win_rate, "n": len(prefs)}, indent=2))
    print("Saved metrics to results/metrics.json")


if __name__ == "__main__":
    main()
