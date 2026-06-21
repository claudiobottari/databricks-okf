---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b83d42885ed75e81cc596d63dea00edcf531a7092c492088061585c9dc348429
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-serverless-compute-autologging-requirement
    - M3SCAR
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: MLflow 3 Serverless Compute Autologging Requirement
description: On Databricks serverless compute clusters, autologging for genAI tracing frameworks is not automatically enabled; users must explicitly call the appropriate `mlflow.<library>.autolog()` function.
tags:
  - mlflow
  - serverless
  - databricks
  - autologging
timestamp: "2026-06-18T14:29:47.904Z"
---

---
title: MLflow 3 Serverless Compute Autologging Requirement
summary: On Databricks serverless compute, automatic tracing for GenAI frameworks is not enabled by default; you must explicitly call the corresponding `mlflow.<library>.autolog()` function.
sources:
  - automatic-tracing-databricks-on-aws.md
kind: concept
createdAt: 
updatedAt: 
tags:
  - mlflow
  - serverless
  - autologging
  - genai
  - tracing
aliases:
  - serverless autologging requirement
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow 3 Serverless Compute Autologging Requirement

When using [MLflow 3](/concepts/mlflow-3.md) on Databricks **serverless compute clusters**, automatic tracing for generative AI frameworks is **not automatically enabled**. Unlike standard compute where autologging may be turned on by default, serverless compute requires you to explicitly enable it by calling the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Why the Requirement Exists

Serverless compute clusters are designed for ephemeral, on-demand workloads and do not pre-load environment configurations that would normally enable autologging. Without explicitly enabling it, traces for supported frameworks such as OpenAI, LangChain, or Anthropic will not be captured, even if the libraries are installed. ^[automatic-tracing-databricks-on-aws.md]

## How to Enable Autologging

To enable automatic tracing on serverless compute, call the integration‑specific autolog function **before** making any traced calls. Databricks recommends using MLflow 3 for the latest GenAI tracing capabilities. ^[automatic-tracing-databricks-on-aws.md]

### Basic Prerequisites

1. Install the required package:

   ```python
   %pip install --upgrade "mlflow[databricks]>=3.1"
   ```

2. Install the SDK for the framework you want to trace (e.g., `openai`, `langchain`, `anthropic`).  
3. Restart the Python interpreter (e.g., `dbutils.library.restartPython()` in Databricks notebooks).  
4. Configure any required API keys (e.g., `OPENAI_API_KEY`) as environment variables. ^[automatic-tracing-databricks-on-aws.md]

### Enabling for a Single Framework

For example, to enable automatic tracing for OpenAI calls (including those that use Databricks Foundation Model APIs):

```python
import mlflow
mlflow.openai.autolog()
```

After this call, every `client.chat.completions.create()` invocation will be automatically traced. ^[automatic-tracing-databricks-on-aws.md]

### Enabling for Multiple Frameworks

You can enable autologging for several frameworks in the same agent. Each requires its own explicit call:

```python
mlflow.openai.autolog()
mlflow.langchain.autolog()
```

This allows traces to capture calls across different providers and libraries in a single workflow. ^[automatic-tracing-databricks-on-aws.md]

### Combining with Manual Tracing

Autologging works seamlessly with manual tracing using `@mlflow.trace`. You can add custom spans around business logic while still benefiting from automatic tracing of framework calls. ^[automatic-tracing-databricks-on-aws.md]

## Supported Integrations

MLflow 3 supports automatic tracing for over 20 libraries and frameworks. The full list is documented in the [Automatic Tracing Integrations](/concepts/automatic-vs-manual-tracing-instrumentation.md) page. Each integration requires its own `mlflow.<library>.autolog()` call on serverless compute. ^[automatic-tracing-databricks-on-aws.md]

## Best Practices

- **Call autolog early** – Enable tracing at the top of your script, before any LLM calls, to ensure all subsequent spans are captured.
- **Keep credentials separate** – Set API keys as environment variables or use Databricks secrets rather than hardcoding them.
- **Use MLflow 3** – The `mlflow[databricks]>=3.1` package provides the most up‑to‑date GenAI tracing features. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) – The general concept of instrumenting framework calls without manual span creation.
- [MLflow 3](/concepts/mlflow-3.md) – The version of MLflow that includes advanced GenAI tracing capabilities.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) – Adding custom spans using `@mlflow.trace`.
- [Automatic Tracing Integrations](/concepts/automatic-vs-manual-tracing-instrumentation.md) – The list of supported libraries and frameworks for autologging.
- Serverless Compute – The Databricks compute environment where autologging is not enabled by default.
- [GenAI Tracing](/concepts/mlflow-genai-tracing.md) – The broader MLflow feature for tracing generative AI application calls.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
