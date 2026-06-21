---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 185c5bcd03e72ae2d0f01d720293b919789c61ecc1b025828e9a20b876dbf45f
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
    - train-classification-models-with-automl-python-api-databricks-on-aws.md
    - train-regression-models-with-automl-python-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-automl-python-api
    - DAPA
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
    - file: train-classification-models-with-automl-python-api-databricks-on-aws.md
    - file: train-regression-models-with-automl-python-api-databricks-on-aws.md
title: Databricks AutoML Python API
description: Programmatic Python interface for Databricks AutoML, providing methods to start classification, regression, and forecasting runs
tags:
  - automl
  - databricks
  - python-api
timestamp: "2026-06-19T09:07:14.200Z"
---

# Databricks AutoML Python API

The **Databricks AutoML Python API** provides programmatic access to automated machine learning (AutoML) capabilities on the Databricks platform. It allows data scientists and ML engineers to automatically train classification, regression, and forecasting models by calling simple Python methods, with each run generating a set of trial notebooks and trained models. ^[automl-python-api-reference-databricks-on-aws.md]

## Overview

The AutoML Python API is available in the `databricks` Python package and is designed to work with [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). It supports three main task types: classification, regression, and forecasting. Each method call returns an [AutoMLSummary](/concepts/automlsummary.md) object that contains metrics, parameters, and details for each trial, as well as the best trial's model path for inference. ^[automl-python-api-reference-databricks-on-aws.md]

The API accepts datasets as pandas DataFrames, PySpark DataFrames, or file paths. You control the duration of an AutoML run using the `timeout_minutes` parameter rather than the deprecated `max_trials` parameter. ^[automl-python-api-reference-databricks-on-aws.md]

## Classification

The `databricks.automl.classify()` method trains classification models. It requires a dataset and a `target_col` specifying the column to predict. The default primary metric is `"f1"`. ^[automl-python-api-reference-databricks-on-aws.md]

### Example

The following example uses the UCI Census Income dataset to predict whether an individual earns more than $50K per year: ^[train-classification-models-with-automl-python-api-databricks-on-aws.md]

```python
from databricks import automl

summary = automl.classify(train_df, target_col="income", timeout_minutes=30)
```

After training, you can load the best model and run inference:

```python
import mlflow

model_uri = summary.best_trial.model_path
model = mlflow.pyfunc.load_model(model_uri)
predictions = model.predict(X_test)
```

^[train-classification-models-with-automl-python-api-databricks-on-aws.md]

## Regression

The `databricks.automl.regress()` method trains regression models. The default primary metric is `"r2"`. ^[automl-python-api-reference-databricks-on-aws.md]

### Example

The following example trains a regression model on the California housing dataset to predict median house value: ^[train-regression-models-with-automl-python-api-databricks-on-aws.md]

```python
from databricks import automl

summary = automl.regress(train_pdf, target_col="MedHouseVal", timeout_minutes=30)
```

Inference follows the same pattern as classification:

```python
model_uri = summary.best_trial.model_path
model = mlflow.pyfunc.load_model(model_uri)
predictions = model.predict(X_test)
```

^[train-regression-models-with-automl-python-api-databricks-on-aws.md]

## Forecasting

The `databricks.automl.forecast()` method trains forecasting models. It requires a `target_col`, a `time_col`, and a `frequency`. The default primary metric is `"smape"`. ^[automl-python-api-reference-databricks-on-aws.md]

Key parameters include:
- `frequency`: The unit of time (default `"D"` for daily)
- `horizon`: The number of time steps to forecast (default `1`)
- `identity_col`: Column(s) identifying individual time series
- `country_code`: For holiday effects (default `"US"`, available from Databricks Runtime 12.0 ML and above)

To use Auto-ARIMA, the time series must have a regular frequency. AutoML handles missing time steps by filling in those values with the previous value. ^[automl-python-api-reference-databricks-on-aws.md]

## Import Notebook

The `databricks.automl.import_notebook()` method imports a notebook that has been saved as an [MLflow](/concepts/mlflow.md) artifact. This is useful for recovering trial notebooks from previous AutoML runs: ^[automl-python-api-reference-databricks-on-aws.md]

```python
summary = automl.classify(...)
result = automl.import_notebook(
    summary.trials[5].artifact_uri,
    "/Users/you@yourcompany.com/path/to/directory"
)
print(result.path)
print(result.url)
```

^[automl-python-api-reference-databricks-on-aws.md]

