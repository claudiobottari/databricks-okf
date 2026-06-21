---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf556bd503656cc176c4d5536b39aad5e64bc78c71b0402578bbc74aaa5b8207
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - crossvalidator-and-trainvalidationsplit-mlflow-integration
    - TrainValidationSplit MLflow Integration and CrossValidator
    - CATMI
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: CrossValidator and TrainValidationSplit MLflow Integration
description: The two Spark MLlib model tuning estimators that, when used with MLlib automated MLflow tracking, automatically log tuning results as nested MLflow runs without requiring explicit API calls.
tags:
  - spark-mllib
  - machine-learning
  - model-tuning
timestamp: "2026-06-18T14:26:27.967Z"
---

# CrossValidator and TrainValidationSplit MLflow Integration

**CrossValidator and TrainValidationSplit MLflow Integration** refers to the automatic logging of hyperparameters and evaluation metrics to [MLflow](/concepts/mlflow.md) when tuning machine learning models using [Apache Spark MLlib](/concepts/apache-spark-mllib.md)'s `CrossValidator` or `TrainValidationSplit`. This integration eliminates the need for explicit MLflow API calls during model tuning workflows.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Overview

MLlib automated MLflow tracking logs tuning results as nested MLflow runs:^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

- **Main or parent run**: Information for the `CrossValidator` or `TrainValidationSplit` is logged to the main run. If an active run already exists, information is logged to that active run and the active run is not stopped. If no active run exists, MLflow creates a new run, logs to it, and ends the run before returning.
- **Child runs**: Each hyperparameter setting tested and its corresponding evaluation metric are logged to a child run under the main run.

## Recommended Usage

When calling `fit()`, Databricks recommends active [MLflow Run](/concepts/mlflow-run.md) management by wrapping the call inside a `with mlflow.start_run():` statement. This ensures that information is logged under its own MLflow main run and makes it easier to log additional tags, parameters, or metrics to that run.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

```python
import mlflow

with mlflow.start_run():
    # CrossValidator or TrainValidationSplit .fit() call
    model = cross_validator.fit(training_data)
```

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), it logs those multiple runs to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to names with conflicts.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Deprecation Status

MLlib automated MLflow tracking is deprecated on clusters that run Databricks Runtime 10.1 ML and above, and it is disabled by default on clusters running Databricks Runtime 10.2 ML and above.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Migration Path

Instead of using the deprecated MLlib automated MLflow tracking, use [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) by calling [`mlflow.pyspark.ml.autolog()`](https://www.mlflow.org/docs/latest/python_api/mlflow.pyspark.ml.html#mlflow.pyspark.ml.autolog), which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md).^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

```python
mlflow.pyspark.ml.autolog()
```

### Re-enabling the Legacy Integration

To use the old MLlib automated MLflow tracking in Databricks Runtime 10.2 ML or above, enable it by setting the following Spark configurations:^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

```
spark.databricks.mlflow.trackMLlib.enabled true
spark.databricks.mlflow.autologging.enabled false
```

## Benefits

With MLlib automated MLflow tracking, when you run tuning code that uses `CrossValidator` or `TrainValidationSplit`, hyperparameters and evaluation metrics are automatically logged in MLflow. Without this integration, you must make explicit API calls to log to MLflow manually.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core MLflow component for logging experiments
- [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) — The recommended replacement for this integration
- [Databricks Autologging](/concepts/databricks-autologging.md) — Automatic logging of models and metrics
- [CrossValidator](/concepts/crossvalidator.md) — Spark MLlib's cross-validation estimator
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) — Spark MLlib's train-validation split estimator
- [Spark MLlib](/concepts/apache-spark-mllib.md) — Apache Spark's machine learning library

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
