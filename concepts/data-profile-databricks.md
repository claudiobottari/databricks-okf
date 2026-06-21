---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e336485246a3fb032628be7affd3525e76589be5d671e612de517313cbc27673
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profile-databricks
    - DP(
    - Data Profile
    - data profile
    - data profiles
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Data Profile (Databricks)
description: "A monitoring construct on a Unity Catalog Delta table that tracks data quality metrics over time, supporting three profile types: TimeSeries, InferenceLog, and Snapshot."
tags:
  - data-quality
  - unity-catalog
  - monitoring
timestamp: "2026-06-19T14:29:01.201Z"
---

# Data Profile (Databricks)

A **Data Profile** (also referred to as a **monitor** in the Databricks SDK) is a mechanism in [Unity Catalog](/concepts/unity-catalog.md) that continuously computes statistical metrics and distribution summaries on a table’s data. Data profiles help you monitor data quality, track changes over time, and detect anomalies. A profile can be created on any managed or external [Delta table](/concepts/delta-lake.md) registered in Unity Catalog. Only one profile per table is allowed in a given [Metastore](/concepts/metastore.md). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Requirements

To use the latest version of the data profiling API, install the Databricks Python SDK version 0.68.0 or later:

```python
%pip install "databricks-sdk>=0.68.0"
```

You must also configure authentication as described in the [Databricks SDK authentication documentation](https://databricks-sdk-py.readthedocs.io/en/latest/authentication.html). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Profile Types

When creating a profile, you choose one of three types: `TimeSeries`, `InferenceLog`, or `Snapshot`. Each type defines how data is sampled and aggregated. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### TimeSeries Profile

A `TimeSeries` profile compares data distributions across successive time windows. It requires:

- A **timestamp column** with a `TIMESTAMP` data type (or a type convertible via `to_timestamp`).
- One or more **granularities** for aggregation (e.g., 5 minutes, 1 hour, 1 day, 1 month, 1 year).

Example configuration:

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

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

**Best practice:** Enable [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on the table so that incremental updates are processed instead of re-reading the entire table on every refresh. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### InferenceLog Profile

An `InferenceLog` profile extends the `TimeSeries` profile with model quality metrics. It requires:

- `problem_type`: classification or regression.
- `prediction_column`, `model_id_column`, and optionally `label_column`.
- A `timestamp_column` and `granularities`.

Slices are automatically created from distinct values of the `model_id_col`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}",
    inference_log=InferenceLogConfig(
        problem_type=InferenceProblemType.INFERENCE_PROBLEM_TYPE_CLASSIFICATION,
        prediction_column="preds",
        model_id_column="model_ver",
        label_column="label",
        timestamp_column="ts",
        granularities=[AggregationGranularity.AGGREGATION_GRANULARITY_1_DAY]
    )
)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

**Note:** When first created, a `TimeSeries` or `InferenceLog` profile analyzes only the last 30 days of data. After creation, all new data is processed incrementally. Profiles defined on materialized views do not support incremental processing. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Snapshot Profile

A `Snapshot` profile computes metrics over the full contents of the table at each refresh. It reflects the complete table state at the time of the refresh. The maximum supported table size for a snapshot profile is **4 TB**; for larger tables, use a `TimeSeries` profile instead. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}",
    snapshot=SnapshotConfig(),
    slicing_exprs=["type='Red'"]
)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Creating a Profile

Use the `w.data_quality.create_monitor()` method, passing a `Monitor` object with `object_type` set to `"table"` and `object_id` set to the table’s UUID. The `data_profiling_config` contains the profile type and its parameters. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Refreshing and Viewing Results

- **`create_refresh`**: Triggers a refresh of the profile metrics. The computation runs on serverless compute, not on the notebook’s attached cluster. You can continue running other commands while statistics update. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- **`list_refreshes`**: Lists the history of all refreshes.
- **`get_refresh`**: Checks the status of a specific refresh (pending, running, finished).

The resulting metric tables are stored as [Unity Catalog](/concepts/unity-catalog.md) tables and can be queried via notebooks or SQL query explorer. They also appear in Catalog Explorer. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Viewing Profile Settings

Use `w.data_quality.get_monitor()` to retrieve the current configuration of a profile, including its type, schedule, and notification settings. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduling

You can attach a cron schedule to a profile so that it refreshes automatically. The schedule is set in the `DataProfilingConfig` using a `CronSchedule` object with a `quartz_cron_expression` and a `timezone_id`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    schedule=CronSchedule(
        quartz_cron_expression="0 0 12 * * ?",
        timezone_id="PST"
    )
)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Notifications

You can configure email notifications for refresh failures or timeouts using the `notification_settings` parameter. Up to five email addresses are supported per event type. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    notification_settings=NotificationSettings(
        on_failure=NotificationDestination(
            email_addresses=["your_email@domain.com"]
        )
    )
)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Controlling Access to Metric Tables

The metric tables and the associated dashboard are owned by the user who created the profile. Access can be controlled using standard [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md). To share the dashboard within the workspace, use the **Share** button in the dashboard UI. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Deleting a Profile

To delete a profile, call `w.data_quality.delete_monitor()`. This does **not** delete the metric tables or dashboard created by the profile; those assets must be removed separately or saved to a different location. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Example Notebooks

The Databricks documentation provides example notebooks for each profile type:
- TimeSeries profile notebook
- InferenceLog profile (regression) notebook
- InferenceLog profile (classification) notebook
- Snapshot profile notebook

These illustrate how to create a profile, refresh it, and examine the resulting metric tables. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- Databricks SDK

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
