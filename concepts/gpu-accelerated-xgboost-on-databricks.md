---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 798ec2ef874011aa348bed4f1f7010a804b4fc589977a34f3edeff9f3e0e073c
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-accelerated-xgboost-on-databricks
    - GXOD
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: GPU-Accelerated XGBoost on Databricks
description: Enabling GPU training for XGBoost models on Databricks clusters by setting use_gpu=True, with compute capability constraints.
tags:
  - gpu
  - xgboost
  - databricks
  - training
timestamp: "2026-06-18T12:05:17.826Z"
---

# GPU-Accelerated XGBoost on Databricks

**GPU-Accelerated XGBoost on Databricks** enables training and inference of [XGBoost](/concepts/xgboostspark-module.md) models using NVIDIA GPU clusters for significant performance improvements. Databricks Runtime ML includes GPU support through the `sparkdl.xgboost` module (deprecated as of Databricks Runtime 12.0 ML; Databricks recommends migrating to the `xgboost.spark` module) and via the underlying `xgboost` Python package. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## GPU Training with sparkdl.xgboost

To enable GPU training when using `sparkdl.xgboost.XgboostClassifier` or `sparkdl.xgboost.XgboostRegressor`, set the `use_gpu` parameter to `True`: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=N, use_gpu=True)
regressor = XgboostRegressor(num_workers=N, use_gpu=True)
```

GPU support is available in Databricks Runtime 9.1 LTS ML and above. Note that Databricks Runtime 11.3 LTS ML includes XGBoost 1.6.1, which does *not* support GPU clusters with compute capability 5.2 and below. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Distributed GPU Training

Distributed training across multiple nodes can be combined with GPU acceleration by setting `num_workers` concurrently with `use_gpu=True`. The `num_workers` parameter controls the number of Spark task slots used; to use all available slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=sc.defaultParallelism, use_gpu=True)
```

Distributed GPU training has the following limitations: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

- `mlflow.xgboost.autolog` is not supported with distributed XGBoost.
- `baseMarginCol` is not supported with distributed XGBoost.
- Distributed XGBoost cannot be used on a cluster with autoscaling enabled.

## Troubleshooting NCCL Communication Errors

During multi-node GPU training, you may encounter the error: `NCCL failure: remote process exited or there was a network error`. This typically indicates a network communication problem among GPUs because NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

To resolve this, set the cluster’s Spark configuration property `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers in a node, instructing NCCL to use the Ethernet interface. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Unsupported Parameters with sparkdl.xgboost

When using GPU training (or any mode) with `sparkdl.xgboost`, the following parameters from the `xgboost` package are not supported: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

- `gpu_id`, `output_margin`, `validate_features`
- `sample_weight`, `eval_set`, `sample_weight_eval_set` (use `weightCol` and `validationIndicatorCol` instead)
- `base_margin`, `base_margin_eval_set` (use `baseMarginCol` instead)
- `missing` has different semantics; in `sparkdl.xgboost`, zero values in a Spark sparse vector are only treated as missing when `missing=0`. Databricks recommends setting `missing=0` for sparse training datasets to reduce memory consumption and improve performance.

## Migration from sparkdl.xgboost

The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks strongly recommends migrating your code to the `xgboost.spark` module, which provides a more modern and maintained API. See the [migration guide](https://docs.databricks.com/aws/en/machine-learning/train-model/xgboost-spark#xgboost-migration) for details. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) — The gradient boosting framework used in these estimators
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The ML-optimized runtime that includes sparkdl.xgboost and GPU support
- [GPU clusters](/concepts/serverless-gpu-compute.md) — Databricks cluster types with NVIDIA GPUs
- NCCL — NVIDIA Collective Communications Library used for multi-GPU communication
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) — Training across multiple nodes with Spark task slots
- [xgboost.spark](/concepts/xgboostspark-module.md) — The recommended successor module for XGBoost on Spark

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
