---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2de81b5f2a01dbdef6f6aa4dfac12d9ddb75725db777482e0aa143ea3db413e
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowset_trace_tag-and-mlflowdelete_trace_tag-apis
    - mlflow.delete_trace_tag APIs and mlflow.set_trace_tag
    - MAMA
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: mlflow.set_trace_tag and mlflow.delete_trace_tag APIs
description: Methods to set or remove tags on a trace that has already been completed and logged, operating on the backend store.
tags:
  - mlflow
  - api
  - tracing
timestamp: "2026-06-19T17:36:04.944Z"
---

# `mlflow.set_trace_tag` and `mlflow.delete_trace_tag` APIs

The `mlflow.set_trace_tag` and `mlflow.delete_trace_tag` APIs allow you to modify tags on a trace after it has been completed and logged in the backend store. Tags are mutable key-value pairs that can be used for organizing, searching, and filtering traces. These APIs complement the in‑execution tag‑setting mechanism provided by [`mlflow.update_current_trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace). ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## `mlflow.set_trace_tag`

`mlflow.set_trace_tag(trace_id, key, value)` sets a tag with the given key and value on an existing trace identified by `trace_id`. If the tag key already exists on that trace, its value is updated to the new value. This method is intended for use after the trace has been finalized and stored. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Parameters

- **trace_id**: The identifier of the trace to modify. It can be obtained, for example, from `mlflow.get_last_active_trace_id()`.<br/>
- **key** (str): The tag name.<br/>
- **value** (str): The tag value.

## `mlflow.delete_trace_tag`

`mlflow.delete_trace_tag(trace_id, key)` removes a tag with the specified key from the trace identified by `trace_id`. If the key does not exist, the call is silently ignored. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Parameters

- **trace_id**: The identifier of the trace from which to remove the tag.<br/>
- **key** (str): The tag name to delete.

## Usage Example

The following example demonstrates creating a traced function, obtaining the trace ID after execution, and then using both APIs to set and delete tags:

```python
import mlflow

# Create and execute a traced function
@mlflow.trace
def process_data(data):
    return data.upper()

# Execute the function to create a trace
result = process_data("hello world")

# Get the trace_id from the most recent trace
trace_id = mlflow.get_last_active_trace_id()

# Set a tag on the trace
mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")

# Set another tag
mlflow.set_trace_tag(trace_id=trace_id, key="data_quality", value="high")

# Delete a tag from the trace
mlflow.delete_trace_tag(trace_id=trace_id, key="data_quality")
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Alternative: Updating Tags in the MLflow UI

As an alternative to the Python APIs, you can update or delete tags on a trace directly from the MLflow UI. Navigate to the trace tab and click the pencil icon next to the tag you want to change. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Comparison with Metadata

While tags are mutable and can be changed after logging, metadata is write‑once and immutable once set. Use these APIs for dynamic information such as review status, whereas metadata is better suited for fixed capturing‑time data like model version or environment. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]]
- mlflow.update_current_trace()|mlflow.update_current_trace
- [Trace Tags](/concepts/trace-tags.md) – Overview of using tags for trace organization.
- [Trace Metadata](/concepts/trace-metadata.md) – Immutable key‑value pairs set during trace execution.
- mlflow.search_traces() API|Search Traces Programmatically – Filter traces using tags.

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
