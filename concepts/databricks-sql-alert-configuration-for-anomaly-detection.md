---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5ae6e073c396add6435169f54a3a2f2744574c048067d8257547bdbe669749b
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sql-alert-configuration-for-anomaly-detection
    - DSACFAD
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Databricks SQL Alert Configuration for Anomaly Detection
description: A method for creating anomaly detection alerts by querying the system.data_quality_monitoring.table_results system table with custom SQL, supporting advanced filtering, trigger conditions, and custom notification templates.
tags:
  - data-quality
  - alerting
  - sql
  - system-tables
  - databricks
timestamp: "2026-06-19T17:32:06.083Z"
---

---
title: Databricks SQL Alert Configuration for Anomaly Detection
summary: Creating custom alerts by querying the system.data_quality_monitoring.table_results system table with SQL, supporting advanced filtering and custom notification templates.
sources:
  - alerts-for-anomaly-detection-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T08:57:39.474Z"
updatedAt: "2026-06-19T13:58:27.436Z"
tags:
  - databricks
  - sql
  - alerting
  - system-tables
aliases:
  - databricks-sql-alert-configuration-for-anomaly-detection
  - DSACFAD
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks SQL Alert Configuration for Anomaly Detection

**Databricks SQL Alert Configuration for Anomaly Detection** refers to the process of creating email notifications that trigger when anomaly detection identifies a data quality issue — such as stale tables, unexpected drops in row count, or other unhealthy conditions. While alerts can also be managed through the Data Quality Monitoring UI (Beta), the SQL approach queries the anomaly detection output system table and supports advanced filtering and custom notification templates. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Overview

Alerts notify selected workspace users when a monitored table becomes unhealthy. The SQL-based method gives administrators full control over the query logic, thresholds, and email formatting by querying the `system.data_quality_monitoring.table_results` system table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Required Permissions

By default, only account admins have access to the system table `system.data_quality_monitoring.table_results`. If non-admin users need to configure alerts, appropriate access must be granted to that table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Creating an Alert with Databricks SQL

The SQL method allows you to define precise trigger conditions and customize the email notification. The general workflow is:

1. Click **Alerts** in the sidebar and click **Create alert**.
2. Enter an SQL query that selects anomaly detection results and filters for unhealthy status.
3. Run the query and configure the alert condition (trigger threshold).
4. Optionally customize the email template using HTML.

### Example Query

The following sample query retrieves stale tables or row-count violations detected in the last six hours, filtering by the number of impacted queries: ^[alerts-for-anomaly-detection-databricks-on-aws.md]

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
  -- enter the minimum number of table violations before the alert is triggered
  AND impacted_queries > :min_tables_affected
  AND status = 'Unhealthy';
```

This query aggregates data by hour and shows the expected vs. actual staleness and row volume for each unhealthy table, along with the number of impacted downstream queries. The parameter `:min_tables_affected` lets you set a dynamic threshold in the alert editor. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

> **Note for legacy beta jobs**: If you are using a legacy beta monitoring setup, replace `system.data_quality_monitoring.table_results` with `<catalog>.<schema>._quality_monitoring_summary`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Configuring the Trigger Condition

After running the query, use the alert editor on the right side of the screen to define the condition. This typically includes choosing the aggregate value and comparison operator (e.g., trigger when the number of unhealthy tables > `0`). For full details, see Create an alert in Databricks SQL. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Customizing the Email Template

On the **Advanced** tab of the alert editor, you can enable a custom HTML template to format the alert email. A sample template that displays a table of failing quality checks is shown below: ^[alerts-for-anomaly-detection-databricks-on-aws.md]

```html
<h4>The following tables are failing quality checks in the last hour</h4>
<table>
  <tr>
    <td>
      <table>
        <tr>
          <th>Table</th>
          <th>Expected Staleness</th>
          <th>Actual Staleness</th>
          <th>Expected Row Volume</th>
          <th>Actual Row Volume</th>
          <th>Impact (queries)</th>
        </tr>
        {{#QUERY_RESULT_ROWS}}
        <tr>
          <td>{{full_table_name}}</td>
          <td>{{commit_expected}}</td>
          <td>{{commit_actual}}</td>
          <td>{{completeness_expected}}</td>
          <td>{{completeness_actual}}</td>
          <td>{{impacted_queries}}</td>
        </tr>
        {{/QUERY_RESULT_ROWS}}
      </table>
    </td>
  </tr>
</table>
```

The template iterates over the rows returned by the alert query and inserts the column values using `{{#QUERY_RESULT_ROWS}}` and `{{column_name}}` placeholders. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The underlying system that computes health status and metrics.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Enable monitoring on schemas to generate the anomaly detection output.
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) – General alerting framework in Databricks SQL.
- System Tables – Metadata tables such as `system.data_quality_monitoring.table_results`.

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
