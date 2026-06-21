---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5ba63a444b18bdc03f31904a3a4d0ca4d2563d738344374fa2adc8243c99a255
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-active-run-management-with-fit
    - MARMWF
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: MLflow Active Run Management with fit()
description: Best practice of wrapping CrossValidator.fit() or TrainValidationSplit.fit() calls inside a 'with mlflow.start_run():' block to ensure tuning results are logged under a dedicated parent run and to simplify adding custom tags, parameters, or metrics.
tags:
  - mlflow
  - best-practices
  - spark-mllib
timestamp: "2026-06-19T17:34:21.356Z"
---

# MLflow Active Run Management with fit()

**MLflow Active Run Management with fit()** refers to the recommended practice of wrapping calls to `CrossValidator.fit()` or `TrainValidationSplit.fit()` inside an explicit `mlflow.start_run()` context when using [Apache Spark MLlib](/concepts/apache-spark-mllib.md) automated MLflow tracking. This approach ensures that hyperparameter tuning results are logged under a dedicated MLflow main run, improving organization and traceability. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Overview

When using MLlib automated MLflow tracking with `CrossValidator` or `TrainValidationSplit`, tuning results are logged as nested MLflow runs:

- **Main (parent) run**: Information for the `CrossValidator` or `TrainValidationSplit` is logged to the main run. If an active run already exists, information is logged to that active run and the active run is not stopped. If no active run exists, MLflow creates a new run, logs to it, and ends the run before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]
- **Child runs**: Each hyperparameter setting tested and its corresponding evaluation metric are logged as a child run under the main run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Recommended Practice

Databricks recommends wrapping the call to `fit()` inside a `with mlflow.start_run():` statement. This ensures that the information is logged under its own MLflow main run and makes it easier to log additional tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

```python
import mlflow

with mlflow.start_run():
    # Additional tags, parameters, or metrics can be logged here
    model = cross_validator.fit(training_data)
```

## Behavior with Multiple fit() Calls

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), those multiple runs are logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to names with conflicts. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Deprecation Notice

MLlib automated MLflow tracking is deprecated on clusters running Databricks Runtime 10.1 ML and above, and it is disabled by default on clusters running Databricks Runtime 10.2 ML and above. Instead, use [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) by calling `mlflow.pyspark.ml.autolog()`, which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md). ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

To use the old MLlib automated MLflow tracking in Databricks Runtime 10.2 ML or above, enable it by setting the Spark configurations `spark.databricks.mlflow.trackMLlib.enabled true` and `spark.databricks.mlflow.autologging.enabled false`. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) – The core MLflow component for logging parameters, metrics, and artifacts.
- [MLflow Nested Runs](/concepts/mlflow-run.md) – The hierarchical run structure used by MLlib automated tracking.
- [CrossValidator](/concepts/crossvalidator.md) – Spark MLlib's cross-validation estimator for hyperparameter tuning.
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) – Spark MLlib's train-validation split estimator for hyperparameter tuning.
- [Databricks Autologging](/concepts/databricks-autologging.md) – Automatic MLflow logging for machine learning workflows.

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
