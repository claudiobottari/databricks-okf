---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1688f9d16fdc318d7d9dcf1ff168fdd32f9f03468ec508c220718b68785292ee
  pageDirectory: concepts
  sources:
    - tracing-gemini-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-gemini-autolog
    - MGA
    - Gemini Autologging
  citations:
    - file: tracing-gemini-databricks-on-aws.md
title: MLflow Gemini Autolog
description: Automatic MLflow tracing for Google Gemini SDK calls via mlflow.gemini.autolog(), capturing prompts, responses, latencies, model names, metadata, function calls, and exceptions.
tags:
  - mlflow
  - tracing
  - gemini
  - databricks
timestamp: "2026-06-19T23:11:41.745Z"
---

# [MLflow](/concepts/mlflow.md) Gemini Autolog

**MLflow Gemini Autolog** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that automatically captures [Traces](/concepts/traces.md) for calls made through the Google Gemini Python SDK. By enabling `mlflow.gemini.autolog()`, [MLflow](/concepts/mlflow.md) logs nested [Traces](/concepts/traces.md) to the active [MLflow Experiment](/concepts/mlflow-experiment.md) whenever Gemini SDK methods such as `generate_content`, `send_message`, or `embed_content` are invoked. ^[tracing-gemini-databricks-on-aws.md]

## Overview

When autologging is turned on, [MLflow](/concepts/mlflow.md) automatically captures the following information for each Gemini call:

- Prompts and completion responses
- Latencies
- Model name
- Additional metadata such as `temperature` and `max_tokens` (if specified)
- Function calling details (if returned in the response)
- Any exception that is raised

On serverless compute clusters, autologging is **not automatically enabled**. You must explicitly call `mlflow.gemini.autolog()` to activate [Automatic Tracing](/concepts/automatic-tracing.md) for the Gemini integration. ^[tracing-gemini-databricks-on-aws.md]

The integration currently supports tracing of **synchronous calls for text interactions only**. Async APIs are not traced, and full inputs may not be recorded for multi-modal inputs. ^[tracing-gemini-databricks-on-aws.md]

## Basic Usage

To enable Gemini autologging, import `mlflow` and call the `autolog` function before making any Gemini SDK calls. Configure [MLflow Tracking](/concepts/mlflow-tracking.md) with the Databricks URI and set an experiment to store the [Traces](/concepts/traces.md).

```python
import [[mlflow|MLflow]]
import google.genai as genai
import os

[[mlflow|MLflow]].gemini.autolog()

[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/gemini-demo")

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="gemini-1.5-flash", contents="The opposite of hot is"
)
```

After execution, a trace is logged to the experiment containing the request, response, latency, and model metadata. ^[tracing-gemini-databricks-on-aws.md]

## Multi-Turn Chat Interactions

[MLflow](/concepts/mlflow.md) also supports tracing multi-turn conversations using the Gemini chat API. Each `send_message` call in a chat session is traced independently, preserving the full conversation history in the trace.

```python
[[mlflow|MLflow]].gemini.autolog()
chat = client.chats.create(model='gemini-1.5-flash')
response = chat.send_message("In one sentence, explain how a computer works to a young child.")
print(response.text)
response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?")
print(response.text)
```

Both turns are captured as separate spans within the same trace. ^[tracing-gemini-databricks-on-aws.md]

## Embeddings

The Gemini autolog integration also supports the [Embeddings API](/concepts/embeddings-api.md). When you call `models.embed_content`, [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) the request and response.

```python
result = client.models.embed_content(
    model="text-embedding-004", contents="Hello world"
)
```

The embedding call is recorded in the active experiment. ^[tracing-gemini-databricks-on-aws.md]

## Disabling Auto-Tracing

Autologging can be disabled globally by calling either:

- `mlflow.gemini.autolog(disable=True)`
- `mlflow.autolog(disable=True)`

This stops further tracing of Gemini SDK calls. ^[tracing-gemini-databricks-on-aws.md]

## Limitations

- Only synchronous (blocking) Gemini SDK calls are traced; async API calls are not supported.
- For multi-modal inputs (e.g., images), the full input payload may not be recorded.
- On serverless compute, autologging is opt-in and must be explicitly enabled.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying tracing framework that captures and organizes trace data.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The destination where [Traces](/concepts/traces.md) are logged and can be visualized in the UI.
- Google Gemini – The generative AI model provider integrated via this autolog feature.
- [LLM Observability](/concepts/genai-observability.md) – The broader practice of monitoring and debugging AI application behavior.

## Sources

- tracing-gemini-databricks-on-aws.md

# Citations

1. [tracing-gemini-databricks-on-aws.md](/references/tracing-gemini-databricks-on-aws-52fc6461.md)
