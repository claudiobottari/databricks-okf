---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac4a4bb3cff8052941dc906af599c115eb572b359162ab2478ecaeefa0c1017e
  pageDirectory: concepts
  sources:
    - tracing-ollama-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disabling-mlflow-autologging
    - DMA
  citations:
    - file: tracing-ollama-databricks-on-aws.md
title: Disabling MLflow Autologging
description: The mechanism to globally disable MLflow auto-tracing for Ollama/OpenAI interactions by calling mlflow.openai.autolog(disable=True) or mlflow.autolog(disable=True).
tags:
  - mlflow
  - configuration
  - tracing
timestamp: "2026-06-19T23:12:50.834Z"
---

# Disabling [MLflow Autologging](/concepts/mlflow-autologging.md)

**Disabling [MLflow](/concepts/mlflow.md) Autologging** refers to turning off the automatic trace and metric capture that [MLflow](/concepts/mlflow.md) performs for supported integrations. When autologging is active, [MLflow](/concepts/mlflow.md) records model parameters, metrics, and inference [Traces](/concepts/traces.md) for each logged operation. Disabling it can be useful for controlling cost, reducing noise, or when manual logging is preferred. ^[tracing-ollama-databricks-on-aws.md]

## How to Disable Autologging

For integrations that use the OpenAI SDK (including [Ollama](/concepts/ollama.md) via its OpenAI-compatible endpoint), autologging can be disabled in two ways:

1. **Integration-specific disable** – Call the `autolog()` function with `disable=True` for the specific library. For example, to disable autologging for OpenAI/[Ollama](/concepts/ollama.md):
   ```python
   [[mlflow|MLflow]].openai.autolog(disable=True)
   ```
   ^[tracing-ollama-databricks-on-aws.md]

2. **Global disable** – Call `mlflow.autolog(disable=True)` to turn off autologging for all integrations at once.
   ```python
   [[mlflow|MLflow]].autolog(disable=True)
   ```
   ^[tracing-ollama-databricks-on-aws.md]

Both calls take effect immediately for subsequent operations. The global call overrides all integration-specific settings.

## Context: Serverless Compute Clusters

On Databricks Serverless Compute clusters, autologging for generative AI tracing frameworks is **not automatically enabled**. Users must explicitly enable autologging for each integration they want to trace (e.g., `mlflow.openai.autolog()`). Therefore, on such clusters, disabling autologging is only relevant if it was previously enabled. ^[tracing-ollama-databricks-on-aws.md]

## Related Concepts

- [MLflow Autologging](/concepts/mlflow-autologging.md) – Overview of automatic logging capabilities.
- [OpenAI Autolog](/concepts/mlflow-openai-autolog.md) – The integration used for OpenAI SDK [Traces](/concepts/traces.md) (also covers [Ollama](/concepts/ollama.md)).
- [Ollama](/concepts/ollama.md) – Local LLM platform that uses the OpenAI API.
- [Tracing](/concepts/mlflow-tracing.md) – How [MLflow](/concepts/mlflow.md) captures and organizes trace data.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Where [Traces](/concepts/traces.md) and metrics are recorded.

## Sources

- tracing-ollama-databricks-on-aws.md

# Citations

1. [tracing-ollama-databricks-on-aws.md](/references/tracing-ollama-databricks-on-aws-d0fc7add.md)
