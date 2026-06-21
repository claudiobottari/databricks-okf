---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6bfc88f8c7b25af173a0af44d91a9cbe8d9a873268660313f823bf8bf5aac206
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profile-data-profiling-in-unity-catalog
    - DDP(PIUC
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Databricks Data Profile (Data Profiling in Unity Catalog)
description: "A feature in Databricks Unity Catalog that tracks statistical properties and quality metrics of Delta tables over time, supporting three profile types: TimeSeries, InferenceLog, and Snapshot."
tags:
  - data-quality
  - unity-catalog
  - databricks
  - data-profiling
timestamp: "2026-06-18T14:46:46.735Z"
---

# Databricks Data Profile (Data Profiling in Unity Catalog)

**Databricks Data Profile** (also referred to as data profiling in Unity Catalog) is a feature that automatically computes and tracks statistical metrics, schema changes, and data quality indicators over time for Unity Catalog tables. It supports three profile types — `TimeSeries`, `InferenceLog`, and `Snapshot` — and can be created and managed via the Databricks SDK, the REST API, or Catalog Explorer. Only a single profile can exist per table within a [Metastore](/concepts/metastore.md).^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Profiles can be created on any managed or external Delta table registered in Unity Catalog. Metrics computed by a profile are stored in Unity Catalog metric tables and can be queried using SQL or viewed in dashboards. Profiling refreshes run on serverless compute, independent of the notebook cluster.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Profile Types

### `TimeSeries` Profile
A `TimeSeries` profile compares data distributions across consecutive time windows. It requires:
- A `timestamp_column` of type `TIMESTAMP` (or coercible via `to_timestamp`).
- One or more `granularities` (e.g., `AGGREGATION_GRANULARITY_1_DAY`, `AGGREGATION_GRANULARITY_1_HOUR`, `AGGREGATION_GRANULARITY_1_WEEK`, up to `AGGREGATION_GRANULARITY_1_YEAR`).

Optionally, `slicing_exprs` can filter which rows are included.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### `InferenceLog` Profile
An `InferenceLog` profile extends the `TimeSeries` profile by also computing model quality metrics. It is intended for tables that store model inference logs. Parameters include:
- `problem_type`: `INFERENCE_PROBLEM_TYPE_CLASSIFICATION` or regression types.
- `prediction_column`: column containing model predictions.
- `model_id_column`: column distinguishing different model versions.
- `label_column` (optional): ground truth column.
- `timestamp_column` and `granularities` as in TimeSeries.

Slices are automatically created from distinct values of `model_id_col`.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### `Snapshot` Profile
A `Snapshot` profile measures the full contents of the table at each refresh. Metrics reflect the entire table state, not windows. The maximum table size for a snapshot profile is 4 TB; larger tables should use time-series profiles. Slicing expressions are supported.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

> **Note**: When a time series or inference profile is first created, Databricks analyzes only data from the 30 days prior to creation. After creation, all new data is processed. Profiles on materialized views do **not** support incremental processing. Enable [change data feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on the table for efficient incremental refreshes.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Creating a Profile

Profiles are created using the Databricks SDK or the REST API. The Python client requires `databricks-sdk>=0.68.0`. The configuration is passed as a `DataProfilingConfig` object with `output_schema_id`, `assets_dir`, and the profile-specific configuration (e.g., `time_series`, `inference_log`, or `snapshot`). The `object_type` is always `"table"`. Here is a minimal example for a `TimeSeries` profile:

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.dataquality import Monitor, DataProfilingConfig, TimeSeriesConfig, AggregationGranularity

w = WorkspaceClient()
schema = w.schemas.get(full_name=f"{catalog}.{schema}")
table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}",
    time_series=TimeSeriesConfig(
        timestamp_column="ts",
        granularities=[AggregationGranularity.AGGREGATION_GRANULARITY_1_DAY]
    ),
    slicing_exprs=["type='Red'"]
)

info = w.data_quality.create_monitor(
    monitor=Monitor(
        object_type="table",
        object_id=table.table_id,
        data_profiling_config=config,
    ),
)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Similar API calls exist for `InferenceLog` and `Snapshot` profiles, using the respective configuration classes.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Refreshing and Viewing Results

To trigger a profile refresh, use `create_refresh`. The refresh runs serverless compute; other notebook commands can continue concurrently.

```python
run_info = w.data_quality.create_refresh(
    object_type="table",
    object_id=table_id,
    refresh=Refresh(object_type="table", object_id=table_id)
)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

You can poll the status using `get_refresh` and list refresh history with `list_refreshes`. Profile metrics are stored in Unity Catalog metric tables; query them in notebooks, the SQL editor, or Catalog Explorer.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

To view current profile settings, use `get_monitor`.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduling

Scheduled refreshes are configured via the `schedule` parameter in `create_monitor`, using a `CronSchedule` with a quartz cron expression and timezone. For example, the following schedules a daily refresh at noon PST:

```python
from databricks.sdk.service.catalog import MonitorCronSchedule

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    schedule=MonitorCronSchedule(
        quartz_cron_expression="0 0 12 * * ?",
        timezone_id="PST",
    ),
)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Notifications

Notifications on refresh failure or timeout can be set using `notification_settings` with `on_failure`. Up to five email addresses are supported per event type.

```python
config = DataProfilingConfig(
    # ... other config ...
    notification_settings=NotificationSettings(
        on_failure=NotificationDestination(
            email_addresses=["your_email@domain.com"]
        )
    )
)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Access Control

Metric tables and dashboards are owned by the profile creator. Unity Catalog privileges control access to the metric tables. Dashboards can be shared within the workspace using the **Share** button.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Deleting a Profile

To delete a profile, call `delete_monitor`. This does **not** delete the metric tables or dashboard; they must be removed separately or saved to another location.

```python
w.data_quality.delete_monitor(object_type="table", object_id=table.table_id)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Tables](/concepts/unity-catalog-delta-table.md) – The tables on which profiles are defined.
- [Metric Tables](/concepts/profile-metric-tables.md) – The output Unity Catalog tables storing profiling results.
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) – Enables incremental processing for efficient refreshes.
- Databricks SDK for Python – The client library used for API calls.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI for viewing and managing profiles.
- Serverless Compute – The compute engine that runs profile refreshes.

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
