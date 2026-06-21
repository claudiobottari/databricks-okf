---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: feeb2bcff871083064afd287ca3587627325abd6609e2fa9e376789925445a80
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 0.98
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-xgboost-training-with-num_workers
    - DXTWN
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: Distributed XGBoost Training with num_workers
description: Distributed training capability in sparkdl.xgboost using the num_workers parameter, which can be set to use all Spark task slots via sc.defaultParallelism
tags:
  - distributed-training
  - xgboost
  - spark
timestamp: "2026-06-19T18:35:34.109Z"
---

# Distributed XGBoost Training with `num_workers`

**Distributed XGBoost Training with `num_workers`** enables parallel model training across multiple Spark tasks using the `xgboost.spark` module, which provides PySpark estimators that support distributed execution. This approach allows XGBoost models to scale training across cluster resources, processing large datasets more efficiently than single-node training.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Overview

The `xgboost.spark` module, available in `xgboost>=1.7`, includes three PySpark estimators — `SparkXGBRegressor`, `SparkXGBClassifier`, and `SparkXGBRanker` — that can be integrated into [SparkML Pipelines](/concepts/mllib-pipelines-api.md). These estimators support distributed training through the `num_workers` parameter, which controls the number of concurrent Spark tasks used during training.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Requirements

- **Databricks Runtime**: 12.0 ML and above.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- **Cluster autoscaling**: Must be disabled. New worker nodes that start in an elastic scaling paradigm cannot receive new sets of tasks and remain idle during distributed XGBoost training.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Using `num_workers`

To use distributed training, create an XGBoost classifier or regressor and set `num_workers` to the desired number of concurrent Spark tasks. To use all available Spark task slots, set `num_workers = sc.defaultParallelism`.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism)
```

### Behavior with `num_workers=1`

Setting `num_workers=1` executes model training using a single Spark task. This utilizes the number of CPU cores specified by the Spark cluster configuration setting `spark.task.cpus`, which is 1 by default. To use more CPU cores for single-task training, increase `num_workers` or `spark.task.cpus`. The `nthread` and `n_jobs` parameters cannot be set directly for estimators defined in `xgboost.spark` — this differs from the deprecated `sparkdl.xgboost` package.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## GPU Training with Distributed XGBoost

PySpark estimators in the `xgboost.spark` module support GPU training when the `use_gpu` parameter is set to `True`. For each Spark task used in distributed training, only one GPU is used. Databricks recommends using the default value of `1` for the Spark cluster configuration `spark.task.resource.gpu.amount` — otherwise, additional GPUs allocated to a task remain idle.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(
    num_workers=sc.defaultParallelism,
    use_gpu=True
)
```

## Best Practices

### Data Partitioning for Large Datasets

For extremely large datasets, increase the `num_workers` parameter so that each training task partitions the data into smaller, more manageable partitions. Setting `num_workers = sc.defaultParallelism` is a recommended approach as it distributes data across all available Spark task slots.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Memory Management

The `xgboost.spark` estimators use the DMatrix data iteration API for efficient memory usage. The deprecated `use_external_storage` and `external_storage_precision` parameters from `sparkdl.xgboost` have been removed — external storage mode is no longer necessary.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Sparse Data Optimization

To enable optimization for training on datasets with sparse features, provide a dataset with a features column of type `pyspark.ml.linalg.SparseVector` and set `enable_sparse_data_optim=True` along with `missing=0.0`:

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(
    enable_sparse_data_optim=True,
    missing=0.0
)
classifier.fit(dataset_with_sparse_features_col)
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Limitations

- **MLflow autologging**: You cannot use `mlflow.xgboost.autolog` with distributed XGBoost. To log an XGBoost Spark model using MLflow, use `mlflow.spark.log_model(spark_xgb_model, artifact_path)`.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- **Autoscaling clusters**: Distributed XGBoost training cannot run on clusters with autoscaling enabled.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Troubleshooting

### NCCL Network Communication Errors

During multi-node GPU training, a `NCCL failure: remote process exited or there was a network error` message typically indicates a problem with network communication among GPUs. This occurs when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication. To resolve, set the cluster's SparkConf for `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`, which sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers in a node.^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md, distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- XGBoost on Databricks — Overview of training XGBoost models
- [SparkML Pipelines](/concepts/mllib-pipelines-api.md) — ML pipelines that can include XGBoost estimators
- GPU Training on Databricks — GPU-accelerated model training
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking for machine learning workflows
- Spark Clusters — Compute resources for distributed training
- [Migration from sparkdl.xgboost](/concepts/migration-from-sparkdlxgboost-to-xgboostspark.md) — Transitioning from the deprecated XGBoost package

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
2. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
