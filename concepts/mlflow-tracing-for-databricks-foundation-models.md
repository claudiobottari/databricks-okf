---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd39f23ca0d01c2b76d6970674922928908b13f0584e4af11cf880cdd4176bd9
  pageDirectory: concepts
  sources:
    - tracing-databricks-foundation-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-databricks-foundation-models
    - MTFDFM
  citations:
    - file: tracing-databricks-foundation-models-databricks-on-aws.md
title: MLflow Tracing for Databricks Foundation Models
description: Automatic tracing capability that captures LLM invocation metadata, prompts, responses, latencies, and exceptions for Databricks Foundation Model API calls via mlflow.openai.autolog().
tags:
  - mlflow
  - tracing
  - databricks
  - llm-observability
timestamp: "2026-06-19T23:10:46.343Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) for Databricks Foundation Models

**MLflow Tracing for Databricks Foundation Models** provides automatic, OpenTelemetry-based trace capture for LLM invocations made through [Databricks Foundation Model Endpoints](/concepts/databricks-foundation-model-endpoints.md). Because Databricks Foundation Models expose an OpenAI-compatible API, tracing is enabled by calling `mlflow.openai.autolog()`. Once activated, [MLflow](/concepts/mlflow.md) records prompts, completions, latencies, model metadata, and any errors directly to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) captures the following information for every Databricks Foundation Model call:

- Prompts and completion responses
- Request latency
- Model name and endpoint
- Additional parameters (e.g., `temperature`, `max_tokens`) if specified
- Function call arguments and results, if function calling is used
- Any exceptions raised during the request

On serverless compute clusters, autologging is not automatically enabled; you must explicitly call `mlflow.openai.autolog()` to start tracing. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Prerequisites

- **MLflow 3** (or later) is recommended for the best tracing experience.
- Install the full [MLflow](/concepts/mlflow.md) package with Databricks extras and the OpenAI SDK:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" openai
```

This installs all required dependencies for local development and experimentation on Databricks. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Environment Setup

Configure your Databricks credentials as environment variables (automatic inside Databricks notebooks):

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"
```

Then enable autologging and set the tracking URI:

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].openai.autolog()
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/databricks-foundation-models-demo")
```

^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Basic Usage

Create an OpenAI client pointing to your Databricks workspace and call a foundation model. [Traces](/concepts/traces.md) are automatically logged to the experiment.

```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    temperature=0.1,
    max_tokens=100,
)
```

^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Streaming

[MLflow Tracing](/concepts/mlflow-tracing.md) supports streaming responses. The trace automatically collects and concatenates the streamed output for display in the span UI.

```python
stream = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[{"role": "user", "content": "Explain the benefits of using Databricks Foundation Models"}],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Function Calling

[MLflow Tracing](/concepts/mlflow-tracing.md) captures function call requests and results. Use the `@mlflow.trace` decorator to instrument tool functions with a dedicated span.

```python
from [[mlflow|MLflow]].entities import SpanType

@mlflow.trace(span_type=SpanType.TOOL)
def get_weather(city: str) -> str:
    if city == "Paris":
        return "rainy"
    return "unknown"

# Then define a tool-calling agent with @mlflow.trace(span_type=SpanType.AGENT)
# The agent invokes the model with tools, processes tool calls, and returns the final answer.
```

The trace UI highlights the function instructions and includes the tool execution span. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Supported APIs

[Automatic Tracing](/concepts/automatic-tracing.md) is currently supported for:

- Chat completions
- Streaming
- Function calling

For other API types (e.g., embeddings, completions), submit a feature request on the [MLflow](/concepts/mlflow.md) GitHub repository](https://github.com/[MLflow](/concepts/mlflow.md)/[MLflow](/concepts/mlflow.md)/issues). ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Available Models

Databricks Foundation Models provides access to a range of state-of-the-art models including Llama, Anthropic, and others. For the latest list of model IDs, see the Databricks Foundation Models documentation.

## Disabling Auto-Tracing

To disable tracing globally:

```python
[[mlflow|MLflow]].openai.autolog(disable=True)
# or
[[mlflow|MLflow]].autolog(disable=True)
```

^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying tracing framework.
- Databricks Foundation Models – The [Model Serving](/concepts/model-serving.md) endpoints being traced.
- [MLflow Autologging](/concepts/mlflow-autologging.md) – Mechanism for automatic trace capture.
- OpenAI API – The API protocol used by Databricks Foundation Models.
- [Function Calling](/concepts/llm-function-calling.md) – Advanced pattern supported in [Traces](/concepts/traces.md).
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The destination for logged [Traces](/concepts/traces.md).
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Compute where explicit `autolog()` is required.

## Sources

- tracing-databricks-foundation-models-databricks-on-aws.md

# Citations

1. [tracing-databricks-foundation-models-databricks-on-aws.md](/references/tracing-databricks-foundation-models-databricks-on-aws-5051d97b.md)
