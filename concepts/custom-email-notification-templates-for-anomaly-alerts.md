---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0958eccef61c48298a56259ba2f32d68029c41d9ba2152effdfe9702fc09e8f
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-email-notification-templates-for-anomaly-alerts
    - CENTFAA
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Custom Email Notification Templates for Anomaly Alerts
description: Feature allowing customization of email notification templates for Databricks SQL alerts, using Handlebars-style template syntax with query result row iteration.
tags:
  - databricks
  - email
  - notifications
  - templates
timestamp: "2026-06-19T22:05:27.389Z"
---

# Custom Email Notification Templates for Anomaly Alerts

**Custom Email Notification Templates for Anomaly Alerts** allow you to personalize the format and content of alert emails sent when [Anomaly Detection](/concepts/anomaly-detection.md) identifies data quality issues in monitored tables. These templates are configured through Databricks SQL and use handlebars-like syntax to insert dynamic values from query results into the email body.

## Overview

When anomaly detection identifies an unhealthy table, alerts notify selected users by email. By default, these notifications use a standard template. However, you can customize the template to include specific fields, formatting, and contextual information relevant to your team. Custom templates are particularly useful for providing stakeholders with actionable details directly in the notification, such as expected values versus actual values, and the downstream impact of data quality issues. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Enabling Custom Email Templates

Custom email templates are available when creating alerts using Databricks SQL rather than the Data Quality Monitoring UI (which is in Beta). To enable custom templates:

1. Navigate to the **Alerts** section in the Databricks sidebar and click **Create alert**.
2. Enter the query that generates the alert data (see the query example below).
3. Run the query to verify it returns results.
4. In the alert editor on the right side of the screen, open the **Advanced** tab.
5. Check **Customize template** to open the template editor.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Required Permissions

By default, only account admins can access the `system.data_quality_monitoring.table_results` system table needed for alert configuration. If other users need to configure alerts, ensure they have appropriate access granted. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Template Syntax

Custom email templates use the following syntax for inserting dynamic values:

- **`{{#QUERY_RESULT_ROWS}}` / `{{/QUERY_RESULT_ROWS}}`** — Iterates over each row returned by the alert query.
- **`{{column_name}}`** — Inserts the value from the specified column in the current row.

These placeholders map to the columns defined in your alert query's SELECT statement. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Example Template

Below is a complete example of a custom email notification template that displays a table of failing quality checks:

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

This template creates an HTML email that lists each affected table with its expected and actual staleness (commit freshness), expected and actual row counts (completeness), and the number of impacted queries on downstream tables. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Alert Query for Template Data

To populate the template, your alert query should generate the data the template references. The recommended query structure:

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

For legacy beta jobs, replace `system.data_quality_monitoring.table_results` with `<catalog>.<schema>._quality_monitoring_summary`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The underlying detection mechanism that triggers alerts
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The framework for monitoring table health
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) — The alert system used for custom templates
- Handlebar templates — The template engine powering custom email notifications
- Alert Conditions — Configuration for when alerts trigger
- downstream_impact Struct|Downstream Impact — The metric measuring query impact on affected tables

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
