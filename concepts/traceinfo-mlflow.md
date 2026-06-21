---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d893275c678714dc290fa0e9982fc20759a1514be433236801ff7f0140f29c71
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traceinfo-mlflow
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: TraceInfo (MLflow)
description: Metadata component of an MLflow Trace, containing trace ID, status (OK/ERROR/IN_PROGRESS), request/response previews, storage location, timing, tags, token usage, and assessments.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T08:50:15.632Z"
---

---
title: TraceInfo (MLflow)
summary: The metadata component of an MLflow Trace object, containing identifiers, status, timing, tags, token usage, assessments, and storage location details.
sources:
  - access-trace-data-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T16:00:00.000Z"
updatedAt: "2026-06-18T16:00:00.000Z"
tags:
  - mlflow
  - tracing
  - metadata
aliases:
  - traceinfo-mlflow
  - TIM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# TraceInfo (MLflow)

**TraceInfo** is the metadata component of an MLflow [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) object. While the `Trace` object is composed of `TraceInfo` (metadata) and [`TraceData`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceData) (execution data), `TraceInfo` contains all high-level information about a trace such as its unique identifier, status, timing, tags, token usage, and assessments. ^[access-trace-data-databricks-on-aws.md]

## Data Fields

All the following fields are accessed via `trace.info.<property>` after retrieving a trace object.

### Basic Metadata

- **`trace_id`** – A unique string identifier for the trace.
- **`request_id`** – An older, deprecated identifier; use `trace_id` instead.
- **`client_request_id`** – An optional client‑supplied identifier.
- **`state`** – The current state of the trace: `OK`, `ERROR`, or `IN_PROGRESS`.
- **`status`** (deprecated) – Use `state` instead.

^[access-trace-data-databricks-on-aws.md]

### Request / Response Previews

- **`request_preview`** – A truncated summary of the input request.
- **`response_preview`** – A truncated summary of the output response.

These previews let you quickly understand what happened without loading the full payloads (which are available in `TraceData`). ^[access-trace-data-databricks-on-aws.md]

### Timing

- **`request_time`** (alias **`timestamp_ms`**) – Start time in milliseconds since the Unix epoch.
- **`execution_duration`** (alias **`execution_time_ms`**) – Total execution duration in milliseconds.

### Tags and Metadata

- **`tags`** – A mutable dictionary of key‑value pairs that can be updated after trace creation (e.g., `environment`, `user_id`).
- **`trace_metadata`** (alias **`request_metadata`**) – An immutable dictionary of metadata set at creation time.

### Token Usage

- **`token_usage`** – A dictionary (if available) containing `input_tokens`, `output_tokens`, and `total_tokens` aggregated from LLM calls within the trace.

Token tracking depends on the LLM provider’s API returning the counts. ^[access-trace-data-databricks-on-aws.md]

### Assessments

- **`assessments`** – A list of assessment objects attached to the trace. Each assessment has `name`, `value`, `source` (type and ID), and optional `rationale`, `metadata`, and `error`. If an assessment is span‑specific, it also contains a `span_id`.

For richer search, use `trace.search_assessments()`, which supports filtering by name, type (`"feedback"` or `"expectation"`), span ID, and whether to include overridden assessments. ^[access-trace-data-databricks-on-aws.md]

### Storage Location

- **`trace_location`** – An object with a `type` field (`"mlflow_experiment"` or `"inference_table"`) and convenience properties:
  - **`mlflow_experiment.experiment_id`** (alias `experiment_id`) – The experiment where the trace is stored.
  - **`inference_table.full_table_name`** – The inference table, if applicable.

## Related Concepts

- [[MLflow Trace]] — The parent object that combines TraceInfo and TraceData.
- [TraceData (MLflow)](/concepts/tracedata-mlflow.md) — The execution data (spans, full request/response) of a trace.
- [MLflow Span](/concepts/mlflow-spans.md) — Individual units of work within a trace.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall mechanism for capturing and inspecting LLM application executions.

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
