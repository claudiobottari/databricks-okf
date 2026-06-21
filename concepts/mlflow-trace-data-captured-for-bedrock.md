---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5091c84d3066e426051322b2425a295c8f909a735883a711fe428ba644b11adf
  pageDirectory: concepts
  sources:
    - tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-data-captured-for-bedrock
    - MTDCFB
  citations:
    - file: tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
title: MLflow Trace Data Captured for Bedrock
description: MLflow automatically captures prompts, completion responses, latencies, model names, metadata (temperature, max_tokens), function calling info, and exceptions from Amazon Bedrock API calls.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T23:08:48.879Z"
---

# [[mlflow-trace|MLflow Trace]] Data Captured for Bedrock

**MLflow Trace Data Captured for Bedrock** refers to the set of metadata, inputs, outputs, and execution details that [MLflow](/concepts/mlflow.md) automatically captures and logs when Tracing Amazon Bedrock with MLflow is enabled. When auto tracing is activated via `mlflow.bedrock.autolog()`, [MLflow](/concepts/mlflow.md) records structured trace data for every Amazon Bedrock invocation and associates it with the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Captured Information

[MLflow](/concepts/mlflow.md) automatically captures the following information about Amazon Bedrock API calls: ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

- **Prompts and completion responses** — The full input messages sent to the model and the generated output.
- **Latencies** — The time taken for each Bedrock API invocation.
- **Model name** — The identifier of the foundation model used (e.g., `anthropic.claude-3-5-sonnet-20241022-v2:0`).
- **Inference configuration** — Metadata such as `temperature`, `maxTokens`, and `topP`, if specified in the request.
- **Function calling** — Tool call requests and results, including function names, input arguments, and tool use IDs, when returned in the response.
- **Exceptions** — Any errors or exceptions raised during the invocation.

## Trace Visualization

The captured trace data is displayed in the [MLflow](/concepts/mlflow.md) UI with different tabs depending on the API used: ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

- **Chat tab** — For the `converse` and `converse_stream` APIs, [MLflow](/concepts/mlflow.md) renders a rich chat-like view showing the conversation messages and function calling metadata in a human-readable format.
- **Inputs / Outputs tab** — Shows the raw input and output payloads, including configuration parameters. This tab is available for all supported APIs.
- **Events tab** — For streaming calls (`converse_stream`, `invoke_model_with_response_stream`), individual response chunks are displayed in the Events tab, while the aggregated output appears in the Chat tab.

## Streaming Behavior

For streaming Bedrock API calls, [MLflow](/concepts/mlflow.md) does not create a trace span immediately when the streaming response is returned. Instead, it creates the span when the streaming chunks are **consumed** — for example, when iterating through the stream in a for-loop. The generated trace shows the complete aggregated output message in the Chat tab. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Function Calling Agent [Traces](/concepts/traces.md)

When [MLflow Tracing](/concepts/mlflow-tracing.md) is combined with [Manual Tracing](/concepts/manual-tracing.md) via the `@mlflow.trace` decorator, the captured data includes the full execution chain of a Function Calling Agent (ReAct). [MLflow](/concepts/mlflow.md) automatically resolves call chains and records execution metadata, including: ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

- Tool function definitions and their input schemas
- Tool invocation requests from the model
- Tool execution results returned to the model
- Subsequent model responses after receiving tool results

Each tool function decorated with `@mlflow.trace(span_type=SpanType.TOOL)` generates a separate span within the trace, and the overall agent execution is captured under an `AGENT` span type.

## Supported APIs

The following Amazon Bedrock Runtime APIs are supported for trace data capture: ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

- `converse`
- `converse_stream`
- `invoke_model`
- `invoke_model_with_response_stream`

## Related Concepts

- Tracing Amazon Bedrock with MLflow — Overview of enabling and using [MLflow Tracing](/concepts/mlflow-tracing.md) for Bedrock.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit where [Traces](/concepts/traces.md) are logged.
- [MLflow Autologging](/concepts/mlflow-autologging.md) — The mechanism that automatically captures trace data.
- [MLflow Span Types](/concepts/mlflow-spans.md) — The span categories used to structure trace data (e.g., `TOOL`, `AGENT`).
- MLflow Trace Visualization — How trace data is rendered in the [MLflow](/concepts/mlflow.md) UI.
- Amazon Bedrock — The managed service providing foundation models.

## Sources

- tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md

# Citations

1. [tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md](/references/tracing-amazon-bedrock-with-mlflow-databricks-on-aws-2f3942c6.md)
