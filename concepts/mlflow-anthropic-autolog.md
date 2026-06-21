---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 474b2f1e6bff164c41880bb90d40dab2bf8884da7c097dc1ed6b3c8dee82af45
  pageDirectory: concepts
  sources:
    - tracing-anthropic-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-anthropic-autolog
    - MAA
    - Anthropic API
    - MLflow Anthropic Integrations
  citations:
    - file: tracing-anthropic-databricks-on-aws.md
title: MLflow Anthropic Autolog
description: Automatic trace capture for Anthropic LLM SDK calls via mlflow.anthropic.autolog()
tags:
  - mlflow
  - tracing
  - anthropic
  - databricks
timestamp: "2026-06-19T23:09:12.062Z"
---

# [MLflow](/concepts/mlflow.md) Anthropic Autolog

**MLflow Anthropic Autolog** is an [Automatic Tracing](/concepts/automatic-tracing.md) capability provided by [MLflow Tracing](/concepts/mlflow-tracing.md)] for Anthropic large language models (LLMs). By calling `mlflow.anthropic.autolog()`, [MLflow](/concepts/mlflow.md) captures nested [Traces](/concepts/traces.md) of Anthropic Python SDK calls and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-anthropic-databricks-on-aws.md]

## Enabling Autolog

Autologging is enabled with a single function call:

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].anthropic.autolog()
```

On serverless compute clusters, autologging is not automatically enabled; you must explicitly call `mlflow.anthropic.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for this integration. ^[tracing-anthropic-databricks-on-aws.md]

## Captured Information

[[mlflow-trace|MLflow Trace]] automatically captures the following data from Anthropic calls:

- Prompts and completion responses
- Latencies
- Model name
- Additional metadata such as `temperature` and `max_tokens` (if specified)
- Function calling details (if returned in the response)
- Any raised exception

^[tracing-anthropic-databricks-on-aws.md]

## Limitations

- Currently, the [MLflow](/concepts/mlflow.md) Anthropic integration only supports tracing for synchronous calls for text interactions.
- Async APIs are not traced (though async support was added in [MLflow](/concepts/mlflow.md) 2.21.0 for certain endpoints – see Supported APIs below).
- Full inputs cannot be recorded for multi-modal inputs.

^[tracing-anthropic-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Anthropic, you need to install [MLflow](/concepts/mlflow.md) and the Anthropic SDK. [MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience. ^[tracing-anthropic-databricks-on-aws.md]

For development environments, install the full [MLflow](/concepts/mlflow.md) package with Databricks extras and `anthropic`:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" anthropic
```

For production, refer to the [secure API key management] guidelines using [AI Gateway](/concepts/ai-gateway.md) or Databricks secrets.

Before running examples, configure your environment:

- **Outside Databricks notebooks**: Set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables.
- **Inside Databricks notebooks**: These credentials are automatically set.
- **API Keys**: Set `ANTHROPIC_API_KEY`. For production, use [AI Gateway](/concepts/ai-gateway.md)] or [Databricks secrets].

^[tracing-anthropic-databricks-on-aws.md]

## Supported APIs

[MLflow](/concepts/mlflow.md) supports [Automatic Tracing](/concepts/automatic-tracing.md) for the following Anthropic APIs:

| API | Async Support | Notes |
|-----|---------------|-------|
| `client.messages.create` | Yes ([MLflow](/concepts/mlflow.md) ≥2.21.0) | Synchronous and async text interactions |

To request support for additional APIs, open a [feature request](https://github.com/[MLflow](/concepts/mlflow.md)/[MLflow](/concepts/mlflow.md)/issues) on GitHub.

^[tracing-anthropic-databricks-on-aws.md]

## Basic Example

```python
import anthropic
import [[mlflow|MLflow]]
import os

# Enable auto-tracing for Anthropic
[[mlflow|MLflow]].anthropic.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] to Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/anthropic-tracing-demo")

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
```

^[tracing-anthropic-databricks-on-aws.md]

## Async Support

For asynchronous calls, use `AsyncAnthropic`:

```python
client = anthropic.AsyncAnthropic()
response = await client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
```

Note that async tracing requires [MLflow](/concepts/mlflow.md) 2.21.0 or later. ^[tracing-anthropic-databricks-on-aws.md]

## Tool Calling with Tracing

[MLflow Tracing](/concepts/mlflow-tracing.md) automatically captures tool calling responses from Anthropic models. The function instruction in the response is highlighted in the trace UI. You can annotate a tool function with the `@mlflow.trace` decorator (using `SpanType.TOOL`) to create a separate span for the tool execution. ^[tracing-anthropic-databricks-on-aws.md]

A typical tool-calling agent pattern involves:

1. Defining the tool function decorated with `@mlflow.trace(span_type=SpanType.TOOL)`.
2. Invoking the model with `tools` specified.
3. Processing `tool_use` content blocks and invoking the corresponding function.
4. Sending tool results back to the model.

The entire agent workflow can be wrapped with `@mlflow.trace(span_type=SpanType.AGENT)` to capture the full chain. ^[tracing-anthropic-databricks-on-aws.md]

## Disabling Autolog

Auto tracing for Anthropic can be disabled globally by calling:

```python
[[mlflow|MLflow]].anthropic.autolog(disable=True)
```

or

```python
[[mlflow|MLflow]].autolog(disable=True)
```

^[tracing-anthropic-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying tracing framework.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Where [Traces](/concepts/traces.md) are logged.
- Anthropic SDK – The SDK being traced.
- [AI Gateway](/concepts/ai-gateway.md) – For secure API key management.
- Databricks Secrets – For storing API keys securely.
- SpanType – Enumerations for span categories (TOOL, AGENT).
- [OpenAI Autolog](/concepts/mlflow-openai-autologging.md) – Similar autologging for OpenAI models.

## Sources

- tracing-anthropic-databricks-on-aws.md

# Citations

1. [tracing-anthropic-databricks-on-aws.md](/references/tracing-anthropic-databricks-on-aws-085cde5b.md)
