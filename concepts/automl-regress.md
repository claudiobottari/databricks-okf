---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f0a06c0ced91e2552fc8d5d3d21f341f8bde25fc5bb4c2044da9e49f4f423e3
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-regress
    - AutoML Regression
    - AutoML Python API reference|regress
    - AutoML for Regression
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML regress()
description: Python API method to start an AutoML regression run, using r2 as the default primary metric and supporting similar parameters to classification.
tags:
  - machine-learning
  - regression
  - api
  - databricks
timestamp: "2026-06-19T22:12:01.949Z"
---

# AutoML regress()

**AutoML `regress()`** is a Python API method in the `databricks.automl` module that configures an automated machine learning run to train a regression model. It is part of Databricks' AutoML framework, which automatically trains multiple models and generates trial notebooks for each model. ^[automl-python-api-reference-databricks-on-aws.md]

## Overview

The `databricks.automl.regress` method initiates an AutoML run specifically for regression tasks — predicting a continuous numerical target variable. The method accepts a dataset, target column specification, and various configuration parameters, then returns an `AutoMLSummary` object describing the results. ^[automl-python-api-reference-databricks-on-aws.md]

## Function Signature

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

### Required Parameters

- **`dataset`**: The input data for training. Accepts a PySpark DataFrame, pandas DataFrame, pandas-on-Spark DataFrame, or a string path to a Delta table. ^[automl-python-api-reference-databricks-on-aws.md]
- **`target_col`**: The name of the column containing the target variable to predict. ^[automl-python-api-reference-databricks-on-aws.md]

### Optional Parameters

- **`primary_metric`**: The primary evaluation metric for model selection. Defaults to `"r2"` (R-squared). ^[automl-python-api-reference-databricks-on-aws.md]
- **`data_dir`**: Directory path for storing AutoML output data. ^[automl-python-api-reference-databricks-on-aws.md]
- **`experiment_dir`**: Directory path for the MLflow experiment (available in Databricks Runtime 10.4 LTS ML and above). ^[automl-python-api-reference-databricks-on-aws.md]
- **`experiment_name`**: Name for the MLflow experiment (available in Databricks Runtime 12.1 ML and above). ^[automl-python-api-reference-databricks-on-aws.md]
- **`exclude_cols`**: List of column names to exclude from training (available in Databricks Runtime 10.3 ML and above). ^[automl-python-api-reference-databricks-on-aws.md]
- **`exclude_frameworks`**: List of ML frameworks to exclude from the AutoML search (available in Databricks Runtime 10.3 ML and above). ^[automl-python-api-reference-databricks-on-aws.md]
- **`feature_store_lookups`**: List of dictionaries specifying feature store lookups for feature engineering (available in Databricks Runtime 11.3 LTS ML and above). ^[automl-python-api-reference-databricks-on-aws.md]
- **`imputers`**: Dictionary specifying imputation strategies for missing values (available in Databricks Runtime 10.4 LTS ML and above). ^[automl-python-api-reference-databricks-on-aws.md]
- **`time_col`**: Name of a timestamp column for time-based data splitting. ^[automl-python-api-reference-databricks-on-aws.md]
- **`split_col`**: Column name for custom train/test splitting (available in Databricks Runtime 15.3 ML and above). ^[automl-python-api-reference-databricks-on-aws.md]
- **`sample_weight_col`**: Column name containing sample weights for weighted training (available in Databricks Runtime 15.3 ML and above). ^[automl-python-api-reference-databricks-on-aws.md]
- **`max_trials`**: Maximum number of trials to run. **Deprecated** in Databricks Runtime 10.4 ML and not supported in 11.0 ML and above. Use `timeout_minutes` instead. ^[automl-python-api-reference-databricks-on-aws.md]
- **`timeout_minutes`**: Maximum duration in minutes for the AutoML run. Use this parameter to control run duration instead of `max_trials`. ^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

The method returns an `AutoMLSummary` object, which describes the metrics, parameters, and other details for each trial. This object can be used to load models trained by specific trials. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [AutoML classify()](/concepts/automl-classify.md) — The classification counterpart to `regress()`
- [AutoML forecast()](/concepts/automl-forecast.md) — The forecasting counterpart for time series prediction
- [AutoMLSummary](/concepts/automlsummary.md) — The summary object returned by AutoML methods
- [TrialInfo](/concepts/trialinfo.md) — Summary object for individual AutoML trials
- [MLflow](/concepts/mlflow.md) — The experiment tracking framework used by AutoML
- Automated Machine Learning — The broader concept of automating ML model development

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
