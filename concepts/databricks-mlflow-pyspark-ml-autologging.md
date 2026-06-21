---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7441df6709031a814a0347c6440559ce43df673c4c2c8e8a766ec32bcc18116
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-pyspark-ml-autologging
    - DMPMA
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Databricks MLflow PySpark ML autologging
description: The replacement for deprecated MLlib automated MLflow tracking, enabled by default in Databricks Runtime 10.2 ML and above via mlflow.pyspark.ml.autolog() and Databricks Autologging.
tags:
  - mlflow
  - databricks
  - autologging
timestamp: "2026-06-18T10:46:55.608Z"
---

# Databricks MLflow PySpark ML autologging

**MLflow PySpark ML autologging** is a built-in feature that automatically logs parameters, metrics, and models when training PySpark ML estimators. It replaces the older MLlib automated MLflow tracking, which is deprecated on clusters running Databricks Runtime 10.1 ML and above and disabled by default on Databricks Runtime 10.2 ML and above.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Overview

When you call `mlflow.pyspark.ml.autolog()`, MLflow automatically captures hyperparameters and evaluation metrics from PySpark ML pipeline training operations such as `fit()`. This eliminates the need for explicit MLflow Tracking API calls in your Spark ML code.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md] In Databricks workspaces, PySpark ML autologging is enabled by default through [Databricks Autologging](/concepts/databricks-autologging.md), so no explicit call is required in most cases.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Comparison with MLlib automated tracking

The older MLlib automated tracking supported `CrossValidator` and `TrainValidationSplit` from [Apache Spark MLlib](/concepts/apache-spark-mllib.md), logging tuning results as nested MLflow runs. In contrast, PySpark ML autologging covers the broader PySpark ML namespace (`pyspark.ml`) and works with the full set of estimators, transformers, and evaluators in Spark ML.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

| Aspect | MLlib automated tracking (deprecated) | PySpark ML autologging |
|---|---|---|
| API | `spark.databricks.mlflow.trackMLlib.enabled` | `mlflow.pyspark.ml.autolog()` |
| Scope | `mllib.tuning.CrossValidator`, `TrainValidationSplit` | All `pyspark.ml` estimators |
| Default (DBR ≥ 10.2 ML) | Disabled | Enabled |

^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Enabling and disabling

On clusters running Databricks Runtime 10.2 ML and above, PySpark ML autologging is active by default. To manually enable it, call:

```python
import mlflow
mlflow.pyspark.ml.autolog()
```

If you need to restore the older MLlib tracking behavior, you can disable PySpark ML autologging and enable the deprecated MLlib tracking by setting the following Spark configurations on your cluster:

- `spark.databricks.mlflow.trackMLlib.enabled true`
- `spark.databricks.mlflow.autologging.enabled false`

^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## How it logs runs

When you call `fit()` on a PySpark ML estimator, MLflow creates a nested run structure under any active [MLflow Run](/concepts/mlflow-run.md). If no active run exists, MLflow creates a new parent run, logs to it, and ends the run after `fit()` returns. For tuning operations like `CrossValidator` or `TrainValidationSplit`, each hyperparameter combination is logged as a child run under the main run, with its own evaluation metrics. MLflow resolves parameter and tag name conflicts by appending a UUID.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

Databricks recommends wrapping `fit()` calls inside an explicit `with mlflow.start_run():` block to have full control over the parent run and to allow logging additional tags, parameters, or metrics alongside the autologged values.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related concepts

- [MLflow](/concepts/mlflow.md) — Open‑source platform for managing the ML lifecycle
- [Databricks Autologging](/concepts/databricks-autologging.md) — Default automated tracking in Databricks notebooks
- PySpark ML — DataFrame‑based machine learning library in Apache Spark
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The component that logs parameters, metrics, and artifacts
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — Older RDD‑based machine learning library (deprecated for autologging)

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
