---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4a8e6e02bbf098d4cb565308fd221cf71fa48d5b46dbe35dd6d4ed6ccfa30b68
  pageDirectory: concepts
  sources:
    - tracing-crewai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-genai-on-databricks
    - MTFGOD
  citations:
    - file: tracing-crewai-databricks-on-aws.md
title: MLflow Tracing for GenAI on Databricks
description: Databricks MLflow 3 provides automatic tracing for GenAI frameworks including CrewAI, LangChain, and others
tags:
  - databricks
  - mlflow
  - tracing
  - genai
timestamp: "2026-06-19T23:10:26.807Z"
---

# [MLflow Tracing for GenAI](/concepts/mlflow-tracing-for-genai.md) on Databricks

**MLflow Tracing for GenAI on Databricks** is a feature of [MLflow](/concepts/mlflow.md) that provides [Automatic Tracing](/concepts/automatic-tracing.md) capability for [GenAI](/concepts/mlflow-genai-evaluate-api.md) frameworks. By calling the appropriate `autolog` function, [MLflow](/concepts/mlflow.md) captures nested [Traces](/concepts/traces.md) of workflow execution and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). This enables observability of multi-agent applications and large language model (LLM) interactions directly within the Databricks platform. ^[tracing-crewai-databricks-on-aws.md]

## How It Works – Auto‑Tracing

[MLflow Tracing](/concepts/mlflow-tracing.md) relies on an explicit `autolog()` call for the specific [GenAI](/concepts/mlflow-genai-evaluate-api.md) framework being used. For example, to trace a CrewAI workflow, call `mlflow.crewai.autolog()`. Once enabled, every subsequent run of the framework’s operations (such as task execution, agent calls, and LLM invocations) is automatically instrumented and the resulting [Traces](/concepts/traces.md) are sent to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-crewai-databricks-on-aws.md]

On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is **not** enabled by default. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for the integrations you want to trace. ^[tracing-crewai-databricks-on-aws.md]

## Captured Information

For a framework like CrewAI, [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) automatically capture the following details:

- Tasks and the Agent that executes each task  
- Every LLM call, including input prompts, completion responses, and associated metadata  
- Memory load and write operations  
- Latency of each operation  
- Any exceptions raised during execution  

Currently, only synchronous task execution is supported; asynchronous task kickoffs are not traced. ^[tracing-crewai-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with a GenAI framework on Databricks, you must install the required packages:

- **Development:** `pip install "[MLflow](/concepts/mlflow.md)[databricks]>=3.1" <framework_package>` (e.g., `crewai`). [MLflow 3](/concepts/mlflow-3.md) is recommended for the best tracing experience.  
- **Credentials:** Inside a Databricks notebook, credentials are automatically configured. Outside Databricks, set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables.  
- **API Keys:** Ensure that any required LLM provider API keys (e.g., `OPENAI_API_KEY`) are set. For production, use [AI Gateway](/concepts/ai-gateway.md) or Databricks Secrets instead of hardcoded values. ^[tracing-crewai-databricks-on-aws.md]

## Example Usage (CrewAI)

The following pattern enables tracing for a CrewAI workflow:

```python
import [[mlflow|MLflow]]

# Enable auto‑tracing
[[mlflow|MLflow]].crewai.autolog()

# Set tracking URI and experiment
[[mlflow|MLflow]].set_tracing_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/crewai-demo")
```

After defining agents, tasks, and a crew, calling `crew.kickoff()` will produce nested [Traces](/concepts/traces.md) that appear in the Databricks experiment UI. ^[tracing-crewai-databricks-on-aws.md]

## Disabling Auto‑Tracing

To disable auto‑tracing for a specific framework, call:

```python
[[mlflow|MLflow]].crewai.autolog(disable=True)
```

To disable all [MLflow Autologging](/concepts/mlflow-autologging.md), use `mlflow.autolog(disable=True)`. ^[tracing-crewai-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md) – The destination for [Traces](/concepts/traces.md) and run metadata.  
- [Autologging](/concepts/mlflow-autologging.md) – Mechanism that automatically instruments framework operations.  
- Serverless Compute – Compute environment where autologging must be explicitly enabled.  
- CrewAI – An example GenAI framework supported by [MLflow Tracing](/concepts/mlflow-tracing.md).  
- LLM – Large language models whose calls are traced.  
- Databricks Secrets – Secure storage for API keys used in production.

## Sources

- tracing-crewai-databricks-on-aws.md

# Citations

1. [tracing-crewai-databricks-on-aws.md](/references/tracing-crewai-databricks-on-aws-c9f44377.md)
