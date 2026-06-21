---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb5dc22dc053706d2cc19c76b334b1b89cb32e86f4cd9dd2d12cd55e96ee5272
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - percent-null
    - percent-null-completeness-check
    - PNCC
    - NCC
    - percent-null-completeness
    - PN(
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Percent Null
description: A supplementary data quality metric that tracks the expected percentage of null values per column over the last 24 hours, flagging incompleteness when observed nulls exceed predicted bounds.
tags:
  - data-quality
  - completeness
  - null-values
timestamp: "2026-06-19T17:33:26.634Z"
---

---

title: Percent Null
summary: A data quality metric that tracks the percentage of rows with null values in a column over a 24-hour window, used to assess completeness.
sources:
  - anomaly-detection-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:00:00.000Z"
updatedAt: "2026-06-19T15:00:00.000Z"
tags:
  - databricks
  - data-quality
  - anomaly-detection
  - completeness
aliases:
  - percent-null
  - null-percentage
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Percent Null

**Percent Null** is a data quality metric used in Databricks [Anomaly Detection](/concepts/anomaly-detection.md) to evaluate the completeness of a table at the column level. It measures the percentage of rows written to the table in the last 24 hours that are expected to have null values for a given column. ^[anomaly-detection-databricks-on-aws.md]

## How it works

Databricks data quality monitoring analyzes the historical trend of the null percentage for each column. Based on this history, it predicts a range of expected null percentages. If the actual percent null for a column over the last 24 hours is higher than the upper bound of this predicted range, the table is marked as **incomplete**. ^[anomaly-detection-databricks-on-aws.md]

Percent null is an additional quality detail layered on top of the base [completeness](/concepts/completeness-data-quality.md) check. While the base completeness check examines overall row counts, percent null provides column-specific insight into data quality. ^[anomaly-detection-databricks-on-aws.md]

## Relationship to completeness

The primary [completeness](/concepts/completeness-data-quality.md) evaluation does not take into account metrics such as the fraction of nulls. Percent null fills this gap by focusing specifically on unexpected null values. When the percentage of null rows in a column exceeds the expected upper bound, it triggers an incompleteness flag, alerting data consumers to potential data quality issues. ^[anomaly-detection-databricks-on-aws.md]

## Limitations

The percent null check applies only to columns that are monitored. It does not apply to views or foreign tables, which are not supported by anomaly detection. Additionally, the analysis relies on historical patterns, so tables with insufficient history may produce less accurate predictions. ^[anomaly-detection-databricks-on-aws.md]

## Related concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The overall feature that monitors data quality across a schema.
- [Completeness (data quality)](/concepts/completeness-data-quality.md) – The broader metric that percent null supplements.
- [Freshness (data quality)](/concepts/freshness-data-quality.md) – The other main quality dimension monitored by anomaly detection.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The set of tools and processes that include percent null checks.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance platform on which anomaly detection is built.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
