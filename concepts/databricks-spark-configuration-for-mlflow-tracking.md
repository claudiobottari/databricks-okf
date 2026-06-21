---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c8cb54399a86e350752b1624b2a10130b53be215326dea39d3159eaac4f671d
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-spark-configuration-for-mlflow-tracking
    - DSCFMT
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Databricks Spark Configuration for MLflow Tracking
description: Spark configuration flags spark.databricks.mlflow.trackMLlib.enabled and spark.databricks.mlflow.autologging.enabled used to enable or disable legacy MLlib automated MLflow tracking in Databricks Runtime 10.2 ML and above.
tags:
  - databricks
  - spark-configuration
  - mlflow
  - devops
timestamp: "2026-06-19T14:02:33.600Z"
---

# Databricks Spark Configuration for MLflow Tracking

**Databricks Spark Configuration for MLflow Tracking** refers to the Spark settings that control how MLflow integrates with [Apache Spark MLlib](/concepts/apache-spark-mllib.md) for automated tracking of machine learning experiments. These configurations enable or disable the legacy automated MLflow tracking for MLlib model tuning workflows.

## Overview

MLflow provides automated tracking for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) model tuning when using `CrossValidator` or `TrainValidationSplit`. With automated tracking, hyperparameters and evaluation metrics are logged automatically without requiring explicit MLflow API calls. Without automation, you must manually call MLflow tracking APIs. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Legacy Automated Tracking (Deprecated)

MLlib automated MLflow tracking is deprecated on clusters running **Databricks Runtime 10.1 ML** and above, and is **disabled by default** on clusters running **Databricks Runtime 10.2 ML** and above. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Enabling Legacy Tracking

To enable the deprecated MLlib automated MLflow tracking on Databricks Runtime 10.2 ML or above, set the following Spark configuration settings: ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

```
spark.databricks.mlflow.trackMLlib.enabled true
spark.databricks.mlflow.autologging.enabled false
```

- `spark.databricks.mlflow.trackMLlib.enabled true` — enables the legacy MLlib tracking mechanism
- `spark.databricks.mlflow.autologging.enabled false` — disables the modern [Databricks Autologging](/concepts/databricks-autologging.md) to prevent conflicts

## Modern Alternative

**MLflow PySpark ML autologging** is the recommended replacement. Call `mlflow.pyspark.ml.autolog()` to enable it. This modern approach is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md) and is the preferred method for new workflows. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Run Structure

When `CrossValidator` or `TrainValidationSplit` runs with automated tracking, results are logged as nested MLflow runs:

- **Main (parent) run**: Logs information for the tuning estimator (`CrossValidator` or `TrainValidationSplit`). If an active run exists, information is logged to that run; if not, MLflow creates a new run and ends it before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]
- **Child runs**: Each hyperparameter setting tested and its corresponding evaluation metric are logged to a child run under the main run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Best Practice for `fit()`

Wrap `fit()` inside a `with mlflow.start_run():` statement to ensure information is logged under its own MLflow main run. This makes it easier to log additional tags, parameters, or metrics. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

If `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), runs are logged to the same main run. To resolve name conflicts for parameters and tags, MLflow appends a UUID. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core experiment logging system
- [Databricks Autologging](/concepts/databricks-autologging.md) — The modern automated logging framework
- Spark Configuration — Cluster-level settings that control runtime behavior
- [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) — The recommended replacement for legacy tracking
- [CrossValidator](/concepts/crossvalidator.md) — MLlib model tuning using cross-validation
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) — MLlib model tuning using train-validation split

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
