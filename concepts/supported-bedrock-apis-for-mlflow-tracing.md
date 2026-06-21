---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 213c54073a5b3d53118dcb42a2d5230e9a1fd7a097ed6b73dd452652b5667912
  pageDirectory: concepts
  sources:
    - tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-bedrock-apis-for-mlflow-tracing
    - SBAFMT
  citations:
    - file: tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
title: Supported Bedrock APIs for MLflow Tracing
description: "MLflow supports auto-tracing for four Bedrock APIs: converse, converse_stream, invoke_model, and invoke_model_with_response_stream."
tags:
  - bedrock
  - api
  - mlflow
timestamp: "2026-06-19T23:08:54.808Z"
---

# Supported Bedrock APIs for [MLflow Tracing](/concepts/mlflow-tracing.md)

**Supported Bedrock APIs for [MLflow](/concepts/mlflow.md) Tracing** refers to the specific Amazon Bedrock Runtime API methods that [MLflow](/concepts/mlflow.md) can automatically trace when the `mlflow.bedrock.autolog()` function is enabled. [MLflow](/concepts/mlflow.md) captures [Traces](/concepts/traces.md) for LLM invocations made through these APIs and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Supported API Methods

[MLflow](/concepts/mlflow.md) supports [Automatic Tracing](/concepts/automatic-tracing.md) for the following Amazon Bedrock Runtime APIs from the Boto3 SDK: ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

- **`converse`** — Sends a message to a model and receives a response. This API supports a rich chat-like UI display in the [[mlflow-trace|MLflow Trace]] UI. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]
- **`converse_stream`** — Sends a message to a model and receives a streaming response. The aggregated output message is displayed in the Chat tab, while individual chunks appear in the Events tab. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]
- **`invoke_model`** — Invokes a model with a given prompt and configuration. [Traces](/concepts/traces.md) for this API display raw inputs and outputs rather than a chat-like interface. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]
- **`invoke_model_with_response_stream`** — Invokes a model with streaming response support. [Traces](/concepts/traces.md) display raw inputs and outputs. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Captured Information

For all supported APIs, [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) automatically capture the following data: ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

- Prompts and completion responses
- Latencies
- Model name
- Additional metadata such as `temperature`, `max_tokens` (if specified)
- Function calling details if returned in the response
- Any exceptions that are raised

## Chat Tab Support

The rich chat-like UI in the **Chat** tab is only supported for the `converse` and `converse_stream` APIs. For `invoke_model` and `invoke_model_with_response_stream`, [MLflow](/concepts/mlflow.md) displays only the **Inputs / Outputs** tab. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Streaming Behavior

When using streaming APIs, [MLflow](/concepts/mlflow.md) does not create a span immediately when the streaming response is returned. Instead, it creates the span only when the streaming chunks are **consumed** in a loop. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Amazon Bedrock, install [MLflow](/concepts/mlflow.md) with Databricks extras and the AWS SDK for Python: ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" boto3
```

On serverless compute clusters, autologging is not automatically enabled; you must explicitly call `mlflow.bedrock.autolog()` to enable tracing. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The general tracing framework for capturing LLM invocation details.
- [MLflow Autologging](/concepts/mlflow-autologging.md) — The mechanism that automatically captures [Traces](/concepts/traces.md) without manual instrumentation.
- Amazon Bedrock — AWS's managed service providing foundation models from leading AI providers.
- [Function Calling Agent Tracing](/concepts/mlflow-function-calling-agent-tracing.md) — Combining auto-tracing with manual `@mlflow.trace` decorators for agent workflows.
- Boto3 SDK — AWS SDK for Python used to invoke Bedrock APIs.

## Sources

- tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md

# Citations

1. [tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md](/references/tracing-amazon-bedrock-with-mlflow-databricks-on-aws-2f3942c6.md)
