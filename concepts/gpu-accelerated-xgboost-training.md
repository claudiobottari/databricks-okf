---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c2fe9346c68f69704a1dc22e67dc9be89e7982f8a649aec6576cff5218406eb
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
    - train-xgboost-model-on-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - gpu-accelerated-xgboost-training
    - GXT
    - GPU-Accelerated Training
    - GPU-accelerated training
    - GPU Accelerators
    - GPU acceleration
    - GPU acceleration for XGBoost
    - GPU-accelerated
    - GPU-accelerated machine learning
    - XGBoost GPU Training
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
    - file: train-xgboost-model-on-a-single-gpu-databricks-on-aws.md
title: GPU-Accelerated XGBoost Training
description: Using GPU clusters for XGBoost training on Databricks by setting use_gpu=True in sparkdl.xgboost estimators.
tags:
  - gpu
  - xgboost
  - databricks
  - machine-learning
timestamp: "2026-06-18T15:32:29.105Z"
---

# GPU-Accelerated XGBoost Training

**GPU-Accelerated XGBoost Training** refers to using NVIDIA GPUs to accelerate the training of [XGBoost](/concepts/xgboostspark-module.md) models, significantly reducing training time for large datasets and complex models. Databricks supports GPU-accelerated XGBoost training through both single-GPU and distributed multi-GPU configurations.

## Overview

XGBoost can leverage GPU hardware to accelerate the histogram-building and tree-construction phases of gradient boosting. By setting the appropriate parameters, training can be offloaded to GPUs, resulting in substantial speed improvements over CPU-only training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md, train-xgboost-model-on-a-single-gpu-databricks-on-aws.md]

## Single-GPU Training

To train an XGBoost model on a single GPU, set the `tree_method` parameter to `"hist"` and the `device` parameter to `"cuda"`. The `"hist"` tree method uses the GPU-accelerated histogram algorithm for faster training. ^[train-xgboost-model-on-a-single-gpu-databricks-on-aws.md]

### Example: Single-GPU Training

The following example trains a regression model on the California Housing dataset using a single GPU: ^[train-xgboost-model-on-a-single-gpu-databricks-on-aws.md]

```python
import xgboost as xgb
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error

# Load and prepare data
X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert to DMatrix
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# GPU training parameters for regression
params = {
    "tree_method": "hist",       # Use GPU histogram
    "device": "cuda",
    "objective": "reg:squarederror",
    "eval_metric": "rmse",
    "max_depth": 6,
    "learning_rate": 0.1,
}

# Train the model
bst = xgb.train(
    params=params,
    dtrain=dtrain,
    num_boost_round=200,
    evals=[(dtest, "eval"), (dtrain, "train")],
    verbose_eval=10,
)

# Evaluate
y_pred = bst.predict(dtest)
rmse = root_mean_squared_error(y_test, y_pred)
print(f"RMSE on test set: {rmse:.4f}")
```

## Distributed Multi-GPU Training

Databricks Runtime ML supports distributed XGBoost training using the `sparkdl.xgboost` module (deprecated since Databricks Runtime 12.0 ML) or the newer `xgboost.spark` module. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### Using sparkdl.xgboost with GPU

To enable GPU training with distributed XGBoost in `sparkdl.xgboost`, set `use_gpu` to `True` and specify the number of workers: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=N, use_gpu=True)
regressor = XgboostRegressor(num_workers=N, use_gpu=True)
```

Set `num_workers` to a value less than or equal to the total number of Spark task slots on your cluster. To use all Spark task slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Requirements and Limitations

### GPU Compatibility

- Databricks Runtime 9.1 LTS ML and above support GPU clusters for XGBoost training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- Databricks Runtime 11.3 LTS ML includes XGBoost 1.6.1, which does not support GPU clusters with compute capability 5.2 and below. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### Distributed Training Limitations

- You cannot use `mlflow.xgboost.autolog` with distributed XGBoost. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- You cannot use `baseMarginCol` with distributed XGBoost. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- Distributed XGBoost does not work on clusters with autoscaling enabled. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### Unsupported Parameters

When using `sparkdl.xgboost`, the following parameters are not supported: `gpu_id`, `output_margin`, `validate_features`, `sample_weight`, `eval_set`, `sample_weight_eval_set`, `base_margin`, and `base_margin_eval_set`. Use alternatives such as `weightCol`, `validationIndicatorCol`, and `baseMarginCol` instead. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Troubleshooting

If you encounter a `NCCL failure: remote process exited or there was a network error` message during multi-node GPU training, it typically indicates a problem with network communication among GPUs. This issue arises when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

To resolve, set the cluster's SparkConf for `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers in a node. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Migration Note

The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks recommends migrating code to use the `xgboost.spark` module instead. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) — The underlying gradient boosting framework
- GPU Scheduling — Optimizing GPU utilization for training
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — High-performance GPU options
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built runtime with GPU support
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General approaches for multi-node training

## Sources

- train-xgboost-model-on-a-single-gpu-databricks-on-aws.md
- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
2. [train-xgboost-model-on-a-single-gpu-databricks-on-aws.md](/references/train-xgboost-model-on-a-single-gpu-databricks-on-aws-20dbc876.md)
