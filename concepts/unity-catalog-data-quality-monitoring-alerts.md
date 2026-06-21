---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35b01153733c4c95683c212a464cedd5328b4781805323cf713c382d94c9d2c1
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-data-quality-monitoring-alerts
    - UCDQMA
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Unity Catalog Data Quality Monitoring Alerts
description: Automated notifications that trigger when anomaly detection identifies unhealthy tables in Unity Catalog, supporting both UI-based and SQL-based configuration.
tags:
  - data-quality
  - unity-catalog
  - monitoring
  - alerting
timestamp: "2026-06-18T10:44:56.502Z"
---

# Unity Catalog Data Quality Monitoring Alerts

**Alerts** in Unity Catalog Data Quality Monitoring notify you when anomaly detection identifies a data quality issue, such as a stale table or an unexpected drop in row count. You can work with alerts using either the Data Quality Monitoring UI (Beta) or a Databricks SQL query against the anomaly detection output system table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

For an introduction to anomaly detection, see [Anomaly Detection](/concepts/anomaly-detection.md).

## Alerts in the Data Quality Monitoring UI (Beta)

The Data Quality Monitoring UI (Beta) lets you create and manage alert rules directly from the monitoring page without leaving the interface. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

Alert rules notify selected workspace users by email when an unhealthy table is detected within a catalog or schema. Each rule is scoped to a catalog or a specific schema. When a monitored table within the rule's scope becomes unhealthy, each recipient receives one email per important unhealthy table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Required permissions

- To create or manage a **schema-level** alert, you must have the `MANAGE` privilege on the schema.
- To create or manage a **catalog-level** alert, you must have the `MANAGE` privilege on the catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

### View and manage alerts

1. Navigate to a schema in [Catalog Explorer](/concepts/catalog-explorer.md). Data Quality Monitoring must be enabled for that schema.
2. Click the **Details** tab. Next to **Data Quality Monitoring**, click **View results** to open the Data Quality Monitoring UI.
3. In the upper-right corner of the page, click **Manage alerts**. A popover shows existing alert rules, including the catalog, schema, and number of recipients for each rule.

From this popover, you can create a new alert rule, edit an existing alert's scope and recipients, or delete an alert. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Create an alert

1. In the upper-right corner of the Data Quality Monitoring UI, click **Manage alerts** to open the alerts popover.
2. Click **Create alert**.
3. Configure the alert rule:
   - **Catalog**: Select the catalog to monitor.
   - **Schema**: Select a specific schema, or select **All Schemas** to create a catalog-level alert covering every schema in the catalog.
   - **Notify**: Search for and select one or more workspace users to notify by email.
4. Click **Save**.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Create an alert with Databricks SQL

> [!important]
> By default, only account admins can access the system table `system.data_quality_monitoring.table_results`. If other users need to configure alerts, grant appropriate access.

To create an alert using Databricks SQL:

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
     -- enter the minimum number of table violations before the alert is triggered
     AND impacted_queries > :min_tables_affected
     AND status = 'Unhealthy';
   ```

3. Run the query.
4. Using the alert editor on the right side of the screen, configure the alert condition. See Create an Alert for details.
5. (Optional) To customize the email template, open the **Advanced** tab and check **Customize template**.

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

Now the alert triggers based on the downstream impact of the quality issue, helping you identify the problematic table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The monitoring process that produces the data quality signals used by alerts
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI used to navigate to schemas and access the Data Quality Monitoring UI
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The broader framework for monitoring table health in Unity Catalog
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) – General alerting mechanism in Databricks SQL
- System Tables – The system data source (`system.data_quality_monitoring.table_results`) that powers SQL-based alerts

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
