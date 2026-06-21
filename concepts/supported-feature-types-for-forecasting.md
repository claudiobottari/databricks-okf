---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8c447edc1657bafd2c11ea501385000f8a2d1de90706e5ba2c936fc8a64e846
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-feature-types-for-forecasting
    - SFTFF
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: Supported Feature Types for Forecasting
description: The set of data types (numeric, boolean, string, timestamps, arrays, decimals) supported by Databricks AutoML for forecasting tasks.
tags:
  - data-types
  - forecasting
  - automl
timestamp: "2026-06-19T18:05:46.770Z"
---

# Supported Feature Types for Forecasting

When preparing data for forecasting with [AutoML for Forecasting](/concepts/auto-arima-for-forecasting.md), only specific feature types are accepted. Understanding which data types are supported helps you structure your input data correctly and avoid common errors during model training. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Supported Feature Types

The following feature types are supported for forecasting tasks. Feature types not listed — such as images — are not supported. ^[data-preparation-for-forecasting-databricks-on-aws.md]

| Feature Type | Spark Data Types | Notes |
|-------------|------------------|-------|
| **Numeric** | `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType` | Standard numeric columns |
| **Boolean** | `BooleanType` | Treated as a categorical feature |
| **String** | `StringType` | Can represent categorical variables or English text |
| **Timestamp** | `TimestampType`, `DateType` | Required for the time component of forecasting |
| **ArrayType[Numeric]** | `ArrayType` with numeric element types | Supported in Databricks Runtime 10.4 LTS ML and above |
| **DecimalType** | `DecimalType` | Supported in Databricks Runtime 11.3 LTS ML and above |

^[data-preparation-for-forecasting-databricks-on-aws.md]

## Unsupported Feature Types

The following feature types are **not** supported:

- **Images** — Image columns are not accepted as features for forecasting models.
- Any Spark data type not listed in the supported table above, including complex nested types (except `ArrayType[Numeric]`).

^[data-preparation-for-forecasting-databricks-on-aws.md]

## Runtime Version Requirements

Two feature types have specific runtime requirements: ^[data-preparation-for-forecasting-databricks-on-aws.md]

- **ArrayType[Numeric]** is supported in Databricks Runtime 10.4 LTS ML and above.
- **DecimalType** is supported in Databricks Runtime 11.3 LTS ML and above.

Using these feature types with an older runtime version will result in errors during model training.

## Best Practices

- **Check your schema before training.** Use `df.printSchema()` or your DataFrame's schema to verify that all columns use supported types.
- **Convert strings to appropriate types.** If a string column represents a numeric value or a timestamp, cast it to the correct type before training.
- **Use ArrayType[Numeric] sparingly.** While supported, array features can increase model complexity and training time. Only include them if they provide meaningful signal for the forecasting task.
- **Verify runtime compatibility.** If using ArrayType[Numeric] or DecimalType, confirm that your cluster runs the required Databricks Runtime version.

## Related Concepts

- Data Preparation for Forecasting — Full guide on preparing data for AutoML forecasting
- [AutoML Forecasting Training](/concepts/automl-forecasting-forecast.md) — How to configure and run forecasting experiments
- [Time Series Cross-Validation](/concepts/time-series-cross-validation.md) — How AutoML splits forecasting data for evaluation
- [Imputation Strategies for Forecasting](/concepts/missing-value-imputation-for-forecasting.md) — Handling missing values in forecasting data
- Spark Data Types — Reference for supported and unsupported Spark types

## Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
