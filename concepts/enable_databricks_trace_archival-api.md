---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a0fa004a5962cde30cc4aa62f043b9c9a8d08cb584ac98e397de33a3e60f0a1
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - enable_databricks_trace_archival-api
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: enable_databricks_trace_archival API
description: An MLflow API function used to begin archiving traces for an experiment by specifying a target Unity Catalog Delta table and optional experiment ID.
tags:
  - mlflow
  - api
  - python
timestamp: "2026-06-19T22:07:54.928Z"
---

# enable_databricks_trace_archival API

`enable_databricks_trace_archival` is a function in the `mlflow.tracing.archival` module that saves MLflow traces and their associated assessments to a Unity Catalog Delta table. This enables long-term storage, advanced analytics, and durable record-keeping of tracing data beyond the default MLflow experiment tracking. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Overview

When called, the function configures an MLflow experiment to automatically archive all future traces (and their assessments) to the specified Delta table. The target table is created automatically if it does not already exist; if it does exist, traces are appended to it. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

The function is designed to be used with [Unity Catalog](/concepts/unity-catalog.md) [Delta table](/concepts/delta-lake-table.md)s, which must be specified with a fully qualified three-level name (catalog.schema.table). The user or service principal calling the function must have the necessary write permissions on the target table. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Function Signature

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname: str,
    experiment_id: Optional[str] = None
)
```

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `delta_table_fullname` | `str` | The fully qualified name of the target Unity Catalog Delta table, including [Catalog and Schema](/concepts/catalog-and-schema.md) (e.g., `"my_catalog.my_schema.archived_traces"`). |
| `experiment_id` | `str` (optional) | The ID of the MLflow experiment for which to enable trace archival. If not provided, archiving is enabled for the currently active experiment. |

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Usage Example

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

# Archive traces from a specific experiment to a Unity Catalog Delta table
enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related API: disable_databricks_trace_archival

To stop archiving traces for an experiment at any time, use the companion function `disable_databricks_trace_archival`, which accepts an `experiment_id` parameter. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

# Stop archiving traces for the specified experiment
disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Next Steps

After enabling archival, you can use the archived traces to:
- Set up [Production Monitoring](/concepts/production-monitoring.md) for GenAI applications.
- Build [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) from historical trace data.

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The framework for capturing and visualizing trace data.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance and catalog system for storing Delta tables.
- [Delta table](/concepts/delta-lake-table.md) – The storage format used for trace archival.
- disable_databricks_trace_archival API – The counterpart to stop archiving.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
