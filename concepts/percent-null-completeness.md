---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e206f3a6bc33e3d92d2883514d3f464167965a483b24ef0a822faf1ab335d4af
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - percent-null-completeness
    - PN(
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Percent Null (Completeness)
description: An additional completeness sub-metric tracking the expected percentage of null values per column over 24 hours to detect anomalous null increases
tags:
  - data-quality
  - monitoring
  - null-values
timestamp: "2026-06-19T14:00:45.180Z"
---

# Percent Null (Completeness)

**Percent Null (Completeness)** is a data quality metric that tracks the percentage of rows written to a table over a 24-hour window that are expected to contain null values for a given column. It is an additional quality detail that informs the broader **completeness** assessment of a table.^[anomaly-detection-databricks-on-aws.md]

## How It Works

Data quality monitoring analyzes the historical trend of null percentages for each column and builds a predictive range of expected values. If the actual percent of null values for a column in the last 24 hours exceeds the upper bound of this predicted range, the table is flagged as **incomplete**.^[anomaly-detection-databricks-on-aws.md]

This mechanism helps detect anomalous increases in null rates, which may indicate upstream data pipeline failures, schema changes, or corruption.

## Relation to Completeness

Completeness in the context of [Anomaly Detection](/concepts/anomaly-detection.md) is primarily based on the number of rows written to a table within a 24-hour period compared to a predicted range. Percent null enhances completeness by penalizing tables where columns unexpectedly contain a high proportion of nulls, even if the overall row count appears normal.

When a table is marked as incomplete due to an elevated percent null, it is recorded in the data quality monitoring results alongside other completeness violations. See [Completeness (data quality)](/concepts/completeness-data-quality.md) for the primary definition.

## Example

Consider a `transactions` table with a `discount_code` column that historically has 5–10% nulls. If a data pipeline failure causes 60% of new rows to have null `discount_code`, the percent null check will detect that the observed percentage exceeds the predicted upper bound, and the table will be flagged as incomplete.^[anomaly-detection-databricks-on-aws.md]

## Limitations

Anomaly detection’s determination of completeness does not take into account metrics such as the fraction of nulls, zero values, or NaN in the legacy implementation. However, the percent null check is explicitly designed to address null fraction as a completeness indicator.^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The overarching feature that monitors tables for freshness and completeness.
- [Completeness (data quality)](/concepts/completeness-data-quality.md) — The primary completeness metric based on row count predictions.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The system that runs background scans and logs results.
- [Health Indicators](/concepts/health-indicators-databricks.md) — Visual statuses displayed in Catalog Explorer for each table.
- [Freshness (data quality)](/concepts/freshness-data-quality.md) — The companion metric that measures how recently a table has been updated.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
