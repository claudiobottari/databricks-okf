---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22c278754481b12e8b21f77fce7d541466fdf81e30fe3da6d1cf905c863cd06b
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
    - trace-concepts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - trace-tags
    - trace tag
    - trace-tags-mlflow
    - TT(
    - Trace (MLflow)
    - Traces (MLflow)
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
    - file: trace-concepts-databricks-on-aws.md
title: Trace Tags
description: Mutable key-value pairs attached to MLflow traces for organization, search, and filtering; can be updated after logging.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T14:04:35.112Z"
---

---
title: Trace Tags
summary: Mutable key-value pairs attached to MLflow traces for dynamic information such as user feedback, review status, or data quality assessments, which can be updated after a trace is logged.
sources:
  - attach-custom-tags-and-metadata-databricks-on-aws.md
  - trace-concepts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:03:24.993Z"
updatedAt: "2026-06-19T09:03:24.993Z"
tags:
  - mlflow
  - tracing
  - observability
aliases:
  - trace-tags
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Trace Tags

**Trace Tags** are mutable key-value pairs that can be attached to [Traces](/concepts/traces.md) in MLflow to organize, search, and filter trace data. Unlike metadata, which is immutable after logging, tags can be updated or removed even after a trace is completed. Tags are useful for storing dynamic information such as user feedback, review status, or data quality assessments. Tags are stored in the `TraceInfo` object, and MLflow defines standard tags for common use cases, including `mlflow.trace.session`, `mlflow.trace.user`, `mlflow.source.name`, `mlflow.source.git.commit`, and `mlflow.source.type`.^[attach-custom-tags-and-metadata-databricks-on-aws.md, trace-concepts-databricks-on-aws.md]

## Difference Between Tags and Metadata

| Property | Tags | Metadata |
|----------|------|----------|
| Mutability | Mutable — can be updated after logging | Immutable — cannot be changed after logging |
| Use case | Dynamic information (e.g., review status, feedback) | Fixed information (e.g., model version, environment) |

Both are key-value pairs but serve different lifecycle purposes.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Setting Tags During Trace Execution

When using automatic tracing or the Fluent API (e.g., `@mlflow.trace`), you can add tags to the currently active trace by calling `mlflow.update_current_trace(tags=...)` from inside the traced function. The function adds the specified keys if they do not already exist, or updates them if they do.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1

my_func(10)
```

## Setting and Deleting Tags on Completed Traces

For traces that have already been logged to the backend store, use `mlflow.set_trace_tag()` to set a single tag and `mlflow.delete_trace_tag()` to remove one. Both require the trace ID.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def process_data(data):
    return data.upper()

result = process_data("hello world")

trace_id = mlflow.get_last_active_trace_id()

# Set a tag
mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")

# Delete a tag
mlflow.delete_trace_tag(trace_id=trace_id, key="review_status")
```

## Editing Tags in the UI

Tags can also be updated or deleted from the MLflow UI. Navigate to the trace tab and click the pencil icon next to the tag to modify it.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Best Practices

- Use tags for information that may change over time (e.g., manual review status, data quality flags).
- Use metadata for immutable attributes captured at trace creation time (e.g., model version, environment).
- Tag keys and values are arbitrary strings; keep them consistent across traces to enable effective Trace Search.

## Related Concepts

- [Traces](/concepts/traces.md)
- [Metadata](/concepts/trace-metadata.md)
- Fluent API
- [Automatic Tracing](/concepts/automatic-tracing.md)
- Trace Search
- [TraceInfo](/concepts/traceinfo.md)

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md
- trace-concepts-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
2. [trace-concepts-databricks-on-aws.md](/references/trace-concepts-databricks-on-aws-9723e725.md)
