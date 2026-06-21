---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc51a7a9a1c97e11178804f908211b72ab6848068a50522ceec7e6d9f627450c
  pageDirectory: concepts
  sources:
    - review-anomaly-detection-logged-results-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - commit_freshness-struct
    - Commit freshness
  citations:
    - file: review-anomaly-detection-logged-results-databricks-on-aws.md
title: commit_freshness Struct
description: A struct in the anomaly detection results table that captures data freshness metrics for each scanned table.
tags:
  - databricks
  - data-quality
  - metrics
timestamp: "2026-06-19T20:15:10.220Z"
---

# commit_freshness Struct

The **`commit_freshness` Struct** is a component of the anomaly detection results schema in Databricks data quality monitoring. It is stored within the `system.data_quality_monitoring.table_results` table, which contains all data quality monitoring scan results across the entire [Metastore](/concepts/metastore.md). ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Schema Structure

The `commit_freshness` struct is an array structure within the anomaly detection result table. Each row in the results table corresponds to a single table in the schema that was scanned, and the `commit_freshness` field provides information about how recently data has been committed to that table. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection Results Table](/concepts/anomaly-detection-result-schema.md) — The system table (`system.data_quality_monitoring.table_results`) that stores all data quality monitoring scan results.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for monitoring data quality in Unity Catalog.
- total_row_count and daily_row_count Structs|total_row_count and daily_row_count Struct — Related array structures in the same results table schema.
- upstream_jobs Array|upstream_jobs Array Structure — Another array structure in the results table schema.
- downstream_impact Struct — A struct column in the results table containing downstream impact information.
- [Default Storage](/concepts/workspace-default-storage-path.md) — The storage mechanism used to store anomaly detection results.

## Sources

- review-anomaly-detection-logged-results-databricks-on-aws.md

# Citations

1. [review-anomaly-detection-logged-results-databricks-on-aws.md](/references/review-anomaly-detection-logged-results-databricks-on-aws-533e3349.md)
