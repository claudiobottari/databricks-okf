---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bef115cc056075dd99f0a042681d026ef61fdcc675a7714f77a435af91a36645
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traceinfo-metadata
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: TraceInfo Metadata
description: TraceInfo contains metadata about a trace including trace ID, request/response previews, timing information, tags, trace metadata (immutable), token usage, assessments, and storage location.
tags:
  - mlflow
  - tracing
  - metadata
timestamp: "2026-06-19T13:52:00.045Z"
---

```markdown
---
title: TraceInfo Metadata
summary: TraceInfo contains trace ID, status (OK/ERROR/IN_PROGRESS), request/response previews, timing, tags, token usage, assessments, and storage location.
sources:
  - access-trace-data-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:37:54.496Z"
updatedAt: "2026-06-18T10:37:54.496Z"
tags:
  - mlflow
  - metadata
  - tracing
aliases:
  - traceinfo-metadata
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# TraceInfo Metadata

`TraceInfo` is a core component of the MLflow [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) object, containing metadata about an executed trace. It provides access to essential information such as trace identification, status, timing, tags, token usage, and assessments, without requiring the full execution data from `TraceData`. ^[access-trace-data-databricks-on-aws.md]

## Basic Metadata and Status

`TraceInfo` includes primary identifiers and status information for a trace. The `trace_id` is a unique string identifier, and `client_request_id` provides an optional client-specified identifier. The `state` field indicates the current status of the trace: `OK`, `ERROR`, or `IN_PROGRESS`. A deprecated `status` field also exists but users should use `state` instead. ^[access-trace-data-databricks-on-aws.md]

```python
print(f"Trace ID: {trace.info.trace_id}")
print(f"Client Request ID: {trace.info.client_request_id}")
print(f"State: {trace.info.state}")
```

## Preview Data

The `request_preview` and `response_preview` properties provide truncated summaries of the full request and response data, allowing quick understanding of what occurred without loading complete payloads. These previews are useful for rapid inspection during development and debugging. Users can compare preview length against full request data to understand the compression ratio. ^[access-trace-data-databricks-on-aws.md]

```python
request_preview = trace.info.request_preview
response_preview = trace.info.response_preview
```

## Timing

`TraceInfo` exposes timing properties including `request_time` (start timestamp in milliseconds since epoch), `timestamp_ms` (alias for request_time), `execution_duration` (in milliseconds), and `execution_time_ms` (alias for execution_duration). These values can be converted to human-readable datetime formats using standard Python libraries. ^[access-trace-data-databricks-on-aws.md]

```python
start_time = datetime.fromtimestamp(trace.info.request_time / 1000)
```

## Tags and Metadata

The `tags` dictionary on `TraceInfo` contains mutable key-value pairs that can be updated after trace creation, useful for storing environment information, user IDs, or other contextual data. `TraceInfo` also provides `trace_metadata` (immutable, set at creation time) and the deprecated `request_metadata` alias for `trace_metadata`. ^[access-trace-data-databricks-on-aws.md]

```python
print(f"Environment: {trace.info.tags.get('environment')}")
```

## Token Usage

`TraceInfo` can track aggregated token usage for LLM calls, storing counts of input tokens, output tokens, and total tokens as reported by LLM provider APIs. Token tracking methods vary by provider; refer to provider-specific documentation for implementation details. ^[access-trace-data-databricks-on-aws.md]

```python
token_usage = trace.info.token_usage
if token_usage:
    print(f"Input tokens: {token_usage.get('input_tokens')}")
    print(f"Output tokens: {token_usage.get('output_tokens')}")
    print(f"Total tokens: {token_usage.get('total_tokens')}")
```

## Assessments

Assessments are evaluations associated with a trace, accessible via `Trace.info.assessments`. Each assessment includes a name, value, source (with type and ID), optional rationale, and optional metadata or error information. Assessments can be searched by name, type (feedback or expectation), or span ID using the `search_assessments()` method. ^[access-trace-data-databricks-on-aws.md]

```python
assessments = trace.info.assessments
```

## Storage Location

`TraceInfo` includes a `trace_location` property that indicates where the trace is stored. If stored in an MLflow experiment, it provides the `experiment_id`. If stored in a Databricks inference table, it provides the full table name. The `experiment_id` shortcut property on `TraceInfo` provides quick access to the experiment identifier. ^[access-trace-data-databricks-on-aws.md]

## Data Export and Conversion

`TraceInfo` supports conversion to dictionary format via `to_dict()`, enabling serialization and reconstruction. It can also be converted to JSON using `to_json()` with optional pretty-printing, and loaded from JSON via `from_json()`. For DataFrame integration, `to_pandas_dataframe_row()` converts trace information into a format suitable for pandas DataFrame rows. ^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [[TraceData]] — The actual execution data component of a Trace
- Span — Building blocks of traces representing individual operations
- SpanType — Enumeration of span types (CHAT_MODEL, LLM, TOOL, RETRIEVER)
- [[MLflow Tracing]] — The tracing framework for MLflow GenAI applications
- [[Traces|Trace]] — The complete MLflow trace object combining TraceInfo and TraceData
- SpanAttributeKey — Constants for accessing specific span attributes

## Sources

- access-trace-data-databricks-on-aws.md
```

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
