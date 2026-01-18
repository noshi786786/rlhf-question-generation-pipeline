# RLHF Question Generation Pipeline (Representative Implementation)

## Overview
This repository provides a clean, representative implementation of a pipeline for improving generated questions using preference data and policy optimization (DPO/GRPO-style). It is designed to demonstrate system architecture, data flow, and evaluation in a public-safe way.

## What this repo demonstrates
- Dataset construction (demo-scale ETL)
- Preference data formatting: (prompt, chosen, rejected)
- Reward/scoring logic (demo-safe)
- Policy improvement loop (demo-scale)
- Offline evaluation + lightweight safety checks

## Pipeline
1. **Build dataset**
   - Load public-domain text or synthetic examples
   - Clean and structure into training instances

2. **Create preferences**
   - Convert each prompt into (chosen, rejected) pairs
   - Supports simulated preferences for demo purposes

3. **Train / optimize**
   - Train a lightweight reward/scoring model (demo-safe)
   - Optimize a policy using a DPO/GRPO-style objective (demo-scale)

4. **Evaluate**
   - Preference agreement / win-rate
   - Rubric-style heuristic scores (clarity, specificity, groundedness)
   - Basic safety checks (placeholder heuristics)

## Data
- Uses public-domain or synthetic text for demonstration.
- Original datasets and internal application integrations from research/industry collaborations are not publicly shareable.

## Quickstart (Demo)
```bash
pip install -r requirements.txt
python -m src.build_dataset
python -m src.make_preferences
python -m src.train_policy
python -m src.evaluate

## What running the demo produces
After running the Quickstart commands, you should see:

- `data/prompts.jsonl` — demo prompt/context pairs
- `data/preferences.jsonl` — preference pairs: (prompt, chosen, rejected)
- `results/policy.json` — demo “policy” configuration
- `results/metrics.json` — evaluation metrics (e.g., win-rate)

## Example preference record (demo)
Each line in `data/preferences.jsonl` is a JSON object like:

```json
{
  "id": "p001",
  "context": "...",
  "prompt": "...",
  "chosen": "...",
  "rejected": "..."
}
