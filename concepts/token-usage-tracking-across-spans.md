---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c956d2bb915dd1f2eb00ebfc0f0a80bd4e6c88993634c1db0440c3707cca0509
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-usage-tracking-across-spans
    - TUTAS
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Token usage tracking across spans
description: Method for tracking and aggregating LLM token usage (input, output, total tokens) across individual spans and spans of type CHAT_MODEL in MLflow traces.
tags:
  - mlflow
  - token-usage
  - cost-monitoring
  - genai-tracing
timestamp: "2026-06-18T12:14:39.965Z"
---

# Token Usage Tracking Across Spans

**Token usage tracking across spans** refers to the practice of recording and aggregating token consumption metrics — input tokens, output tokens, and total tokens — at the individual span level within a [GenAI Trace](/concepts/mlflow-genai-trace.md), enabling detailed cost analysis and performance monitoring of LLM-based applications.

## Overview

In [MLflow Tracing](/concepts/mlflow-tracing.md), token usage is tracked per span and can be aggregated across an entire trace to provide a complete picture of LLM consumption. This allows developers to identify which parts of a pipeline consume the most tokens, monitor cost, and detect anomalous usage patterns. ^[examples-analyzing-traces-databricks-on-aws.md]

## Recording Token Usage on Spans

Token usage is stored as attributes on spans that represent LLM calls, typically spans of type `CHAT_MODEL` or `LLM`. The standard attribute keys follow a convention using the prefix `llm.token_usage`:

- `llm.token_usage.input_tokens`
- `llm.token_usage.output_tokens`
- `llm.token_usage.total_tokens`

To record token usage on an active span, obtain the current span and set the relevant attributes:^[examples-analyzing-traces-databricks-on-aws.md]

```python
from mlflow.tracing import set_span_chat_tools

span = mlflow.get_current_active_span()
span.set_attribute("llm.token_usage.input_tokens", 150)
span.set_attribute("llm.token_usage.output_tokens", 75)
span.set_attribute("llm.token_usage.total_tokens", 225)
```

## Aggregating Token Usage Across Spans

When analyzing a trace, token usage can be collected from all LLM-related spans and summed to determine total consumption for the entire pipeline. The following example demonstrates how to aggregate token usage from spans of type `CHAT_MODEL`:^[examples-analyzing-traces-databricks-on-aws.md]

```python
total_input = 0
total_output = 0
for span in trace.data.spans:
    if span.span_type == SpanType.CHAT_MODEL:
        total_input += span.get_attribute("llm.token_usage.input_tokens") or 0
        total_output += span.get_attribute("llm.token_usage.output_tokens") or 0
```

## Token Usage in Trace Metadata

Token usage is also available at the trace level via `trace.info.token_usage`, which provides a summary dictionary with keys for `input_tokens`, `output_tokens`, and `total_tokens`. This is useful for quick inspection without iterating over individual spans.^[examples-analyzing-traces-databricks-on-aws.md]

```python
if tokens := trace.info.token_usage:
    print(f"Input: {tokens.get('input_tokens', 0)}")
    print(f"Output: {tokens.get('output_tokens', 0)}")
    print(f"Total: {tokens.get('total_tokens', 0)}")
```

## Reusable Utility: LLM Usage Summary

For production monitoring, a reusable utility class can aggregate LLM usage across all spans in a trace, providing a structured summary for cost tracking and performance analysis:^[examples-analyzing-traces-databricks-on-aws.md]

```python
class TraceAnalyzer:
    def get_llm_usage_summary(self):
        """Aggregate LLM usage across all spans."""
        usage = {
            "total_llm_calls": 0,
            "total_input_tokens": 0,
            "total_output_tokens": 0,
            "spans": []
        }
        for span in self.trace.data.spans:
            if span.span_type in [SpanType.CHAT_MODEL, "LLM"]:
                usage["total_llm_calls"] += 1
                input_tokens = span.get_attribute("llm.token_usage.input_tokens") or 0
                output_tokens = span.get_attribute("llm.token_usage.output_tokens") or 0
                usage["total_input_tokens"] += input_tokens
                usage["total_output_tokens"] += output_tokens
                usage["spans"].append({
                    "name": span.name,
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens
                })
        usage["total_tokens"] = usage["total_input_tokens"] + usage["total_output_tokens"]
        return usage
```

## Use Cases

- **Cost attribution**: Determine which spans or components of a pipeline contribute most to total token consumption.
- **Performance monitoring**: Track token usage trends over time to detect regressions or cost increases.
- **Bottleneck identification**: LLM spans with unusually high token counts may indicate inefficiencies in prompt construction or retrieval.
- **Auditing and compliance**: Record token usage data for downstream analysis in `[ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md)` or cost management systems.

## Best Practices

- **Record token usage consistently on all LLM spans** to ensure accurate aggregation. Every span that makes an LLM call should set `input_tokens`, `output_tokens`, and `total_tokens` attributes.
- **Use span type filtering** when aggregating to focus only on spans that consume tokens (e.g., `CHAT_MODEL` or `LLM` types).
- **Compare trace-level and span-level totals** to verify consistency; discrepancies may indicate missing token attributes on some spans.
- **Automate token tracking** by wrapping LLM calls with `@mlflow.trace(span_type=SpanType.CHAT_MODEL)` and setting token attributes immediately after the response is received.

## Related Concepts

- [GenAI Trace](/concepts/mlflow-genai-trace.md) — The structured record of an entire pipeline execution
- [Performance monitoring](/concepts/performance-monitoring-with-mlflow-traces.md) — Analyzing performance characteristics and identifying bottlenecks using traces
- Error monitoring — Monitoring and analyzing errors in production traces
- [Span Analysis](/concepts/span-search-and-analysis.md) — Detailed examination of individual spans within a trace
- [Trace Analyzer Utility](/concepts/traceanalyzer-reusable-utility-class.md) — Reusable class for comprehensive trace analysis

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
