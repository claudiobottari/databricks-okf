---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8963075496e2ade490fd47382da36c365211d6106451923bcb32711da5ca0615
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tracedata-mlflow
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: TraceData (MLflow)
description: Execution data component of an MLflow Trace, containing spans, full request/response data, and intermediate outputs from non-root spans.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T08:50:23.594Z"
---

---
title: TraceData (MLflow)
summary: The component of an MLflow Trace object containing the actual execution data, including spans, full request/response payloads, and intermediate outputs.
sources:
  - access-trace-data-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - mlflow
  - tracing
  - spans
  - evaluation
aliases:
  - tracedata-mlflow
  - tracedata
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# TraceData (MLflow)

**TraceData** is the component of an MLflow [[MLflow Trace|Trace (MLflow)|Trace]] object that holds the execution-level details of the traced operation, as opposed to [TraceInfo](/concepts/traceinfo-mlflow.md), which stores metadata. It provides programmatic access to the raw request and response payloads, the full hierarchy of spans recorded during execution, and any intermediate outputs produced by non-root spans. ^[access-trace-data-databricks-on-aws.md]

## Properties

### `spans`

The `spans` attribute returns a list of [Span (MLflow)|Span](/concepts/mlflow-spans.md) objects that represent the individual units of work within the trace. Each span has properties such as `span_id`, `name`, `span_type`, `start_time_ns`, `end_time_ns`, `status`, `inputs`, and `outputs`. The spans list includes all spans across the execution tree; parent-child relationships are accessible via the `parent_id` attribute of each span. ^[access-trace-data-databricks-on-aws.md]

### `request` / `response`

The `request` and `response` attributes provide the full text of the input and output of the root span. These properties mirror the truncated previews available in `TraceInfo.request_preview` and `TraceInfo.response_preview`, but contain the complete payload rather than a summary. The values are typically JSON strings that can be parsed for analysis. ^[access-trace-data-databricks-on-aws.md]

### `intermediate_outputs`

The `intermediate_outputs` property returns a dictionary mapping span names (strings) to their output values for non-root spans. This is useful for inspecting the results of intermediate steps such as retriever calls or tool invocations without iterating through the full spans list. ^[access-trace-data-databricks-on-aws.md]

## Methods

### `to_dict()`

Converts the TraceData object to a Python dictionary representation, suitable for serialization or debugging. ^[access-trace-data-databricks-on-aws.md]

## Access Pattern

TraceData is accessed via the `data` attribute of a Trace object:

```python
trace = mlflow.get_trace(trace_id)
spans = trace.data.spans
request_text = trace.data.request
response_text = trace.data.response
intermediate = trace.data.intermediate_outputs
```

^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- Trace (MLflow) — The top-level object that combines TraceInfo and TraceData.
- [TraceInfo (MLflow)](/concepts/traceinfo-mlflow.md) — Metadata component (ID, status, timestamps, tags, token usage, assessments).
- [Span (MLflow)](/concepts/mlflow-tracing.md) — Individual execution unit within TraceData.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader system for instrumenting and collecting trace data.
- mlflow.search_traces()|Search Traces — API for retrieving Trace objects from the backend.

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
