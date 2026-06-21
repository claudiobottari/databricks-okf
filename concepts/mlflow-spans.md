---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3dcf4ef72432425acb12ebdfb59b80970fdd464bb13a4847b778ff020fc6f5ba
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-spans
    - MLflow Span
    - MLflow Span Types
    - MLflow span types
    - MLflow Span Types|MLflow span type
    - MLflow span type
    - Span (MLflow)|Span
    - mlflow.start_span()
    - span types
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: MLflow Spans
description: Building blocks of traces representing individual operations with properties like span_id, name, type, timing, status, inputs/outputs, and parent-child relationships.
tags:
  - mlflow
  - tracing
  - spans
timestamp: "2026-06-19T21:56:46.898Z"
---

# MLflow Spans

**MLflow Spans** are the fundamental building blocks of [[MLflow Trace]] objects. Each span represents an individual operation or unit of work within a trace, such as an LLM call, a tool invocation, or a retrieval step. Spans are immutable once created and are used to record the execution path of a GenAI application. ^[access-trace-data-databricks-on-aws.md]

## Span Properties

Every span exposes a set of properties that describe its identity, timing, and data:

- **span_id** – Unique identifier for the span.
- **name** – Human-readable name of the operation (e.g., `retrieve_documents`).
- **span_type** – Category of the operation, represented by the SpanType enum (e.g., `CHAT_MODEL`, `TOOL`, `RETRIEVER`).
- **trace_id** – The trace this span belongs to.
- **parent_id** – The ID of the parent span, or `None` for root spans.
- **start_time_ns** / **end_time_ns** – Timestamps in nanoseconds.
- **status** – A [SpanStatus](/concepts/spanstatus-api.md) object with a `status_code` and optional `description`.
- **inputs** / **outputs** – The input and output payloads of the operation.

^[access-trace-data-databricks-on-aws.md]

## Working with Spans

Spans are accessed from a `Trace` object via the `trace.data.spans` list or by using the convenience method `trace.search_spans()`. The `search_spans()` method supports filtering by:

- **name** – Exact name or a regex pattern.
- **span_type** – A `SpanType` value or its string representation.
- **span_id** – A specific span ID.
- Any combination of the above criteria.

^[access-trace-data-databricks-on-aws.md]

## Span Attributes

Attributes are key-value metadata attached to a span. They can be accessed through the `attributes` dictionary or by calling `span.get_attribute(key)`. For chat‑model spans, the SpanAttributeKey constants (e.g., `CHAT_MESSAGES`, `CHAT_TOOLS`) provide typed access to LLM‑specific information. Token usage is also stored as attributes with keys like `llm.token_usage.input_tokens`. ^[access-trace-data-databricks-on-aws.md]

## Advanced Operations

- **Serialization**: Spans can be converted to dictionaries using `span.to_dict()` and reconstructed with `Span.from_dict()`, enabling deep inspection or storage. ^[access-trace-data-databricks-on-aws.md]
- **Span tree analysis**: By examining parent‑child relationships, you can reconstruct the execution hierarchy, identify the critical path (the longest chain of spans), and compute per‑type timing statistics (e.g., total LLM time vs. retrieval time). This is useful for profiling and debugging. ^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace]] – The container that holds spans and trace metadata.
- SpanType – Enum classifying the kind of operation a span represents.
- SpanAttributeKey – Constants for accessing typed span attributes.
- Access trace data – Guide for retrieving and inspecting traces and spans programmatically.

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
