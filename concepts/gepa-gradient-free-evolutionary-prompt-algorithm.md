---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 63a3add7b2b7d64bcca3e17f9d0773a5a5e9ad8f764caa1f15a14ecedd41e211
  pageDirectory: concepts
  sources:
    - optimize-prompts-tutorial-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gepa-gradient-free-evolutionary-prompt-algorithm
    - G(EPA
    - GEPA
  citations:
    - file: optimize-prompts-tutorial-databricks-on-aws.md
title: GEPA (Gradient-Free Evolutionary Prompt Algorithm)
description: An evolutionary optimization algorithm used by MLflow to iteratively refine prompt templates without gradient computation
tags:
  - optimization
  - evolutionary-algorithm
  - prompt-engineering
timestamp: "2026-06-19T19:52:14.844Z"
---

# GEPA (Gradient-Free Evolutionary Prompt Algorithm)

**GEPA (Gradient-Free Evolutionary Prompt Algorithm)** is a prompt optimization technique provided by [MLflow](/concepts/mlflow.md)’s `mlflow.genai.optimize` module. It applies evolutionary search to automatically improve prompt templates for large language models, using a **reflection model** to generate candidate refinements and a **scorer** to evaluate their quality against training data. ^[optimize-prompts-tutorial-databricks-on-aws.md]

## Overview

GEPA is designed for tasks where the goal is to adapt a generic prompt (e.g., `"classify this: {{query}}"`) to produce outputs that match specific formatting or content constraints. It is gradient‑free — it does not rely on backpropagation or model gradients — and instead explores the space of prompt variations through an evolutionary process guided by feedback from a more capable language model. ^[optimize-prompts-tutorial-databricks-on-aws.md]

In the tutorial that introduces GEPA, it is used to optimize a classification prompt for a **GPT-OSS 20B** model (served via Databricks Foundation Model APIs). The initial prompt is a bare‑bones instruction; after optimization, it outputs only the expected classification label (e.g., `BACKGROUND`, `METHODS`) without additional explanation. ^[optimize-prompts-tutorial-databricks-on-aws.md]

## How It Works

GEPA operates in an iterative loop:

1. **Initial prompt** — A user‑defined prompt template is registered via `mlflow.genai.register_prompt()`.
2. **Training data** — A dataset of input‑output pairs, together with optional `expectations` (such as required facts), is provided as `train_data`.
3. **Reflection model** — Specified through the `reflection_model` parameter of `GepaPromptOptimizer`. This model (e.g., Claude Sonnet 4‑5) critiques the current prompt and suggests improved versions.
4. **Scorer** — A configurable scorer (e.g., `Correctness` using GPT‑5) evaluates each candidate prompt on the training data by comparing its predictions against the expected outputs.
5. **Evolution** — The algorithm evolves the prompt by combining reflection‑based suggestions with selection pressure from the scorer. The best‑performing prompt is returned.

The result is an **optimized prompt** stored as a new prompt version, which can be loaded and used in a prediction function. ^[optimize-prompts-tutorial-databricks-on-aws.md]

## Usage Example

The following code snippet demonstrates the core workflow. The initial prompt `"classify this: {{query}}"` is registered, a prediction function is defined, and GEPA is invoked via `mlflow.genai.optimize_prompts()`.

```python
import mlflow
from mlflow.genai.optimize import [[gepapromptoptimizer|GepaPromptOptimizer]]
from mlflow.genai.scorers import Correctness

# Register initial prompt
prompt = mlflow.genai.register_prompt(
    name="my_catalog.my_schema.qa",
    template="classify this: {{query}}",
)

# Define prediction function
def predict_fn(query: str) -> str:
    prompt_version = mlflow.genai.load_prompt("prompts:/my_catalog.my_schema.qa/1")
    completion = openai_client.chat.completions.create(
        model="databricks-gpt-oss-20b",
        messages=[{"role": "user", "content": prompt_version.format(query=query)}],
    )
    return completion.choices[0].message.content

# Optimize
result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,          # list of dicts with inputs, outputs, expectations
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(
        reflection_model="databricks:/databricks-claude-sonnet-4-5"
    ),
    scorers=[Correctness(model="databricks:/databricks-gpt-5")],
)

optimized_prompt = result.optimized_prompts[0]
print(f"Optimized template: {optimized_prompt.template}")
```

^[optimize-prompts-tutorial-databricks-on-aws.md]

## Requirements

- Access to **Databricks Foundation Model APIs** (e.g., `databricks-gpt-oss-20b` for the prediction function, a reflection model, and a scorer model).
- The reflection model and scorer must be accessible via Databricks serving endpoints (e.g., `databricks:/databricks-claude-sonnet-4-5`, `databricks:/databricks-gpt-5`).
- The training dataset must contain `inputs`, `outputs`, and optionally `expectations` fields to guide optimization.

## Related Concepts

- [MLflow Prompt Optimization](/concepts/mlflow-prompt-optimization-api.md) — The broader framework that includes GEPA.
- Reflection Model — The LLM used to critique and refine prompts during evolution.
- [[Scorers|Scorer]] — A metric function that measures prompt quality on training data.
- [[GPT-OSS 20B]] — An open‑source model used in the tutorial as the target prediction model.
- [Prompt Versioning](/concepts/prompt-versioning.md) — How optimized prompts are stored and loaded via `mlflow.genai`.

## Sources

- optimize-prompts-tutorial-databricks-on-aws.md

# Citations

1. [optimize-prompts-tutorial-databricks-on-aws.md](/references/optimize-prompts-tutorial-databricks-on-aws-b91f2148.md)
