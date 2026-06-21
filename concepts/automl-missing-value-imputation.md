---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 195f4a87fce360dfc3267c16fdc31c9ea4af2caefd65a4635776ca27578337ee
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-missing-value-imputation
    - AMVI
    - AutoML Impute Missing Values
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: AutoML Missing Value Imputation
description: Configurable strategies for handling null values in AutoML regression training, including default per-column-type imputation and custom overrides via UI or API.
tags:
  - machine-learning
  - automl
  - data-cleaning
timestamp: "2026-06-19T14:41:59.212Z"
---

# AutoML Missing Value Imputation

**AutoML Missing Value Imputation** refers to the mechanism by which Databricks AutoML handles null (missing) values in training datasets for supervised learning problems, particularly for regression tasks. AutoML provides both automatic and configurable imputation strategies.

## Default Imputation

By default, AutoML selects an imputation method based on the column’s data type and its content. The system examines the schema and distribution of values to determine a reasonable fill strategy—for example, replacing missing numeric values with the mean or median, and missing categorical values with the mode. This automatic selection applies unless the user explicitly overrides it. ^[data-preparation-for-regression-databricks-on-aws.md]

## Custom Imputation

Starting with **Databricks Runtime 10.4 LTS ML**, users can specify a custom imputation method for each column. In the AutoML UI, a drop-down menu labeled **Impute with** appears in the table schema view, allowing selection of the desired strategy. When using the [AutoML Python API](/concepts/automl-python-api.md), the `imputers` parameter controls this behavior. ^[data-preparation-for-regression-databricks-on-aws.md]

## Impact on Semantic Type Detection

If a user specifies a non-default imputation method for any column, AutoML **disables semantic type detection** for the entire dataset. Semantic type detection normally attempts to reinterpret columns (e.g., treating a string column containing numeric values as numeric, or an integer column containing IDs as categorical). The note in the documentation warns: “If you specify a non-default imputation method, AutoML does not perform semantic type detection.” ^[data-preparation-for-regression-databricks-on-aws.md]

## Supported Feature Types

The imputation feature applies only to supported data types. For regression, AutoML supports the following column types, each of which may contain null values requiring imputation:

- Numeric (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`)
- Boolean
- String (categorical or English text)
- Timestamps (`TimestampType`, `DateType`)
- `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above)
- `DecimalType` (Databricks Runtime 11.3 LTS ML and above)

^[data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- [AutoML (Databricks)](/concepts/automl-on-databricks.md) – The automated machine learning service that includes missing value imputation.
- [Semantic Type Detection](/concepts/semantic-type-detection.md) – AutoML’s automatic detection of column semantics, which is disabled when custom imputation is used.
- [AutoML Python API](/concepts/automl-python-api.md) – Programmatic interface for configuring imputation via the `imputers` parameter.
- Data Preparation for Regression – Broader data preparation steps including column selection, splitting, and sampling.

## Sources

- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
