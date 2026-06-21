---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8423bd0d5c03021730a0a22eadf724eb4594018140d79535365161173f5c138
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - active-mlflow-run-management-in-tuning
    - AMRMIT
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Active MLflow Run Management in Tuning
description: Best practice of wrapping CrossValidator or TrainValidationSplit fit() calls inside a 'with mlflow.start_run():' context to ensure clean parent runs and avoid UUID name conflicts
tags:
  - mlflow
  - best-practice
  - machine-learning
  - apache-spark
timestamp: "2026-06-19T09:00:44.382Z"
---

# Active [MLflow Run](/concepts/mlflow-run.md) Management in Tuning

**Active [MLflow Run](/concepts/mlflow-run.md) Management in Tuning** refers to the practice of explicitly wrapping calls to `fit()` (from `CrossValidator` or `TrainValidationSplit`) inside a `with mlflow.start_run():` context manager to control how tuning results are logged as nested MLflow runs.

## Overview

When using [MLlib Automated MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md), `CrossValidator` or `TrainValidationSplit` log tuning results as nested runs:

- **Main (parent) run**: Contains information for the `CrossValidator` or `TrainValidationSplit` itself.
- **Child runs**: Each hyperparameter setting tested and its corresponding evaluation metric are logged as a child run under the main run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

Without active run management, if there is no active [MLflow Run](/concepts/mlflow-run.md) at the time of calling `fit()`, MLflow automatically creates a new run, logs to it, and ends the run before returning. If there is already an active run, information is logged to that active run and the active run is not stopped. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Recommended Practice

Databricks recommends wrapping the call to `fit()` inside a `with mlflow.start_run():` statement. This approach ensures that tuning information is logged under its own dedicated MLflow main run, making it easier to log additional tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Example

```python
import mlflow

with mlflow.start_run():
    # Additional tags, parameters, or metrics can be logged here
    mlflow.set_tag("model_type", "random_forest")
    
    # CrossValidator or TrainValidationSplit fit() call
    model = cv.fit(training_data)
```

## Important Behavior

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), multiple tuning sessions are logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to names with conflicts. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Benefits

- **Explicit run ownership**: Each tuning session gets its own dedicated main run, avoiding accidental logging to unintended active runs.
- **Organized logging**: Child runs (one per hyperparameter combination) are clearly nested under the parent, improving traceability.
- **Enhanced metadata**: Additional tags, parameters, or metrics can be attached to the main run alongside the automatically logged tuning results. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLlib Automated MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md) – The automated logging system for Spark MLlib tuning
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The core MLflow component for logging experiments
- [CrossValidator](/concepts/crossvalidator.md) – Spark MLlib's cross-validation estimator
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) – Spark MLlib's train-validation split estimator
- [Nested MLflow Runs](/concepts/nested-mlflow-runs-for-tuning.md) – Parent-child run structure used for tuning experiments
- [Databricks Autologging](/concepts/databricks-autologging.md) – Modern alternative for automated MLflow logging

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
