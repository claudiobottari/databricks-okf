---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6271d7d38fead7fe2d7cc3e3e6f85c8d3b8875e1291a3cd5a58896ca8d6c9305
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-immutability-model
    - MTIM
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: MLflow Trace Immutability Model
description: Distinction between mutable tags and immutable metadata in MLflow tracing, where metadata keys are set-once and ignored on update attempts.
tags:
  - mlflow
  - tracing
  - design
timestamp: "2026-06-18T10:48:41.647Z"
---

---
title: MLflow Trace Immutability Model
summary: Describes the immutability model for MLflow Traces, distinguishing between mutable tags and write-once immutable metadata, and explains how to attach, update, and delete these key-value pairs.
sources:
  - attach-custom-tags-and-metadata-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:47:17.732Z"
updatedAt: "2026-06-18T10:47:17.732Z"
tags:
  - mlflow
  - tracing
  - observability
  - genai
aliases:
  - mlflow-trace-immutability-model
  - trace-tags-vs-metadata
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Trace Immutability Model

MLflow Traces support two types of key-value pairs for attaching additional information: **tags** and **metadata**. They follow different immutability rules. Tags are mutable and can be updated after a trace is logged. Metadata is write-once and immutable after logging.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Tags (Mutable)

Tags are intended for dynamic information that may change over time, such as user feedback, review status, or data quality assessments. Tags can be set or updated after a trace has been completed and logged.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

To add tags during trace execution (inside a traced function), use `mlflow.update_current_trace(tags=...)`. If a tag key already exists, `mlflow.update_current_trace` updates that key with the new value.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

For already‑completed traces, use `mlflow.set_trace_tag(trace_id, key, value)` to set or update a tag, and `mlflow.delete_trace_tag(trace_id, key)` to remove a tag. You can also update or delete tags from the MLflow UI by navigating to the trace tab and clicking the pencil icon next to the tag.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Example

```python
import mlflow

@mlflow.trace
def process_data(data):
    return data.upper()

result = process_data("hello world")
trace_id = mlflow.get_last_active_trace_id()

mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")
mlflow.set_trace_tag(trace_id=trace_id, key="data_quality", value="high")
mlflow.delete_trace_tag(trace_id=trace_id, key="data_quality")
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Metadata (Immutable)

Metadata is intended for fixed information captured during trace execution, such as model version, environment, or system configuration. Once set, metadata **cannot be changed**; any attempt to set a metadata key that already exists is silently ignored and the original value remains.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

To attach metadata during trace execution, call `mlflow.update_current_trace(metadata=...)` inside the traced function. Because metadata is immutable, only the first write of each key is persisted.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Example

```python
import mlflow

@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(
        metadata={
            "model_version": "v1.2.3",
            "environment": "production"
        }
    )
    return x + 1

my_func(10)
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Practical Guidance

- Use tags for information that may be updated after the trace is complete (e.g., manual review status, A/B test assignment).
- Use metadata for immutable attributes known at run time (e.g., Git commit hash, model registry version, pipeline run ID).
- The distinction helps maintain data integrity: metadata guarantees that logged values are never silently overwritten, while tags provide flexibility for post‑hoc annotation.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The observability system for GenAI applications
- [[MLflow Trace|MLflow Traces]] — The fundamental unit of tracing
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — Tracking users, sessions, versions, and environments
- mlflow.search_traces() API|Search Traces Programmatically — Filtering and searching using tags and metadata

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
