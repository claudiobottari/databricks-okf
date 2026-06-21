---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4ff726cba4a26258f1615e3fb567c977bef5b90dc9c7bb45a06188729a7bd90
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-training-for-xgboost-on-spark
    - GTFXOS
    - GPU Training for XGBoost
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: GPU Training for XGBoost on Spark
description: GPU-accelerated XGBoost training on Databricks clusters via the use_gpu parameter, supported from Databricks Runtime 9.1 LTS ML and above.
tags:
  - machine-learning
  - gpu
  - xgboost
  - spark
timestamp: "2026-06-19T10:18:24.571Z"
---

---
title: GPU Training for XGBoost on Spark
summary: GPU-accelerated training for xgboost.spark estimators via the use_gpu parameter, with NCCL networking considerations
sources:
  - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:32:51.101Z"
updatedAt: "2026-06-18T15:32:51.101Z"
tags:
  - gpu
  - xgboost
  - spark
  - performance
aliases:
  - gpu-training-for-xgboost-on-spark
  - GTFXOS
confidence: 0.97
provenanceState: extracted
inferredParagraphs: 1
---

# GPU Training for XGBoost on Spark

**GPU Training for XGBoost on Spark** refers to the capability of training XGBoost models using GPU acceleration within a Spark distributed computing environment, enabled by the `xgboost.spark` module available in XGBoost version 1.7 and above.

## Overview

The `xgboost.spark` module provides PySpark estimators — `SparkXGBRegressor`, `SparkXGBClassifier`, and `SparkXGBRanker` — that support GPU training. These estimators can be included in SparkML Pipelines and support most standard XGBoost parameters, with some exceptions such as `gpu_id`, `nthread`, `sample_weight`, and `eval_set`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Requirements

GPU training with `xgboost.spark` requires Databricks Runtime 12.0 ML and above. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Enabling GPU Training

To enable GPU training, set the `use_gpu` parameter to `True` when creating the estimator: ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(
    num_workers=sc.defaultParallelism,
    use_gpu=True
)
```

## GPU Resource Allocation

When `use_gpu` is set to `True`, each Spark task used in XGBoost distributed training utilizes only one GPU. Databricks recommends using the default value of `1` for the Spark cluster configuration `spark.task.resource.gpu.amount`. Setting this value higher would result in additional GPUs allocated to a Spark task remaining idle. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Distributed Training with GPUs

GPU training can be combined with distributed training by setting the `num_workers` parameter. To use all available Spark task slots, set `num_workers=sc.defaultParallelism`. This configuration distributes the training workload across multiple workers, each utilizing its allocated GPU. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Limitations

- **Autoscaling not supported**: Distributed XGBoost cannot be used on clusters with autoscaling enabled, as new worker nodes that start during elastic scaling cannot receive new tasks and remain idle. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- **MLflow autologging**: `mlflow.xgboost.autolog` is not compatible with distributed XGBoost. To log an XGBoost Spark model using MLflow, use `mlflow.spark.log_model(spark_xgb_model, artifact_path)`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Troubleshooting NCCL Errors

During multi-node GPU training, you may encounter a `NCCL failure: remote process exited or there was a network error` message. This typically indicates a problem with network communication among GPUs, occurring when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

To resolve this issue, set the cluster's Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers in a node. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- [Distributed Training of XGBoost Models](/concepts/distributed-training-with-xgboostspark.md) — General distributed training with `xgboost.spark`
- GPU Scheduling — Optimizing GPU utilization in Spark clusters
- [SparkML Pipelines](/concepts/mllib-pipelines-api.md) — Integrating XGBoost estimators into ML workflows
- NCCL Configuration — Network communication for multi-GPU training
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — ML-optimized runtime with GPU support

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