## Inference

After an AutoML run completes, you can use the best model for inference on both pandas DataFrames and Spark DataFrames. ^[train-classification-models-with-automl-python-api-databricks-on-aws.md]

### pandas DataFrame inference

```python
model = mlflow.pyfunc.load_model(model_uri)
predictions = model.predict(X_test)
```

### Spark DataFrame inference

```python
predict_udf = mlflow.pyfunc.spark_udf(spark, model_uri=model_uri, result_type="string")
display(test_df.withColumn("income_predicted", predict_udf()))
```

^[train-classification-models-with-automl-python-api-databricks-on-aws.md, train-regression-models-with-automl-python-api-databricks-on-aws.md]

## Model Registration and Deployment

Models trained by AutoML can be registered and deployed through the [MLflow Model Registry](/concepts/mlflow-model-registry.md) like any other MLflow model. ^[train-classification-models-with-automl-python-api-databricks-on-aws.md]

### Troubleshooting: pandas dependency error

When serving an AutoML-trained model with [Model Serving](/concepts/model-serving.md), you may encounter the error `No module named pandas.core.indexes.numeric`. This occurs when the `pandas` version used during training differs from the serving environment. To resolve this: ^[train-classification-models-with-automl-python-api-databricks-on-aws.md, train-regression-models-with-automl-python-api-databricks-on-aws.md]

1. Download the `add-pandas-dependency.py` script (available in the Databricks documentation)
2. Edit the script to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md)
3. Run the script to pin `pandas==1.5.3` in `requirements.txt` and `conda.yaml`
4. Re-register the model
5. Serve the new model version

## Key Parameters

Common parameters across all methods include:

| Parameter | Description |
|-----------|-------------|
| `dataset` | Training data (pandas DataFrame, PySpark DataFrame, or file path string) |
| `target_col` | Name of the target column to predict |
| `primary_metric` | Evaluation metric (default varies by task) |
| `timeout_minutes` | Maximum run duration (replaces deprecated `max_trials`) |
| `experiment_dir` | Directory for experiment output |
| `experiment_name` | Name for the experiment (Databricks Runtime 12.1 ML and above) |
| `exclude_cols` | Columns to exclude from training |
| `exclude_frameworks` | Frameworks to exclude from trials |
| `feature_store_lookups` | Feature store lookups (Databricks Runtime 11.3 LTS ML and above) |
| `imputers` | Custom imputation strategies (Databricks Runtime 10.4 LTS ML and above) |
| `sample_weight_col` | Column containing sample weights |
| `split_col` | Custom train/test split column |

^[automl-python-api-reference-databricks-on-aws.md]

## Return Objects

### AutoMLSummary

The summary object contains:
- `best_trial`: The [TrialInfo](/concepts/trialinfo.md) for the best-performing trial
- `trials`: A list of all [TrialInfo](/concepts/trialinfo.md) objects
- Methods to access metrics, parameters, and model paths

### TrialInfo

Each trial object includes:
- `artifact_uri`: URI for the notebook artifact
- `model_path`: Path to load the trained model
- Metrics and parameters for that trial

### ImportNotebookResult

Contains:
- `path`: The destination path of the imported notebook
- `url`: The URL to the imported notebook

^[automl-python-api-reference-databricks-on-aws.md]

## Iterating on AutoML Results

After an AutoML run, you can:
1. Explore the generated notebooks and experiments
2. Clone the best trial notebook and modify hyperparameters or preprocessing steps
3. Train an improved model and note its artifact URI for inference

^[train-regression-models-with-automl-python-api-databricks-on-aws.md]

## Related Concepts

- What is AutoML? — The low-code UI option for AutoML on Databricks
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Required runtime environment
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model management
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Model versioning and deployment
- [Model Serving](/concepts/model-serving.md) — Production deployment for AutoML models
- [Feature Store](/concepts/feature-store.md) — Feature management and lookups for AutoML runs

## Sources

- automl-python-api-reference-databricks-on-aws.md
- train-classification-models-with-automl-python-api-databricks-on-aws.md
- train-regression-models-with-automl-python-api-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
2. [train-classification-models-with-automl-python-api-databricks-on-aws.md](/references/train-classification-models-with-automl-python-api-databricks-on-aws-db7a11ef.md)
3. [train-regression-models-with-automl-python-api-databricks-on-aws.md](/references/train-regression-models-with-automl-python-api-databricks-on-aws-b83f8bc4.md)
