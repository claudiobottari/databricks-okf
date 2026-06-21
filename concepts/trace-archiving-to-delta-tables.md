---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e112673925c223ff917fc022b0933b68749080f7de6adb879c7636dbcf5bf672
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-archiving-to-delta-tables
    - TATDT
    - Archive Traces to a Delta Table
    - Archive traces to a Delta table
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Trace Archiving to Delta Tables
description: The ability to save MLflow traces and their associated assessments to a Unity Catalog Delta table for long-term storage and advanced analysis.
tags:
  - mlflow
  - monitoring
  - databricks
timestamp: "2026-06-19T22:08:12.983Z"
---

# Trace Archiving to Delta Tables

**Trace Archiving to Delta Tables** is a feature in [MLflow Tracing](/concepts/mlflow-tracing.md) that lets you save traces and their associated assessments to a [Unity Catalog](/concepts/unity-catalog.md) [Delta Table](/concepts/delta-lake-table.md) for long-term storage and advanced analysis. Archived traces are useful for building custom dashboards, performing in-depth analytics on application behavior, and maintaining a durable record of your application's interactions. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Requirements

You must have the necessary permissions to write to the specified Unity Catalog Delta table. If the table does not already exist, it will be created automatically. If the table already exists, traces are appended to it. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Enabling Trace Archiving

To begin archiving traces for an experiment, call the `enable_databricks_trace_archival` function from the `mlflow.tracing.archival` module. You must provide the full name of the target Delta table, including [Catalog and Schema](/concepts/catalog-and-schema.md). If you do not supply an `experiment_id`, archiving is enabled for the currently active experiment. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

## Disabling Trace Archiving

To stop archiving traces for a specific experiment, call the `disable_databricks_trace_archival` function with the same `experiment_id`. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

## Related Concepts

- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Set up ongoing monitoring of GenAI applications.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Building evaluation datasets from archived traces.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing infrastructure that captures the archived data.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
