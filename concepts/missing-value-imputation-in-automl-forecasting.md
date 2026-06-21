---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f4e32103a3cf5442c43f3f0152dca5cb99f2728ddfc0a35b8fb23bf700db557
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing-value-imputation-in-automl-forecasting
    - MVIIAF
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
      start: 54
      end: 55
    - file: data-preparation-for-forecasting-databricks-on-aws.md
      start: 46
      end: 50
    - file: data-preparation-for-forecasting-databricks-on-aws.md
      start: 51
      end: 53
    - file: data-preparation-for-forecasting-databricks-on-aws.md
      start: 57
      end: 60
    - file: data-preparation-for-forecasting-databricks-on-aws.md
      start: 12
      end: 22
title: Missing Value Imputation in AutoML Forecasting
description: How Databricks AutoML handles null values in forecasting datasets, including configurable imputation methods via UI or API, with automatic selection based on column type and content.
tags:
  - forecasting
  - data-preparation
  - imputation
  - databricks
timestamp: "2026-06-19T14:41:37.708Z"
---

Here is the updated wiki page for "Missing Value Imputation in AutoML Forecasting" that includes only the information from the provided source material.

---

# Missing Value Imputation in AutoML Forecasting

**Missing value imputation** is the process of replacing null (missing) values in a dataset with substituted values to prepare data for [AutoML Forecasting](/concepts/automl-forecast.md) model training. AutoML supports configurable imputation strategies to handle missing data in time series and other forecasting datasets.

## Default Imputation Behavior

By default, AutoML selects an imputation method based on the column type and content. The system automatically chooses a suitable strategy (e.g., mean, median, or forward-fill for time series) depending on the data characteristics. This default behavior applies to both the UI and API workflows. ^[data-preparation-for-forecasting-databricks-on-aws.md:54-55]

## Custom Imputation (Databricks Runtime 10.4 LTS ML and above)

Starting with Databricks Runtime 10.4 LTS ML, users can override the default imputation method for each column:

- **In the UI:** During experiment setup, open the table schema and select a method from the drop-down in the **Impute with** column. ^[data-preparation-for-forecasting-databricks-on-aws.md:46-50]
- **In the API:** Use the `imputers` parameter when configuring the forecasting experiment. See the [AutoML Python API reference](/concepts/automl-python-api.md) for full details. ^[data-preparation-for-forecasting-databricks-on-aws.md:51-53]

Available imputation strategies may include mean, median, mode, constant value, or time-series‑specific methods like forward fill or linear interpolation. The exact set of supported options depends on the Databricks Runtime version.

## Impact on Semantic Type Detection

If you specify a non‑default imputation method, AutoML does **not** perform [Semantic Type Detection](/concepts/semantic-type-detection.md) on the affected column. Semantic type detection automatically identifies column types such as categorical, numeric, or timestamp, enabling further feature engineering. Custom imputation opts out of this detection, so you may need to ensure that the column’s type is correctly understood for downstream modeling. ^[data-preparation-for-forecasting-databricks-on-aws.md:57-60]

## Supported Feature Types for Imputation

Imputation is available for the following column types, all of which are supported as valid feature types in AutoML Forecasting:

- Numeric (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`)
- Boolean
- String (categorical or English text)
- Timestamps (`TimestampType`, `DateType`)
- `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above)
- `DecimalType` (Databricks Runtime 11.3 LTS ML and above)

^[data-preparation-for-forecasting-databricks-on-aws.md:12-22]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) – Overview of automated forecasting on Databricks
- [Time Series Cross-Validation](/concepts/time-series-cross-validation.md) – How AutoML splits forecasting data
- [Semantic Type Detection](/concepts/semantic-type-detection.md) – Automatic identification of column semantics
- [AutoML Python API Reference](/concepts/automl-python-api.md) – API for configuring imputation and other settings
- Data Preparation for Forecasting – Full guide for forecasting data preparation

## Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md:54-55](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
2. [data-preparation-for-forecasting-databricks-on-aws.md:46-50](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
3. [data-preparation-for-forecasting-databricks-on-aws.md:51-53](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
4. [data-preparation-for-forecasting-databricks-on-aws.md:57-60](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
5. [data-preparation-for-forecasting-databricks-on-aws.md:12-22](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
