---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b8e69fd7de47c4f4fa60e3df15ea681c138c360ad755fd7396329c97e2ac7a1
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-usage-in-mlflow-traces
    - TUIMT
    - Token usage display in MLflow traces
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Token Usage in MLflow Traces
description: Mechanism for tracking LLM token consumption (input, output, total tokens) within trace metadata and individual span attributes.
tags:
  - mlflow
  - tracing
  - llm
  - tokens
timestamp: "2026-06-19T17:25:31.030Z"
---

---
title: Token Usage in MLflow Traces
summary: How token usage is tracked and accessed in MLflow traces, including aggregated trace-level counts and per-span breakdowns.
sources:
  - access-trace-data-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T16:00:00.000Z"
updatedAt: "2026-06-19T16:00:00.000Z"
tags:
  - mlflow
  - tracing
  - token-usage
aliases:
  - token-usage-in-mlflow-traces
  - TUIMT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Token Usage in MLflow Traces

**Token Usage in MLflow Traces** refers to the tracking and retrieval of token consumption metrics for LLM calls captured in [Trace](/concepts/traces.md) objects. [MLflow Tracing](/concepts/mlflow-tracing.md) can capture token counts returned by LLM provider APIs, making it possible to monitor input, output, and total tokens used during model inference. ^[access-trace-data-databricks-on-aws.md]

## Accessing Token Usage

### Trace-Level Aggregated Counts

The `TraceInfo` object provides a `.token_usage` property that returns a dictionary (or `None` if unavailable) containing aggregated token counts across all spans in the trace: ^[access-trace-data-databricks-on-aws.md]

```python
token_usage = trace.info.token_usage
if token_usage:
    print(f"Input tokens: {token_usage.get('input_tokens')}")
    print(f"Output tokens: {token_usage.get('output_tokens')}")
    print(f"Total tokens: {token_usage.get('total_tokens')}")
```

- **`input_tokens`** – total tokens in the prompt/request.
- **`output_tokens`** – total tokens in the completion/response.
- **`total_tokens`** – sum of input and output tokens.

### Span-Level Token Usage

For a finer-grained view, token usage can be retrieved from individual Span objects that represent LLM calls (``span_type == "CHAT_MODEL"`` or ``SpanType.LLM``). Use the span’s ``get_attribute()`` method with the key `"llm.token_usage.input_tokens"` or `"llm.token_usage.output_tokens"`: ^[access-trace-data-databricks-on-aws.md]

```python
chat_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
output_tokens = chat_span.get_attribute("llm.token_usage.output_tokens")
```

Span-level token attributes are only present on spans that correspond to LLM calls and whose provider returns token count information.

## Provider Dependence

Token availability and accuracy depend entirely on the LLM provider and the integration. MLflow captures the token counts that the provider API returns; if a provider does not expose token usage metadata, the trace-level `token_usage` will be `None` and span-level attributes will be absent. The MLflow documentation describes provider-specific methods for enabling token tracking. ^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [Trace](/concepts/traces.md) – The top-level object that aggregates spans and metadata, including token usage.
- Span – Individual operation within a trace; can carry per-call token counts.
- LLM Tracing – The broader MLflow feature for capturing LLM execution data.
- Token Usage – General concept of monitoring token consumption (cost, limits).
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organizational unit under which traces are stored.

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
