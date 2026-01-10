# RLHF Question Generation Pipeline (Representative Implementation)

## Overview
This repository provides a clean, representative implementation of a pipeline for improving generated questions using preference data and policy optimization (DPO/GRPO-style).

## Pipeline
1. **ETL / Dataset Construction**
   - Load raw text documents (public or synthetic)
   - Clean and structure into training examples

2. **Preference Data**
   - Create (prompt, chosen, rejected) pairs
   - Support both human-labeled preferences and simulated preferences for demo purposes

3. **Optimization**
   - Train a lightweight reward model or scoring function
   - Optimize a policy using DPO/GRPO-style objectives (demo-scale)

4. **Evaluation**
   - Offline metrics (e.g., preference accuracy, rubric scores)
   - Basic safety checks (heuristic or model-based placeholders)

## Data
- Uses public-domain text or synthetic examples for demonstration.
- Original datasets and internal tooling from research/industry collaborations are not publicly shareable.

## How to Run (Demo)
```bash
pip install -r requirements.txt
python src/build_dataset.py
python src/make_preferences.py
python src/train_policy.py
python src/evaluate.py
