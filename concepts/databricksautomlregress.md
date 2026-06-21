---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c2cb8d9cf59683234b030ebc837b2291e51f51eee0db12858a8e3cd1ca7242f
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricksautomlregress
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: databricks.automl.regress
description: AutoML method that trains regression models, returning an AutoMLSummary with per-trial notebooks and metrics; primary metric defaults to r2.
tags:
  - AutoML
  - regression
  - Databricks
  - API
timestamp: "2026-06-19T14:07:48.246Z"
---

```markdown
# databricks.automl.regress

The `databricks.automl.regress` method configures an AutoML run to train a regression model. It accepts a dataset and a target column, trains multiple candidate models, generates a trial notebook for each model, and returns an `AutoMLSummary` object with the results. ^[automl-python-api-reference-databricks-on-aws.md]

## Signature

```python
databricks.automl.regress(
  dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
  *,
  target_col: str,
  primary_metric: str = "r2",
  data_dir: Optional[str] = None,
  experiment_dir: Optional[str] = None,                             # DBR 10.4 LTS ML and above
  experiment_name: Optional[str] = None,                            # DBR 12.1 ML and above
  exclude_cols: Optional[List[str]] = None,                         # DBR 10.3 ML and above
  exclude_frameworks: Optional[List[str]] = None,                   # DBR 10.3 ML and above
  feature_store_lookups: Optional[List[Dict]] = None,               # DBR 11.3 LTS ML and above
  imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None, # DBR 10.4 LTS ML and above
  time_col: Optional[str] = None,
  split_col: Optional[str] = None,                                  # DBR 15.3 ML and above
  sample_weight_col: Optional[str] = None,                          # DBR 15.3 ML and above
  max_trials: Optional[int] = None,                                 # DBR 10.5 ML and below
  timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```
^[automl-python-api-reference-databricks-on-aws.md]

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `dataset` | `Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str]` | — | The dataset to train on. Can be a PySpark DataFrame, pandas DataFrame, pandas-on-Spark DataFrame, or a path to a file (e.g., a Delta table path or a CSV path). |
| `target_col` | `str` | — | The name of the column containing the target variable to predict. |
| `primary_metric` | `str` | `"r2"` | The primary metric to optimize during training. For regression, common choices include `"r2"`, `"rmse"`, `"mae"`. |
| `data_dir` | `Optional[str]` | `None` | Directory path for storing data artifacts. |
| `experiment_dir` | `Optional[str]` | `None` | Directory path for the MLflow experiment (available in DBR 10.4 LTS ML and above). |
| `experiment_name` | `Optional[str]` | `None` | Name of the MLflow experiment (available in DBR 12.1 ML and above). Overrides `experiment_dir` if both are provided. |
| `exclude_cols` | `Optional[List[str]]` | `None` | Columns to exclude from training features (available in DBR 10.3 ML and above). |
| `exclude_frameworks` | `Optional[List[str]]` | `None` | Frameworks to exclude from the trial search (available in DBR 10.3 ML and above). For example, `["sklearn"]`. |
| `feature_store_lookups` | `Optional[List[Dict]]` | `None` | List of feature store lookup configurations for feature engineering (available in DBR 11.3 LTS ML and above). |
| `imputers` | `Optional[Dict[str, Union[str, Dict[str, Any]]]]` | `None` | Imputation strategies for missing values. A dictionary mapping column names to an imputation method (or a dict with method and parameters). Available in DBR 10.4 LTS ML and above. |
| `time_col` | `Optional[str]` | `None` | Name of the time column if the data contains a time dimension (e.g., for time‑aware splitting). |
| `split_col` | `Optional[str]` | `None` | Column used for custom train/test splits (available in DBR 15.3 ML and above). |
| `sample_weight_col` | `Optional[str]` | `None` | Column containing sample weights for weighted training (available in DBR 15.3 ML and above). |
| `max_trials` | `Optional[int]` | `None` | **Deprecated** in DBR 10.4 ML. Not supported in DBR 11.0 ML and above. Use `timeout_minutes` instead. |
| `timeout_minutes` | `Optional[int]` | `None` | Maximum duration (in minutes) for the AutoML run. Replaces `max_trials` for controlling run length. |

^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

Returns an `AutoMLSummary` object. The summary contains metrics, parameters, and details for each trial (model) that was trained. You can use the summary to load a model from a specific trial or to inspect trial results. ^[automl-python-api-reference-databricks-on-aws.md]

## Usage Example

```python
summary = databricks.automl.regress(
    dataset=df,
    target_col="price",
    primary_metric="rmse",
    timeout_minutes=30,
    exclude_frameworks=["sklearn"],
)
print(f"Best trial: {summary.best_trial}")
model = summary.best_trial.load_model()
```

## Notes

- The `max_trials` parameter is deprecated: in Databricks Runtime 10.4 ML it is no longer supported; use `timeout_minutes` to control the duration of the AutoML run. In DBR 11.0 ML and above, `max_trials` is completely unsupported. ^[automl-python-api-reference-databricks-on-aws.md]
- The method supports datasets provided as PySpark DataFrames, pandas DataFrames, pandas-on-Spark DataFrames, or a string path (e.g., a Delta table path or CSV file path). ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [[databricks.automl.classify]] — The analogous method for classification tasks
- [[databricks.automl.forecast]] — AutoML method for time series forecasting
- AutoML — Overview of AutoML on Databricks
- [[AutoMLSummary]] — The result object returned by AutoML runs
- [[AutoML Regress API|Regression]] — The supervised learning task AutoML addresses here
- [[MLflow]] — Experiment tracking used by AutoML trials

## Sources

- automl-python-api-reference-databricks-on-aws.md
```

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
