---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 333011eed05472a3e8d5a7816cd3d4012b9d090838620136a7e9f04ded4097ab
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - snapshot-profile
    - Snapshot Profiling
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Snapshot Profile
description: A data profile type that profiles the full contents of a table over time, with a 4TB maximum table size limit
tags:
  - databricks
  - snapshot
  - data-profiling
timestamp: "2026-06-19T17:55:52.590Z"
---

# Snapshot Profile

A **Snapshot profile** is a type of [data profile](/concepts/data-profile-databricks.md) in Databricks that captures how the full contents of a table change over time. Unlike time-series profiles that compare data distributions across windows, a snapshot profile calculates metrics over **all data** in the table, reflecting the table state at each refresh.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Characteristics

- **Full-table analysis**: Metrics are computed across the entire table, not just recent partitions or sliding windows.^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- **Point-in-time state**: Each refresh records a complete picture of the table, so you can see how the dataset evolves over time.^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- **No incremental processing**: Like other profile types, snapshot profiles do not support incremental processing on [materialized views](/concepts/materialized-views-in-databricks.md). For such views, consider using a [TimeSeries Profile](/concepts/timeseries-profile.md) instead.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Size Limit

The maximum table size supported for a snapshot profile is **4 TB**. For larger tables, use a [TimeSeries Profile](/concepts/timeseries-profile.md) instead.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Creating a Snapshot Profile (API)

A snapshot profile is created using the Databricks SDK (or REST API) on any managed or external Delta table registered in [Unity Catalog](/concepts/unity-catalog.md). Only one profile can exist per table per [Metastore](/concepts/metastore.md).^[create-a-data-profile-using-the-api-databricks-on-aws.md]

The following Python example creates a snapshot profile with an optional slicing expression:^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.dataquality import Monitor, DataProfilingConfig, SnapshotConfig

w = WorkspaceClient()
schema = w.schemas.get(full_name=f"{catalog}.{schema}")
table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}",
    snapshot=SnapshotConfig(),
    slicing_exprs=["type='Red'"]    # optional
)

info = w.data_quality.create_monitor(
    monitor=Monitor(
        object_type="table",
        object_id=table.table_id,
        data_profiling_config=config,
    ),
)
```

### Key parameters

- `snapshot`: Must be set to `SnapshotConfig()` (no additional fields required) to indicate the profile type.^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- `slicing_exprs` (optional): A list of SQL expressions to create slices — for example, to analyze subsets of data separately.^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- `output_schema_id`: The schema where metric tables are stored; obtained from the schema object.^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- `assets_dir`: A Workspace path for generated dashboards and assets.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Refreshing and Viewing Results

Once created, you can trigger a refresh to compute metrics and update the profile tables. Refreshes run on serverless compute, not on the notebook's attached cluster.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()

run_info = w.data_quality.create_refresh(
    object_type="table",
    object_id=table_id,
    refresh=Refresh(
        object_type="table",
        object_id=table_id,
    )
)
```

Metric tables are [Unity Catalog](/concepts/unity-catalog.md) tables and can be queried in notebooks or SQL query explorer, and viewed in Catalog Explorer. You can also schedule automatic refreshes using a cron expression.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduling

To set a profile to refresh on a schedule, include the `schedule` parameter in `create_monitor`. The example below refreshes daily at noon PST:^[create-a-data-profile-using-the-api-databricks-on-aws.md]

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

## Notifications

You can configure email notifications for failures (up to 5 addresses per event type). Example:^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
notification_settings=NotificationSettings(
    on_failure=NotificationDestination(
        email_addresses=["your_email@domain.com"]
    )
)
```

## Access Control

Metric tables and dashboards created by a profile are owned by the user who created the profile. Use standard Unity Catalog privileges to manage access to metric tables. Dashboards can be shared within the workspace using the **Share** button.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Deleting a Snapshot Profile

Deleting the profile does **not** automatically delete the metric tables or dashboard. Those assets must be removed separately.^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Requirements

- The table must be a managed or external Delta table registered in Unity Catalog.^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- The Databricks SDK version must be `>=0.68.0` to use the latest API features.^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- Authentication must be configured for the SDK. See the [Databricks SDK authentication documentation](https://databricks-sdk-py.readthedocs.io/en/latest/authentication.html).^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The broader practice of analyzing data quality
- [TimeSeries Profile](/concepts/timeseries-profile.md) — Compares data distributions across time windows
- [InferenceLog Profile](/concepts/inferencelog-profile.md) — Time-series profile with model quality metrics
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where profiles are defined
- [Metric Tables](/concepts/profile-metric-tables.md) — The output tables generated by a profile
- Databricks SDK — The programmatic interface for creating profiles

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
