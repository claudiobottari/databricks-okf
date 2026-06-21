---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b36b9fc9e12b4c8bf428aa569aa3e1581310cebff8c70533b50001aeadfd36b5
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-cdf-for-efficient-profiling
    - CDF(FEP
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Change Data Feed (CDF) for Efficient Profiling
description: Best practice to enable change data feed on tables to process only newly appended data during TimeSeries and Inference profile refreshes instead of re-processing the entire table.
tags:
  - databricks
  - change-data-feed
  - optimization
  - data-profiling
  - performance
timestamp: "2026-06-19T09:27:53.869Z"
---

# Change Data Feed (CDF) for Efficient Profiling

**Change Data Feed (CDF) for Efficient Profiling** refers to the practice of enabling Delta Lake’s Change Data Feed on a table that is being profiled by [Databricks Data Profiling](/concepts/databricks-data-profiling.md) (the monitoring service for Unity Catalog tables). When CDF is enabled for a `TimeSeries` or `InferenceLog` profile, the profiling engine processes only newly appended data during each refresh cycle instead of scanning the entire table, leading to more efficient execution and lower costs as the number of profiled tables grows. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## How CDF Enhances Profiling Efficiency

By default, without CDF, a profile refresh would re-process all rows in the table to compute distribution metrics, trends, and model quality statistics. When CDF is turned on, [Delta Lake](/concepts/delta-lake.md) records row-level changes (inserts, updates, deletes) in a separate change log. The profiling engine can then read only the delta since the last refresh — specifically, the newly appended data — rather than performing a full table scan. This reduces the amount of data read and processed each cycle, making refreshes faster and more resource-efficient. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Applicable Profile Types

The recommendation to enable CDF applies specifically to **TimeSeries** and **InferenceLog** profiles, which compute metrics over sliding time windows and rely on incremental data to track changes in distributions or model performance. The source material explicitly states that for these profile types, enabling CDF is a best practice. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

CDF is **not mentioned** as a requirement or best practice for **Snapshot** profiles, which analyze the full content of a table as it changes over time. Snapshot profiles inherently process all data on each refresh and do not benefit from incremental processing via CDF in the same way. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Additionally, profiles defined on materialized views do not support incremental processing at all, regardless of CDF status. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Best Practices

- Enable CDF on any Delta table that will be profiled with a `TimeSeries` or `InferenceLog` profile. This is listed as a best practice in the Databricks documentation. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- Confirm that CDF is turned on before creating the profile. CDF can be enabled on a table using `ALTER TABLE ... SET TBLPROPERTIES (delta.enableChangeDataFeed = true)`.
- When scaling data profiling across many tables, using CDF helps contain compute costs and refresh latency because each table’s profiling run only touches the newly arrived data. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) – The underlying Delta Lake feature that tracks row-level changes.
- [TimeSeries Profile](/concepts/timeseries-profile.md) – A profiling type that benefits from CDF for incremental computation.
- [InferenceLog Profile](/concepts/inferencelog-profile.md) – A profiling type that also benefits from CDF.
- [Snapshot Profile](/concepts/snapshot-profile.md) – A profiling type that does not use incremental processing.
- [Data Profiling Metrics Tables](/concepts/databricks-data-profiling-metric-tables.md) – The output tables created by a profile refresh.
- Databricks SDK for Data Quality – The API used to create and manage profiles.

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
