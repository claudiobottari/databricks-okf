---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2748583fd99651fec129b637a1a7d732671d6917f192e2461a81604d61f1af7c
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-llms-with-mlflow
    - DLWM
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Databricks-hosted LLMs with MLflow
description: Integration of Databricks-hosted foundation models (via the databricks-openai package) with MLflow Tracing and Evaluation for GenAI applications.
tags:
  - databricks
  - llm
  - mlflow
  - integration
timestamp: "2026-06-19T15:11:55.024Z"
---

# Databricks-hosted LLMs with MLflow

**Databricks-hosted LLMs with MLflow** refers to the integration between MLflow and Databricks-managed large language models (LLMs) accessed via the OpenAI-compatible API. This setup allows developers to instrument, trace, and evaluate applications that use foundation models hosted on the Databricks platform.

## Overview

When building AI applications that call Databricks-hosted LLMs, MLflow provides automatic instrumentation and tracing capabilities. The `mlflow.openai.autolog()` function automatically tracks all calls made through an OpenAI-compatible client, recording inputs, outputs, and metadata for each LLM interaction. ^[develop-code-based-scorers-databricks-on-aws.md]

## Setup and Configuration

### Prerequisites

To use Databricks-hosted LLMs with MLflow, install the required packages:

```
%pip install -q --upgrade "mlflow[databricks]>=3.1" openai
```

The `databricks-openai` package provides a client that connects to Databricks-hosted foundation models. ^[develop-code-based-scorers-databricks-on-aws.md]

### Connecting to Databricks LLMs

Use the `DatabricksOpenAI` class to create a client that routes requests to Databricks-hosted models:

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()
```

Select a model from the [available foundation models](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models) on Databricks. ^[develop-code-based-scorers-databricks-on-aws.md]

### Enabling Automatic Tracing

Enable [MLflow Tracing](/concepts/mlflow-tracing.md) with a single call:

```python
import mlflow
mlflow.openai.autolog()
```

If running outside of Databricks, set the tracking URI to a Databricks workspace:

```python
mlflow.set_tracking_uri("databricks")
```

In Databricks notebooks, the experiment defaults to the notebook experiment automatically. ^[develop-code-based-scorers-databricks-on-aws.md]

## Building Applications with Databricks LLMs

A typical application wraps LLM calls in traced functions. The `@mlflow.trace` decorator adds the function's inputs and outputs to the MLflow trace:

```python
@mlflow.trace
def sample_app(messages: list[dict[str, str]]):
    messages_for_llm = [
        {"role": "system", "content": "You are a helpful assistant."},
        *messages,
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages_for_llm,
    )
    return response.choices[0].message.content
```

The trace captures the entire conversation, including system prompts, user messages, and the LLM's response. ^[develop-code-based-scorers-databricks-on-aws.md]

## Evaluation Workflows

### Generating Evaluation Traces

Use `mlflow.genai.evaluate()` to generate traces from a Databricks LLM application. The evaluation produces one trace per row in the dataset and stores it in the MLflow experiment:

```python
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric]
)
```

Generated traces are visible in the Databricks notebook Trace UI and in the MLflow Experiment UI under the **Response** column. ^[develop-code-based-scorers-databricks-on-aws.md]

### Iterating on Scorers Without Re-running the App

A key advantage of using MLflow with Databricks-hosted LLMs is the ability to iterate on custom scorers without re-calling the LLM. After generating traces, store them as a Pandas DataFrame:

```python
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)
```

Then evaluate new scorers against these precomputed traces:

```python
mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length]
)
```

This workflow saves both time and cost by avoiding repeated LLM API calls during metric development. ^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying instrumentation framework for recording LLM interactions
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation metrics that analyze LLM outputs
- MLflow Evaluation for GenAI — The broader evaluation framework for AI agents and applications
- [Foundation Model APIs on Databricks](/concepts/foundation-models-apis-on-databricks.md) — The Databricks-managed LLM endpoints accessed via OpenAI-compatible API
- Production Monitoring with MLflow — Deploying scorers for continuous monitoring of deployed applications

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
