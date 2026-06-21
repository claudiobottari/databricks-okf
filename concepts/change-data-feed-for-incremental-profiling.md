---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0eea3848d74202a98177497472df083f757403cb96f5028082957dad34092eb9
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-for-incremental-profiling
    - CDFFIP
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Change Data Feed for Incremental Profiling
description: A best practice to enable change data feed (CDF) on tables so profiling processes only newly appended data instead of re-processing the entire table on every refresh.
tags:
  - performance
  - incremental-processing
  - data-profiling
timestamp: "2026-06-19T17:56:29.900Z"
---

# Change Data Feed for Incremental Profiling

**Change Data Feed (CDF) for Incremental Profiling** is a mechanism that enables [Databricks Lakehouse Monitoring](/concepts/lakehouse-monitoring.md) to process only newly appended data during each profile refresh, instead of re-scanning the entire table. This optimization is available for [TimeSeries profiles](/concepts/timeseries-profile.md) and [Inference profiles](/concepts/inference-profile.md) and is strongly recommended to improve execution efficiency and reduce cost as profiling scales across many tables. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## How It Works

When you enable change data feed on a table, Databricks automatically tracks row-level changes (inserts, updates, deletes). The monitoring system reads only the incremental changes since the last profile run, applying the same profiling logic to the delta. This means that even if the underlying table grows to billions of rows, each refresh processes only a fraction of the data. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

The recommendation applies specifically when you create a profile using the **TimeSeries** or **Inference** profile type. These profile types are designed to analyze data partitioned by time windows, and incremental processing aligns naturally with their sliding-window refresh pattern. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

> **Note:** When you first create a time series or inference profile, the profile analyzes only data from the 30 days prior to its creation. After the profile is created, all new data is processed. This 30‑day lookback window is independent of the CDF incremental processing; CDF applies on subsequent refreshes once the baseline is established. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Benefits

- **Efficiency**: Only new data is processed per refresh, dramatically reducing compute time for large tables. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Cost reduction**: Because fewer resources are consumed per refresh, the total cost of maintaining multiple profiles across many tables is lowered. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Scalability**: Incremental processing makes it practical to run frequent (e.g., hourly) profiles even on tables with high data volumes. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Limitations

- Monitors defined on **materialized views** do not support incremental processing. If you use a materialized view as the source table, the profile will always re-scan the full view on each refresh. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- CDF must be enabled on the source table before creating the profile. You can enable it via `ALTER TABLE ... SET TBLPROPERTIES ('delta.enableChangeDataFeed' = true)` or in the Catalog Explorer UI. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Best Practices

- **Enable CDF before creating the profile.** If CDF is turned on after the profile is created, the next refresh may still re-process the full table because the system lacks a baseline. For best results, enable CDF at table creation time or before first profile configuration. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Use TimeSeries or Inference profiles** if your use case involves temporal data or model inference monitoring. These profiles are designed to take full advantage of CDF. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Avoid materialized views** as profile sources when incremental processing is desired. Use regular Delta tables with CDF enabled instead. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- [Data Profiling with Databricks Lakehouse Monitoring](/concepts/data-profiling.md)
- [TimeSeries Profile](/concepts/timeseries-profile.md)
- [Inference Profile](/concepts/inference-profile.md)
- [Databricks Lakehouse Monitoring](/concepts/lakehouse-monitoring.md)
- [Delta Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- Creating a Profile Using the Databricks UI

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
