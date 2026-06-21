---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36eee1ee45bbddec9ee1e5ed54b0c9ee6b54b92d9f587458298dcb334cec6459
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-advanced-configuration-options
    - AACO
  citations:
    - file: classification-with-automl-databricks-on-aws.md
    - file: classification-with-automl-databricks-on-aws.md#advanced-configurations
title: AutoML Advanced Configuration Options
description: Optional parameters for AutoML classification experiments including evaluation metrics, framework exclusion, stopping conditions, and time column splitting
tags:
  - databricks
  - automl
  - configuration
timestamp: "2026-06-19T17:43:36.278Z"
---

# AutoML Advanced Configuration Options

Databricks AutoML provides several advanced configuration parameters that let you fine-tune the experiment setup for classification, regression, and forecasting tasks. These options are available in the **Advanced Configuration (optional)** section of the AutoML UI and are also exposed in the corresponding API. ^[classification-with-automl-databricks-on-aws.md]

## Evaluation Metric

You can specify the **primary metric** used to score and rank trial runs. The available metrics vary by problem type. If not set, AutoML uses a default metric appropriate for the task (e.g., log loss for classification, RMSE for regression). The full list of supported metrics is documented in the AutoML API Reference. ^[classification-with-automl-databricks-on-aws.md#advanced-configurations]

## Exclude Training Frameworks

In Databricks Runtime 10.4 LTS ML and above, you can exclude certain training frameworks from consideration. By default, AutoML trains models using all frameworks listed under AutoML algorithms. Excluding specific frameworks can reduce experiment time or focus on preferred model families. ^[classification-with-automl-databricks-on-aws.md#advanced-configurations]

## Stopping Conditions

You can adjust the **stopping conditions** that determine when the experiment ends. Defaults are:

- **Forecasting experiments**: stop after **120 minutes**.
- **Classification and regression experiments** (Databricks Runtime 10.4 LTS ML and below): stop after **60 minutes** or **200 trials**, whichever happens first.
- **Classification and regression experiments** (Databricks Runtime 11.0 ML and above): the number of trials is **not used** as a stopping condition; only the time limit applies.
- In Databricks Runtime 10.4 LTS ML and above, AutoML incorporates **early stopping**: training and tuning stops when the validation metric is no longer improving.

^[classification-with-automl-databricks-on-aws.md#advanced-configurations]

## Time Column for Chronological Split

In Databricks Runtime 10.4 LTS ML and above, you can select a **time column** to split the data chronologically for training, validation, and testing. This applies only to classification and regression experiments. When set, AutoML uses the time column to order rows, ensuring that all training data comes from earlier time periods than the validation and test sets. ^[classification-with-automl-databricks-on-aws.md#advanced-configurations]

## Data Directory

Databricks recommends leaving the **Data directory** field empty. When empty, AutoML stores the dataset securely as an [MLflow](/concepts/mlflow.md) artifact associated with the experiment. If you specify a DBFS path, the dataset does not inherit the AutoML experiment's access permissions, which can lead to security gaps. ^[classification-with-automl-databricks-on-aws.md#advanced-configurations]

## Column Selection and Null Imputation

Although not part of the standard **Advanced Configuration** section, two data preparation options are also configurable during experiment setup:

- **Column selection** (Databricks Runtime 10.3 ML and above): you can specify which columns AutoML should use for training. You cannot remove the prediction target column or the time column (if set).
- **Null value imputation** (Databricks Runtime 10.4 LTS ML and above): choose how missing values are imputed from the **Impute with** dropdown. By default, AutoML selects an imputation method based on column type and content.

^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML — Overview of automated machine learning on Databricks
- Classification with AutoML — Problem-specific guide
- Regression with AutoML — Problem-specific guide
- Forecasting with AutoML — Problem-specific guide (classic compute)
- AutoML API Reference — Full list of parameters and metrics
- [MLflow](/concepts/mlflow.md) — Experiment tracking and artifact storage
- [Feature Store](/concepts/feature-store.md) — Augmenting datasets with feature tables
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — Compute requirements for AutoML

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
2. classification-with-automl-databricks-on-aws.md#advanced-configurations
