---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dfabc40c8f7e68596054df55f5977d78d91141c8d044ee5b4b658435619e3fee
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection-output-system-table
    - ADOST
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Anomaly Detection Output System Table
description: The system table system.data_quality_monitoring.table_results that stores anomaly detection output results and can be queried for alert configuration, with legacy beta jobs using an alternative table path.
tags:
  - databricks
  - system-table
  - data-quality
  - monitoring
timestamp: "2026-06-19T08:57:44.653Z"
---

# Anomaly Detection Output System Table

The **Anomaly Detection Output System Table** is a Databricks system table that stores the results of [Anomaly Detection](/concepts/anomaly-detection.md) checks run by [Data Quality Monitoring](/concepts/data-quality-monitoring.md) in Unity Catalog. It is accessible as `system.data_quality_monitoring.table_results` and contains freshness, completeness, and downstream impact metrics for each monitored table. This table enables users to programmatically query the health status of tables and configure custom alerts via [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md). ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Schema and Key Columns

The following columns are used in the alert query example and are part of the table schema: ^[alerts-for-anomaly-detection-databricks-on-aws.md]

- `event_time` – Timestamp of the check evaluation.
- `catalog_name`, `schema_name`, `table_name` – Three-level namespace identifying the monitored table.
- `status` – Health status (e.g., `Unhealthy`).
- `downstream_impact.num_queries_on_affected_tables` – Number of queries potentially affected by the quality issue.
- `freshness.commit_freshness.predicted_value` – Expected staleness (commit freshness) predicted by the anomaly detection model.
- `freshness.commit_freshness.last_value` – Actual observed staleness.
- `completeness.daily_row_count.min_predicted_value` – Lower bound of the predicted daily row count.
- `completeness.daily_row_count.last_value` – Actual last observed row count.

These columns allow comparison of expected vs. actual values for both freshness and completeness, providing a quantitative basis for alerting. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Access Control

By default, only account admins can access `system.data_quality_monitoring.table_results`. Workspace admins must grant appropriate privileges to other users who need to configure alerts. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Usage for Alerting

The primary use of this system table is to create custom alerts in Databricks SQL. A typical query filters for unhealthy tables within a recent time window (e.g., 6 hours) and aggregates by hour, comparing expected vs. actual metrics. The alert can be parameterized with a threshold for the minimum number of affected queries (`:min_tables_affected`) to reduce noise. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

Example query:

```sql
WITH rounded_data AS (
  SELECT
    DATE_TRUNC('HOUR', event_time) AS evaluated_at,
    CONCAT(catalog_name, '.', schema_name, '.', table_name) AS full_table_name,
    status,
    MAX(downstream_impact.num_queries_on_affected_tables) AS impacted_queries,
    MAX(freshness.commit_freshness.predicted_value) AS commit_expected,
    MAX(freshness.commit_freshness.last_value) AS commit_actual,
    MAX(completeness.daily_row_count.min_predicted_value) AS completeness_expected,
    MAX(completeness.daily_row_count.last_value) AS completeness_actual
  FROM system.data_quality_monitoring.table_results
  GROUP BY ALL
)
SELECT ...
WHERE evaluated_at >= current_timestamp() - INTERVAL 6 HOURS
  AND impacted_queries > :min_tables_affected
  AND status = 'Unhealthy';
```

The results can populate a custom email notification template that shows the table name, expected vs. actual freshness, expected vs. actual row volume, and query impact. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Legacy Beta Jobs

For monitoring configurations created with legacy beta jobs, the output table resides in a user-specified schema under the name `_quality_monitoring_summary` (i.e., `<catalog>.<schema>._quality_monitoring_summary`). Existing alert configurations using this legacy table should be updated to point to `system.data_quality_monitoring.table_results` when migrating. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The underlying machine learning models that generate predicted values.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The framework that manages quality checks and produces the table.
- System Tables – The broader concept of Databricks system tables for operational data.
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) – The alerting tool that queries this table.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer hosting the system table.

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
