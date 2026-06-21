---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 709279aecf3a4b9f44dbc2e820532ef00c3d4b84be354dd037eeb80792d3da75
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-enablement-via-autolog
    - MTEVA
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: MLflow Tracing Enablement via Autolog
description: A mechanism to enable or disable tracing for generative AI framework integrations (OpenAI, LangChain, LlamaIndex, AutoGen) using autolog functions.
tags:
  - mlflow
  - tracing
  - generative-ai
  - llm
timestamp: "2026-06-19T18:08:14.793Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Enablement via Autolog

**MLflow Tracing Enablement via Autolog** refers to the mechanism by which [MLflow Tracing](/concepts/mlflow-tracing.md) is controlled through the `autolog` functionality within supported [MLflow](/concepts/mlflow.md) framework integrations. Tracing captures detailed execution traces of generative AI (genAI) workloads, and the autolog APIs provide a programmatic way to enable or disable this tracing support. ^[databricks-autologging-databricks-on-aws.md]

## How It Works

[MLflow Tracing](/concepts/mlflow-tracing.md) leverages the existing `autolog` feature in each framework integration to toggle tracing on or off. Users call the framework‑specific `autolog()` function with a `log_traces` parameter to control whether traces are recorded during model execution. ^[databricks-autologging-databricks-on-aws.md]

For example, to enable tracing when using a LlamaIndex model, call `mlflow.llama_index.autolog(log_traces=True)`: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow

mlflow.llama_index.autolog(log_traces=True)
```

## Serverless Compute Consideration

On serverless compute clusters, tracing autologging is **not** automatically enabled. Users must explicitly enable autologging for each specific framework integration they want to trace — for example, by calling `mlflow.openai.autolog()` or `mlflow.langchain.autolog()`. ^[databricks-autologging-databricks-on-aws.md]

## Supported Integrations

The following framework integrations support trace enablement through their autolog implementations: ^[databricks-autologging-databricks-on-aws.md]

- OpenAI — via `mlflow.openai.autolog()`
- LangChain — via `mlflow.langchain.autolog()`
- LangGraph — via `mlflow.langchain.autolog()`
- LlamaIndex — via `mlflow.llama_index.autolog()`
- [AutoGen](/concepts/autogen-auto-tracing.md) — via `mlflow.autogen.autolog()`

## Relation to Databricks Autologging

Databricks Autologging automatically calls `mlflow.autolog()` when a notebook is attached to an interactive cluster. However, for genAI tracing, it is important to understand that Databricks Autologging and [MLflow Tracing](/concepts/mlflow-tracing.md) autolog are separate features. While Databricks Autologging handles automatic tracking for traditional ML workflows (like scikit-learn, TensorFlow, etc.), tracing for genAI workflows requires explicit framework‑specific autolog calls — especially on serverless compute. ^[databricks-autologging-databricks-on-aws.md]

## Best Practices

- **Always explicitly enable tracing autolog on serverless compute.** Default autologging is not applied on serverless clusters. ^[databricks-autologging-databricks-on-aws.md]
- **Call the framework‑specific autolog function** rather than relying on the generic `mlflow.autolog()` for tracing purposes. ^[databricks-autologging-databricks-on-aws.md]
- **Verify tracing is working** by checking the [MLflow Tracking UI](/concepts/mlflow-tracking.md) for trace data after running a genAI workload.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The system that captures and stores execution traces for genAI models.
- [Databricks Autologging](/concepts/databricks-autologging.md) — Automatic MLflow tracking for traditional ML frameworks.
- [MLflow Experiment Permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md) — Controls that secure trace data stored in MLflow Tracking.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Where traced models can be logged for lifecycle management.
- [OpenAI Autologging](/concepts/mlflow-openai-autologging.md) — Specific autolog implementation for OpenAI models.

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
