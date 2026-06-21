---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65e6ecc991eab2e0d76f217e5b576b70a940d14cc82b0d124aa34b1924d141f9
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring-alert-rules
    - DQMAR
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Data Quality Monitoring Alert Rules
description: Rules that notify workspace users by email when anomaly detection identifies unhealthy tables within a catalog or schema scope.
tags:
  - alerting
  - data-quality
  - databricks
timestamp: "2026-06-18T14:23:50.079Z"
---

## Data Quality Monitoring Alert Rules

**Data Quality Monitoring Alert Rules** notify workspace users when [Anomaly Detection](/concepts/anomaly-detection.md) identifies a data quality issue, such as a stale table or an unexpected drop in row count. Alert rules can be created and managed either through the Data Quality Monitoring UI (Beta) or by configuring a Databricks SQL alert on the anomaly detection output system table.

### Methods for Creating Alerts

Alerts can be created using two approaches:

- **Data Quality Monitoring UI (Beta)** – Create and manage alert rules directly on the Data Quality Monitoring page, without leaving the workflow. ^[alerts-for-anomaly-detection-databricks-on-aws.md]
- **Databricks SQL** – Query the anomaly detection output system table to configure an alert. This method supports advanced filtering and custom notification templates. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Required Permissions

The privileges required to create or manage an alert rule depend on the rule's scope:

- To create a **schema-level alert**, you must have the `MANAGE` privilege on the schema.
- To create a **catalog-level alert**, you must have the `MANAGE` privilege on the catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Creating Alerts in the Data Quality Monitoring UI (Beta)

To create an alert using the UI:

1. Navigate to a schema in [Catalog Explorer](/concepts/catalog-explorer.md). Data quality monitoring must be enabled for that schema.
2. Click the **Details** tab. Next to **Data Quality Monitoring**, click **View results** to open the Data Quality Monitoring UI.
3. In the upper‑right corner, click **Manage alerts**. A popover lists existing alert rules.
4. Click **Create alert** and configure the rule:
   - **Catalog** – Select the catalog to monitor.
   - **Schema** – Select a specific schema, or choose **All Schemas** to create a catalog‑level alert covering every schema in the catalog.
   - **Notify** – Search for and select one or more workspace users to notify by email.
5. Click **Save**.

Each alert rule is scoped to a catalog or a specific schema. When a monitored table within the rule’s scope becomes unhealthy, each recipient receives one email per important unhealthy table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Creating an Alert with Databricks SQL

To create an alert using Databricks SQL:

1. Click **Alerts** in the sidebar and click **Create alert**.
2. Enter the following query in the query editor (replace any placeholder values as needed):

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
     -- Minimum number of table violations before the alert is triggered
     AND impacted_queries > :min_tables_affected
     AND status = 'Unhealthy';
   ```

   > **Note:** For legacy beta jobs, replace `system.data_quality_monitoring.table_results` with `<catalog>.<schema>._quality_monitoring_summary`.

3. Run the query.
4. Using the alert editor on the right side of the screen, configure the trigger condition (see [Create an alert](https://docs.databricks.com/aws/en/sql/user/alerts/create#create-alert)).
5. (Optional) To customize the email template, open the **Advanced** tab and check **Customize template**.

An example custom email template that lists affected tables and their metrics is provided in the source documentation. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

By default, only account admins can access the system table `system.data_quality_monitoring.table_results`. Grant appropriate access to other users who need to configure SQL alerts. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- Databricks SQL
- System Tables
- Email Notifications

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
