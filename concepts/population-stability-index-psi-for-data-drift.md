---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa591af822a378730b09a7401eb3a6dd060f5b60157b6bc257a5c475d468a475
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - population-stability-index-psi-for-data-drift
    - PSI(FDD
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Population Stability Index (PSI) for Data Drift
description: PSI is a numeric metric in [0, ∞) comparing two distributions; <0.1 no significant change, <0.2 moderate change, >=0.2 significant change. Used in Databricks drift metrics tables.
tags:
  - drift-detection
  - statistics
  - population-stability-index
timestamp: "2026-06-19T09:45:18.146Z"
---

# Population Stability Index (PSI) for Data Drift

**Population Stability Index (PSI) for Data Drift** is a statistical measure that quantifies how much a distribution has shifted between two time periods or populations. In the context of [Data Drift Monitoring](/concepts/data-drift-monitoring.md), PSI provides a standardized method for detecting when the underlying distribution of a dataset has changed significantly.

## Overview

PSI is a numeric value that represents how different two distributions are. The metric has a range of $[0, \infty)$. The magnitude of the PSI value indicates the severity of the population change:^[data-profiling-metric-tables-databricks-on-aws.md]

- **PSI < 0.1**: No significant population change
- **PSI < 0.2**: Moderate population change
- **PSI >= 0.2**: Significant population change

## Calculation

PSI compares two distributions by dividing them into bins or buckets and computing the proportion of observations in each bin for both distributions. The formula for PSI is:

$$\text{PSI} = \sum_{i=1}^{n} (P_i - Q_i) \times \ln\left(\frac{P_i}{Q_i}\right)$$

Where:
- $P_i$ is the proportion of observations in bin $i$ for the first distribution (e.g., the current time window)
- $Q_i$ is the proportion of observations in bin $i$ for the second distribution (e.g., the baseline or previous time window)
- $n$ is the total number of bins

## Use in Data Drift Monitoring

In the context of [Databricks Data Profiling](/concepts/databricks-data-profiling.md), PSI is computed by the drift metrics table to track changes in distribution for each metric. The drift table is generated only when a baseline table is provided, or when a consecutive time window exists after aggregation according to the specified granularities.^[data-profiling-metric-tables-databricks-on-aws.md]

### Types of Drift Comparison

The drift metrics table computes two types of drift using PSI:^[data-profiling-metric-tables-databricks-on-aws.md]

1. **Consecutive drift**: Compares a window to the previous time window. Consecutive drift is only calculated if a consecutive time window exists after aggregation according to the specified granularities.
2. **Baseline drift**: Compares a window to the baseline distribution determined by the baseline table. Baseline drift is only calculated if a baseline table is provided.

## Implementation in Databricks

When you create a data profile on a Databricks table, the profiling system generates two metric tables: a profile metrics table and a drift metrics table. The drift metrics table contains PSI values along with other drift statistics that track changes in distribution over time. These tables are stored at `{output_schema}.{table_name}_drift_metrics`.^[data-profiling-metric-tables-databricks-on-aws.md]

### PSI in the Drift Metrics Table Schema

Within the drift metrics table, PSI values appear alongside other drift metrics. The table uses grouping columns such as time window, granularity, slice key and value, and model ID (for [InferenceLog Analysis](/concepts/inferencelog-analysis.md)) to organize the drift calculations. The drift type column indicates whether the PSI value represents a comparison to the previous window or to the baseline table.^[data-profiling-metric-tables-databricks-on-aws.md]

## Usage for Alerting

PSI values from drift metrics tables can be used to visualize changes in the data or to set up alerts that trigger when the PSI exceeds defined thresholds. For example, a monitoring system could alert when PSI >= 0.2, indicating a significant population change that may require investigation.^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Drift Monitoring](/concepts/data-drift-monitoring.md)
- Data Profiling Metric Tables
- [Baseline Table](/concepts/baseline-table.md)
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- Distribution Shift

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
