---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 81328764db1d006eeb5f9e969a22d25985d64133e807653254da2a0445d4fe0c
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - crossvalidator-and-trainvalidationsplit
    - TrainValidationSplit and CrossValidator
    - CAT
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: CrossValidator and TrainValidationSplit
description: Spark MLlib model tuning utilities whose hyperparameter search results are automatically logged as nested MLflow runs when automated tracking is enabled.
tags:
  - spark-mllib
  - machine-learning
  - model-tuning
timestamp: "2026-06-19T22:06:48.489Z"
---

# CrossValidator and TrainValidationSplit

**CrossValidator** and **TrainValidationSplit** are model tuning tools in [Apache Spark MLlib](/concepts/apache-spark-mllib.md) that perform hyperparameter search through cross-validation or train-validation splitting. In Databricks, when used with automated [MLflow Tracking](/concepts/mlflow-tracking.md), these tools log hyperparameters and evaluation metrics without requiring explicit API calls. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Automated MLflow Tracking

Automated MLflow Tracking for MLlib model tuning is available for Python notebooks on [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). When tuning code runs `CrossValidator` or `TrainValidationSplit`, hyperparameters and evaluation metrics are automatically logged to MLflow. Without this automation, you must make explicit logging API calls. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

> **Note**: This feature is deprecated on clusters running Databricks Runtime 10.1 ML and above, and is disabled by default on clusters running Databricks Runtime 10.2 ML and above. Databricks recommends using `mlflow.pyspark.ml.autolog()` instead, which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md). ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Nested Run Structure

`CrossValidator` and `TrainValidationSplit` log tuning results as nested MLflow runs: ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

- **Parent run** (main run): Logs information about the `CrossValidator` or `TrainValidationSplit` itself. If an active run already exists, information is logged to that active run. If no active run exists, MLflow creates a new run, logs to it, and ends the run before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]
- **Child runs**: Each hyperparameter setting tested and its corresponding evaluation metric are logged to a child run under the main run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Active Run Management

Databricks recommends wrapping the call to `fit()` inside a `with mlflow.start_run():` statement. This ensures the tuning information is logged under its own MLflow main run and makes it easier to log additional tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), the multiple calls are logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to names that would otherwise collide. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Example

An automated MLflow tracking notebook demonstrates the behavior. After executing the notebook’s final cell, the MLflow UI displays a main run for the `CrossValidator` or `TrainValidationSplit` and nested child runs for each evaluated hyperparameter combination. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) – The core logging and experimentation platform.
- [Databricks Autologging](/concepts/databricks-autologging.md) – The recommended modern approach for automatic MLflow logging.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – General methods for model parameter search.
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) – The machine learning library that provides `CrossValidator` and `TrainValidationSplit`.

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
