---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8eba9e620d77553d083b3cd273a8e229843c34a4146560ff9ac591bf63633541
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - systemdata_quality_monitoringtable_results-system-table
    - SST
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: system.data_quality_monitoring.table_results System Table
description: The Databricks system table that stores anomaly detection output results, containing fields like event_time, catalog_name, schema_name, table_name, status, freshness metrics, completeness metrics, and downstream impact data.
tags:
  - databricks
  - system-tables
  - data-quality
  - monitoring
timestamp: "2026-06-19T22:04:39.498Z"
---

# `system.data_quality_monitoring.table_results` System Table

The **`system.data_quality_monitoring.table_results`** system table stores the output of [Anomaly Detection](/concepts/anomaly-detection.md) evaluations performed by [Data Quality Monitoring](/concepts/data-quality-monitoring.md) in Unity Catalog. It is the primary source of data for creating custom alerts when monitored tables are flagged as unhealthy. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Purpose

This table contains the results of anomaly detection checks on tables that have data quality monitoring enabled. You can query it directly with Databricks SQL to build custom alert triggers, dashboards, or notification templates. For legacy beta jobs, the equivalent table was named `<catalog>.<schema>._quality_monitoring_summary`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Columns

The following columns are used in the documented alert query against `system.data_quality_monitoring.table_results`. Additional columns may exist but are not described in the source material.

| Column | Description |
|--------|-------------|
| `event_time` | Timestamp of the anomaly detection evaluation. |
| `catalog_name` | The catalog containing the monitored table. |
| `schema_name` | The schema containing the monitored table. |
| `table_name` | The name of the monitored table. |
| `status` | Health status of the table (e.g., `'Unhealthy'`). |
| `downstream_impact.num_queries_on_affected_tables` | Number of queries that were impacted by unhealthy tables. |
| `freshness.commit_freshness.predicted_value` | Expected (predicted) most recent commit time. |
| `freshness.commit_freshness.last_value` | Actual most recent commit time detected. |
| `completeness.daily_row_count.min_predicted_value` | Minimum expected row count for the day. |
| `completeness.daily_row_count.last_value` | Actual row count detected. |

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Access control

By default, only [account admin](/concepts/account-admin-unity-catalog.md) users can access `system.data_quality_monitoring.table_results`. To allow other workspace users to query the table (for example, to configure alerts), an account admin must grant appropriate access. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Usage: Creating alerts with Databricks SQL

The primary documented use of this system table is to create alerts via Databricks SQL. The alert query typically joins the anomaly detection status with downstream impact information and filters for unhealthy tables within a recent time window. A minimal query structure is:

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
SELECT *
FROM rounded_data
WHERE evaluated_at >= current_timestamp() - INTERVAL 6 HOURS
  AND impacted_queries > :min_tables_affected
  AND status = 'Unhealthy';
```

The query computes the downstream impact (number of queries on affected tables) and the expected versus actual values for freshness and completeness. This enables triggering alerts only when the impact exceeds a configurable threshold. Custom email templates can reference the result columns (e.g., `{{full_table_name}}`, `{{commit_expected}}`, `{{impacted_queries}}`). ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – the process that populates this system table
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – enables monitoring on schemas and tables
- Alerts for anomaly detection – how to set up alerts using this table or the Data Quality Monitoring UI
- System tables – the broader set of system tables in Unity Catalog
- [Account admin](/concepts/account-admin-unity-catalog.md) – the role that can grant access to this table

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
