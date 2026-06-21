---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1ef5256a8627047f06598563820c9f2aca38b8fde534e188e4de02ba53d0d954
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - slicing-expressions-in-data-profiling
    - SEIDP
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Slicing Expressions in Data Profiling
description: Mechanism to compute metrics for data subsets defined by boolean expressions or column values, identified by slice_key and slice_value columns.
tags:
  - databricks
  - data-profiling
  - slicing
timestamp: "2026-06-19T14:43:39.339Z"
---

I'll update the existing wiki page with proper citations from the source material.

# Slicing Expressions in Data Profiling

**Slicing Expressions** are a feature of [Databricks Data Profiling](/concepts/databricks-data-profiling.md) that allow you to compute summary statistics not just for the entire table, but also for meaningful subsets of the data called *slices*. By providing one or more Boolean or categorical expressions, you can break down profile metrics and drift metrics by conditions such as column values or comparisons, enabling more granular analysis of data quality and distribution changes. ^[data-profiling-metric-tables-databricks-on-aws.md]

## How Slicing Works

When you create a monitor using `create_monitor`, you can supply a list of slicing expressions via the `slicing_exprs` parameter. Each expression defines a potential slice key. For each slice key, Databricks automatically generates all possible slices:

- For a Boolean expression such as `col_2 > 10`, two slices are created: one where the condition is true and one where it is false.
- For a categorical column reference such as `col_1`, a slice is created for each unique value in that column.

For example, the following configuration:

```python
slicing_exprs=["col_1", "col_2 > 10"]
```

generates the following slices:

- One slice for `col_2 > 10` (true)
- One slice for `col_2 <= 10` (false)
- One slice for each unique value in `col_1`

Metrics are computed for every combination of time window and slice, in addition to the overall table summary. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Slice Keys and Slice Values in Metric Tables

Slices are identified in the profile metrics and drift metrics tables by two columns:

- `slice_key`: the textual representation of the slicing expression (e.g., `"col_2 > 10"` or `"col_1"`).
- `slice_value`: the actual value of the slice for that key (e.g., `"true"`, `"false"`, or a specific category like `"engineering"`).

A slice is always defined by a single slice key. The aggregate over the entire table is represented by `slice_key = NULL` and `slice_value = NULL`. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Scope of Slicing

Metrics are computed for all possible groups defined by the time windows, slice keys, and slice values. For [InferenceLog Analysis](/concepts/inferencelog-analysis.md), additional slices are automatically created based on the distinct values of the `model_id_col` column, so you can analyze performance per model version. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Use Cases

- **Data quality monitoring**: Track how null counts, distinct values, or distributional statistics vary across departments, regions, or time periods.
- **Fairness and bias analysis**: For classification models, fairness and bias statistics are calculated for slices that have a Boolean value, enabling comparison of model performance across demographic groups.
- **Drift detection**: Drift metrics can be computed per slice, allowing you to alert on distributional changes that affect only specific segments of the data.

## Related Concepts

- Data Profiling Metric Tables – The output tables where sliced metrics are stored.
- [Drift Metrics](/concepts/drift-metrics.md) – Distribution-change statistics, also computed per slice.
- Profile Metrics Table Schema – Full list of columns including `slice_key` and `slice_value`.
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md) – Automated slicing by model ID.
- [Fairness and Bias Statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) – Boolean slice analysis for classification models.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
