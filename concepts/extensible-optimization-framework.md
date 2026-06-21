---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8b852f4d67d325736b09366f0eef85cb47c607a87072eae98e3774c49358d2c
  pageDirectory: concepts
  sources:
    - mlflow-prompt-optimization-beta-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - extensible-optimization-framework
    - EOF
  citations:
    - file: mlflow-prompt-optimization-beta-databricks-on-aws.md
title: Extensible Optimization Framework
description: MLflow's prompt optimization framework allows plugging in custom optimization algorithms by extending the base class, making it framework-agnostic and compatible with any agent system.
tags:
  - mlflow
  - extensibility
  - framework
timestamp: "2026-06-19T19:40:15.076Z"
---

# Extensible Optimization Framework

The **Extensible Optimization Framework** is a component of [MLflow](/concepts/mlflow.md)'s prompt optimization system that allows users to automatically improve prompts using evaluation metrics and training data. It is currently in Beta. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

The framework provides the [`mlflow.genai.optimize_prompts()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.optimize_prompt) API, which takes a prediction function, training data, prompt URIs, an optimizer, and one or more scorers, and returns an optimized prompt. It is designed to be framework‑agnostic, working with any agent framework. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Key Features

- **Automatic Improvement** – Optimizes prompts based on evaluation metrics without manual tuning. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Data‑Driven Optimization** – Uses training data and custom scorers to guide the optimization process. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Framework Agnostic** – Works with any agent framework, providing broad compatibility. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Joint Optimization** – Enables simultaneous refinement of multiple prompts for best overall performance. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Flexible Evaluation** – Supports custom scorers and aggregation functions. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Version Control** – Automatically registers optimized prompts in the [MLflow Prompt Registry](/concepts/prompt-registry.md). ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]
- **Extensible** – Users can plug in custom optimization algorithms by extending a base class. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Extending with Custom Optimizers

The framework includes a built‑in optimizer, [GEPA](/concepts/gepa-gradient-free-evolutionary-prompt-algorithm.md) ([GepaPromptOptimizer](/concepts/gepapromptoptimizer.md)), researched and validated by the Databricks AI Research Team. GEPA iteratively refines prompts using LLM‑driven reflection and automated feedback. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

To add a custom optimization algorithm, users create a subclass of the base optimizer class provided by the framework. The custom optimizer can then be passed to the `optimizer` parameter of `mlflow.genai.optimize_prompts()`. This design allows teams to implement proprietary or domain‑specific optimization strategies while leveraging the rest of the framework’s infrastructure (data loading, scoring, versioning). ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

### Example Usage

```python
import mlflow
from mlflow.genai.optimize import [[gepapromptoptimizer|GepaPromptOptimizer]]

result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gpt-5"),
    scorers=[Correctness(model="databricks:/databricks-claude-sonnet-4-5")],
)
```

For custom optimizers, the framework expects the same interface as the base class. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Version Requirements

The `optimize_prompts` API requires **MLflow >= 3.5.0**. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Related Concepts

- Prompt Optimization – Overview of automated prompt improvement.
- [GEPA](/concepts/gepa-gradient-free-evolutionary-prompt-algorithm.md) – The built‑in optimization algorithm.
- [MLflow Prompt Registry](/concepts/prompt-registry.md) – Version‑control system for prompts.
- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) – Extensible scoring functions used in optimization.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Tracing support for GenAI applications.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Evaluation workflow for agents.

## Sources

- mlflow-prompt-optimization-beta-databricks-on-aws.md

# Citations

1. [mlflow-prompt-optimization-beta-databricks-on-aws.md](/references/mlflow-prompt-optimization-beta-databricks-on-aws-9e2888f4.md)
