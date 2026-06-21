---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 178decab4211bdbc2baa7ab2beacd6b22a14011ad45fb9c5f5048c6f3e209e96
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection-alert
    - ADA
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Anomaly Detection Alert
description: A Databricks feature that notifies users when anomaly detection identifies data quality issues such as stale tables or unexpected drops in row count.
tags:
  - data-quality
  - monitoring
  - alerting
  - databricks
timestamp: "2026-06-19T17:31:51.799Z"
---

# Anomaly Detection Alert

**Anomaly Detection Alert** is a notification mechanism in Databricks that informs users when [Anomaly Detection](/concepts/anomaly-detection.md) identifies a data quality issue, such as a stale table or an unexpected drop in row count. Alerts help teams respond quickly to data quality problems in monitored tables. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Overview

Anomaly detection alerts notify selected workspace users by email when an unhealthy table is detected. Users can work with alerts in two ways: through the Data Quality Monitoring UI (Beta) or by configuring alerts with Databricks SQL queries against the anomaly detection output system table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Alerts in the Data Quality Monitoring UI

The Data Quality Monitoring UI provides a visual interface for creating and managing alert rules. This feature is in Beta and is visible to all users by default; workspace admins do not need to enable it from the Previews page. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Scope and Behavior

Each alert rule is scoped to a catalog or a specific schema. When a monitored table within the rule's scope becomes unhealthy, each recipient receives one email per important unhealthy table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Required Permissions

The privileges required to create or manage an alert rule depend on the rule's scope:

- To create a **schema-level alert**, you must have the `MANAGE` privilege on the schema.
- To create a **catalog-level alert**, you must have the `MANAGE` privilege on the catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Viewing and Managing Alerts

To view alert rules:

1. Navigate to a schema in [Catalog Explorer](/concepts/catalog-explorer.md). Data quality monitoring must be enabled for this schema.
2. Click the **Details** tab. Next to **Data Quality Monitoring**, click **View results** to open the Data Quality Monitoring UI.
3. In the upper-right corner, click **Manage alerts** to see existing alert rules, including the catalog, schema, and number of recipients for each rule.

From the Manage alerts popover, users can create new alert rules, edit existing rules' scope and recipients, or delete alerts. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Creating an Alert in the UI

To create an alert:

1. In the Data Quality Monitoring UI, click **Manage alerts**.
2. Click **Create alert**.
3. Configure the alert rule:
   - **Catalog**: Select the catalog to monitor.
   - **Schema**: Select a specific schema, or select **All Schemas** to create a catalog-level alert covering every schema in the catalog.
   - **Notify**: Search for and select one or more workspace users to notify by email.
4. Click **Save**.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Creating an Alert with Databricks SQL

For advanced filtering and custom notification templates, users can configure alerts by querying the anomaly detection output system table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Access Requirements

By default, only account admins can access the system table `system.data_quality_monitoring.table_results`. If other users need to configure alerts, appropriate access must be granted. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Steps

1. Click **Alerts** in the sidebar and click **Create alert**.
2. Enter a query in the query editor. The following example query checks for unhealthy tables in the last 6 hours:

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

3. Run the query.
4. Using the alert editor on the right side of the screen, configure the alert condition.
5. (Optional) To customize the email template, open the **Advanced** tab and check **Customize template** to open the template editor. An example custom email template is available in the documentation. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Legacy Beta Jobs Note

For legacy beta jobs, existing alert configuration should replace `system.data_quality_monitoring.table_results` with `<catalog>.<schema>._quality_monitoring_summary`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The underlying detection system that identifies data quality issues
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for monitoring table health
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where monitored tables reside
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) — The alerting infrastructure used for SQL-based alert configuration
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI tool for navigating and managing data assets

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
