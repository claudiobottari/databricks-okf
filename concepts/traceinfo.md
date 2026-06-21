---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4665d072e64e9319e5461fcb44948b37cbb5c44ca8c9a0b8ef4721ac604b16d4
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traceinfo
    - Trace Info
    - Trace info object
    - traceinfo-mlflow
  citations:
    - file: access-trace-data-databricks-on-aws.md
    - file: trace-concepts-databricks-on-aws.md
title: TraceInfo
description: Metadata component of a trace containing identifiers, status, timing, tags, token usage, and assessments.
tags:
  - mlflow
  - tracing
  - metadata
timestamp: "2026-06-19T21:56:38.290Z"
---

```yaml
---
title: TraceInfo
summary: Metadata component of an MLflow Trace containing identifiers, status, request/response previews, timing, tags, token usage, and assessments.
sources:
  - access-trace-data-databricks-on-aws.md
  - trace-concepts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:17:47.169Z"
updatedAt: "2026-06-19T17:26:40.152Z"
tags:
  - mlflow
  - tracing
  - metadata
aliases:
  - traceinfo
confidence: 0.95
provenanceState: merged
inferredParagraphs: 0
---

# TraceInfo

**TraceInfo** is the metadata component of an [[MLflow Trace]]. It contains identifiers, status, request/response previews, timing information, tags, token usage, and assessments – everything needed to describe a trace without loading the full execution payload. `TraceInfo` is accessible via `trace.info` on any `Trace` instance and is stored as indexed rows in a relational database to support fast searching and filtering. ^[access-trace-data-databricks-on-aws.md, trace-concepts-databricks-on-aws.md]

## Overview

The `Trace` object in MLflow comprises two primary components: `TraceInfo` (metadata) and `TraceData` (the actual execution payload containing spans). While `TraceData` is stored in artifact storage (e.g., a Unity Catalog volume) to keep queries performant as trace volume grows, `TraceInfo` is stored in a relational database for efficient indexing and retrieval. ^[trace-concepts-databricks-on-aws.md]

`TraceInfo` provides the high-level metadata that lets you identify, organize, and assess traces without loading the full execution details. Key properties include identifiers, status, request/response previews, timing, tags, metadata, token usage, and assessments. ^[access-trace-data-databricks-on-aws.md]

## Key Properties

The following table summarizes the most important fields available on `TraceInfo`. All properties are accessed via `trace.info.<field>` in Python.

| Property | Type | Description |
|----------|------|-------------|
| `trace_id` | string | Unique identifier for the trace. ^[access-trace-data-databricks-on-aws.md] |
| `client_request_id` | string | Client-provided request identifier. ^[access-trace-data-databricks-on-aws.md] |
| `state` | string | Current state: `OK`, `ERROR`, or `IN_PROGRESS`. ^[access-trace-data-databricks-on-aws.md] |
| `status` | string | Deprecated alias for `state`. ^[access-trace-data-databricks-on-aws.md] |
| `request_preview` | string | Truncated summary of the full request data. ^[access-trace-data-databricks-on-aws.md] |
| `response_preview` | string | Truncated summary of the full response data. ^[access-trace-data-databricks-on-aws.md] |
| `request_time` / `timestamp_ms` | int | Start time in milliseconds since epoch. ^[access-trace-data-databricks-on-aws.md] |
| `execution_duration` / `execution_time_ms` | int | Duration in milliseconds. ^[access-trace-data-databricks-on-aws.md] |
| `tags` | dict | Mutable key-value pairs for organization and filtering. ^[access-trace-data-databricks-on-aws.md] |
| `trace_metadata` / `request_metadata` | dict | Immutable metadata set at trace creation. ^[access-trace-data-databricks-on-aws.md] |
| `token_usage` | dict | Aggregated token counts (input, output, total), if tracked by the LLM provider. ^[access-trace-data-databricks-on-aws.md] |
| `assessments` | list | Assessment objects attached to the trace. ^[access-trace-data-databricks-on-aws.md] |
| `trace_location` | object | Storage location (MLflow experiment or inference table). ^[access-trace-data-databricks-on-aws.md] |
| `experiment_id` | string | Shortcut to the experiment ID, if stored in an MLflow experiment. ^[access-trace-data-databricks-on-aws.md] |

## Accessing TraceInfo

You typically obtain a `Trace` object by searching traces or by retrieving the last active trace. From a `Trace` instance, all metadata is available through `trace.info`. ^[access-trace-data-databricks-on-aws.md]

### Basic Metadata

```python
print(f"Trace ID: {trace.info.trace_id}")
print(f"Client Request ID: {trace.info.client_request_id}")
print(f"State: {trace.info.state}")  # OK, ERROR, IN_PROGRESS
print(f"Status (deprecated): {trace.info.status}")
```

^[access-trace-data-databricks-on-aws.md]

### Request and Response Previews

The `request_preview` and `response_preview` properties provide truncated summaries of the full payload, making it easy to understand what happened without loading the complete data.

```python
request_preview = trace.info.request_preview
response_preview = trace.info.response_preview
```

^[access-trace-data-databricks-on-aws.md]

### Timing Information

Timestamps are in milliseconds since the Unix epoch. Duration is in milliseconds.

```python
import datetime
start_time = datetime.datetime.fromtimestamp(trace.info.request_time / 1000)
print(f"Start time (ms): {trace.info.request_time}")
print(f"Execution duration (ms): {trace.info.execution_duration}")
```

^[access-trace-data-databricks-on-aws.md]

### Tags and Metadata

Tags are mutable and can be updated after trace creation. `trace_metadata` (also aliased as `request_metadata`) is immutable and set at creation time.

```python
for key, value in trace.info.tags.items():
    print(f"  {key}: {value}")

