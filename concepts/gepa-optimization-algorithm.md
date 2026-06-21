---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a894206cea7f6a9c93f007e118f1492bce7453f664466efcdd57aaf336e2c050
  pageDirectory: concepts
  sources:
    - mlflow-prompt-optimization-beta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gepa-optimization-algorithm
    - GOA
    - GEPA algorithm
  citations:
    - file: mlflow-prompt-optimization-beta-databricks-on-aws.md
title: GEPA Optimization Algorithm
description: Generative Evolutionary Prompt Algorithm (GEPA) - the prompt optimization algorithm implemented via GepaPromptOptimizer, researched by Databricks AI Research Team, which iteratively refines prompts using LLM-driven reflection and automated feedback.
tags:
  - algorithm
  - optimization
  - mlflow
  - llm
timestamp: "2026-06-19T19:39:25.742Z"
---

---
title: GEPA Optimization Algorithm
summary: An LLM-driven prompt optimization algorithm that iteratively refines prompts using automated feedback, reducing manual effort and improving prompt quality.
sources:
  - mlflow-prompt-optimization-beta-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T21:00:00.000Z"
updatedAt: "2026-06-19T21:00:00.000Z"
tags:
  - mlflow
  - prompt-optimization
  - generative-ai
  - algorithms
aliases:
  - gepa-optimization-algorithm
  - GEPA
  - gepa-prompt-optimizer
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# GEPA Optimization Algorithm

The **GEPA Optimization Algorithm** (short for *Gradient‑free Evolutionary Prompt Adaptation*) is an automated prompt optimization algorithm researched and validated by the Databricks AI Research Team. It iteratively refines prompts using LLM‑driven reflection and automated feedback, leading to systematic, data‑driven improvements without manual tuning.^[mlflow-prompt-optimization-beta-databricks-on-aws.md] The algorithm is described in the preprint *GEPA: Automated Prompt Optimization for Enterprise Agents* (arXiv:2507.19457).^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Overview

MLflow supports the GEPA algorithm through the [`GepaPromptOptimizer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.optimize.[GepaPromptOptimizer](/concepts/gepapromptoptimizer.md)) class, which is used with the [`mlflow.genai.optimize_prompts()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.optimize_prompt) API. The optimizer takes a starting prompt, a set of training data, evaluation scorers, and a reflection model, then produces an improved prompt that performs better on the specified criteria.^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

### Key Benefits

- **Automatic Improvement**: Optimizes prompts based on evaluation metrics without manual tuning.
- **Data‑Driven Optimization**: Uses your training data and custom scorers to guide the search.
- **Framework Agnostic**: Works with any agent framework, providing broad compatibility.
- **Joint Optimization**: Enables simultaneous refinement of multiple prompts for best overall performance.
- **Flexible Evaluation**: Supports custom scorers and aggregation functions.
- **Version Control**: Automatically registers optimized prompts in the [MLflow Prompt Registry](/concepts/prompt-registry.md).
- **Extensible**: Allows plugging in custom optimization algorithms by extending the base class.^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Usage

The basic workflow requires:

1. A `predict_fn` that calls a prompt from the registry.
2. Training data (a list of inputs with expected outputs).
3. One or more prompt URIs pointing to [PromptVersion](/concepts/prompt-versioning.md) entries.
4. An instance of `GepaPromptOptimizer` specifying a reflection model.
5. A list of scorers (e.g., `Correctness`, `Safety`).

Example for improving accuracy:

```python
from mlflow.genai.scorers import Correctness

result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gpt-5"),
    scorers=[Correctness(model="databricks:/databricks-claude-sonnet-4-5")],
)
```

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

The algorithm can also optimize for safeness using the `Safety` scorer.^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

### Requirements

The `optimize_prompts` API requires **MLflow >= 3.5.0**.^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Troubleshooting

If optimization takes too long, reduce the dataset size or lower the optimizer budget (`max_metric_calls`). If no improvement is observed, verify that the scorers accurately measure the desired quality, increase training data diversity, or adjust optimizer configurations. Ensure `predict_fn` calls `mlflow.entities.model_registry.PromptVersion.format` so that the optimizer can reference the registry prompt.^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Related Concepts

- Prompt Optimization – The broader category of automated prompt tuning.
- [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) – The MLflow class implementing the GEPA algorithm.
- [MLflow Prompt Registry](/concepts/prompt-registry.md) – Storage for version‑controlled prompts.
- [Evaluation Scorers](/concepts/hallucination-scorer.md) – Metrics used to guide prompt improvement.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Framework for evaluating generative AI agents.
- LLM-driven reflection – The mechanism by which GEPA refines prompts.

## Sources

- mlflow-prompt-optimization-beta-databricks-on-aws.md

# Citations

1. [mlflow-prompt-optimization-beta-databricks-on-aws.md](/references/mlflow-prompt-optimization-beta-databricks-on-aws-9e2888f4.md)
