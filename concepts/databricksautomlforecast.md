---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd1aba1035e9f4b395711f9f8a40dd4145e079ee94511e007dc7bb2f42948ae4
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricksautomlforecast
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: databricks.automl.forecast
description: AutoML method that trains forecasting models with required time_col, frequency, horizon, and optional identity_col for time series data.
tags:
  - AutoML
  - forecasting
  - Databricks
  - time-series
timestamp: "2026-06-19T14:07:36.494Z"
---

---
title: databricks.automl.forecast
summary: The `databricks.automl.forecast` function configures an AutoML run to train a forecasting model on time-series data, returning an AutoMLSummary object.
sources:
  - automl-python-api-reference-databricks-on-aws.md
kind: api-reference
createdAt: "2026-06-18T08:09:21.819Z"
updatedAt: "2026-06-18T08:09:21.819Z"
tags:
  - automl
  - forecasting
  - python-api
  - time-series
aliases:
  - forecast
  - forecasting automl
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# `databricks.automl.forecast`

The `databricks.automl.forecast` method configures an AutoML run for training a forecasting model. It accepts a dataset with a time column and a target column, and returns an [AutoMLSummary](/concepts/automlsummary.md) object describing the trials.^[automl-python-api-reference-databricks-on-aws.md]

To use Auto-ARIMA, the time series must have a regular frequency (i.e., the interval between any two points must be the same throughout the time series). The frequency must match the frequency unit specified in the API call. AutoML handles missing time steps by filling in those values with the previous value.^[automl-python-api-reference-databricks-on-aws.md]

## Syntax

```python
databricks.automl.forecast(
  dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
  *,
  target_col: str,
  time_col: str,
  primary_metric: str = "smape",
  country_code: str = "US",                                         # :re[DBR] 12.0 ML and above
  frequency: str = "D",
  horizon: int = 1,
  data_dir: Optional[str] = None,
  experiment_dir: Optional[str] = None,
  experiment_name: Optional[str] = None,                            # :re[DBR] 12.1 ML and above
  exclude_frameworks: Optional[List[str]] = None,
  feature_store_lookups: Optional[List[Dict]] = None,               # :re[DBR] 12.2 LTS ML and above
  identity_col: Optional[Union[str, List[str]]] = None,
  sample_weight_col: Optional[str] = None,                          # :re[DBR] 16.0 ML and above
  output_database: Optional[str] = None,                            # :re[DBR] 10.5 ML and above
  timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

^[automl-python-api-reference-databricks-on-aws.md]

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `dataset` | `Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str]` | required | Input dataset. Can be a Spark DataFrame, pandas DataFrame, pandas-on-Spark DataFrame, or a path string (e.g., to a Delta table). |
| `target_col` | `str` | required | Name of the column containing the target (forecast) values. |
| `time_col` | `str` | required | Name of the column containing timestamps. |
| `primary_metric` | `str` | `"smape"` | Primary evaluation metric for model selection (e.g., `"smape"`, `"mae"`, `"rmse"`). |
| `country_code` | `str` | `"US"` | Country code for holiday effects; available in Databricks Runtime 12.0 ML and above. |
| `frequency` | `str` | `"D"` | Frequency of the time series (e.g., `"D"` for daily, `"H"` for hourly, `"W"` for weekly). Must match the actual data frequency for Auto-ARIMA to work. |
| `horizon` | `int` | `1` | Number of future time steps to forecast. |
| `data_dir` | `Optional[str]` | `None` | Directory path to store intermediate data artifacts. |
| `experiment_dir` | `Optional[str]` | `None` | Directory path for the MLflow experiment (Databricks Runtime 10.4 LTS ML and above). |
| `experiment_name` | `Optional[str]` | `None` | Name of the MLflow experiment (Databricks Runtime 12.1 ML and above). |
| `exclude_frameworks` | `Optional[List[str]]` | `None` | List of framework names to exclude from automated trials. |
| `feature_store_lookups` | `Optional[List[Dict]]` | `None` | Feature store lookups to use as additional features (Databricks Runtime 12.2 LTS ML and above). |
| `identity_col` | `Optional[Union[str, List[str]]]` | `None` | Column(s) that identify distinct time series (e.g., a product ID for multiple series in the same dataset). |
| `sample_weight_col` | `Optional[str]` | `None` | Column specifying sample weights for weighted training (Databricks Runtime 16.0 ML and above). |
| `output_database` | `Optional[str]` | `None` | Database name to store the forecasting results table (Databricks Runtime 10.5 ML and above). |
| `timeout_minutes` | `Optional[int]` | `None` | Maximum duration for the AutoML run in minutes. |

^[automl-python-api-reference-databricks-on-aws.md]

## Notes

- If the time series has irregular frequency, Auto-ARIMA will not be applied. AutoML handles missing time steps by forward-filling (using the previous value).^[automl-python-api-reference-databricks-on-aws.md]
- The `max_trials` parameter is not supported for forecasting in Databricks Runtime 11.0 ML and above; use `timeout_minutes` instead.^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

Returns an [AutoMLSummary](/concepts/automlsummary.md) object. This object provides access to trial information, metrics, parameters, and methods to load individual models.^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [databricks.automl.classify](/concepts/databricksautomlclassify.md) — AutoML for classification tasks
- [databricks.automl.regress](/concepts/databricksautomlregress.md) — AutoML for regression tasks
- [AutoMLSummary](/concepts/automlsummary.md) — Summary object returned by all AutoML methods
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — Broader topic of forecasting with machine learning
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizing and tracking AutoML runs

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
