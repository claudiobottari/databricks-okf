---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2452735bad55dc34e34af8e06e167edbf2aac82524d13676ed2f71f4a2da95a6
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-in-databricks
    - DPID
    - Data Profiling on Databricks
    - Data profiling on Databricks
    - Data Profiling on Databricks|data profile
    - data-profiling-in-databricks-unity-catalog
    - DPIDUC
    - data-profiling-in-unity-catalog
    - DPIUC
    - Data Billing in Unity Catalog
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Data Profiling in Databricks
description: A feature in Databricks Unity Catalog that analyzes table data to compute summary statistics, detect anomalies, and monitor data quality over time, configurable via the UI or API.
tags:
  - data-governance
  - data-quality
  - unity-catalog
  - databricks
timestamp: "2026-06-19T14:30:09.521Z"
---

---
title: "Data Profiling in Databricks"
summary: "Data Profiling in Databricks enables automated collection of statistical metrics about table data, supporting time-series and inference-based profiles with configurable schedules, custom metrics, and anomaly detection integration."
sources:
  - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:04:16.036Z"
updatedAt: "2026-06-18T08:04:16.036Z"
tags:
  - databricks
  - data-profiling
  - data-quality
  - unity-catalog
aliases:
  - data-profiling-in-databricks
  - DPD
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Data Profiling in Databricks

**Data Profiling in Databricks** is a feature of [Unity Catalog](/concepts/unity-catalog.md) that automatically collects statistical metrics from your tables, enabling you to monitor data quality over time. You can create profiles through the [Catalog Explorer](/concepts/catalog-explorer.md) UI or via the API. Profiling can be combined with [Anomaly Detection](/concepts/anomaly-detection.md) to alert on unexpected changes in your data.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Creating a Profile in the UI

To create a profile, open Catalog Explorer from the workspace left sidebar, navigate to the table you want to profile, and click the **Quality** tab. If anomaly detection is not yet enabled for the schema, click **Enable**; if it is already enabled, click **Configure**. In the **Data Quality Monitoring** dialog, under **Data profiling**, click **Configure** to open the profile configuration options.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Profile Types

From the **Profile type** drop-down menu, you select the type of profile to create. The supported types are:

- **Snapshot** (default) – profiles the entire current state of the table.
- **TimeSeries** – profiles data partitioned into time windows based on a timestamp column.
- **Inference** – profiles model inference data, requiring additional columns for predictions, labels, and model identifiers.

Additional parameters are required for TimeSeries and Inference profiles.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### TimeSeries Profile

For a TimeSeries profile you must specify:

- **Metric granularities** – how to partition data into time windows (e.g., daily, hourly).
- **Timestamp column** – a column of type `TIMESTAMP` or convertible via `to_timestamp`.

When first created, a TimeSeries profile analyzes only data from the 30 days prior to creation. After creation, all new data is processed incrementally if [change data feed (CDF)](/concepts/delta-change-data-feed-cdf.md) is enabled on the table; otherwise the entire table is re-scanned each refresh.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Inference Profile

For an Inference profile you must additionally specify:

- **Problem type** – classification or regression.
- **Prediction column** – the column containing model predictions.
- **Label column** (optional) – the ground truth for predictions.
- **Model ID column** – the column identifying which model produced the prediction.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Advanced Options

In the **Advanced options** section you can control scheduling, notifications, and metrics configuration.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Schedule

You can choose **Refresh on schedule** with a frequency and time, or **Refresh manually** to run the profile only when triggered. Manual refreshes can be initiated later from the **Quality** tab.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Notifications

Email notifications can be set for profile events. Up to five email addresses are supported per notification event type.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Metrics

You can customize:

- **Metrics tables schema name** – the Unity Catalog schema where metric tables are stored (defaults to the table’s own schema).
- **Assets directory** – the path to store profiling assets (defaults to `/Users/{username}/databricks_lakehouse_monitoring/{tableName}`). For shared profiles, use a path under `/Shared/`.
- **Unity Catalog baseline table name** – a table or view for comparison.
- **Metric slicing expressions** – SQL expressions that define subsets of the table to profile independently (e.g., `"col_2 > 10"` creates slices for each condition and its complement).
- **Custom metrics** – additional metrics defined via SQL with a name, type (Aggregate, Derived, or Drift), input columns, output Spark data type, and definition. Custom metrics appear in the metric tables like built-in metrics.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Editing and Managing Profiles

After a profile is created, you can edit its settings by clicking **Configure** on the **Quality** tab and then **Configure** in the Data Profiling section. To delete a profile, open the **Update profile** dialog, select **Delete** from the **Update** dropdown menu.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Refreshing and Viewing Results

To run a manual refresh, click **View refresh history** on the **Quality** tab, then click **Refresh metrics**. You must be in the same workspace from which profiling was enabled to see the refresh history. Metric tables are Unity Catalog tables that can be queried in notebooks, SQL query explorer, or viewed in Catalog Explorer. For details on the statistics stored, see Monitor metric tables.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Controlling Access

Metric tables and dashboards created by a profile are owned by the user who created them. Access to metric tables can be managed using [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md). Dashboards can be shared within a workspace using the **Share** button.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Best Practices

- For TimeSeries and Inference profiles, enable [change data feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on the table. When CDF is enabled, only newly appended data is processed on each refresh, improving efficiency and reducing costs as profiling scales across many tables.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- Monitors defined on materialized views do not support incremental processing.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- Monitor metric tables

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
