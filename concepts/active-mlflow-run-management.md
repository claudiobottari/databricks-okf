---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02ecbcce37212c0cdf012f62383089f780c62f28254a08f4ed1daadc027ed99a
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - active-mlflow-run-management
    - AMRM
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
      start: 31
      end: 33
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
      start: 31
      end: 36
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
      start: 24
      end: 26
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
      start: 36
      end: 38
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
      start: 21
      end: 26
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
      start: 1
      end: 8
title: Active MLflow run management
description: The practice of wrapping fit() calls inside a 'with mlflow.start_run():' statement to ensure tuning information is logged under its own MLflow main run for better organization.
tags:
  - mlflow
  - best-practices
  - experiment-tracking
timestamp: "2026-06-18T10:47:17.732Z"
---

# Active [MLflow Run](/concepts/mlflow-run.md) management

**Active [MLflow Run](/concepts/mlflow-run.md) management** refers to the practice of explicitly wrapping a machine learning model training call—such as `fit()` in Apache Spark MLlib—inside a `with mlflow.start_run():` context manager. This ensures that all logging for that training operation occurs under a dedicated MLflow main run, rather than being merged into an existing active run or handled automatically by the framework.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:31-33]

## Why it is recommended

When using [MLlib Automated MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md) (or any [MLflow Tracking](/concepts/mlflow-tracking.md) integration), Databricks recommends active [MLflow Run](/concepts/mlflow-run.md) management when calling `fit()` from `CrossValidator` or `TrainValidationSplit`. Wrapping the call in `with mlflow.start_run():` guarantees that:

- The hyperparameters, evaluation metrics, and other artifacts are logged under a distinct MLflow main run.
- You can easily add custom tags, parameters, or metrics to that specific run without affecting other runs.
- The run lifecycle is explicitly controlled, avoiding unintended side effects from reusing a previously started run.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:31-36]

## Default behavior without active management

If no active [MLflow Run](/concepts/mlflow-run.md) exists when `fit()` is called, the MLlib automated tracking creates a new run, logs the tuning results to it, and ends the run before returning. If an active run already exists, the information is logged to that existing run, and the active run is **not** stopped.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:24-26]

## Behavior when calling `fit()` multiple times

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), the library logs all those invocations to the same main run. To avoid name conflicts for MLflow parameters and tags, MLflow appends a UUID to any names that would otherwise collide. This ensures each parameter and tag remains unique within that run.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:36-38]

## Nested run structure

In MLlib automated MLflow tracking, the tuning process creates a nested run structure:

- **Main (parent) run**: Information about the `CrossValidator` or `TrainValidationSplit` itself—estimator, evaluator, and overall configuration.
- **Child runs**: A child run for every hyperparameter setting tested, recording the parameter values and the corresponding evaluation metric.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:21-26]

Active run management places the main run explicitly within the `with mlflow.start_run():` block, giving you full control over that parent run's lifecycle.

## Deprecation note

MLlib automated MLflow tracking is deprecated on clusters running Databricks Runtime 10.1 ML and above and disabled by default on Databricks Runtime 10.2 ML and above. Databricks recommends using [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) by calling `mlflow.pyspark.ml.autolog()` instead. However, the concept of active [MLflow Run](/concepts/mlflow-run.md) management—explicitly starting and ending runs—remains a best practice for any MLflow tracking scenario, not just for MLlib.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:1-8]

## Related concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core logging component of MLflow
- [MLlib Automated MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md) — The deprecated automatic tracking feature for MLlib tuning
- [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) — The recommended replacement for automated tracking
- [Databricks Autologging](/concepts/databricks-autologging.md) — Automatic MLflow logging for common ML frameworks
- [MLflow Runs](/concepts/mlflow-run.md) — The fundamental unit of logged experiments

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:31-33](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
2. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:31-36](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
3. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:24-26](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
4. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:36-38](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
5. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:21-26](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
6. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md:1-8](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
