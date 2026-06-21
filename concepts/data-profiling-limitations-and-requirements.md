---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a2f27cc4351a673536779d8f107fce423d3a15027a8aab7518e79797e19aa9a
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-limitations-and-requirements
    - Requirements and Data Profiling Limitations
    - DPLAR
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Data Profiling Limitations and Requirements
description: Constraints for Databricks data profiling including Unity Catalog enablement, supported table types (Delta only), regional availability, and size limits for snapshot profiles.
tags:
  - databricks
  - data-quality
  - requirements
timestamp: "2026-06-19T18:07:29.941Z"
---

# Data Profiling Limitations and Requirements

**Data profiling** on Databricks provides summary statistics for tables, enabling monitoring of data quality and ML model performance over time. However, it has specific requirements and limitations that users must understand before implementation.

## Requirements

### Unity Catalog and SQL Access

Your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md), and you must have access to Databricks SQL. ^[data-profiling-databricks-on-aws.md]

### Required Privileges

To enable data profiling, you need the following privileges on the catalog, schema, or table:

- `USE CATALOG` on the catalog and `USE SCHEMA` on the schema containing the table
- `SELECT` on the table
- `MANAGE` on the catalog, schema, or table

^[data-profiling-databricks-on-aws.md]

### Supported Table Types

Only [Delta Tables](/concepts/delta-lake-table.md) are supported for profiling. The table must be one of the following types:

- Managed tables
- External tables
- Views
- Materialized views
- Streaming tables

^[data-profiling-databricks-on-aws.md]

### Baseline Table Requirements

When using a baseline table for drift measurement, it must match the schema of the profiled table. The exception is the timestamp column for tables used with time series or inference profiles. If columns are missing in either the primary table or the baseline table, profiling uses best-effort heuristics to compute the output metrics. ^[data-profiling-databricks-on-aws.md]

For inference profiles, a good baseline is the data used to train or validate the model being profiled. This table should contain the same feature columns as the primary table, and additionally should have the same `model_id_col` that was specified for the primary table's InferenceLog. ^[data-profiling-databricks-on-aws.md]

### Compute Requirements

Data profiling uses serverless compute for jobs but does not require that your account be enabled for Serverless Compute. ^[data-profiling-databricks-on-aws.md]

## Limitations

### Supported Table Types

Only Delta tables are supported for profiling. ^[data-profiling-databricks-on-aws.md]

### Materialized View Processing

Profiles created over materialized views do not support incremental processing. ^[data-profiling-databricks-on-aws.md]

### Regional Availability

Not all regions are supported for data profiling. For regional support, refer to the **Data profiling** column in Databricks' AI and machine learning features availability documentation. ^[data-profiling-databricks-on-aws.md]

### Time Series and Inference Profile Time Limits

Profiles created using the **time series** or **inference analysis** modes only compute metrics over the last 30 days. If you need to adjust this limit, contact your Databricks account team. ^[data-profiling-databricks-on-aws.md]

### Snapshot Profile Size Limit

The maximum table size for a [Snapshot Profile](/concepts/snapshot-profile.md) is 4TB. For larger tables, use time series profiles instead. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Profile Metrics Table](/concepts/profile-metrics-table.md) — Stores summary statistics for each column, time window, and slice
- [Drift Metrics Table](/concepts/drift-metrics-table.md) — Stores statistics tracking distribution changes over time
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) — The default time boundary applied during time series and inference profiling
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — Overview of monitoring data quality on Databricks
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) — Profiling for ML model monitoring

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
