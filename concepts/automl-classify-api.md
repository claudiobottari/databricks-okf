---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8eece8447c0b903f863978a4de86ddf9ee0dacc1c5cf56e122f37c87f74ead72
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-classify-api
    - ACA
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML Classify API
description: Databricks AutoML method to configure and run classification model training
tags:
  - machine-learning
  - automl
  - classification
  - databricks
timestamp: "2026-06-18T10:51:35.737Z"
---

# AutoML Classify API

**AutoML Classify API** is a Python API method (`databricks.automl.classify`) that launches an AutoML run to train a classification model. It accepts a dataset and configuration parameters, automatically generates trial notebooks for each model, and returns an `AutoMLSummary` object describing the results.^[automl-python-api-reference-databricks-on-aws.md]

## Signature

```python
databricks.automl.classify(
    dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
    *,
    target_col: str,
    primary_metric: str = "f1",
    data_dir: Optional[str] = None,
    experiment_dir: Optional[str] = None,
    experiment_name: Optional[str] = None,
    exclude_cols: Optional[List[str]] = None,
    exclude_frameworks: Optional[List[str]] = None,
    feature_store_lookups: Optional[List[Dict]] = None,
    imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None,
    pos_label: Optional[Union[int, bool, str]] = None,
    time_col: Optional[str] = None,
    split_col: Optional[str] = None,
    sample_weight_col: Optional[str] = None,
    max_trials: Optional[int] = None,
    timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

^[automl-python-api-reference-databricks-on-aws.md]

## Parameters

The `classify` method accepts the following parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `dataset` | `pyspark.sql.DataFrame`, `pandas.DataFrame`, `pyspark.pandas.DataFrame`, or `str` | The input dataset for training. A `str` can be a path to a Delta table or a Unity Catalog table name. |
| `target_col` | `str` | The name of the column that contains the ground-truth labels. |
| `primary_metric` | `str` | The metric to optimize during training. Default is `"f1"`. |
| `data_dir` | `Optional[str]` | Directory path to save the dataset snapshot. |
| `experiment_dir` | `Optional[str]` | Directory for the MLflow experiment (available in Databricks Runtime 10.4 LTS ML and above). |
| `experiment_name` | `Optional[str]` | Name of the MLflow experiment (available in Databricks Runtime 12.1 ML and above). |
| `exclude_cols` | `Optional[List[str]]` | Columns to exclude from training (available in Databricks Runtime 10.3 ML and above). |
| `exclude_frameworks` | `Optional[List[str]]` | Frameworks to exclude from the AutoML search (available in Databricks Runtime 10.3 ML and above). |
| `feature_store_lookups` | `Optional[List[Dict]]` | Feature store lookups for feature engineering (available in Databricks Runtime 11.3 LTS ML and above). |
| `imputers` | `Optional[Dict[str, Union[str, Dict[str, Any]]]]` | Custom imputation strategies for missing values (available in Databricks Runtime 10.4 LTS ML and above). |
| `pos_label` | `Optional[Union[int, bool, str]]` | The positive class label for binary classification (available in Databricks Runtime 11.1 ML and above). |
| `time_col` | `Optional[str]` | Column containing timestamps, used for time‑based splitting. |
| `split_col` | `Optional[str]` | Column used to split the dataset into train and test sets (available in Databricks Runtime 15.3 ML and above). |
| `sample_weight_col` | `Optional[str]` | Column containing sample weights (available in Databricks Runtime 15.4 ML and above). |
| `max_trials` | `Optional[int]` | **Deprecated** in Databricks Runtime 10.4 ML; not supported in Runtime 11.0 ML and above. Use `timeout_minutes` instead. |
| `timeout_minutes` | `Optional[int]` | Maximum runtime for the AutoML run, in minutes. |

^[automl-python-api-reference-databricks-on-aws.md]

All parameters except `dataset` and `target_col` are keyword-only (separated by `*`).^[automl-python-api-reference-databricks-on-aws.md]

## Return type

The method returns an `AutoMLSummary` object that describes the metrics, parameters, and other details for each trial. Each trial is represented as a `TrialInfo` object. `TrialInfo` includes a method to load the trained model for that trial.^[automl-python-api-reference-databricks-on-aws.md]

## Example

```python
import databricks.automl

summary = databricks.automl.classify(
    dataset=df,
    target_col="label",
    timeout_minutes=60,
    primary_metric="f1"
)

# Load the best model from the first trial
best_trial = summary.trials[0]
model = best_trial.load_model()
```

^[automl-python-api-reference-databricks-on-aws.md]

The `AutoMLSummary` can also be used to import a trial notebook via `databricks.automl.import_notebook()`.^[automl-python-api-reference-databricks-on-aws.md]

## Related concepts

- AutoML — The broader automated machine learning feature
- [AutoML Regress API](/concepts/automl-regress-api.md) — The regression variant of the AutoML API
- [AutoML Forecast API](/concepts/automl-forecast-api.md) — The forecasting variant of the AutoML API
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registry used by AutoML
- pyspark.sql.DataFrame — One of the supported input dataset types

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
