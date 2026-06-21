---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 125af591d2bb40e22ac694244a942ef033c0682ae76deaac4dfeb8617811f946
  pageDirectory: concepts
  sources:
    - mlflow-tracing-integrations-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-integration-auto-tracing-in-mlflow
    - MATIM
  citations:
    - file: mlflow-tracing-integrations-databricks-on-aws.md
title: Multi-Integration Auto Tracing in MLflow
description: Enabling auto-tracing for several GenAI libraries simultaneously to produce a single cohesive trace across combined toolchains.
tags:
  - mlflow
  - tracing
  - multi-integration
timestamp: "2026-06-19T19:41:01.813Z"
---

# Multi-Integration Auto Tracing in MLflow

**Multi-Integration Auto Tracing** in MLflow refers to the ability to enable automatic tracing for several Generative AI libraries and frameworks simultaneously within a single application. This provides a unified, end-to-end trace that captures steps from all instrumented libraries, allowing developers to inspect the complete flow of their GenAI applications without manual instrumentation. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) offers a one-line automatic tracing experience for a wide array of popular libraries including OpenAI, LangChain, LangGraph, Anthropic, DSPy, Databricks, Bedrock, and AutoGen. Because GenAI applications often combine multiple libraries (e.g., LangChain with direct OpenAI calls), MLflow allows you to enable auto-tracing for each library independently. When multiple integrations are enabled, MLflow generates a **single, cohesive trace** that combines steps from all of them. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Example: Enabling LangChain and OpenAI Together

The following example demonstrates enabling auto-tracing for both LangChain and OpenAI simultaneously:

```python
import mlflow

# Enable [[mlflow-tracing|MLflow Tracing]] for both LangChain and OpenAI
mlflow.langchain.autolog()
mlflow.openai.autolog()

# Your code using both LangChain and OpenAI directly...
```

The resulting trace merges the internal steps from LangChain and direct OpenAI LLM calls into one unified view. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Important Usage Notes

- **Serverless compute**: On serverless compute clusters, autologging for GenAI tracing frameworks is **not automatically enabled**. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace. ^[mlflow-tracing-integrations-databricks-on-aws.md]
- **Disabling auto tracing**: You can disable auto-tracing for a specific library by calling `mlflow.<library>.autolog(disable=True)`. To disable all autologging integrations at once, use `mlflow.autolog(disable=True)`. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Secure API Key Management

For production environments, Databricks recommends managing API keys through [AI Gateway](/concepts/ai-gateway.md) (preferred) or Databricks Secrets. AI Gateway offers additional governance features such as rate limiting, fallbacks, and guardrails. Never commit API keys directly in code or notebooks. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Custom Components and Unsupported Libraries

For custom components or libraries not covered by automatic tracing, MLflow provides powerful [Manual Tracing APIs](/concepts/manual-tracing-apis.md) that allow you to instrument any part of your application. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overarching observability system for GenAI applications.
- [Automatic Tracing](/concepts/automatic-tracing.md) – The mechanism that captures logic and intermediate steps without code changes.
- [Manual Tracing](/concepts/manual-tracing.md) – APIs for instrumenting custom or unsupported components.
- [AI Gateway](/concepts/ai-gateway.md) – Recommended service for governing and monitoring access to GenAI models.
- LangChain Tracing – Specific integration for LangChain applications.
- OpenAI Tracing – Specific integration for direct OpenAI library calls.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Compute environment where autologging must be explicitly enabled.

## Sources

- mlflow-tracing-integrations-databricks-on-aws.md

# Citations

1. [mlflow-tracing-integrations-databricks-on-aws.md](/references/mlflow-tracing-integrations-databricks-on-aws-22e947f8.md)
