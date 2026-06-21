---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6673a8b63bd0bc4e737311b2fb718a39c3c949de32647cc91feae47c59c55809
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 0.95
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - automl-forecasting-data-splitting-strategy
    - AFDSS
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: AutoML Forecasting Data Splitting Strategy
description: How Databricks AutoML partitions forecasting data into train, validation, and test sets using time series cross-validation, where the number of folds depends on input table characteristics such as number of time series, covariates presence, and series length.
tags:
  - forecasting
  - data-splitting
  - model-validation
  - databricks
timestamp: "2026-06-19T14:41:49.335Z"
---

## AutoML Forecasting Data Splitting Strategy

**AutoML Forecasting Data Splitting Strategy** refers to the method AutoML uses to partition time series data into training, validation, and test sets for forecasting model training. Unlike random splitting used in non-temporal tasks, forecasting requires a chronological approach to preserve the temporal order of observations and prevent data leakage. ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Time Series Cross-Validation

For forecasting tasks, AutoML applies **time series cross-validation**. This technique incrementally extends the training dataset in chronological order and performs validation on subsequent time points that follow the training window. This approach provides a robust evaluation of model performance over different segments of time, ensuring that the forecasting model is rigorously tested against unseen future data and maintaining the relevance and accuracy of predictions. ^[data-preparation-for-forecasting-databricks-on-aws.md]

The number of cross-validation folds is not fixed; it depends on several characteristics of the input table, including:

- The number of distinct time series in the data
- The presence of covariates (exogenous variables)
- The length of each time series

AutoML selects the fold count automatically based on these factors. ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Related Data Preparation Steps

Before splitting, AutoML performs a number of data preparation operations that affect the splitting strategy:

- **Imputation of missing values**: You can specify how null values are imputed (via the UI or the `imputers` API parameter). AutoML selects a default method based on column type and content. ^[data-preparation-for-forecasting-databricks-on-aws.md]
- **Time series aggregation**: When multiple values exist for the same timestamp within a time series, AutoML averages those values. You can change this to use the sum by editing the generated source code notebook. ^[data-preparation-for-forecasting-databricks-on-aws.md]

Only certain feature types are supported in forecasting data: numeric, boolean, string (categorical or text), timestamps, `ArrayType[Numeric]`, and `DecimalType`. ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Configuration

You can adjust data splitting and preparation settings during experiment setup in the AutoML UI, or via the [AutoML Python API](/concepts/automl-python-api.md) using parameters such as `imputers`. For details, see the [AutoML Python API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference). ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Related Concepts

- [Time Series Cross-Validation](/concepts/time-series-cross-validation.md)
- [AutoML Forecasting](/concepts/automl-forecast.md)
- Data Preparation for Forecasting
- [Imputation in AutoML](/concepts/missing-value-imputation-in-automl.md)

### Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
