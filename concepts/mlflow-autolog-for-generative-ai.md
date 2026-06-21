---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0da4bb4bd9db9150ee7b0965dd1c38790dc489dd3281ed733cc659e9f50cfb1
  pageDirectory: concepts
  sources:
    - tracing-txtai-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-autolog-for-generative-ai
    - MAFGA
  citations:
    - file: tracing-txtai-databricks-on-aws.md
title: MLflow autolog for generative AI
description: The mechanism in MLflow that automatically captures traces for supported GenAI frameworks (including txtai) when the autolog function is called
tags:
  - mlflow
  - autolog
  - tracing
  - genai
timestamp: "2026-06-19T23:13:41.998Z"
---

# [MLflow](/concepts/mlflow.md) autolog for generative AI

**MLflow autolog for generative AI** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that automatically captures [Traces](/concepts/traces.md) from supported generative AI frameworks without requiring manual instrumentation. By calling `mlflow.autolog()` or a framework-specific `autolog()` function, [MLflow](/concepts/mlflow.md) records [trace data](/concepts/tracedata.md) for LLM invocations, embeddings, AI search operations, and agent workflows, logging them to the active [MLflow Experiment](/concepts/mlflow-experiment.md).

## Overview

[MLflow](/concepts/mlflow.md) autolog for generative AI works by patching the framework's core functions so that every call is automatically wrapped in a trace span. When autolog is enabled, each LLM request, embedding computation, search query, and tool invocation is recorded along with its inputs, outputs, latency, and other metadata. This trace data is then stored in the [MLflow Experiment](/concepts/mlflow-experiment.md) and can be viewed in the Trace UI for debugging and observability. ^[tracing-txtai-databricks-on-aws.md]

## Supported Frameworks

Autolog for generative AI is available for several frameworks through dedicated [MLflow](/concepts/mlflow.md) extension packages. Each framework has its own `autolog()` function that enables tracing for that specific library's operations.

For [txtai](/concepts/txtai.md), autolog is enabled by calling `mlflow.[txtai](/concepts/txtai.md).autolog()`. This captures [Traces](/concepts/traces.md) for LLM invocation, embeddings, AI Search, Textractor pipelines, RAG pipelines, and agent workflows. ^[tracing-txtai-databricks-on-aws.md]

To use [txtai](/concepts/txtai.md) tracing, you need to install `mlflow-txtai` alongside `txtai` and [MLflow](/concepts/mlflow.md):

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" [[txtai|txtai]] mlflow-txtai
```

[MLflow 3](/concepts/mlflow-3.md) is recommended for the best tracing experience with [txtai](/concepts/txtai.md). ^[tracing-txtai-databricks-on-aws.md]

## Enabling Autolog

The general pattern for enabling autologging depends on the framework and the execution environment.

**General Python environment**: Call the framework-specific `autolog()` function before creating any pipeline or agent objects:

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].[[txtai|txtai]].autolog()
```

After autolog is enabled, subsequent calls to the framework's tracing-supported operations are automatically captured. ^[tracing-txtai-databricks-on-aws.md]

**Serverless compute clusters**: On Databricks serverless compute, autologging for generative AI tracing frameworks is **not automatically enabled**. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[tracing-txtai-databricks-on-aws.md]

## Configuration

After enabling autolog, you must configure [MLflow](/concepts/mlflow.md) to send [Traces](/concepts/traces.md) to a tracking destination. For Databricks, set the tracking URI and experiment:

```python
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/my-experiment")
```

In Databricks notebooks, these credentials are automatically configured. For environments outside Databricks notebooks, you must set the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. ^[tracing-txtai-databricks-on-aws.md]

## Traced Operations

The specific operations captured by autolog vary by framework. For [txtai](/concepts/txtai.md), autolog automatically [Traces](/concepts/traces.md):

- **Textractor pipelines**: Text extraction and processing operations
- **RAG pipelines**: Retrieval Augmented Generation flows combining embeddings search with LLM generation
- **Agent workflows**: Multi-step agents using tools, with each iteration and tool call recorded separately
- **Embeddings operations**: Semantic search and AI Search queries

Each trace captures the full call chain, including the input prompts, retrieved context, generated responses, and intermediate steps. ^[tracing-txtai-databricks-on-aws.md]

## Viewing [Traces](/concepts/traces.md)

Once autolog is enabled and [Traces](/concepts/traces.md) are captured, they appear in the [MLflow Experiment](/concepts/mlflow-experiment.md) under the active run. The Trace UI provides a visual representation of the trace, showing each span, its duration, inputs, outputs, and parent-child relationships. This enables debugging and observability of RAG workflows and agent workflows without manual instrumentation. ^[tracing-txtai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying tracing system that autolog uses
- [Trace data](/concepts/tracedata.md) — The structured records of LLM and AI operations
- Trace UI — The interface for inspecting captured [Traces](/concepts/traces.md)
- [txtai](/concepts/txtai.md) — A supported framework for embeddings and LLM orchestration
- RAG pipelines — Retrieval Augmented Generation workflows traced by autolog
- Agent workflows — Multi-step agent [Traces](/concepts/traces.md) captured by autolog
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The organizational unit for runs and [Traces](/concepts/traces.md)

## Sources

- tracing-txtai-databricks-on-aws.md

# Citations

1. [tracing-txtai-databricks-on-aws.md](/references/tracing-txtai-databricks-on-aws-a07dafba.md)
