---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f817fdcfc1c85dd7580e95923a755676d90f1437ba67d9ba223d79b43b52ed6
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection-alerts
    - ADA
    - Advanced settings for alerts
    - advanced settings for alerts
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Anomaly Detection Alerts
description: Notifications triggered when Databricks anomaly detection identifies data quality issues such as stale tables or unexpected drops in row count.
tags:
  - databricks
  - data-quality
  - alerting
  - anomaly-detection
timestamp: "2026-06-19T13:58:53.624Z"
---

# Anomaly Detection Alerts

**Anomaly Detection Alerts** are automated notifications that flag data quality issues identified by [Anomaly Detection](/concepts/anomaly-detection.md) in Unity Catalog. Alerts help teams respond quickly to problems such as stale tables, unexpected drops in row count, or other deviations from expected data quality patterns. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Overview

When anomaly detection identifies an unhealthy table — for example, a table that has not been updated within its expected freshness window or that shows an abnormal decrease in row volume — alerts notify designated workspace users by email. Databricks supports two methods for configuring these alerts: the Data Quality Monitoring UI (Beta) and Databricks SQL queries. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Alerts in the Data Quality Monitoring UI

The Data Quality Monitoring UI provides a visual interface for creating and managing alert rules. This feature is in Beta and is visible to all users by default — workspace admins do not need to enable it from the **Previews** page. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

Each alert rule is scoped to a catalog or a specific schema. When a monitored table within the rule's scope becomes unhealthy, each recipient receives one email per important unhealthy table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Required Permissions

- To create a **schema-level** alert, you must have the `MANAGE` privilege on the schema.
- To create a **catalog-level** alert, you must have the `MANAGE` privilege on the catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Viewing and Managing Alerts

1. Navigate to a schema in Catalog Explorer. Data quality monitoring must be enabled for this schema.
2. Click the **Details** tab. Next to **Data Quality Monitoring**, click **View results** to open the Data Quality Monitoring UI.
3. In the upper-right corner, click **Manage alerts** to open a popover showing existing alert rules, including the catalog, schema, and number of recipients for each rule.

From this popover, you can create a new alert rule, select an existing alert to edit its scope and recipients, or delete an alert. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Creating an Alert in the UI

1. In the Data Quality Monitoring UI, click **Manage alerts**.
2. Click **Create alert**.
3. Configure the alert rule:
   - **Catalog**: Select the catalog to monitor.
   - **Schema**: Select a specific schema, or select **All Schemas** to create a catalog-level alert covering every schema in the catalog.
   - **Notify**: Search for and select one or more workspace users to notify by email.
4. Click **Save**.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Create an Alert with Databricks SQL

For advanced filtering and custom notification templates, alerts can be configured by querying the anomaly detection output system table.

### Prerequisites

By default, only account admins can access the system table `system.data_quality_monitoring.table_results`. If other users need to configure alerts, grant appropriate access. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Steps

1. Click **Alerts** in the sidebar and click **Create alert**.
2. Enter the following query in the query editor:

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

> **Note:** For legacy beta jobs, replace `system.data_quality_monitoring.table_results` with `<catalog>.<schema>._quality_monitoring_summary`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

3. Run the query.
4. Using the alert editor on the right side, configure the trigger condition (e.g., threshold for `impacted_queries`).
5. (Optional) To customize the email template, open the **Advanced** tab and check **Customize template**. An example custom HTML template is shown in the source documentation.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The underlying detection mechanism that identifies data quality issues
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where monitored tables and schemas reside
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for tracking table health
- System Tables — System-available tables for monitoring and alerting
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) — The alerting infrastructure used for SQL-based anomaly alerts

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
