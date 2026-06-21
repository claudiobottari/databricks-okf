---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5a460ad6a4021cf7c50bdebb86567aefbeac2b07f556b1cf2aa94e765348aea
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profiling-unity-catalog
    - DDP(C
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Databricks Data Profiling (Unity Catalog)
description: API-driven data profiling service for Delta tables in Unity Catalog, supporting TimeSeries, InferenceLog, and Snapshot profile types
tags:
  - databricks
  - data-profiling
  - unity-catalog
timestamp: "2026-06-19T17:54:45.993Z"
---

# Databricks Data Profiling (Unity Catalog)

**Databricks Data Profiling (Unity Catalog)** is a feature that automatically generates and maintains statistical summaries of table data within [Unity Catalog](/concepts/unity-catalog.md). It continuously monitors data quality by computing descriptive statistics, distribution metrics, and drift detection across time windows or between snapshots. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Overview

Data profiling enables you to track the statistical properties of your Unity Catalog tables over time. You can create a profile on any managed or external [Delta Table](/concepts/delta-lake-table.md) registered in Unity Catalog. Only a single profile can be created per table within a [Metastore](/concepts/metastore.md). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

The system stores computed statistics in Unity Catalog metric tables, which can be queried using SQL or viewed in Catalog Explorer and dashboards. A profile can be refreshed on demand or on a scheduled basis using cron expressions. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Requirements

To create and manage profiles via the Python API, install the Databricks SDK version 0.68.0 or later:

```python
%pip install "databricks-sdk>=0.68.0"
```

Authentication follows standard [Databricks SDK authentication](/concepts/databricks-sdk-authentication-methods.md) patterns. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Profile Types

When creating a profile, you select one of three profile types: `TimeSeries`, `InferenceLog`, or `Snapshot`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### TimeSeries Profile

A `TimeSeries` profile compares data distributions across consecutive time windows. It requires: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

- A **timestamp column** (`timestamp_column`), which must be of type `TIMESTAMP` or convertible using `to_timestamp`.
- A set of **granularities** over which to calculate metrics. Available granularities include 5 minutes, 30 minutes, 1 hour, 1 day, 1 week, 2 weeks, 3 weeks, 4 weeks, 1 month, and 1 year.

```python
config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}",
    time_series=TimeSeriesConfig(
        timestamp_column="ts",
        granularities=[AggregationGranularity.AGGREGATION_GRANULARITY_1_DAY]
    ),
    slicing_exprs=["type='Red'"]
)
```

### InferenceLog Profile

An `InferenceLog` profile extends the `TimeSeries` profile by including model quality metrics such as predictions, labels, and model identifiers. It automatically creates slices based on the distinct values of `model_id_col`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Key parameters include:
- `problem_type`: `CLASSIFICATION` or `REGRESSION`
- `prediction_column`: Column containing model predictions
- `model_id_column`: Column identifying different model versions
- `label_column` (optional): Column containing ground-truth labels
- `timestamp_column` and `granularities`: Same as TimeSeries

### Snapshot Profile

A `Snapshot` profile computes metrics over the full contents of the table at the time of each refresh. It shows how the entire table changes over time rather than tracking rolling windows. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

**Note:** The maximum table size for a snapshot profile is 4 TB. For larger tables, use a time series profile instead. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}",
    snapshot=SnapshotConfig(),
    slicing_exprs=["type='Red'"]
)
```

## Best Practices

For TimeSeries and InferenceLog profiles, enable [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on your table. When CDF is enabled, only newly appended data is processed on each refresh, making execution more efficient and reducing costs as you scale across many tables. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Profiles defined on [materialized views](/concepts/materialized-views-in-databricks.md) do not support incremental processing. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Refreshing and Viewing Results

To refresh the metric tables, call `create_refresh`. The calculation runs on serverless compute, not on the notebook's attached cluster. You can continue running commands in the notebook while statistics are updated. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
run_info = w.data_quality.create_refresh(
    object_type=table_object_type,
    object_id=table_id,
    refresh=Refresh(...)
)
```

Use `list_refreshes` to view the refresh history and `get_refresh` to check the status of a specific run. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Metric tables are Unity Catalog tables. They can be queried in notebooks, in the SQL query explorer, and viewed in [Catalog Explorer](/concepts/catalog-explorer.md). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduling and Notifications

Profiles can be scheduled using cron expressions via the `schedule` parameter:

```python
config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    schedule=CronSchedule(
        quartz_cron_expression="0 0 12 * * ?",
        timezone_id="PST",
    )
)
```

Notification settings allow alerts via email when a refresh fails or times out. A maximum of 5 email addresses is supported per event type. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Data Slicing

All profile types support **slicing expressions** (`slicing_exprs`), which are SQL expressions that define subsets of data for separate metric computation. For example, `"type='Red'"` would compute separate statistics for rows where the `type` column equals `'Red'`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Access Control

The metric tables and dashboard created by a profile are owned by the user who created the profile. Access is controlled using standard [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md). Dashboards can be shared within a workspace using the **Share** button. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Limitations

- When you first create a time series or inference profile, Databricks analyzes only data from the 30 days prior to creation. After creation, all new data is processed. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- Snapshot profiles are limited to 4 TB tables. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- Materialized views do not support incremental processing. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Deleting a Profile

Deleting a profile does not automatically delete the metric tables and dashboard created by the profile. Those assets must be deleted in a separate step or can be saved in a different location. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Table](/concepts/delta-lake-table.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Drift Detection](/concepts/data-drift-detection.md)
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md)

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
