---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b944f35dcac867c9c26af0b2abb21379e21c67f39e3c8f1aac99fd57442b7926
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-data-feature-types-for-automl
    - SDFTFA
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Supported Data Feature Types for AutoML
description: The data types that Databricks AutoML supports for classification, including numeric, boolean, string, timestamps, arrays, and decimal types.
tags:
  - automl
  - databricks
  - data-types
  - classification
timestamp: "2026-06-18T14:59:23.875Z"
---

# Supported Data Feature Types for AutoML

**Supported Data Feature Types for AutoML** defines the column data types that AutoML on Databricks can use as input features for training classification, regression, and forecasting models. Only the feature types listed below are supported; for example, images are _not_ supported. ^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Feature Types

AutoML supports the following feature types:

- **Numeric** – `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, and `DoubleType`
- **Boolean**
- **String** – treated as categorical or English text (see [Semantic Type Detection](/concepts/semantic-type-detection.md))
- **Timestamps** – `TimestampType` and `DateType`
- **ArrayType[Numeric]** – supported in Databricks Runtime 10.4 LTS ML and above
- **DecimalType** – supported in Databricks Runtime 11.3 LTS ML and above

^[data-preparation-for-classification-databricks-on-aws.md]

## Unsupported Feature Types

AutoML does **not** support feature types outside the list above. In particular, images, binary data, and complex nested types (other than `ArrayType[Numeric]`) are not supported as features. ^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- [Impute Missing Values](/concepts/imputation-of-missing-values-in-automl.md) – configuring how null values are handled for supported feature types
- [Column Selection](/concepts/automl-column-selection.md) – choosing which columns (of supported types) to include in training
- [Semantic Type Detection](/concepts/semantic-type-detection.md) – AutoML’s ability to automatically treat strings as dates or numbers, and numeric columns as categorical IDs
- Classification Data Preparation – end-to-end data preparation for classification problems
- Data Preparation for Regression and Forecasting – similar feature type constraints for other problem types

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
