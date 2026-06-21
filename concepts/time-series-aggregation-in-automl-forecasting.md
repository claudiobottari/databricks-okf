---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3523854bc579ec5b320aa1568f0ca687fe1791ccf1fcb7fa1d14ae14902ed707
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-aggregation-in-automl-forecasting
    - TSAIAF
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: Time Series Aggregation in AutoML Forecasting
description: How AutoML handles multiple values at the same timestamp in a time series, defaulting to averaging and allowing customization to sum via notebook edits.
tags:
  - databricks
  - automl
  - forecasting
  - aggregation
timestamp: "2026-06-19T09:43:18.825Z"
---

# Time Series Aggregation in AutoML Forecasting

**Time series aggregation** is the process of combining multiple values that occur at the same timestamp within a single time series. In [AutoML Forecasting](/concepts/automl-forecast.md), aggregation is necessary when the training data contains more than one observation per time point for a given time series.

## Default Aggregation: Average

When there are multiple values for the same timestamp in a time series, AutoML automatically calculates the **average** of those values. This is the default behavior and is implemented as `avg` in the generated notebook code. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Changing to Sum Aggregation

If the sum of the values is more appropriate for the forecasting problem (for example, when aggregating sales or event counts), you can change the aggregation method from average to sum. To do this, edit the source code notebook that AutoML generates during trial runs. In the **Aggregate data by …** cell, replace `.agg(y=(target_col, "avg"))` with `.agg(y=(target_col, "sum"))`. ^[data-preparation-for-forecasting-databricks-on-aws.md]

```python
group_cols = [time_col] + id_cols
df_aggregation = df_loaded \
  .groupby(group_cols) \
  .agg(y=(target_col, "sum")) \
  .reset_index() \
  .rename(columns={ time_col : "ds" })
```

## Related Concepts

- Data preparation for forecasting – Full guide to configurable data settings in AutoML Forecasting.
- [AutoML Forecasting](/concepts/automl-forecast.md) – Overview of the automated forecasting workflow.
- [Time Series Cross-Validation](/concepts/time-series-cross-validation.md) – How AutoML splits forecasting data for evaluation.
- [AutoML Python API reference](/concepts/automl-python-api.md) – API options for configuring data preparation.
- Notebook generation – How AutoML creates editable notebooks from trial runs.

## Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
