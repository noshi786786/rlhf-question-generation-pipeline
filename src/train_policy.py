"""
train_policy.py

Demo-scale "policy" step.

In a full RLHF system, this would update a model policy using preference data.
Here, we define the policy as: choose the candidate with higher heuristic reward.

We save a small policy config to results/policy.json to show reproducibility.
"""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    policy = {
        "policy_type": "heuristic_reward_selection",
        "notes": "Demo policy chooses between candidate questions using transparent heuristic reward.",
    }

    (out_dir / "policy.json").write_text(json.dumps(policy, indent=2))
    print("Saved policy config to results/policy.json")
    print("Policy ready (demo-scale).")


if __name__ == "__main__":
    main()
