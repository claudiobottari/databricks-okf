---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03e6faefd34a52f144ef14088a016f68264018ba61badbbd3d75fdd45e332600
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - percent-null-completeness-check
    - PNCC
    - NCC
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Percent Null Completeness Check
description: An additional quality detail of completeness that monitors the expected percentage of rows with null values for a given column over the last 24 hours, flagging a table as incomplete if the observed null percentage exceeds the predicted upper bound.
tags:
  - data-quality
  - anomaly-detection
  - null-analysis
timestamp: "2026-06-19T09:04:00.618Z"
---

# Percent Null Completeness Check

**Percent Null Completeness Check** is a data quality metric within [Anomaly Detection](/concepts/anomaly-detection.md) on Databricks that monitors the expected null rate of columns in a table. It provides additional detail to the standard completeness evaluation by tracking whether the percentage of null values in a column deviates significantly from historical patterns.

## Overview

Percent null measures the percentage of rows written to a table in the last 24 hours that have null values for a given column. Data quality monitoring analyzes the historical trend for each column and, based on this data, predicts an expected range. If the percent null for a column over the last 24 hours is higher than the upper bound of this range, the table is marked as incomplete. ^[anomaly-detection-databricks-on-aws.md]

This metric is part of the **completeness** dimension of anomaly detection. Completeness refers to the number of rows expected to be written to the table in the last 24 hours. Data quality monitoring analyzes historical row counts, predicts a range of expected row counts, and marks tables as incomplete if committed rows fall below the lower bound. Percent null adds column-level granularity to this assessment. ^[anomaly-detection-databricks-on-aws.md]

## How It Works

The percent null completeness check operates as follows:

1. **Historical analysis**: Databricks analyzes historical trends for each column to establish a baseline pattern of null values. ^[anomaly-detection-databricks-on-aws.md]
2. **Range prediction**: Based on historical data, the system predicts an expected range for the percentage of null values in the last 24 hours. ^[anomaly-detection-databricks-on-aws.md]
3. **Anomaly detection**: If the observed percent null exceeds the upper bound of the predicted range, the table is flagged as **incomplete**. ^[anomaly-detection-databricks-on-aws.md]

This check does not consider other metrics such as zero values or NaN — it focuses specifically on null percentages. ^[anomaly-detection-databricks-on-aws.md]

## Relation to Completeness

The percent null check adds additional quality details to the completeness evaluation. While completeness evaluates whether enough total rows were written, percent null evaluates whether individual columns contain an acceptable proportion of null values. A table may pass the row count completeness check but fail the percent null completeness check if a specific column shows an unusual increase in null values. ^[anomaly-detection-databricks-on-aws.md]

## Limitations

- The determination of completeness does not take into account metrics such as the fraction of nulls, zero values, or NaN — except through the specific percent null check described here. ^[anomaly-detection-databricks-on-aws.md]
- Percent null analysis is limited to columns that have sufficient historical data for the predictive model to establish a reliable baseline.

## Viewing Results

Results for the percent null completeness check can be viewed through:

- **Health indicators** in Catalog Explorer, which show summary table health status
- **Data Quality Monitoring UI**, which displays incident details for unhealthy tables
- **Table Quality Details** view, which shows graphs of predicted and observed values at each evaluation timestamp, including percent null trends over the last week of data

Users need SELECT or BROWSE privileges to view health indicator status. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The overarching framework for monitoring data quality
- [Freshness Completeness Checks](/concepts/freshness-and-completeness-quality-metrics.md) — The two primary dimensions of anomaly detection
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader system for tracking table health
- [Health Indicators](/concepts/health-indicators-databricks.md) — Visual summaries of table quality status in Catalog Explorer
- [Table Quality Details](/concepts/table-quality-details-ui.md) — Deep-dive UI showing trends and root cause analysis

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
