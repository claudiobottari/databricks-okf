---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: daa271ade86ac185470eb7a1ba5a401f933927873c762521804de204352f63cf
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-forecasting-forecast
    - AF(
    - auto-ml-forecasting|forecasting
    - AutoML Forecasting Training
    - AutoML Forecasting on Databricks
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML Forecasting (forecast)
description: Method for time series forecasting model training, requiring target_col, time_col, frequency, horizon, and supporting identity_col for multiple time series
tags:
  - automl
  - forecasting
  - time-series
timestamp: "2026-06-19T09:07:24.235Z"
---

#AutoML Forecasting (forecast)

**AutoML Forecasting (forecast)** is a Databricks AutoML method that automatically trains and tunes time‑series forecasting models. It is one of three core AutoML task types, alongside [AutoML Classify (classify)|classification](/concepts/automl-classification-classify.md) and [AutoML Regress (regress)|regression](/concepts/automl-regression-regress.md). The method returns an [AutoMLSummary](/concepts/automlsummary.md) object describing the trials and generated notebooks. ^[automl-python-api-reference-databricks-on-aws.md]

## API Signature

```python
databricks.automl.forecast(
    dataset,
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

The following table describes the parameters specific to `forecast`. Shared AutoML parameters (such as `data_dir`, `experiment_dir`, `experiment_name`, `exclude_frameworks`, `feature_store_lookups`, `timeout_minutes`) behave as they do for `classify` and `regress`. ^[automl-python-api-reference-databricks-on-aws.md]

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `dataset` | `Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str]` | — | The input data. Can be a Spark DataFrame, pandas DataFrame, or a path to a file. ^[automl-python-api-reference-databricks-on-aws.md] |
| `target_col` | `str` | — | The name of the column to forecast. ^[automl-python-api-reference-databricks-on-aws.md] |
| `time_col` | `str` | — | The name of the column containing the time stamps or time indices. ^[automl-python-api-reference-databricks-on-aws.md] |
| `primary_metric` | `str` | `"smape"` | The primary evaluation metric for model selection. ^[automl-python-api-reference-databricks-on-aws.md] |
| `country_code` | `str` | `"US"` | A two‑letter ISO country code used for holiday effects in certain models. Available in Databricks Runtime 12.0 ML and above. ^[automl-python-api-reference-databricks-on-aws.md] |
| `frequency` | `str` | `"D"` | The frequency unit of the time series (e.g., `"D"` for daily, `"H"` for hourly). Must match the actual interval between consecutive time points. ^[automl-python-api-reference-databricks-on-aws.md] |
| `horizon` | `int` | `1` | The number of future time steps to forecast. ^[automl-python-api-reference-databricks-on-aws.md] |
| `identity_col` | `Optional[Union[str, List[str]]]` | `None` | One or more columns that identify individual time series (useful for grouped or hierarchical forecasting). ^[automl-python-api-reference-databricks-on-aws.md] |
| `sample_weight_col` | `Optional[str]` | `None` | Name of a column containing sample weights. Available in Databricks Runtime 16.0 ML and above. ^[automl-python-api-reference-databricks-on-aws.md] |
| `output_database` | `Optional[str]` | `None` | The database in which to store forecasting result tables. Available in Databricks Runtime 10.5 ML and above. ^[automl-python-api-reference-databricks-on-aws.md] |

## Behavior Details

- **Auto‑ARIMA support**: To use Auto‑ARIMA, the time series must have a **regular frequency** — that is, the interval between any two consecutive observations must be constant throughout the series. The frequency must match the `frequency` parameter supplied in the API call. ^[automl-python-api-reference-databricks-on-aws.md]

- **Missing time steps**: AutoML handles missing time steps by forward‑filling (i.e., filling gaps with the previous observed value). ^[automl-python-api-reference-databricks-on-aws.md]

- **Return value**: The method returns an `AutoMLSummary` object that describes the metrics, parameters, and details for each trial (model). This summary can be used to load the trained model or to inspect trial results. ^[automl-python-api-reference-databricks-on-aws.md]

- **Related methods**: The `forecast` method follows the same general pattern as `classify` and `regress`. All three share parameters such as `dataset`, `target_col`, `timeout_minutes`, and `exclude_frameworks`. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- AutoML — Overview of Databricks AutoML capabilities (low‑code UI and Python API)
- [AutoML Classify (classify)](/concepts/automl-classification-classify.md) — Classification task method
- [AutoML Regress (regress)](/concepts/automl-regression-regress.md) — Regression task method
- [AutoMLSummary](/concepts/automlsummary.md) — Object returned by all AutoML methods
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — General concept of forecasting
- Auto-ARIMA — Model that requires regular frequency

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
