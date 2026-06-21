---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 100ee3e87426629ecbd532da5fe45905e65e23bb705e15be86c8eb55a4f3176e
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mllib-mlflow-tracking-deprecation
    - DMMTD
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Databricks MLlib MLflow Tracking Deprecation
description: MLlib automated MLflow tracking is deprecated on Databricks Runtime 10.1 ML and above, disabled by default from 10.2 ML onwards, with mlflow.pyspark.ml.autolog() as the recommended replacement.
tags:
  - databricks
  - deprecation
  - mlflow
  - migration
timestamp: "2026-06-19T14:01:54.564Z"
---

# Databricks MLlib MLflow Tracking Deprecation

**Databricks MLlib MLflow Tracking Deprecation** refers to the retirement of automated MLflow tracking for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) model tuning on Databricks clusters running Runtime 10.1 ML and above. The feature is disabled by default from Runtime 10.2 ML onward, and users are directed to migrate to [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md).

## Overview

MLlib automated MLflow Tracking automatically logged hyperparameters and evaluation metrics when using `CrossValidator` or `TrainValidationSplit` for model tuning, without requiring explicit API calls to MLflow. This feature is now deprecated and no longer supported in recent Databricks Runtime versions.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Deprecation Timeline

| Databricks Runtime Version | Status |
|---------------------------|--------|
| 10.1 ML and above         | Deprecated |
| 10.2 ML and above         | Disabled by default |

^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

The deprecation applies to clusters running these Runtime versions. The documentation for this feature has been retired and may not be updated; the products, services, or technologies mentioned are no longer supported.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Recommended Migration

Instead of the deprecated MLlib MLflow Tracking, users should use [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) by calling `mlflow.pyspark.ml.autolog()`. This autologging function is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md).^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Enabling the Deprecated Feature (Not Recommended)

To use the old MLlib automated MLflow tracking in Databricks Runtime 10.2 ML or above, enable it by setting the following Spark configurations:

```plaintext
spark.databricks.mlflow.trackMLlib.enabled true
spark.databricks.mlflow.autologging.enabled false
```

These configurations are set in the cluster's Spark configuration UI (Compute > Configure > Spark configuration).^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## How the Deprecated Feature Worked

When enabled, the legacy tracking logged tuning results as nested MLflow runs:

- **Main or parent run:** Information for the `CrossValidator` or `TrainValidationSplit` is logged to the main run. If an active [MLflow Run](/concepts/mlflow-run.md) already exists, information is logged to that active run and it is not stopped. If there is no active run, MLflow creates a new run, logs to it, and ends the run before returning.
- **Child runs:** Each hyperparameter setting tested and the corresponding evaluation metric are logged to a child run under the main run.

Databricks recommended active [MLflow Run](/concepts/mlflow-run.md) management by wrapping `fit()` calls inside a `with mlflow.start_run():` statement to ensure clean logging and easier tagging. When `fit()` is called multiple times within the same active run, MLflow logs those multiple runs to the same main run and appends a UUID to resolve name conflicts for parameters and tags.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Supported Languages

The deprecated automated tracking was only supported for Python notebooks. MLflow Tracking for model tuning in R and Scala required explicit API calls and was never automated via this feature.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – Open source platform for managing ML lifecycle
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Component for logging parameters, metrics, and artifacts
- [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) – Current recommended autologging for PySpark ML
- [Databricks Autologging](/concepts/databricks-autologging.md) – Default automatic logging for MLflow on Databricks
- [CrossValidator](/concepts/crossvalidator.md) – Spark MLlib model tuning estimator
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) – Spark MLlib model tuning estimator

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
