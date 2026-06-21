---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 884ba906d8b0296a9d72778a005290cba56db92d05ec7082434d95c707403666
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profiling-granularity-options
    - PGO
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Profiling Granularity Options
description: The set of predefined aggregation granularities (from 5 minutes to 1 year) available for time-based profiles in Databricks data profiling.
tags:
  - databricks
  - granularity
  - time-series
  - data-profiling
  - configuration
timestamp: "2026-06-19T09:27:43.308Z"
---

# Profiling Granularity Options

**Profiling Granularity Options** refer to the set of time-window sizes available when creating a [TimeSeries Profile](/concepts/timeseries-profile.md) or an [InferenceLog Profile](/concepts/inferencelog-profile.md) in Databricks data profiling. These granularities determine the intervals over which aggregate statistics and model quality metrics are calculated.

## Overview

When configuring a data profile using the API, you must specify one or more granularities for `TimeSeries` and `InferenceLog` profiles. Each granularity defines a time bucket (e.g., 1 hour, 1 day) that the profiling engine uses to compute per-window statistics. After the profile is created, these statistics are refreshed incrementally — only newly appended data is processed if [change data feed (CDF)](/concepts/delta-change-data-feed-cdf.md) is enabled on the table. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Available Granularities

The following granularity values are supported. They are specified via the `ganularities` parameter of the API call.

| Constant | Time Window |
| -------- | ----------- |
| `AGGREGATION_GRANULARITY_5_MINUTES` | 5 minutes |
| `AGGREGATION_GRANULARITY_30_MINUTES` | 30 minutes |
| `AGGREGATION_GRANULARITY_1_HOUR` | 1 hour |
| `AGGREGATION_GRANULARITY_1_DAY` | 1 day |
| `AGGREGATION_GRANULARITY_1_WEEK` | 1 week |
| `AGGREGATION_GRANULARITY_2_WEEKS` | 2 weeks |
| `AGGREGATION_GRANULARITY_3_WEEKS` | 3 weeks |
| `AGGREGATION_GRANULARITY_4_WEEKS` | 4 weeks |
| `AGGREGATION_GRANULARITY_1_MONTH` | 1 month |
| `AGGREGATION_GRANULARITY_1_YEAR` | 1 year |

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

These granularities are used by both `TimeSeries` and `InferenceLog` profiles. The set must be provided as a list when creating the profile. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### TimeSeries Profile Example

A `TimeSeries` profile compares data distributions across each time window defined by the chosen granularities. In the API example, `granularities=[AggregationGranularity.AGGREGATION_GRANULARITY_1_DAY]` is used to calculate daily statistics. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### InferenceLog Profile Example

An `InferenceLog` profile also accepts granularities and additionally includes model quality metrics. It uses the same granularity constants in the `granularities` parameter. For example, `granularities=[AggregationGranularity.AGGREGATION_GRANULARITY_1_DAY]` creates daily model quality reports. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Important Notes

- **Initial data range**: When you first create a time series or inference profile, Databricks analyzes only data from the 30 days prior to its creation. After creation, all new data is processed at the specified granularity. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- **Snapshot profiles** do not use granularities; they profile the full table contents over time and are limited to 4 TB. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The overall monitoring framework.
- [TimeSeries Profile](/concepts/timeseries-profile.md) — Profile type that uses granularities for time-window comparisons.
- [InferenceLog Profile](/concepts/inferencelog-profile.md) — Profile type that includes model quality metrics with granularities.
- [Snapshot Profile](/concepts/snapshot-profile.md) — Profile type that does not use granularities.

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
