---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7971592d3e732db5eae530f1d9d0a7f15006594f4638885e88dc6b8ffd07d568
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-python-api
    - APA
    - AutoML API
    - AutoML Python API Reference
    - AutoML Python API reference
    - AutoML Python API reference|AutoML Python API
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML Python API
description: Programmatic interface for Databricks AutoML that provides methods to start classification, regression, and forecasting runs.
tags:
  - auto-ml
  - python-api
  - databricks
timestamp: "2026-06-19T17:39:05.050Z"
---

# AutoML Python API

The **AutoML Python API** is a programmatic interface within Databricks Machine Learning that provides methods to start classification, regression, and forecasting AutoML runs. Each method call trains a set of models and generates a trial notebook for each trained model. The API is part of the `databricks.automl` module and is available on Databricks Runtime ML and above. ^[automl-python-api-reference-databricks-on-aws.md]

In addition to starting runs, the API includes a method to import notebooks that have been saved as MLflow artifacts, as well as summary objects (`AutoMLSummary`, `TrialInfo`, `ImportNotebookResult`) that describe the results of a run. ^[automl-python-api-reference-databricks-on-aws.md]

---

## `classify` Method

The `databricks.automl.classify` method configures an AutoML run to train a Classification Model. It returns an `AutoMLSummary` object.

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
    feature_store_lookups: Optional[List[Dict]] = None,  # DBR 11.3 LTS ML and above
    imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None,  # DBR 10.4 LTS ML and above
    pos_label: Optional[Union[int, bool, str]] = None,  # DBR 11.1 ML and above
    time_col: Optional[str] = None,
    split_col: Optional[str] = None,               # DBR 15.3 ML and above
    sample_weight_col: Optional[str] = None,       # DBR 15.4 ML and above
    max_trials: Optional[int] = None,              # Deprecated, DBR 10.5 ML and below
    timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

The `max_trials` parameter is **deprecated** in Databricks Runtime 10.4 ML and is **not supported** in Databricks Runtime 11.0 ML and above. Use `timeout_minutes` to control the duration of an AutoML run instead. ^[automl-python-api-reference-databricks-on-aws.md]

### Key Parameters

- **`dataset`** – The training data, provided as a Spark DataFrame, pandas DataFrame, pandas-on-Spark DataFrame, or a path (string) to a Delta table.
- **`target_col`** – The name of the column to predict.
- **`primary_metric`** – The metric to optimize during model selection. Default is `"f1"`. ^[automl-python-api-reference-databricks-on-aws.md]
- **`exclude_frameworks`** (DBR 10.3 ML+) – A list of framework names to exclude from the AutoML search (e.g., `["lightgbm"]`).
- **`timeout_minutes`** – The maximum number of minutes the AutoML run is allowed to execute. When `timeout_minutes` is reached, the run stops gracefully.

---

## `regress` Method

The `databricks.automl.regress` method configures an AutoML run to train a Regression Model. It returns an `AutoMLSummary` object.

