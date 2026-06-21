---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85d0235f7cb02c39a071eeea92d1304f3046140416107831122b3b9ab50690ae
  pageDirectory: concepts
  sources:
    - tracing-databricks-foundation-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autologging-configuration-for-databricks-environments
    - ACFDE
  citations:
    - file: tracing-databricks-foundation-models-databricks-on-aws.md
title: Autologging Configuration for Databricks Environments
description: Prerequisites and configuration steps for enabling MLflow Tracing on Databricks Foundation Models, including installing mlflow[databricks]>=3.1 and the OpenAI SDK, setting environment variables (DATABRICKS_HOST, DATABRICKS_TOKEN), and noting that serverless compute clusters require explicit autolog() calls.
tags:
  - mlflow
  - configuration
  - databricks
  - prerequisites
timestamp: "2026-06-19T23:11:51.074Z"
---

# Autologging Configuration for Databricks Environments

**Autologging Configuration for Databricks Environments** refers to the setup and management of automatic [MLflow Tracing](/concepts/mlflow-tracing.md) for machine learning workflows running on Databricks. Autologging automatically captures [Traces](/concepts/traces.md), metrics, parameters, and model artifacts without requiring manual instrumentation of code. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) provides automatic trace capture for various ML integrations on Databricks. For Databricks Foundation Models, which use an OpenAI-compatible API, autologging is enabled by calling `mlflow.openai.autolog()`. Once enabled, [MLflow](/concepts/mlflow.md) captures [Traces](/concepts/traces.md) for LLM invocations and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Serverless Compute Considerations

On serverless compute clusters, autologging is **not automatically enabled**. Users must explicitly call `mlflow.openai.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for the Databricks Foundation Models integration. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Databricks Foundation Models, install [MLflow](/concepts/mlflow.md) and the OpenAI SDK (required because Databricks Foundation Models use an OpenAI-compatible API). ^[tracing-databricks-foundation-models-databricks-on-aws.md]

For development environments, install the full [MLflow](/concepts/mlflow.md) package with Databricks extras:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" openai
```

The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks. [MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience with Databricks Foundation Models. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Environment Configuration

For users outside Databricks notebooks, set the following environment variables:

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"
```

For users inside Databricks notebooks, these credentials are automatically set. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Captured Information

When autologging is enabled, [[mlflow-trace|MLflow Trace]] automatically captures the following information about Databricks Foundation Model calls: ^[tracing-databricks-foundation-models-databricks-on-aws.md]

- Prompts and completion responses
- Latencies
- Model name and endpoint
- Additional metadata such as `temperature` and `max_tokens`, if specified
- Function calling if returned in the response
- Any exception if raised

## Supported APIs

[MLflow](/concepts/mlflow.md) supports [Automatic Tracing](/concepts/automatic-tracing.md) for supported [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md). To request support for additional APIs, submit a feature request on the [MLflow](/concepts/mlflow.md) GitHub repository. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Streaming Support

[MLflow Tracing](/concepts/mlflow-tracing.md) supports the streaming API of Databricks Foundation Models. With autologging enabled, [MLflow](/concepts/mlflow.md) automatically [Traces](/concepts/traces.md) the streaming response and renders the concatenated output in the span UI. This allows developers to use `stream=True` in their API calls and still receive full trace visibility. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Function Calling

[MLflow Tracing](/concepts/mlflow-tracing.md) automatically captures function calling responses from Databricks Foundation Models. Function instructions in the response are highlighted in the trace UI. Additionally, tool functions can be annotated with the `@mlflow.trace` decorator (using `SpanType.TOOL`) to create spans for tool execution, enabling end-to-end visibility of [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) workflows. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Disabling Autologging

Auto tracing for Databricks Foundation Models can be disabled globally by calling:

```python
[[mlflow|MLflow]].openai.autolog(disable=True)
```

or

```python
[[mlflow|MLflow]].autolog(disable=True)
```

^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that powers autologging
- Databricks Foundation Models — The [Model Serving](/concepts/model-serving.md) endpoints that support OpenAI-compatible APIs
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit where [Traces](/concepts/traces.md) are logged
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Compute environment requiring explicit autologging configuration
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflows that benefit from function calling [Traces](/concepts/traces.md)
- [Production Monitoring](/concepts/production-monitoring.md) — Monitoring workflows that may use scheduled scoring with traced models

## Sources

- tracing-databricks-foundation-models-databricks-on-aws.md

# Citations

1. [tracing-databricks-foundation-models-databricks-on-aws.md](/references/tracing-databricks-foundation-models-databricks-on-aws-5051d97b.md)
