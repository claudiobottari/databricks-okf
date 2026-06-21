---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d4b1d296f37692aeb9881d1861461642b200322b5314d70d1ae97908c9bc399
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - supported-data-feature-types-in-automl
    - SDFTIA
    - supported data feature types
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Supported Data Feature Types in AutoML
description: The data types supported by AutoML for training, including numeric, Boolean, string, timestamp, array, and decimal types, with exclusions like images.
tags:
  - machine-learning
  - automl
  - data-types
timestamp: "2026-06-19T18:05:07.421Z"
---

# Supported Data Feature Types in AutoML

**Supported Data Feature Types in AutoML** defines which column data types Databricks AutoML can accept as input features for classification and regression tasks. Only the types listed below are eligible; unsupported types (such as images) are automatically excluded or cause an error. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Supported Types

AutoML supports the following Spark and pandas data types as feature columns:

- **Numeric** – `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`
- **Boolean**
- **String** – treated as either a categorical feature or English text, depending on content
- **Timestamps** – `TimestampType`, `DateType`
- **`ArrayType[Numeric]`** – available in Databricks Runtime 10.4 LTS ML and above
- **`DecimalType`** – available in Databricks Runtime 11.3 LTS ML and above

^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

AutoML does **not** support image columns or any other unstructured data type not listed above. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Semantic Type Detection

In Databricks Runtime 9.1 LTS ML and above, AutoML attempts to detect a semantic type that may differ from the raw Spark or pandas type. For example, a string column containing numeric characters is treated as numeric, and a numeric column holding categorical IDs is treated as categorical. This detection enriches the feature representation but does not change the base supported type list. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

For more information on semantic type annotations and how to override detection, see [Semantic Type Detection in AutoML](/concepts/semantic-type-detection.md).

## Relationship to Other Data Preparation Steps

- [Data Imputation in AutoML](/concepts/missing-value-imputation-in-automl.md) – Null values can be imputed per column; custom imputation disables semantic type detection.
- [Column Selection in AutoML](/concepts/column-selection-in-automl.md) – Users can exclude columns from training via the UI or API.
- [Data Splitting in AutoML](/concepts/data-splitting-strategies.md) – Supported feature types apply equally across random, chronological, and manual splits.

## Sources

- data-preparation-for-classification-databricks-on-aws.md
- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
2. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
