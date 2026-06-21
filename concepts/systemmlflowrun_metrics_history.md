---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6d55be699111f72e712037a2a8c5e5dffa9a7e43ea0068c92d338bae7bce684
  pageDirectory: concepts
  sources:
    - mlflow-system-tables-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - systemmlflowrun_metrics_history
    - system.mlflow.run_metrics_history
  citations:
    - file: mlflow-system-tables-reference-databricks-on-aws.md
title: system.mlflow.run_metrics_history
description: A system table that records the name, value, timestamp, and step of all metrics logged on runs, enabling detailed timeseries analysis.
tags:
  - mlflow
  - databricks
  - table-schema
  - metrics
timestamp: "2026-06-19T19:40:36.586Z"
---

# system.mlflow.run_metrics_history

The `system.mlflow.run_metrics_history` table records the name, value, timestamp, and step of every metric logged on MLflow runs. It is one of the core [MLflow System Tables](/concepts/mlflow-system-tables.md) and is designed for time‑series analysis of run metrics, similar to the data shown on the **Metrics** tab of the [run details page](https://docs.databricks.com/aws/en/mlflow/runs). ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Schema and Contents

Each row in `run_metrics_history` corresponds to a single metric value logged at a particular point during a run. The table captures the following elements:

- **metric_name** – the name of the metric (e.g., `accuracy`, `loss`).
- **metric_value** – the numeric value recorded.
- **metric_time** – the timestamp when the metric was logged.
- **step** – the training step (epoch, batch, etc.) associated with the value.

This schema allows users to reconstruct the full evolution of a metric over the duration of a run, enabling detailed time‑series plots and trend analysis. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Data Availability

The `mlflow` system tables began recording data from all regions on **September 2, 2025**. Metric entries from before that date may not be present in the table. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Common Use Cases

- **Plotting metric histories** – Create line charts showing how training loss or accuracy changed over steps.
- **Summary statistics** – Compute averages, percentiles, minima, and maxima for any metric across a run.
- **Drift detection** – Compare metric distributions between runs or experiments.
- **Dashboarding** – Build AI/BI dashboards on top of metric time‑series data across workspaces.

## Sample Query: Summary Statistics for a Run

The following query returns key statistics for each metric logged in a given run:

```sql
SELECT
  metric_name,
  count(metric_time) AS num_data_points,
  ROUND(avg(metric_value), 1) AS avg,
  ROUND(max(metric_value), 1) AS max,
  ROUND(min(metric_value), 1) AS min,
  ROUND(PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY metric_value), 1) AS pct_25,
  ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY metric_value), 1) AS median,
  ROUND(PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY metric_value), 1) AS pct_75
FROM system.mlflow.run_metrics_history
WHERE run_id = :run_id
GROUP BY metric_name, run_id
LIMIT 100;
```

The result includes the number of data points, average, min, max, and quartile values for each metric. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Access and Permissions

Only [account admins](/concepts/account-admin-unity-catalog.md) can grant access to `system.mlflow.*` tables. Users who have been granted `USE` and `SELECT` permissions on the `system.mlflow` schema can view metadata across all MLflow experiments for all workspaces in the account. For finer‑grained control, administrators can create [dynamic views](/concepts/opensharing-views.md) that filter records based on experiment IDs or other criteria. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Related Concepts

- system.mlflow.runs_latest – Contains run lifecycle information and aggregated metric stats.
- system.mlflow.experiments_latest – Records experiment names and soft‑deletion events.
- [MLflow tracking service](/concepts/remote-mlflow-tracking-server.md) – The underlying service that ingests metrics.
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) – Can be configured on queries against `run_metrics_history`.
- AI/BI dashboards – Built on top of system table data for visualization.

## Sources

- mlflow-system-tables-reference-databricks-on-aws.md

# Citations

1. [mlflow-system-tables-reference-databricks-on-aws.md](/references/mlflow-system-tables-reference-databricks-on-aws-4d1f3c50.md)
