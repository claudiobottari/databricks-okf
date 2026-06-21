---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7283ec2f1a78459f851d5baed1a13c1976879bb5bf58596c5eb05a6e6dd48e88
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-spans
    - Spans|Trace Span
    - Trace span types
    - Traces and Spans
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Trace Spans
description: Immutable building blocks representing individual operations within a trace, with properties including span_id, name, type, timing, status, inputs/outputs, and parent-child relationships.
tags:
  - mlflow
  - tracing
  - spans
timestamp: "2026-06-18T14:17:51.627Z"
---

# Trace Spans

**Trace Spans** are the building blocks of [Traces](/concepts/traces.md) in [MLflow Tracing](/concepts/mlflow-tracing.md). Each span represents an individual operation or unit of work within a trace, such as an LLM call, a tool invocation, or a retrieval step. A trace is composed of multiple spans arranged in a parent-child hierarchy that captures the execution flow. ^[access-trace-data-databricks-on-aws.md]

## Accessing Spans

Spans are stored in the `TraceData` object of a trace. You can retrieve all spans from a trace using `trace.data.spans`, which returns a list of [`Span`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span) objects. You can also use `trace.search_spans()` to find spans matching specific criteria. ^[access-trace-data-databricks-on-aws.md]

```python
# Access all spans from a trace
spans = trace.data.spans
print(f"Total spans: {len(spans)}")
```

## Span Properties

Each `Span` object exposes the following key properties:

| Property | Description |
|---|---|
| `span_id` | Unique identifier for the span |
| `name` | Human-readable name of the operation |
| `span_type` | Type of operation (e.g., `CHAT_MODEL`, `TOOL`, `RETRIEVER`); see SpanType |
| `trace_id` | ID of the parent trace |
| `parent_id` | ID of the parent span; `None` for root spans |
| `start_time_ns` | Start time in nanoseconds |
| `end_time_ns` | End time in nanoseconds |
| `status` | Status code and description (e.g., `OK`, `ERROR`) |
| `inputs` | Input data to the operation |
| `outputs` | Output data from the operation |

^[access-trace-data-databricks-on-aws.md]

### Status Information

The `status` property returns a [`SpanStatus`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.SpanStatus) object with:
- `status_code`: e.g., `OK`, `ERROR`
- `description`: human-readable error description if applicable

^[access-trace-data-databricks-on-aws.md]

### Timing

Both `start_time_ns` and `end_time_ns` are in nanoseconds. To convert to milliseconds, subtract and divide by 1,000,000. ^[access-trace-data-databricks-on-aws.md]

```python
duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000
```

## Searching Spans

The `trace.search_spans()` method allows you to find spans by name (exact or regex), span type, or span ID. You can combine multiple criteria. ^[access-trace-data-databricks-on-aws.md]

```python
# Search by exact name
retriever_spans = trace.search_spans(name="retrieve_documents")

# Search by regex pattern
import re
tool_spans = trace.search_spans(name=re.compile(r".*_tool$"))

# Search by span type
chat_spans = trace.search_spans(span_type="CHAT_MODEL")

# Search by span ID
specific_span = trace.search_spans(span_id=some_id)
```

## Span Attributes

Spans can carry additional attributes beyond the core properties. Use `span.get_attribute(key)` or access `span.attributes` dictionary to retrieve them. Predefined keys are available via `SpanAttributeKey`, such as `CHAT_MESSAGES`, `CHAT_TOOLS`, and token usage values like `llm.token_usage.input_tokens`. ^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.tracing.constant import SpanAttributeKey

chat_span = trace.search_spans(span_type="CHAT_MODEL")[0]

# Access chat-specific attributes
messages = chat_span.get_attribute(SpanAttributeKey.CHAT_MESSAGES)
tools = chat_span.get_attribute(SpanAttributeKey.CHAT_TOOLS)

# Access token usage
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
```

## Intermediate Outputs

Non-root spans can expose their outputs as intermediate outputs of the trace. Access them via `trace.data.intermediate_outputs`, which returns a dictionary mapping span names to their outputs. ^[access-trace-data-databricks-on-aws.md]

```python
intermediate = trace.data.intermediate_outputs
if intermediate:
    for span_name, output in intermediate.items():
        print(f"  {span_name}: {output}")
```

## Advanced Span Operations

### Serialization

Spans can be converted to and from dictionaries using `span.to_dict()` and `Span.from_dict()`. The entire trace can be similarly serialized with `trace.to_dict()` and `Trace.from_dict()`. ^[access-trace-data-databricks-on-aws.md]

```python
# Convert span to dictionary
span_dict = span.to_dict()

# Recreate span from dictionary
from mlflow.entities import Span
reconstructed_span = Span.from_dict(span_dict)
```

### Span Tree Analysis

You can analyze the span hierarchy by building parent-child relationships. A common use case is identifying the critical path (longest duration path from root to leaf) and computing statistics per span type. The source material provides a reference implementation for `analyze_span_tree()`. ^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [Traces](/concepts/traces.md) — The container for spans, representing a full execution
- [TraceData](/concepts/tracedata.md) — The component that holds spans and request/response data
- SpanType — Enum defining span categories (CHAT_MODEL, TOOL, RETRIEVER, etc.)
- [Span Attributes](/concepts/span-attributes-and-search.md) — Custom and predefined attributes attached to spans
- Token Usage — Token counts tracked on LLM spans
- [TraceInfo](/concepts/traceinfo.md) — Metadata about a trace, including tags and assessments

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
