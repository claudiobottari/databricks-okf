---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24666552604cbe228401f276640627c97452068755b7e768b51e96e372f754aa
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-forecast
    - AutoML Forecasting
    - AutoML Forecasting UI
    - AutoML forecasting
    - AutoML Python API reference|forecast
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML forecast()
description: Python API method to start an AutoML forecasting run with parameters for time column, frequency, horizon, identity column, and country code.
tags:
  - machine-learning
  - forecasting
  - api
  - databricks
timestamp: "2026-06-19T22:12:11.695Z"
---

# AutoML forecast()

The `databricks.automl.forecast` method configures an AutoML run for training a forecasting model on time series data. It returns an [AutoMLSummary](/concepts/automlsummary.md) object that describes the metrics, parameters, and other details for each trial. ^[automl-python-api-reference-databricks-on-aws.md]

## Overview

The `forecast()` method is one of three primary AutoML task methods, alongside `classify()` and `regress()`. It is designed specifically for time series forecasting problems where the goal is to predict future values based on historical data. ^[automl-python-api-reference-databricks-on-aws.md]

## Syntax

```python
databricks.automl.forecast(
  dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
  *,
  target_col: str,
  time_col: str,
  primary_metric: str = "smape",
  country_code: str = "US",
  frequency: str = "D",
  horizon: int = 1,
  data_dir: Optional[str] = None,
  experiment_dir: Optional[str] = None,
  experiment_name: Optional[str] = None,
  exclude_frameworks: Optional[List[str]] = None,
  feature_store_lookups: Optional[List[Dict]] = None,
  identity_col: Optional[Union[str, List[str]]] = None,
  sample_weight_col: Optional[str] = None,
  output_database: Optional[str] = None,
  timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

^[automl-python-api-reference-databricks-on-aws.md]

## Parameters

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `dataset` | `Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str]` | The input dataset for training. Can be a Spark DataFrame, pandas DataFrame, pandas-on-Spark DataFrame, or a string path to a data source. |
| `target_col` | `str` | The name of the column containing the target variable to forecast. |
| `time_col` | `str` | The name of the column containing the time stamps for the time series. |

^[automl-python-api-reference-databricks-on-aws.md]

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `primary_metric` | `str` | `"smape"` | The primary evaluation metric for model selection. Default is Symmetric Mean Absolute Percentage Error (SMAPE). |
| `country_code` | `str` | `"US"` | Country code for holiday effects modeling. Available in Databricks Runtime 12.0 ML and above. |
| `frequency` | `str` | `"D"` | The frequency of the time series data. Default is daily (`"D"`). |
| `horizon` | `int` | `1` | The number of time steps to forecast into the future. |
| `data_dir` | `Optional[str]` | `None` | Directory path for saving intermediate data. |
| `experiment_dir` | `Optional[str]` | `None` | Directory path for the MLflow experiment. Available in Databricks Runtime 10.4 LTS ML and above. |
| `experiment_name` | `Optional[str]` | `None` | Name of the MLflow experiment. Available in Databricks Runtime 12.1 ML and above. |
| `exclude_frameworks` | `Optional[List[str]]` | `None` | List of framework names to exclude from the AutoML run. |
| `feature_store_lookups` | `Optional[List[Dict]]` | `None` | Feature store lookup configurations. Available in Databricks Runtime 12.2 LTS ML and above. |
| `identity_col` | `Optional[Union[str, List[str]]]` | `None` | Column(s) that identify individual time series when the dataset contains multiple time series. |
| `sample_weight_col` | `Optional[str]` | `None` | Column name for sample weights. Available in Databricks Runtime 16.0 ML and above. |
| `output_database` | `Optional[str]` | `None` | Database name for storing output predictions. Available in Databricks Runtime 10.5 ML and above. |
| `timeout_minutes` | `Optional[int]` | `None` | Maximum time in minutes for the AutoML run. |

^[automl-python-api-reference-databricks-on-aws.md]

## Auto-ARIMA and Frequency Requirements

To use Auto-ARIMA, the time series must have a regular frequency — the interval between any two consecutive time points must be the same throughout the entire series. The frequency must match the frequency unit specified in the `frequency` parameter of the API call. AutoML handles missing time steps by filling in those values with the previous value (forward fill). ^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

The method returns an [AutoMLSummary](/concepts/automlsummary.md) object, which provides access to trial information, metrics, and model loading capabilities. Each trial is represented by a [TrialInfo](/concepts/trialinfo.md) object. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [AutoML classify()](/concepts/automl-classify.md) — The AutoML method for classification tasks
- [AutoML regress()](/concepts/automl-regress.md) — The AutoML method for regression tasks
- [AutoMLSummary](/concepts/automlsummary.md) — The summary object returned by AutoML methods
- [TrialInfo](/concepts/trialinfo.md) — Summary object for individual AutoML trials
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — The broader concept of forecasting future values from historical data
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The experiment tracking system used by AutoML

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
