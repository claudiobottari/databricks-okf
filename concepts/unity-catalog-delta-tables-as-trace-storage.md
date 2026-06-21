---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 483b8b96ee67247fa8e1c18c47f73a76ac64759708815063e5ee7284ba5377b6
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-delta-tables-as-trace-storage
    - UCDTATS
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Unity Catalog Delta Tables as Trace Storage
description: Unity Catalog Delta tables act as the durable storage target for archived MLflow traces, supporting automatic table creation, append-only writes, and cross-catalog/schema organization.
tags:
  - unity-catalog
  - delta-lake
  - storage
timestamp: "2026-06-19T09:02:52.472Z"
---

# Unity Catalog Delta Tables as Trace Storage

**Unity Catalog Delta Tables as Trace Storage** refers to the capability of archiving [[MLflow Trace|MLflow Traces]] and their associated assessments into a [Unity Catalog](/concepts/unity-catalog.md) managed Delta table. This feature enables long-term retention, advanced analytics, and custom dashboarding on trace data beyond the default storage period.

## Overview

When you archive traces to a Unity Catalog Delta table, each trace and its corresponding assessments (such as evaluation scores or human feedback) are saved as rows in the table. The table is created automatically if it does not exist; if it already exists, new traces are appended. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

This feature is available through the MLflow Python API or the Databricks UI. It is particularly useful for [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) where you need to maintain a durable record of your application's behavior over time. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Benefits

- **Long-term storage**: Traces are retained indefinitely in Unity Catalog, independent of MLflow’s default trace retention policies.
- **Advanced analytics**: Use SQL, Databricks SQL, or notebooks to query archived traces for performance trends, failure analysis, or compliance reporting.
- **Custom dashboards**: Build dashboards in Lakeview Dashboards or other BI tools directly on the Delta table.
- **Evaluation dataset generation**: Archived traces can be reused to build [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) for further model testing and quality improvement. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Requirements

- You must have the necessary permissions to write to the specified Unity Catalog Delta table. The table is referenced by its full three‑level name (`catalog.schema.table`). ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## How to Enable Trace Archiving

### Using the MLflow API

Call `enable_databricks_trace_archival` with the target Delta table full name and an optional experiment ID. If no experiment ID is provided, archiving is enabled for the currently active MLflow experiment.

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

### Using the Databricks UI

The Databricks UI provides a no-code alternative to enable archiving. (The source document does not detail the UI steps, but it indicates the option exists.) ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## How to Disable Trace Archiving

To stop archiving traces for a specific experiment, call `disable_databricks_trace_archival` with the experiment ID:

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Important Details

- The target Delta table must reside in Unity Catalog; external locations are not supported.
- If the table already exists, new traces are appended; existing data is not overwritten.
- Archiving is performed per experiment. You can enable archiving for multiple experiments to separate traces by use case.

## Related Concepts

- [[MLflow Trace|MLflow Traces]] – The fundamental unit of trace data recorded during GenAI application execution.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Ongoing quality monitoring that feeds into trace archives.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that stores the archived Delta table.
- [Building MLflow evaluation datasets](/concepts/mlflow-evaluation-datasets.md) – How to use archived traces to create evaluation datasets.
- Lakeview Dashboards – A visualization tool that can query archived trace data.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
