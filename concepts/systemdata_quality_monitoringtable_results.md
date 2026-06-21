---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b90f555f7ec53e474d11f84f2fdb2503e5449485fd6c92fedda8598ec0a2ec6
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
    - review-anomaly-detection-logged-results-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - systemdata_quality_monitoringtable_results
    - System Tables for Data Quality Monitoring
  citations:
    - file: review-anomaly-detection-logged-results-databricks-on-aws.md
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: system.data_quality_monitoring.table_results
description: A system table in Databricks that stores anomaly detection output results, including event time, table status, freshness metrics, completeness metrics, and downstream impact information.
tags:
  - system-tables
  - data-quality
  - monitoring
  - databricks
timestamp: "2026-06-19T17:32:10.123Z"
---

# system.data_quality_monitoring.table_results

**`system.data_quality_monitoring.table_results`** is a Databricks system table in Unity Catalog that stores all anomaly detection and data quality monitoring scan results across an entire [Metastore](/concepts/metastore.md). It serves as the primary output location for data quality monitoring scans and powers alerts and downstream analysis. ^[review-anomaly-detection-logged-results-databricks-on-aws.md, alerts-for-anomaly-detection-databricks-on-aws.md]

## Purpose

Data quality monitoring automatically logs scan results to this table. Each row corresponds to a single monitored table in the [Metastore](/concepts/metastore.md), containing metrics about freshness, completeness, row counts, upstream job dependencies, and downstream impact. The table uses default storage and is not billed separately from the storage costs. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Access control

By default, only account admins can access `system.data_quality_monitoring.table_results`. They must grant explicit access to other users or service principals as needed. Because the table contains sample values from tables in every catalog, it should be shared only with users authorized to view metastore-wide quality results. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Schema overview

The table includes the following key columns and structures:

| Column name | Type | Description |
|-------------|------|-------------|
| `catalog_name`, `schema_name`, `table_name` | string | Identifies the observed table. |
| `status` | string | Health status (e.g., `'Unhealthy'`). |
| `commit_freshness` | struct | Freshness metrics including expected and actual commit times. |
| `daily_row_count` | struct | Completeness metrics including predicted versus actual daily row counts. |
| `total_row_count` | struct | Total row count metrics. |
| `upstream_jobs` | array | Upstream job dependencies for the table. |
| `downstream_impact` | struct | Impact information, including `num_queries_on_affected_tables`. |

Detailed schema descriptions for each struct and array column are available in the Databricks documentation. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Usage in alerts

The table is a core data source for configuring Alerts for anomaly detection using Databricks SQL. A standard alert query uses `system.data_quality_monitoring.table_results` to find tables whose `status` is `'Unhealthy'` within the last six hours, with a configurable minimum number of affected queries (`impacted_queries`). ^[alerts-for-anomaly-detection-databricks-on-aws.md]

Alert queries typically aggregate data by hour and table, selecting metrics such as:

- `commit_expected` and `commit_actual` (freshness)
- `completeness_expected` and `completeness_actual` (row volume)
- `impacted_queries` (downstream impact)

Custom email templates can include these metrics to notify recipients of specific quality failures. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

> **Note:** For legacy beta jobs, alert configurations should replace `system.data_quality_monitoring.table_results` with `<catalog>.<schema>._quality_monitoring_summary`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related concepts

- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- Unity Catalog system tables
- Alerts for anomaly detection
- Review anomaly detection logged results

## Sources

- review-anomaly-detection-logged-results-databricks-on-aws.md
- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [review-anomaly-detection-logged-results-databricks-on-aws.md](/references/review-anomaly-detection-logged-results-databricks-on-aws-533e3349.md)
2. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
