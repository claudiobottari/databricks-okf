---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2966c784f63f313805eefd2312154650017545f12d785d22aa11021e72d3c3f
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
    - tracing-agno-databricks-on-aws.md
    - tracing-pydanticai-databricks-on-aws.md
    - tracing-semantic-kernel-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - token-usage-tracking-in-mlflow-traces
    - TUTIMT
  citations:
    - file: access-trace-data-databricks-on-aws.md
    - file: tracing-agno-databricks-on-aws.md
    - file: tracing-pydanticai-databricks-on-aws.md
    - file: tracing-semantic-kernel-databricks-on-aws.md
title: Token Usage Tracking in MLflow Traces
description: Mechanism for tracking LLM token consumption via aggregated token counts (input, output, total) derived from provider APIs and span-level attributes.
tags:
  - mlflow
  - tracing
  - token-usage
  - llm
timestamp: "2026-06-19T21:57:23.282Z"
---

# Token Usage Tracking in MLflow Traces

**Token Usage Tracking in MLflow Traces** refers to the ability to record and query the number of input and output tokens consumed by large language model (LLM) calls during a traced execution. [MLflow Tracing](/concepts/mlflow-tracing.md) automatically captures token counts returned by LLM provider APIs and surfaces them both at the individual span level and as aggregated totals on the trace object. ^[access-trace-data-databricks-on-aws.md, tracing-agno-databricks-on-aws.md, tracing-pydanticai-databricks-on-aws.md, tracing-semantic-kernel-databricks-on-aws.md]

## How Token Usage Is Stored

### Span-Level Usage

For each LLM call, token usage is stored as a span attribute. The primary attribute key is `mlflow.chat.tokenUsage`, whose value is a dictionary containing `input_tokens`, `output_tokens`, and `total_tokens`. This attribute is recorded by the [MLflow Tracing](/concepts/mlflow-tracing.md) integrations for Agno, PydanticAI, and Semantic Kernel. ^[tracing-agno-databricks-on-aws.md, tracing-pydanticai-databricks-on-aws.md, tracing-semantic-kernel-databricks-on-aws.md]

Some providers or versions may also store token counts as individual span attributes under the keys `llm.token_usage.input_tokens` and `llm.token_usage.output_tokens`. Both representations can coexist on the same span depending on the provider’s response format. ^[access-trace-data-databricks-on-aws.md]

### Trace-Level Aggregation

The total token usage across all LLM calls in a trace is aggregated and exposed via `trace.info.token_usage`. This property returns a dictionary with keys `input_tokens`, `output_tokens`, and `total_tokens`. Aggregated totals are available starting in MLflow 3.2.0. ^[access-trace-data-databricks-on-aws.md, tracing-pydanticai-databricks-on-aws.md, tracing-semantic-kernel-databricks-on-aws.md]

## Accessing Token Usage

### From a Trace Object

```python
token_usage = trace.info.token_usage
if token_usage:
    print(f"Input tokens: {token_usage['input_tokens']}")
    print(f"Output tokens: {token_usage['output_tokens']}")
    print(f"Total tokens: {token_usage['total_tokens']}")
```

^[access-trace-data-databricks-on-aws.md]

### From Individual Spans

```python
for span in trace.data.spans:
    if usage := span.get_attribute("mlflow.chat.tokenUsage"):
        print(f"{span.name}:")
        print(f"  Input tokens: {usage['input_tokens']}")
        print(f"  Output tokens: {usage['output_tokens']}")
        print(f"  Total tokens: {usage['total_tokens']}")
```

^[tracing-agno-databricks-on-aws.md, tracing-pydanticai-databricks-on-aws.md, tracing-semantic-kernel-databricks-on-aws.md]

Alternatively, if the span uses the legacy attribute keys:

```python
input_tokens = span.get_attribute("llm.token_usage.input_tokens")
output_tokens = span.get_attribute("llm.token_usage.output_tokens")
```

^[access-trace-data-databricks-on-aws.md]

## Provider Support

