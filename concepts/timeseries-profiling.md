---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a51b420b5f70d9a53b659f43b81ec81a1f27ee3b35ec1418e522b26d61c3cc8
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - timeseries-profiling
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: TimeSeries Profiling
description: A data profiling type that partitions data into time-based windows using a timestamp column and metric granularities for trend analysis.
tags:
  - data-profiling
  - time-series
  - unity-catalog
timestamp: "2026-06-19T09:28:30.694Z"
---

# TimeSeries Profiling

**TimeSeries Profiling** is a data profiling mode in Databricks that analyzes how key statistics and metrics of a table evolve over time. Unlike static profiling, which produces a single snapshot, TimeSeries profiling partitions the data into time windows and computes metrics per window, enabling trend analysis, anomaly detection, and monitoring of data quality across time.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Overview

TimeSeries profiling is configured through the **Quality** tab of a table in Catalog Explorer. It is one of three profile types available: the other two are standard profiling and [Inference profiling](/concepts/inference-profile.md). When you select TimeSeries, you must provide additional parameters that define how data is grouped into time windows and which column contains the timestamp.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Configuring a TimeSeries Profile

To create a TimeSeries profile from the Databricks UI, follow the steps in Create a profile using the Databricks UI. After clicking **Configure** in the **Data Quality Monitoring** dialog, select **TimeSeries** from the **Profile type** drop-down. You must then specify:^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- **Metric granularities** – The granularity (e.g., hour, day, week) that determines how data is partitioned into time windows for metric computation.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Timestamp column** – The column in the table that contains the timestamp for each record. The column must have a data type of `TIMESTAMP` or a type convertible to timestamps using the PySpark `to_timestamp` function.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

Once configured, Databricks profiles the data, storing metric tables and optionally generating a dashboard. You can also set a schedule, notifications, custom metrics, and slicing expressions through the advanced options. See the general profiling documentation for details on these settings.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

> **Note**: When you first create a TimeSeries (or Inference) profile, the profile analyzes only data from the 30 days prior to its creation. After the profile is created, all new data is processed incrementally. Monitors defined on materialized views do **not** support incremental processing.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Best Practices

- **Enable change data feed (CDF)** on the table. When CDF is enabled, only newly appended data is processed on each refresh, rather than re‑scanning the entire table. This improves performance and reduces cost, especially when profiling many tables at scale.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- Choose a metric granularity that aligns with your monitoring frequency and data arrival rate. For example, use **hourly** if data arrives constantly and you need near‑real‑time insight; use **daily** for batch‑processed tables.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- Ensure the timestamp column has a proper `TIMESTAMP` type or is explicitly cast to avoid conversion failures.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The general concept of analyzing table statistics.
- [Inference Profile](/concepts/inference-profile.md) – A profile type for model inference data, similar to TimeSeries but with additional fields for predictions and labels.
- [Anomaly Detection](/concepts/anomaly-detection.md) – A related feature that can be enabled alongside profiling to alert on statistical outliers in metric trends.
- Metric Granularities – How time windows are defined in TimeSeries profiling.
- [Metric Tables](/concepts/profile-metric-tables.md) – The output tables that store profiled statistics over time.

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
