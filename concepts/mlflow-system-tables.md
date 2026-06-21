---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0411f0a175ce7782d5156da711fae537ce5652b02bc4e34bcad606b14c6c4ec1
  pageDirectory: concepts
  sources:
    - mlflow-system-tables-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-system-tables
    - MST
    - MLflow System Tables Reference
    - MLflow metadata in system tables
    - MLflow system tables reference
    - System Tables for ML
    - system tables
  citations:
    - file: mlflow-system-tables-reference-databricks-on-aws.md
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: MLflow System Tables
description: System tables in Databricks that capture MLflow experiment metadata across all workspaces in a region, enabling large-scale analytics via SQL and dashboards.
tags:
  - mlflow
  - databricks
  - system-tables
  - metadata
timestamp: "2026-06-19T19:40:22.218Z"
---

# MLflow System Tables

**MLflow System Tables** are Databricks system tables that capture experiment and run metadata managed by the [MLflow tracking service](/concepts/remote-mlflow-tracking-server.md) across all workspaces within a region. They allow privileged users to query MLflow data using standard SQL, build custom dashboards, set up alerts, and perform large‑scale analytical analyses without relying solely on the MLflow UI or REST APIs. ^[mlflow-system-tables-reference-databricks-on-aws.md]

Through the `mlflow` system tables, users can answer questions such as which experiments have the lowest reliability or what the average GPU utilization is across different experiments. ^[mlflow-system-tables-reference-databricks-on-aws.md]

> **Note**: The `mlflow` system tables began recording data from all regions on **September 2, 2025**. Data from before that date may not be available. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Available Tables

The schema `system.mlflow` includes three tables:

- **`system.mlflow.experiments_latest`** – Records experiment names and soft‑deletion events. The content is similar to the experiments page in the MLflow UI. ^[mlflow-system-tables-reference-databricks-on-aws.md]
- **`system.mlflow.runs_latest`** – Records run‑lifecycle information, parameters, tags, and aggregated metric statistics (min, max, latest). The content is similar to the runs search or runs detail page. ^[mlflow-system-tables-reference-databricks-on-aws.md]
- **`system.mlflow.run_metrics_history`** – Records the name, value, timestamp, and step of all logged metrics, enabling detailed time‑series plotting. The content is similar to the metrics tab on the runs detail page. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Table Schemas

The entity‑relationship diagram below shows the relationships between the three tables:

