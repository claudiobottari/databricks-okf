---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c12e9772785103f99c14772fc4608c596224292631179ab03b127b4dc96dffe5
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-refresh-and-scheduling
    - Scheduling and Profile Refresh
    - PRAS
    - Scheduling Profile Refreshes
    - Profile Schedules
    - scheduled profile run
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Profile Refresh and Scheduling
description: Mechanisms to refresh data profiling metrics on-demand or on a cron schedule, with serverless compute execution.
tags:
  - databricks
  - scheduling
  - data-quality
timestamp: "2026-06-18T11:13:20.647Z"
---

# Profile Refresh and Scheduling

**Profile Refresh and Scheduling** refers to the mechanisms for triggering updates to [data profiles](/concepts/data-profile-databricks.md) in Databricks and automating those updates on a recurring basis. Profiles are computed metrics about the contents of a Unity Catalog table (TimeSeries, InferenceLog, or Snapshot type). After a profile is created, its metric tables must be refreshed periodically to reflect new data. Refresh can be performed on-demand using the API or automatically via a cron-based schedule. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## On-Demand Refresh

To manually refresh a profile’s metric tables, use the `create_refresh` method from the Databricks SDK. The refresh computation runs on serverless compute, not on the notebook’s attached cluster, so notebook commands can continue while the update proceeds. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
run_info = w.data_quality.create_refresh(
    object_type="table",
    object_id=table_id,
    refresh=Refresh(object_type="table", object_id=table_id),
)
```

After calling `create_refresh`, you can monitor the refresh status with `list_refreshes` and `get_refresh`. The refresh moves through `MONITOR_REFRESH_STATE_PENDING`, `RUNNING`, and terminal states such as `SUCCESS` or `FAILED`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
it = w.data_quality.list_refresh(object_type="table", object_id=table_id)
run_info = next(it, None)
while run_info.state in (
    RefreshState.MONITOR_REFRESH_STATE_PENDING,
    RefreshState.MONITOR_REFRESH_STATE_RUNNING,
):
    run_info = w.data_quality.get_refresh(
        object_type="table",
        object_id=table_id,
        refresh_id=run_info.refresh_id,
    )
    time.sleep(30)
```

For profiles with change data feed (CDF) enabled on the table, only newly appended data is processed on each refresh rather than the entire table, improving efficiency and reducing cost. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduled Refresh

A profile can be configured to refresh automatically on a recurring schedule. Provide a `CronSchedule` object inside the `schedule` parameter of `create_monitor`. The schedule is defined by a quartz cron expression and a time zone ID. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk.service.catalog import MonitorCronSchedule

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    schedule=MonitorCronSchedule(
        quartz_cron_expression="0 0 12 * * ?",  # daily at 12:00
        timezone_id="PST",
    ),
)

info = w.data_quality.create_monitor(
    monitor=Monitor(
        object_type="table",
        object_id=table.table_id,
        data_profiling_config=config,
    )
)
```

The schedule can be added at profile creation time. To update or remove the schedule after creation, use the `update_monitor` method (not shown in the source). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Notifications

To receive alerts when a profile refresh fails or times out, configure the `notifications` parameter with an email address. Up to 5 email addresses are supported per event type. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk.service.dataquality import NotificationSettings, NotificationDestination

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    notification_settings=NotificationSettings(
        on_failure=NotificationDestination(
            email_addresses=["your_email@domain.com"]
        )
    ),
)

info = w.data_quality.create_monitor(...)
```

After the profile is created, you can also view and manage notifications through Catalog Explorer. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Viewing Refresh History

The full history of all refreshes associated with a profile can be retrieved using `list_refreshes`. Each entry shows the refresh state, timestamps, and other metadata. The refresh history is only accessible from the Databricks workspace where the profile was created. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The overall practice of generating statistics and metrics about table data.
- [TimeSeries Profile](/concepts/timeseries-profile.md) – Profiles that compare data distributions across time windows.
- [InferenceLog Profile](/concepts/inferencelog-profile.md) – Profiles that include model quality metrics alongside time-series analysis.
- [Snapshot Profile](/concepts/snapshot-profile.md) – Profiles that capture the full table state at each refresh.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that stores profile configurations and metric tables.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Enabling CDF improves incremental refresh efficiency.
- Cron Expression – Standard format for defining recurring schedules.

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
