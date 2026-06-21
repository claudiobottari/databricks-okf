---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b8c465f47dd3fcfecaaf8ec927fecc1325c6de417529c821c8b0bc93511ed1f
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-supported-feature-types
    - ASFT
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: AutoML Supported Feature Types
description: The specific Spark data types supported as features in Databricks AutoML classification, including numeric, boolean, string, timestamps, arrays, and decimal types.
tags:
  - databricks
  - automl
  - data-types
  - feature-engineering
timestamp: "2026-06-19T09:43:10.492Z"
---

# AutoML Supported Feature Types

**AutoML Supported Feature Types** describes the set of column data types that [Databricks AutoML](/concepts/databricks-automl.md) can use as input features for classification and regression training. AutoML automatically detects and processes these feature types during experiment setup, and you can override the detected semantic type using annotations. ^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Data Types

The following Spark and pandas data types are supported as features in AutoML experiments. Types not listed in this table — such as images — are not supported. ^[data-preparation-for-classification-databricks-on-aws.md]

| Feature Type | Underlying Spark Types |
|--------------|------------------------|
| **Numeric** | `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType` |
| **Boolean** | `BooleanType` |
| **String** | `StringType` (treated as categorical or English text depending on content) |
| **Timestamp** | `TimestampType`, `DateType` |
| **ArrayType[Numeric]** | `ArrayType` with numeric element type (Databricks Runtime 10.4 LTS ML and above) |
| **DecimalType** | `DecimalType` (Databricks Runtime 11.3 LTS ML and above) |

All listed types are eligible for use as predictor columns in classification and regression models. Unsupported types are automatically excluded from training. ^[data-preparation-for-classification-databricks-on-aws.md]

## Semantic Type Detection

AutoML runs semantic type detection to refine how columns are interpreted, unless a custom imputation method has been set for the column. The following adjustments are applied based on column content: ^[data-preparation-for-classification-databricks-on-aws.md]

- String and integer columns that contain date or timestamp values are treated as timestamps.
- String columns that represent numeric data are treated as numeric.
- Numeric columns that contain categorical IDs are treated as categorical features (Databricks Runtime 10.1 ML and above).
- String columns that contain English text are treated as text features (Databricks Runtime 10.1 ML and above).

You can manually override the semantic type using annotations with values `categorical`, `numeric`, `datetime`, or `text`. To disable detection entirely on a column, use the special annotation `native`. ^[data-preparation-for-classification-databricks-on-aws.md]

## Imputation

AutoML imputes missing values for supported feature types. The default imputation method depends on the column type and content; you can specify a custom method in the UI or via the API (Databricks Runtime 10.4 LTS ML and above). If a non-default imputation method is specified, semantic type detection is not performed for that column. ^[data-preparation-for-classification-databricks-on-aws.md]

## Column Selection

You can exclude columns from training using the `exclude_cols` parameter or by unchecking them in the UI (Databricks Runtime 10.3 ML and above). The prediction target column and the time column (if used for chronological splitting) cannot be excluded. ^[data-preparation-for-classification-databricks-on-aws.md]

## Imbalanced Dataset Support (Classification)

In Databricks Runtime 11.3 LTS ML and above, if AutoML detects that a dataset is imbalanced, it reduces the imbalance of the training dataset by downsampling the major class(es) and adding class weights. AutoML only balances the training dataset and does not balance the test and validation datasets, ensuring that model performance is evaluated on the non-enriched dataset with the true input class distribution. Class weights are inversely related to the degree of downsampling, and AutoML uses these weights in model training to appropriately weight samples from each class. ^[data-preparation-for-classification-databricks-on-aws.md]

## Data Splitting

AutoML splits data into training, validation, and test sets. Three methods are available:

- **Random split** (default): 60% train, 20% validation, 20% test. For classification, a stratified random split ensures each class is proportionally represented.
- **Chronological split** (Databricks Runtime 10.4 LTS ML and above): Uses a time column to create splits based on temporal order (earliest data for training, latest for testing).
- **Manual split** (Databricks Runtime 15.3 ML and above): Uses a designated split column with values `train`, `validate`, or `test`.

^[data-preparation-for-classification-databricks-on-aws.md]

## Sampling Large Datasets

AutoML automatically estimates the memory required to load and train your dataset and samples the dataset if necessary. For classification problems, AutoML uses the PySpark `sampleBy` method for stratified sampling to preserve the target label distribution. ^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- [AutoML Classification](/concepts/automl-classification-classify.md) — The classification training workflow that uses these feature types
- [AutoML Regression](/concepts/automl-regress.md) — Regression experiments that support the same feature types
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — How AutoML refines feature interpretation
- [Data Preparation for AutoML](/concepts/automl-data-preparation.md) — Broader data preparation steps including imputation and splitting
- Categorical Features — How string and numeric ID columns are handled
- Text Features — How text columns are processed in AutoML

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
