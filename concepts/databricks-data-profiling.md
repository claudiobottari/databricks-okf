---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5506a5222a44bff4253fd08690c841160a0eb1c8c4fa6f70bdd17caadb1a8056
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profiling
    - DDP
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Databricks Data Profiling
description: A feature in Databricks Unity Catalog that analyzes table statistics, distributions, and quality metrics to help users understand their data.
tags:
  - data-governance
  - unity-catalog
  - data-quality
timestamp: "2026-06-19T09:28:25.364Z"
---

# Databricks Data Profiling

**Databricks Data Profiling** is a feature in [Unity Catalog](/concepts/unity-catalog.md) that automatically computes statistical summaries and quality metrics for Delta tables. It enables data teams to monitor the structure, content, and distribution of their data over time without writing custom analysis code. Profiles can be created and managed using the Databricks UI or the API. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Profile Types

When creating a profile, you select one of two types: `TimeSeries` or `Inference`. Each type serves a different monitoring purpose.

### TimeSeries Profile

A `TimeSeries` profile compares data distributions across time windows. It requires a **timestamp column** and one or more **metric granularities** that determine how to partition data into time windows. Available granularities range from 5 minutes to 1 year. The timestamp column must have a `TIMESTAMP` data type or be convertible using the `to_timestamp` PySpark function. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

When you first create a TimeSeries profile, it analyzes only data from the 30 days prior to its creation. After the profile is created, all new data is processed on subsequent refreshes. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

Best practice: enable [change data feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on the table so that only newly appended data is processed on each refresh, reducing cost and improving efficiency. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Inference Profile

An `Inference` profile is designed for monitoring machine learning model inference data. In addition to the timestamp column and granularities, you must specify:

- **Problem type**: `classification` or `regression`
- **Prediction column**: the column containing the model’s predicted values
- **Model ID column**: the column identifying which model was used
- **Label column** (optional): the column containing ground truth for model predictions

When you first create an Inference profile, it also analyzes only data from the 30 days prior to creation. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

> **Note**: Profiles defined on materialized views do not support incremental processing for either profile type. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Advanced Options

In the advanced options, you can configure a schedule, email notifications, custom metrics, slicing expressions, and the storage location for metric tables and assets.

### Schedule

To run a profile automatically, set a schedule by selecting **Refresh on schedule** and specifying the frequency and time. If you prefer manual refreshes, select **Refresh manually**; you can later trigger a refresh from the **Quality** tab. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Notifications

Email notifications can be set up for profile events (e.g., failure or timeout). You can enter up to 5 email addresses per notification event type. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Metrics Storage

By default, the metric tables created by the profile are stored in the same Unity Catalog schema as the profiled table. You can change this by specifying a different schema in the format `{catalog}.{schema}`. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

The **assets directory** stores dashboards and other assets. The default is `/Users/{user_name}/databricks_lakehouse_monitoring/{table_name}`. You can specify any workspace path; for shared profiles, use a path under `/Shared/`. This field cannot be left blank. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

Additional optional settings include:

- **Baseline table name**: a table or view containing baseline data for comparison.
- **Slicing expressions**: define subsets of the table to profile independently. For example, the expression `col_2 > 10` generates two slices: one for `col_2 > 10` and one for `col_2 <= 10`. An expression like `col_1` generates one slice per unique value in that column.
- **Custom metrics**: define additional metrics (Aggregate, Derived, or Drift) by providing a name, input columns, output Spark data type, and SQL definition. Custom metrics appear in metric tables alongside built-in metrics. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Creating and Editing a Profile in the UI

To create a profile:

1. In the workspace sidebar, click the Data icon to open [Catalog Explorer](/concepts/catalog-explorer.md).
2. Navigate to the target table and click the **Quality** tab.
3. If anomaly detection is not enabled for the schema, click **Enable**. If already enabled, click **Configure**.
4. In the **Data Quality Monitoring** dialog, under **Data profiling**, click **Configure**.
5. Select the profile type (`TimeSeries` or `Inference`) and fill in the required parameters.
6. Expand **Advanced options** to set schedule, notifications, metrics schema, assets directory, baseline table, slicing expressions, and custom metrics.
7. Click **Create**. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

To edit an existing profile, click **Configure** on the **Quality** tab, then click **Configure** again under the **Data profiling** section. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Refreshing and Viewing Results

To manually refresh a profile, click **View refresh history**, then click **Refresh metrics**. The refresh history dialog shows all previous runs. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

Metric tables are Unity Catalog tables. You can query them in notebooks or the SQL query explorer, and view them in Catalog Explorer. For details on available statistics, see Monitor Metric Tables. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

Note: To see the refresh history, you must use the Databricks workspace from which the profile was created. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Access Control

The metric tables and dashboard created by a profile are owned by the user who created the profile. Use Unity Catalog privileges to control access to metric tables. To share the dashboard within the workspace, click the **Share** button in the top-right corner of the dashboard. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Deleting a Profile

To delete a profile from the UI, open the **Update profile** dialog (via **Configure** on the **Quality** tab), select **Delete** from the **Update** dropdown menu, and confirm. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- Monitor Metric Tables
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md)
- [Anomaly Detection](/concepts/anomaly-detection.md)

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
