---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac639e9175c76205f3501c5583f9af5c73153592aea7d3ad849accf1e890261d
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nested-mlflow-runs-for-model-tuning
    - NMRFMT
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Nested MLflow Runs for Model Tuning
description: The logging structure where CrossValidator or TrainValidationSplit tuning results are organized as parent (main) runs and child runs per hyperparameter setting tested.
tags:
  - mlflow
  - logging
  - machine-learning
timestamp: "2026-06-19T22:07:03.405Z"
---

# Nested MLflow Runs for Model Tuning

**Nested MLflow Runs for Model Tuning** refers to the hierarchical run structure automatically created by [MLflow](/concepts/mlflow.md) when tuning [Apache Spark MLlib](/concepts/apache-spark-mllib.md) models using `CrossValidator` or `TrainValidationSplit`. This structure organizes hyperparameter search results into parent and child runs for clear tracking and comparison.

## Overview

When performing model tuning with MLlib's `CrossValidator` or `TrainValidationSplit`, MLflow automatically logs tuning results as nested runs. This automated tracking eliminates the need for explicit API calls to log hyperparameters and evaluation metrics. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Run Hierarchy

The nested run structure consists of two levels:

### Main (Parent) Run

The information for the `CrossValidator` or `TrainValidationSplit` operation is logged to the main run. If there is already an active [MLflow Run](/concepts/mlflow-run.md), information is logged to that active run without stopping it. If no active run exists, MLflow creates a new run, logs to it, and ends the run before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Child Runs

Each hyperparameter setting tested during tuning is logged as a child run under the main run. Each child run contains the specific parameter combination tested and its corresponding evaluation metric. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Best Practices for Run Management

Databricks recommends active [MLflow Run](/concepts/mlflow-run.md) management when calling `fit()`. Specifically, wrap the call to `fit()` inside a `with mlflow.start_run():` statement. This ensures that tuning information is logged under its own MLflow main run and makes it easier to log additional tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Multiple `fit()` Calls

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), those multiple runs are logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to names with conflicts. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Deprecation Notice

MLlib automated MLflow tracking is deprecated on clusters running Databricks Runtime 10.1 ML and above, and it is disabled by default on clusters running Databricks Runtime 10.2 ML and above. Instead, use [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) by calling `mlflow.pyspark.ml.autolog()`, which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md). ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

To re-enable the old MLlib automated MLflow tracking in Databricks Runtime 10.2 ML or above, set the Spark configurations:
- `spark.databricks.mlflow.trackMLlib.enabled true`
- `spark.databricks.mlflow.autologging.enabled false`

^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core MLflow component for logging and querying experiments.
- [CrossValidator](/concepts/crossvalidator.md) — MLlib's cross-validation estimator for hyperparameter tuning.
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) — MLlib's train-validation split estimator for hyperparameter tuning.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — The broader practice of optimizing model parameters.
- [Databricks Autologging](/concepts/databricks-autologging.md) — Automatic MLflow logging for common ML frameworks.

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
