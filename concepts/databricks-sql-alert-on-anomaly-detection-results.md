---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2fbf895c2c4f4f917b42b19f8dcd616303040f2229c79d6f28659c81783ce92d
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sql-alert-on-anomaly-detection-results
    - DSAOADR
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Databricks SQL Alert on Anomaly Detection Results
description: Method for creating advanced alerts by querying the system.data_quality_monitoring.table_results system table with Databricks SQL, supporting custom filtering and notification templates.
tags:
  - databricks
  - sql
  - alerting
  - system-tables
timestamp: "2026-06-19T22:04:37.255Z"
---

# Databricks SQL Alert on Anomaly Detection Results

**Databricks SQL Alert on Anomaly Detection Results** is a notification mechanism that triggers when [Anomaly Detection](/concepts/anomaly-detection.md) identifies data quality issues, such as stale tables or unexpected drops in row count. By querying the anomaly detection output system table with Databricks SQL, users can configure alerts that support advanced filtering and custom notification templates. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Overview

Alerts notify selected workspace users when [Data Quality Monitoring](/concepts/data-quality-monitoring.md) detects unhealthy tables. While the [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md) provides a simpler mechanism for creating alerts within a catalog or schema, the Databricks SQL approach offers greater flexibility for filtering results and customizing email notifications. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Required Permissions

By default, only account admins can access the system table `system.data_quality_monitoring.table_results`. If other users need to configure alerts, ensure appropriate access is granted. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Creating an Alert with Databricks SQL

To create an alert on the anomaly detection output results table using Databricks SQL, follow these steps:

### Step 1: Create the Query

1. Click **Alerts** in the sidebar and click **Create alert**.
2. Enter the following text in the query editor:

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

^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Step 2: Run and Configure the Alert

3. Run the query.
4. Using the alert editor on the right side of the screen, configure the alert condition. For details, see creating alerts in Databricks SQL. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Step 3: Customize the Email Template (Optional)

To customize the email template, open the **Advanced** tab on the right side of the screen and check **Customize template** to open the template editor.

An example custom email template:

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

For more information about custom templates, see [advanced settings for alerts](/concepts/anomaly-detection-alerts.md). ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Query Details

The alert query performs the following:

- **Rounds event times** to the hour using `DATE_TRUNC` for time-bucketed analysis.
- **Concatenates** catalog, schema, and table names to create a fully qualified table identifier.
- **Filters** for results within the last 6 hours where tables are marked as `Unhealthy`.
- **Uses a parameterized threshold** (`:min_tables_affected`) to specify the minimum number of downstream queries affected before the alert triggers.

This approach helps debug the table that triggered the alert by focusing on the downstream impact of the quality issue. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Legacy Note

For legacy beta jobs, existing alert configurations should replace `system.data_quality_monitoring.table_results` with `<catalog>.<schema>._quality_monitoring_summary`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md)
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md)
- System Tables in Databricks
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
