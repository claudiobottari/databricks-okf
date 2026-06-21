---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f088a81844df0cdd3dc6c92ca209b61547ad2caa7ad0b54b70e457e3157ed711
  pageDirectory: concepts
  sources:
    - review-anomaly-detection-logged-results-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - total_row_count-and-daily_row_count-structs
    - daily_row_count Structs and total_row_count
    - TADS
    - total_row_count and daily_row_count Struct
  citations:
    - file: review-anomaly-detection-logged-results-databricks-on-aws.md
title: total_row_count and daily_row_count Structs
description: Structs in the anomaly detection results table that track overall and daily row count metrics per table.
tags:
  - databricks
  - data-quality
  - metrics
timestamp: "2026-06-19T20:15:12.680Z"
---

---

## `total_row_count` and `daily_row_count` Structs

The `total_row_count` and `daily_row_count` structs are columns in the [review anomaly detection logged results|anomaly detection result table schema](/concepts/anomaly-detection-result-schema.md) (stored in the `system.data_quality_monitoring.table_results` table). They contain row‑count statistics computed during data quality monitoring scans.

- **`total_row_count`** – A struct that stores the overall row count for the monitored table.
- **`daily_row_count`** – A struct that stores the row count broken down by day.

The exact fields within each struct are described in the source documentation under the heading "`total_row_count` and `daily_row_count` array structure". ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### Related Concepts

- Anomaly detection results table
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [default storage for anomaly detection](/concepts/databricks-anomaly-detection.md)

### Sources

- review-anomaly-detection-logged-results-databricks-on-aws.md

# Citations

1. [review-anomaly-detection-logged-results-databricks-on-aws.md](/references/review-anomaly-detection-logged-results-databricks-on-aws-533e3349.md)
