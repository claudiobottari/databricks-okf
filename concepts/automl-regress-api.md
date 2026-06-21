---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 879a2724047057333d93e96a7f066da689d429e104d94dc07c448865d5e2d7ae
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-regress-api
    - ARA
    - AutoML Regression API
    - Regression
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML Regress API
description: Databricks AutoML method to configure and run regression model training
tags:
  - machine-learning
  - automl
  - regression
  - databricks
timestamp: "2026-06-18T10:51:28.568Z"
---

# AutoML Regress API

**`databricks.automl.regress`** is a Python API method that configures and starts an Automated Machine Learning (AutoML) run to train a regression model on a provided dataset. The method automatically explores multiple algorithms, hyperparameter settings, and preprocessing steps, then returns a summary of the resulting trials. ^[automl-python-api-reference-databricks-on-aws.md]

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
|---|---|---|
| `dataset` | `Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str]` | Input dataset. If a string, it is interpreted as a path to a file (e.g., CSV or Parquet) in DBFS or Unity Catalog. |
| `target_col` | `str` | Name of the column containing the regression target (label). |
| `primary_metric` | `str` | Primary evaluation metric for model selection. Default is `"r2"`. |
| `data_dir` | `Optional[str]` | Directory for intermediate data artifacts. |
| `experiment_dir` | `Optional[str]` | Path to the parent directory for the MLflow experiment (Databricks Runtime 10.4 LTS ML and above). |
| `experiment_name` | `Optional[str]` | Name of the MLflow experiment (Databricks Runtime 12.1 ML and above). |
| `exclude_cols` | `Optional[List[str]]` | Columns to exclude from feature training (Databricks Runtime 10.3 ML and above). |
| `exclude_frameworks` | `Optional[List[str]]` | ML frameworks to exclude from the search (Databricks Runtime 10.3 ML and above). |
| `feature_store_lookups` | `Optional[List[Dict]]` | Feature store lookup configurations (Databricks Runtime 11.3 LTS ML and above). |
| `imputers` | `Optional[Dict[str, Union[str, Dict[str, Any]]]]` | Imputation strategies per column (Databricks Runtime 10.4 LTS ML and above). |
| `time_col` | `Optional[str]` | Name of the time column if the data has a time ordering. |
| `split_col` | `Optional[str]` | Column used for a predefined train/test split (Databricks Runtime 15.3 ML and above). |
| `sample_weight_col` | `Optional[str]` | Column containing sample weights (Databricks Runtime 15.3 ML and above). |
| `max_trials` | `Optional[int]` | Maximum number of trials. **Deprecated** in Databricks Runtime 10.4 ML and not supported in Runtime 11.0 ML and above. |
| `timeout_minutes` | `Optional[int]` | Maximum duration of the AutoML run in minutes. Use this instead of `max_trials` to control run time. |

^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

The method returns an `AutoMLSummary` object that provides metrics, parameters, and details for each trial. The summary can be used to inspect results, load trained models, or import a trial notebook. ^[automl-python-api-reference-databricks-on-aws.md]

## Notes

- The `max_trials` parameter is **deprecated** starting in Databricks Runtime 10.4 ML and is **removed** in Databricks Runtime 11.0 ML and above. Use `timeout_minutes` to cap the run duration. ^[automl-python-api-reference-databricks-on-aws.md]
- The method generates a set of trial notebooks — one per trained model — that can be reviewed and modified. ^[automl-python-api-reference-databricks-on-aws.md]
- For other problem types, see the related APIs [AutoML Classify API](/concepts/automl-classify-api.md) (classification) and [AutoML Forecast API](/concepts/automl-forecast-api.md) (forecasting).

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
