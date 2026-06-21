---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6ce32315adcb00ce2f016aaf0d156a75ab1d31db2ca1cf580f2b059f9d840e9
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-data-feature-types-for-automl-forecasting
    - SDFTFAF
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: Supported Data Feature Types for AutoML Forecasting
description: The specific data types (numeric, boolean, string, timestamp, array, decimal) that AutoML accepts for forecasting tasks on Databricks.
tags:
  - databricks
  - automl
  - forecasting
  - data-types
timestamp: "2026-06-19T09:43:16.708Z"
---

# Supported Data Feature Types for AutoML Forecasting

**Supported Data Feature Types for AutoML Forecasting** defines the column data types that AutoML on Databricks can accept as input features when training forecasting models. Only the types listed below are supported; unsupported types such as images will cause the experiment to fail. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Supported Types

The following feature types are supported by AutoML forecasting:

- **Numeric** — `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, and `DoubleType`
- **Boolean**
- **String** — treated as categorical or English text
- **Timestamps** — `TimestampType` and `DateType`
- **ArrayType[Numeric]** — supported in Databricks Runtime 10.4 LTS ML and above
- **DecimalType** — supported in Databricks Runtime 11.3 LTS ML and above

^[data-preparation-for-forecasting-databricks-on-aws.md]

## Unsupported Types

Data types not in the list above are unsupported. In particular, images and other non-tabular data types are not supported for forecasting. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Additional Data Preparation Details

### Imputation of Missing Values

AutoML can impute null values using a method selected automatically based on column type and content, or a user-specified method (available from Databricks Runtime 10.4 LTS ML and above). For more details, see [Impute Missing Values for Forecasting](/concepts/missing-value-imputation-for-forecasting.md).^[data-preparation-for-forecasting-databricks-on-aws.md]

### Time Series Cross-Validation

AutoML uses time series cross-validation to split data into train, validation, and test sets. The number of folds depends on the input table’s characteristics such as the number of time series, presence of covariates, and series length. ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Aggregation

When multiple values exist for the same timestamp in a time series, AutoML uses the average by default. To use the sum instead, the generated source notebook must be edited. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Related Concepts

- AutoML Overview — General introduction to automated machine learning on Databricks
- Forecasting with AutoML — End-to-end workflow for time series forecasting
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Runtime versions that include feature support
- Data Types in Spark — Spark SQL data type reference
- [AutoML Python API Reference](/concepts/automl-python-api.md) — Programmatic configuration of feature types and imputation

## Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
