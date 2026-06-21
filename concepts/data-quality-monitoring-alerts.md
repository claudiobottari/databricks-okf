---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6560c6e1dff9a938af5ef6d850c80a4ee616cd492dcd0d1763c6dc7259d87fc1
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring-alerts
    - DQMA
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Data Quality Monitoring Alerts
description: Notification system that alerts workspace users when anomaly detection identifies data quality issues like stale tables or unexpected drops in row count.
tags:
  - databricks
  - data-quality
  - monitoring
  - alerts
timestamp: "2026-06-19T08:57:52.072Z"
---

# Data Quality Monitoring Alerts

**Data Quality Monitoring Alerts** notify workspace users when [Anomaly Detection](/concepts/anomaly-detection.md) identifies a data quality issue, such as a stale table or an unexpected drop in row count. Two approaches are available: the Data Quality Monitoring UI (Beta) and Databricks SQL. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Alerts in the Data Quality Monitoring UI (Beta)

The Data Quality Monitoring UI provides a visual interface for creating and managing alert rules. An alert rule is scoped to a catalog or a specific schema. When a monitored table within the rule's scope becomes unhealthy, each recipient receives one email per important unhealthy table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Required Permissions

- **Schema-level alert**: the user must have the `MANAGE` privilege on the schema. ^[alerts-for-anomaly-detection-databricks-on-aws.md]
- **Catalog-level alert**: the user must have the `MANAGE` privilege on the catalog. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### View and Manage Alerts

1. Navigate to a schema in Catalog Explorer (data quality monitoring must be enabled for that schema).
2. Click the **Details** tab, then next to **Data Quality Monitoring**, click **View results** to open the Data Quality Monitoring UI.
3. In the upper-right corner, click **Manage alerts**. A popover lists existing alert rules with their catalog, schema, and number of recipients. From this popover you can create, edit, or delete alert rules. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Create an Alert

1. In the Data Quality Monitoring UI, click **Manage alerts** → **Create alert**.
2. Configure:
   - **Catalog**: select the catalog to monitor.
   - **Schema**: select a specific schema or choose **All Schemas** for a catalog-level alert.
   - **Notify**: search for and select one or more workspace users to notify by email.
3. Click **Save**. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Create an Alert with Databricks SQL

For advanced filtering and custom notification templates, use Databricks SQL to set up an alert that queries the anomaly detection output system table `system.data_quality_monitoring.table_results`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

> By default, only account admins can access this system table. Grant appropriate access if other users need to configure alerts. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Steps

1. Click **Alerts** in the sidebar → **Create alert**.
2. Enter a query that selects from the system table. The example below retrieves unhealthy tables evaluated in the last six hours, filtering by a minimum number of affected queries:
   ```sql
   WITH rounded_data AS (SELECT
     DATE_TRUNC('HOUR', event_time) AS evaluated_at,
     CONCAT(catalog_name, '.', schema_name, '.', table_name) AS full_table_name,
     status,
     MAX(downstream_impact.num_queries_on_affected_tables) AS impacted_queries,
     MAX(freshness.commit_freshness.predicted_value) AS commit_expected,
     MAX(freshness.commit_freshness.last_value) AS commit_actual,
     MAX(completeness.daily_row_count.min_predicted_value) AS completeness_expected,
     MAX(completeness.daily_row_count.last_value) AS completeness_actual
   FROM system.data_quality_monitoring.table_results
   GROUP BY ALL)
   SELECT
     evaluated_at, full_table_name, status,
     commit_expected, commit_actual,
     completeness_expected, completeness_actual,
     impacted_queries
   FROM rounded_data
   WHERE
     evaluated_at >= current_timestamp() - INTERVAL 6 HOURS
     AND impacted_queries > :min_tables_affected
     AND status = 'Unhealthy';
   ```
   ^[alerts-for-anomaly-detection-databricks-on-aws.md]
3. Run the query.
4. In the alert editor on the right, configure the trigger condition. See Create an alert (Databricks SQL) for details. ^[alerts-for-anomaly-detection-databricks-on-aws.md]
5. (Optional) To customize the email template, open the **Advanced** tab and check **Customize template**. Example custom template:
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
   ^[alerts-for-anomaly-detection-databricks-on-aws.md]

The alert triggers based on the downstream impact of the quality issue, helping you debug the table that triggered the alert. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- System Tables
- Create an alert (Databricks SQL)
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
