---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 518ee45efba7999e45ba2dbe406aca12f1ac37137c4512f1d1a686533b03a5d9
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - post-completion-tag-management-mlflowset_trace_tag-mlflowdelete_trace_tag
    - PTM(/M
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
      start: 60
      end: 73
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
      start: 5
      end: 8
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
      start: 75
      end: 79
title: Post-completion Tag Management (mlflow.set_trace_tag / mlflow.delete_trace_tag)
description: MLflow API methods for setting or deleting tags on traces that have already been completed and logged in the backend store.
tags:
  - MLflow
  - API
  - tracing
timestamp: "2026-06-18T14:27:52.100Z"
---

# Post-completion Tag Management (`mlflow.set_trace_tag` / `mlflow.delete_trace_tag`)

**Post-completion Tag Management** refers to the ability to add, update, or remove tags on an [[MLflow trace]] after the trace has been fully logged to the backend store. Unlike metadata (which is write‑once and immutable), tags can be modified at any point after a trace is completed, making them suitable for dynamic information such as review status, data quality assessments, or user feedback. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## When to Use Post‑completion Tags

- **Mutable data** – Tags are designed for information that may change after the trace is logged. For example, a human reviewer might mark a trace as `"approved"` or `"needs_review"` hours after the trace was created.
- **Annotating existing traces** – When you need to add context to traces that were created by automatic tracing or by earlier runs, without rerunning the traced function.
- **Categorization and search** – Tags can be used to filter and search traces programmatically or in the MLflow UI.

If you need to attach information during the trace’s execution (while it is still active), use [`mlflow.update_current_trace`](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/attach-tags/#update-tags-during-execution) instead. Post‑completion methods are only for traces that have already finished and been persisted. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## API Functions

### `mlflow.set_trace_tag(trace_id, key, value)`

Sets a tag (key‑value pair) on an already‑completed trace identified by `trace_id`. If the key already exists, the value is overwritten. This function is available after the trace has been logged to the backend store. ^[attach-custom-tags-and-metadata-databricks-on-aws.md#L60-L73]

### `mlflow.delete_trace_tag(trace_id, key)`

Removes a tag from an already‑completed trace. The trace must exist and the key must be present; otherwise the operation is ignored. ^[attach-custom-tags-and-metadata-databricks-on-aws.md#L60-L73]

## Example

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

# Set tags on the completed trace
mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")
mlflow.set_trace_tag(trace_id=trace_id, key="data_quality", value="high")

# Delete a tag from the trace
mlflow.delete_trace_tag(trace_id=trace_id, key="data_quality")
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md#L60-L73]

## Comparison with Metadata

| Feature | Metadata | Tags |
|---------|----------|------|
| Mutability | Immutable (write‑once) | Mutable (can be updated/deleted) |
| Typical use | Fixed information captured during execution (model version, environment) | Dynamic information that may change (review status, feedback) |
| Set during execution | `mlflow.update_current_trace(metadata={…})` | `mlflow.update_current_trace(tags={…})` |
| Set after completion | Not supported | `mlflow.set_trace_tag()` / `mlflow.delete_trace_tag()` |

^[attach-custom-tags-and-metadata-databricks-on-aws.md#L5-L8]

## UI‑Based Management

You can also update or delete tags from the MLflow UI. Navigate to the trace tab, then click the pencil icon next to the tag you want to update. Deletion is available through the same interface. ^[attach-custom-tags-and-metadata-databricks-on-aws.md#L75-L79]

## Related Concepts

- [Traces](/concepts/traces.md) – The fundamental unit of observation in MLflow GenAI.
- [Metadata](/concepts/trace-metadata.md) – Immutable key‑value pairs attached during trace execution.
- mlflow.update_current_trace()|mlflow.update_current_trace – Function to set tags/metadata while a trace is still active.
- mlflow.search_traces() API|Search Traces Programmatically – How to filter and query traces using tags.
- Attach Custom Tags and Metadata – Full guide covering both during‑execution and post‑completion methods.

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
2. [attach-custom-tags-and-metadata-databricks-on-aws.md:60-73](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
3. [attach-custom-tags-and-metadata-databricks-on-aws.md:5-8](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
4. [attach-custom-tags-and-metadata-databricks-on-aws.md:75-79](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
