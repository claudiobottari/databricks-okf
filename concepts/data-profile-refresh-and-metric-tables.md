---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2297e0472aee295e1254ec1cab6a7d3543457729e4fe0f785e132745f3c57db
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profile-refresh-and-metric-tables
    - Metric Tables and Data Profile Refresh
    - DPRAMT
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Data Profile Refresh and Metric Tables
description: The process of refreshing data profile metrics using create_refresh, viewing refresh history, and accessing metric tables stored as Unity Catalog tables for querying.
tags:
  - databricks
  - data-profiling
  - metrics
  - unity-catalog
  - refresh
timestamp: "2026-06-19T09:27:41.482Z"
---

# Data Profile Refresh and Metric Tables

**Data Profile Refresh and Metric Tables** refers to the process of updating a [data profile](/concepts/data-profile-databricks.md) on a Unity Catalog table and the underlying storage tables (metric tables) that hold the computed statistics. Refreshing a profile recomputes the profiling metrics and updates these metric tables, which are Unity Catalog tables that can be queried and viewed.

## Data Profile Refresh

A data profile must be refreshed to compute or update its statistics. The API method `create_refresh` triggers the refresh operation. When called from a notebook, the metric tables are created or updated. The refresh calculation runs on [serverless compute](/concepts/serverless-gpu-compute.md), not on the cluster the notebook is attached to, so notebook commands can continue while the statistics are being updated. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
run_info = w.data_quality.create_refresh(
    object_type=table_object_type,
    object_id=table_id,
    refresh=Refresh(
        object_type=table_object_type,
        object_id=table_id,
    )
)
```

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Refresh History

To view the history of all refreshes associated with a profile, use `list_refreshes`:^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
it = w.data_quality.list_refresh(object_type=table_object_type, object_id=table_id)
```

To check the status of a specific refresh (queued, running, or finished), use `get_refresh`:^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
it = w.data_quality.list_refresh(object_type=table_object_type, object_id=table_id)
run_info = next(it, None)
while run_info.state in (RefreshState.MONITOR_REFRESH_STATE_PENDING,
                         RefreshState.MONITOR_REFRESH_STATE_RUNNING):
    run_info = w.data_quality.get_refresh(
        object_type=table_object_type,
        object_id=table_id,
        refresh_id=run_info.refresh_id
    )
    time.sleep(30)
```

### First Refresh Behavior

When a `TimeSeries` or `InferenceLog` profile is first created, the initial refresh analyzes only data from the 30 days prior to creation. After the profile is created, all new data is processed in subsequent refreshes. Profiles defined on [materialized views](/concepts/materialized-views-in-databricks.md) do not support incremental processing. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Metric Tables

The statistics computed by a data profile are stored in **metric tables**. These are Unity Catalog tables that are automatically created or updated during a refresh. They can be queried in notebooks, in the SQL query explorer, and viewed in [Catalog Explorer](/concepts/catalog-explorer.md). For information about the statistics stored in these tables, see the Monitor metric tables documentation. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Access Control

Metric tables are owned by the user who created the profile. Access can be controlled using standard Unity Catalog privileges. Dashboards created alongside the profile can be shared within a workspace using the **Share** button. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Schedule

A profile can be configured to run on a scheduled basis using the `schedule` parameter of `create_monitor`. The schedule is defined with a cron expression and a timezone. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.catalog import MonitorTimeSeries, MonitorCronSchedule

w = WorkspaceClient()
schema = w.schemas.get(full_name=f"{catalog}.{schema}")
table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    schedule=CronSchedule(
        quartz_cron_expression="0 0 12 * * ?",  # daily at 12 noon
        timezone_id="PST",
    )
)
info = w.data_quality.create_monitor(
    monitor=Monitor(
        object_type="table",
        object_id=table.table_id,
        data_profiling_config=config,
    )
)
```

## Notifications

Notifications can be configured to alert when a refresh fails or times out. Use the `notifications` parameter of `create_monitor` with the `on_failure` setting. A maximum of five email addresses is supported per event type. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

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

## Viewing Profile Settings

To review the current settings of a profile, use the `get_monitor` API method. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")
w.data_quality.get_monitor(object_type="table", object_id=table.table_id)
```

## Related Concepts

- [Data Profile Types](/concepts/data-profiling-analysis-types.md) (TimeSeries, InferenceLog, Snapshot)
- [Create a Data Profile using the API](/concepts/databricks-data-profiling-api.md)
- Monitor Metric Tables
- Serverless Compute
- [Catalog Explorer](/concepts/catalog-explorer.md)
- Cron Expressions

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
