---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43ff494c72483540e7a5171783dda934d9ee20a7fbaa56f7b745d1a84c0add85
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-pyspark-ml-autologging
    - MPMA
    - Spark model logging
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: MLflow PySpark ML Autologging
description: The recommended replacement for MLlib automated MLflow tracking, enabled by calling mlflow.pyspark.ml.autolog() and enabled by default with Databricks Autologging on Databricks Runtime 10.1 ML and above.
tags:
  - machine-learning
  - mlflow
  - databricks
  - spark-mllib
timestamp: "2026-06-19T22:06:58.626Z"
---

# MLflow PySpark ML Autologging

**MLflow PySpark ML Autologging** is an automatic tracking mechanism for PySpark ML models that logs parameters, metrics, and fitted models without requiring explicit `mlflow.log_*()` API calls. It is the recommended replacement for the deprecated [Apache Spark MLlib automated MLflow tracking](/concepts/mllib-automated-mlflow-tracking.md). ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Overview

When you train a PySpark ML model using classes such as `CrossValidator` or `TrainValidationSplit`, MLflow PySpark ML Autologging automatically captures hyperparameters, evaluation metrics, and the fitted model, and logs them to the active [MLflow Run](/concepts/mlflow-run.md). If no active run exists, it creates a new run, logs to it, and ends the run before returning. This reduces boilerplate code and ensures consistent tracking across experiments. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Run Hierarchy

`CrossValidator` or `TrainValidationSplit` log tuning results as nested MLflow runs: ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

- **Main (parent) run**: Information for the tuning estimator itself is logged to the main run.
- **Child runs**: Each hyperparameter setting tested and its corresponding evaluation metric are logged to a child run under the main run.

## Enabling and Default Behavior

Autologging is enabled by calling `mlflow.pyspark.ml.autolog()`. On Databricks, this function is **enabled by default** as part of [Databricks Autologging](/concepts/databricks-autologging.md) on clusters running Databricks Runtime 10.2 ML and above. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Explicit Activation

```python
import mlflow.pyspark.ml
mlflow.pyspark.ml.autolog()
```

## Relation to Deprecated MLlib Automated Tracking

The older MLlib automated MLflow tracking (for Spark MLlib tuning) is deprecated on clusters that run Databricks Runtime 10.1 ML and above, and disabled by default from Databricks Runtime 10.2 ML onward. Users are encouraged to migrate to MLflow PySpark ML Autologging, which works with the broader PySpark ML library rather than only MLlib tuning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

To re-enable the deprecated MLlib tracking on Databricks Runtime 10.2 ML or above, set the following Spark configurations: ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

```
spark.databricks.mlflow.trackMLlib.enabled true
spark.databricks.mlflow.autologging.enabled false
```

## Usage Notes

- When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), results are logged to that same parent run. To avoid name conflicts for parameters and tags, MLflow appends a UUID to the conflicting names. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]
- Databricks recommends wrapping `fit()` inside a `with mlflow.start_run():` block. This ensures each training invocation runs under its own parent run, making it easier to log additional tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Example

The following snippet demonstrates typical usage after enabling autologging: ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

```python
import mlflow
import mlflow.pyspark.ml

mlflow.pyspark.ml.autolog()

with mlflow.start_run(run_name="my_pyspark_run"):
    # CrossValidator or TrainValidationSplit fitting
    model = cross_validator.fit(training_data)
    # Parameters and metrics are automatically logged
```

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) — Broader automatic MLflow tracking on Databricks
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The underlying tracking system
- [Apache Spark MLlib automated MLflow tracking](/concepts/mllib-automated-mlflow-tracking.md) — The deprecated predecessor
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — General approaches for tuning models
- [CrossValidator and TrainValidationSplit](/concepts/crossvalidator-and-trainvalidationsplit.md) — PySpark ML tuning estimators

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
