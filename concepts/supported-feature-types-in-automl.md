---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e810580be72897588bff16e65e7f3f0ad1fd90130d3d54b23039c8b6dee7a42f
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-feature-types-in-automl
    - SFTIA
    - Feature Types in AutoML
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Supported Feature Types in AutoML
description: The set of data types (numeric, boolean, string, timestamp, array, decimal) that AutoML supports for classification feature columns.
tags:
  - data-types
  - feature-types
  - automl
  - databricks
timestamp: "2026-06-19T14:41:36.484Z"
---

#Supported Feature Types in AutoML

**Supported Feature Types in AutoML** defines the specific data types that [Databricks AutoML](/concepts/databricks-automl.md) can process when training classification models (the same list applies to other problem types). Only the feature types listed below are accepted; unsupported types, such as images, are not supported. ^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Feature Types

The following feature types are supported for use in AutoML experiments: ^[data-preparation-for-classification-databricks-on-aws.md]

- **Numeric** — `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, and `DoubleType`
- **Boolean**
- **String** — treated as categorical or English text
- **Timestamps** — `TimestampType` and `DateType`
- **ArrayType[Numeric]** — supported in Databricks Runtime 10.4 LTS ML and above
- **DecimalType** — supported in Databricks Runtime 11.3 LTS ML and above

## Semantic Type Detection

With Databricks Runtime 9.1 LTS ML and above, AutoML attempts to detect semantic types that differ from the raw Spark or pandas data type. AutoML makes the following adjustments: ^[data-preparation-for-classification-databricks-on-aws.md]

- String and integer columns representing date or timestamp data are treated as a timestamp type.
- String columns that represent numeric data are treated as a numeric type.

With Databricks Runtime 10.1 ML and above, AutoML also makes these additional adjustments: ^[data-preparation-for-classification-databricks-on-aws.md]

- Numeric columns that contain categorical IDs are treated as a categorical feature.
- String columns that contain English text are treated as a text feature.

Semantic type detection is not performed on columns that have custom imputation methods specified. ^[data-preparation-for-classification-databricks-on-aws.md]

### Semantic Type Annotations

With Databricks Runtime 10.1 ML and above, you can manually control the assigned semantic type by placing a semantic type annotation on a column. The accepted annotation values are: ^[data-preparation-for-classification-databricks-on-aws.md]

- `categorical` — column contains categorical values
- `numeric` — column contains numeric values
- `datetime` — column contains timestamp values
- `text` — string column contains English text

To disable semantic type detection on a column, use the special keyword annotation `native`. ^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- AutoML API Reference — Configuring feature types and other settings programmatically
- [Data Preparation for Classification](/concepts/automl-data-preparation-for-classification.md) — Full guide on preparing data for classification tasks
- [Impute Missing Values in AutoML](/concepts/imputation-of-missing-values-in-automl.md) — Handling null values during training
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — Automatic detection of semantic types during AutoML experiments
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — ML-specific runtime versions that support AutoML features

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
