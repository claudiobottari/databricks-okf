---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1a9c76ce495075ffc8c419a50fe56d2e8c034d4fcb8ffc54f2e75b7188825ab
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-archival
    - Trace Archiving
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Trace Archival
description: The process of saving MLflow traces and their assessments to a Unity Catalog Delta table for long-term storage and advanced analysis.
tags:
  - mlflow
  - traces
  - databricks
  - storage
timestamp: "2026-06-19T14:03:25.135Z"
---

#Trace Archival

**Trace Archival** is the process of saving [[MLflow Trace|MLflow Traces]] and their associated assessments to a [Unity Catalog](/concepts/unity-catalog.md) [Delta Table](/concepts/delta-lake-table.md) for long-term storage and advanced analysis. This feature enables users to build custom dashboards, perform in-depth analytics on trace data, and maintain a durable record of application behavior. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Enabling Trace Archival

Trace archival is enabled per experiment using the `enable_databricks_trace_archival` function from the `mlflow.tracing.archival` module. You must specify the full three‑level name of the target Delta table, including [Catalog and Schema](/concepts/catalog-and-schema.md) (e.g., `"my_catalog.my_schema.archived_traces"`). If no `experiment_id` is provided, archival is enabled for the currently active experiment. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

If the target table does not already exist, it is created automatically. If it does exist, new traces are appended to the existing table. The user must have the necessary permissions to write to the specified Delta table. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Disabling Trace Archival

To stop archiving traces for a given experiment, call `disable_databricks_trace_archival`. This function accepts the `experiment_id` of the experiment for which archival should be disabled. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

## Next Steps

After enabling trace archival, you can use the archived data to:

- Set up [Production Monitoring](/concepts/production-monitoring.md) for GenAI applications.
- Build [MLflow Evaluation Datasets](/concepts/evaluation-datasets.md) from the stored traces and assessments.

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] – The execution traces that are archived.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that manages the Delta table.
- [Delta Table](/concepts/delta-lake-table.md) – The storage format for archived traces.
- [Production Monitoring](/concepts/production-monitoring.md) – Monitoring workflow that can use archived traces.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Datasets that can be built from archived traces.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
