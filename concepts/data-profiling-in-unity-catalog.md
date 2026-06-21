---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc633086df23adf6d549457bfb48c29d86a5b5504cf90329973d9595829f18dd
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-in-unity-catalog
    - DPIUC
    - Data Billing in Unity Catalog
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Data Profiling in Unity Catalog
description: The practice of analyzing and generating statistical summaries of table data within Databricks Unity Catalog to monitor data quality over time.
tags:
  - data-governance
  - unity-catalog
  - data-quality
timestamp: "2026-06-19T17:57:14.506Z"
---

# Data Profiling in Unity Catalog

**Data Profiling in Unity Catalog** is a feature that automatically analyzes the statistical properties of tables registered in [Unity Catalog](/concepts/unity-catalog.md), providing insights into data quality, distribution, and trends over time. Profiles can be created through the Databricks UI or programmatically via the API, and they store results in Unity Catalog-managed metric tables for querying and visualization. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Overview

Data profiling in Unity Catalog enables data engineers and analysts to understand the characteristics of their datasets without writing custom analysis code. The system computes statistical summaries, detects anomalies, and tracks changes to data distributions over time. Profiles are configured per table and can be scheduled to run automatically or triggered manually. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Profile Types

The system supports three profile types, each designed for different monitoring scenarios: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

| Profile Type | Use Case |
|---|---|
| `Snapshot` | One-time or periodic analysis of the entire table's current state |
| `TimeSeries` | Track how data distributions change over time windows |
| `Inference` | Monitor model prediction quality and drift over time |

### Snapshot Profile

A snapshot profile analyzes the table at a point in time, computing standard statistics such as row count, null counts, distinct values, min/max values, and distribution summaries for each column. This is suitable for ad-hoc data quality checks or baseline establishment. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### TimeSeries Profile

A time series profile requires additional configuration beyond the snapshot type: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- **Metric granularities**: Defines how to partition data into time windows (e.g., hourly, daily, weekly) for trend analysis.
- **Timestamp column**: The column containing timestamps to partition data. The data type must be `TIMESTAMP` or convertible using the `to_timestamp` PySpark function.

When first created, a time series profile analyzes only data from the 30 days prior to creation. After creation, all new data is processed incrementally. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Inference Profile

An inference profile is designed for monitoring machine learning model outputs in production. In addition to granularities and timestamp columns, it requires: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- **Problem type**: Either classification or regression.
- **Prediction column**: The column containing the model's predicted values.
- **Label column** (optional): The column containing ground truth for model predictions, enabling accuracy and drift metrics.
- **Model ID column**: The column identifying which model generated each prediction.

## Creating a Profile Using the UI

### Prerequisites

Access the Databricks UI by: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

1. Clicking the **Data icon** in the workspace left sidebar to open [Catalog Explorer](/concepts/catalog-explorer.md).
2. Navigating to the table you want to profile.
3. Clicking the **Quality** tab.
4. Enabling anomaly detection for the schema if not already enabled.

### Configuration Steps

1. In the **Quality** tab, click **Configure** to open the **Data Quality Monitoring** dialog.
2. In the **Data profiling** field, click **Configure**.
3. Select the **Profile type** from the dropdown menu.
4. For `TimeSeries` and `Inference` profiles, specify the required parameters as described above.

It is a best practice to enable [change data feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on the table for `TimeSeries` and `Inference` profiles. When CDF is enabled, only newly appended data is processed rather than re-processing the entire table every refresh, improving efficiency and reducing costs as profiling scales across many tables. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Advanced Options

#### Schedule

Profiles can be scheduled to run automatically or refreshed manually: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- **Refresh on schedule**: Select frequency and time for automatic runs.
- **Refresh manually**: Run profiles on demand from the **Quality** tab.

#### Notifications

Email notifications can be configured for profile events, supporting up to five email addresses per notification event type. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

#### Metrics Configuration

The following settings can be customized: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- **Metrics tables schema name**: The Unity Catalog schema where metric tables are stored. Default: same schema as the profiled table.
- **Assets directory**: Absolute path to store profiling assets. Default: `/Users/{user_name}/databricks_lakehouse_monitoring/{table_name}`. This field cannot be left blank.
- **Baseline table name**: A table or view containing baseline data for comparison.
- **Metric slicing expressions**: Define subsets of the table to profile independently. For example, `"col_2 > 10"` generates two slices: one for `col_2 > 10` and one for `col_2 <= 10`. An expression like `"col_1"` generates one slice per unique value in `col_1`.
- **Custom metrics**: Appear in metric tables alongside built-in metrics. Types include `Aggregate`, `Derived`, or `Drift`. Each requires a name, input columns, output Spark data type, and SQL definition.

### Editing an Existing Profile

After profile creation, settings can be modified by clicking **Configure** on the **Quality** tab, then clicking **Configure** in the **Data profiling** section of the dialog. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Viewing Profile Results

Profile results are stored in Unity Catalog tables. To view results: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- Click **View refresh history** to see all previous profile runs.
- Click **Refresh metrics** to trigger a manual profile update.
- Query metric tables in notebooks or the SQL query explorer.
- View metric tables in Catalog Explorer.

Access to the refresh history requires using the Databricks workspace from which data profiling was enabled. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

For detailed information about the statistics stored in profile metric tables, see Monitor metric tables. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Access Control

Metric tables and dashboards created by a profile are owned by the profile creator. Access can be controlled using [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md): ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- Grant or revoke permissions on metric tables through Unity Catalog.
- Share dashboards within a workspace using the **Share** button in the upper-right corner of the dashboard.

## Deleting a Profile

To delete a profile: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

1. Open the **Update profile** dialog by following the steps to edit configuration.
2. From the **Update** dropdown menu, select **Delete**.

## Best Practices

- **Enable CDF** for time series and inference profiles to improve performance and reduce costs through incremental processing. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Use path-based slicing** for logical data subsets rather than creating separate profiles for each category.
- **Configure notifications** for critical tables to alert relevant teams when data quality issues are detected.
- **Store assets in shared directories** (e.g., `/Shared/`) for profiles intended to be accessed across the organization. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Document baseline tables** and comparison criteria to ensure consistent interpretation of drift metrics.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that supports profiling
- [Anomaly Detection](/concepts/anomaly-detection.md) — Detection of unusual patterns in data profiles
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — Enables incremental processing for profiles
- [Lakehouse Monitoring](/concepts/lakehouse-monitoring.md) — The monitoring framework that data profiling is part of
- [Custom Metrics in Data Profiling](/concepts/custom-metrics-in-data-profiling.md) — User-defined metrics for specialized analysis
- [Slicing Expressions](/concepts/data-slicing-expressions.md) — Partition data into meaningful subsets for granular profiling

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
