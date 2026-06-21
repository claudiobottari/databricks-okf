---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa8c084c76c3ee76aa62665b2ebb3d5c9eab4a332ff74d928fa63d235e2632e3
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection-alerts-in-databricks-unity-catalog
    - ADAIDUC
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Anomaly Detection Alerts in Databricks Unity Catalog
description: Overview of alerting mechanisms that notify users when anomaly detection identifies data quality issues in Unity Catalog, supporting both UI-based and SQL-based configuration.
tags:
  - databricks
  - unity-catalog
  - alerting
  - data-quality
timestamp: "2026-06-19T22:05:22.533Z"
---

---

## Anomaly Detection Alerts in Databricks Unity Catalog

**Anomaly Detection Alerts** in Databricks Unity Catalog notify workspace users when [Anomaly Detection](/concepts/anomaly-detection.md) identifies a data quality issue, such as a stale table or an unexpected drop in row count. You can configure alerts to watch for these issues across a catalog or a specific schema. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

There are two primary ways to work with alerts:

*   **Data Quality Monitoring UI (Beta)**: Create and manage alerts directly from the Data Quality Monitoring UI without leaving the page. ^[alerts-for-anomaly-detection-databricks-on-aws.md]
*   **Databricks SQL**: Configure an alert by querying the anomaly detection output system table. This approach supports advanced filtering and custom notification templates. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Alerts in the Data Quality Monitoring UI

This feature is in **Beta** and is visible to all users by default. Workspace admins do not need to enable the feature from the **Previews** page. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

Alert rules notify selected workspace users by email when an unhealthy table is detected within a catalog or schema. Each alert rule is scoped to a catalog or a specific schema. When a monitored table within the rule’s scope becomes unhealthy, each recipient receives one email per important unhealthy table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Required Permissions

The privileges required to create or manage an alert rule depend on the rule's scope:

*   To create a **schema-level** alert, you must have the `MANAGE` privilege on the schema.
*   To create a **catalog-level** alert, you must have the `MANAGE` privilege on the catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

### View and Manage Data Quality Monitoring Alerts

To view your alert rules:

1.  Navigate to a schema in Catalog Explorer. Data quality monitoring must be enabled for this schema.
2.  Click the **Details** tab. Next to **Data Quality Monitoring**, click **View results**. This opens the Data Quality Monitoring UI.
3.  In the upper‑right corner of the page, click **Manage alerts**. A popover opens showing your existing alert rules, including the catalog, schema, and number of recipients for each rule.

From this popover, you can create a new alert rule, select an existing alert to edit its scope and recipients, or delete the alert. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Create an Alert

To create an alert:

1.  In the upper‑right corner of the Data Quality Monitoring UI, click **Manage alerts** to open the alerts popover.
2.  Click **Create alert**.
3.  Configure the alert rule:
    *   **Catalog**: Select the catalog to monitor.
    *   **Schema**: Select a specific schema, or select **All Schemas** to create a catalog‑level alert that covers every schema in the catalog.
    *   **Notify**: Search for and select one or more workspace users to notify by email.
4.  Click **Save**.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Create an Alert with Databricks SQL

By default, only account admins can access the system table `system.data_quality_monitoring.table_results`. If other users need to configure alerts, ensure they are granted appropriate access. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

To create an alert on the anomaly detection output results table using Databricks SQL:

1.  Click **Alerts** in the sidebar and click **Create alert**.
2.  Enter the following text in the query editor:

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

3.  Run the query.
4.  Using the alert editor on the right side of the screen, configure the alert condition.
5.  (Optional) To customize the email template, open the **Advanced** tab and check **Customize template** to open the template editor.

For legacy beta jobs, existing alert configuration should replace `system.data_quality_monitoring.table_results` with `<catalog>.<schema>._quality_monitoring_summary`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Custom Email Template Example

An example custom email template is shown below:

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

Now, you have an alert that triggers based on the downstream impact of the quality issue. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The detection engine that identifies data quality issues.
- [Data Quality Monitoring in Unity Catalog](/concepts/data-quality-monitoring-databricks.md) – The overall framework for monitoring data quality.
- Table Results System Table – The system table used for querying anomaly detection output.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI for navigating catalogs and schemas.
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) – The general alerting framework in Databricks SQL.

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
