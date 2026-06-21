---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee6f823d30fb71dcfe041e99be38271824c093eab64b95f17b49cad87de59f74
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-ui-workflow
    - DPUW
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Data Profiling UI Workflow
description: The step-by-step process in Databricks Catalog Explorer to enable, configure, schedule, refresh, view, and delete data profiles through the Quality tab interface.
tags:
  - user-interface
  - workflow
  - catalog-explorer
timestamp: "2026-06-19T17:56:20.653Z"
---

# Data Profiling UI Workflow

The **Data Profiling UI Workflow** refers to the process of creating, configuring, and managing data profiles for Unity Catalog tables using the Databricks workspace interface. This workflow allows users to set up automated statistical analysis of their data without writing code, define slicing expressions and custom metrics, and schedule regular refreshes.

## Prerequisites

To access the data profiling UI, anomaly detection must be enabled for the schema containing the target table. If anomaly detection is not yet enabled, the **Quality** tab on the table overview page will show an **Enable** button. After enabling anomaly detection, the **Configure** button becomes available for data profiling. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Accessing the Profiling Interface

1. In the workspace left sidebar, click the **Data** icon to open [Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/).
2. Navigate to the table you want to profile.
3. Click the **Quality** tab.
4. If anomaly detection is not enabled, click **Enable**; if already enabled, click **Configure**.
5. In the **Data Quality Monitoring** dialog, in the **Data profiling** field, click **Configure**.

The dialog that opens presents the **Profile type** drop-down and additional configuration sections. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Profile Types

From the **Profile type** drop-down, select one of three types: `Snapshot`, `TimeSeries`, or `Inference`. The selection determines which additional parameters are required.

| Profile Type | Description |
|--------------|-------------|
| `Snapshot`   | Profiles the table as a single point-in-time snapshot. No additional parameters beyond the basic settings are needed. |
| `TimeSeries` | Profiles data over rolling time windows. Requires a **Timestamp column** and one or more **Metric granularities** (e.g., weekly, daily). |
| `Inference`  | Profiles model inference logs over time. Requires a **Timestamp column**, **Metric granularities**, **Problem type** (classification or regression), **Prediction column**, optionally a **Label column**, and a **Model ID column**. |

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### 30-Day Lookback Window

When a `TimeSeries` or `Inference` profile is first created, it analyzes only data from the 30 days prior to its creation. After the profile is created, all new data is processed on subsequent refreshes. This means the first analysis window may be a partial window if the 30‑day cutoff falls in the middle of a metric granularity period. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md] ^[data-profiling-metric-tables-databricks-on-aws.md]

### Best Practice: Enable Change Data Feed

For `TimeSeries` and `Inference` profiles, enabling **change data feed (CDF)** on the profiled table is recommended. When CDF is enabled, only newly appended data is processed on each refresh, rather than re‑processing the entire table. This improves efficiency and reduces costs as profiling scales across many tables. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Advanced Options

The **Advanced options** section allows customization of the profile’s behavior.

### Schedule

Choose **Refresh on schedule** to run the profile automatically at a specified frequency and time. Alternatively, choose **Refresh manually** to trigger refreshes on demand from the **Quality** tab. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Notifications

To receive email alerts for profile events, enter up to five email addresses and select the notification types to enable (e.g., on failure, on completion). ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Metrics Configuration

The following default settings can be changed:

- **Metrics tables schema name**: The Unity Catalog schema where the metric tables ([Profile Metrics Table](/concepts/profile-metrics-table.md), [Drift Metrics Table](/concepts/drift-metrics-table.md)) are stored. Defaults to the same schema as the profiled table.
- **Assets directory**: The absolute path to an existing directory where profiling assets are stored. Default is `/Users/{user_name}/databricks_lakehouse_monitoring/{table_name}`. For shared profiles, use a path under `/Shared/`. This field cannot be blank.
- **Unity Catalog baseline table name**: An optional table or view containing baseline data for comparison.
- **Metric slicing expressions**: Define subsets of the table to profile independently. For example, the expression `"col_2 > 10"` generates two slices: one for rows satisfying the condition and one for its complement. Each slicing expression is evaluated independently.
- **Custom metrics**: Add custom SQL-defined metrics with types `Aggregate`, `Derived`, or `Drift`. Each custom metric appears in the metric tables alongside built‑in metrics.

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Timestamp Column Requirements

When using `TimeSeries` or `Inference` profiles, the timestamp column must have a data type of `TIMESTAMP` or a type that can be converted using the PySpark `to_timestamp` function. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Editing and Deleting a Profile

To modify an existing profile, click **Configure** on the **Quality** tab. This re‑opens the **Update profile** dialog. From the **Update** drop‑down, you can either adjust settings or select **Delete** to remove the profile. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Refreshing and Viewing Results

To run the profile manually, click **View refresh history** on the **Quality** tab. A dialog shows all previous profile runs. Click **Refresh metrics** to trigger a new update. After a refresh, the results are stored in Unity Catalog metric tables. These tables can be queried using notebooks, the SQL query explorer, or viewed in Catalog Explorer. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Access Control

The metric tables and dashboard created by a profile are owned by the user who created the profile. Access to metric tables is controlled via Unity Catalog privileges. To share dashboards within a workspace, use the **Share** button on the upper‑right side of the dashboard. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Drift Metrics Table](/concepts/drift-metrics-table.md)
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md)
- Time Series Analysis
- [Inference Log Analysis](/concepts/inferencelog-analysis.md)
- [Data Slicing](/concepts/data-slicing-expressions.md)
- [Baseline Table](/concepts/baseline-table.md)
- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md
- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
2. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