```python
databricks.automl.regress(
    dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
    *,
    target_col: str,
    primary_metric: str = "r2",
    data_dir: Optional[str] = None,
    experiment_dir: Optional[str] = None,          # DBR 10.4 LTS ML and above
    experiment_name: Optional[str] = None,         # DBR 12.1 ML and above
    exclude_cols: Optional[List[str]] = None,      # DBR 10.3 ML and above
    exclude_frameworks: Optional[List[str]] = None, # DBR 10.3 ML and above
    feature_store_lookups: Optional[List[Dict]] = None,  # DBR 11.3 LTS ML and above
    imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None,  # DBR 10.4 LTS ML and above
    time_col: Optional[str] = None,
    split_col: Optional[str] = None,               # DBR 15.3 ML and above
    sample_weight_col: Optional[str] = None,       # DBR 15.3 ML and above
    max_trials: Optional[int] = None,              # Deprecated, DBR 10.5 ML and below
    timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

The same deprecation note applies to `max_trials` as in `classify`. ^[automl-python-api-reference-databricks-on-aws.md] The default `primary_metric` is `"r2"` (coefficient of determination). ^[automl-python-api-reference-databricks-on-aws.md]

---

## `forecast` Method

The `databricks.automl.forecast` method configures an AutoML run for training a [Time Series Forecasting](/concepts/multi-series-forecasting.md) model. It returns an `AutoMLSummary` object.

```python
databricks.automl.forecast(
    dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
    *,
    target_col: str,
    time_col: str,
    primary_metric: str = "smape",
    country_code: str = "US",                      # DBR 12.0 ML and above
    frequency: str = "D",
    horizon: int = 1,
    data_dir: Optional[str] = None,
    experiment_dir: Optional[str] = None,
    experiment_name: Optional[str] = None,         # DBR 12.1 ML and above
    exclude_frameworks: Optional[List[str]] = None,
    feature_store_lookups: Optional[List[Dict]] = None,  # DBR 12.2 LTS ML and above
    identity_col: Optional[Union[str, List[str]]] = None,
    sample_weight_col: Optional[str] = None,       # DBR 16.0 ML and above
    output_database: Optional[str] = None,         # DBR 10.5 ML and above
    timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

### Forecasting-specific Behaviour

To use Auto-ARIMA, the time series must have a **regular frequency** (i.e., the interval between any two points must be the same throughout the series). The frequency must also match the frequency unit specified in the `frequency` parameter. AutoML handles missing time steps by filling in those values with the previous value (forward fill). ^[automl-python-api-reference-databricks-on-aws.md]

- **`frequency`** – The unit of time between observations. Default is `"D"` (daily). Other typical values include `"W"`, `"M"`, `"H"`, etc.
- **`horizon`** – The number of time steps to forecast into the future. Default is 1.
- **`country_code`** (DBR 12.0 ML+) – Used for holiday effect modeling. Default is `"US"`.
- **`identity_col`** – Column(s) that identify individual time series when the dataset contains multiple series.

---

## `import_notebook` Method

The `databricks.automl.import_notebook` method imports a notebook that has been saved as an [MLflow](/concepts/mlflow.md) artifact. This is useful for taking a trial notebook generated by an AutoML run and placing it into a user‑specified workspace path. It returns an `ImportNotebookResult` object.

```python
databricks.automl.import_notebook(
    artifact_uri: str,
    path: str,
    overwrite: bool = False
) -> ImportNotebookResult
```

**Example:**

```python
summary = databricks.automl.classify(...)
result = databricks.automl.import_notebook(
    summary.trials[5].artifact_uri,
    "/Users/you@yourcompany.com/path/to/directory"
)
print(result.path)
print(result.url)
```

^[automl-python-api-reference-databricks-on-aws.md]

---

## Summary Objects

### `AutoMLSummary`

The `AutoMLSummary` object is the return type for `classify`, `regress`, and `forecast`. It describes the metrics, parameters, and other details for each of the trials (individual model trainings) that were evaluated during the AutoML run. It also provides methods to load the model trained by a specific trial. ^[automl-python-api-reference-databricks-on-aws.md]

### `TrialInfo`

The `TrialInfo` object summarises each individual trial within an `AutoMLSummary`. It has a method to load the model generated for that trial. ^[automl-python-api-reference-databricks-on-aws.md]

### `ImportNotebookResult`

The `ImportNotebookResult` object is returned by `import_notebook`. It contains the workspace path and URL of the imported notebook. ^[automl-python-api-reference-databricks-on-aws.md]

---

## Related Concepts

- AutoML Overview – Low‑code UI alternative and conceptual introduction.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime environment that supports the AutoML Python API.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Where AutoML runs are logged.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – Many AutoML trials use hyperparameter search.
- Time Series Forecasting on Databricks – Broader guidance for forecasting workflows.

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
