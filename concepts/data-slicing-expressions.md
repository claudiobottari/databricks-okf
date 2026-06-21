---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64756188c29e43ad62938a70a11b487ee54bd131b3e8a5171f1fcc24c80046c2
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-slicing-expressions
    - DSE
    - Slicing Expression
    - Slicing Expressions
    - Slicing expressions
    - Data Slicing
    - Slice Expression
    - slice expression
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Data Slicing Expressions
description: A mechanism to compute per-segment statistics by partitioning data based on column values or Boolean expressions, generating multiple slice keys and values.
tags:
  - data-profiling
  - segmentation
  - databricks
timestamp: "2026-06-18T15:01:26.346Z"
---

# Data Slicing Expressions

**Data Slicing Expressions** are expressions used in [Data Profiling](/concepts/data-profiling.md) to partition data into subsets, called "slices," for which summary statistics are computed independently. When a [data quality monitor](/concepts/data-quality-monitoring.md) runs on a Databricks table, metrics are always computed for the entire table, and if slicing expressions are provided, metrics are also computed for each individual data slice defined by a value of the expression.^[data-profiling-metric-tables-databricks-on-aws.md]

## How Slicing Works

A slicing expression is a Boolean expression or column reference that defines how to partition the data. When multiple slicing expressions are provided, each expression generates its own set of slices independently. Slices are identified in metric tables by the column names `slice_key` and `slice_value`.^[data-profiling-metric-tables-databricks-on-aws.md]

For example, given the slicing expressions:

```
slicing_exprs=["col_1", "col_2 > 10"]
```

The following slices are generated:
- One slice for `col_2 > 10` (true values)
- One slice for `col_2 <= 10` (false values)
- One slice for each unique value in `col_1`

The slice key would be the expression string (e.g., "col_2 > 10") and the slice value would be the evaluated result (e.g., "true" or "false"). The entire table is equivalent to `slice_key = NULL` and `slice_value = NULL`. Each slice is defined by a single slice key.^[data-profiling-metric-tables-databricks-on-aws.md]

## Purpose

Slicing allows you to:
- Analyze subpopulations within your data
- Identify performance or quality differences across data segments
- Detect [data drift](/concepts/data-drift-detection.md) within specific groups rather than only at the aggregate level
- Monitor fairness and bias statistics for classification models (for [InferenceLog Analysis](/concepts/inferencelog-analysis.md), slices that have a Boolean value automatically receive fairness and bias statistics)^[data-profiling-metric-tables-databricks-on-aws.md]

## Automatic Slicing for Model Inference Logs

For `InferenceLog` analysis, slices are automatically created based on the distinct values of `model_id_col`. Each model version gets its own slice, allowing per-model monitoring. Additionally, for classification models, fairness and bias statistics are calculated for slices that have a Boolean value.^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data profiling metric tables](/concepts/profile-metrics-table.md) — The metric tables where slice statistics are stored
- [Drift Metrics](/concepts/drift-metrics.md) — How slicing enables per-slice drift detection
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — Overview of monitoring concepts
- [Fairness and bias statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) — Slice-based fairness analysis for classification models

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
