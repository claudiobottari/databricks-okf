---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5ca71dbeafaebfeec33f9c3f327ca1747f6896c51e87e57e3ccae9470783c633
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profile-refresh-management
    - DDPRM
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Databricks Data Profile Refresh Management
description: Creating, listing, and monitoring refresh runs for data profiles using the API
tags:
  - databricks
  - refresh
  - data-profiling
timestamp: "2026-06-19T17:55:14.474Z"
---

# Databricks Data Profile Refresh Management

**Data Profile Refresh Management** refers to the set of API operations and configuration options used to trigger, schedule, monitor, and retrieve the status of data profile refreshes in Databricks. A data profile computes statistical metrics over a table’s data, and refreshing it updates the associated metric tables with the latest information. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Overview

When a data profile is created on a Unity Catalog registered table (managed or external Delta), the system supports both manual and scheduled refreshes. Refreshes are run on serverless compute rather than on the notebook cluster, allowing the notebook to continue executing while the statistics are updated. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

The refresh mechanism is used for all profile types: `TimeSeries`, `InferenceLog`, and `Snapshot`. For `TimeSeries` and `InferenceLog` profiles, the first refresh analyzes only data from the 30 days prior to profile creation; subsequent refreshes process all newly ingested data. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Refreshing Metrics Tables

To manually trigger a refresh, use the `create_refresh` method from the Databricks SDK:

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

This call creates or updates the [Profile Metrics Table](/concepts/profile-metrics-table.md) and [Drift Metrics Table](/concepts/drift-metrics-table.md) for the profiled table. The refresh runs asynchronously on Databricks serverless compute. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduling

Refreshes can be scheduled by providing a `CronSchedule` in the `schedule` parameter when creating the profile via `create_monitor`. The schedule uses a standard quartz cron expression and a timezone:

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

Once set, the profile refreshes automatically at the specified intervals. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Viewing Refresh History and Status

To list all refresh runs associated with a profile, call `list_refreshes`:

```python
it = w.data_quality.list_refresh(object_type=table_object_type, object_id=table_id)
```

To check the status of a specific refresh (e.g., pending, running, or finished), use `get_refresh` with the `refresh_id` obtained from the list:

```python
run_info = w.data_quality.get_refresh(
  object_type=table_object_type,
  object_id=table_id,
  refresh_id=run_info.refresh_id
)
```

The refresh state can be polled until it leaves the pending or running state. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Notifications

Notifications can be configured to alert when a refresh fails or times out. The `notification_settings` parameter of `create_monitor` accepts an `on_failure` destination that can include up to five email addresses:

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

Notifications are triggered per event type (e.g., “on_failure”). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Important Considerations

- The first time a `TimeSeries` or `InferenceLog` profile is refreshed, only data from the last 30 days is processed. Subsequent refreshes cover all new data since the last refresh. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- Profile refreshes run on serverless compute, not on the cluster attached to the notebook. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- For `TimeSeries` and `InferenceLog` profiles, enabling [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on the source table is recommended so that only newly appended data is processed, improving efficiency. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- Refresh history can only be viewed from the Databricks workspace where the profile was originally created. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- Deleting a profile via `delete_monitor` does **not** delete the metric tables or the associated dashboard; those assets must be removed separately. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of statistical analysis on Databricks tables.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for each column, time window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics that track distribution changes over time.
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) – The default time boundary applied to the first refresh of time series and inference profiles.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – A profile type that includes model quality metrics.
- Time Series Analysis – A profile type for monitoring data over continuous time windows.
- Snapshot Analysis – A profile type that profiles the full table contents at each refresh.

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
