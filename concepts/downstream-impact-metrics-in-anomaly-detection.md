---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce791e959a7ebd4f2ca57165c214bf0ea9765ab8612bbc8e29045bc02c0662c5
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - downstream-impact-metrics-in-anomaly-detection
    - DIMIAD
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Downstream Impact Metrics in Anomaly Detection
description: Concept of measuring the impact of data quality issues by tracking the number of queries affected on unhealthy tables, used as a trigger threshold for alerts.
tags:
  - databricks
  - metrics
  - data-quality
  - impact-analysis
timestamp: "2026-06-19T22:04:46.830Z"
---

# Downstream Impact Metrics in Anomaly Detection

**Downstream Impact Metrics in Anomaly Detection** are statistical measures that quantify the real-world effect of a data quality anomaly on downstream consumers, such as queries or dashboards that depend on the affected table. These metrics help prioritize which anomalies to address by providing business context beyond whether a table is simply "unhealthy."

## Overview

In [Anomaly Detection](/concepts/anomaly-detection.md) on Databricks, the `downstream_impact` field captures the practical consequences of a data quality violation. The most commonly tracked metric is the number of queries on affected tables, which indicates how many downstream processes are impacted by a stale, incomplete, or anomalous table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Key Metrics

The primary downstream impact metric available in the anomaly detection output is:

- **`num_queries_on_affected_tables`**: The count of queries that have been run against tables affected by the detected anomaly. This provides a direct measure of the blast radius of a data quality issue. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Usage in Alerting

Downstream impact metrics are particularly useful when configuring Alerts for Anomaly Detection. By filtering on the impact metric, users can ensure that notifications are only sent when an anomaly affects a meaningful number of downstream consumers, reducing alert fatigue. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### SQL Alert Example

When creating a Databricks SQL alert, users can query the `system.data_quality_monitoring.table_results` system table and filter by downstream impact:

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
SELECT
  evaluated_at,
  full_table_name,
  status,
  commit_expected,
  commit_actual,
  completeness_expected,
  completeness_actual,
  impacted_queries
FROM rounded_data
WHERE
  evaluated_at >= current_timestamp() - INTERVAL 6 HOURS
  AND impacted_queries > :min_tables_affected
  AND status = 'Unhealthy';
```

^[alerts-for-anomaly-detection-databricks-on-aws.md]

The `:min_tables_affected` parameter allows users to set a minimum threshold for the number of affected queries before triggering an alert, providing fine-grained control over notification sensitivity. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Custom Email Templates

Downstream impact metrics can be included in custom email notification templates to give recipients immediate context about the severity of an anomaly:

```
Impact (queries): {{impacted_queries}}
```

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Relationship to Other Quality Metrics

Downstream impact metrics complement other [Anomaly Detection Metrics](/concepts/anomaly-detection-databricks.md) such as:

- **Freshness metrics** (e.g., `commit_freshness`) — How stale a table has become
- **Completeness metrics** (e.g., `daily_row_count`) — Unexpected drops in row volume

While freshness and completeness indicate *what* is wrong with a table, downstream impact metrics indicate *how many people or processes* are affected by the issue. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — Overview of detecting data quality issues
- Alerts for Anomaly Detection — Configuring notifications based on anomaly results
- [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md) — Visual interface for managing quality checks
- System Tables — Metadata tables storing anomaly detection results
- [Freshness Metrics](/concepts/freshness-data-quality-metric.md) — Measures of data staleness
- [Completeness Metrics](/concepts/completeness-data-quality-metric.md) — Measures of data row volume expectations

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
