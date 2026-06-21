---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2201f4ac8467ab907da75032589189c03c83b635fbf948efb3b8020b629f17dc
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-training-for-xgboost-on-databricks
    - GTFXOD
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: GPU Training for XGBoost on Databricks
description: Support for GPU-accelerated XGBoost training on Databricks clusters using the use_gpu parameter, with compute capability requirements for different runtime versions
tags:
  - gpu
  - xgboost
  - databricks
timestamp: "2026-06-19T18:35:32.701Z"
---

# GPU Training for XGBoost on Databricks

**GPU Training for XGBoost on Databricks** refers to the ability to accelerate gradient-boosted tree model training by using GPU-enabled clusters with the `sparkdl.xgboost` package. Databricks Runtime ML includes PySpark estimators (`XgboostRegressor`, `XgboostClassifier`) that natively support GPU acceleration. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Enabling GPU Training

To use GPU clusters for XGBoost training, set the `use_gpu` parameter to `True` when creating a classifier or regressor. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=N, use_gpu=True)
regressor = XgboostRegressor(num_workers=N, use_gpu=True)
```

The `use_gpu` parameter is available in Databricks Runtime 9.1 LTS ML and above. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## GPU Compute Capability Requirement

Databricks Runtime 11.3 LTS ML includes XGBoost 1.6.1, which does **not** support GPU clusters with [compute capability](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#compute-capability) 5.2 and below. Older GPU hardware may require using a different Databricks Runtime version or checking XGBoost compatibility. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Distributed GPU Training

GPU training can be combined with distributed training across multiple workers. The `num_workers` parameter controls the number of Spark task slots used. Set it to a value less than or equal to the total number of Spark task slots on your cluster. To use all available slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

When using multiple nodes with GPU training, NCCL (NVIDIA Collective Communications Library) may fail if it cannot use certain network interfaces. If you encounter a `NCCL failure: remote process exited or there was a network error` message, set the cluster Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers in a node, resolving the network communication issue. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Limitations

The following limitations apply when using GPU training (and distributed training in general) with `sparkdl.xgboost`:

- `mlflow.xgboost.autolog` cannot be used with distributed XGBoost. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- `baseMarginCol` is not supported with distributed XGBoost. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- Distributed XGBoost (including GPU) requires a cluster without autoscaling enabled. Autoscaling must be disabled. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- The `use_gpu` parameter is only available in Databricks Runtime 9.1 LTS ML and above; earlier versions do not support GPU training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Deprecation Note

The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks recommends migrating to the `xgboost.spark` module. A migration guide is available. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) – The underlying gradient-boosting framework.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – Using multiple workers to scale model training.
- [sparkdl.xgboost](/concepts/sparkdlxgboost-module.md) – The PySpark package for XGBoost estimators.
- [xgboost.spark](/concepts/xgboostspark-module.md) – The replacement module for newer Databricks Runtime versions.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The machine learning-optimized runtime.
- NCCL – NVIDIA Collective Communications Library used for GPU communication.
- GPU clusters on Databricks – Overview of GPU-enabled compute resources.
- Autoscaling considerations – Limitations when using autoscaling with distributed training.

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
