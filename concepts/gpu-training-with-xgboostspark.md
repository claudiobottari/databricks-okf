---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c10207b9aefaf9f322227ac820eed4d0aa7d7506b8818371fc78e197a9c3d046
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-training-with-xgboostspark
    - GTWX
    - GPU Training with XGBoost
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: GPU Training with xgboost.spark
description: Enabling GPU-accelerated training by setting use_gpu=True, with recommendation to keep spark.task.resource.gpu.amount=1 to avoid idle GPUs.
tags:
  - gpu
  - spark
  - xgboost
timestamp: "2026-06-19T18:35:50.868Z"
---

# GPU Training with xgboost.spark

The `xgboost.spark` module, available in `xgboost>=1.7`, provides PySpark estimators (`SparkXGBRegressor`, `SparkXGBClassifier`, `SparkXGBRanker`) that support GPU-accelerated distributed training through the `use_gpu` parameter. These estimators can be integrated into [SparkML Pipelines](/concepts/mllib-pipelines-api.md) for scalable machine learning workflows on Databricks.

## Requirements

GPU training with `xgboost.spark` requires Databricks Runtime 12.0 ML and above. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Enabling GPU Training

To enable GPU support, set the `use_gpu` parameter to `True` when creating the estimator. This applies to all three estimator classes (`SparkXGBClassifier`, `SparkXGBRegressor`, and `SparkXGBRanker`). ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Example

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(
    num_workers=sc.defaultParallelism,
    use_gpu=True
)
```

## GPU Resource Allocation

When training with `use_gpu=True`, each Spark task uses only one GPU. Databricks recommends keeping the default value of `1` for the Spark configuration `spark.task.resource.gpu.amount`. Setting this to a higher value results in idle GPUs for each task. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Distributed GPU Training

GPU training can be combined with distributed training by setting the `num_workers` parameter. To use all available Spark task slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Limitations

- Distributed GPU training is not supported on clusters with autoscaling enabled. New worker nodes in an auto-scaling cluster become idle as they cannot receive new task sets. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- [MLflow Autologging](/concepts/mlflow-autologging.md) (`mlflow.xgboost.autolog`) is not supported with distributed XGBoost. Use `mlflow.spark.log_model()` instead. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Troubleshooting GPU Communication Errors

During multi-node GPU training, you may encounter an error like:

```
NCCL failure: remote process exited or there was a network error
```

This occurs when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication. To resolve, set the Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth` in the cluster configuration. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers in a node. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- SparkXGBClassifier — The PySpark classifier for XGBoost
- SparkXGBRegressor — The PySpark regressor for XGBoost
- SparkXGBRanker — The PySpark ranker for XGBoost
- [Distributed XGBoost Training](/concepts/distributed-xgboost-training-on-databricks.md) — General distributed training with `xgboost.spark`
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) — Pipeline integration for XGBoost estimators
- XGBoost Parameters — Standard XGBoost parameter reference

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
