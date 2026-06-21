---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c55512771fdcfa1739cd159c4f505cee7ab8a7aead4fb22e405caccaa839032f
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-tag-management-via-ui
    - MTTMVU
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: MLflow Trace Tag Management via UI
description: Graphical interface in the MLflow UI for updating or deleting tags on traces by navigating to the trace tab and using the pencil icon.
tags:
  - mlflow
  - ui
  - tracing
timestamp: "2026-06-19T17:35:48.351Z"
---

# MLflow Trace Tag Management via UI

**MLflow Trace Tag Management via UI** refers to the ability to update and delete tags on existing traces directly through the MLflow user interface, without requiring programmatic access via the Python SDK.

## Overview

Tags in MLflow are mutable key-value pairs that can be attached to traces for organization, search, and filtering purposes. Unlike metadata, which is write-once and immutable after logging, tags can be updated or removed after a trace has been completed and logged in the backend store. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

The MLflow UI provides a visual interface for managing tags on traces that have already been logged, complementing the programmatic methods available through the Python SDK. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Updating Tags via the UI

To update a tag on a trace from the MLflow UI:

1. Navigate to the **Traces** tab for the relevant experiment.
2. Locate the trace whose tag you want to modify.
3. Click on the **pencil icon** next to the tag you wish to update.

This action allows you to modify the tag's value directly in the interface. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Deleting Tags via the UI

The MLflow UI also supports deleting tags from traces. While the documentation specifically shows the pencil icon for updating tags, the UI provides mechanisms for tag removal as well. For programmatic deletion, the [`mlflow.delete_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.delete_trace_tag) method is available. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Comparison with Programmatic Tag Management

| Method | Use Case | Timing |
|--------|----------|--------|
| UI (pencil icon) | Ad-hoc updates after trace completion | Post-logging |
| `mlflow.set_trace_tag()` | Automated or batch updates | Post-logging |
| `mlflow.update_current_trace(tags=...)` | Adding tags during trace execution | During execution |

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Best Practices

- Use tags for dynamic information that may change over time, such as user feedback, review status, or data quality assessments. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]
- Use [MLflow Trace Metadata Management](/concepts/mlflow-trace-metadata.md) (immutable) for fixed information captured during execution, such as model version, environment, or system configuration. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]
- The UI is ideal for manual review workflows where a human needs to update tags after inspecting a trace. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- [MLflow Trace Metadata Management](/concepts/mlflow-trace-metadata.md) — Write-once immutable key-value pairs for traces
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the tracing system
- mlflow.search_traces() API|Search Traces Programmatically — Filtering and searching traces using tags and metadata
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — Tracking users, sessions, versions, and environments

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
