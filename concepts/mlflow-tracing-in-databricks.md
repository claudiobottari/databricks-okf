---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ebc4d8e7a0cb933b1986b7c743e32beb85ffe85bfe5afec0389fab762b1606d6
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-in-databricks
    - MTID
    - MLflow Tracking on Databricks
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: MLflow Tracing in Databricks
description: An autolog-based tracing feature for generative AI workloads that enables trace logging for LLM frameworks such as OpenAI, LangChain, LangGraph, LlamaIndex, and AutoGen.
tags:
  - generative-ai
  - mlflow
  - tracing
  - llm
timestamp: "2026-06-18T15:02:04.475Z"
---

---

title: [MLflow Tracing](/concepts/mlflow-tracing.md) in Databricks
summary: [MLflow Tracing](/concepts/mlflow-tracing.md) automatically captures trace data for generative AI workloads on Databricks via autologging integrations with frameworks like OpenAI, LangChain, LlamaIndex, and more.
sources:
  - databricks-autologging-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:26:53.977Z"
updatedAt: "2026-06-18T12:26:53.977Z"
tags:
  - mlflow
  - tracing
  - observability
  - genai
aliases:
  - mlflow-tracing-in-databricks
  - MTID
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0

---

# [MLflow Tracing](/concepts/mlflow-tracing.md) in Databricks

**MLflow Tracing in Databricks** refers to the automatic capture of trace data for generative AI workloads using the [MLflow Autologging](/concepts/mlflow-autologging.md) system. It enables observability for large language model (LLM) calls, agent steps, and other AI model invocations by recording detailed execution traces as part of MLflow tracking runs. ^[databricks-autologging-databricks-on-aws.md]

## How it works

[MLflow Tracing](/concepts/mlflow-tracing.md) leverages the autolog feature of specific model framework integrations to control whether tracing is enabled or disabled for that integration. When you call the appropriate autolog function with tracing enabled, each subsequent model invocation (e.g., an OpenAI chat completion or a LangChain chain execution) is automatically traced, recording inputs, outputs, and timing information. ^[databricks-autologging-databricks-on-aws.md]

## Enabling tracing

To enable tracing for a supported framework, use the corresponding autolog function with `log_traces=True`. For example, for a LlamaIndex model:

```python
import mlflow
mlflow.llama_index.autolog(log_traces=True)
```

The following integrations support trace enablement through their autolog implementations:

- OpenAI (`mlflow.openai.autolog()`)
- LangChain and LangGraph (`mlflow.langchain.autolog()`)
- LlamaIndex (`mlflow.llama_index.autolog()`)
- [AutoGen](/concepts/autogen-auto-tracing.md) (`mlflow.autogen.autolog()`)

^[databricks-autologging-databricks-on-aws.md]

## Serverless compute considerations

For serverless compute clusters, autologging for tracing is **not** automatically enabled. You must explicitly call the autolog function for each framework integration you wish to trace (for example, `mlflow.openai.autolog()` or `mlflow.langchain.autolog()`). ^[databricks-autologging-databricks-on-aws.md]

## Supported frameworks

The supported integrations that have trace enablement within their autolog implementations are:

- OpenAI
- LangChain
- LangGraph
- LlamaIndex
- AutoGen

^[databricks-autologging-databricks-on-aws.md]

## Relationship to Databricks Autologging

The general [Databricks Autologging](/concepts/databricks-autologging.md) feature automatically captures model parameters, metrics, files, and lineage information when you train models from popular machine learning libraries. [MLflow Tracing](/concepts/mlflow-tracing.md) extends this capability to generative AI workloads by adding trace logging, which is not automatically enabled for all frameworks. While Databricks Autologging calls `mlflow.autolog()` by default on interactive Python notebook clusters, [MLflow Tracing](/concepts/mlflow-tracing.md) requires explicit framework-specific autolog invocation for most integrations. ^[databricks-autologging-databricks-on-aws.md]

## Related concepts

- [MLflow Autologging](/concepts/mlflow-autologging.md) — The underlying automatic logging system used to enable tracing.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The storage and UI layer where traces are recorded.
- [Generative AI on Databricks](/concepts/ai-runtime-ai-v5-on-databricks.md) — Overview of GenAI workloads that benefit from tracing.
- [OpenAI Autologging](/concepts/mlflow-openai-autolog.md) — Details on tracing for OpenAI models.
- LangChain Autologging — Tracing for LangChain and LangGraph workflows.

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
