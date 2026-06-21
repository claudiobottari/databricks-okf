---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d39f163b6918f4112eda54f1e99f65c92e3e67005408a67c619dd3a8b154192
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-foundation-models-via-openai-client
    - DFMVOC
  citations:
    - file: get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
title: Databricks-hosted foundation models via OpenAI client
description: The databricks_openai.DatabricksOpenAI client allows calling Databricks-hosted LLMs (e.g., Claude Sonnet 4) using the standard OpenAI SDK interface.
tags:
  - databricks
  - openai
  - llm
  - foundation-models
timestamp: "2026-06-19T18:59:27.734Z"
---

# Databricks-hosted foundation models via OpenAI client

The **Databricks-hosted foundation models via OpenAI client** pattern refers to the use of an OpenAI‑compatible client library – specifically `DatabricksOpenAI` – to invoke foundation models that are served on the Databricks platform. This approach lets developers interact with models such as Claude Sonnet and others using the familiar OpenAI SDK interface, while keeping all data and inference within the Databricks environment.

## Overview

Databricks provides a Python client, `databricks_openai`, that exposes a `DatabricksOpenAI` class. The class mirrors the interface of the standard `openai.OpenAI` client, but routes all requests to Databricks-hosted model endpoints. This eliminates the need to manage separate API keys or endpoints for Databricks models; authentication and routing are handled automatically by the client when running inside a Databricks workspace.

To use the client, install the required packages and create an instance:

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()
model_name = "databricks-claude-sonnet-4"
```

The resulting object (`client`) can then be used with any method of the OpenAI API, such as `client.chat.completions.create()`. The model name string (e.g., `"databricks-claude-sonnet-4"`) identifies which Databricks-hosted foundation model to use.

This approach is particularly useful when building GenAI applications that will be traced with [MLflow Tracing](/concepts/mlflow-tracing.md), as shown in the quickstart tutorial for Databricks notebooks. The auto‑tracing capability of `mlflow.openai.autolog()` automatically captures every call made through the OpenAI client, providing insight into inputs, outputs, token counts, and latency. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Alternative: Standard OpenAI SDK

If you are instead calling models hosted on OpenAI’s own platform (e.g., GPT‑4), you can use the standard `openai.OpenAI` client with a configured `OPENAI_API_KEY`. The tutorial documentation shows both options, allowing the developer to choose the appropriate backend while keeping the rest of the code nearly identical. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Integration with [MLflow Tracing](/concepts/mlflow-tracing.md)

When combined with [MLflow Tracing](/concepts/mlflow-tracing.md), the `DatabricksOpenAI` client enables automatic instrumentation of every model invocation. The following pattern is typical:

```python
import mlflow

mlflow.openai.autolog()
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/tracing-quickstart")

@mlflow.trace
def my_app(input: str):
    response = client.chat.completions.create(
        model=model_name,
        temperature=0.1,
        max_tokens=200,
        messages=[...]
    )
    return response.choices[0].message.content
```

After running the application, a trace containing a root span (the `my_app` call) and a child span (the OpenAI completion request) appears in the MLflow experiment UI. The trace shows inputs, outputs, model name, token counts, and timing. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Model Names

Databricks-hosted models are referenced using the prefix `databricks-` followed by the model identifier. For example, `"databricks-claude-sonnet-4"` aliases the Anthropic Claude Sonnet 4 model served by Databricks. The exact list of available model names can be found in the documentation for [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md). ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Requirements

- The code must run in a Databricks workspace where the `databricks_openai` package is installed and the caller has appropriate permissions to access the foundation model endpoints.
- For standard OpenAI SDK usage, an `OPENAI_API_KEY` must be set in the environment.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Automatic tracing of LLM calls, including those made via the OpenAI client.
- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) – The underlying API endpoints that `DatabricksOpenAI` calls.
- [OpenAI client](/concepts/openai-client-compatibility.md) – The general OpenAI SDK interface that `DatabricksOpenAI` implements.
- GenAI application instrumentation – Broader topic on adding tracing and monitoring to GenAI apps.
- [Databricks notebook development](/concepts/databricks-genai-notebook-development.md) – The typical environment for using this pattern.

## Sources

- get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws-860f2761.md)
