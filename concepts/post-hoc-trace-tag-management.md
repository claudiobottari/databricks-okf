---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2be7fe5ab662fbf48df775563f09bdd95c292c3ba957562e20a6d666d4084e00
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - post-hoc-trace-tag-management
    - PTTM
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: Post-hoc trace tag management
description: The ability to set or delete tags on an MLflow trace that has already been completed and logged, using mlflow.set_trace_tag and mlflow.delete_trace_tag functions or the MLflow UI.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T09:03:41.229Z"
---

# Post-hoc trace tag management

**Post-hoc trace tag management** refers to the ability to add, update, and remove tags on an [[MLflow trace]] after it has been completed and logged to the backend store. This capability enables dynamic organization, search, and filtering of traces based on mutable information such as review status, data quality assessments, or user feedback. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Overview

Tags are key-value pairs that can be attached to traces. Unlike [Trace Metadata](/concepts/trace-metadata.md), which is write-once and immutable after logging, tags are fully mutable — they can be added, updated, or deleted at any point, even after the trace has been recorded. This makes tags the appropriate mechanism for information that may change over time, such as human review labels, approval status, or operational annotations. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Setting tags after trace completion

To add or update a tag on an already-logged trace, use the [`mlflow.set_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_trace_tag) function. It takes a `trace_id`, a `key`, and a `value`. If the key does not yet exist on the trace, it is added; if the key already exists, its value is overwritten. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
import mlflow

# Execute a traced function to create a trace
@mlflow.trace
def process_data(data):
    return data.upper()

result = process_data("hello world")

# Get the trace_id from the most recent active trace
trace_id = mlflow.get_last_active_trace_id()

# Set a tag on the trace
mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")

# Set another tag
mlflow.set_trace_tag(trace_id=trace_id, key="data_quality", value="high")
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Deleting tags

To remove a tag from a trace, use the [`mlflow.delete_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.delete_trace_tag) function. It requires the `trace_id` and the `key` of the tag to delete. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
mlflow.delete_trace_tag(trace_id=trace_id, key="data_quality")
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Using the UI

Tags can also be updated or deleted directly from the [MLflow UI](/concepts/mlflow.md). Navigate to the **Traces** tab for a given experiment, locate the trace of interest, and click the pencil icon next to the tag you wish to modify. The UI provides a visual way to manage tags without writing code. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

![Traces tag update](https://assets.docs.databricks.com/_static/images/mlflow3/tracing/trace-set-tag.gif)

## Differences from metadata

The primary distinction between tags and metadata is mutability:

| Property | Tags | Metadata |
|----------|------|----------|
| Mutable after logging | Yes | No (write-once) |
| Use cases | Dynamic info (review status, feedback) | Fixed info (model version, environment) |
| Update API | `mlflow.set_trace_tag` | `mlflow.update_current_trace` (only during execution) |
| Delete API | `mlflow.delete_trace_tag` | Not supported |

During trace execution, tags and metadata can both be set via `mlflow.update_current_trace()`. However, only tags can be modified after the trace has been logged. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Best practices

- Use tags for any attribute that might need correction or enrichment after the trace is created — for example, human-annotated quality scores, audit status, or operational notes.
- Use metadata for information that is known at trace creation time and will never change, such as the model version used or the environment name.
- Avoid storing large or complex data structures in tag values; tags are intended for simple key-value filtering.

## Related concepts

- [Trace Metadata](/concepts/trace-metadata.md) — Immutable key-value pairs set at trace creation.
- [[MLflow Trace|MLflow traces]] — The core observability unit for GenAI agent executions.
- mlflow.search_traces() API|Search traces programmatically — Filtering traces by tag values using the SDK.
- Attach custom tags during trace execution — Setting tags inside a traced function with `mlflow.update_current_trace`.

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
