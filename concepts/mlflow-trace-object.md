---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8dd86a025d8d19ad86f8f654aebefc7f8edba80d20894ea513e4ee4b48f7e14c
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-object
    - MTO
    - Trace Object
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: MLflow Trace Object
description: Core entity representing a complete record of an LLM or application execution, composed of TraceInfo (metadata) and TraceData (execution data).
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T21:57:17.525Z"
---

# MLflow Trace Object

The **MLflow Trace Object** (`mlflow.entities.Trace`) is the core data structure in [MLflow Tracing](/concepts/mlflow-tracing.md) that represents a single traced execution of an AI application. It captures both immutable metadata about the invocation and detailed execution data—including spans, timing, inputs, outputs, token usage, and assessments—making it possible to perform fine‑grained analysis and evaluation of [GenAI](/concepts/mlflow-genai-evaluate-api.md) workflows.^[access-trace-data-databricks-on-aws.md]

## Structure

A `Trace` object is composed of two main components, accessible via `trace.info` and `trace.data`:

| Component | Description | Reference |
|-----------|-------------|-----------|
| `TraceInfo` | Immutable metadata: trace ID, status, timestamps, tags, token usage, assessments, and request/response previews. | [`TraceInfo`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo) |
| `TraceData` | Execution data: the complete span hierarchy, full request/response payloads, and intermediate outputs. | [`TraceData`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceData) |

^[access-trace-data-databricks-on-aws.md]

## Components

### TraceInfo — Metadata

`TraceInfo` provides a non‑mutable record of the trace’s lifecycle and context:

- **Identifiers**: `trace_id`, `client_request_id`
- **Status**: `state` (OK, ERROR, IN_PROGRESS) and the deprecated `status`
- **Timing**: `request_time` / `timestamp_ms` (milliseconds since epoch), `execution_duration` / `execution_time_ms`
- **Tags** (mutable) and `trace_metadata` (immutable, formerly `request_metadata`)
- **Token usage**: aggregated counts (input, output, total) when available from the LLM provider
- **Assessments**: evaluation feedback attached to the trace or individual spans
- **Previews**: `request_preview` and `response_preview` provide truncated summaries of the full payloads

The storage location is also accessible via `trace.info.trace_location`, which can point to an [MLflow Experiment](/concepts/mlflow-experiment.md) (with `experiment_id`) or a [Databricks Inference Table](/concepts/inference-tables.md).^[access-trace-data-databricks-on-aws.md]

### TraceData — Execution Data

`TraceData` holds the runtime details of the invocation:

- `spans`: a list of Span objects representing individual operations (LLM calls, tool invocations, retrieval steps, etc.)
- `request` / `response`: complete JSON strings of the root request and response
- `intermediate_outputs`: a dictionary mapping span names to their outputs for non‑root spans

^[access-trace-data-databricks-on-aws.md]

### Spans

Each Span (`mlflow.entities.Span`) represents a unit of work and includes:

- **Hierarchy**: `span_id`, `trace_id`, `parent_id`
- **Name and type**: human‑readable name and a SpanType (e.g., `CHAT_MODEL`, `LLM`, `TOOL`, `RETRIEVER`, `AGENT`, `CHAIN`)
- **Timing**: `start_time_ns` and `end_time_ns` in nanoseconds
- **Status**: a `SpanStatusCode` object with `status_code` and `description`
- **Inputs and outputs**: operation‑specific data
- **Attributes**: arbitrary key‑value metadata, including chat‑specific fields accessible via `SpanAttributeKey`

The `Trace` object provides a `search_spans()` method to filter spans by name (exact or regex), span type, or span ID.^[access-trace-data-databricks-on-aws.md]

### Assessments

Assessments are evaluation results (feedback or expectations) attached to the trace or to specific spans. The `search_assessments()` method on a trace can filter by:

- **Name** (e.g., `"helpfulness"`)
- **Type** (`"feedback"` or `"expectation"`)
- **Span ID**
- A combination of criteria

Each assessment carries a `value`, `source` (type and ID), optional `rationale`, `metadata`, `error`, and `span_id`. The `all=True` flag includes assessments that have been overridden.^[access-trace-data-databricks-on-aws.md]

## Key Methods

The `Trace` object offers several convenience methods for data access and conversion:

| Method | Purpose |
|--------|---------|
| `search_spans(name, span_type, span_id)` | Filter spans by name (string or regex), SpanType, or span ID. |
| `search_assessments(name, type, span_id, all)` | Filter assessments by name, type, span, or include overridden ones. |
| `to_dict()` | Convert the entire trace to a dictionary. |
| `to_json(pretty=False)` | Serialize to a JSON string. |
| `to_pandas_dataframe_row()` | Convert to a row suitable for building a Pandas DataFrame. |

The class also provides `from_dict()` and `from_json()` static methods for reconstruction.^[access-trace-data-databricks-on-aws.md]

## Usage Examples

### Accessing a trace

Traces are retrieved via `mlflow.search_traces()`, which returns a Pandas DataFrame. Individual `Trace` objects can be extracted from the DataFrame or obtained directly.^[access-trace-data-databricks-on-aws.md]

### Analyzing timing

```python
from mlflow.entities import SpanType

llm_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]
duration_ms = (llm_span.end_time_ns - llm_span.start_time_ns) / 1_000_000
```

### Retrieving token usage

```python
token_usage = trace.info.token_usage
if token_usage:
    print(f"Input tokens: {token_usage.get('input_tokens')}")
```

### Exporting a trace

```python
trace_dict = trace.to_dict()
trace_json = trace.to_json(pretty=True)
```

^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [TraceInfo](/concepts/traceinfo.md) – metadata component of a trace
- [TraceData](/concepts/tracedata.md) – execution data component
- Span – individual operation within a trace
- SpanType – enumeration of span types
- [Feedback](/concepts/feedback-object.md) – evaluation feedback attached to traces or spans
- [MLflow Tracing](/concepts/mlflow-tracing.md) – the overall tracing subsystem
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – using traces in evaluation workflows
- mlflow.search_traces() API|Search Traces API – methods for retrieving trace objects

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
