---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5c4ce5f0d6b526d36a0ccd6d52652f8c15592d919fc266c1b066e35c1f93aaf
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-logging-limitations-for-distributed-xgboost
    - MLLFDX
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: MLflow Logging Limitations for Distributed XGBoost
description: Inability to use mlflow.xgboost.autolog with distributed XGBoost; alternative use of mlflow.spark.log_model for logging xgboost.spark models
tags:
  - mlflow
  - logging
  - xgboost
  - spark
timestamp: "2026-06-19T10:17:55.701Z"
---

# MLflow Logging Limitations for Distributed XGBoost

**MLflow Logging Limitations for Distributed XGBoost** refers to the restriction that the `mlflow.xgboost.autolog` function does not work when training XGBoost models using the distributed mode of the `xgboost.spark` module. Users must use an alternative logging method to record model artifacts and metrics.

## Overview

The `xgboost.spark` module (available in `xgboost>=1.7`) provides PySpark estimators—`SparkXGBRegressor`, `SparkXGBClassifier`, and `SparkXGBRanker`—that support distributed training via the `num_workers` parameter. While these estimators integrate with Spark ML Pipelines, they do not support the automatic logging functionality provided by `mlflow.xgboost.autolog`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Limitation

When using distributed XGBoost training (i.e., setting `num_workers` to a value greater than 1), the `mlflow.xgboost.autolog` function is incompatible and will not log model parameters, metrics, or artifacts automatically. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

An additional infrastructure limitation is that distributed XGBoost cannot be used on a cluster with autoscaling enabled. New worker nodes that start during autoscaling cannot receive new tasks and remain idle, which breaks the distributed training process. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Workaround

To log an XGBoost Spark model using [MLflow Tracking](/concepts/mlflow-tracking.md), use `mlflow.spark.log_model()` instead of relying on autologging. This function can log the trained Spark XGBoost model to MLflow as an artifact:

```python
mlflow.spark.log_model(spark_xgb_model, artifact_path)
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

This workaround allows you to store the model for later deployment and versioning, but you must manually log any hyperparameters or metrics you wish to track, as `mlflow.spark.log_model` only captures the model object itself.

## Related Concepts

- [MLflow Automatic Logging (autolog)](/concepts/mlflow-autologging.md) – The feature that is unsupported for distributed XGBoost.
- [XGBoost Spark](/concepts/xgboostspark-module.md) – The `xgboost.spark` module used for distributed training.
- [Distributed XGBoost Training](/concepts/distributed-xgboost-training-on-databricks.md) – Training with multiple workers via the `num_workers` parameter.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The broader MLflow component used for logging experiments.
- Databricks Autoscaling – A cluster configuration that is incompatible with distributed XGBoost.
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) – The pipeline framework into which XGBoost Spark estimators integrate.

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
