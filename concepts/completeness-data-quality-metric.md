---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c18916f2e52a313a6b29044400cb30c7c94d0475f586c1585b692a665d933221
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - completeness-data-quality-metric
    - C(QM
    - Completeness Metric
    - Completeness Metrics
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Completeness (data quality metric)
description: A metric measuring expected row counts in the last 24 hours, with anomalous low counts flagging a table as incomplete, and optionally augmented by percent-null analysis per column.
tags:
  - data-quality
  - monitoring
  - completeness
timestamp: "2026-06-19T17:33:05.783Z"
---

---

title: Completeness (Data Quality Metric)
summary: A metric measuring expected row counts over the last 24 hours; if actual rows fall below the predicted lower bound, the table is marked incomplete. Optionally includes a percent-null check per column.
sources:
  - anomaly-detection-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:45:32.462Z"
updatedAt: "2026-06-18T10:45:32.462Z"
tags:
  - data-quality
  - monitoring
  - metrics
aliases:
  - completeness-data-quality-metric
  - C(QM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0

---

# Completeness (Data Quality Metric)

**Completeness** is a data quality metric that measures whether a table has received the expected number of rows within a given time window. In Databricks data quality monitoring, completeness specifically refers to the number of rows expected to be written to a table in the last 24 hours.^[anomaly-detection-databricks-on-aws.md]

## How Completeness is Evaluated

Data quality monitoring analyzes the historical row count of a table and, based on this data, predicts a range of expected row counts. If the number of rows committed over the last 24 hours falls below the lower bound of this predicted range, the table is marked as **incomplete**.^[anomaly-detection-databricks-on-aws.md]

Completeness evaluation is part of the [Anomaly Detection](/concepts/anomaly-detection.md) system, which operates as a background job that monitors tables across a schema. The system builds per-table models based on historical patterns to determine expected values.^[anomaly-detection-databricks-on-aws.md]

### Percent Null for Completeness

**Percent null** adds additional quality details to completeness. It measures the percentage of rows written to the table in the last 24 hours that are expected to have null values for a given column. Data quality monitoring analyzes the historical trend for each column and predicts a range. If the percent null for a column over the last 24 hours exceeds the upper bound of this range, the table is also marked as incomplete.^[anomaly-detection-databricks-on-aws.md]

## Comparison with Freshness

Completeness is evaluated alongside [Freshness (data quality metric)](/concepts/freshness-data-quality-metric.md), which tracks how recently a table has been updated. While freshness measures timeliness of updates, completeness measures whether the volume of data meets expectations. A table can be timely (fresh) but incomplete if fewer rows than expected arrive.^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The system that evaluates completeness and freshness
- [Freshness (data quality metric)](/concepts/freshness-data-quality-metric.md) — The companion metric measuring update timeliness
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for tracking data quality
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where anomaly detection operates

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
