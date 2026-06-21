---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 305cb2423ca372dd005e69d4f89cf1df0b4ecc1d377729e36f806365daa2fb2c
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-data-preparation-settings
    - ADPS
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Data Preparation Settings
description: Configuration options for data preparation in AutoML including column selection, null value imputation, and chronological data splitting
tags:
  - databricks
  - automl
  - data-preparation
timestamp: "2026-06-19T17:43:41.710Z"
---

# AutoML Data Preparation Settings

**AutoML Data Preparation Settings** refer to the configurable options in the Databricks AutoML UI that control how the input dataset is preprocessed before training. These settings allow users to specify which columns to use for training, how to handle missing values, and how to split data for evaluation, ensuring the experiment is tailored to the dataset's characteristics.

## Column Selection

In Databricks Runtime 10.3 ML and above, AutoML allows users to specify which columns should be used for training during experiment setup. The schema of the selected table is displayed, and users can deselect columns that should be excluded from the feature set. The column selected as the **Prediction target** and any column chosen as the **Time column** for chronological splitting cannot be removed from the training set. ^[classification-with-automl-databricks-on-aws.md]

## Impute Missing Values

Starting with Databricks Runtime 10.4 LTS ML, AutoML provides a dropdown menu to choose how null values are imputed for each column. By default, AutoML selects an imputation method automatically based on the column data type and content. Users can override this per‑column default to enforce a specific strategy (e.g., mean, median, or constant imputation). ^[classification-with-automl-databricks-on-aws.md]

## Time Column for Chronological Data Split

In Databricks Runtime 10.4 LTS ML and above, a **Time column** can be specified for classification and regression experiments (and is always required for forecasting experiments). When a time column is provided, AutoML splits the data into training, validation, and test sets in chronological order rather than using a random split. This option is available under the **Advanced Configuration (optional)** section. ^[classification-with-automl-databricks-on-aws.md]

## Automated Warnings for Data Quality

During experiment progress monitoring, AutoML (Databricks Runtime 10.1 ML and above) scans the dataset and displays warnings for potential issues such as unsupported column types or high‑cardinality columns. These warnings are accessible on the **Warnings** tab of the training page or the experiment page after the experiment completes. While these alerts are not exhaustive, they help users identify data preparation concerns early. ^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML – Overview of automated machine learning on Databricks.
- Classification with AutoML – Full setup and configuration for classification experiments.
- Regression with AutoML – Similar data preparation settings for regression tasks.
- Forecasting with AutoML – Chronological data splitting is mandatory for forecasting.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – Required compute for AutoML experiments.
- [MLflow](/concepts/mlflow.md) – The tracking system that stores AutoML experiment results and artifacts.

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
