---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce8fecd4bae1c5c917e714e808d41dce49a1632996d31daf58409a42d35098c1
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-token-usage-tracking
    - MTUT
    - Token Usage Tracking
    - Token Consumption Tracking
    - Token Usage Analytics
    - Token usage
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: MLflow Token Usage Tracking
description: Mechanism for tracking token consumption in LLM calls within traces, aggregating input_tokens, output_tokens, and total_tokens from provider APIs at both trace and span level.
tags:
  - mlflow
  - tracing
  - llm
  - tokens
timestamp: "2026-06-19T08:50:30.290Z"
---

# MLflow Token Usage Tracking

**MLflow Token Usage Tracking** refers to the capability within [MLflow Tracing](/concepts/mlflow-tracing.md) to capture and report token consumption metrics for LLM calls. This feature enables developers to monitor the cost and efficiency of language model invocations by recording input, output, and total token counts returned by LLM provider APIs.

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) can automatically track token usage of LLM calls using token counts returned by LLM provider APIs. This information is stored as part of the trace metadata and can be accessed programmatically for analysis, cost tracking, and optimization. ^[access-trace-data-databricks-on-aws.md]

## Accessing Token Usage Data

Token usage information is available through the `TraceInfo` object's `token_usage` property. This returns a dictionary containing the token counts if the LLM provider returns them. ^[access-trace-data-databricks-on-aws.md]

```python
# Get aggregated token usage (if available)
token_usage = trace.info.token_usage
if token_usage:
    print(f"Input tokens: {token_usage.get('input_tokens')}")
    print(f"Output tokens: {token_usage.get('output_tokens')}")
    print(f"Total tokens: {token_usage.get('total_tokens')}")
```

## Provider-Specific Tracking

The method for tracking token usage depends on the LLM provider. Different providers and platforms return token counts in different ways, and [MLflow Tracing](/concepts/mlflow-tracing.md) adapts to these variations. ^[access-trace-data-databricks-on-aws.md]

## Span-Level Token Access

Token usage can also be accessed at the individual span level, which is useful for analyzing token consumption for specific operations within a trace. ^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.tracing.constant import SpanAttributeKey

# Get a chat model span
chat_span = trace.search_spans(span_type="CHAT_MODEL")[0]

# Access token usage from span
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
output_tokens = chat_span.get_attribute("llm.token_usage.output_tokens")
print(f"Span token usage - Input: {input_tokens}, Output: {output_tokens}")
```

## Use Cases

- **Cost monitoring**: Track total token consumption across all LLM calls to estimate API costs.
- **Performance optimization**: Identify spans or traces with unusually high token usage for optimization.
- **Budget management**: Set thresholds and alerts based on token consumption patterns.
- **Comparative analysis**: Compare token usage across different model versions or configurations.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing infrastructure that captures execution data including token usage.
- [Trace Data Access](/concepts/tracedata.md) — How to access all aspects of trace data including spans, assessments, and metadata.
- [Span Attributes](/concepts/span-attributes-and-search.md) — Additional metadata stored on spans, including token usage information.
- LLM Provider Integration — How MLflow integrates with different LLM providers for token tracking.

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
