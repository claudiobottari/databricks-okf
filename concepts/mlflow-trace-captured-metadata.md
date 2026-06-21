---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78ea726c6d39a13e5916f130cc649bb6e17d6011df8f59ae819dc20f0558bb6e
  pageDirectory: concepts
  sources:
    - tracing-databricks-foundation-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-captured-metadata
    - MTCM
  citations:
    - file: tracing-databricks-foundation-models-databricks-on-aws.md
title: MLflow Trace Captured Metadata
description: Information automatically captured by MLflow traces for Databricks Foundation Model calls including prompts, completions, latencies, model name/endpoint, temperature/max_tokens parameters, function calls, and exceptions.
tags:
  - mlflow
  - tracing
  - observability
  - metadata
timestamp: "2026-06-19T23:10:57.371Z"
---

## [[mlflow-trace|MLflow Trace]] Captured Metadata

**MLflow Trace Captured Metadata** refers to the set of information that [MLflow Tracing](/concepts/mlflow-tracing.md) automatically records when tracing Databricks Foundation Model calls. By enabling auto‑tracing with `mlflow.openai.autolog()`, [MLflow](/concepts/mlflow.md) captures detailed [Traces](/concepts/traces.md) for any Databricks Foundation Models invocation made through the OpenAI‑compatible API. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

### Captured Fields

When a Foundation Model call is traced, [MLflow](/concepts/mlflow.md) automatically captures the following metadata:

- **Prompts and completion responses** – the full input messages and the model’s generated output.
- **Latencies** – the round‑trip time for the API call.
- **Model name and endpoint** – the specific model ID (e.g., `databricks-llama-4-maverick`) and the serving endpoint used.
- **Additional parameters** – values such as `temperature` and `max_tokens` when they are explicitly provided in the request.
- **Function calling** – if the model returns function calls as part of its response, the function name, arguments, and results are captured.
- **Exceptions** – any exception raised during the invocation is recorded in the trace.

^[tracing-databricks-foundation-models-databricks-on-aws.md]

### Streaming Support

[MLflow Tracing](/concepts/mlflow-tracing.md) also supports the streaming API of Databricks Foundation Models. When streaming is enabled (`stream=True`), [MLflow](/concepts/mlflow.md) automatically [Traces](/concepts/traces.md) the streaming response and renders the concatenated output in the span UI. The same captured metadata (prompts, latencies, model info, parameters, and exceptions) applies to streaming calls. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

### Function Calling Details

When a function calling response is returned, [MLflow Tracing](/concepts/mlflow-tracing.md) highlights the function instruction in the trace UI. Additionally, users can use the `@mlflow.trace` decorator on tool functions to create a dedicated span (with `SpanType.TOOL`) for the tool’s execution. This enables full observability into the agent’s reasoning and tool‑use steps. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

### How to Enable Auto‑Tracing

Auto‑tracing for Databricks Foundation Models is enabled by calling `mlflow.openai.autolog()`. On serverless compute clusters, this must be done explicitly; it is not enabled by default. After calling this function, every subsequent invocation of the OpenAI‑compatible API (with the Databricks endpoint) is traced automatically. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

### Disabling Auto‑Tracing

To disable auto‑tracing globally, call `mlflow.openai.autolog(disable=True)` or `mlflow.autolog(disable=True)`. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Databricks Foundation Models
- [OpenAI-compatible API](/concepts/openai-compatible-api-interface.md)
- [mlflow.openai.autolog()](/concepts/mlflowopenaiautolog.md)
- SpanType
- [MLflow Experiments](/concepts/mlflow-experiment.md)

### Sources

- tracing-databricks-foundation-models-databricks-on-aws.md

# Citations

1. [tracing-databricks-foundation-models-databricks-on-aws.md](/references/tracing-databricks-foundation-models-databricks-on-aws-5051d97b.md)
