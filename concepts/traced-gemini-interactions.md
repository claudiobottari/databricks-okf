---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c30ffede04cd39a361fc5150c5422ed8a87baff22d465a1b970ed46d897b012a
  pageDirectory: concepts
  sources:
    - tracing-gemini-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traced-gemini-interactions
    - TGI
  citations:
    - file: tracing-gemini-databricks-on-aws.md
title: Traced Gemini Interactions
description: "MLflow supports tracing multiple types of Gemini SDK interactions: synchronous text generation, multi-turn chat conversations, and embeddings API calls."
tags:
  - mlflow
  - tracing
  - gemini
  - llm
timestamp: "2026-06-19T23:11:43.391Z"
---

# Traced Gemini Interactions

**Traced Gemini Interactions** refers to the automatic capture and logging of Google Gemini model invocations using [MLflow Tracing](/concepts/mlflow-tracing.md) on the Databricks platform. By enabling auto tracing for the Gemini Python SDK, [MLflow](/concepts/mlflow.md) records detailed trace data for each call, including prompts, responses, latencies, model metadata, and exceptions, and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md).^[tracing-gemini-databricks-on-aws.md]

## Enabling [Automatic Tracing](/concepts/automatic-tracing.md)

To enable [Automatic Tracing](/concepts/automatic-tracing.md) for Gemini, call the `mlflow.gemini.autolog()` function before any Gemini SDK operations. This must be done explicitly; on serverless compute clusters, autologging is not automatically enabled. After calling `autolog()`, [MLflow](/concepts/mlflow.md) will capture [Traces](/concepts/traces.md) upon invocation of the Gemini Python SDK's synchronous `generate_content` method, chat interactions, and embedding requests.^[tracing-gemini-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].gemini.autolog()
```

## Captured Information

[[mlflow-trace|MLflow Trace]] automatically captures the following details about Gemini calls:^[tracing-gemini-databricks-on-aws.md]

- Prompts and completion responses
- Latencies (time taken for the call)
- Model name (e.g., `gemini-1.5-flash`)
- Additional metadata such as `temperature`, `max_tokens`, if specified
- Function calling if returned in the response
- Any exception if raised during the call

## Limitations

Currently, the [MLflow](/concepts/mlflow.md) Gemini integration only supports tracing of **synchronous calls for text interactions**. Async APIs are not traced, and full inputs may not be recorded for multi-modal inputs (e.g., images or audio).^[tracing-gemini-databricks-on-aws.md]

## Basic Example

The following example demonstrates a simple text generation call with auto tracing enabled:^[tracing-gemini-databricks-on-aws.md]

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

## Multi-turn Chat Interactions

[MLflow](/concepts/mlflow.md) also supports tracing multi-turn conversations with Gemini. Each `send_message` call in a chat session is captured as a separate trace, preserving the conversation context:^[tracing-gemini-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].gemini.autolog()

chat = client.chats.create(model='gemini-1.5-flash')
response = chat.send_message("In one sentence, explain how a computer works to a young child.")
print(response.text)
response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?")
print(response.text)
```

## Embeddings

The tracing integration also supports the [Embeddings API](/concepts/embeddings-api.md). When you call `client.models.embed_content`, [MLflow](/concepts/mlflow.md) captures the embedding request and response:^[tracing-gemini-databricks-on-aws.md]

```python
result = client.models.embed_content(model="text-embedding-004", contents="Hello world")
```

## Disabling Auto-tracing

Auto tracing for Gemini can be disabled globally by calling `mlflow.gemini.autolog(disable=True)` or by calling `mlflow.autolog(disable=True)`.^[tracing-gemini-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying framework that captures and organizes trace data.
- [Autologging](/concepts/mlflow-autologging.md) – The mechanism in [MLflow](/concepts/mlflow.md) for automatic instrumentation of libraries.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit where traced interactions are logged.
- Gemini SDK – The Python client library for accessing Google Gemini models.

## Sources

- tracing-gemini-databricks-on-aws.md

# Citations

1. [tracing-gemini-databricks-on-aws.md](/references/tracing-gemini-databricks-on-aws-52fc6461.md)
