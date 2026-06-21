---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 640d7a9835274d3481117e4f1fbbeca4fcb7bed0636d09fc5f1a981061659cf4
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - common-automl-parameters
    - CAP
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: Common AutoML Parameters
description: Shared configuration parameters across classify, regress, and forecast methods including dataset, target_col, primary_metric, timeout_minutes, exclude_cols, exclude_frameworks, and feature_store_lookups.
tags:
  - AutoML
  - configuration
  - Databricks
timestamp: "2026-06-19T14:07:53.680Z"
---

## Common AutoML Parameters

**Common AutoML Parameters** refers to the set of configuration inputs shared across the `databricks.automl.classify`, `databricks.automl.regress`, and `databricks.automl.forecast` methods in the Databricks AutoML Python API. These parameters control the dataset, target variable, evaluation metric, and runtime behavior of an automated machine learning run. ^[automl-python-api-reference-databricks-on-aws.md]

## Shared Parameters

The following table lists parameters that appear in at least two of the three AutoML methods (classify, regress, forecast). Parameters specific to a single method (e.g., `pos_label` for classify, `frequency` and `horizon` for forecast) are described separately.

| Parameter | Description | Used by |
|-----------|-------------|---------|
| `dataset` | Input data. Accepts a PySpark DataFrame, pandas DataFrame, pandas-on-Spark DataFrame, or a path string. | classify, regress, forecast |
| `target_col` | Name of the column to predict. | classify, regress, forecast |
| `primary_metric` | Evaluation metric to optimize during model selection. Defaults differ: `"f1"` for classification, `"r2"` for regression, `"smape"` for forecasting. | classify, regress, forecast |
| `timeout_minutes` | Maximum duration of the AutoML run (in minutes). Replaces deprecated `max_trials` from Databricks Runtime 11.0 ML onwards. | classify, regress, forecast |
| `data_dir` | Path to a DBFS directory for storing intermediate data artifacts. | classify, regress, forecast |
| `experiment_dir` | Path to an existing directory under which an MLflow experiment is created or reused (Databricks Runtime 10.4 LTS ML and above). | classify, regress, forecast |
| `experiment_name` | Full name of an MLflow experiment to use. If specified, `experiment_dir` is ignored (Databricks Runtime 12.1 ML and above). | classify, regress, forecast |
| `exclude_cols` | List of column names to exclude from training (Databricks Runtime 10.3 ML and above). | classify, regress |
| `exclude_frameworks` | List of ML frameworks to skip during model training (Databricks Runtime 10.3 ML and above). | classify, regress, forecast |
| `feature_store_lookups` | List of dictionaries specifying Feature Store lookups for enriching the training dataset (Databricks Runtime 11.3 LTS ML and above). | classify, regress, forecast |
| `imputers` | Dictionary specifying imputation strategies for missing values. Each key is a column name, value is an imputer type string or a dictionary with parameters (Databricks Runtime 10.4 LTS ML and above). | classify, regress |
| `time_col` | Name of the column containing time stamps. Required for forecasting; optional in classify and regress. | classify, regress, forecast |
| `split_col` | Column used to define a custom train/validation split (Databricks Runtime 15.3 ML and above). | classify, regress |
| `sample_weight_col` | Column containing sample weights for weighted training (Databricks Runtime 15.4 ML and above for classify; 15.3 ML and above for regress; 16.0 ML and above for forecast). | classify, regress, forecast |

^[automl-python-api-reference-databricks-on-aws.md]

## Deprecated Parameters

- **`max_trials`** : Deprecated in Databricks Runtime 10.4 ML and not supported in Databricks Runtime 11.0 ML and above. Use `timeout_minutes` to control the duration of an AutoML run. ^[automl-python-api-reference-databricks-on-aws.md]

## Method-Specific Parameters

### Classification-only

- **`pos_label`** : The positive class label for binary classification. Accepts an integer, boolean, or string (Databricks Runtime 11.1 ML and above). ^[automl-python-api-reference-databricks-on-aws.md]

### Forecasting-only

- **`country_code`** : Optional ISO 3166-1 alpha-2 country code for holiday effect modeling in Prophet-based models (Databricks Runtime 12.0 ML and above). Default `"US"`. ^[automl-python-api-reference-databricks-on-aws.md]
- **`frequency`** : Time series frequency string (e.g., `"D"` for daily, `"H"` for hourly). The time series must have a regular frequency; missing timestamps are forward-filled. Default `"D"`. ^[automl-python-api-reference-databricks-on-aws.md]
- **`horizon`** : Number of time steps to forecast into the future. Default `1`. ^[automl-python-api-reference-databricks-on-aws.md]
- **`identity_col`** : Column or list of columns that uniquely identify a time series. Required when the dataset contains multiple series. ^[automl-python-api-reference-databricks-on-aws.md]
- **`output_database`** : Name of a database where forecast results are saved (Databricks Runtime 10.5 ML and above). ^[automl-python-api-reference-databricks-on-aws.md]

## Return Type

All three methods return an `AutoMLSummary` object, which contains metrics, parameters, and a `trials` list of `TrialInfo` objects, each representing a trained model trial. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- AutoML — Overview of automated machine learning on Databricks
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Tracking and organizing AutoML runs
- Time Series Forecasting with AutoML — Parameters for `forecast`
- [Feature Store Integration](/concepts/automl-feature-store-integration.md) — Using `feature_store_lookups`
- Imputation Strategies — Handling missing values with `imputers`

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
