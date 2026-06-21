---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5a77f7673e5723c563b99cf1ea830b97d75f3bfdcaf9c3ed37374b1aa96ff36
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-feature-types-in-databricks-automl
    - SFTIDA
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Supported Feature Types in Databricks AutoML
description: The exhaustive list of Spark data types (numeric, boolean, string, timestamp, array, decimal) that AutoML accepts as feature columns.
tags:
  - machine-learning
  - automl
  - data-types
timestamp: "2026-06-19T14:42:14.918Z"
---

# Supported Feature Types in Databricks AutoML

**Supported Feature Types in Databricks AutoML** defines the column data types that AutoML can process during model training. If a dataset contains unsupported feature types — such as images — those columns must be removed or transformed before AutoML can use the data. ^[data-preparation-for-regression-databricks-on-aws.md]

## Supported Feature Types

AutoML supports the following Spark SQL feature types for regression (and by extension, classification) tasks:

| Feature Type | Spark Data Types | Notes |
|---|---|---|
| Numeric | `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType` | Standard numerical columns. |
| Boolean | `BooleanType` | Binary features. |
| String | `StringType` | Treated as categorical or English text; semantic type detection may further refine the treatment. |
| Timestamps | `TimestampType`, `DateType` | Time-related features. |
| ArrayType[Numeric] | `ArrayType` with numeric element type | Supported in Databricks Runtime 10.4 LTS ML and above. |
| DecimalType | `DecimalType` | Supported in Databricks Runtime 11.3 LTS ML and above. |

^[data-preparation-for-regression-databricks-on-aws.md]

Columns with unsupported types (e.g., structs, maps, images) are ignored or must be excluded during data preparation.

## Semantic Type Detection

Even when columns have a raw Spark data type that is supported, AutoML attempts to detect a more appropriate **semantic type** for the column’s content. This detection is best-effort and can be overridden manually using semantic type annotations.

The following adjustments are made automatically in Databricks Runtime 10.1 ML and above:

- **String or integer columns representing dates/timestamps** → treated as timestamp type.
- **String columns representing numeric data** → treated as numeric type.
- **Numeric columns that contain categorical IDs** → treated as categorical feature.
- **String columns containing English text** → treated as text feature (for natural language processing).

^[data-preparation-for-regression-databricks-on-aws.md]

Semantic type detection is not applied to columns that have a custom [imputation](/concepts/missing-value-imputation.md) method specified. ^[data-preparation-for-regression-databricks-on-aws.md]

### Manual Annotations

You can manually assign a semantic type to a column using the `spark.contentAnnotation.semanticType` metadata key. Valid annotation values are: `categorical`, `numeric`, `datetime`, `text`. To disable detection for a column, use the keyword `native`. ^[data-preparation-for-regression-databricks-on-aws.md]

## Column Selection

By default, AutoML includes all columns in the dataset. You can exclude columns in the UI by unchecking the **Include** checkbox, or in the API using the `exclude_cols` parameter. The prediction target column and the time column (if used for chronological splitting) cannot be excluded. ^[data-preparation-for-regression-databricks-on-aws.md]

## Imputation of Missing Values

AutoML automatically imputes missing values based on the column type and content. In Databricks Runtime 10.4 LTS ML and above, you can override the default imputation method for each column using the **Impute with** dropdown in the UI or the `imputers` parameter in the API. If you specify a non-default imputation method, [Semantic Type Detection](/concepts/semantic-type-detection.md) is not performed. ^[data-preparation-for-regression-databricks-on-aws.md]

## Data Splitting

AutoML supports three data split methods: **random split** (default, 60/20/20), **chronological split** using a time column, and **manual split** using a column with `train`, `validate`, or `test` values (Databricks Runtime 15.3 ML and above). For classification, stratified random sampling preserves label distribution. ^[data-preparation-for-regression-databricks-on-aws.md]

## Sampling Large Datasets

When the dataset is too large to fit in a single worker node’s memory, AutoML automatically samples the data. For regression, it uses PySpark’s `sample` method; for classification, it uses `sampleBy` for stratified sampling to preserve target label distribution. ^[data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- AutoML — Automatic machine learning in Databricks.
- [Regression](/concepts/automl-regress-api.md) — The ML task for which these feature types are documented.
- [Classification](/concepts/data-classification.md) — A related task that shares the same supported feature types.
- Data Preparation — General preprocessing steps before AutoML.
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — AutoML’s automatic type inference.
- [Imputation](/concepts/missing-value-imputation.md) — Handling missing values.

## Sources

- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
