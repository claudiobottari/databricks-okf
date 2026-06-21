---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58021b7765b1c82f0d96866fce3c5b2412a56242d1c8701fd536203982dd7a0b
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-limitations
    - DPL
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Data Profiling Limitations
description: Constraints for Databricks data profiling including supported table types (only Delta tables), regional availability, 30-day time window for time series/inference profiles, and 4TB maximum for snapshot profiles.
tags:
  - data-quality
  - databricks
  - limitations
timestamp: "2026-06-19T14:42:56.047Z"
---

# Data Profiling Limitations

**Data Profiling Limitations** describes the constraints and restrictions that apply when using Databricks data profiling to compute summary statistics and drift metrics for tables.

## Overview

Data profiling provides summary statistics for a table, computing profiling metrics over time to track data quality and model performance. However, several limitations affect the tables, analysis modes, and regions that can be used. ^[data-profiling-databricks-on-aws.md]

## Supported Table Types

Only [Delta tables](/concepts/delta-lake-table.md) are supported for profiling. The table must be one of the following types: managed tables, external tables, views, materialized views, or streaming tables. ^[data-profiling-databricks-on-aws.md]

## Materialized Views and Incremental Processing

Profiles created over [materialized views](/concepts/materialized-views-in-databricks.md) do not support incremental processing. This means that each profile refresh must recompute metrics from the full view rather than applying only the changes since the last run. ^[data-profiling-databricks-on-aws.md]

## Regional Availability

Data profiling is not available in all regions. For regional support, see the column **Data profiling** in the table [AI and machine learning features availability](https://docs.databricks.com/aws/en/resources/feature-region-support#ai-aws). ^[data-profiling-databricks-on-aws.md]

## Time Series and Inference Profile Time Window

Profiles created using the time series or inference analysis modes only compute metrics over the most recent 30 days. If you need to adjust this window, you must contact your Databricks account team. ^[data-profiling-databricks-on-aws.md]

## Snapshot Profile Table Size

The maximum table size for a [Snapshot Profile](/concepts/snapshot-profile.md) is 4 TB. For tables larger than 4 TB, use a time series profile instead. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- [Delta Tables](/concepts/delta-lake-table.md)
- [Materialized Views](/concepts/materialized-views-in-databricks.md)
- Incremental Processing
- [Snapshot Profile](/concepts/snapshot-profile.md)
- [Time Series Profile](/concepts/time-series-profile.md)
- [Inference Profile](/concepts/inference-profile.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
