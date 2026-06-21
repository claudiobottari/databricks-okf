---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c475b4fe798b1d277c455312f14fa4c0285c541c54c32ab351c29522876d706d
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowset_trace_tag-and-mlflowdelete_trace_tag
    - mlflow.delete_trace_tag and mlflow.set_trace_tag
    - MAM
    - mlflowset_trace_tag-and-mlflowdelete_trace_tag-apis
    - mlflow.delete_trace_tag APIs and mlflow.set_trace_tag
    - MAMA
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: mlflow.set_trace_tag and mlflow.delete_trace_tag
description: Post-hoc API methods to set or remove tags on already-completed MLflow traces stored in the backend, using the trace ID.
tags:
  - mlflow
  - api
  - tracing
timestamp: "2026-06-19T22:08:29.545Z"
---

```markdown
---
title: mlflow.set_trace_tag and mlflow.delete_trace_tag
summary: Post-tracing API methods to set or remove tags on an already-logged trace in the backend store, identified by trace_id.
sources:
  - attach-custom-tags-and-metadata-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:48:43.333Z"
updatedAt: "2026-06-18T10:48:43.333Z"
tags:
  - mlflow
  - api
  - tracing
aliases:
  - mlflowset_trace_tag-and-mlflowdelete_trace_tag
  - mlflow.delete_trace_tag and mlflow.set_trace_tag
  - MAM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

## `mlflow.set_trace_tag` and `mlflow.delete_trace_tag`

`mlflow.set_trace_tag` and `mlflow.delete_trace_tag` are MLflow Python API methods for managing tags on traces that have already been completed and logged to the backend store. Tags are mutable key-value pairs used for organization, search, and filtering of traces, and can be updated after a trace is logged.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

- **`mlflow.set_trace_tag(trace_id, key, value)`**: Sets a tag on a trace identified by `trace_id`. If the tag key already exists, it overwrites the value.^[attach-custom-tags-and-metadata-databricks-on-aws.md]
- **`mlflow.delete_trace_tag(trace_id, key)`**: Removes a tag with the given key from the trace.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

These methods are intended for post-hoc tagging scenarios — for example, adding a review status or data quality assessment after a trace has been captured.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Example

The following example creates a traced function, retrieves its `trace_id`, sets two tags, and then deletes one of them:

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

### Comparison with `mlflow.update_current_trace`

For tags that need to be added *during* trace execution (before the trace is completed), use `mlflow.update_current_trace(tags={...})`. The `mlflow.set_trace_tag` and `mlflow.delete_trace_tag` methods, in contrast, operate on traces that have already been finalized and stored. Tags added via `update_current_trace` are also mutable later using `set_trace_tag`.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### UI alternative

You can also update or delete tags on a trace from the MLflow UI. Navigate to the **Traces** tab, locate the trace, and click the pencil icon next to the tag you want to modify.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Related concepts

- [[MLflow Tracing]] — The overall tracing framework in MLflow
- [[Traces]] — The fundamental unit of trace data
- mlflow.update_current_trace()|mlflow.update_current_trace — Method for adding tags/metadata during trace execution
- [[Trace Tags and Metadata|Attach custom tags and metadata — Tags vs Metadata]] — Explanation of mutable tags and immutable metadata

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md
```

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
