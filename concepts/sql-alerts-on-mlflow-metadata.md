---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b481d864173d07f4ceb4c4d753c70b1ba5b857b31b0cf478dedc6553d28db402
  pageDirectory: concepts
  sources:
    - mlflow-system-tables-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sql-alerts-on-mlflow-metadata
    - SAOMM
  citations:
    - file: mlflow-system-tables-reference-databricks-on-aws.md
title: SQL Alerts on MLflow Metadata
description: Using Databricks SQL alerts with MLflow system tables to monitor experiment reliability and be notified when constraints are violated.
tags:
  - mlflow
  - databricks
  - sql-alerts
  - monitoring
timestamp: "2026-06-19T19:40:31.359Z"
---

# SQL Alerts on MLflow Metadata

**SQL Alerts on MLflow Metadata** allow users to schedule recurring queries against [MLflow System Tables](/concepts/mlflow-system-tables.md) and receive notifications when specified conditions are met. These alerts are built on [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) and can be used to proactively monitor the health, performance, and reliability of MLflow experiments across a workspace. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Overview

The `mlflow` system tables (`system.mlflow.experiments_latest`, `system.mlflow.runs_latest`, `system.mlflow.run_metrics_history`) capture experiment metadata from the MLflow tracking service. Privileged users can leverage Databricks lakehouse tooling—including Databricks SQL—to build custom dashboards, run analytical queries, or set up SQL alerts on this data. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Prerequisites

By default, only account admins have access to system schemas. To give other users access to the MLflow system tables, an account admin must grant `USE` and `SELECT` permissions on the `system.mlflow.` schema. Any user with access can view metadata across all MLflow experiments for all workspaces in the account. For finer‑grained control, you can use Dynamic Views to restrict which records specific groups can see. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Example: Alert for Low Experiment Reliability

The following example demonstrates a SQL alert that monitors the most frequently run experiments for low reliability. It uses the `runs_latest` table to calculate the ratio of runs marked as `FINISHED` to the total number of runs. ^[mlflow-system-tables-reference-databricks-on-aws.md]

### Query

```sql
SELECT
  experiment_id,
  AVG(CASE WHEN status = 'FINISHED' THEN 1.0 ELSE 0.0 END) AS success_ratio,
  COUNT(status) AS run_count
FROM system.mlflow.runs_latest
WHERE status IS NOT NULL
GROUP BY experiment_id
ORDER BY run_count DESC
LIMIT 20;
```

^[mlflow-system-tables-reference-databricks-on-aws.md]

### Alert Configuration

1. In the Databricks sidebar, click **Alerts** → **Create Alert**.
2. Paste the query into the query editor.
3. Set the **Condition** to `MIN success_ratio < 0.9`. This triggers the alert if any of the top 20 experiments has a success ratio below 90%.
4. Optionally set a schedule, test the condition, and configure notifications (e.g., email, webhook).

^[mlflow-system-tables-reference-databricks-on-aws.md]

### How the Query Works

- `AVG(CASE WHEN status = 'FINISHED' THEN 1.0 ELSE 0.0 END)` computes the fraction of runs that completed successfully.
- `COUNT(status)` gives the total number of runs per experiment.
- The `WHERE` clause excludes rows with a null status.
- The `ORDER BY run_count DESC LIMIT 20` focuses on the top 20 experiments by number of runs, ensuring the alert monitors the most active experiments.

^[mlflow-system-tables-reference-databricks-on-aws.md]

## Use Cases

- **Reliability monitoring**: Detect experiments where many runs are failing or cancelled.
- **Performance tracking**: Combine with metric history tables to alert on low GPU utilization or long run times.
- **Cost optimization**: Identify experiments with unexpectedly high run counts.

^[mlflow-system-tables-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md) — The underlying tables (`experiments_latest`, `runs_latest`, `run_metrics_history`) that store MLflow metadata.
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) — The alerting mechanism used to define conditions and notifications.
- Dynamic Views — A method to create filtered views of system tables for granular access control.
- Experiment Reliability — A metric derived from the ratio of successful runs to total runs.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational container for runs in MLflow.

## Sources

- mlflow-system-tables-reference-databricks-on-aws.md

# Citations

1. [mlflow-system-tables-reference-databricks-on-aws.md](/references/mlflow-system-tables-reference-databricks-on-aws-4d1f3c50.md)
