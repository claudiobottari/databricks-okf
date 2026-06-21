---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa121a08ccd547c597b67f543706e2d7c4067310a19d7975e0850bdad58c504c
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profile-scheduling-and-notifications
    - Notifications and Databricks Data Profile Scheduling
    - DDPSAN
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Databricks Data Profile Scheduling and Notifications
description: Configuring cron-based schedules and email notifications for data profile refreshes
tags:
  - databricks
  - scheduling
  - notifications
timestamp: "2026-06-19T17:55:18.823Z"
---

# Databricks Data Profile Scheduling and Notifications

**Databricks Data Profile Scheduling and Notifications** refers to the automated refresh cadence and alerting capabilities that can be configured when creating or updating a data profile (monitor) on a Unity Catalog table. These features allow profile owners to control how frequently profile metrics are recalculated and to receive email alerts when a refresh fails or times out.

## Overview

Data profiles (also called monitors) can be set to run on a scheduled basis instead of being triggered manually. Scheduling is defined at profile creation time through the `schedule` parameter, while notifications for failures are defined through the `notifications` parameter. Both are optional configurations provided within the [`DataProfilingConfig`](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dataquality/data_quality.html) object when calling the `create_monitor` API. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Profiles are created on any managed or external Delta table registered in [Unity Catalog](/concepts/unity-catalog.md). Only one profile can exist per table per [Metastore](/concepts/metastore.md). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduling

The `schedule` parameter accepts a `MonitorCronSchedule` object that specifies a Quartz cron expression and a timezone ID. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Example: Daily refresh at 12 noon PST

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
        quartz_cron_expression="0 0 12 * * ?",  # every day at noon
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

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

The cron expression follows standard Quartz syntax (see cron expressions for more details). The schedule applies to all refresh runs of the profile. For [TimeSeries Profile](/concepts/timeseries-profile.md) and [InferenceLog Profile](/concepts/inferencelog-profile.md) types, incremental processing can be enabled via change data feed (CDF) on the source table, making scheduled refreshes more efficient. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Notifications

The `notifications` parameter accepts a `NotificationSettings` object that contains one or more event-based destinations. Currently, the only supported event is `on_failure`, which triggers when a monitoring refresh fails or times out. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Example: Email notification on failure

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.dataquality import Monitor, DataProfilingConfig, SnapshotConfig, NotificationSettings, NotificationDestination

w = WorkspaceClient()
schema = w.schemas.get(full_name=f"{catalog}.{schema}")
table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")

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

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

A maximum of 5 email addresses is supported per event type (for example, `on_failure`). Notifications are sent to the specified addresses whenever a refresh run fails or times out. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Refreshing metric tables

Regardless of scheduling, you can also trigger a manual refresh using the `create_refresh` API. The refresh calculation runs on serverless compute, independent of the notebook cluster. Metric tables are created or updated in [Unity Catalog](/concepts/unity-catalog.md) and can be queried via SQL or viewed in Catalog Explorer. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Limitations and best practices

- The maximum table size for a [Snapshot Profile](/concepts/snapshot-profile.md) is 4 TB. For larger tables, use a [TimeSeries Profile](/concepts/timeseries-profile.md) instead. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- For `TimeSeries` and `InferenceLog` profiles, enabling [change data feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on the source table is a best practice: it allows incremental processing rather than full table scans on every scheduled refresh. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- Only one profile can exist per table per [Metastore](/concepts/metastore.md). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- Deleting a profile does not automatically delete the associated metric tables and dashboard; those assets must be removed separately. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related concepts

- Data Profiling using the API – Full guide on creating and managing profiles
- [TimeSeries Profile](/concepts/timeseries-profile.md) – Profile type for comparing distributions across time windows
- [InferenceLog Profile](/concepts/inferencelog-profile.md) – Profile type that includes model quality metrics
- [Snapshot Profile](/concepts/snapshot-profile.md) – Profile type that captures the full table state on refresh
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – The schema and contents of the generated metric tables
- Cron expressions – Standard format for scheduling with Quartz
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where profiles and metric tables are registered

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
