---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 738a4a08fa857d31751cec1ce65a25d609085f75e86295745f0307101538569f
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-advanced-configuration-parameters
    - AACP
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Advanced Configuration Parameters
description: Configurable options for AutoML experiments including evaluation metrics, training framework exclusions, stopping conditions, time-based data splitting, and data directory security.
tags:
  - databricks
  - automl
  - configuration
  - hyperparameters
timestamp: "2026-06-18T14:35:52.457Z"
---

# AutoML Advanced Configuration Parameters

**AutoML Advanced Configuration Parameters** are optional settings that fine‑tune how an AutoML experiment runs. They control the evaluation metric, the set of training frameworks considered, stopping criteria, data splitting strategy, and other experiment‑specific behaviors. All parameters are accessible through the **Advanced Configuration (optional)** section of the AutoML UI.^[classification-with-automl-databricks-on-aws.md]

## Evaluation Metric

The evaluation metric is the primary metric used to score each trial run. The choice of metric determines which model is reported as the best at the end of the experiment. Available metrics depend on the problem type (classification, regression, or forecasting). For details, see the AutoML API reference.^[classification-with-automl-databricks-on-aws.md]

## Excluded Training Frameworks

By default, AutoML trains models using all algorithms listed under AutoML algorithms. In Databricks Runtime 10.4 LTS ML and above, you can exclude specific frameworks from consideration. This is useful when you already know that certain algorithm families are unsuitable for your dataset or performance requirements.^[classification-with-automl-databricks-on-aws.md]

## Stopping Conditions

The stopping conditions define when AutoML should stop training and tuning models. Defaults vary by problem type:

| Problem Type | Default Stopping Condition |
|--------------|----------------------------|
| Classification / Regression (Databricks Runtime 10.4 LTS ML and below) | Stop after 60 minutes **or** after completing 200 trials, whichever occurs first. |
| Classification / Regression (Databricks Runtime 11.0 ML and above) | The number of trials is no longer used as a stopping condition. |
| Forecasting | Stop after 120 minutes. |

In Databricks Runtime 10.4 LTS ML and above, classification and regression experiments also incorporate early stopping: training and tuning halt automatically if the validation metric ceases to improve.^[classification-with-automl-databricks-on-aws.md]

## Time Column for Data Splitting

In Databricks Runtime 10.4 LTS ML and above, you can select a time column to split the data into training, validation, and testing sets in chronological order. This option applies only to classification and regression experiments. When enabled, AutoML uses the time column to ensure that future data is never used to predict the past.^[classification-with-automl-databricks-on-aws.md]

## Data Directory

The **Data directory** field controls where the input dataset is stored. Databricks recommends leaving this field empty, which triggers the default behavior of securely storing the dataset as an [MLflow](/concepts/mlflow.md) artifact. If you specify a DBFS path, the dataset does not inherit the AutoML experiment’s access permissions, which can lead to unintended exposure.^[classification-with-automl-databricks-on-aws.md]

## Column Selection and Null Imputation

Two additional settings, while not in the advanced configuration panel, are accessible during experiment setup in the **Dataset** section:

- **Column selection** (Databricks Runtime 10.3 ML and above): Specify which columns AutoML should use for training. The prediction target column and the time column (if used for splitting) cannot be removed.
- **Null imputation** (Databricks Runtime 10.4 LTS ML and above): Choose how null values are imputed from the **Impute with** dropdown. By default, AutoML selects an imputation method based on the column type and content.^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- Classification with AutoML – Overview of classification experiments.
- Regression with AutoML – Regression experiment setup and configuration.
- Forecasting with AutoML – How to run forecasting experiments.
- [AutoML Data Preparation](/concepts/automl-data-preparation.md) – Column selection, null imputation, and time‑based splits.
- AutoML API Reference – Full specification of metrics and parameters.

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
