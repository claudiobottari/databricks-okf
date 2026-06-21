---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 63f16da35f015379caf2f41848aee91f74a02d945d16532e6b5f0759d3acc793
  pageDirectory: concepts
  sources:
    - tracing-crewai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genai-tracing-autolog-on-serverless-clusters
    - GTAOSC
  citations:
    - file: tracing-crewai-databricks-on-aws.md
title: GenAI Tracing Autolog on Serverless Clusters
description: On Databricks serverless compute clusters, genAI tracing autologging must be explicitly enabled per integration
tags:
  - databricks
  - serverless
  - autolog
  - tracing
timestamp: "2026-06-19T23:10:36.520Z"
---

## GenAI Tracing Autolog on Serverless Clusters

**GenAI Tracing Autolog on Serverless Clusters** refers to the behavior of [MLflow Tracing](/concepts/mlflow-tracing.md) for generative AI (GenAI) frameworks when running on Databricks Serverless Compute clusters. [MLflow](/concepts/mlflow.md) provides automatic trace capture for frameworks like CrewAI, LangChain, LlamaIndex, and others through integration‑specific `autolog()` functions. On serverless clusters, however, this autologging is **not enabled by default**; users must explicitly call the appropriate `mlflow.<library>.autolog()` function to start tracing. ^[tracing-crewai-databricks-on-aws.md]

### Behavior on Serverless Clusters

The key difference between classic compute and serverless clusters is the default autologging policy:

- On **non‑serverless** (classic) Databricks compute, GenAI tracing autolog is automatically enabled for supported frameworks when [MLflow](/concepts/mlflow.md) is imported.
- On **serverless** clusters, autologging is not automatically turned on. You must explicitly call `mlflow.crewai.autolog()` (or the corresponding function for your framework) to start tracing. ^[tracing-crewai-databricks-on-aws.md]

This applies to all GenAI tracing integrations that use MLflow’s autolog mechanism. The explicit call ensures that [Traces](/concepts/traces.md) are captured for all subsequent operations of the framework (LLM calls, tool usage, agent steps, etc.) and logged to the active [MLflow Experiment](/concepts/mlflow-experiment.md).

### Prerequisites

To use GenAI Tracing Autolog on a serverless cluster, install [MLflow](/concepts/mlflow.md) with the Databricks extras and the desired GenAI library (e.g., `crewai`, `langchain`, `llama-index`). For example, for CrewAI:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" crewai
```

If running outside a Databricks notebook (e.g., local development), set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN`. Inside a Databricks notebook these are automatically set. Ensure any LLM provider API keys (e.g., `OPENAI_API_KEY`) are configured. ^[tracing-crewai-databricks-on-aws.md]

### Enabling Autolog

Call the framework‑specific `autolog()` function before instantiating any agents, tasks, or chains. For CrewAI:

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].crewai.autolog()
```

Optionally set an experiment to organise [Traces](/concepts/traces.md):

```python
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/my-experiment")
```

After enabling autolog, every operation within the framework (task execution, LLM calls, memory reads/writes, exceptions) is automatically traced and nested into a single trace. ^[tracing-crewai-databricks-on-aws.md]

### Disabling Autolog

To disable autolog globally for a specific framework:

```python
[[mlflow|MLflow]].crewai.autolog(disable=True)
```

Or disable all [MLflow Autologging](/concepts/mlflow-autologging.md):

```python
[[mlflow|MLflow]].autolog(disable=True)
```

Disabling stops the capture of new [Traces](/concepts/traces.md) but does not clear already‑logged [Traces](/concepts/traces.md). ^[tracing-crewai-databricks-on-aws.md]

### Supported Integrations

Autolog is supported for several GenAI frameworks. The list includes (but is not limited to):

- CrewAI – synchronous task execution only (async not yet supported)
- LangChain
- LlamaIndex
- [Autogen](/concepts/autogen-auto-tracing.md)

Each integration requires its own `autolog()` call (e.g., `mlflow.langchain.autolog()`).

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying trace capture system.
- Databricks Serverless Compute – The compute infrastructure where autolog is not automatically enabled.
- CrewAI – A multi‑agent framework supported by GenAI Tracing.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – Destination for logged [Traces](/concepts/traces.md).
- [Autolog](/concepts/mlflow-autologging.md) – General [MLflow](/concepts/mlflow.md) mechanism for automatic logging.

### Sources

- tracing-crewai-databricks-on-aws.md

# Citations

1. [tracing-crewai-databricks-on-aws.md](/references/tracing-crewai-databricks-on-aws-c9f44377.md)
