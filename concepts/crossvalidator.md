---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3091063243aae47391c94d394b3f14b8024f24cd28091914e0130f21ceddab68
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - crossvalidator
    - Cross-Validation
    - Cross-validation
    - cross-validation
    - Cross-Validation (Spark)
    - Cross-Validation in Spark ML
    - MLlib Cross-Validation
    - MLlib Cross‑Validation
    - MLlib cross-validation pipeline
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: CrossValidator
description: A Spark MLlib model tuning tool that, when used with MLlib automated MLflow tracking, automatically logs hyperparameter settings and evaluation metrics to MLflow as nested runs.
tags:
  - machine-learning
  - spark-mllib
  - model-tuning
timestamp: "2026-06-18T10:47:17.146Z"
---

# CrossValidator

**CrossValidator** is a model tuning tool in [Apache Spark MLlib](/concepts/apache-spark-mllib.md) that performs cross-validation to select the best model from a grid of hyperparameters. It evaluates each combination of parameters by splitting the training data into multiple folds, training the model on a subset of folds, and evaluating it on the remaining fold.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Automated MLflow Tracking

CrossValidator supports automated [MLflow Tracking](/concepts/mlflow-tracking.md) integration, which automatically logs hyperparameters and evaluation metrics without requiring explicit API calls. This automated tracking is available for Python notebooks in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md).^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Run Structure

When CrossValidator runs with automated MLflow tracking, it logs tuning results as nested MLflow runs:^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

- **Main (parent) run**: Information about the CrossValidator itself is logged to the main run. If an active run already exists, information is logged to that active run and it is not stopped. If no active run exists, MLflow creates a new run, logs to it, and ends the run before returning.
- **Child runs**: Each hyperparameter setting tested and its corresponding evaluation metric are logged to a child run under the main run.

When calling `fit()`, Databricks recommends wrapping the call inside a `with mlflow.start_run():` statement to ensure information is logged under its own MLflow main run and to simplify logging additional tags, parameters, or metrics.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Deprecation Status

MLlib automated MLflow tracking is deprecated on clusters running Databricks Runtime 10.1 ML and above, and is disabled by default on clusters running Databricks Runtime 10.2 ML and above. Instead, use [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) by calling `mlflow.pyspark.ml.autolog()`, which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md).^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

To use the old MLlib automated MLflow tracking in Databricks Runtime 10.2 ML or above, enable it by setting the Spark configurations `spark.databricks.mlflow.trackMLlib.enabled true` and `spark.databricks.mlflow.autologging.enabled false`.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Multiple Fit Calls

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), multiple runs are logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to names with conflicts.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Relationship to TrainValidationSplit

CrossValidator is similar to [TrainValidationSplit](/concepts/trainvalidationsplit.md), another Spark MLlib model tuning tool. Both support automated MLflow tracking, logging hyperparameters and evaluation metrics for each parameter combination tested. The key difference is that CrossValidator uses k-fold cross-validation, while TrainValidationSplit uses a single train-validation split.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — Open source platform for managing the machine learning lifecycle
- [MLflow Tracking](/concepts/mlflow-tracking.md) — MLflow component for logging parameters, metrics, and artifacts
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) — Alternative model tuning approach using single train-validation split
- [Databricks Autologging](/concepts/databricks-autologging.md) — Automatic MLflow logging for common ML frameworks
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Databricks Runtime optimized for ML workloads

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