![Entity‑relationship diagram for MLflow system tables](https://docs.databricks.com/aws/en/assets/images/er-diagram-8687a2649617fa4db6f86ea4604bfbdc.svg)

^[mlflow-system-tables-reference-databricks-on-aws.md]

### `system.mlflow.experiments_latest`

| Column Name       | Type      | Description                                       |
|-------------------|-----------|---------------------------------------------------|
| `experiment_id`   | STRING    | Unique identifier for the experiment.             |
| `name`            | STRING    | User‑provided name of the experiment.             |
| `artifact_location` | STRING  | Location where artifacts for the experiment are stored. |
| `lifecycle_stage` | STRING    | Current lifecycle stage (e.g., “active” or “deleted”). |
| `creation_time`   | TIMESTAMP | Time the experiment was created.                  |
| `last_update_time`| TIMESTAMP | Time the experiment was last updated.             |

### `system.mlflow.runs_latest`

| Column Name      | Type                   | Description                                      |
|------------------|------------------------|--------------------------------------------------|
| `run_id`         | STRING                 | Unique identifier for the run.                   |
| `experiment_id`  | STRING                 | Foreign key to the experiment.                   |
| `run_name`       | STRING                 | User‑provided name for the run.                  |
| `status`         | STRING                 | Run status (e.g., RUNNING, FINISHED, FAILED).    |
| `start_time`     | TIMESTAMP              | Time the run started.                            |
| `end_time`       | TIMESTAMP              | Time the run finished.                           |
| `user_id`        | STRING                 | User who created the run.                        |
| `params`         | MAP<STRING,STRING>     | Parameters logged for the run.                   |
| `tags`           | MAP<STRING,STRING>     | Tags associated with the run.                    |
| `lifecyle_stage` | STRING                 | Lifecycle stage (e.g., “active” or “deleted”).   |
| `min_metrics`    | MAP<STRING,DOUBLE>     | Minimum value for each metric.                   |
| `max_metrics`    | MAP<STRING,DOUBLE>     | Maximum value for each metric.                   |
| `latest_metrics` | MAP<STRING,DOUBLE>     | Most recent value for each metric.               |

### `system.mlflow.run_metrics_history`

| Column Name      | Type      | Description                                         |
|------------------|-----------|-----------------------------------------------------|
| `run_id`         | STRING    | Foreign key to the run.                             |
| `metric_key`     | STRING    | Name of the metric.                                 |
| `metric_value`   | DOUBLE    | Value of the metric at a given step and timestamp.  |
| `metric_timestamp`| TIMESTAMP| When the metric was logged.                         |
| `metric_step`    | BIGINT    | Step number at which the metric was logged.         |

^[mlflow-system-tables-reference-databricks-on-aws.md]

## Sharing Access with Users

By default, only account admins have access to system schemas. To grant additional users access to the `system.mlflow` tables, an account admin must grant them `USE` and `SELECT` permissions on the schema. See [Unity Catalog privileges reference](/concepts/privileges-and-ownership.md). ^[mlflow-system-tables-reference-databricks-on-aws.md]

**Any user with access to these tables can view metadata across all MLflow experiments for all workspaces in the account.** To configure table access for a group rather than individual users, see Unity Catalog best practices. ^[mlflow-system-tables-reference-databricks-on-aws.md]

If finer‑grained control is required, use [dynamic views](/concepts/opensharing-views.md) with custom criteria. For example, create a view that only shows records from a particular set of experiment IDs, then give users the name of that dynamic view to query instead of the system table directly. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Example Use Cases

### Build a Dashboard for Single Run Details

Using the MLflow system tables, you can build an AI/BI dashboard that reproduces the information on the [MLflow Run](/concepts/mlflow-run.md) details page. Download [this example dashboard](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) as a JSON file and import it into your workspace. For a given experiment ID, run ID, and metric name, the dashboard shows run details, tags, parameters, and a metric graph. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

You can obtain the experiment ID and run ID from the run details page URL: `https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>`. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Monitor Average GPU Utilization Across Experiments

Input a metric name to get summary statistics across all experiments that log that metric within a given time window. This is useful for monitoring system metrics (e.g., GPU, CPU, memory) recorded by MLflow to detect inefficient utilization. The example below shows several experiments with average GPU utilization below 10% that may warrant investigation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

![Dashboard showing average GPU utilization per experiment](https://docs.databricks.com/aws/en/assets/images/dashboard-gpu-utilization-6d32069b826aad9ed769ef394b34dd76.png)

### Configure a SQL Alert for Low Experiment Reliability

Using [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md), schedule a regularly recurring query that checks the success ratio of frequently run experiments. The example below calculates the fraction of runs that finished successfully and triggers an alert if any of the top 20 experiments has a success ratio below 90%. ^[mlflow-system-tables-reference-databricks-on-aws.md]

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

Set the alert condition to `MIN success_ratio < 0.9`. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Sample Queries

### Get Run Information from `runs_latest`

```sql
SELECT
  run_name,
  date(start_time) AS start_date,
  status,
  TIMESTAMPDIFF(MINUTE, start_time, end_time) AS run_length_minutes
FROM system.mlflow.runs_latest
WHERE
  experiment_id = :experiment_id
  AND run_id = :run_id
LIMIT 1
```

^[mlflow-system-tables-reference-databricks-on-aws.md]

### Get Experiment and Run Information from `experiments_latest` and `runs_latest`

```sql
SELECT
  runs.run_name,
  experiments.name,
  date(runs.start_time) AS start_date,
  runs.status,
  TIMESTAMPDIFF(MINUTE, runs.start_time, runs.end_time) AS run_length_minutes
FROM system.mlflow.runs_latest runs
  JOIN system.mlflow.experiments_latest experiments
    ON runs.experiment_id = experiments.experiment_id
WHERE
  runs.experiment_id = :experiment_id
  AND runs.run_id = :run_id
LIMIT 1
```

^[mlflow-system-tables-reference-databricks-on-aws.md]

### Get Summary Statistics from `run_metrics_history`

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
FROM
  system.mlflow.run_metrics_history
WHERE
  run_id = :run_id
GROUP BY
  metric_name, run_id
LIMIT 100
```

^[mlflow-system-tables-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) – Core logging service that populates the system tables.
- AI/BI Dashboards – Tool for building visualizations on top of system table data.
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) – Mechanism for monitoring system table metrics.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for managing system table access.
- [Account Admin (Unity Catalog)](/concepts/account-admin-unity-catalog.md) – Role required to grant initial access.
- Dynamic Views – Way to implement fine‑grained access control.
- [Experiments (MLflow)](/concepts/active-experiment-in-mlflow.md) – Organizational unit for runs.
- Runs (MLflow) – Individual execution records.

## Sources

- mlflow-system-tables-reference-databricks-on-aws.md
- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [mlflow-system-tables-reference-databricks-on-aws.md](/references/mlflow-system-tables-reference-databricks-on-aws-4d1f3c50.md)
2. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
