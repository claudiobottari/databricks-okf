---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca1fd6223490ed5573a6b8c53cd6c7b4a8178530708a89bae8efc632af9ad87d
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-ui-trace-tag-editing
    - MUTTE
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: MLflow UI Trace Tag Editing
description: Graphical interface in the MLflow UI for updating or deleting tags on traces via the trace tab, using a pencil icon.
tags:
  - MLflow
  - UI
  - tracing
timestamp: "2026-06-18T14:28:04.737Z"
---

# MLflow UI Trace Tag Editing

**MLflow UI Trace Tag Editing** refers to the ability to update, add, or remove tags on an existing trace directly through the MLflow user interface, without writing code. Tags are mutable key-value pairs that can be dynamically modified after a trace has been logged to the backend store. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Overview

In MLflow, tags are mutable metadata attachments that can be updated after a trace is logged. Unlike [metadata](attach-custom-tags-and-metadata-databricks-on-aws.md), which is write-once and immutable, tags are designed for dynamic information that may change over time — such as user feedback, review status, or data quality assessments. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Editing Tags in the UI

To edit tags on a trace from the MLflow UI: navigate to the trace tab, then click on the pencil icon next to the tag you want to update. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

This allows you to modify the value of an existing tag without needing to re-run the traced function or interact with the Python API.

## Adding Tags in the UI

The same pencil icon workflow can be used to add new tags to an existing trace. Clicking the pencil icon on an empty or available slot lets you specify a new key-value pair to attach to the trace. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Deleting Tags in the UI

Tags can also be removed from a trace through the UI, though the source material does not specify the exact UI mechanism for deletion (the equivalent programmatic method is [`mlflow.delete_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.delete_trace_tag)). ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Programmatic Alternatives

While the UI provides a visual editor, tags can also be manipulated programmatically using:

- [`mlflow.set_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_trace_tag) — to set a tag on a completed trace
- [`mlflow.delete_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.delete_trace_tag) — to remove a tag from a trace

These methods operate on already-logged traces by their `trace_id`. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Tags vs. Metadata

When deciding what to attach to a trace, consider the differences:

| Property | Tags | Metadata |
|----------|------|----------|
| Mutability | Mutable — can be updated after logging | Immutable — write-once |
| Use case | Dynamic information (review status, feedback) | Fixed information (model version, environment) |
| Update method | UI pencil icon or `set_trace_tag()` | [`mlflow.update_current_trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) (during execution only) |

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Best Practices

- Use tags for information that may change over the lifecycle of a trace, such as approval status or manual annotations.
- Prefer [metadata](attach-custom-tags-and-metadata-databricks-on-aws.md) for immutable execution-time details like model version, environment name, or system configuration.
- Editing tags in the UI is useful for ad-hoc annotation and review workflows, while programmatic methods are better suited for automated pipelines. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Trace Metadata](/concepts/trace-metadata.md)
- [MLflow UI](/concepts/mlflow.md)
- mlflow.search_traces() API|Search traces programmatically

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
