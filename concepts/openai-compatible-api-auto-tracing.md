---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b180bedb3b7e328333718315937fcb144e97155237c8637ffdfbcd7bff5fc053
  pageDirectory: concepts
  sources:
    - tracing-databricks-foundation-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - openai-compatible-api-auto-tracing
    - OAA
  citations:
    - file: tracing-databricks-foundation-models-databricks-on-aws.md
title: OpenAI-Compatible API Auto-Tracing
description: MLflow leverages the OpenAI SDK to automatically trace Databricks Foundation Model calls because these models expose an OpenAI-compatible API, enabling reuse of mlflow.openai.autolog().
tags:
  - mlflow
  - openai
  - api-compatibility
  - databricks
timestamp: "2026-06-19T23:10:53.716Z"
---

# OpenAI-Compatible API Auto-Tracing

**OpenAI-Compatible API Auto-Tracing** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that automatically captures trace data for calls made to any API that follows the OpenAI-compatible specification. This includes Databricks Foundation Models, which expose an OpenAI-compatible endpoint. By calling `mlflow.openai.autolog()`, [MLflow](/concepts/mlflow.md) automatically instruments the OpenAI SDK and logs detailed spans to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## How It Works

When `mlflow.openai.autolog()` is enabled, [MLflow](/concepts/mlflow.md) intercepts calls made through the OpenAI Python client (including those configured to talk to non-OpenAI endpoints) and records the following information:

- Prompts and completion responses
- Latencies
- Model name and endpoint URL
- Additional metadata such as `temperature` and `max_tokens`, if specified
- Function‑calling arguments and results, if returned in the response
- Any exception that is raised

^[tracing-databricks-foundation-models-databricks-on-aws.md]

The [Traces](/concepts/traces.md) are stored in the active [MLflow Experiment](/concepts/mlflow-experiment.md) and are visible in the [MLflow](/concepts/mlflow.md) UI. On serverless compute clusters, autologging is **not** enabled by default; you must explicitly call `mlflow.openai.autolog()` to turn it on. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Prerequisites

To use OpenAI-compatible API auto-tracing, install the [MLflow](/concepts/mlflow.md) package (≥3.1) with Databricks extras and the OpenAI SDK:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" openai
```

If you are running outside a Databricks notebook, set the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. Inside Databricks notebooks these credentials are already configured. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Supported APIs

[MLflow](/concepts/mlflow.md) supports auto‑tracing for the following OpenAI-compatible API patterns:

- Chat completions (non‑streaming and streaming)
- Function calling (tool use)

To request support for additional APIs, see the [MLflow](/concepts/mlflow.md) feature request page](https://github.com/[MLflow](/concepts/mlflow.md)/[MLflow](/concepts/mlflow.md)/issues). ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Usage Examples

### Basic Chat Completion

The following example enables auto‑tracing, sets up an OpenAI client pointed at a Databricks Foundation Models endpoint, and sends a chat completion request:

```python
import [[mlflow|MLflow]]
import os
from openai import OpenAI

[[mlflow|MLflow]].openai.autolog()
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/databricks-foundation-models-demo")

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

[MLflow](/concepts/mlflow.md) captures the prompt, response, latency, model name, and the `temperature`/`max_tokens` metadata.

### Streaming

Auto‑tracing also works with streaming responses. [MLflow](/concepts/mlflow.md) automatically concatenates the streamed content and renders it as a single output in the span UI:

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

### Function Calling

[MLflow](/concepts/mlflow.md) automatically captures function‑calling instructions and results in the trace. You can annotate tool functions with `@mlflow.trace` to create a separate span for each tool execution:

```python
@mlflow.trace(span_type=SpanType.TOOL)
def get_weather(city: str) -> str:
    # ...
    return "sunny"

# The OpenAI client call with tools=... is traced automatically
response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=messages,
    tools=tools,
)
```

^[tracing-databricks-foundation-models-databricks-on-aws.md]

For a full agent example that chains multiple tool calls, see the [function calling example](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/databricks-foundation-models).

## Disabling Auto-Tracing

To disable auto‑tracing globally, call:

```python
[[mlflow|MLflow]].openai.autolog(disable=True)
```

or

```python
[[mlflow|MLflow]].autolog(disable=True)
```

^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – MLflow’s framework for capturing LLM call [Traces](/concepts/traces.md).
- Databricks Foundation Models – The set of models served through a Databricks endpoint with an OpenAI‑compatible API.
- [OpenAI-Compatible API](/concepts/openai-compatible-api-interface.md) – API specification that Databricks Foundation Models implement.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The logical unit where [Traces](/concepts/traces.md) are logged.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Compute environment where autologging must be explicitly enabled.
- [Function Calling](/concepts/llm-function-calling.md) – A pattern where the model returns tool call instructions instead of a final text response.

## Sources

- tracing-databricks-foundation-models-databricks-on-aws.md

# Citations

1. [tracing-databricks-foundation-models-databricks-on-aws.md](/references/tracing-databricks-foundation-models-databricks-on-aws-5051d97b.md)
