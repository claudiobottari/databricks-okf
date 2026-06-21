---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50c4d8f85835ca5dd9ff7d8cef5093130500747035a23103d949586cf48f7fbd
  pageDirectory: concepts
  sources:
    - tracing-smolagents-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-auto-tracing-limitations
    - MAL
  citations:
    - file: tracing-smolagents-databricks-on-aws.md
title: MLflow Auto-Tracing Limitations
description: MLflow auto-tracing only supports synchronous calls; async and streaming methods are not traced
tags:
  - mlflow
  - limitations
  - tracing
timestamp: "2026-06-19T23:13:15.167Z"
---

# [MLflow](/concepts/mlflow.md) Auto-Tracing Limitations

**MLflow Auto-Tracing Limitations** describes the known restrictions and required conditions when using MLflow’s [Automatic Tracing](/concepts/automatic-tracing.md) feature with supported agent frameworks. These limitations affect the types of calls that can be traced, the compute environments where autologging is active, and the configuration steps needed to enable tracing.

## Synchronous‑Call Only Support

[MLflow](/concepts/mlflow.md) auto-tracing only supports **synchronous API calls**. Asynchronous methods and streaming responses are not traced. If an integration (such as [Smolagents](/concepts/smolagents.md)) provides both synchronous and asynchronous interfaces, only the synchronous calls produce [Traces](/concepts/traces.md); any asynchronous or stream‑based invocations are silently ignored by the auto‑tracing machinery. ^[tracing-smolagents-databricks-on-aws.md]

## Autologging Not Enabled by Default on Serverless Compute

On Serverless Compute clusters, autologging for generative AI tracing frameworks is **not automatically enabled**. Users must explicitly call the appropriate `mlflow.<framework>.autolog()` function for each integration they wish to trace. For example, when using [Smolagents](/concepts/smolagents.md) on a serverless cluster, `mlflow.[Smolagents](/concepts/smolagents.md).autolog()` must be called before the agent code runs. This applies to all genAI tracing integrations, not just [Smolagents](/concepts/smolagents.md), but the behavior is documented specifically in the context of serverless compute. ^[tracing-smolagents-databricks-on-aws.md]

## Required Library Versions and Dependencies

To use auto‑tracing, the [MLflow](/concepts/mlflow.md) version must be **3.0 or higher** ([MLflow 3](/concepts/mlflow-3.md) is recommended). Additionally, the integration library (e.g., `smolagents`) must be installed with the correct extras. For development environments, the full `mlflow[databricks]` package is required. If these dependencies are missing, tracing may fail silently or not be generated. ^[tracing-smolagents-databricks-on-aws.md]

## Token Tracking Behavior

[MLflow](/concepts/mlflow.md) logs token usage for each LLM call within a trace and aggregates it in the trace object. This is a feature, not a limitation, but users should be aware that token tracking depends on the LLM provider returning token counts. If the provider does not expose token usage, the `token_usage` fields may be absent or zero. ^[tracing-smolagents-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing subsystem
- [Smolagents](/concepts/smolagents.md) – Lightweight agent framework that integrates with [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Autologging](/concepts/mlflow-autologging.md) – Mechanism that automatically captures trace data
- Synchronous vs Asynchronous Calls – Why only synchronous calls are traced
- Serverless Compute – Where autologging must be explicitly enabled
- [MLflow 3](/concepts/mlflow-3.md) – Recommended version for the best tracing experience

## Sources

- tracing-smolagents-databricks-on-aws.md

# Citations

1. [tracing-smolagents-databricks-on-aws.md](/references/tracing-smolagents-databricks-on-aws-485dc1ff.md)
