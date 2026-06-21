---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c1bfa852b01d93bc0950d1c1fbe4aef3978b1fc2f5ec3ab7d17a0c003eafd89
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-classification-classify
    - AC(
    - AutoML Classification API
    - AutoML Classify (classify)
    - auto-ml-classification|classification
    - AutoML API for classification
    - AutoML Classification
    - AutoML Classify (classify)|classification
    - AutoML classification training
    - AutoML for Classification
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML Classification (classify)
description: Method to configure and train classification models via AutoML, supporting parameters like target_col, primary_metric, timeout_minutes, and pos_label
tags:
  - automl
  - classification
  - machine-learning
timestamp: "2026-06-19T09:07:14.025Z"
---

# AutoML Classification (classify)

**AutoML Classification (classify)** is a method provided by the Databricks AutoML Python API that automatically trains and evaluates machine learning models for classification tasks. It is part of the AutoML suite, which also includes [AutoML Regression (regress)](/concepts/automl-regression-regress.md) and [AutoML Forecasting (forecast)](/concepts/automl-forecasting-forecast.md). The `databricks.automl.classify` method accepts a dataset and a target column, then runs a set of trials, each of which produces a trained model and a corresponding trial notebook. The method returns an [AutoMLSummary](/concepts/automlsummary.md) object containing metrics, parameters, and trial details. ^[automl-python-api-reference-databricks-on-aws.md]

## API Reference

The function signature is as follows:

```python
databricks.automl.classify(
    dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
    *,
    target_col: str,
    primary_metric: str = "f1",
    data_dir: Optional[str] = None,
    experiment_dir: Optional[str] = None,          # DBR 10.4 LTS ML and above
    experiment_name: Optional[str] = None,         # DBR 12.1 ML and above
    exclude_cols: Optional[List[str]] = None,      # DBR 10.3 ML and above
    exclude_frameworks: Optional[List[str]] = None, # DBR 10.3 ML and above
    feature_store_lookups: Optional[List[Dict]] = None, # DBR 11.3 LTS ML and above
    imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None, # DBR 10.4 LTS ML and above
    pos_label: Optional[Union[int, bool, str]] = None, # DBR 11.1 ML and above
    time_col: Optional[str] = None,
    split_col: Optional[str] = None,               # DBR 15.3 ML and above
    sample_weight_col: Optional[str] = None,       # DBR 15.4 ML and above
    max_trials: Optional[int] = None,              # DBR 10.5 ML and below (deprecated)
    timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

^[automl-python-api-reference-databricks-on-aws.md]

## Parameters

The `classify` method accepts the following key parameters:

- **`dataset`** – The training data. Can be a Spark DataFrame (`pyspark.sql.DataFrame`), a pandas DataFrame, a pandas-on-Spark DataFrame, or a string path to a file. ^[automl-python-api-reference-databricks-on-aws.md]
- **`target_col`** – (required) The name of the column to predict. ^[automl-python-api-reference-databricks-on-aws.md]
- **`primary_metric`** – The metric used to select the best model. Default is `"f1"`. Other common classification metrics such as `"accuracy"`, `"precision"`, `"recall"`, and `"log_loss"` are also supported. ^[automl-python-api-reference-databricks-on-aws.md]
- **`timeout_minutes`** – Maximum run duration in minutes. This replaces the deprecated `max_trials` parameter in Databricks Runtime 11.0 ML and above. ^[automl-python-api-reference-databricks-on-aws.md]
- **`pos_label`** – (DBR 11.1 ML+, optional) The positive class label when computing metrics for binary classification. ^[automl-python-api-reference-databricks-on-aws.md]
- **`exclude_cols`** – (DBR 10.3 ML+, optional) List of column names to exclude from training features. ^[automl-python-api-reference-databricks-on-aws.md]
- **`exclude_frameworks`** – (DBR 10.3 ML+, optional) List of ML frameworks to exclude from the trial search space (e.g., `["xgboost", "lightgbm"]`). ^[automl-python-api-reference-databricks-on-aws.md]
- **`feature_store_lookups`** – (DBR 11.3 LTS ML+, optional) List of dictionaries describing feature store lookups. ^[automl-python-api-reference-databricks-on-aws.md]
- **`imputers`** – (DBR 10.4 LTS ML+, optional) Dictionary mapping column names to imputation strategies. ^[automl-python-api-reference-databricks-on-aws.md]
- **`sample_weight_col`** – (DBR 15.4 ML+, optional) Column name used for sample weights. ^[automl-python-api-reference-databricks-on-aws.md]
- **`split_col`** – (DBR 15.3 ML+, optional) Column used to define training/validation splits. ^[automl-python-api-reference-databricks-on-aws.md]
- Additional parameters (`data_dir`, `experiment_dir`, `experiment_name`, `time_col`) control directory paths and experiment naming. ^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

The method returns an `AutoMLSummary` object. This summary describes the metrics, parameters, and other details for each trial. It also provides methods to load the trained model from a specific trial. Each trial is represented by a [TrialInfo](/concepts/trialinfo.md) object, which contains the artifact URI and a model-loading method. ^[automl-python-api-reference-databricks-on-aws.md]

## Usage Example

A typical call to `classify` looks like:

```python
summary = databricks.automl.classify(
    dataset=train_df,
    target_col="label",
    primary_metric="f1",
    timeout_minutes=60,
)
```

To inspect a specific trial: ^[automl-python-api-reference-databricks-on-aws.md]

```python
trial_info = summary.trials[0]
model = trial_info.load_model()
```

## Deprecation Notes

- The `max_trials` parameter is deprecated in Databricks Runtime 10.4 ML and is not supported in Databricks Runtime 11.0 ML and above. Use `timeout_minutes` to control the duration of an AutoML run instead. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [AutoML Regression (regress)](/concepts/automl-regression-regress.md) – The analogous method for regression tasks.
- [AutoML Forecasting (forecast)](/concepts/automl-forecasting-forecast.md) – The method for time-series forecasting.
- [AutoMLSummary](/concepts/automlsummary.md) – The result object returned by all AutoML methods.
- [TrialInfo](/concepts/trialinfo.md) – Object representing a single trial’s metrics, parameters, and model.
- [ImportNotebookResult](/concepts/importnotebookresult.md) – Object returned by `databricks.automl.import_notebook`.
- AutoML UI – Low-code interface for AutoML functionality.

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
