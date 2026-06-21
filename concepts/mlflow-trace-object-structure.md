---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfcfafa6707d2c9e95911ad2e98c03729280045fc0e2864bcef18cbce0a65aa1
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-object-structure
    - MTOS
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: MLflow Trace Object Structure
description: "The MLflow Trace object is composed of two main components: TraceInfo (metadata about the trace) and TraceData (actual execution data including spans and request/response payloads)."
tags:
  - mlflow
  - tracing
  - data-structures
timestamp: "2026-06-19T13:52:26.550Z"
---

# MLflow Trace Object Structure

The MLflow `Trace` object is the fundamental unit of observation in [MLflow Tracing](/concepts/mlflow-tracing.md), representing a single execution of an application or workflow. Each trace captures the complete lifecycle of a request — from its initial invocation through all intermediate operations to the final response — along with metadata, timing, token usage, and human or automated assessments. A trace is composed of two primary components: `TraceInfo` (metadata about the trace) and `TraceData` (the actual execution data, including spans). ^[access-trace-data-databricks-on-aws.md]

## TraceInfo: Metadata

`TraceInfo` holds the descriptive and diagnostic metadata for a trace. It is the first place to look for high-level information about what happened, when it happened, and what the outcome was. ^[access-trace-data-databricks-on-aws.md]

### Basic Metadata

Every trace has a unique identifier and status information:

- `trace_id`: A string uniquely identifying the trace within the experiment or workspace.
- `request_id` / `client_request_id`: An optional client-supplied identifier that can correlate the trace to an external system.
- `state`: The final state of the trace — `OK`, `ERROR`, or `IN_PROGRESS`. This is the preferred property for checking status.
- `status` (deprecated): An older status field; use `state` instead.

^[access-trace-data-databricks-on-aws.md]

### Storage Location

A trace's storage location determines how it can be queried and for how long it is retained. The `trace_location` property reveals whether the trace is stored in an [MLflow Experiment](/concepts/mlflow-experiment.md) or in a [Databricks Inference Table](/concepts/inference-tables.md):

- If stored in an MLflow experiment, `location.mlflow_experiment.experiment_id` gives the experiment ID.
- If stored in an inference table, `location.inference_table.full_table_name` gives the fully qualified table name.
- A shortcut property `trace.info.experiment_id` returns the experiment ID directly when applicable.

^[access-trace-data-databricks-on-aws.md]

### Preview Data

`request_preview` and `response_preview` provide truncated summaries of the full request and response payloads. These are useful for quickly understanding the gist of a trace without loading the complete data. Comparing preview length to full data length can give a sense of payload size. ^[access-trace-data-databricks-on-aws.md]

### Timing

Trace timing is recorded in milliseconds since the Unix epoch:

- `request_time` (or its alias `timestamp_ms`): The start timestamp in milliseconds.
- `execution_duration` (or its alias `execution_time_ms`): The total duration of the trace in milliseconds.

These can be converted to human-readable timestamps using standard Python datetime utilities. ^[access-trace-data-databricks-on-aws.md]

### Tags

Tags are **mutable** key-value pairs that can be added or updated after trace creation. They are useful for attaching environment identifiers, user IDs, version labels, or any custom metadata that should be searchable. Common use cases include:

```python
trace.info.tags.get('environment')      # e.g., "production"
trace.info.tags.get('user_id')          # e.g., "user_abc123"
```

In contrast, `trace_metadata` (also accessible as `request_metadata`) is **immutable** — set at creation time and not intended to be changed afterward. ^[access-trace-data-databricks-on-aws.md]

### Token Usage

When tracing LLM calls, MLflow can capture token usage counts returned by the provider API. The aggregated token usage is available as a dictionary:

- `token_usage['input_tokens']`: Total input tokens across all LLM calls in the trace.
- `token_usage['output_tokens']`: Total output tokens.
- `token_usage['total_tokens']`: Sum of input and output tokens.

Token tracking methods vary by LLM provider and platform configuration. ^[access-trace-data-databricks-on-aws.md]

### Assessments

Assessments are feedback or evaluation results attached to a trace. They can come from human raters (feedback), automated evaluators (expectations), or system checks. Each assessment has:

- `name`: A label such as "helpfulness" or "correctness".
- `value`: The assessment score or value.
- `source`: An object indicating the source type (`human`, `llm_judge`, `auto`, etc.) and source ID.
- `rationale`: An optional text explanation.
- `metadata`: Optional additional structured data.
- `span_id`: Optional — when present, the assessment is scoped to a specific span rather than the entire trace.

