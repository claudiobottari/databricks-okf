---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e0bdfbab51225c5a346a7a3dc2636dfd750f72398c98b6c541b72f373bb94e39
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trainvalidationsplit
    - Train-Validation Split
    - Train-Validation-Test Split
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: TrainValidationSplit
description: A Spark MLlib model tuning tool that, when used with MLlib automated MLflow tracking, automatically logs hyperparameter settings and evaluation metrics as nested MLflow runs.
tags:
  - machine-learning
  - spark-mllib
  - model-tuning
timestamp: "2026-06-18T10:46:51.437Z"
---

# TrainValidationSplit

**TrainValidationSplit** is a model tuning tool in [Apache Spark MLlib](/concepts/apache-spark-mllib.md) used to evaluate and select the best model by splitting the training data into a single training set and a validation set. It works similarly to [CrossValidator](/concepts/crossvalidator.md) but uses one train‑validation split rather than k‑fold cross‑validation. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

In Databricks, when you run tuning code that uses `TrainValidationSplit` (or `CrossValidator`), hyperparameters and evaluation metrics are automatically logged to [MLflow Tracking](/concepts/mlflow-tracking.md) through automated MLflow tracking. This eliminates the need for explicit MLflow API calls to record tuning results. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

---

## [MLflow Run](/concepts/mlflow-run.md) structure

`TrainValidationSplit` logs tuning results as nested MLflow runs:

- **Main (parent) run**: Information for the `TrainValidationSplit` is logged to the main run. If there is an active run already, information is logged to that active run. If there is no active run, MLflow creates a new run, logs to it, and ends the run before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]
- **Child runs**: Each hyperparameter setting tested and the corresponding evaluation metric are logged to a child run under the main run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

Databricks recommends wrapping the call to `fit()` inside a `with mlflow.start_run():` statement. This ensures the information is logged under its own MLflow main run and makes it easier to log additional tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), multiple runs are logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to conflicting names. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

---

## Deprecation and migration

> ⚠️ The source document for this page has been archived and might not be updated. The following information reflects the state of automated MLlib MLflow tracking at the time of retirement.

MLlib automated MLflow tracking is **deprecated** on clusters that run Databricks Runtime 10.1 ML and above, and it is **disabled by default** on clusters running Databricks Runtime 10.2 ML and above. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

Instead of relying on the deprecated automated tracking, Databricks recommends using **MLflow PySpark ML autologging** by calling `mlflow.pyspark.ml.autolog()`, which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md). ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

To re‑enable the old MLlib automated MLflow tracking in Databricks Runtime 10.2 ML or above, set the following Spark configurations:

```
spark.databricks.mlflow.trackMLlib.enabled true
spark.databricks.mlflow.autologging.enabled false
```

^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

---

## Related concepts

- [CrossValidator](/concepts/crossvalidator.md) – Another MLlib tuning tool that performs k‑fold cross‑validation
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The experiment‑tracking component of MLflow
- [Databricks Autologging](/concepts/databricks-autologging.md) – The modern, recommended approach for automatic MLflow logging
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) – The machine learning library that provides `TrainValidationSplit`

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
