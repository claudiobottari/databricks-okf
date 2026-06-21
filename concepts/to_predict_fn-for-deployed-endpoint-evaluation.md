---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a5a71d260ece7a59590d5f51ef91404afb02e02239742aece2ec2959369c005c
  pageDirectory: concepts
  sources:
    - mlflow-evaluation-examples-for-genai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - to_predict_fn-for-deployed-endpoint-evaluation
    - TFDEE
  citations:
    - file: mlflow-evaluation-examples-for-genai-databricks-on-aws.md
title: to_predict_fn for Deployed Endpoint Evaluation
description: Using mlflow.genai.to_predict_fn() to evaluate deployed Model Serving chat endpoints, Custom Agents, and custom endpoints.
tags:
  - mlflow
  - endpoints
  - deployment
  - evaluation
timestamp: "2026-06-19T19:38:21.850Z"
---

# to_predict_fn for Deployed Endpoint Evaluation

**`to_predict_fn`** is a utility function in the MLflow GenAI evaluation API that creates a compatible predict function for evaluating deployed endpoints, including Custom Agents, Model Serving chat endpoints, and custom endpoints. It automatically extracts traces from tracing-enabled endpoints for full observability during evaluation. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Overview

When using `mlflow.genai.evaluate()` to assess a deployed endpoint, the `predict_fn` parameter must be a callable that accepts named parameters matching the keys in your evaluation dataset. The `to_predict_fn` function bridges this gap by generating a predict function that is compatible with deployed endpoints, performing a `kwargs` pass-through directly to the endpoint. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Input Format Requirements

The `to_predict_fn` function performs a direct `kwargs` pass-through to your endpoint. This means your evaluation data must match the input format that your endpoint expects. If the formats do not match, the evaluation fails with an error message about unrecognized input keys. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

### Model Serving Chat Endpoints

For Model Serving chat endpoints, the data must be formatted with the `messages` key:

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery

# Create predict function for a chat endpoint
predict_fn = mlflow.genai.to_predict_fn("endpoints:/my-chatbot-endpoint")

# Evaluate the chat endpoint
results = mlflow.genai.evaluate(
    data=[{"inputs": {"messages": [{"role": "user", "content": "How does MLflow work?"}]}}],
    predict_fn=predict_fn,
    scorers=[RelevanceToQuery()],
)
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

### Custom Agents and Custom Endpoints

For Custom Agents and custom endpoints, the input format depends on the specific endpoint's expected schema. The `to_predict_fn` function passes the input data through as keyword arguments, so the evaluation dataset keys must correspond to the endpoint's expected parameter names. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Usage Pattern

The typical workflow for evaluating a deployed endpoint with `to_predict_fn` is:

1. Create a predict function using `mlflow.genai.to_predict_fn()` with the endpoint URI.
2. Prepare evaluation data that matches the endpoint's expected input format.
3. Call `mlflow.genai.evaluate()` with the predict function and evaluation data.
4. Optionally include [MLflow GenAI Scorers](/concepts/mlflow-genai-scorers.md) to assess response quality.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The overall evaluation framework for GenAI applications.
- [MLflow GenAI Scorers](/concepts/mlflow-genai-scorers.md) — Built-in and custom scoring functions for evaluating model outputs.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — The deployment infrastructure for serving models as endpoints.
- Custom Agents — Deployable agent applications that can be evaluated with this function.
- [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) — Versioned datasets for production-ready evaluation.
- predict_fn Patterns in MLflow Evaluation|predict_fn Patterns — Common patterns for providing prediction functions to the evaluation harness.

## Sources

- mlflow-evaluation-examples-for-genai-databricks-on-aws.md

# Citations

1. [mlflow-evaluation-examples-for-genai-databricks-on-aws.md](/references/mlflow-evaluation-examples-for-genai-databricks-on-aws-2da85b83.md)