Assessments can be queried using `trace.search_assessments()` with filters for name, type (`"feedback"` or `"expectation"`), span_id, or a combination. By default, only the most recent assessment for each name/source/span combination is returned; pass `all=True` to retrieve overridden or superseded assessments as well. ^[access-trace-data-databricks-on-aws.md]

## TraceData: Execution Data

`TraceData` contains the actual execution artifacts of the trace — the sequence of operations (spans), the full request and response payloads, and intermediate outputs. ^[access-trace-data-databricks-on-aws.md]

### Spans

Spans are the building blocks of a trace, each representing a single unit of work. A trace can have multiple spans organized in a parent-child hierarchy. The `Span` class represents immutable, completed spans retrieved from a trace. ^[access-trace-data-databricks-on-aws.md]

#### Span Properties

Each span has the following core properties:

- `span_id`: A unique identifier for the span within the trace.
- `name`: A human-readable name describing the operation (e.g., "retrieve_documents", "chat_completion").
- `span_type`: The type of operation, drawn from the `SpanType` enum or a string. Common types include `CHAT_MODEL`, `LLM`, `TOOL`, `RETRIEVER`, `AGENT`, `CHAIN`, `PARSER`, and `UNKNOWN`.
- `trace_id`: The ID of the parent trace.
- `parent_id`: The ID of the parent span, or `None` for root spans.
- `start_time_ns` and `end_time_ns`: Timing in nanoseconds, allowing precise duration calculations.
- `status`: An object with a `status_code` (indicating success or error) and an optional `description`.
- `inputs` and `outputs`: The span-specific input and output data.

^[access-trace-data-databricks-on-aws.md]

#### Searching Spans

`trace.search_spans()` provides flexible filtering:

- **By name**: Exact match (string) or regex pattern (`re.compile(...)`).
- **By span_type**: Match against `SpanType` enum values or their string equivalents.
- **By span_id**: Retrieve a specific span by its ID.
- **Combined**: Multiple criteria can be applied together for precise queries.

^[access-trace-data-databricks-on-aws.md]

#### Span Attributes

Spans can carry additional attributes accessed via `span.get_attribute(key)`. For chat model spans, special attribute keys exist under `SpanAttributeKey`:

- `SpanAttributeKey.CHAT_MESSAGES`: The chat messages exchanged.
- `SpanAttributeKey.CHAT_TOOLS`: The tools available to the model.
- Custom attributes can be stored and retrieved by key.

Token usage at the individual span level is also available through attributes like `"llm.token_usage.input_tokens"` and `"llm.token_usage.output_tokens"`. ^[access-trace-data-databricks-on-aws.md]

#### Intermediate Outputs

`trace.data.intermediate_outputs` provides a dictionary mapping span names to their outputs for non-root spans. This is useful for extracting the result of a specific operation without walking the entire span tree. ^[access-trace-data-databricks-on-aws.md]

### Full Request and Response Data

`trace.data.request` and `trace.data.response` contain the complete request and response payloads as JSON strings. These are the full, untruncated versions of what the `request_preview` and `response_preview` summarize. They can be parsed into Python dictionaries using `json.loads()`. ^[access-trace-data-databricks-on-aws.md]

## Advanced Span Operations

### Span Hierarchy Analysis

Spans form a parent-child tree. By building a children map from the flat list of spans and identifying root spans (those with `parent_id = None`), you can reconstruct the entire execution tree. This enables:

- **Hierarchy printing**: Recursively print the span tree with indentation.
- **Duration breakdown**: Calculate the proportion of time spent in LLM calls vs. retrieval vs. tool execution.
- **Critical path analysis**: Identify the longest-duration path from a root span to a leaf, highlighting the operations that contribute most to overall latency.

^[access-trace-data-databricks-on-aws.md]

### Serialization and Conversion

Traces and their components support several formats for persistence and exchange:

- **Dictionary conversion**: `trace.to_dict()` returns a nested dictionary; `Span.to_dict()` and `Span.from_dict()` enable round-trip conversion of individual spans.
- **JSON serialization**: `trace.to_json()` produces a JSON string; `trace.to_json(pretty=True)` produces a human-readable version. Traces can be deserialized with `Trace.from_json()`.
- **Pandas DataFrame**: `trace.to_pandas_dataframe_row()` converts a single trace to a dictionary suitable for DataFrame construction. When processing multiple traces, each can produce a row, and the rows can be aggregated into a DataFrame for analysis.

^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The framework that produces Trace objects
- MLflow Trace Client — API for searching, storing, and deleting traces
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Automated assessment integration with trace data
- [MLflow Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — Adding human assessments to traces
- [LLM Observability](/concepts/genai-observability.md) — Broader monitoring and analysis patterns
- [MLflow Experiment](/concepts/mlflow-experiment.md) — Storage target for trace data

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
