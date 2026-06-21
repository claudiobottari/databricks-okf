---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef4ec33afdfb0f9c904d530929b19f289ab4ec3885d4311c500bd970ae81fa9b
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-based-scorers-for-mlflow-genai
    - CSFMG
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Code-based Scorers for MLflow GenAI
description: Custom evaluation metrics defined as Python functions using the @scorer decorator pattern for evaluating GenAI applications in MLflow.
tags:
  - MLflow
  - evaluation
  - scorers
  - GenAI
timestamp: "2026-06-19T18:31:45.707Z"
---

# Code-based Scorers for MLflow GenAI

**Code-based Scorers for MLflow GenAI** are custom evaluation functions that allow you to define flexible, programmatic metrics for assessing the performance of AI agents and applications built with MLflow. Unlike built-in metrics, code-based scorers (also called "custom scorers") give you full control over the evaluation logic, making them suitable for application-specific quality checks that go beyond simple LLM-as-a-judge assessments. ^[develop-code-based-scorers-databricks-on-aws.md]

## Overview

A code-based scorer is a Python function decorated with the `@scorer` decorator from `mlflow.genai.scorers`. The decorator marks the function as an evaluable metric that can be passed to `mlflow.genai.evaluate()` alongside an evaluation dataset. The scorer function receives either the raw input/output data or the stored traces from a previous run, and returns a scalar value (typically an integer or float) that represents the metric score for that row. ^[develop-code-based-scorers-databricks-on-aws.md]

Code-based scorers are particularly useful when:

- You need to compute a metric that is not covered by the built-in MLflow evaluation metrics.
- You want to measure a specific attribute of the response, such as length, safety, or factual consistency.
- You are iterating on a custom metric and do not want to re-run the entire application each time.

## Developer Workflow

The recommended workflow for developing code-based scorers involves four steps: ^[develop-code-based-scorers-databricks-on-aws.md]

1. **Define evaluation data** – Prepare a list of input requests (e.g., user messages) that your AI application should handle.
2. **Generate traces from your app** – Run `mlflow.genai.evaluate()` with a placeholder scorer to produce traces. Each trace corresponds to one row of the evaluation dataset.
3. **Query and store the resulting traces** – Use `mlflow.search_traces()` to retrieve the generated traces as a Pandas DataFrame. This DataFrame becomes the reusable input for subsequent scorer iterations.
4. **As you iterate on your scorer, call `evaluate()` using the stored traces** – Pass the stored traces DataFrame directly to `evaluate()` as the `data` parameter. Because the traces already contain the model outputs, you can omit the `predict_fn` argument. This allows you to update your metric without re-running the entire application.

This workflow is designed for rapid iteration. Once traces are generated, you can redefine the scorer function and re-evaluate it against the same traces without waiting for the LLM to respond again. ^[develop-code-based-scorers-databricks-on-aws.md]

## Example

```python
from mlflow.genai.scorers import scorer

@scorer
def response_length(outputs: str) -> int:
    # Example metric: measure the length of the response.
    return len(outputs)
```

When calling `evaluate()` with a stored traces DataFrame, the scorer function receives the `outputs` field from each trace row. The `evaluate()` call then computes the metric for every row and returns the results. ^[develop-code-based-scorers-databricks-on-aws.md]

## Prerequisites

To use code-based scorers, you must have `mlflow[databricks]` version 3.1 or later installed, and the `openai` client package if your application uses an OpenAI-compatible endpoint. Databricks recommends using the `databricks-openai` package to connect to Databricks-hosted LLMs when running inside a Databricks workspace. ^[develop-code-based-scorers-databricks-on-aws.md]

## Related concepts

- [Custom LLM scorers](/concepts/custom-judge-scorers.md) – A simpler, LLM-as-a-judge approach for semantic evaluation.
- [Production Monitoring](/concepts/production-monitoring.md) – Deploying scorers for continuous, scheduled evaluation.
- Build evaluation datasets – Guidelines for creating test data that scorers will process.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The infrastructure that records and stores traces for later evaluation.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
