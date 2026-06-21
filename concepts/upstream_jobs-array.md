---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e46c336f6e59f151fa192684c966fd065511e7aab3db81d8f0b3538242c7c1f
  pageDirectory: concepts
  sources:
    - review-anomaly-detection-logged-results-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - upstream_jobs-array
    - upstream jobs
    - upstream_jobs Array Structure
  citations:
    - file: review-anomaly-detection-logged-results-databricks-on-aws.md
title: upstream_jobs Array
description: An array column in the anomaly detection results table that records information about upstream jobs feeding each scanned table.
tags:
  - databricks
  - data-quality
  - lineage
timestamp: "2026-06-19T20:15:43.968Z"
---

# upstream_jobs Array

The `upstream_jobs` array is a column in the anomaly detection result table (stored in `system.data_quality_monitoring.table_results`). This column stores information about upstream jobs that process data for the table being monitored, providing insight into the data pipeline's source dependencies. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Structure

The `upstream_jobs` column is an array of structs. Each struct in the array contains information about a single upstream job that processes data for the monitored table. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

The exact schema of each struct within the array includes the following fields:

### `job_name`[​](#job_name "Direct link to job_name")

The **`job_name`** field is a string that contains the name of the upstream job. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### `run_id`[​](#run_id "Direct link to run_id")

The **`run_id`** field is a string that contains the identifier for a specific run of the upstream job. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### `run_name`[​](#run_name "Direct link to run_name")

The **`run_name`** field is a string that contains a human-readable name for the specific job run. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### `run_start_time`[​](#run_start_time "Direct link to run_start_time")

The **`run_start_time`** field is a timestamp (in milliseconds since Unix epoch) indicating when the upstream job run started. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### `run_end_time`[​](#run_end_time "Direct link to run_end_end_time")

The **`run_end_time`** field is a timestamp (in milliseconds since Unix epoch) indicating when the upstream job run ended. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

## Usage

You can use the `upstream_jobs` array to identify which upstream_jobs Array|upstream jobs processed data for a monitored table. This is useful for [Data Lineage](/concepts/data-lineage.md) tracking and [Data Quality Monitoring](/concepts/data-quality-monitoring.md).

This column appears in the results table for monitoring scans with the `anomaly_detection` profile type.

## Related Concepts

- [Anomaly detection result table](/concepts/anomaly-detection-result-schema.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Data Lineage](/concepts/data-lineage.md)
- Upstream jobs
- downstream_impact Struct|Downstream impact
- commit_freshness Struct|Commit freshness
- Total row count
- Daily row count

# Citations

1. [review-anomaly-detection-logged-results-databricks-on-aws.md](/references/review-anomaly-detection-logged-results-databricks-on-aws-533e3349.md)
