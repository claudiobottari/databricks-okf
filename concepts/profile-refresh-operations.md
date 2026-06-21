---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a5803a08b4e6ffeaa7c9a2abab1be825c01ff4ec88273a7b7e0b650e4ee94de3
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-refresh-operations
    - PRO
    - Profile Refresh Methods
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Profile Refresh Operations
description: The process of triggering metric table creation/update via create_refresh API, running on serverless compute, with status monitoring via list_refreshes and get_refresh.
tags:
  - data-quality
  - api
  - operations
timestamp: "2026-06-19T14:29:28.291Z"
---

# Profile Refresh Operations

**Profile Refresh Operations** are the set of actions used to compute updated statistics and quality metrics for an existing [data profile](/concepts/data-profile-databricks.md) on a Unity Catalog table. After a profile is created, it must be refreshed periodically to reflect new or changed data. The refresh can be triggered on demand, scheduled, or monitored via the Databricks SDK and REST API. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Triggering a Refresh

To perform an immediate refresh of a profile’s metric tables, call `create_refresh`: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

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

When this call is made from a notebook, the metric computation runs on [serverless compute](/concepts/serverless-gpu-compute.md), not on the cluster the notebook is attached to. You can continue to run other commands while the refresh is in progress. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Viewing Refresh History and Status

To see all past refresh runs for a profile, use `list_refreshes`: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
it = w.data_quality.list_refresh(object_type=table_object_type, object_id=table_id)
```

To check the status of a specific refresh while it is queued, running, or finished, use `get_refresh` with the `refresh_id`: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
while run_info.state in (RefreshState.MONITOR_REFRESH_STATE_PENDING,
                         RefreshState.MONITOR_REFRESH_STATE_RUNNING):
  run_info = w.data_quality.get_refresh(
    object_type=table_object_type,
    object_id=table_id,
    refresh_id=run_info.refresh_id
  )
  time.sleep(30)
```

The refresh history is visible only from the Databricks workspace in which the profile was originally enabled. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduling Automatic Refreshes

When creating a profile, you can set a recurring schedule using the `schedule` parameter. This parameter accepts a cron expression and a time zone: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk.service.catalog import MonitorCronSchedule

config = DataProfilingConfig(
  output_schema_id=schema.schema_id,
  snapshot=SnapshotConfig(),
  schedule=CronSchedule(
    quartz_cron_expression="0 0 12 * * ?",   # every day at 12 noon
    timezone_id="PST",
  )
)
```

The profile will then be refreshed automatically at the specified intervals. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Notifications for Refresh Failures

You can configure notifications so that specific email addresses are alerted when a refresh fails or times out. This is done with the `notifications` parameter during profile creation: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

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

A maximum of five email addresses is supported per event type (for example, `on_failure`). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Performance Considerations

For TimeSeries and InferenceLog profiles, it is a best practice to enable [change data feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on the source table. When CDF is enabled, only newly appended data is processed during each refresh instead of re-scanning the entire table. This makes refreshes more efficient and reduces cost as the number of profiled tables grows. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Note: Profiles defined on materialized views do not support incremental processing; every refresh recomputes over the full view. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- [TimeSeries Profile](/concepts/timeseries-profile.md)
- [InferenceLog Profile](/concepts/inferencelog-profile.md)
- [Snapshot Profile](/concepts/snapshot-profile.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Metric Tables](/concepts/profile-metric-tables.md)
- Serverless Compute
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md)

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
