---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 28f5180663a97eb04e0f009723ff947b3a7e2b99917018cd8cfaf4ec03e7c87b
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-metadata
    - MTM
    - MLflow metadata
    - MLflow Trace Metadata Management
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: MLflow Trace Metadata
description: Immutable, write-once key-value pairs attached to traces at logging time for fixed information such as model version and environment.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T22:08:38.915Z"
---

# MLflow Trace Metadata

**MLflow Trace Metadata** refers to immutable, write-once key-value pairs that are attached to a trace during its execution. Metadata is designed to capture fixed information that does not change after logging, such as model version, environment, or system configuration. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Metadata vs. Tags

MLflow traces support two types of user-defined key-value data: metadata and tags. The key distinction is mutability:

- **Metadata** is write‑once and immutable after logging. Once a metadata key is set, any subsequent attempt to update the same key is silently ignored and the original value remains unchanged. This guarantees that execution‑time metadata cannot be accidentally overwritten. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]
- **Tags** are mutable and can be updated after a trace is logged. Tags are suitable for dynamic information that may change over time, such as user feedback, review status, or data quality assessments. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

Both metadata and tags are used for organization, search, and filtering of traces. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Adding Metadata During Trace Execution

To add metadata to a trace while it is still running, use the [`mlflow.update_current_trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) function. This works with both automatic tracing and the fluent trace API.

```python
import mlflow

@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(
        metadata={"model_version": "v1.2.3", "environment": "production"}
    )
    return x + 1

my_func(10)
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Immutability Constraint

Metadata is immutable once set. If you attempt to update metadata with a key that already exists, the operation will be ignored and the original value will remain unchanged. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Prerequisites for Using Metadata

Before adding metadata to traces, ensure the following requirements are met:

1. Install MLflow and required packages:
   ```bash
   pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"
   ```
2. Create an MLflow experiment by following the setup environment quickstart. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Adding Tags During Trace Execution

Tags can also be added during trace execution using `mlflow.update_current_trace`. Unlike metadata, if a tag key already exists, the value is updated with the new value. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1

my_func(10)
```

## Modifying Tags After Trace Completion

After a trace has been completed and logged, tags can still be modified using dedicated API methods:

- [`mlflow.set_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_trace_tag) — sets a tag on an existing trace (updates if key exists).
- [`mlflow.delete_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.delete_trace_tag) — removes a tag from an existing trace.

Example: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

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

Tags can also be updated or deleted from the [MLflow UI](/concepts/mlflow.md) by navigating to the trace tab and clicking the pencil icon next to the tag. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] — The core tracing abstraction for logging and monitoring ML executions.
- [MLflow Tags](/concepts/mlflow-trace-tags.md) — Mutable key-value pairs that can be modified after trace logging.
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — Track users, sessions, versions, and environments in traces.
- mlflow.search_traces() API|Search Traces Programmatically — Filter and search traces using tags and metadata.

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
