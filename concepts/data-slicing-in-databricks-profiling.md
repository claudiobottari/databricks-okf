---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e768b674b6ac4d883c6b86a6bde7d87e35bfccc40e48b5af43536b4b7489ee4
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-slicing-in-databricks-profiling
    - DSIDP
    - Data Slicing in Data Profiling
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Data Slicing in Databricks Profiling
description: A technique for computing profile metrics on subsets of data defined by boolean expressions or column values, enabling segmented analysis of data quality.
tags:
  - data-profiling
  - data-quality
  - slicing
timestamp: "2026-06-18T11:31:31.180Z"
---

# Data Slicing in Databricks Profiling

**Data Slicing** in Databricks Profiling allows you to compute statistics and metrics for specific subsets of your data, in addition to the overall table-wide calculations. By providing slicing expressions, you define logical partitions of your data, and the profiling engine automatically generates and evaluates metrics for each slice. ^[data-profiling-metric-tables-databricks-on-aws.md]

## How Slicing Works

When you configure data profiling, you can specify one or more slicing expressions using the `slicing_exprs` parameter. These expressions are evaluated by the profiling engine to create named data slices. Each expression generates two slice results: one for when the expression evaluates to `true` and one for `false`. For example:

`slicing_exprs=["col_1", "col_2 > 10"]`

This configuration produces the following slices:
- One slice for `col_2 > 10` (true)
- One slice for `col_2 <= 10` (false)
- One slice for each unique value in `col_1`

^[data-profiling-metric-tables-databricks-on-aws.md]

## Slice Identification in Metric Tables

Slices are identified in the [Profile Metrics Table](/concepts/profile-metrics-table.md) and [Drift Metrics Table](/concepts/drift-metrics-table.md) by two key columns: ^[data-profiling-metric-tables-databricks-on-aws.md]

| Column | Description |
|--------|-------------|
| `slice_key` | The name or expression used to define the slice |
| `slice_value` | The boolean or categorical value of the slice |

The overall table (no slicing applied) is represented by `slice_key` = NULL and `slice_value` = NULL. Each slice is defined by a single slice key and its corresponding value. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Computing Metrics Per Slice

Metrics are always computed for the entire table. When you provide slicing expressions, the profiling engine calculates statistics for each data slice defined by a value of the expression. This enables you to compare performance or characteristics across different segments of your data. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Example: Querying Slice-Specific Metrics

Using InferenceLog analysis, you can query metrics for specific slices:

```sql
SELECT window.start, column_name, count, num_nulls, distinct_count, frequent_items
FROM census_monitor_db.adult_census_profile_metrics
WHERE model_id = 1
  AND slice_key IS NULL    -- look at aggregate metrics over the whole data
  AND column_name = "income_predicted"
ORDER BY window.start
```

^[data-profiling-metric-tables-databricks-on-aws.md]

## Use Cases for Data Slicing

### Model Accuracy Analysis (InferenceLog)

For `InferenceLog` analysis, additional statistics are calculated automatically:
- Slices are created based on distinct values of `model_id_col`
- For classification models, fairness and bias statistics are calculated for Boolean-valued slices
- Model quality is computed when both `label_col` and `prediction_col` are provided

^[data-profiling-metric-tables-databricks-on-aws.md]

### Comparative Analysis

Data slicing enables you to:
- Identify performance variations across different data segments
- Monitor drift patterns within specific subsets
- Compare model behavior across different model versions or deployment scenarios

## Related Concepts

- [Profile Metrics Table](/concepts/profile-metrics-table.md) — Stores summary statistics for each slice and column combination
- [Drift Metrics Table](/concepts/drift-metrics-table.md) — Tracks distribution changes across slices
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md) — Automated slicing by model_id for model monitoring
- [Fairness and Bias Statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) — Calculated for Boolean-valued slices in classification models
- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) — Visual representation of profiling results

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
