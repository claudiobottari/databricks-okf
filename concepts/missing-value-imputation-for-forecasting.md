---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f7d2bb41ce5b8c6dd9fc385ceeb2a38be2218544ffdcb9f3238c16c025cc8d39
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing-value-imputation-for-forecasting
    - MVIFF
    - Imputation Strategies for Forecasting
    - Impute Missing Values for Forecasting
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: Missing Value Imputation for Forecasting
description: AutoML allows specifying imputation methods for null values per column; defaults are chosen by column type and content, and custom imputation disables semantic type detection.
tags:
  - imputation
  - missing-values
  - forecasting
  - databricks
timestamp: "2026-06-18T11:29:19.164Z"
---

# Missing Value Imputation for Forecasting

**Missing Value Imputation for Forecasting** refers to the techniques used by [AutoML Forecasting](/concepts/automl-forecast.md) to handle null values in time series data before training models. Proper imputation is critical because forecasting algorithms typically require complete, regularly spaced observations.

## Overview

In forecasting tasks, missing values can arise from data collection gaps, sensor failures, or irregular reporting intervals. Databricks AutoML supports configurable imputation methods to fill these gaps. By default, AutoML automatically selects an imputation method based on the column’s data type and content.^[data-preparation-for-forecasting-databricks-on-aws.md]

## Supported Data Types for Imputation

Imputation is available only for the following feature types. Other types, such as images, are not supported:

- Numeric (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`)
- Boolean
- String (categorical or English text)
- Timestamps (`TimestampType`, `DateType`)
- `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above)
- `DecimalType` (Databricks Runtime 11.3 LTS ML and above)

^[data-preparation-for-forecasting-databricks-on-aws.md]

## Default Imputation Behavior

When no custom imputation method is specified, AutoML examines each column’s type and content to choose a sensible strategy (e.g., mean or median for numeric columns, mode for categorical columns). This automatic selection is part of the data preparation pipeline and runs before model training.^[data-preparation-for-forecasting-databricks-on-aws.md]

## Custom Imputation Methods

Users can override the default imputation for specific columns. This is available in Databricks Runtime 10.4 LTS ML and above.

- **In the UI**: Select a method from the drop-down menu in the **Impute with** column of the table schema during experiment setup.
- **In the API**: Use the `imputers` parameter. For details, see the [AutoML Python API reference](/concepts/automl-python-api.md).

^[data-preparation-for-forecasting-databricks-on-aws.md]

> **Important**: If you specify a non-default imputation method, AutoML does **not** perform semantic type detection on that column. Semantic type detection normally identifies date, text, or categorical columns automatically; with a custom imputer, you must ensure the column type is explicitly set.^[data-preparation-for-forecasting-databricks-on-aws.md]

## Integration with Time Series Cross-Validation

Imputation is applied during data preparation, before the data is split into training, validation, and test sets using [Time Series Cross-Validation](/concepts/time-series-cross-validation.md). Because the same imputation strategy is used across all folds, the validation and test sets reflect the preprocessed data that the model will see in production.^[data-preparation-for-forecasting-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) – The overall forecasting pipeline that includes imputation
- [Semantic Type Detection](/concepts/semantic-type-detection.md) – An automated step that is skipped when custom imputers are used
- [Time Series Aggregation](/concepts/time-series-aggregation.md) – How AutoML handles multiple values per timestamp (uses average by default)
- [Databricks AutoML](/concepts/databricks-automl.md) – The machine learning automation platform

## Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
