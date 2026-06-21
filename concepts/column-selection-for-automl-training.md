---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d04103148f7cb95e035e6fef0cc2313e511d42a466207edcdf191636ecac4c1
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-selection-for-automl-training
    - CSFAT
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Column Selection for AutoML Training
description: Ability to specify which columns AutoML should use for training by excluding columns via the UI or the exclude_cols API parameter; the prediction target and time column cannot be dropped.
tags:
  - automl
  - feature-selection
  - data-preparation
timestamp: "2026-06-18T15:00:24.770Z"
---

# Column Selection for AutoML Training

**Column Selection for AutoML Training** refers to the ability to specify which columns the AutoML process should use when training regression, classification, or forecasting models. This feature allows practitioners to exclude irrelevant or problematic columns from the training pipeline without modifying the source dataset.

## Overview

Starting in Databricks Runtime 10.3 ML and above, AutoML supports explicit column selection for training. By default, all columns in the input dataset are included in the training process. Users can exclude columns they do not want AutoML to use. ^[data-preparation-for-regression-databricks-on-aws.md]

Columns that are excluded from training are simply omitted from the feature set passed to the model training trials. They are **not** dropped from the original dataset.

## Configuring Column Selection

### Using the UI

In the AutoML experiment setup UI, each column in the data schema has an **Include** checkbox. To exclude a column, uncheck its checkbox. ^[data-preparation-for-regression-databricks-on-aws.md]

### Using the API

When using the AutoML Python API, pass the `exclude_cols` parameter to specify which columns to exclude. See the [AutoML Python API Reference](/concepts/automl-python-api.md) for detailed usage. ^[data-preparation-for-regression-databricks-on-aws.md]

## Restrictions

There are two columns that cannot be excluded from training:

- **The prediction target column**: The column specified as the value to predict must always be included.
- **The time column** (if used for chronological splits): When using a [chronological data split](/concepts/chronological-data-splitting-in-automl.md) based on a time column, that column cannot be excluded. ^[data-preparation-for-regression-databricks-on-aws.md]

If you attempt to exclude these protected columns, AutoML will raise an error.

## Use Cases

Column selection is useful in several scenarios:

- **Removing redundant or highly correlated features** to reduce noise and improve model stability.
- **Excluding identifier columns** (e.g., user IDs, transaction IDs) that should not influence predictions.
- **Omitting derived columns** that leak information from the target variable.
- **Managing memory or compute constraints** by reducing the feature dimensionality for large datasets.
- **Testing feature importance** by systematically excluding candidate features and comparing model performance.

## Relationship to Other Data Preparation Features

Column selection is part of a broader set of data preparation controls in AutoML, which also includes:

- [Impute Missing Values for AutoML](/concepts/imputation-of-missing-values-in-automl.md) — Specify how null values are handled per column.
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — AutoML can detect and treat columns as categorical, numeric, datetime, or text features.
- [Data Splitting Strategies](/concepts/data-splitting-strategies.md) — Control how data is divided into training, validation, and test sets.

## Implementation Notes

- If you specify a non-default imputation method for any column, AutoML does **not** perform semantic type detection on that column. However, column selection works independently from imputation settings.
- Column selection operates at the feature level and does not affect the row-level sampling that AutoML performs for large dataset sampling.

## Related Concepts

- [AutoML Training on Databricks](/concepts/automl-on-databricks.md)
- Feature Engineering for AutoML
- Data Preparation for Regression
- [Data Preparation for Classification](/concepts/automl-data-preparation-for-classification.md)

## Sources

- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
