---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c19720606721d4debc65ed1cdc69af0b690f69c4e88c781d2b72a7d3835cf19
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-archival-api
    - MTAA
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: MLflow Tracing Archival API
description: Python API functions (enable_databricks_trace_archival and disable_databricks_trace_archival) in mlflow.tracing.archival that control whether traces from an experiment are saved to a Unity Catalog Delta table.
tags:
  - mlflow
  - api
  - python
timestamp: "2026-06-19T09:02:32.186Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Archival API

**MLflow Tracing Archival API** is a feature that enables saving [[MLflow Trace|MLflow Traces]] and their associated assessments to a [Unity Catalog](/concepts/unity-catalog.md) Delta table for long-term storage and advanced analysis. This API is useful for building custom dashboards, performing in-depth analytics on trace data, and maintaining a durable record of application behavior. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Overview

The Tracing Archival API allows you to persist trace data beyond the default retention period of an MLflow experiment. By archiving traces to a Delta table, you gain the ability to query and analyze historical trace data using standard SQL tools and build custom visualizations. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

You must have the necessary permissions to write to the specified Unity Catalog Delta table. If the target table does not exist, it will be created automatically. If the table already exists, traces are appended to it. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Enable Trace Archiving

### Using the MLflow API

To begin archiving traces for an experiment, use the `enable_databricks_trace_archival` function from the `mlflow.tracing.archival` module. You must specify the full name of the target Delta table, including [Catalog and Schema](/concepts/catalog-and-schema.md). If you don't provide an `experiment_id`, archiving is enabled for the currently active experiment. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

# Archive traces from a specific experiment to a Unity Catalog Delta table
enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

### Using the Databricks UI

Trace archiving can also be configured through the Databricks UI, providing an alternative to the programmatic API. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Disable Trace Archiving

### Using the MLflow API

Stop archiving traces for an experiment at any time by using the `disable_databricks_trace_archival` function. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

# Stop archiving traces for the specified experiment
disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

### Using the Databricks UI

Trace archiving can also be disabled through the Databricks UI. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] — The execution trace data that can be archived
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where archived traces are stored
- [Delta Tables](/concepts/delta-lake-table.md) — The storage format for archived traces
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Setting up production monitoring using traces
- Building MLflow Evaluation Datasets — Using archived traces to build evaluation datasets
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and traces

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
