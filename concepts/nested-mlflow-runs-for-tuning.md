---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 679a055f96b1936bb29e6d9d44d5bb624d01b22b8c096743a64424cbc8fd965a
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nested-mlflow-runs-for-tuning
    - NMRFT
    - Nested MLflow Runs
    - Nested Runs
    - nested-mlflow-runs-for-hyperparameter-tuning
    - NMRFHT
    - nested-mlflow-runs-for-model-tuning
    - NMRFMT
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Nested MLflow Runs for Tuning
description: Pattern where CrossValidator or TrainValidationSplit log tuning results as nested MLflow runs with a parent run for the estimator and child runs for each hyperparameter setting tested
tags:
  - mlflow
  - machine-learning
  - hyperparameter-tuning
  - apache-spark
timestamp: "2026-06-19T09:00:27.795Z"
---

# Nested MLflow Runs for Tuning

**Nested MLflow Runs for Tuning** is a mechanism used by [MLflow](/concepts/mlflow.md) when tracking hyperparameter optimization workflows in [Apache Spark MLlib](/concepts/apache-spark-mllib.md). When a tuning estimator such as `CrossValidator` or `TrainValidationSplit` calls `fit()`, it automatically organizes the results as a hierarchy of MLflow runs: one main (parent) run representing the overall tuning process, and one child run for each hyperparameter combination that is tested. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Main Run (Parent)

The main run logs the overall information for the `CrossValidator` or `TrainValidationSplit` operation. If an [MLflow Run](/concepts/mlflow-run.md) is already active when `fit()` is called, the tuning information is logged into that active run and the active run is **not** stopped. If no run is active, MLflow creates a new run, logs the data to it, and ends the run before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Child Runs

Each hyperparameter setting tested by the tuning estimator, along with its corresponding evaluation metric, is recorded in a child run. These child runs appear nested under the main run in the MLflow UI, allowing easy comparison of parameter configurations. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Best Practices

Databricks recommends wrapping calls to `fit()` inside a `with mlflow.start_run():` statement. This practice ensures that the tuning results are logged under a dedicated main run, and makes it straightforward to add custom tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

If `fit()` is called multiple times inside the same active [MLflow Run](/concepts/mlflow-run.md), all those calls are logged into the same main run. To avoid name collisions for MLflow parameters and tags, MLflow appends a UUID to any names that conflict. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Deprecation Note

The automated MLlib MLflow tracking described above is **deprecated** on clusters running Databricks Runtime 10.1 ML and later, and is **disabled by default** starting with Databricks Runtime 10.2 ML. For current development, use `mlflow.pyspark.ml.autolog()` by calling `mlflow.pyspark.ml.autolog()`; this newer autologging is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md). If you need to re-enable the legacy MLlib automated tracking on Databricks Runtime 10.2 ML or later, set the Spark configurations `spark.databricks.mlflow.trackMLlib.enabled true` and `spark.databricks.mlflow.autologging.enabled false`. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) – Core component for logging experiments.
- [CrossValidator](/concepts/crossvalidator.md) – MLlib tuning method that uses cross-validation.
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) – MLlib tuning method that uses a single train-validation split.
- MLlib – Apache Spark’s machine learning library.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – General concept of optimizing model parameters.
- [Databricks Autologging](/concepts/databricks-autologging.md) – Default [MLflow Autologging](/concepts/mlflow-autologging.md) in recent Databricks Runtimes.

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
