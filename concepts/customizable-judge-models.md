---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 566ed3ddba4ac26e4b8ed307b309a4930a7b9531b454950fda0828b1862317de
  pageDirectory: concepts
  sources:
    - safety-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customizable-judge-models
    - CJM
  citations:
    - file: safety-judge-databricks-on-aws.md
title: Customizable Judge Models
description: The ability to change which LLM powers a built-in judge by specifying a model in '<provider>:/<model-name>' format, compatible with LiteLLM providers including Databricks serving endpoints.
tags:
  - llm-evaluation
  - configuration
  - mlflow
timestamp: "2026-06-19T20:17:50.658Z"
---

# Customizable Judge Models

**Customizable Judge Models** refers to the ability to replace the default LLM that powers built-in MLflow judges with a different model of your choice. This allows you to tailor evaluation criteria, performance characteristics, or cost profile to your specific use case.

## Overview

Built-in judges in MLflow, such as the [Safety Judge](/concepts/safety-judge-mlflow.md), use a Databricks-hosted LLM by default to perform GenAI quality assessments. However, you can customize which model powers a judge by specifying the `model` argument when creating the judge instance. ^[safety-judge-databricks-on-aws.md]

## Model Specification Format

When customizing a judge model, the model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name corresponds to the serving endpoint name. ^[safety-judge-databricks-on-aws.md]

## Usage Example

The following example demonstrates customizing the Safety judge to use a different model:

```python
from mlflow.genai.scorers import Safety

# Use a different model for safety evaluation
safety_judge = Safety(
    model="databricks:/databricks-claude-opus-4-5"  # Use a different model
)

# Run evaluation with Safety judge
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[safety_judge]
)
```

^[safety-judge-databricks-on-aws.md]

## Supported Judge Types

Customizable judge models are available for all built-in judges, including:

- [Safety Judge](/concepts/safety-judge-mlflow.md) — Evaluates text content for harmful, offensive, or inappropriate material
- [Guidelines Judge](/concepts/guidelines-llm-judge.md) — Allows creation of custom safety criteria
- Other built-in judges for relevance, groundedness, and correctness assessments

## Considerations

When selecting a custom judge model, consider the following:

- **Provider compatibility**: The model provider must be LiteLLM-compatible
- **Endpoint naming**: For Databricks-hosted models, use the serving endpoint name as the model name
- **Performance characteristics**: Different models may have varying accuracy, latency, and cost profiles for evaluation tasks

## Related Concepts

- [Safety Judge](/concepts/safety-judge-mlflow.md) — The built-in judge for content safety evaluation
- [Guidelines Judge](/concepts/guidelines-llm-judge.md) — A judge for custom safety criteria
- MLflow Evaluation Framework — The framework for running batch evaluations with judges
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — The paradigm of using LLMs for evaluation

## Sources

- safety-judge-databricks-on-aws.md

# Citations

1. [safety-judge-databricks-on-aws.md](/references/safety-judge-databricks-on-aws-d841b2a4.md)
