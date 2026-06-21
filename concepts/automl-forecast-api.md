---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d4afdf568be5341c8fa9d54bb9d75646324e4f8e0e16d703bc4933d96d9b6ff
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-forecast-api
    - AFA
    - AutoML Forecasting API
    - AutoML forecasting Python API
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML Forecast API
description: Databricks AutoML method to configure and run time-series forecasting model training
tags:
  - machine-learning
  - automl
  - forecasting
  - time-series
  - databricks
timestamp: "2026-06-18T10:51:33.604Z"
---

# AutoML Forecast API

**AutoML Forecast API** is a Python method in AutoML that configures and launches a forecasting model training run. The API is provided by the `databricks.automl` module and returns an `AutoMLSummary` object describing the trial results.^[automl-python-api-reference-databricks-on-aws.md]

## Method Signature

The `databricks.automl.forecast` function accepts a dataset, a target column, a time column, forecasting parameters, and optional configuration options. Its signature is:^[automl-python-api-reference-databricks-on-aws.md]

```python
databricks.automl.forecast(
  dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
  *,
  target_col: str,
  time_col: str,
  primary_metric: str = "smape",
  country_code: str = "US",                                         # DBR 12.0 ML+
  frequency: str = "D",
  horizon: int = 1,
  data_dir: Optional[str] = None,
  experiment_dir: Optional[str] = None,
  experiment_name: Optional[str] = None,                            # DBR 12.1 ML+
  exclude_frameworks: Optional[List[str]] = None,
  feature_store_lookups: Optional[List[Dict]] = None,               # DBR 12.2 LTS ML+
  identity_col: Optional[Union[str, List[str]]] = None,
  sample_weight_col: Optional[str] = None,                          # DBR 16.0 ML+
  output_database: Optional[str] = None,                            # DBR 10.5 ML+
  timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

The method trains a set of forecasting models and generates a trial notebook for each model, as with other AutoML types.^[automl-python-api-reference-databricks-on-aws.md]

## Forecasting Parameters

When using Auto-ARIMA, the time series must have a regular frequency — the interval between any two points must be the same throughout the series. The frequency must match the frequency unit specified in the `frequency` parameter. Missing time steps are handled by filling in those values with the previous value.^[automl-python-api-reference-databricks-on-aws.md]

The `frequency` parameter defaults to `"D"` (daily). The `horizon` parameter defaults to 1, meaning only the next period is predicted. Use `primary_metric` to select the evaluation metric; the default for forecasting is `"smape"` (symmetric mean absolute percentage error).^[automl-python-api-reference-databricks-on-aws.md]

| Parameter | Type | Default | Description |
|---|---|---|---|
| `dataset` | DataFrame or str | — | Training data. Can be PySpark, pandas, Koalas, or a file path. |
| `target_col` | str | — | Name of the column to predict. |
| `time_col` | str | — | Name of the column containing time stamps. |
| `primary_metric` | str | `"smape"` | Metric to optimize during training. |
| `country_code` | str | `"US"` | Country code for holiday effects (DBR 12.0+). |
| `frequency` | str | `"D"` | Frequency of the time series (e.g., `"D"`, `"W"`, `"M"`). |
| `horizon` | int | 1 | Number of future periods to forecast. |
| `data_dir` | str or None | None | Directory to store interim data. |
| `experiment_dir` | str or None | None | Path to the MLflow experiment directory. |
| `experiment_name` | str or None | None | Name of the MLflow experiment (DBR 12.1+). |
| `exclude_frameworks` | list of str | None | Frameworks to exclude from training. |
| `feature_store_lookups` | list of dict | None | Feature store lookup definitions (DBR 12.2 LTS+). |
| `identity_col` | str or list of str | None | Column(s) that identify individual time series. |
| `sample_weight_col` | str or None | None | Column with sample weights (DBR 16.0+). |
| `output_database` | str or None | None | Database where predictions are saved (DBR 10.5+). |
| `timeout_minutes` | int or None | None | Maximum duration for the run. |

^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

The method returns an [`AutoMLSummary`](automl-python-api-reference-databricks-on-aws.md#automlsummary) object that describes the run's metrics, parameters, and details for each trial. Use this object to inspect results or load a trained model from a specific trial.^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- AutoML – overview of Databricks AutoML features
- [MLflow Tracking](/concepts/mlflow-tracking.md) – tracking mechanism for AutoML trials
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – general forecasting concepts
- [AutoML Python API Reference](/concepts/automl-python-api.md) – full reference including `classify` and `regress` methods

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
