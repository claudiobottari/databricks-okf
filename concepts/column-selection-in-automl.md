---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f48b7d0c16ac08ad156cda29692f11429d1d80d17cb8a0574f11689ad276a955
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-selection-in-automl
    - CSIA
    - Column Selection for AutoML
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Column Selection in AutoML
description: The ability to include or exclude specific columns from AutoML training via UI checkboxes or the exclude_cols API parameter.
tags:
  - automl
  - data-preprocessing
  - feature-selection
timestamp: "2026-06-19T18:06:24.109Z"
---

# Column Selection in AutoML

**Column Selection in AutoML** refers to the ability to specify which columns from a dataset are included or excluded when training machine learning models using AutoML. This feature allows users to control the feature set used during model training, improving performance by removing irrelevant or noisy columns. ^[data-preparation-for-regression-databricks-on-aws.md]

## Overview

AutoML provides mechanisms for users to select which columns are used for training. By default, all columns in the dataset are included. However, users can exclude specific columns to focus the model on relevant features and avoid overfitting or unnecessary computation. ^[data-preparation-for-regression-databricks-on-aws.md]

## Supported Column Types

AutoML supports the following feature types for column selection:

- Numeric (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, and `DoubleType`)
- Boolean
- String (categorical or English text)
- Timestamps (`TimestampType`, `DateType`)
- `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above)
- `DecimalType` (Databricks Runtime 11.3 LTS ML and above)

^[data-preparation-for-regression-databricks-on-aws.md]

## How to Select Columns

### Using the AutoML UI

In the AutoML UI, you can exclude a column by unchecking it in the **Include** column of the table schema view. This is available starting in Databricks Runtime 10.3 ML and above. ^[data-preparation-for-regression-databricks-on-aws.md]

### Using the AutoML API

When using the AutoML Python API, you can specify which columns to exclude using the `exclude_cols` parameter. For more details, refer to the [AutoML Python API Reference](/concepts/automl-python-api.md). ^[data-preparation-for-regression-databricks-on-aws.md]

## Restrictions

Certain columns cannot be excluded from training:

- The column selected as the **prediction target** cannot be dropped.
- The column selected as the **time column** (for chronological data splitting) cannot be dropped.

^[data-preparation-for-regression-databricks-on-aws.md]

## Default Behavior

By default, all columns in the dataset are included for training. Users must explicitly exclude columns they do not want to use. ^[data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- Data Preparation for Regression — Broader data preparation workflows for regression problems
- [AutoML Python API Reference](/concepts/automl-python-api.md) — API documentation for configuring AutoML experiments
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — AutoML's automatic detection of column semantic types
- [Impute Missing Values](/concepts/imputation-of-missing-values-in-automl.md) — Handling null values in training data
- [Data Splitting Strategies](/concepts/data-splitting-strategies.md) — Methods for dividing data into train, validation, and test sets

## Sources

- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
