---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d9deec9ab010786234f133208481d0693d0325e8513d7b8adb7ce9288505687
  pageDirectory: concepts
  sources:
    - tracing-ollama-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-openai-autolog-for-ollama-tracing
    - MOAFOT
  citations:
    - file: tracing-ollama-databricks-on-aws.md
title: MLflow OpenAI Autolog for Ollama Tracing
description: Technique using mlflow.openai.autolog() to automatically capture and record Ollama LLM interactions as traces in MLflow, leveraging Ollama's OpenAI API compatibility.
tags:
  - mlflow
  - tracing
  - observability
  - databricks
timestamp: "2026-06-19T23:13:06.771Z"
---

# [MLflow OpenAI Autolog](/concepts/mlflow-openai-autolog.md) for [Ollama](/concepts/ollama.md) Tracing

**MLflow OpenAI Autolog for [Ollama](/concepts/ollama.md) Tracing** is a method for instrumenting and capturing trace data from [Ollama](/concepts/ollama.md)-served large language models (LLMs) using [MLflow](/concepts/mlflow.md)'s OpenAI SDK compatibility layer. Since [Ollama](/concepts/ollama.md) exposes a local API endpoint that is compatible with the OpenAI API format, you can use `mlflow.openai.autolog()` to automatically record all LLM interactions made through the OpenAI client library when pointed at an [Ollama](/concepts/ollama.md) server. ^[tracing-ollama-databricks-on-aws.md]

## Overview

[Ollama](/concepts/ollama.md) is an open-source platform that enables users to run LLMs locally on their devices. Supported models include Llama 3.2, Gemma 2, Mistral, Code Llama, and many others. Because the local endpoint served by [Ollama](/concepts/ollama.md) is compatible with the OpenAI API, any code written against the OpenAI SDK can be redirected to a local [Ollama](/concepts/ollama.md) instance simply by changing the `base_url` and `api_key` parameters. ^[tracing-ollama-databricks-on-aws.md]

When `mlflow.openai.autolog()` is enabled, every call to `client.chat.completions.create()` (and other OpenAI-compatible methods) is automatically traced and recorded to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-ollama-databricks-on-aws.md]

## Enabling Autologging

To enable tracing for [Ollama](/concepts/ollama.md), call:

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].openai.autolog()
```

On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is **not** automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace. ^[tracing-ollama-databricks-on-aws.md]

## Example Usage

1. **Start the [Ollama](/concepts/ollama.md) server** with the desired LLM model (e.g., `ollama run llama3.2:1b`).

2. **Enable auto-tracing and configure [MLflow Tracking](/concepts/mlflow-tracking.md):**

   ```python
   import [[mlflow|MLflow]]

   # Enable auto-tracing for OpenAI SDK
   [[mlflow|MLflow]].openai.autolog()

   # Set up [[mlflow-tracking|MLflow Tracking]] on Databricks
   [[mlflow|MLflow]].set_tracking_uri("databricks")
   [[mlflow|MLflow]].set_experiment("/Shared/ollama-demo")
   ```

3. **Query the LLM via the [Ollama](/concepts/ollama.md) endpoint:**

   ```python
   from openai import OpenAI

   client = OpenAI(
       base_url="http://localhost:11434/v1",  # The local [[ollama|Ollama]] REST endpoint
       api_key="dummy",  # Required but can be any string
   )

   response = client.chat.completions.create(
       model="llama3.2:1b",
       messages=[
           {"role": "system", "content": "You are a science teacher."},
           {"role": "user", "content": "Why is the sky blue?"},
       ],
   )
   ```

   All interactions are automatically traced and appear in the [MLflow](/concepts/mlflow.md) UI under the experiment `/Shared/ollama-demo`. ^[tracing-ollama-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto-tracing can be disabled globally in two ways:

- `mlflow.openai.autolog(disable=True)` — disables only the OpenAI/[Ollama](/concepts/ollama.md) integration
- `mlflow.autolog(disable=True)` — disables all autologging integrations ^[tracing-ollama-databricks-on-aws.md]

## How It Works

The mechanism relies on [Ollama](/concepts/ollama.md)'s API compatibility with OpenAI. By setting `base_url="http://localhost:11434/v1"`, the OpenAI client routes requests to the local [Ollama](/concepts/ollama.md) server instead of the OpenAI cloud API. The `api_key` parameter is still required by the OpenAI client library to instantiate the object, but it can be set to any arbitrary string (e.g., `"dummy"`) when connecting to [Ollama](/concepts/ollama.md). ^[tracing-ollama-databricks-on-aws.md]

[MLflow](/concepts/mlflow.md)'s autologging intercepts the SDK calls and records trace data — including input messages, output completions, latency, and model metadata — to the [MLflow Experiment](/concepts/mlflow-experiment.md) trace storage. ^[tracing-ollama-databricks-on-aws.md]

## Limitations and Notes

- **Serverless Clusters:** On Databricks serverless compute, [Automatic Tracing](/concepts/automatic-tracing.md) is not enabled by default. You must call `mlflow.openai.autolog()` explicitly. ^[tracing-ollama-databricks-on-aws.md]
- **Local Dependency:** The [Ollama](/concepts/ollama.md) server must be running locally (or on a reachable network address) at the time of the API calls. [MLflow Tracing](/concepts/mlflow-tracing.md) does not manage the [Ollama](/concepts/ollama.md) process itself. ^[tracing-ollama-databricks-on-aws.md]
- **API Key Requirement:** The OpenAI SDK enforces a non-empty `api_key` string at instantiation. While [Ollama](/concepts/ollama.md) does not require a real key, the parameter must still be provided. ^[tracing-ollama-databricks-on-aws.md]

## Related Concepts

- [Ollama](/concepts/ollama.md) — The local LLM serving platform
- [MLflow OpenAI Autolog](/concepts/mlflow-openai-autolog.md) — The underlying tracing mechanism for OpenAI SDK interactions
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader framework for capturing and visualizing trace data
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit where trace data is stored
- [GenAI Tracing](/concepts/mlflow-genai-tracing.md) — General approach for instrumenting generative AI applications
- Serverless Compute on Databricks — Environment where explicit autolog is required

## Sources

- tracing-ollama-databricks-on-aws.md

# Citations

1. [tracing-ollama-databricks-on-aws.md](/references/tracing-ollama-databricks-on-aws-d0fc7add.md)
