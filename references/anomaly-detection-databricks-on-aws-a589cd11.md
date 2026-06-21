---
title: Anomaly detection | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/
ingestedAt: "2026-06-18T08:04:08.272Z"
---

This page describes what anomaly detection is, what it monitors, and how to use it.

important

Anomaly detection uses [default storage](https://docs.databricks.com/aws/en/storage/default-storage) to store scan results in the `system.data_quality_monitoring.table_results` system table. You are not billed for this storage.

## What is anomaly detection?[​](#what-is-anomaly-detection "Direct link to What is anomaly detection?")

Anomaly detection enables you to monitor data quality across all tables in a schema. By analyzing historical patterns, Databricks automatically evaluates the completeness and freshness of each table. Results are available in Catalog Explorer.

## Requirements[​](#requirements "Direct link to Requirements")

*   Unity Catalog enabled workspace.
*   [Serverless compute](https://docs.databricks.com/aws/en/compute/serverless/) must be available in your workspace (enabled by default in workspaces with Unity Catalog).
*   To enable anomaly detection on a schema, you must have MANAGE SCHEMA or MANAGE CATALOG privileges on the catalog schema.
*   To view the health indicator status of tables, you need SELECT or BROWSE privileges.

## How does anomaly detection work?[​](#how-does-anomaly-detection-work "Direct link to How does anomaly detection work?")

Databricks creates a background job that monitors tables for _freshness_ and _completeness_.

**Freshness** refers to how recently a table has been updated. Data quality monitoring analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as stale.

**Completeness** refers to the number of rows expected to be written to the table in the last 24 hours. Data quality monitoring analyzes the historical row count, and based on this data, predicts a range of expected number of rows. If the number of rows committed over the last 24 hours is less than the lower bound of this range, a table is marked as incomplete.

Databricks uses intelligent scanning to automate table scan frequencies. Intelligent scanning prioritizes high-impact tables as determined by popularity and downstream usage, and reduces frequency for less critical tables. To manually exclude tables, use the Create a Monitor or Update a Monitor API and specify the excluded tables in the `excluded_table_full_names` parameter. For more information, see the [API documentation](https://docs.databricks.com/api/workspace/dataquality/createmonitor#anomaly_detection_config-excluded_table_full_names).

Anomaly detection **does not** modify any tables it monitors, nor does it add overhead to any jobs that populate these tables.

note

Event freshness, which is based on event time columns and ingestion latency, was available only to users of the data quality monitoring beta version. In the current version, event freshness is not supported.

### Percent null for completeness[​](#percent-null-for-completeness "Direct link to Percent null for completeness")

**Percent null** adds additional quality details to _completeness_. Percent null is the percentage of rows written to the table in the last 24 hours expected to have null values for a given column. Data quality monitoring analyzes the historical trend for each column, and based on this data, predicts a range. If the percent null for a column over the last 24 hours is higher than the upper bound of this range, a table is marked as incomplete.

## Enable anomaly detection on a schema[​](#enable-anomaly-detection-on-a-schema "Direct link to enable-anomaly-detection-on-a-schema")

To enable anomaly detection on a schema, navigate to the schema in Unity Catalog.

1.  On the schema page, click the **Details** tab.
    
    ![Details tab for the schema page in Catalog Explorer.](https://docs.databricks.com/aws/en/assets/images/schema-details-tab-337de9fb7f793ffe2567597271b72551.png)
    
2.  Click **Enable**. In the **Data Quality Monitoring** dialog, ensure that **Anomaly detection** is toggled on, then click **Save**.
    
3.  A scan is initiated. Databricks automatically scans each table at the same frequency it’s updated, providing up-to-date insights without requiring manual configuration for each table. For schemas enabled prior to September 24, 2025, Databricks ran the monitor on historical data ("backtesting") for the first scan, to check the quality of your tables as if data quality monitoring had been enabled on your schema two weeks ago.
    
4.  After the scan is complete, you can view anomaly detection results for your tables in the following ways:
    

*   Health indicators appear in Catalog Explorer for each table within a schema. See [Health indicators](#health-indicators).
*   On the **Details** tab of a schema with **Data Quality Monitoring** enabled, click **View results**, and then view the results in **Data Quality Monitoring**. See [View data quality monitoring results in the UI](#incidents).
*   Detected quality issues are logged in the output system table. See [Review anomaly detection logged results](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/results).

### Disable anomaly detection[​](#disable-anomaly-detection "Direct link to Disable anomaly detection")

To disable anomaly detection:

1.  Click the pencil icon.
    
    ![Pencil icon in Advanced field of Details tab.](https://docs.databricks.com/aws/en/assets/images/pencil-icon-1653e5c65900cda8121473a353380e01.png)
    
2.  In the **Data Quality Monitoring** dialog, click the toggle.
    
    important
    
    When you disable anomaly detection, the anomaly detection job and all anomaly detection tables and information are deleted. This action cannot be undone.
    
    ![Toggle switch in Data Quality Monitoring dialog.](https://docs.databricks.com/aws/en/assets/images/data-quality-disable-toggle-c9cdb9a0f849a387a2b416705b2889db.png)
    
3.  Click **Save**.
    

## Health indicators[​](#health-indicators "Direct link to health-indicators")

After you enable anomaly detection on a schema, health indicators appear on the schema and table overview pages in Catalog Explorer. The health indicator shows a summary of table health for data consumers and business users without requiring them to navigate to the [Data Quality Monitoring UI](#incidents). Users need the SELECT or BROWSE permission to view the health indicator status.

![Health indicators for tables in a schema.](https://docs.databricks.com/aws/en/assets/images/anomaly-detection-health-indicators-d8e978de4283df5a4c8fc0c5815eaa92.png)

The following table describes each health indicator status:

note

Smart scanning might delay the population of health indicators for some tables by up to two weeks if the table was skipped during the initial scan. The health indicator is populated on the next scheduled rescan.

## View data quality monitoring results in the UI[​](#-view-data-quality-monitoring-results-in-the-ui "Direct link to -view-data-quality-monitoring-results-in-the-ui")

important

On October 7, 2025, Databricks released a new version of the Data Quality Monitoring UI. Schemas enabled for data quality monitoring on or after that date automatically use this new UI. This section describes this latest version of the UI.

For information about the legacy UI, see [Data quality dashboard (legacy)](#dashboard).

Databricks recommends that you enable the new version for all of your existing schemas.

To enable the new version, click the **Data Quality Monitoring** toggle to turn off the feature, and then click again to turn it back on.

After you enable data quality monitoring on a schema, you can open the results page by clicking **View results**. You can also access results from all schemas that have monitoring enabled in Catalog Explorer.

The results UI contains catalog and schema dropdowns. When you select a catalog, the schema dropdown is populated with schemas in that catalog that have data quality monitoring enabled.

*   If you have **MANAGE** or **SELECT** privileges on the catalog, you can view incidents at the catalog level. To view all incidents in a catalog, select **All Schemas** from the **Schema** drop-down menu.
    
    ![Selecting All Schemas from the Schema drop-down menu.](https://docs.databricks.com/aws/en/assets/images/all-schemas-ad4a698996ef72e687259058ec6db295.png)
    
*   To view incidents for a specific schema, you must also have **MANAGE** or **SELECT** privileges on that schema. Selecting a schema then shows incidents for just that schema.
    

The results page shows a summary section at the top, which displays overall data quality for the selected scope, including the percentage of healthy tables and the percentage of schemas/tables currently monitored. Below this section is a table listing incidents across all monitored tables in the selected scope. Use the buttons to display **Unhealthy**, **Healthy**, or **Error** tables.

![Incidents UI showing summary, important incidents, and all incidents tabs.](https://docs.databricks.com/aws/en/assets/images/quality-incidents-170a2cc87458af297b51e9ab633db3f6.png)

The following table describes the columns, which are slightly different depending on if you select **Unhealthy**, **Healthy**, or **Error**.

## Manage unhealthy table incidents[​](#-manage-unhealthy-table-incidents "Direct link to -manage-unhealthy-table-incidents")

From the **Unhealthy** tab, click **Review** in the **Results** column to open the incident details for the table. From this view, two actions are available:

*   **Assign to me**: Claims ownership of the incident to indicate that it is actively being investigated. The table remains in an **Unhealthy** status. The assignment persists for 7 days.
*   **Not an issue**: Marks the incident as a false positive and dismisses it. The table's status changes from **Unhealthy** to **Healthy**, and the **Resolution** column in the [Recently Resolved Incidents](#recently-resolved) section displays **Not an issue**. The dismissal persists for 7 days.

![Incident details showing the Assign to me and Not an issue actions.](https://docs.databricks.com/aws/en/assets/images/dqm-unhealthy-table-assign-to-me-244e90c77c90a2f888638ff43e307669.png)

## View recently resolved incidents[​](#-view-recently-resolved-incidents "Direct link to -view-recently-resolved-incidents")

The **Recently Resolved Incidents** section of the data quality monitoring dashboard shows tables that were previously unhealthy but have since recovered on their own. A table appears in this section when its status changes from **Unhealthy** to **Healthy** automatically, without manual intervention.

![Recently Resolved Incidents section showing tables that returned to a Healthy status within the last seven days.](https://docs.databricks.com/aws/en/assets/images/anomaly-detection-dqm-recently-resolved-incidents-70fdbcf8d024c2cb43cfaadb3d8d6eff.png)

Monitoring recently auto-resolved incidents helps you identify self-healing data quality issues. Typically, these issues are transient problems such as upstream delays or staleness windows that resolve after fresh data arrives. Reviewing auto-resolved incidents helps you distinguish flaky issues from persistent problems and ensures that your tables remain healthy over time.

The following table describes the columns in this section:

This section provides a template that you can import to your workspace. This template creates a dashboard that lets you view all quality results across the metastore.

To use this template, you must have access to the `system.data_quality_monitoring.table_results` table. By default, only account admins have access to this table. They can grant access to others as needed.

### How to use the template[​](#how-to-use-the-template "Direct link to How to use the template")

Follow these steps:

1.  Download the template file: [metastore-quality-dashboard.lvdash.json](https://docs.databricks.com/aws/en/assets/files/metastore-quality-dashboard.lvdash-f0c55012cc8f965edeeb5034e570c80a.json).
2.  In the workspace sidebar, click ![Dashboards Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAGKADAAQAAAABAAAAGAAAAADiNXWtAAACX0lEQVRIDbVWTWsTURQ9M53MJJm0UvGDqgm1RaRV46JqRSiiBRddiAhdFeyu9R+omxbEjbhQF0K7cOlGxF/gLoIIFaR+4EaRFnUjCjZfM6EzfefJDPPSSeNIchfJ+7jvnHfPu+/d0QbPTvqe56FWd+D7PjphmqYhk7ag6zoMgvfmbExNnoedyXQCH5VaDaXXK9goV4C9xXP+9ZuLYvOdNWIS2xCwIoKc3LnjuPi8tg5dhBg1T/gw5MKBATm89v2HlDTOb7iQh2WZEpPYBldQJtoXAT5xdQaWacp+8OO4LsZOjOLp0gM5NH9jAW/efYz1e/n8CUaODIeYkiAA4uEQvJmA86lUKnCT7VZ+xIiaHu10o61E8C8E1LXuOKiKTNnc/CttsM5xnVCaYCwRgef56BMpfX/xFsqVqshzVQ7OD+YPBtjyPxGBzArDQHHkqAKyUycRAQ+QGfWi9Ao/f/1GT496hJTs8qWL6N/VF3ImIqAk1P7e0mOsrL5H2rRCIDbq4gxOnzzemoD34U+5HLuwUq3Jt4pR2NmMOIvctnQ23ZR8f6KsSgQD+/fh0Z2F2ND37O5HVrxVJEpiCgG1m52+suN6Zk8SUwio79sPn2LTL2dnMSqegOab2o5MIfi6/g1T1+aEturh8QKNFY/h2fLDbeSJCFggqHPzW8R0TFtW4t2TXE3kdtv5j3lFIt5UXqRm41ij0QiH2W7lR4yoSQJKQxsSxaIk3vO4QsKC02vb0m/57u2WBYcYtADTYFZsiMtFYyViprSzw/lD7VwkJrG1wpkLPov+xPiprhR9rdufLVtC7EXy6T31AwAAAABJRU5ErkJggg==) **Dashboards**.
3.  In the upper-right corner, select **Import dashboard from file** from the **Create dashboard** drop-down menu.
4.  In the dialog, click **Choose file**, navigate to the template file, and click **Import dashboard**.

The file is imported and the dashboard appears.

![Example of metastore-level data quality dashboard.](https://docs.databricks.com/aws/en/assets/images/metastore-data-quality-dashboard-9d194085ce5d7c9ccba7dff860d7988a.png)

## Table quality details[​](#-table-quality-details "Direct link to -table-quality-details")

The **Table Quality Details** UI allows you to dive deeper into trends and understand why anomalies were detected for specific tables in your schema. You can access this view in several ways:

*   From the **Results UI** (new experience), by clicking on the review link in the incidents list.
*   From the **Monitoring Dashboard** (legacy Lakeview dashboard), by clicking on the table name in the Quality Overview tab.
*   From the **UC Table viewer**, by visiting the **Quality** tab on the table page.

All options take you to the same **Table Quality Details** view for the selected table.

Given a table, the UI shows summaries from each quality check for the table, with graphs of predicted and observed values at each evaluation timestamp. The graphs plot results from the last 1 week of data.

![Table Quality Details UI for anomaly detection.](https://docs.databricks.com/aws/en/assets/images/anomaly-detection-table-quality-details-327338117321c8763e194f6c6a984630.png)

If the table failed the quality checks, the UI also displays any upstream jobs that were identified as the root cause.

![Table Quality Details UI root cause table.](https://docs.databricks.com/aws/en/assets/images/anomaly-detection-table-quality-root-cause-2cc4f226b4458cf9d2d78a08db76828b.png)

## Set up alerts[​](#set-up-alerts "Direct link to Set up alerts")

To configure a Databricks SQL alert on the output results table, see [Alerts for anomaly detection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/alerts).

## Limitations[​](#limitations "Direct link to Limitations")

*   Anomaly detection does not support views or foreign tables.
*   The determination of completeness does not take into account metrics such as the fraction of nulls, zero values, or NaN.

## Legacy anomaly detection[​](#legacy-anomaly-detection "Direct link to Legacy anomaly detection")

The following sections cover two legacy features: the data quality dashboard and anomaly detection job configuration. The current version of anomaly detection does not include these features. The dashboard has been replaced by the [data quality monitoring results UI](#incidents).

**Data quality dashboard (legacy)**

### Data quality dashboard (legacy)[​](#-data-quality-dashboard-legacy "Direct link to -data-quality-dashboard-legacy")

note

The data quality monitoring dashboard was available only to legacy users. In the current version, use [View data quality monitoring results in the UI](#incidents).

The first data quality monitor run creates a dashboard to summarize results and trends derived from the logging table. The dashboard is automatically populated with insights for the scanned schema. A single dashboard is created per workspace at this path: `/Shared/Databricks Quality Monitoring/Data Quality Monitoring`.

#### Quality overview[​](#quality-overview "Direct link to Quality overview")

The **Quality Overview** tab shows a summary of the latest quality status of tables in your schema based on the most recent evaluation.

To get started, you must enter the logging table for the schema you want to analyze to populate the dashboard.

The top section of the dashboard shows an overview of the results of the scan.

![Data quality monitor schema summary in Quality Overview tab of the Dashboard.](https://docs.databricks.com/aws/en/assets/images/anomaly-detection-dashboard-quality-overview-schema-summary-dc82695a747dac5dfdd2b1894d0e707b.png)

Below the summary is a table listing quality incidents by impact. Any identified root causes are displayed in the `root_cause_analysis` column.

![Quality incidents by impact in Quality Overview tab of the Dashboard.](https://docs.databricks.com/aws/en/assets/images/anomaly-detection-dashboard-quality-overview-results-table-b4a4359e733c5327fcebcd41897822fc.png)

Below the quality incident table is a table of identified static tables that have not been updated in a long time.

**Set parameters for freshness and completeness evaluation (legacy)**

### Set parameters for freshness and completeness evaluation (legacy)[​](#-set-parameters-for-freshness-and-completeness-evaluation-legacy "Direct link to -set-parameters-for-freshness-and-completeness-evaluation-legacy")

note

Starting from July 21, 2025, configuration of the job parameters is not supported for new customers. If you need to configure the job settings, contact Databricks.

To edit the parameters that control the job, such as how often the job runs or the name of the logged results table, you must edit the job parameters on the **Tasks** tab of the job page.

![Jobs page showing anomaly detection job.](https://docs.databricks.com/aws/en/assets/images/anomaly-detection-job-tasks-8ae4dfb9cc5296fb76742b56a9cd7eb2.png)

The following sections describe specific settings. For information about how to set task parameters, see [Configure task parameters](https://docs.databricks.com/aws/en/jobs/task-parameters).

#### Schedule and notifications (legacy)[​](#schedule-and-notifications-legacy "Direct link to Schedule and notifications (legacy)")

To customize the schedule for the job, or to set up notifications, use the **Schedules & Triggers** settings on the jobs page. See [Automate jobs with schedules and triggers](https://docs.databricks.com/aws/en/jobs/triggers).

#### Name of logging table (legacy)[​](#name-of-logging-table-legacy "Direct link to Name of logging table (legacy)")

To change the name of the logging table, or save the table in a different schema, edit the job task parameter `logging_table_name` and specify the desired name. To save the logging table in a different schema, specify the full 3-level name.

#### Customize `freshness` and `completeness` evaluations (legacy)[​](#customize-freshness-and-completeness-evaluations-legacy "Direct link to customize-freshness-and-completeness-evaluations-legacy")

All of the parameters in this section are optional. By default, anomaly detection determines thresholds based on an analysis of the table's history.

These parameters are fields inside the task parameter `metric_configs`. The format of `metric_configs` is a JSON string with the following default values:

JSON

    [  {    "disable_check": false,    "tables_to_skip": null,    "tables_to_scan": null,    "table_threshold_overrides": null,    "table_latency_threshold_overrides": null,    "static_table_threshold_override": null,    "event_timestamp_col_names": null,    "metric_type": "FreshnessConfig"  },  {    "disable_check": true,    "tables_to_skip": null,    "tables_to_scan": null,    "table_threshold_overrides": null,    "metric_type": "CompletenessConfig"  }]

The following parameters can be used for both `freshness` and `completeness` evaluations.

The following parameters apply only to the `freshness` evaluation:

The following parameter applies only to the `completeness` evaluation:
