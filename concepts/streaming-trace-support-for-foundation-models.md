---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd67db2beb52263d776ecb4442fb6a29cc0de2088f92a9b49b7eb344333d1784
  pageDirectory: concepts
  sources:
    - tracing-databricks-foundation-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-trace-support-for-foundation-models
    - STSFFM
  citations:
    - file: tracing-databricks-foundation-models-databricks-on-aws.md
title: Streaming Trace Support for Foundation Models
description: MLflow Tracing supports streaming API responses from Databricks Foundation Models, automatically capturing and rendering the concatenated streaming output in the span UI.
tags:
  - mlflow
  - tracing
  - streaming
  - databricks
timestamp: "2026-06-19T23:11:08.572Z"
---

---
title: Streaming Trace Support for Foundation Models
summary: [MLflow Tracing](/concepts/mlflow-tracing.md) support for streaming responses from Databricks Foundation Models, capturing prompts, chunks, and latencies in a trace span.
sources:
  - tracing-databricks-foundation-models-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00.000Z"
updatedAt: "2026-06-20T10:00:00.000Z"
tags:
  - [MLflow](/concepts/mlflow.md)
  - tracing
  - foundation-models
  - streaming
aliases:
  - streaming-trace-support-for-foundation-models
  - STSFM
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# Streaming Trace Support for Foundation Models

**Streaming Trace Support for Foundation Models** refers to the ability of [MLflow Tracing](/concepts/mlflow-tracing.md) to automatically capture and render trace data for streaming API calls made to Databricks Foundation Models. When a streaming response is used, [MLflow](/concepts/mlflow.md) automatically [Traces](/concepts/traces.md) the stream and displays the concatenated output in the span UI, providing end-to-end observability into the model invocation. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## How It Works

Databricks Foundation Models expose an OpenAI-compatible API. To enable [Automatic Tracing](/concepts/automatic-tracing.md), call `mlflow.openai.autolog()`. After this call, any chat completion request — including those with `stream=True` — is automatically traced. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

For streaming responses, [MLflow](/concepts/mlflow.md) captures:

- The full streaming request (prompts, model name, parameters such as `temperature` and `max_tokens`)
- The concatenated streaming output rendered in the span UI
- Latency of the entire streaming operation
- Model name and endpoint
- Any exceptions raised during streaming ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Example

The following example demonstrates streaming trace with Databricks Foundation Models using the OpenAI-compatible client:

```python
import [[mlflow|MLflow]]
import os
from openai import OpenAI

# Enable auto-tracing for OpenAI (which will trace Databricks Foundation Model API calls)
[[mlflow|MLflow]].openai.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] to Databricks if not already configured
# [[mlflow|MLflow]].set_tracking_uri("databricks")
# [[mlflow|MLflow]].set_experiment("/Shared/databricks-streaming-demo")

# Create OpenAI client configured for Databricks
client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

stream = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[
        {"role": "user", "content": "Explain the benefits of using Databricks Foundation Models"}
    ],
    stream=True,  # Enable streaming response
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

^[tracing-databricks-foundation-models-databricks-on-aws.md]

After running this code, the [MLflow](/concepts/mlflow.md) UI shows a trace span containing the concatenated streaming output along with metadata such as latency and model name. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Prerequisites

To use streaming trace support, install the following packages:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" openai
```

[MLflow 3](/concepts/mlflow-3.md) or later is recommended for the best tracing experience. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

When running outside a Databricks notebook, set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN`. Inside a Databricks notebook these credentials are automatically configured. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Important Notes

On serverless compute clusters, autologging is not automatically enabled. You must explicitly call `mlflow.openai.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for this integration. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Disabling Auto Tracing

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

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Databricks Foundation Models
- [OpenAI API Compatible Endpoints](/concepts/openai-compatible-api-interface.md)
- [Function Calling Trace Support](/concepts/function-calling-trace-integration.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- Serverless Compute

## Sources

- tracing-databricks-foundation-models-databricks-on-aws.md

# Citations

1. [tracing-databricks-foundation-models-databricks-on-aws.md](/references/tracing-databricks-foundation-models-databricks-on-aws-5051d97b.md)
