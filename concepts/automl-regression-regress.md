---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e21b97c00b9efc95b555186a2fdde81dd0f74d7b300b43e9d9a8458cb9f7afa3
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-regression-regress
    - AR(
    - AutoML Regress (regress)
    - AutoML Regress (regress)|regression
    - AutoML Regression UI Workflow
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
    - file: automl-python-api-reference-databricks- on-aws.md
title: AutoML Regression (regress)
description: Method to configure and train regression models via AutoML, with primary_metric defaulting to r2 and supporting similar parameters to classify
tags:
  - automl
  - regression
  - machine-learning
timestamp: "2026-06-19T09:08:02.597Z"
---

# AutoML Regression (regress)

**AutoML Regression (regress)** is a method in the Databricks AutoML Python API that configures and runs an automated machine learning workflow to train regression models. Regression is a supervised learning task where the goal is to predict a continuous numeric value based on input features.

## Overview

The `databricks.automl.regress` method automates the model training process for regression problems. It trains a set of candidate models and generates a trial notebook for each model, allowing users to inspect, modify, and reproduce the training logic. The method returns an [AutoMLSummary](/concepts/automlsummary.md) object containing metrics, parameters, and other details for each trial. ^[automl-python-api-reference-databricks-on-aws.md]

## Method Signature

```python
databricks.automl.regress(
  dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
  *,
  target_col: str,
  primary_metric: str = "r2",
  data_dir: Optional[str] = None,
  experiment_dir: Optional[str] = None,
  experiment_name: Optional[str] = None,
  exclude_cols: Optional[List[str]] = None,
  exclude_frameworks: Optional[List[str]] = None,
  feature_store_lookups: Optional[List[Dict]] = None,
  imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None,
  time_col: Optional[str] = None,
  split_col: Optional[str] = None,
  sample_weight_col: Optional[str] = None,
  max_trials: Optional[int] = None,
  timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

^[automl-python-api-reference-databricks-on-aws.md]

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `dataset` | Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str] | The input dataset for training. Can be a Spark DataFrame, pandas DataFrame, pandas-on-Spark DataFrame, or a path string to a data source. |
| `target_col` | str | The name of the column containing the target variable to predict. |
| `primary_metric` | str | The primary evaluation metric for model selection. Defaults to `"r2"`. |
| `data_dir` | Optional[str] | Directory path for storing AutoML-generated data artifacts. |
| `experiment_dir` | Optional[str] | Directory for the MLflow experiment (Databricks Runtime 10.4 LTS ML and above). |
| `experiment_name` | Optional[str] | Name for the MLflow experiment (Databricks Runtime 12.1 ML and above). |
| `exclude_cols` | Optional[List[str]] | Columns to exclude from training features (Databricks Runtime 10.3 ML and above). |
| `exclude_frameworks` | Optional[List[str]] | Machine learning frameworks to exclude from the search (Databricks Runtime 10.3 ML and above). |
| `feature_store_lookups` | Optional[List[Dict]] | Feature store lookups for enriching the dataset (Databricks Runtime 11.3 LTS ML and above). |
| `imputers` | Optional[Dict[str, Union[str, Dict[str, Any]]]] | Custom imputation strategies for missing values (Databricks Runtime 10.4 LTS ML and above). |
| `time_col` | Optional[str] | The name of a time column if the data has a temporal component. |
| `split_col` | Optional[str] | Column name for custom train/test split assignment (Databricks Runtime 15.3 ML and above). |
| `sample_weight_col` | Optional[str] | Column name containing sample weights (Databricks Runtime 15.3 ML and above). |
| `max_trials` | Optional[int] | **Deprecated** — Maximum number of trials. Use `timeout_minutes` instead. Supported only in Databricks Runtime 10.5 ML and below. |
| `timeout_minutes` | Optional[int] | Maximum duration of the AutoML run in minutes. |

^[automl-python-api-reference-databricks- on-aws.md]

## Notes

- The `max_trials` parameter is deprecated in Databricks Runtime 10.4 ML and is not supported in Databricks Runtime 11.0 ML and above. Users should control the duration of an AutoML run using the `timeout_minutes` parameter instead. ^[automl-python-api-reference-databricks-on-aws.md]
- Each method call trains a set of models and generates trial notebooks that document the training process for each model. These notebooks can be imported and modified for further experimentation. ^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

The method returns an [AutoMLSummary](/concepts/automlsummary.md) object, which contains:

- Metrics and parameters for each trial
- Methods for loading trained models
- Artifact URIs for importing trial notebooks

Each individual trial is represented by a [TrialInfo](/concepts/trialinfo.md) object, which has methods to load the model generated for that trial. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [AutoML Classification (classify)](/concepts/automl-classification-classify.md) — The counterpart method for classification tasks
- [AutoML Forecasting (forecast)](/concepts/automl-forecasting-forecast.md) — Time series forecasting with AutoML
- [AutoMLSummary](/concepts/automlsummary.md) — The summary object returned by AutoML methods
- [TrialInfo](/concepts/trialinfo.md) — Per-trial summary containing metrics and model loading capabilities
- [ImportNotebookResult](/concepts/importnotebookresult.md) — Result object from importing trial notebooks
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The experiment tracking system used by AutoML
- [Feature Store](/concepts/feature-store.md) — Feature store lookups for enriching training data

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
2. automl-python-api-reference-databricks- on-aws.md