for key, value in trace.info.trace_metadata.items():
    print(f"  {key}: {value}")
```

^[access-trace-data-databricks-on-aws.md]

### Token Usage

If the LLM provider returns token counts, they are aggregated in `token_usage`.

```python
token_usage = trace.info.token_usage
if token_usage:
    print(f"Input tokens: {token_usage.get('input_tokens')}")
    print(f"Output tokens: {token_usage.get('output_tokens')}")
    print(f"Total tokens: {token_usage.get('total_tokens')}")
```

^[access-trace-data-databricks-on-aws.md]

### Assessments

Assessments attached to the trace can be accessed via the `assessments` list or searched using `trace.search_assessments()`.

```python
for assessment in trace.info.assessments:
    print(f"Name: {assessment.name}, Value: {assessment.value}")
```

^[access-trace-data-databricks-on-aws.md]

### Storage Location

The `trace_location` object reveals whether the trace is stored in an MLflow experiment or a Databricks inference table.

```python
location = trace.info.trace_location
if location.mlflow_experiment:
    print(f"Experiment ID: {location.mlflow_experiment.experiment_id}")
if location.inference_table:
    print(f"Table: {location.inference_table.full_table_name}")
```

^[access-trace-data-databricks-on-aws.md]

You can also use the shortcut `trace.info.experiment_id` to get the experiment ID directly. ^[access-trace-data-databricks-on-aws.md]

## Storage Layout

`TraceInfo` is stored directly in a relational database as indexed rows, which enables fast queries for searching and filtering traces. This is distinct from `TraceData`, which is stored in artifact storage (e.g., a Unity Catalog volume) to keep queries performant even as trace volume grows. ^[trace-concepts-databricks-on-aws.md]

## Standard Tags

MLflow defines several standard tags for common use cases, all accessible through `trace.info.tags`:

- `mlflow.trace.session`: Session identifier for grouping related traces. ^[trace-concepts-databricks-on-aws.md]
- `mlflow.trace.user`: User identifier for tracking per-user interactions. ^[trace-concepts-databricks-on-aws.md]
- `mlflow.source.name`: Entry point or script that generated the trace. ^[trace-concepts-databricks-on-aws.md]
- `mlflow.source.git.commit`: Git commit hash of the source code (if applicable). ^[trace-concepts-databricks-on-aws.md]
- `mlflow.source.type`: Source type (`PROJECT`, `NOTEBOOK`, etc.). ^[trace-concepts-databricks-on-aws.md]

You can also add custom tags for your specific needs. See [[Best Practices for Adding Context to MLflow Traces|Add Context to Traces]] and Attach Custom Tags. ^[trace-concepts-databricks-on-aws.md]

## Related Concepts

- [[Traces|Trace]] – The complete trace object containing both `TraceInfo` and `TraceData`.
- [[TraceData]] – The container for span execution data.
- Span – Individual operations captured within a trace.
- [[MLflow Tracing]] – The broader observability framework.
- [[Assessments]] – Quality annotations attached to traces.
- Token Usage – Aggregated token consumption data.

## Sources

- access-trace-data-databricks-on-aws.md
- trace-concepts-databricks-on-aws.md
```

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
2. [trace-concepts-databricks-on-aws.md](/references/trace-concepts-databricks-on-aws-9723e725.md)
