---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10caf70953a9be3d36edabb5418666317b0fee2cc964a360000a5e1d0a17c470
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-scheduling-and-notifications
    - Notifications and Profile Scheduling
    - PSAN
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Profile Scheduling and Notifications
description: Configuration options for data profiles including scheduled refreshes using cron expressions and failure notifications via email (up to 5 addresses).
tags:
  - data-quality
  - scheduling
  - notifications
timestamp: "2026-06-19T14:29:38.537Z"
---

# Profile Scheduling and Notifications

Profile scheduling and notifications allow you to configure when a data profile runs automatically and how you are alerted to its results. When creating a profile via the Databricks SDK or REST API, you can set a cron-based schedule and configure email notifications for failures. These settings are specified at profile creation time. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduling

To set up a profile to run on a scheduled basis, use the `schedule` parameter of `create_monitor`. The schedule is defined using a quartz cron expression and a timezone ID. The following example schedules a refresh every day at 12:00 noon Pacific Time: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

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
        quartz_cron_expression="0 0 12 * * ?",  # every day at 12 noon
        timezone_id="PST",
    )
)

info = w.data_quality.create_monitor(
    monitor=Monitor(
        object_type="table",
        object_id=table.table_id,
        data_profiling_config=config,
    ),
)
```

If you do not set a schedule, the profile will not run automatically and must be refreshed manually using `create_refresh`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Notifications

To set up email notifications for a profile, use the `notification_settings` parameter of `create_monitor`. You can specify email addresses to be notified when a monitoring refresh fails or times out: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk.service.dataquality import Monitor, DataProfilingConfig, SnapshotConfig, NotificationSettings, NotificationDestination

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    notification_settings=NotificationSettings(
        on_failure=NotificationDestination(
            email_addresses=["your_email@domain.com"]
        )
    )
)

info = w.data_quality.create_monitor(
    monitor=Monitor(
        object_type="table",
        object_id=table.table_id,
        data_profiling_config=config,
    ),
)
```

A maximum of 5 email addresses is supported per event type (for example, “on_failure”). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Viewing Current Settings

You can review the current schedule and notification configuration of a profile using the `get_monitor` API: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
w.data_quality.get_monitor(object_type="table", object_id=table.table_id)
```

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The process of generating data quality metrics from Unity Catalog tables.
- [Metric Tables](/concepts/profile-metric-tables.md) — Unity Catalog tables that store profile results and can be queried directly.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — A best practice for efficient profile processing on `TimeSeries` and `InferenceLog` profiles.

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
