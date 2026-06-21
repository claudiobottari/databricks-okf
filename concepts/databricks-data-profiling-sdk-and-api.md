---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4676edd6f85219c117debbfc87127bcd77230e231df971d75524e1854d50b7a5
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profiling-sdk-and-api
    - API and Databricks Data Profiling SDK
    - DDPSAA
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Databricks Data Profiling SDK and API
description: Python SDK and REST API for creating and managing data profiles on Unity Catalog tables programmatically.
tags:
  - databricks
  - api
  - sdk
  - python
timestamp: "2026-06-18T11:13:18.003Z"
---

# Databricks Data Profiling SDK and API

**Databricks Data Profiling** lets you create and manage data profiles on Unity Catalog tables to track data quality, distributions, and model performance over time. You can create, refresh, and monitor profiles using the Databricks Python SDK (`databricks-sdk`) or the REST API. Profiles can be `TimeSeries`, `InferenceLog`, or `Snapshot`, each serving a different monitoring purpose. Only one profile can exist per table in a Unity Catalog [Metastore](/concepts/metastore.md). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Requirements

To use the most recent API features, install the Python client with `%pip install "databricks-sdk>=0.68.0"`. Authenticate to the SDK according to the [Authentication documentation](https://databricks-sdk-py.readthedocs.io/en/latest/authentication.html). A profile can be created on any [managed table](/concepts/unity-catalog-managed-tables.md) or external Delta table registered in [Unity Catalog](/concepts/unity-catalog.md). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Profile Types

When creating a profile, you select one of three types: `TimeSeries`, `InferenceLog`, or `Snapshot`. For `TimeSeries` and `InferenceLog` profiles, only data from the 30 days prior to creation is analyzed initially; after creation, all new data is processed. Profiles defined on [materialized views](/concepts/materialized-views-in-databricks.md) do not support incremental processing. It is a best practice to enable [change data feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on the table so that only newly appended data is processed on each refresh, improving efficiency and reducing cost. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### `TimeSeries` Profile

A `TimeSeries` profile compares data distributions across successive time windows. You must provide:

- A `timestamp_column` of type `TIMESTAMP` (or convertible via `to_timestamp`).
- One or more `granularities` from a predefined list (e.g. `AGGREGATION_GRANULARITY_1_DAY`, `AGGREGATION_GRANULARITY_1_HOUR`).

Optional `slicing_exprs` can be used to filter the rows analyzed (e.g., `["type='Red'"]`). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
# Example TimeSeries profile creation
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

### `InferenceLog` Profile

An `InferenceLog` profile is similar to `TimeSeries` but also computes model quality metrics (e.g., accuracy, drift) by comparing predictions against labels. Required parameters include:

- `prediction_column` – column containing model predictions.
- `model_id_column` – column identifying which model version produced each prediction.
- `timestamp_column` and `granularities` (same as TimeSeries).
- `problem_type` – e.g., `INFERENCE_PROBLEM_TYPE_CLASSIFICATION`.
- `label_column` (optional) – ground truth labels.

Slices are automatically created based on the distinct values of `model_id_col`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
# Example InferenceLog profile creation
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

### `Snapshot` Profile

A `Snapshot` profile analyzes the full contents of the table at each refresh point, capturing how the entire dataset changes over time. The maximum table size for a snapshot profile is 4 TB; for larger tables, use a time series profile instead. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
# Example Snapshot profile creation
config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}",
    snapshot=SnapshotConfig(),
    slicing_exprs=["type='Red'"]
)
```

## Refresh and View Results

To trigger a manual refresh and populate the metric tables, call `w.data_quality.create_refresh(...)`. The calculation runs on [serverless compute](/concepts/serverless-gpu-compute.md) independently of the notebook’s cluster. You can check refresh status by polling with `w.data_quality.get_refresh(...)` while the state is `PENDING` or `RUNNING`. Use `w.data_quality.list_refresh(...)` to see the history of all refreshes. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
run_info = w.data_quality.create_refresh(
    object_type=table_object_type,
    object_id=table_id,
    refresh=Refresh(object_type=table_object_type, object_id=table_id)
)
```

The metric tables are Unity Catalog tables that you can query in notebooks, the SQL query explorer, or view in [Catalog Explorer](/concepts/catalog-explorer.md). The refresh history display requires the same Databricks workspace from which the profile was enabled. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## View Profile Settings

To retrieve the current profile configuration (including type, schedule, notifications), use `w.data_quality.get_monitor(object_type="table", object_id=table.table_id)`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Schedule

You can set a recurring refresh schedule using the `schedule` parameter when creating the profile. The schedule is defined with a quartz cron expression and a timezone ID. The example below runs a snapshot refresh every day at 12:00 PM PST. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk.service.catalog import MonitorCronSchedule

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    schedule=CronSchedule(
        quartz_cron_expression="0 0 12 * * ?",
        timezone_id="PST"
    )
)
```

## Notifications

To receive email alerts when a profile refresh fails or times out, use the `notifications` parameter. You can specify up to five email addresses for the `on_failure` event. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk.service.dataquality import NotificationSettings, NotificationDestination

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

## Control Access to Metric Tables

The metric tables and dashboard created by a profile are owned by the user who created the profile. You can use standard Unity Catalog privileges to control access to the metric tables. To share dashboards within the workspace, use the **Share** button at the upper-right of the dashboard. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Delete a Profile

Deleting a profile removes the monitoring configuration but does **not** delete the associated metric tables or dashboard. Those assets must be removed separately or left in place. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
w.data_quality.delete_monitor(object_type="table", object_id=table.table_id)
```

## Example Notebooks

The documentation includes example notebooks for each profile type: TimeSeries, InferenceLog (regression and classification), and Snapshot. These notebooks demonstrate end-to-end creation, refresh, and analysis of metric tables. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
