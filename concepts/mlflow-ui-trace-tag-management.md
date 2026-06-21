---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 286ad4f54e5bbed349bbf1307690096adf31c6702dece0500a7725ddecff6448
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-ui-trace-tag-management
    - MUTTM
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: MLflow UI Trace Tag Management
description: Graphical method within the MLflow UI to view, update, and delete tags on existing traces using a pencil icon in the trace tab.
tags:
  - mlflow
  - ui
  - tracing
timestamp: "2026-06-19T22:08:26.055Z"
---

Here is the wiki page for "MLflow UI Trace Tag Management", written solely from the provided source material.

---

## MLflow UI Trace Tag Management

**MLflow UI Trace Tag Management** refers to the process of viewing, adding, editing, and deleting tags on traces directly through the MLflow user interface. This provides a visual method for organizing, searching, and filtering traces without writing code.

### Overview

Tags are key-value pairs that can be attached to traces to provide organizational metadata. Unlike [Trace Metadata](/concepts/trace-metadata.md), which is immutable after logging, tags are mutable and can be updated after a trace is logged. This makes tags suitable for dynamic information that may change over time, such as user feedback, review status, or data quality assessments. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Managing Tags via the MLflow UI

The MLflow UI allows users to update or delete tags on a trace that has already been completed and logged in the backend store. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

To edit a tag:
1. Navigate to the trace tab.
2. Click on the pencil icon next to the tag you want to update. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

This operation is the UI equivalent of the [`mlflow.set_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_trace_tag) and [`mlflow.delete_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.delete_trace_tag) API methods. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Related Concepts

- [Trace Metadata](/concepts/trace-metadata.md) — Immutable key-value data set during trace execution.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall system for logging, storing, and querying trace data.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and traces.

### Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
