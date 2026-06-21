---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14a970a45580340a517388f75a7ba2b2349d677528800eafea4fad9bca320e6c
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-delta-tables-for-trace-storage
    - UCDTFTS
    - Unity Catalog tables for traces
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Unity Catalog Delta Tables for Trace Storage
description: Target storage format for archived traces, requiring write permissions and supporting automatic table creation or append behavior.
tags:
  - unity-catalog
  - delta-lake
  - storage
timestamp: "2026-06-18T10:48:07.822Z"
---

# Unity Catalog Delta Tables for Trace Storage

**Unity Catalog Delta Tables for trace storage** provide a durable, queryable destination for persisting [MLflow traces](/concepts/mlflow-tracing.md) and their associated assessments. By archiving traces to a [Unity Catalog](/concepts/unity-catalog.md) managed [Delta table](/concepts/delta-lake-table.md), you enable long-term storage, custom analytics, and integration with dashboards and downstream data pipelines.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Overview

When you enable trace archiving, every trace (including its evaluation assessments) produced by an [MLflow Experiment](/concepts/mlflow-experiment.md) is copied into a specified [Delta table](/concepts/delta-lake-table.md) in Unity Catalog. This table can be queried with SQL, used as the basis for custom dashboards (e.g., in Databricks SQL or Lakeview Dashboards), or joined with other data for deeper analysis. The archiving mechanism is built into the MLflow Python library and is managed through a simple API.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Enabling Trace Archiving

To begin archiving traces for an experiment, use the `enable_databricks_trace_archival` function from the `mlflow.tracing.archival` module. You must provide the full Unity Catalog three‑level name of the target Delta table (including [Catalog and Schema](/concepts/catalog-and-schema.md)). An optional `experiment_id` parameter lets you target a specific experiment; if omitted, archiving is enabled for the currently active experiment.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

The target table is created automatically if it does not already exist. If the table already exists, new traces are appended to it.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Disabling Trace Archiving

You can stop archiving traces for an experiment at any time by calling `disable_databricks_trace_archival` with the corresponding experiment ID. No data is removed from the Delta table; archiving is simply deactivated going forward.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

## Permissions

To enable trace archiving, the principal calling `enable_databricks_trace_archival` must have the necessary permissions to write to the specified Unity Catalog Delta table. This typically requires `WRITE` or `MODIFY` privilege on the table (or on its parent schema and catalog) in Unity Catalog. Without sufficient permissions, the archiving setup will fail.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Table Behavior

- **First‑time use**: If the table does not exist, it is created automatically with a schema that matches the trace and assessment structure.
- **Existing table**: If the table already exists, traces are appended as new rows. The table is never overwritten or truncated by the archiving operation.
- **Long‑term storage**: Because the data is stored in [Delta Lake](/concepts/delta-lake.md) format, you can apply time‑travel queries, vacuum old data, or further transform the table using standard Delta Lake operations.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Use Cases

- **Custom dashboards**: Build operational or analytical dashboards in Databricks SQL or Lakeview Dashboards that display trace volume, latency distributions, error rates, or assessment scores over time.
- **Advanced analytics**: Join archived traces with other tables (e.g., model metadata, user feedback) for in‑depth analysis of application behavior and model performance.
- **Durable record**: Maintain a permanent, immutable record of all traces for compliance, auditing, or debugging purposes.
- **Evaluation dataset creation**: Use archived traces to construct training or evaluation datasets for future iterations of your GenAI application (see [Building MLflow evaluation datasets](/concepts/mlflow-evaluation-datasets.md)).^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The core mechanism that records trace data before archiving.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages access to the Delta table.
- [Delta Lake](/concepts/delta-lake.md) – The storage format that provides ACID transactions and time travel on the archived table.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The logical container for which trace archiving is configured.
- [Production Monitoring](/concepts/production-monitoring.md) – A complementary feature for monitoring GenAI apps in production.
- [Building MLflow evaluation datasets](/concepts/mlflow-evaluation-datasets.md) – A workflow that can consume archived traces as input.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
