---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d53592cca52b74fcf4452be6e0393ced0075420f4e558d7f4946c0d8803ca40
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-profile-scheduling-and-notifications
    - Notifications and Databricks Profile Scheduling
    - DPSAN
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Databricks Profile Scheduling and Notifications
description: Configuring cron-based schedules and email notifications for automated data profile refreshes in Databricks.
tags:
  - databricks
  - scheduling
  - notifications
  - data-profiling
timestamp: "2026-06-19T09:27:25.735Z"
---

## Databricks Profile Scheduling and Notifications

**Databricks Profile Scheduling and Notifications** covers how to configure automated refreshes and alerting for [Data Profiling](/concepts/data-profiling.md) monitors created on Unity Catalog tables. When you create a data profile (monitor) using the Databricks SDK or REST API, you can set a schedule that triggers periodic refresh calculations and define notification rules that send email alerts when a refresh fails or times out. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Scheduling a Profile Refresh

To run a profile refresh on a recurring basis, include the `schedule` parameter in the `create_monitor` call. The schedule is defined using a `MonitorCronSchedule` object that specifies a Quartz cron expression and a timezone ID. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk.service.catalog import MonitorCronSchedule

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    snapshot=SnapshotConfig(),
    schedule=MonitorCronSchedule(
        quartz_cron_expression="0 0 12 * * ?",   # every day at noon
        timezone_id="PST",
    ),
)
```

The cron expression follows standard Unix cron syntax (see Cron Expressions). The timezone ID must be a valid IANA time zone string (e.g., `"PST"`, `"America/New_York"`). Once set, the profile will automatically refresh at the specified intervals. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Configuring Notifications

You can configure notifications to alert you when a profile refresh fails or times out. Notifications are set via the `notification_settings` parameter in `create_monitor`. Use a `NotificationSettings` object with an `on_failure` field that points to a `NotificationDestination` containing email addresses. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

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
```

A maximum of five email addresses is supported per event type (e.g., `on_failure`). The notification is sent only when a refresh run fails or times out. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Considerations

- Scheduling and notifications are optional parameters of the `create_monitor` API call. If omitted, the profile must be refreshed manually (e.g., via `create_refresh`), and no alert emails are sent. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- The `schedule` and `notification_settings` can be combined in a single `DataProfilingConfig` for a monitor that both refreshes automatically and sends failure alerts. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Related Concepts

- [Data Profiling on Databricks](/concepts/data-profiling-in-databricks.md) — Overview of creating and managing profiles.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — Broader framework for monitoring data quality.
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog system where profiled tables are registered.
- Cron Expressions — Standard syntax for scheduling tasks.

### Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
