---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6647fb0188d4d09c354c76db4f4f50b45815297655caecb808b8edfe0543131b
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sdk-data-profiling-api
    - DSDPA
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Databricks SDK Data Profiling API
description: The Python SDK and REST API for creating, refreshing, viewing, and deleting data profiles on Unity Catalog tables, including support for scheduling and notifications.
tags:
  - api
  - python-sdk
  - databricks
  - automation
timestamp: "2026-06-18T14:47:00.474Z"
---

# Databricks SDK Data Profiling API

The **Databricks SDK Data Profiling API** allows users to create, manage, and refresh data profiles on Delta tables registered in [Unity Catalog](/concepts/unity-catalog.md). A data profile captures statistics about table data over time — such as row counts, null ratios, distribution shapes, and — for inference tables — model quality metrics. The API is exposed through the `databricks-sdk` Python package and the underlying REST API. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Only a single profile can be created per table in a given Unity Catalog [Metastore](/concepts/metastore.md). Profiles can be applied to both managed tables and external Delta tables in Unity Catalog. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Requirements

The most recent version of the API requires `databricks-sdk>=0.68.0`. Authentication follows the standard SDK authentication flow. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Profile Types

Three profile types are available: `TimeSeries`, `InferenceLog`, and `Snapshot`. The type determines what metrics are computed and how data is segmented over time.

### `TimeSeries` profile

A `TimeSeries` profile compares data distributions across time windows. It requires a timestamp column (of type `TIMESTAMP` or convertible via `to_timestamp`) and one or more aggregation granularities. Available granularities range from 5 minutes to 1 year (e.g., `AGGREGATION_GRANULARITY_1_DAY`). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Optional `slicing_exprs` can be added to further segment the data (e.g., `"type='Red'"`). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### `InferenceLog` profile

An `InferenceLog` profile extends the TimeSeries profile with model quality metrics. It requires:
- `prediction_column` – column containing predictions.
- `model_id_column` – column identifying the model version.
- `label_column` – (optional) ground truth labels.
- `timestamp_column`
- `granularities`
- `problem_type` – e.g., `INFERENCE_PROBLEM_TYPE_CLASSIFICATION`.

Slices are automatically created based on distinct values of the model ID column. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### `Snapshot` profile

A `Snapshot` profile computes metrics over the entire table at each refresh point, reflecting the full table state. The maximum table size for a snapshot profile is **4 TB**; for larger tables, use `TimeSeries` profiles. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Refresh and View Results

To populate or update metric tables, use `create_refresh`. The refresh runs on serverless compute, not on the notebook cluster, allowing the notebook to continue running while statistics are computed. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

- `list_refreshes` returns the refresh history.
- `get_refresh` returns the status of a specific refresh (states include `PENDING`, `RUNNING`, `MONITOR_REFRESH_STATE_PENDING`, `MONITOR_REFRESH_STATE_RUNNING`).

Metric tables are Unity Catalog tables and can be queried via notebooks, SQL query explorer, or Catalog Explorer. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## View Profile Settings

Use `get_monitor` to review the current configuration of a profile, including its type, granularities, slicing expressions, schedule, and notification settings. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Schedule

A profile can be set to refresh on a recurring schedule by providing a `CronSchedule` object in the `schedule` parameter of `create_monitor`. The schedule is defined by a quartz cron expression and a timezone ID (e.g., `"0 0 12 * * ?"` at `"PST"` for daily at noon). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Notifications

Notifications can be configured using the `notification_settings` parameter. Currently, `on_failure` notifications can be sent to up to 5 email addresses when a refresh fails or times out. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Access Control

The metric tables and dashboard created by a profile are owned by the user who created the profile. Access to metric tables can be managed via Unity Catalog privileges. Dashboards can be shared within the workspace using the **Share** button. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Deleting a Profile

Call `delete_monitor` to remove a profile. This does **not** delete the metric tables or dashboard; those assets must be deleted separately or stored in a different location. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Example Notebooks

The provided source includes four example notebooks illustrating creation and usage for each profile type (TimeSeries, InferenceLog regression, InferenceLog classification, and Snapshot). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
