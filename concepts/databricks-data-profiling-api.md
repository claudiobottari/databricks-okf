---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73cdc5a5de03477fe5490a056647b1b5bfe888eab4262d179a2dc74f8d6cc050
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profiling-api
    - DDP(
    - DDP
    - Create a Data Profile Monitor (API)
    - Create a Data Profile using the API
    - Create a data profile using the API
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Databricks Data Profiling (API)
description: Creating and managing data profiles on Unity Catalog tables using the Databricks SDK or REST API to monitor data quality and distribution over time.
tags:
  - databricks
  - data-quality
  - api
  - unity-catalog
timestamp: "2026-06-19T09:27:45.182Z"
---

# Databricks Data Profiling (API)

**Databricks Data Profiling (API)** refers to the programmatic interface for creating, managing, and monitoring data quality profiles on Delta tables registered in [Unity Catalog](/concepts/unity-catalog.md). Using the Databricks SDK (Python) or the REST API, you can define profiling configurations that track how data distributions and model quality metrics change over time. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Overview

Data profiling via the API enables automated monitoring of data quality on managed or external Delta tables. Only a single profile can exist per table in a Unity Catalog [Metastore](/concepts/metastore.md). The API supports three profile types: `TimeSeries`, `InferenceLog`, and `Snapshot`, each tailored to different monitoring needs. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Requirements

To use the most recent version of the API, install the Databricks Python SDK version 0.68.0 or later:

```python
%pip install "databricks-sdk>=0.68.0"
```

Authentication follows standard [Databricks SDK authentication](/concepts/databricks-sdk-authentication-methods.md) practices. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Profile Types

### TimeSeries Profile
A `TimeSeries` profile compares data distributions across time windows. Required parameters:
- A `timestamp_column` (must be `TIMESTAMP` type or convertible via `to_timestamp`).
- One or more `granularities` (e.g., `AGGREGATION_GRANULARITY_1_DAY`, `AGGREGATION_GRANULARITY_1_HOUR`).

Upon creation, Databricks analyzes only the 30 days prior to profile creation. All subsequent new data is processed incrementally. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### InferenceLog Profile
Similar to `TimeSeries`, but includes model quality metrics. Requires:
- `problem_type` (classification or regression).
- `prediction_column`, `model_id_column`, and optional `label_column`.
- Timestamp column and granularities.

Slices are automatically created based on distinct values of `model_id_column`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Snapshot Profile
A `Snapshot` profile captures the full table state at each refresh. The maximum table size is 4TB. For larger tables, use `TimeSeries` profiles instead. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Best Practices

- **Enable Change Data Feed (CDF)** on your table for `TimeSeries` and `Inference` profiles. CDF ensures only newly appended data is processed, reducing costs and improving efficiency. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- **Use `slicing_exprs`** to filter data (e.g., `slicing_exprs=["type='Red'"]`). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Refresh and View Results

Use `create_refresh` to update metric tables. This computation runs on [serverless compute](/concepts/serverless-gpu-compute.md), not on the cluster attached to the notebook. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
run_info = w.data_quality.create_refresh(
  object_type=table_object_type,
  object_id=table_id,
  refresh=Refresh(...)
)
```

To review profile settings, use `get_monitor`. To view refresh history, use `list_refreshes` and `get_refresh`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Scheduling

Profiles can run on a schedule using the `CronSchedule` parameter:

```python
schedule=CronSchedule(
    quartz_cron_expression="0 0 12 * * ?",
    timezone_id="PST"
)
```

## Notifications

Configure email notifications for failures using `NotificationSettings`:

```python
notification_settings=NotificationSettings(
    on_failure=NotificationDestination(
        email_addresses=["your_email@domain.com"]
    )
)
```

A maximum of 5 email addresses is supported per event type. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Access Control

Metric tables and dashboards are owned by the profile creator. Use Unity Catalog privileges for access control, and the **Share** button within the workspace to share dashboards. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Deletion

Deleting a profile via the API does **not** remove the metric tables or dashboard; these must be cleaned up separately. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Data Quality Monitoring on Databricks](/concepts/data-quality-monitoring-databricks.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Tables](/concepts/delta-lake-table.md)
- Serverless Compute
- [Metric Tables](/concepts/profile-metric-tables.md)

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
