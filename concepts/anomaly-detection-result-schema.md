---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36d7f9df70bfc9550c21b111fe244b0d9c4f219fbc3732774156a16f77a25b2e
  pageDirectory: concepts
  sources:
    - review-anomaly-detection-logged-results-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection-result-schema
    - ADRS
    - Anomaly Detection Results
    - Anomaly Detection Results Table
    - Anomaly detection results
    - Anomaly detection results table
    - Anomaly detection result table
    - review anomaly detection logged results|anomaly detection result table schema
  citations:
    - file: review-anomaly-detection-logged-results-databricks-on-aws.md
title: Anomaly Detection Result Schema
description: Schema of the anomaly detection results table, with rows representing scanned tables and columns including commit_freshness, total_row_count, daily_row_count, upstream_jobs, and downstream_impact.
tags:
  - databricks
  - data-quality
  - schema
timestamp: "2026-06-19T20:15:05.803Z"
---

# Anomaly Detection Result Schema

The **Anomaly Detection Result Schema** defines the structure of the `system.data_quality_monitoring.table_results` table, which stores the output of data quality monitoring scans in [Unity Catalog](/concepts/unity-catalog.md). Each row in the results table corresponds to a single table that was scanned during a monitoring run. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Access and Permissions

By default, the results table is accessible only to account admins. These admins must grant access to other users as needed. The table contains all results across the entire [Metastore](/concepts/metastore.md), including sample values from tables in each catalog, so it should be shared only with users authorized to view metastore-wide data quality monitoring results. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Storage and Billing

Anomaly detection results use [default storage](/concepts/workspace-default-storage-path.md) and are not billed separately for storage. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Schema Overview

The results table contains multiple columns, each storing structured data about the monitoring scan. Key columns and their structures are described below.

### `commit_freshness` Array Structure

The `commit_freshness` column is a `struct` that captures information about data freshness. Its structure includes fields for tracking when data was last committed and monitoring freshness metrics. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### `total_row_count` and `daily_row_count` Array Structure

Both `total_row_count` and `daily_row_count` columns are `struct` types that store row count information. These contain metrics for tracking changes in data volume over time. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### `upstream_jobs` Array Structure

The `upstream_jobs` column contains an array of structs, each describing an upstream job that feeds data into the monitored table. The structure captures job execution and dependency information. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### `downstream_impact` Structure

The `downstream_impact` column is a `struct` that contains information about how anomalies in the monitored table affect downstream consumers. This enables impact analysis when data quality issues are detected. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The framework that generates these results
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer in which monitoring runs
- [Anomaly Detection](/concepts/anomaly-detection.md) — The detection algorithms that produce these results
- [Data Profiling](/concepts/data-profiling.md) — The statistical analysis that feeds anomaly detection
- System Tables — The broader category of system-owned metadata tables

## Sources

- review-anomaly-detection-logged-results-databricks-on-aws.md

# Citations

1. [review-anomaly-detection-logged-results-databricks-on-aws.md](/references/review-anomaly-detection-logged-results-databricks-on-aws-533e3349.md)
