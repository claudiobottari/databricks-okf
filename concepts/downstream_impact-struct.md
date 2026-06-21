---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b22c4d2bc96e99cfa7451a2b0355928e5031a53de88a5faaf286f5c81e5867da
  pageDirectory: concepts
  sources:
    - review-anomaly-detection-logged-results-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - downstream_impact-struct
    - Downstream Impact
    - Downstream impact
    - downstream_impact Struct
  citations:
    - file: review-anomaly-detection-logged-results-databricks-on-aws.md
title: downstream_impact Struct
description: A struct column in the anomaly detection results table that captures downstream impact information for each scanned table.
tags:
  - databricks
  - data-quality
  - lineage
timestamp: "2026-06-19T20:15:29.730Z"
---

# downstream_impact Struct

`downstream_impact` is a `struct` column in the `system.data_quality_monitoring.table_results` table that captures information about how data quality issues from a scanned table may affect downstream consumers. It is part of the anomaly detection logged results schema on Databricks. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Schema

The `downstream_impact` struct contains information about tables that depend on the scanned table, such as through data pipelines or data transformations. This can include details about affected tables, jobs, and other downstream consumers. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Context

The `downstream_impact` struct appears alongside other structs like `commit_freshness`, `total_row_count`, `daily_row_count`, and `upstream_jobs` in the anomaly detection results table. These columns together provide a comprehensive view of data quality for a given table. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Usage

Analysts and data engineers can inspect the `downstream_impact` column to understand the breadth of impact when a data quality issue is detected, helping them prioritize data remediation efforts and assess the blast radius of data issues. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Related Concepts

- Anomaly detection results
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- Upstream jobs
- commit_freshness Struct|Commit freshness
- Row count

## Sources

- review-anomaly-detection-logged-results-databricks-on-aws.md

# Citations

1. [review-anomaly-detection-logged-results-databricks-on-aws.md](/references/review-anomaly-detection-logged-results-databricks-on-aws-533e3349.md)
