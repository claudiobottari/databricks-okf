---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75519ff796f41a2f83e82143f974b11f980c0fcf9c4943cb43d8959a1b7f2026
  pageDirectory: concepts
  sources:
    - mlflow-system-tables-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - systemmlflowruns_latest
    - system.mlflow.runs_latest
  citations:
    - file: mlflow-system-tables-reference-databricks-on-aws.md
title: system.mlflow.runs_latest
description: A system table that records run-lifecycle information, params, tags, and aggregated metric statistics (min, max, latest) for MLflow runs.
tags:
  - mlflow
  - databricks
  - table-schema
  - runs
timestamp: "2026-06-19T19:40:27.132Z"
---

# system.mlflow.runs_latest

The **`system.mlflow.runs_latest`** table is one of the [MLflow System Tables](/concepts/mlflow-system-tables.md) that captures metadata about MLflow runs across all workspaces within a region. It records run-lifecycle information, the params and tags associated with each run, and aggregated statistics (minimum, maximum, and latest values) of all metrics logged on that run. The data in this table is similar to what you see on the runs search page or runs detail page in the MLflow UI. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Available columns

Based on the documented sample queries and the description of the table, `system.mlflow.runs_latest` includes at least the following columns:

- `run_id` – Unique identifier for the run.
- `experiment_id` – The experiment the run belongs to.
- `run_name` – The name of the run.
- `status` – Run lifecycle status (e.g., `FINISHED`, `FAILED`).
- `start_time` – Timestamp when the run started.
- `end_time` – Timestamp when the run ended.
- Params, tags, and aggregated metric stats (min, max, latest values) are also recorded.

For the full schema, see the [MLflow system tables reference](/concepts/mlflow-system-tables.md) and the accompanying ER diagram. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Usage examples

The table is frequently used in analytical queries and Databricks SQL alerts. Example use cases include:

- **Run information retrieval** – Get the name, status, and duration of a specific run by filtering on `experiment_id` and `run_id`. ^[mlflow-system-tables-reference-databricks-on-aws.md]
- **Experiment reliability monitoring** – Calculate the success ratio (`FINISHED` / total runs) per experiment to identify experiments with low reliability. This can be paired with [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) to trigger notifications when the ratio falls below a threshold. ^[mlflow-system-tables-reference-databricks-on-aws.md]
- **Joining with other tables** – `system.mlflow.runs_latest` is often joined with system.mlflow.experiments_latest to enrich run data with experiment names, and with system.mlflow.run_metrics_history to retrieve detailed time-series metrics. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Access and governance

By default, only account admins have access to the `system.mlflow` schema. To grant other users access, an admin must grant `USE` and `SELECT` permissions on the schema. Because the table contains metadata from *all* workspaces in the region, access should be carefully managed. Finer-grained control can be achieved by creating [dynamic views](/concepts/opensharing-views.md) that filter rows based on experiment IDs or other criteria. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Related concepts

- [MLflow tracking service](/concepts/remote-mlflow-tracking-server.md)
- system.mlflow.experiments_latest
- system.mlflow.run_metrics_history
- Databricks SQL
- [Unity Catalog privileges reference](/concepts/privileges-and-ownership.md)

## Sources

- mlflow-system-tables-reference-databricks-on-aws.md

# Citations

1. [mlflow-system-tables-reference-databricks-on-aws.md](/references/mlflow-system-tables-reference-databricks-on-aws-4d1f3c50.md)
