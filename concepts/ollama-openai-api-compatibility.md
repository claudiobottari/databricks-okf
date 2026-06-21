---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25fa44c0da3a0c1a6da5af760b3ad0b0569e516f682f48c5982460a3db9fa6b9
  pageDirectory: concepts
  sources:
    - tracing-ollama-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ollama-openai-api-compatibility
    - OOAC
    - OpenAI API Compatibility
  citations:
    - file: tracing-ollama-databricks-on-aws.md
title: Ollama OpenAI API Compatibility
description: Ollama's local endpoint is compatible with the OpenAI API format, allowing the OpenAI SDK client to query it by setting a custom base_url and dummy api_key.
tags:
  - api
  - openai
  - ollama
  - compatibility
timestamp: "2026-06-19T23:12:47.042Z"
---

# [Ollama](/concepts/ollama.md) OpenAI API Compatibility

**Ollama OpenAI API Compatibility** refers to the design property of the [Ollama](/concepts/ollama.md)](https://[Ollama](/concepts/ollama.md).com/) platform that makes its local LLM endpoint compatible with the OpenAI API specification. This compatibility allows developers to query locally served models using the OpenAI SDK and enables seamless integration with observability tools like [MLflow Tracing](/concepts/mlflow-tracing.md). ^[tracing-ollama-databricks-on-aws.md]

## Overview

[Ollama](/concepts/ollama.md) is an open-source platform that enables users to run large language models (LLMs) locally on their devices, including models such as Llama 3.2, Gemma 2, Mistral, Code Llama, and more. Because the local LLM endpoint served by [Ollama](/concepts/ollama.md) is compatible with the OpenAI API, you can query it using the OpenAI SDK as if you were connecting to OpenAI's cloud service. ^[tracing-ollama-databricks-on-aws.md]

## How It Works

To leverage [Ollama](/concepts/ollama.md)'s OpenAI API compatibility, you configure the OpenAI client to point to the local [Ollama](/concepts/ollama.md) REST endpoint instead of the OpenAI cloud endpoint. The client is instantiated with a `base_url` pointing to `http://localhost:11434/v1` and an `api_key` parameter, which is required to instantiate the client but can be set to any dummy value since the local server does not authenticate. ^[tracing-ollama-databricks-on-aws.md]

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",  # The local [[ollama|Ollama]] REST endpoint
    api_key="dummy",  # Required to instantiate OpenAI client, can be a random string
)

response = client.chat.completions.create(
    model="llama3.2:1b",
    messages=[
        {"role": "system", "content": "You are a science teacher."},
        {"role": "user", "content": "Why is the sky blue?"},
    ],
)
```

^[tracing-ollama-databricks-on-aws.md]

## Tracing with [MLflow](/concepts/mlflow.md)

The OpenAI API compatibility of [Ollama](/concepts/ollama.md) enables tracing via [MLflow](/concepts/mlflow.md) Open AI autologging](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).openai.html#mlflow.openai.autolog). By calling `mlflow.openai.autolog()`, any LLM interactions performed through [Ollama](/concepts/ollama.md) are automatically recorded to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-ollama-databricks-on-aws.md]

### Enabling Auto-Tracing

To enable tracing for [Ollama](/concepts/ollama.md):

```python
import [[mlflow|MLflow]]

# Enable auto-tracing for OpenAI
[[mlflow|MLflow]].openai.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] on Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/ollama-demo")
```

^[tracing-ollama-databricks-on-aws.md]

### Important Note on Serverless Compute

On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[tracing-ollama-databricks-on-aws.md]

### Disabling Auto-Tracing

Auto tracing for [Ollama](/concepts/ollama.md) can be disabled globally by calling `mlflow.openai.autolog(disable=True)` or `mlflow.autolog(disable=True)`. ^[tracing-ollama-databricks-on-aws.md]

## Workflow

1. Run the [Ollama](/concepts/ollama.md) server with the desired LLM model.
2. Enable auto-tracing for OpenAI SDK using `mlflow.openai.autolog()`.
3. Query the LLM using the OpenAI client configured with the local [Ollama](/concepts/ollama.md) endpoint.
4. View the [Traces](/concepts/traces.md) in the [MLflow](/concepts/mlflow.md) UI.

^[tracing-ollama-databricks-on-aws.md]

## Related Concepts

- [Tracing Ollama](/concepts/ollama.md) — Detailed guide on setting up tracing for [Ollama](/concepts/ollama.md) models
- [MLflow Tracing](/concepts/mlflow-tracing.md) — How [MLflow](/concepts/mlflow.md) captures and organizes trace data
- OpenAI SDK Integration — Using the OpenAI SDK for local and remote LLM inference
- Local LLM Deployment — Running large language models on local devices
- GenAI Tracing Frameworks — Overview of tracing frameworks for generative AI applications

## Sources

- tracing-ollama-databricks-on-aws.md

# Citations

1. [tracing-ollama-databricks-on-aws.md](/references/tracing-ollama-databricks-on-aws-d0fc7add.md)
