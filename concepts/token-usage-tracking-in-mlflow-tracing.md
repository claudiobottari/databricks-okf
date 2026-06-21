---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74aeea167f651653ba5b6a9b85c1d06c12cfe17efb60fd2f8353a95000460925
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
    - tracing-haystack-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - token-usage-tracking-in-mlflow-tracing
    - TUTIMT
  citations:
    - file: access-trace-data-databricks-on-aws.md
    - file: tracing-haystack-databricks-on-aws.md
title: Token Usage Tracking in MLflow Tracing
description: Mechanism for tracking LLM token counts (input, output, total) within traces, with provider-specific methods for token tracking.
tags:
  - mlflow
  - tracing
  - llm
  - token-usage
timestamp: "2026-06-18T14:18:00.653Z"
---

Here is the wiki page for "Token Usage Tracking in [MLflow Tracing](/concepts/mlflow-tracing.md)".

---

## Token Usage Tracking in [MLflow Tracing](/concepts/mlflow-tracing.md)

**Token usage tracking** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that captures and makes visible the number of tokens consumed by [large language model](/concepts/large-language-models-llms-on-databricks.md) (LLM) calls during [trace](/concepts/traces.md) execution. Token counts—broken down into input tokens, output tokens, and total tokens—are returned by LLM provider APIs and automatically aggregated by MLflow into the trace metadata.

## How Token Usage Is Stored

Token usage is stored on the [TraceInfo](/concepts/traceinfo.md) object of a trace, specifically in the `token_usage` property. This property returns a dictionary with keys `input_tokens`, `output_tokens`, and `total_tokens` when the provider API returns those counts. ^[access-trace-data-databricks-on-aws.md]

```python
token_usage = trace.info.token_usage
if token_usage:
    print(f"Input tokens: {token_usage.get('input_tokens')}")
    print(f"Output tokens: {token_usage.get('output_tokens')}")
    print(f"Total tokens: {token_usage.get('total_tokens')}")
```

^[access-trace-data-databricks-on-aws.md]

## Per-Span Token Usage

For finer-grained analysis, token usage can also be retrieved at the span level using the `llm.token_usage` attribute keys. This allows you to see which specific LLM call within a multi-step agent pipeline consumed the most tokens. ^[access-trace-data-databricks-on-aws.md]

```python
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
output_tokens = chat_span.get_attribute("llm.token_usage.output_tokens")
```

^[access-trace-data-databricks-on-aws.md]

## Provider-Specific Tracking

How token usage is tracked depends on the LLM provider. The following table describes different methods for tracking token usage across various providers and platforms. ^[access-trace-data-databricks-on-aws.md]

| Provider | Tracking Method |
|----------|-----------------|
| OpenAI | Automatic via `response.usage` |
| Anthropic | Automatic via `message.usage` |
| Databricks | Automatic via AI Gateway |
| Custom providers | Manual via `mlflow.trace.set_trace_tag()` |

## Automatic Logging in Frameworks

When using MLflow Tracing with Haystack, MLflow version 3.4.0 or later automatically tracks token usage for Haystack pipelines. Token usage information includes input tokens, output tokens, and total tokens consumed during pipeline execution. ^[tracing-haystack-databricks-on-aws.md]

## Viewing Token Usage in the UI

Token usage details are displayed in the [MLflow Tracing](/concepts/mlflow-tracing.md) UI, allowing you to monitor and optimize your pipeline's performance and costs. ^[access-trace-data-databricks-on-aws.md, tracing-haystack-databricks-on-aws.md]

## Related Concepts

- [TraceInfo](/concepts/traceinfo.md) — The metadata object containing token usage information
- Span — The execution unit that can hold per-span token usage
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall tracing framework
- [Token Usage Analytics](/concepts/mlflow-token-usage-tracking.md) — Advanced analysis of token consumption patterns
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The GenAI evaluation framework that integrates with tracing

## Sources

- access-trace-data-databricks-on-aws.md
- tracing-haystack-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
2. [tracing-haystack-databricks-on-aws.md](/references/tracing-haystack-databricks-on-aws-174dcdf4.md)
