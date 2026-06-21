---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 76f5c294d5064f11e1722aa5efb1fa152849e6c24d26ac2bf5ade830e930805f
  pageDirectory: concepts
  sources:
    - tracing-anthropic-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-captured-data-for-anthropic
    - MTCDFA
  citations:
    - file: tracing-anthropic-databricks-on-aws.md
title: MLflow Trace Captured Data for Anthropic
description: The specific telemetry automatically captured by MLflow Traces from Anthropic SDK calls, including prompts, responses, latencies, model names, metadata, function calls, and exceptions
tags:
  - mlflow
  - tracing
  - telemetry
  - anthropic
timestamp: "2026-06-19T23:09:03.798Z"
---

## [[mlflow-trace|MLflow Trace]] Captured Data for Anthropic

When [MLflow Tracing](/concepts/mlflow-tracing.md)] is enabled for the [Anthropic] Python SDK via `mlflow.anthropic.autolog()`, every invocation of a supported Anthropic API method is automatically recorded as a trace. The trace is logged to the active [MLflow Experiment](/concepts/mlflow-experiment.md) and captures a specific set of data fields about the request, response, and execution. ^[tracing-anthropic-databricks-on-aws.md]

### Captured Data Fields

[MLflow](/concepts/mlflow.md) automatically captures the following information for each traced Anthropic call:

* **Prompts and completion responses** – The full input messages sent to the model and the generated response content. ^[tracing-anthropic-databricks-on-aws.md]
* **Latencies** – The time taken for the API call to complete. ^[tracing-anthropic-databricks-on-aws.md]
* **Model name** – The identifier of the Anthropic model used (e.g., `claude-3-5-sonnet-20241022`). ^[tracing-anthropic-databricks-on-aws.md]
* **Additional metadata** – Parameters such as `temperature` and `max_tokens` if they were specified in the request. ^[tracing-anthropic-databricks-on-aws.md]
* **Function calling** – If the response contains a tool call (`tool_use` content block), the function name and its input arguments are recorded. ^[tracing-anthropic-databricks-on-aws.md]
* **Exceptions** – Any exception raised during the API call is captured as part of the trace. ^[tracing-anthropic-databricks-on-aws.md]

### Supported APIs and Limitations

- [MLflow](/concepts/mlflow.md) supports tracing for synchronous calls via `client.messages.create`. ^[tracing-anthropic-databricks-on-aws.md]
- Async support (`AsyncAnthropic`) was added in [MLflow](/concepts/mlflow.md) 2.21.0. Earlier versions do not trace asynchronous calls. ^[tracing-anthropic-databricks-on-aws.md]
- Multi-modal inputs (e.g., images) cannot be fully recorded in the trace. ^[tracing-anthropic-databricks-on-aws.md]
- On serverless compute clusters, autologging is not enabled automatically; the user must explicitly call `mlflow.anthropic.autolog()`. ^[tracing-anthropic-databricks-on-aws.md]

### Tool Calling Trace Data

When a traced Anthropic call returns a tool-use response, the function instruction and its arguments are highlighted in the trace UI. Additionally, user-defined tool functions can be decorated with `@mlflow.trace(span_type=SpanType.TOOL)` to create a nested span that captures the tool’s execution details, including its input, output, and duration. ^[tracing-anthropic-databricks-on-aws.md]

Example (excerpt from source): ^[tracing-anthropic-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.TOOL)
async def get_weather(city: str) -> str:
    ...
```

### Disabling Auto-Tracing

Auto-tracing can be disabled globally by calling `mlflow.anthropic.autolog(disable=True)` or `mlflow.autolog(disable=True)`. ^[tracing-anthropic-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The tracing subsystem that records and visualizes LLM calls.
- [Autolog](/concepts/mlflow-autologging.md) – The mechanism that enables [Automatic Tracing](/concepts/automatic-tracing.md) without manual instrumentation.
- Span – A unit of work within a trace; tool execution can be captured as a child span.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The destination where [Traces](/concepts/traces.md) are logged.
- Anthropic SDK – The Python client library that is instrumented by [MLflow](/concepts/mlflow.md).
- [Tool Calling](/concepts/llm-function-calling.md) – Model capability to request execution of user‑defined functions.
- Latency Monitoring – Using trace timing data to monitor API performance.

### Sources

- tracing-anthropic-databricks-on-aws.md

# Citations

1. [tracing-anthropic-databricks-on-aws.md](/references/tracing-anthropic-databricks-on-aws-085cde5b.md)
