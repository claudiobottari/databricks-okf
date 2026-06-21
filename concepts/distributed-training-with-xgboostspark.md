---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 414f72daff0539faeacb42e8a8aa9eb1fac0c4a961f56589e150bb8ea0d57051
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-with-xgboostspark
    - DTWX
    - Distributed training with XGBoost
    - Distributed Training of XGBoost Models
    - Distributed XGBoost
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: Distributed Training with xgboost.spark
description: Distributed XGBoost training on Spark using the num_workers parameter, with restrictions on autoscaling and MLflow autologging
tags:
  - machine-learning
  - xgboost
  - distributed-training
  - spark
timestamp: "2026-06-18T15:32:58.601Z"
---

# Distributed Training with xgboost.spark

**Distributed Training with xgboost.spark** refers to the capability of training XGBoost models across multiple Spark tasks in parallel using the `xgboost.spark` module. This module provides PySpark estimators that integrate with [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) and support distributed computation for scalable model training on large datasets. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Overview

The `xgboost.spark` module, available in Python package `xgboost>=1.7`, includes three main PySpark estimator classes: `SparkXGBRegressor`, `SparkXGBClassifier`, and `SparkXGBRanker`. These classes allow XGBoost models to be trained in a distributed manner across a Spark cluster, leveraging Spark's task scheduling for parallel computation. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

Distributed training with `xgboost.spark` is supported on Databricks Runtime 12.0 ML and above. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Using the `num_workers` Parameter

The core mechanism for distributed training is the `num_workers` parameter, which controls the number of concurrent running Spark tasks during training. To use distributed training, create an estimator and set `num_workers` to the desired number of tasks. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism)
```

To utilize all available Spark task slots in the cluster, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Requirements and Limitations

### Cluster Configuration

Distributed XGBoost cannot be used on a cluster with autoscaling enabled. When autoscaling adds new worker nodes during training, those nodes cannot receive new tasks and remain idle, disrupting the distributed training process. Disable autoscaling on the cluster before using distributed XGBoost. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### MLflow Integration

The `mlflow.xgboost.autolog` function is not compatible with distributed XGBoost training. To log a Spark XGBoost model using MLflow, use `mlflow.spark.log_model(spark_xgb_model, artifact_path)` instead. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Parameters and Arguments

The estimators in `xgboost.spark` support most parameters from the standard XGBoost library, with naming, values, and defaults largely identical to those described in the [XGBoost parameters documentation](https://xgboost.readthedocs.io/en/stable/parameter.html). ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

Key differences from `xgboost.sklearn` include:

- **Unsupported parameters**: `gpu_id`, `nthread`, `sample_weight`, `eval_set` are not available. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- **Added PySpark-specific parameters**: `featuresCol`, `labelCol`, `use_gpu`, `validationIndicatorCol` have been added for Spark integration. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Sparse Data Optimization

For datasets with sparse features, `xgboost.spark` provides an optimization mode. To enable it, provide a dataset where the features column contains values of type `pyspark.ml.linalg.SparseVector`, set the estimator parameter `enable_sparse_data_optim` to `True`, and set the `missing` parameter to `0.0`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(enable_sparse_data_optim=True, missing=0.0)
classifier.fit(dataset_with_sparse_features_col)
```

## GPU Training

Distributed training with `xgboost.spark` supports GPU acceleration. Set the `use_gpu` parameter to `True` to enable GPU training. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism, use_gpu=True)
```

### GPU Configuration Notes

When `use_gpu` is set to `True`, each Spark task in the distributed training uses exactly one GPU. Databricks recommends using the default value of `1` for the Spark cluster configuration `spark.task.resource.gpu.amount`. If this value is higher, the additional GPUs allocated to a Spark task remain idle. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Troubleshooting NCCL Errors

During multi-node GPU training, an error message such as `NCCL failure: remote process exited or there was a network error` may occur. This typically indicates a network communication problem between GPUs, arising when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

To resolve this issue, set the cluster's `sparkConf` for `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers in a node. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Migration from `sparkdl.xgboost`

The deprecated `sparkdl.xgboost` module has been replaced by `xgboost.spark`. Key migration steps include: ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

- Replace import statements: `from sparkdl.xgboost import XgboostRegressor` becomes `from xgboost.spark import SparkXGBRegressor`, and similarly for classifiers.
- Change parameter names from camelCase to snake_case (e.g., `featuresCol` becomes `features_col`).
- The parameters `use_external_storage` and `external_storage_precision` have been removed. The `xgboost.spark` estimators use the DMatrix data iteration API for more efficient memory usage.
- For extremely large datasets, increase `num_workers` to partition data into smaller, more manageable partitions. Setting `num_workers = sc.defaultParallelism` is recommended.
- When `num_workers=1`, training uses a single Spark task with the number of CPU cores specified by `spark.task.cpus` (default is 1). To use more cores, increase `num_workers` or `spark.task.cpus`. The `nthread` or `n_jobs` parameters cannot be set for `xgboost.spark` estimators.

A utility function is available to convert `sparkdl.xgboost` models into `xgboost.spark` models, including within pyspark.ml.PipelineModel pipelines. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) — The underlying gradient boosting framework
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) — Integration point for PySpark estimators
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Alternative distributed training approach
- GPU Scheduling — Configuring GPU resources for distributed training
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Logging models trained with distributed XGBoost
- Spark Configuration — Cluster settings for distributed training tasks

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
