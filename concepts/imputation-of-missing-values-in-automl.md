---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53a4fdba80d6867ad9c9eefdb5b5cebe4fbdfbf6a90ddf435a7cbfa88c6c60dc
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - imputation-of-missing-values-in-automl
    - IOMVIA
    - Imputation of Missing Values
    - Impute Missing Values in AutoML
    - Impute missing values in AutoML
    - Impute Missing Values
    - Impute Missing Values for AutoML
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Imputation of Missing Values in AutoML
description: How AutoML handles null value imputation, including default behavior and custom imputation methods configurable via UI or API.
tags:
  - machine-learning
  - automl
  - data-cleaning
timestamp: "2026-06-19T18:05:15.064Z"
---

# Imputation of Missing Values in AutoML

**Imputation of Missing Values in AutoML** refers to the process by which Databricks AutoML handles null or missing values in training data. AutoML provides configurable imputation strategies that can be specified per column, with default methods selected based on column type and content. ^[data-preparation-for-classification-databricks-on-aws.md]

## Overview

During data preparation for classification (and other AutoML tasks), null values must be addressed before model training. AutoML automatically selects an imputation method based on the column's data type and content. Users can override these defaults to specify custom imputation strategies for individual columns. ^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Since

Custom imputation specification is available in Databricks Runtime 10.4 LTS ML and above. Earlier versions use default imputation only. ^[data-preparation-for-classification-databricks-on-aws.md]

## Configuring Imputation

### In the UI

During experiment setup in the AutoML UI, navigate to the table schema view. Each column displays an **Impute with** drop-down menu where you can select the desired imputation method. ^[data-preparation-for-classification-databricks-on-aws.md]

### In the API

When using the AutoML API, specify imputation strategies using the `imputers` parameter. For full API details, see the [AutoML Python API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference). ^[data-preparation-for-classification-databricks-on-aws.md]

## Effect on Semantic Type Detection

AutoML does **not** perform semantic type detection for columns that have a custom (non-default) imputation method specified. If you specify a custom imputation method, any automatic detection of semantic types (such as treating numeric strings as numeric, or treating categorical IDs as categorical) is skipped for that column. ^[data-preparation-for-classification-databricks-on-aws.md]

## Default Imputation Behavior

By default, AutoML selects an imputation method based on the column type and content. The specific default strategies depend on:

- **Numeric columns** (ByteType, ShortType, IntegerType, LongType, FloatType, DoubleType, DecimalType): Typically imputed with the mean or median value.
- **Boolean columns**: Imputed with the mode (most frequent value).
- **String columns**: Imputed with the mode or treated as a missing category.
- **Timestamp columns** (TimestampType, DateType): Imputed with the mode or a forward-fill strategy.
- **ArrayType[Numeric]** columns: Imputed per-element or dropped depending on configuration.

^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- [Data Preparation for Classification](/concepts/automl-data-preparation-for-classification.md) — Full overview of AutoML data preparation steps.
- AutoML API Reference — Programmatic control of AutoML experiments.
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — AutoML's automatic detection of column types beyond raw schema.
- [Column Selection in AutoML](/concepts/column-selection-in-automl.md) — Including and excluding columns from training.
- [Imbalanced Dataset Handling](/concepts/imbalanced-dataset-handling.md) — AutoML's approach to class imbalance during classification.
- [Split Strategies in AutoML](/concepts/data-splitting-strategies.md) — How AutoML divides data into train/validation/test sets.

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
