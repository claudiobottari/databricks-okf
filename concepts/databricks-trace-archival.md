---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: defd4b1e267cb0151af9a65b60c35d84b0d8b819b37ffcebf212d564539773ba
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-trace-archival
    - DTA
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Databricks Trace Archival
description: Mechanism for persisting MLflow traces and their assessments to Unity Catalog Delta tables for long-term storage and advanced analysis.
tags:
  - mlflow
  - databricks
  - tracing
timestamp: "2026-06-18T10:47:53.183Z"
---

# Databricks Trace Archival

**Databricks Trace Archival** allows you to save traces and their associated assessments to a Unity Catalog Delta table for long-term storage and advanced analysis. This is useful for building custom dashboards, performing in-depth analytics on trace data, and maintaining a durable record of your application's behavior.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Prerequisites

You must have the necessary permissions to write to the specified Unity Catalog Delta table. The target table will be created if it does not already exist. If the table already exists, traces are appended to it.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Enabling trace archiving

To begin archiving traces for an experiment, use the `enable_databricks_trace_archival` function. You must specify the full name of the target Delta table, including [Catalog and Schema](/concepts/catalog-and-schema.md). If you don't provide an `experiment_id`, archiving is enabled for the currently active experiment.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

Archival can also be enabled from the Databricks UI.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Disabling trace archiving

Stop archiving traces for an experiment at any time by using the `disable_databricks_trace_archival` function.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

Disabling can also be performed from the Databricks UI.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that generates traces archived by this feature.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where archived traces are stored as Delta tables.
- [Delta Table](/concepts/delta-lake-table.md) — The storage format used for archived traces.
- GenAI Monitoring — The monitoring context in which trace archival is commonly used.
- [Experiment Tracking](/concepts/mlflow-experiment-tracking.md) — The experiment that you associate with trace archival.

## Next steps

- [Monitor GenAI apps in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) — Set up production monitoring.
- [Building MLflow evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) — Use archived traces to build evaluation datasets.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
