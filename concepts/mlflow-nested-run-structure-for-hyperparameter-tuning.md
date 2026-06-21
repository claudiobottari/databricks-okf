---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0dbcbbd121b8b3cad8d630be6e8bc80ed1881785c7bdec611321044682852be
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-nested-run-structure-for-hyperparameter-tuning
    - MNRSFHT
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: MLflow Nested Run Structure for Hyperparameter Tuning
description: "How MLlib automated MLflow tracking organizes tuning results: a parent run for the CrossValidator/TrainValidationSplit and child runs for each hyperparameter setting tested."
tags:
  - mlflow
  - experiment-tracking
  - hyperparameter-tuning
timestamp: "2026-06-19T14:01:51.829Z"
---

# MLflow Nested Run Structure for Hyperparameter Tuning

**MLflow Nested Run Structure for Hyperparameter Tuning** refers to the hierarchical organization of MLflow runs that is automatically created when tuning [Apache Spark MLlib](/concepts/apache-spark-mllib.md) models using `CrossValidator` or `TrainValidationSplit`. In this structure, the overall tuning operation is recorded as a parent run, and each individual hyperparameter setting tested is recorded as a child run, enabling clear traceability and comparison of evaluation results.

## Overview

When automated MLflow tracking is enabled for MLlib model tuning, calls to `CrossValidator.fit()` or `TrainValidationSplit.fit()` produce nested MLflow runs. This design groups all trials together under a single parent run, making it easy to inspect the full tuning experiment and drill into individual configurations. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Structure

The nested run structure consists of two levels:

### Main (Parent) Run

The main run captures the information for the `CrossValidator` or `TrainValidationSplit` itself. If there is already an active [MLflow Run](/concepts/mlflow-run.md) when `fit()` is called, the tuning information is logged to that active run and the run is not stopped. If no active run exists, MLflow creates a new run, logs to it, and ends the run before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Child Runs

Each hyperparameter setting that is evaluated during tuning is logged as a separate child run under the main run. The child run records the specific parameters tested and the corresponding evaluation metric(s). ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Active Run Management

Databricks recommends wrapping the call to `fit()` inside a `with mlflow.start_run():` statement. This active run management ensures that the tuning information is logged under its own dedicated MLflow main run, and it simplifies the process of logging additional tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

```python
with mlflow.start_run():
    model = crossval.fit(training_data)
```

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), all of those tuning jobs are logged under the same main run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Name Conflict Resolution

Because multiple child runs or repeated `fit()` calls may produce parameters and tags with identical names, MLflow automatically appends a UUID to any names that would otherwise conflict. This ensures that all entries remain unique within the run hierarchy. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Deprecation Note

MLlib automated MLflow tracking is deprecated on clusters that run Databricks Runtime 10.1 ML and above, and it is disabled by default on clusters running Databricks Runtime 10.2 ML and above. Databricks recommends using MLflow PySpark ML autologging by calling `mlflow.pyspark.ml.autolog()` instead, which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md). To re‑enable the old MLlib automated tracking on Databricks Runtime 10.2 ML or later, set the Spark configurations `spark.databricks.mlflow.trackMLlib.enabled true` and `spark.databricks.mlflow.autologging.enabled false`. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [CrossValidator](/concepts/crossvalidator.md)
- [TrainValidationSplit](/concepts/trainvalidationsplit.md)
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- [Databricks Autologging](/concepts/databricks-autologging.md)
- [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md)
- [MLflow Runs](/concepts/mlflow-run.md)

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
