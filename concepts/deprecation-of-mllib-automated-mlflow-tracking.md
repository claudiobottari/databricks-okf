---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af6dfd03b09d79abe460ad447f5a71193aaf3945dc3e17fbd85be61173373b50
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deprecation-of-mllib-automated-mlflow-tracking
    - DOMAMT
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Deprecation of MLlib Automated MLflow Tracking
description: MLlib automated MLflow tracking is deprecated on Databricks Runtime 10.1 ML and above, disabled by default on 10.2 ML+, with a configuration escape hatch to re-enable the old behavior
tags:
  - deprecation
  - databricks
  - machine-learning
  - mlflow
timestamp: "2026-06-19T09:00:48.306Z"
---

# Deprecation of MLlib Automated MLflow Tracking

**MLlib automated MLflow tracking** is a legacy feature that automatically logged hyperparameters and evaluation metrics from [Apache Spark MLlib](/concepts/apache-spark-mllib.md) model tuning (using `CrossValidator` or `TrainValidationSplit`) into MLflow runs. This feature has been deprecated and is no longer supported in recent Databricks Runtime versions. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Deprecation timeline

MLlib automated MLflow tracking is deprecated on clusters running **Databricks Runtime 10.1 ML and above**, and is disabled by default on clusters running **Databricks Runtime 10.2 ML and above**. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Recommended replacement

Instead of the deprecated MLlib automated tracking, use [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) by calling `mlflow.pyspark.ml.autolog()`, which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md). This provides a more current and supported approach for automatic MLflow tracking with PySpark ML. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Re-enabling the old feature (not recommended)

To use the old MLlib automated MLflow tracking in Databricks Runtime 10.2 ML or above, you can enable it by setting the following Spark configurations:

- `spark.databricks.mlflow.trackMLlib.enabled true`
- `spark.databricks.mlflow.autologging.enabled false`

This is not recommended for new projects; the configuration is provided only for backward compatibility during migration. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## How automated tracking previously worked

With MLlib automated MLflow tracking, when tuning code using `CrossValidator` or `TrainValidationSplit` was executed, hyperparameters and evaluation metrics were automatically logged to MLflow without requiring explicit API calls. The tracking logged results as nested MLflow runs: ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

- **Main (parent) run**: Information for `CrossValidator` or `TrainValidationSplit` was logged to the main run. If an active run already existed, information was logged to it; if not, MLflow created a new run.
- **Child runs**: Each hyperparameter setting tested and its corresponding evaluation metric were logged as a child run under the main run.

When `fit()` was called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), those multiple runs were logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appended a UUID to names with conflicts. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related concepts

- [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md)
- [Databricks Autologging](/concepts/databricks-autologging.md)
- [CrossValidator](/concepts/crossvalidator.md)
- [TrainValidationSplit](/concepts/trainvalidationsplit.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
