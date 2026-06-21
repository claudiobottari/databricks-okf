---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a842180bcf043e4a360954064bb3d2d8123faef4f2f5e5bbfaaeffceaf436a86
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparkdlxgboost-module
    - sparkdl.xgboost
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: sparkdl.xgboost Module
description: A deprecated PySpark module providing XgboostRegressor and XgboostClassifier estimators for distributed XGBoost training within Spark ML pipelines, superseded by xgboost.spark in Databricks Runtime 12.0 ML.
tags:
  - machine-learning
  - databricks
  - xgboost
  - spark
timestamp: "2026-06-19T10:17:16.112Z"
---

# sparkdl.xgboost Module

The `sparkdl.xgboost` module provides PySpark estimators that wrap the Python `xgboost` package, enabling XGBoost training within a Spark ML pipeline. The module includes two main estimators: `XgboostRegressor` for regression tasks and `XgboostClassifier` for classification tasks. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Deprecation and Migration

`sparkdl.xgboost` was deprecated starting in Databricks Runtime 12.0 ML. Databricks recommends migrating existing code to the `xgboost.spark` module, which provides a more modern and actively maintained integration. See the xgboost.spark migration guide for details. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

Databricks strongly recommends using Databricks Runtime 11.3 LTS ML or above when working with `sparkdl.xgboost`, as earlier versions contain bugs in older releases of the module. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Key Features

### Distributed Training

The module supports distributed [XGBoost](/concepts/xgboostspark-module.md) training across multiple Spark task slots by setting the `num_workers` parameter. This parameter must be less than or equal to the total number of Spark task slots on the cluster. To use all available slots, set `num_workers = sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=sc.defaultParallelism)
regressor = XgboostRegressor(num_workers=sc.defaultParallelism)
```

### GPU Training

On Databricks Runtime 9.1 LTS ML and above, the module can leverage GPU clusters for accelerated training. To enable GPU support, set `use_gpu=True` when creating the estimator. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=N, use_gpu=True)
regressor = XgboostRegressor(num_workers=N, use_gpu=True)
```

Note that Databricks Runtime 11.3 LTS ML includes XGBoost 1.6.1, which does **not** support GPU clusters with NVIDIA compute capability 5.2 or below. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Unsupported Parameters

The `sparkdl.xgboost` estimators do not support several parameters that exist in the native `xgboost` package: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

| Unsupported Parameter | Replacement |
|-----------------------|-------------|
| `gpu_id`, `output_margin`, `validate_features` | Not available |
| `sample_weight`, `eval_set`, `sample_weight_eval_set` | Use `weightCol` and `validationIndicatorCol` |
| `base_margin`, `base_margin_eval_set` | Use `baseMarginCol` |
| `missing` | See note below |

### Handling of Missing Values with Sparse Data

The `missing` parameter has different semantics compared to the standard `xgboost` package. In `xgboost`, zero values in a SciPy sparse matrix are treated as missing regardless of the `missing` parameter. In `sparkdl.xgboost`, zero values in a Spark sparse vector are **not** treated as missing unless you explicitly set `missing=0`. For sparse training datasets where most feature values are missing, Databricks recommends setting `missing=0` to reduce memory consumption and achieve better performance. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Limitations

- **MLflow autologging**: `mlflow.xgboost.autolog` cannot be used with distributed XGBoost training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- **baseMarginCol**: The `baseMarginCol` parameter is not supported when using distributed training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- **Autoscaling**: Distributed XGBoost training cannot be used on a cluster with autoscaling enabled. Autoscaling must be disabled for multi-worker training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Troubleshooting: NCCL Network Errors

During multi-node GPU training, you may encounter the error: `NCCL failure: remote process exited or there was a network error`. This typically indicates a problem with network communication among GPUs when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

**Solution**: Set the cluster Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers on a node, ensuring NCCL uses the correct network interface. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [XGBoost for PySpark Pipeline](/concepts/xgboostspark-module.md) — Official documentation of `sparkdl.xgboost`
- [xgboost.spark Module](/concepts/xgboostspark-module.md) — The recommended replacement for `sparkdl.xgboost`
- [Distributed ML Training](/concepts/workload-yaml-for-distributed-training.md) — General concepts of distributed model training
- GPU Computing on Databricks — GPU cluster setup and best practices
- [PySpark ML Pipelines](/concepts/mllib-pipelines-api.md) — Building ML workflows with Spark

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
