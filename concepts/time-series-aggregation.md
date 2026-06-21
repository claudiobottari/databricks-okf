---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bed9e8dd944b0468350f6ef5d7de60a5f0ae0a3c328c2150b2690b21ea273551
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-aggregation
    - TSA
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: Time Series Aggregation
description: Method for handling multiple values per timestamp in a time series, defaulting to averaging, with configurable options like sum.
tags:
  - time-series
  - aggregation
  - data-preprocessing
  - forecasting
timestamp: "2026-06-19T18:06:23.384Z"
---

# Time Series Aggregation

**Time Series Aggregation** refers to the process of combining multiple data points that share the same timestamp within a single time series, typically to produce a single representative value for that time point. In AutoML forecasting on Databricks, aggregation is necessary when the input table contains more than one observation for a given time series at the same timestamp.

## Default Behavior

When there are multiple values for a timestamp in a time series, AutoML for forecasting uses the **average** of those values as the aggregated value for that time point. This is the default aggregation method applied during data preparation. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Configuring the Aggregation Function

To use the **sum** instead of the average, you must manually edit the source code notebook that AutoML generates during trial runs. Specifically, locate the cell titled "Aggregate data by …" and change the `.agg()` call from `"avg"` to `"sum"` for the target column. ^[data-preparation-for-forecasting-databricks-on-aws.md]

The following example shows the modification in the generated notebook (Python code):

```python
group_cols = [time_col] + id_cols
df_aggregation = df_loaded \
  .groupby(group_cols) \
  .agg(y=(target_col, "sum")) \
  .reset_index() \
  .rename(columns={ time_col : "ds" })
```

After this change, AutoML will use the sum of the target column values for each timestamp instead of the average during model training and validation. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Related Concepts

- AutoML – Automated machine learning workflows on Databricks.
- [Forecasting](/concepts/forecast.md) – Time series prediction tasks supported by AutoML.
- [Time Series Cross-Validation](/concepts/time-series-cross-validation.md) – The validation strategy used for forecasting in AutoML.
- Data Preparation for Forecasting – The broader data-preparation pipeline that includes imputation, splitting, and aggregation.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime environment that supports forecasting AutoML runs.

## Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
