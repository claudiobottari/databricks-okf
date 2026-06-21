---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc92275ebe9dbf094d963de144bed0e5a259a6dda50882557eae5f64bf14fc52
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-usage-tracking-in-tracing
    - TUTIT
  citations:
    - file: access-trace-data-databricks-on-aws.md
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: Token Usage Tracking in Tracing
description: MLflow Tracing can track token usage from LLM provider APIs, exposing input_tokens, output_tokens, and total_tokens via trace metadata and span attributes.
tags:
  - mlflow
  - token-usage
  - llm
timestamp: "2026-06-18T10:38:33.702Z"
---

# Token Usage Tracking in Tracing

**Token usage tracking** is a capability in [MLflow Tracing](/concepts/mlflow-tracing.md) that captures the number of input, output, and total tokens consumed during LLM calls. Token counts are obtained from the token counters returned by LLM provider APIs and are accessible through trace metadata and span attributes.

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) can automatically track token usage for LLM calls, using the token counts returned by the LLM provider's API. This enables monitoring of consumption, cost estimation, and optimization of GenAI applications. ^[access-trace-data-databricks-on-aws.md]

Token usage data is available at two levels:
- **Trace level**: Aggregated token usage across all spans in a trace
- **Span level**: Individual token usage for specific LLM or chat model spans

## Accessing Token Usage

### Trace-Level Token Usage

The aggregated token usage for a trace can be accessed through the `token_usage` property on the `TraceInfo` object. This property returns a dictionary containing `input_tokens`, `output_tokens`, and `total_tokens` values when available. ^[access-trace-data-databricks-on-aws.md]

```python
# Get aggregated token usage (if available)
token_usage = trace.info.token_usage
if token_usage:
    print(f"Input tokens: {token_usage.get('input_tokens')}")
    print(f"Output tokens: {token_usage.get('output_tokens')}")
    print(f"Total tokens: {token_usage.get('total_tokens')}")
```

^[access-trace-data-databricks-on-aws.md]

### Span-Level Token Usage

Token usage per individual LLM call can be accessed through span attributes. For chat model spans, the token usage is stored under the `llm.token_usage` attribute key, with `input_tokens` and `output_tokens` sub-attributes. ^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.tracing.constant import SpanAttributeKey

# Get a chat model span
chat_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]

# Access token usage from span
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
output_tokens = chat_span.get_attribute("llm.token_usage.output_tokens")
print(f"Span token usage - Input: {input_tokens}, Output: {output_tokens}")
```

^[access-trace-data-databricks-on-aws.md]

The `SpanAttributeKey` class provides constants for accessing chat-specific attributes, including token counts, making it easier to retrieve this data programmatically. ^[access-trace-data-databricks-on-aws.md]

## How Token Tracking Works

The method for tracking token usage depends on the LLM provider being used. [MLflow Tracing](/concepts/mlflow-tracing.md) relies on the token counts that LLM provider APIs return as part of their response. Different providers may return token counts through different mechanisms — for example, some return them in the API response body, while others provide them through response headers or structured metadata. ^[access-trace-data-databricks-on-aws.md]

| Provider Type | Token Count Source |
|---|---|
| OpenAI-compatible APIs | Response body `usage` field |
| Other LLM providers | Provider-specific response fields |
| Databricks-hosted endpoints | Automatic via serving endpoint metadata |

## Integration with [MLflow Tracing](/concepts/mlflow-tracing.md)

Token usage tracking integrates with the broader [MLflow Tracing](/concepts/mlflow-tracing.md) framework. When [MLflow Tracing](/concepts/mlflow-tracing.md) is enabled — for example, through `mlflow.openai.autolog()` — token usage data is automatically captured for supported LLM providers. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md, access-trace-data-databricks-on-aws.md]

The captured token data can be used in conjunction with [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) for cost-aware evaluation, or analyzed alongside [Trace Assessments](/concepts/trace-assessments.md) to understand the relationship between token consumption and output quality. ^[access-trace-data-databricks-on-aws.md]

## Use Cases

- **Cost tracking**: Monitor token consumption across applications and users to estimate API costs
- **Performance optimization**: Identify spans with unusually high token usage that may indicate inefficiencies
- **Budget management**: Set thresholds and alert on excessive token consumption
- **Capacity planning**: Forecast token usage based on historical trace data
- **Comparative analysis**: Compare token efficiency across different models or prompt strategies

## Best Practices

- **Enable tracing early**: Use `mlflow.openai.autolog()` or equivalent to capture token usage from the start of development
- **Use span-level data for granularity**: Access token counts from individual spans to identify which components of an application consume the most tokens
- **Aggregate for reporting**: Use trace-level `token_usage` for summary dashboards and cost reports
- **Combine with assessments**: Correlate token usage with quality assessments to optimize the cost-quality trade-off

## Limitations

- Token usage tracking depends on the LLM provider returning token counts in their API response — not all providers support this
- Aggregated trace-level token usage may not be available for all trace types or providers
- Token counts reflect what the provider reports and may differ from client-side estimation

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that captures token usage
- [Trace Data Access](/concepts/tracedata.md) — How to access all aspects of trace data
- [Trace Assessments](/concepts/trace-assessments.md) — Evaluating quality alongside token usage
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Quantitative assessment of model outputs
- [Databricks-hosted LLM Serving](/concepts/databricks-hosted-llm-serving.md) — Inference endpoints with automatic token tracking
- [Span Attributes](/concepts/span-attributes-and-search.md) — Where token usage data is stored at the span level

## Sources

- access-trace-data-databricks-on-aws.md
- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
2. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
