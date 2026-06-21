---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad1305307a2c6ecd8e1167ce0457e6cad737cfd3360e5e0fe5df54c52c16e195
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-feature-types-supported-by-databricks-automl-forecasting
    - DFTSBDAF
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: Data Feature Types Supported by Databricks AutoML Forecasting
description: The specific column types (Numeric, Boolean, String, Timestamps, ArrayType[Numeric], DecimalType) that are supported for forecasting tasks in Databricks AutoML.
tags:
  - forecasting
  - data-types
  - databricks
  - automl
timestamp: "2026-06-19T14:42:07.119Z"
---

# Data Feature Types Supported by Databricks AutoML Forecasting

**Data Feature Types Supported by Databricks AutoML Forecasting** defines the specific Spark SQL data types that are accepted as input features when training forecasting models using [Databricks AutoML](/concepts/databricks-automl.md). Only the types listed below are supported; unsupported types such as images will cause errors. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Supported Feature Types

The following feature types are supported for forecasting training: ^[data-preparation-for-forecasting-databricks-on-aws.md]

| Category | Supported Types |
|----------|-----------------|
| **Numeric** | `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType` |
| **Boolean** | `BooleanType` |
| **String** | Categorical or English text |
| **Timestamp** | `TimestampType`, `DateType` |
| **Array** | `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above) |
| **Decimal** | `DecimalType` (Databricks Runtime 11.3 LTS ML and above) |

### Numeric Types

Standard numeric Spark SQL types — from `ByteType` through `DoubleType` — are supported as features. These cover integer and floating-point columns. ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Boolean Type

`BooleanType` columns are accepted as features. ^[data-preparation-for-forecasting-databricks-on-aws.md]

### String Type

`StringType` columns are interpreted as either categorical features or free-form English text, depending on the column content and the AutoML [Semantic Type Detection](/concepts/semantic-type-detection.md) mechanism (when default imputation is used). ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Timestamp Types

`TimestampType` and `DateType` columns are supported and typically used as the time axis for forecasting. ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Array[Numeric] Type (Runtime 10.4 LTS ML+)

`ArrayType[Numeric]` is supported starting in Databricks Runtime 10.4 LTS ML. This allows columns that contain arrays of numeric values to be used as features. ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Decimal Type (Runtime 11.3 LTS ML+)

`DecimalType` is supported starting in Databricks Runtime 11.3 LTS ML. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Unsupported Types

Feature types not listed above are not supported. For example, image columns (or other binary or complex types) are explicitly unsupported and will cause forecasting training to fail. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Configuration During Experiment Setup

These feature type constraints are enforced during the data ingestion step of an AutoML forecasting experiment. You can review and adjust which columns are included as features — and how null values are imputed — during experiment setup in the AutoML UI or via the [AutoML forecasting Python API](/concepts/automl-forecast-api.md). ^[data-preparation-for-forecasting-databricks-on-aws.md]

### Imputation Methods per Column

In the UI, the **Impute with** drop-down column in the table schema allows you to specify how null values are handled for each supported feature type. By default, AutoML selects an imputation method based on the column type and content. ^[data-preparation-for-forecasting-databricks-on-aws.md]

> **Note:** If you specify a non-default imputation method, AutoML skips [Semantic Type Detection](/concepts/semantic-type-detection.md) and treats columns strictly according to their declared Spark SQL type. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Related Concepts

- [Data Preparation for AutoML Forecasting](/concepts/databricks-automl-forecasting-api.md) — Full guide to preparing data for forecasting experiments
- [AutoML Forecasting on Databricks](/concepts/automl-forecasting-forecast.md) — Overview of the automated forecasting workflow
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — How AutoML interprets column meanings
- [Imputation Strategies in AutoML](/concepts/automl-imputation-strategies.md) — Handling missing values
- Spark SQL Data Types — Reference for all supported Spark types

## Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
