---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a84c9b0e8547b373be1386a177cc19ee685eaeaf0413d9c41aee0922dda753c
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - automl-data-preparation-and-column-configuration
    - Column Configuration and AutoML Data Preparation
    - ADPACC
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Data Preparation and Column Configuration
description: Capabilities to specify which columns AutoML uses for training, configure null value imputation strategies, and control chronological data splitting using a time column.
tags:
  - databricks
  - automl
  - data-preparation
  - feature-engineering
timestamp: "2026-06-18T14:36:15.598Z"
---

# AutoML Data Preparation and Column Configuration

**AutoML Data Preparation and Column Configuration** refers to the settings and options available when setting up an AutoML experiment on Databricks, covering how to select columns, handle missing values, split data, and store the dataset. These settings are exposed both in the AutoML UI and via the classification, regression, and forecasting APIs.

## Column Configuration

When configuring a classification AutoML experiment, after selecting a dataset table, the schema of the table is displayed. Users can specify which columns AutoML should use for training (available in Databricks Runtime 10.3 ML and above). However, the column selected as the **Prediction target** (the label to predict) and the **Time column** (if used for chronological splitting) cannot be removed. ^[classification-with-automl-databricks-on-aws.md]

The prediction target is a required field. Once the dataset is selected, a drop-down lists all columns from the schema for the user to choose the target. ^[classification-with-automl-databricks-on-aws.md]

Additionally, AutoML can augment the original input dataset with existing feature tables from [Feature Store](/concepts/feature-store.md), enabling reuse of curated features across experiments. ^[classification-with-automl-databricks-on-aws.md]

## Handling Missing Values

In Databricks Runtime 10.4 LTS ML and above, users can control how null values in the dataset are imputed by selecting an option from the **Impute with** dropdown. By default, AutoML automatically selects an imputation method based on the column type and content (e.g., mean/mode for numerical columns, most frequent for categorical). ^[classification-with-automl-databricks-on-aws.md]

## Data Splitting

An optional **Time column** can be specified (Databricks Runtime 10.4 LTS ML and above) to split the data for training, validation, and testing in chronological order. This feature is available for classification and regression experiments. When a time column is selected, AutoML ensures that earlier data is used for training and later data for validation/testing, preventing lookahead bias. ^[classification-with-automl-databricks-on-aws.md]

## Advanced Configuration Options

Open the **Advanced Configuration (optional)** section in the UI to access additional parameters:

- **Evaluation metric** – The primary metric used to score the runs (e.g., accuracy, F1, log loss). See the AutoML API reference for available metrics.
- **Exclude training frameworks** – You can exclude certain frameworks from consideration. By default, all supported AutoML algorithms are included.
- **Stopping conditions** – Default stopping conditions vary by experiment type:
    - For forecasting: stop after 120 minutes.
    - For classification and regression (Databricks Runtime 10.4 LTS ML and below): stop after 60 minutes **or** after 200 trials, whichever comes first. From 11.0 ML and above, the number of trials is not used as a stopping condition.
    - Early stopping (10.4 LTS ML and above) stops training and tuning if the validation metric is no longer improving. ^[classification-with-automl-databricks-on-aws.md]

## Data Storage

Databricks recommends leaving the **Data directory** field empty. When empty, the dataset is securely stored as an [MLflow](/concepts/mlflow.md) artifact, inheriting the experiment's access permissions. If a DBFS path is specified instead, the dataset does not inherit those permissions, which can lead to unintended access. ^[classification-with-automl-databricks-on-aws.md]

## Warnings and Alerts

In Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential issues with the dataset, such as unsupported column types or high-cardinality columns. These warnings appear in a dedicated **Warnings** tab on the training page and also after the experiment completes, helping users identify data quality problems before the model is deployed. ^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- [AutoML in Databricks](/concepts/automl-on-databricks.md)
- [Feature Store Integration](/concepts/automl-feature-store-integration.md)
- Imputation Strategies
- Data Splitting for Time Series
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- AutoML API Reference

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
