---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7ce623c416ac16da5ddb7266823d5c807f975b059f6aef418a484aee3af38b0a
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-metadata-in-mlflow
    - TMIM
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: Trace Metadata in MLflow
description: Write-once, immutable key-value pairs attached to MLflow traces during execution for fixed information such as model version or environment.
tags:
  - MLflow
  - tracing
  - observability
timestamp: "2026-06-18T14:27:42.611Z"
---

# Trace Metadata in MLflow

**Trace metadata** in MLflow refers to key-value pairs that can be attached to a [trace](/concepts/traces.md) for organization, search, and filtering. MLflow supports two distinct types of key-value pairs on traces: **metadata** (write-once and immutable) and **tags** (mutable and updatable after logging). The choice between them depends on whether the information is fixed at capture time or may change later. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Metadata (Immutable)

Metadata is write-once and immutable after the trace is logged. Use metadata for fixed information captured during execution, such as model version, environment, or system configuration. Attempting to update metadata with a key that already exists is silently ignored and the original value persists. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

To set metadata on a trace during its execution (when using automatic tracing or fluent APIs), call [`mlflow.update_current_trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) with a `metadata` dictionary:

```python
import mlflow

@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(metadata={"model_version": "v1.2.3", "environment": "production"})
    return x + 1

my_func(10)
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Tags (Mutable)

Tags are mutable and can be updated after a trace is logged. Use tags for dynamic information that may change, such as user feedback, review status, or data quality assessments. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Setting Tags During Trace Execution

When using automatic tracing or fluent APIs, call `mlflow.update_current_trace` with a `tags` dictionary. This function adds a tag when the key is not already present, and updates the value if the key already exists. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1

my_func(10)
```

### Setting and Deleting Tags After Trace Completion

For traces already logged to the backend store, use:

- [`mlflow.set_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_trace_tag) — sets a tag on a completed trace.
- [`mlflow.delete_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.delete_trace_tag) — removes a tag from a trace.

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

### Updating Tags in the MLflow UI

Tags can also be updated or deleted from the [MLflow UI](/concepts/mlflow.md): navigate to the trace tab and click the pencil icon next to the tag you wish to update. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of tracing in MLflow
- [Traces](/concepts/traces.md) — The core object that carries metadata and tags
- mlflow.search_traces() API|Search Traces Programmatically — Filter and search traces using tags and metadata
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — Track users, sessions, versions, and environments

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
