---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0c0014521e04de9f3ab4ec87d4b306435ba3cbbbbd718f3946b65d7e5c7e7d2b
  pageDirectory: concepts
  sources:
    - migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-to-unity-catalog-trace-migration
    - MTUCTM
  citations:
    - file: migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
title: MLflow to Unity Catalog Trace Migration
description: A process for copying traces, spans, assessments, tags, and metadata from an MLflow experiment into Unity Catalog Delta tables, removing trace storage limits and enabling fine-grained access control.
tags:
  - mlflow
  - unity-catalog
  - tracing
  - migration
timestamp: "2026-06-19T19:33:02.384Z"
---

## MLflow to Unity Catalog Trace Migration

**MLflow to Unity Catalog Trace Migration** is the process of copying traces stored in an [MLflow Experiment](/concepts/mlflow-experiment.md) to [Unity Catalog](/concepts/unity-catalog.md) Delta tables. Storing traces in Unity Catalog removes trace storage limits, provides fine-grained access controls through Unity Catalog governance, and makes traces queryable from notebooks, SQL, Genie, AI/BI dashboards, and any Spark-based tool. The migration copies traces, spans, assessments, tags, and metadata from the source experiment to Unity Catalog tables; the source experiment is not modified. Archived or deleted traces, dataset records, labeling sessions, runs, and non-trace entities are **not** copied. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Prerequisites

Before performing the migration, you need:

- A Unity Catalog‑enabled workspace.
- A Databricks Runtime cluster running version 15.3 or above.
- The `databricks-agents` Python package (version ≥1.10.1), installed via `pip install "databricks-agents>=1.10.1"`.
- Read access to the source experiment, and `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` permissions on the destination [Catalog and Schema](/concepts/catalog-and-schema.md). ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Step 1: Create a Destination Experiment

The destination is a new MLflow experiment bound to a Unity Catalog trace location. The trace location is a three-part path (`catalog.schema.table_prefix`). The table prefix is applied to the four Delta tables that back the experiment:

- `<prefix>_otel_spans`
- `<prefix>_otel_annotations`
- `<prefix>_otel_logs`
- `<prefix>_otel_metrics`

Use `mlflow.set_experiment()` with a `trace_location` parameter of type `UnityCatalog` to create the destination experiment. Save the returned experiment ID; it is needed in the subsequent steps. You may optionally ingest a few test traces into the new experiment to verify that Unity Catalog tracing works for your workflow before proceeding. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Step 2: Switch Trace Logging and Stop Writes to the Source

Before running the migration, redirect all trace logging to the destination experiment and stop all writes to the source experiment. Any traces written to the source during the migration might not be copied. Replace any existing `set_experiment` call that points to the source experiment with one that points to the destination experiment, either by name or by ID. For deployed applications, containerized services, or model serving endpoints, also adjust environment variables such as `MLFLOW_EXPERIMENT_NAME` or `MLFLOW_EXPERIMENT_ID`. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Step 3: Run the Migration

In a Databricks notebook on the cluster, run the following:

```python
from databricks.migrations.migrate_traces_to_uc import run
run(
    source_experiment_id="<source_experiment_id>",
    target_experiment_id="<destination_experiment_id>",
)
```

Replace `<source_experiment_id>` with the ID of the existing experiment containing the traces, and `<destination_experiment_id>` with the ID of the Unity Catalog‑backed experiment created in Step 1. The migration is **idempotent** — if interrupted (for example, by a cluster timeout), you can safely rerun the same command and it will resume from where it left off, skipping already‑migrated rows. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

To migrate only traces created after a specific time, pass the `start_time_ms` parameter (epoch milliseconds). The migration will ingest all traces with a request time at or after the specified timestamp, skipping any that have already been migrated. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### After Migration

Once the migration completes, the traces are available in the new destination experiment. The source experiment is not modified and can be retained as a backup. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — Data governance platform for managing and securing data assets.
- [MLflow Experiment](/concepts/mlflow-experiment.md) — Organizational unit for MLflow runs and traces.
- [Trace location](/concepts/trace-mlflow-evaluation.md) — Configuration that determines where traces are stored.
- [Delta tables](/concepts/delta-lake-table.md) — Storage format used by Unity Catalog for trace data.
- [Genie](/concepts/genie-code.md) — Databricks natural‑language query interface.
- AI/BI dashboards — Databricks dashboards for analytics and reporting.
- Databricks Runtime — The runtime environment for clusters.

### Sources

- migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md](/references/migrate-experiment-traces-to-unity-catalog-databricks-on-aws-a625531c.md)
