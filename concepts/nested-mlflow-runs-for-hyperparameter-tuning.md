---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa8a21eda9f8b1c6838e18a34b5e4a97d5b04a65d9c27d9ac0e6ee361b7670ce
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nested-mlflow-runs-for-hyperparameter-tuning
    - NMRFHT
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Nested MLflow Runs for Hyperparameter Tuning
description: A pattern where CrossValidator or TrainValidationSplit logs tuning results as a parent run (containing the estimator metadata) and child runs (one per hyperparameter setting tested, with its evaluation metric).
tags:
  - mlflow
  - machine-learning
  - experiment-tracking
timestamp: "2026-06-18T14:26:08.205Z"
---

---
title: Nested MLflow runs for hyperparameter tuning
summary: An organizational pattern where CrossValidator or TrainValidationSplit tuning results are logged as a parent run (for the tuning estimator) with child runs for each hyperparameter setting tested.
sources:
  - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:46:47.774Z"
updatedAt: "2026-06-18T10:46:47.774Z"
tags:
  - mlflow
  - experiment-tracking
  - hyperparameter-tuning
aliases:
  - nested-mlflow-runs-for-hyperparameter-tuning
  - NMRFHT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Nested MLflow runs for hyperparameter tuning

When using **Apache Spark MLlib** with automated MLflow tracking, hyperparameter tuning with `CrossValidator` or `TrainValidationSplit` logs results as **nested MLflow runs**. This structure organizes tuning experiments into a parent run containing multiple child runs, one for each hyperparameter setting tested. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Run structure

- **Main or parent run**: The information for the tuning estimator (`CrossValidator` or `TrainValidationSplit`) is logged to the main run. If an [MLflow Run](/concepts/mlflow-run.md) is already active, information is logged to that active run and the run is not stopped. If there is no active run, MLflow creates a new run, logs to it, and ends the run before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]
- **Child runs**: Each hyperparameter setting tested, along with its corresponding evaluation metric, is logged as a child run under the main run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Recommended run management

When calling `fit()`, Databricks recommends wrapping the call inside a `with mlflow.start_run():` statement. This ensures that the information is logged under its own MLflow main run, and makes it easier to log additional tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Note on multiple `fit()` calls

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), the multiple runs are logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to names with conflicts. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Deprecation and alternatives

MLlib automated MLflow tracking is deprecated on clusters running **Databricks Runtime 10.1 ML and above**, and disabled by default in **Databricks Runtime 10.2 ML and above**. For these versions, use [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) by calling `mlflow.pyspark.ml.autolog()`, which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md). ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

To re-enable the old MLlib automated MLflow tracking in Databricks Runtime 10.2 ML or above, set the Spark configurations `spark.databricks.mlflow.trackMLlib.enabled true` and `spark.databricks.mlflow.autologging.enabled false`. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related concepts

- [MLflow](/concepts/mlflow.md) — The open source platform for managing the end-to-end machine learning lifecycle
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The component that records runs, parameters, metrics, and artifacts
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — The machine learning library built on Apache Spark
- [CrossValidator](/concepts/crossvalidator.md) — MLlib estimator for model selection via cross-validation
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) — MLlib estimator for model selection via train-validation split
- [Databricks Autologging](/concepts/databricks-autologging.md) — Automatic MLflow tracking for common ML frameworks

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
