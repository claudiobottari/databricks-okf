---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1353ccd1623c4f320beb1473d5f4ca51ad60975f604672ed96d853ce0f710628
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - experiment-level-trace-archival-configuration
    - ETAC
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Experiment-Level Trace Archival Configuration
description: The pattern of enabling or disabling trace archival on a per-experiment basis using experiment_id parameters.
tags:
  - mlflow
  - experiments
  - traces
  - configuration
timestamp: "2026-06-19T14:03:23.160Z"
---

# Experiment-Level Trace Archival Configuration

**Experiment-Level Trace Archival Configuration** refers to the process of saving [[MLflow Trace|MLflow traces]] and their associated assessments from a specific experiment to a [Unity Catalog](/concepts/unity-catalog.md) [Delta table](/concepts/delta-lake-table.md) for long-term storage, advanced analysis, and durable record‑keeping. This configuration is useful for building custom dashboards, performing in-depth analytics on trace data, and maintaining a persistent history of an application's behavior across multiple evaluation runs. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Prerequisites

The user or service principal configuring archival must have the necessary permissions to write to the specified Unity Catalog Delta table. If the target table does not already exist, archival will create it; if it already exists, traces are appended to it. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Enabling Trace Archival

Trace archival can be enabled using either the MLflow API or the Databricks UI.

### Using the MLflow API

Call the `enable_databricks_trace_archival` function from the `mlflow.tracing.archival` module. You must supply the full name (catalog, schema, and table name) of the target Delta table. Optionally, provide an `experiment_id`; if omitted, archival is enabled for the currently active experiment. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

# Archive traces from a specific experiment to a Unity Catalog Delta table
enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

### Using the Databricks UI

The same functionality is available through the Databricks UI, though the specific UI steps are not detailed in the source material. The API and UI methods are equivalent in effect.

## Disabling Trace Archival

To stop archiving traces for an experiment, call the `disable_databricks_trace_archival` function, providing the `experiment_id` for which archival should be disabled. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

# Stop archiving traces for the specified experiment
disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

## Related Concepts

- [Delta table](/concepts/delta-lake-table.md) — The storage format for archived trace data.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer that manages the target table.
- [[MLflow Trace|MLflow traces]] — The execution traces stored in the archive.
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for which archival is configured.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Downstream monitoring workflows that can consume archived traces.
- [Building MLflow evaluation datasets](/concepts/evaluation-datasets.md) — Using archived traces to construct evaluation datasets.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
