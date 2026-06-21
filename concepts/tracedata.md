---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 665f5dad08a96eeea1c7a3175adf20dbcd83a9490d89234ac746ee974b97eacb
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tracedata
    - Trace Data
    - Trace data
    - trace data
    - Trace Data Access
    - Trace data model
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: TraceData
description: Execution data component of a trace containing spans, full request/response payloads, and intermediate outputs.
tags:
  - mlflow
  - tracing
  - execution-data
timestamp: "2026-06-19T21:56:48.630Z"
---

```markdown
---
title: TraceData
summary: The execution data component of an MLflow Trace object containing spans, full request/response payloads, and intermediate outputs.
sources:
  - access-trace-data-databricks-on-aws.md
kind: concept
createdAt: "2026-06-21T12:00:00.000Z"
updatedAt: "2026-06-21T12:00:00.000Z"
tags:
  - mlflow
  - tracing
  - execution-data
aliases:
  - tracedata
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# TraceData

**TraceData** is a component of the MLflow [[Traces|Trace]] object that stores the actual execution data of a traced operation, including the full request and response payloads, intermediate outputs, and the collection of instrumented Spans that capture the application's step-by-step execution flow. ^[access-trace-data-databricks-on-aws.md]

## Overview

The MLflow Trace object comprises two main components: [[TraceInfo]] and TraceData. While TraceInfo holds lightweight metadata about the trace (such as ID, status, timing, tags, token usage, and assessments), TraceData contains the substantive execution data — the complete request and response text, intermediate outputs, and the spans that document each operation performed during the trace. ^[access-trace-data-databricks-on-aws.md]

## Structure and Properties

### Spans

The primary container within TraceData is the list of Span objects, accessible via `trace.data.spans`. Each span captures information about a specific operation, including its inputs, outputs, start and end times (in nanoseconds), status, span type, and parent-child relationships (for hierarchical execution flow). Spans can be searched using the `trace.search_spans()` method, which supports filtering by name (exact or regex), span type (e.g., `CHAT_MODEL`, `TOOL`, `RETRIEVER`), and span ID. ^[access-trace-data-databricks-on-aws.md]

### Request and Response Data

The full request and response payloads are accessible through `trace.data.request` and `trace.data.response`. These represent the complete data, as opposed to the truncated previews available in `TraceInfo.request_preview` and `trace.info.response_preview`. The payloads are typically JSON strings that can be parsed for analysis. ^[access-trace-data-databricks-on-aws.md]

### Intermediate Outputs

`trace.data.intermediate_outputs` provides a dictionary mapping span names to their intermediate outputs, which can be used for deeper analysis of the execution flow beyond root span outputs. ^[access-trace-data-databricks-on-aws.md]

## Data Conversion and Export

TraceData supports several conversion and serialization methods: ^[access-trace-data-databricks-on-aws.md]

- `trace.data.to_dict()` — converts the entire TraceData to a dictionary
- `trace.data.spans` can be individually converted using `span.to_dict()` and reconstructed with `Span.from_dict()`
- The complete Trace object (including Info and Data) can be serialized to a dictionary with `trace.to_dict()` and reconstructed with `Trace.from_dict()`
- JSON serialization is available via `trace.to_json()` and `trace.to_json(pretty=True)` for human-readable output
- Traces can be converted to Pandas DataFrame rows using `trace.to_pandas_dataframe_row()`

## Accessing TraceData from a Trace Object

Once a Trace object is retrieved (for example, by searching traces with `mlflow.search_traces()`), its TraceData is immediately available. The following code snippet demonstrates basic access:

```python
trace = mlflow.search_traces(max_results=1)[0]

# Access spans
spans = trace.data.spans
for span in spans:
    print(span.name, span.span_type, span.inputs, span.outputs)

# Access full request/response
request = trace.data.request
response = trace.data.response

# Access intermediate outputs
intermediate = trace.data.intermediate_outputs
```

^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [[Traces|Trace]] — The complete traced execution object
- [[TraceInfo]] — Metadata component of the Trace
- Span — An individual operation within TraceData
- SpanType — Enumeration of span types (CHAT_MODEL, TOOL, etc.)
- OpenTelemetry — Industry standard for observability, compatible with MLflow traces

## Sources

- access-trace-data-databricks-on-aws.md
```

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