Token tracking relies on the LLM provider returning token counts in its API response. The method used to track tokens varies by provider. Supported providers include OpenAI, Anthropic, Google Gemini, and others that expose token metadata. MLflow's tracing integrations with Agno, PydanticAI, and Semantic Kernel all capture token usage automatically when autologging is enabled. ^[tracing-agno-databricks-on-aws.md, tracing-pydanticai-databricks-on-aws.md, tracing-semantic-kernel-databricks-on-aws.md]

For providers that do not return token counts, the token usage fields will be empty or absent.

## Framework Integrations

The following [MLflow Autologging](/concepts/mlflow-autologging.md) integrations record token usage as part of their tracing:

- **Agno**: `mlflow.agno.autolog()` — logs token usage per agent call to `mlflow.chat.tokenUsage`. ^[tracing-agno-databricks-on-aws.md]
- **PydanticAI**: `mlflow.pydantic_ai.autolog()` — MLflow 3.2.0+ records token usage totals in trace info and per call in span attributes. ^[tracing-pydanticai-databricks-on-aws.md]
- **Semantic Kernel**: `mlflow.semantic_kernel.autolog()` — same behavior as PydanticAI. ^[tracing-semantic-kernel-databricks-on-aws.md]

All three integrations store per-span token usage under the key `mlflow.chat.tokenUsage` and provide aggregated totals via `trace.info.token_usage`.

## Example: Accessing Token Usage After a Trace

```python
import mlflow

# Get the trace from the last active session
last_trace_id = mlflow.get_last_active_trace_id()
trace = mlflow.get_trace(trace_id=last_trace_id)

# Aggregated usage
total_usage = trace.info.token_usage
print("== Total token usage ==")
print(f"  Input tokens: {total_usage['input_tokens']}")
print(f"  Output tokens: {total_usage['output_tokens']}")
print(f"  Total tokens: {total_usage['total_tokens']}")

# Per-call (span) usage
print("\n== Detailed usage for each LLM call ==")
for span in trace.data.spans:
    if usage := span.get_attribute("mlflow.chat.tokenUsage"):
        print(f"{span.name}:")
        print(f"  Input tokens: {usage['input_tokens']}")
        print(f"  Output tokens: {usage['output_tokens']}")
        print(f"  Total tokens: {usage['total_tokens']}")
```

^[tracing-agno-databricks-on-aws.md, tracing-pydanticai-databricks-on-aws.md]

## Requirements

- **MLflow 3.2.0 or later** is required for aggregated token totals in `trace.info.token_usage`. Span-level attributes (`mlflow.chat.tokenUsage`) are available in earlier MLflow 3.x versions but may vary by provider. ^[tracing-pydanticai-databricks-on-aws.md, tracing-semantic-kernel-databricks-on-aws.md]
- Autologging must be explicitly enabled for the relevant framework integration (e.g., `mlflow.agno.autolog()`); it is not automatically enabled on serverless compute clusters. ^[tracing-agno-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] — The core tracing infrastructure in MLflow 3.
- [Span Attributes](/concepts/span-attributes-and-search.md) — Custom key-value metadata stored on spans.
- Agno Integration — Tracing and token tracking for the Agno agent framework.
- PydanticAI Integration — Tracing and token tracking for PydanticAI.
- Semantic Kernel Integration — Tracing and token tracking for Semantic Kernel.
- [Accessing Trace Data](/concepts/trace-data-export-and-conversion.md) — Full guide to reading trace metadata, spans, and assessments.

## Sources

- access-trace-data-databricks-on-aws.md
- tracing-agno-databricks-on-aws.md
- tracing-pydanticai-databricks-on-aws.md
- tracing-semantic-kernel-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
2. [tracing-agno-databricks-on-aws.md](/references/tracing-agno-databricks-on-aws-c7a8a057.md)
3. [tracing-pydanticai-databricks-on-aws.md](/references/tracing-pydanticai-databricks-on-aws-55f7c746.md)
4. [tracing-semantic-kernel-databricks-on-aws.md](/references/tracing-semantic-kernel-databricks-on-aws-b5fb97fc.md)
