---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4917fa88463cb870bbe52d902626cd4ea11e6e05e23ce81d58ce98ebad308b0
  pageDirectory: concepts
  sources:
    - mlflow-tracing-integrations-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-tracing-requirements
    - SCTR
    - Serverless compute requirements
    - serverless compute requirements
    - serverless computing|serverless
  citations:
    - file: mlflow-tracing-integrations-databricks-on-aws.md
title: Serverless Compute Tracing Requirements
description: On serverless compute clusters, GenAI tracing autologging is not automatically enabled and must be explicitly enabled by calling mlflow.<library>.autolog() functions.
tags:
  - mlflow
  - serverless
  - tracing
timestamp: "2026-06-19T19:41:32.844Z"
---

# Serverless Compute Tracing Requirements

**Serverless Compute Tracing Requirements** refers to the specific configuration needed to enable [MLflow Tracing](/concepts/mlflow-tracing.md)] automatic instrumentation on [Serverless Compute] clusters in Databricks. Unlike traditional compute environments where autologging is automatically enabled, serverless compute requires explicit activation of tracing functionality. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Explicit Autologging Requirement

On serverless compute clusters, autologging for GenAI tracing frameworks is **not automatically enabled**. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for each specific integration you want to trace. ^[mlflow-tracing-integrations-databricks-on-aws.md]

This requirement applies to all supported tracing integrations, including [OpenAI], [LangChain], [LangGraph], [Anthropic], [DSPy], [Databricks], [Bedrock], and [AutoGen]. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Basic Configuration Example

The following example demonstrates enabling tracing for OpenAI on serverless compute:

```python
import mlflow
import openai

# Enable auto-tracing for OpenAI
mlflow.openai.autolog()

# Set up MLflow tracking
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/openai-tracing-demo")
```

^[mlflow-tracing-integrations-databricks-on-aws.md]

## Enabling Multiple Tracing Integrations

GenAI applications often combine multiple libraries. You can enable auto-tracing for several integrations simultaneously to create a unified tracing experience: ^[mlflow-tracing-integrations-databricks-on-aws.md]

```python
import mlflow

# Enable [[mlflow-tracing|MLflow Tracing]] for both LangChain and OpenAI
mlflow.langchain.autolog()
mlflow.openai.autolog()
```

MLflow will generate a single, cohesive trace that combines steps from both integrations. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Disabling Auto Tracing

To disable auto tracing for a specific library, call `mlflow.<library>.autolog(disable=True)`. To disable all autologging integrations at once, use `mlflow.autolog(disable=True)`. ^[mlflow-tracing-integrations-databricks-on-aws.md]

```python
import mlflow

# Disable for a specific library
mlflow.openai.autolog(disable=True)

# Disable all autologging
mlflow.autolog(disable=True)
```

## Secure API Key Management

For production environments, Databricks recommends using [AI Gateway] or [Databricks Secrets] to manage API keys. Never commit API keys directly in your code or notebooks. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that provides observability into GenAI applications
- Serverless Compute — The compute infrastructure that requires explicit autologging
- [Automatic Tracing](/concepts/automatic-tracing.md) — The one-line instrumentation approach for [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Manual Tracing APIs] — For custom components or unsupported libraries
- [AI Gateway](/concepts/ai-gateway.md) — Preferred method for managing API keys with governance features
- Databricks Secrets — Alternative for managing sensitive credentials

## Sources

- mlflow-tracing-integrations-databricks-on-aws.md

# Citations

1. [mlflow-tracing-integrations-databricks-on-aws.md](/references/mlflow-tracing-integrations-databricks-on-aws-22e947f8.md)
