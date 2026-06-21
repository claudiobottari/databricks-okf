---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c2702bf07029089cd8f269de9b8aa01c22d5ddbb91a57b2cfc3260dd00e95a1
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparkdlxgboost-pyspark-estimators
    - SPE
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: sparkdl.xgboost PySpark Estimators
description: PySpark ML pipeline estimators (XgboostRegressor and XgboostClassifier) from the sparkdl.xgboost module for distributed XGBoost training on Databricks
tags:
  - machine-learning
  - xgboost
  - databricks
  - spark
timestamp: "2026-06-19T18:35:20.069Z"
---

# sparkdl.xgboost PySpark Estimators

The **sparkdl.xgboost PySpark Estimators** are PySpark estimators based on the Python `xgboost` package, provided by the `sparkdl.xgboost` module in Databricks Runtime ML. These estimators allow you to create ML pipelines for distributed XGBoost training using Spark's MLlib framework. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Available Estimators

The `sparkdl.xgboost` module provides two primary estimators:

- **`XgboostRegressor`** — For regression tasks
- **`XgboostClassifier`** — For classification tasks

Both estimators integrate with Spark MLlib's pipeline API, allowing them to be used as stages in a [Spark ML Pipeline](/concepts/mllib-pipelines-api.md). ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Deprecation Notice

The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks recommends migrating code to use the `xgboost.spark` module instead. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Version Requirements

Databricks strongly recommends using Databricks Runtime 11.3 LTS ML or above for `sparkdl.xgboost` users. Previous Databricks Runtime versions are affected by bugs in older versions of `sparkdl.xgboost`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Unsupported Parameters

The following parameters from the standard `xgboost` package are **not supported** by `sparkdl.xgboost`:

- `gpu_id`
- `output_margin`
- `validate_features`

The parameters `sample_weight`, `eval_set`, and `sample_weight_eval_set` are not supported. Instead, use the parameters `weightCol` and `validationIndicatorCol`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

The parameters `base_margin` and `base_margin_eval_set` are not supported. Use the parameter `baseMarginCol` instead. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Missing Value Semantics

The `missing` parameter has different semantics from the standard `xgboost` package. In the standard `xgboost` package, zero values in a SciPy sparse matrix are treated as missing values regardless of the value of `missing`. For the PySpark estimators in the `sparkdl` package, zero values in a Spark sparse vector are **not** treated as missing values unless you set `missing=0`. If you have a sparse training dataset where most feature values are missing, Databricks recommends setting `missing=0` to reduce memory consumption and achieve better performance. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Distributed Training

Databricks Runtime ML supports distributed XGBoost training using the `num_workers` parameter. To use distributed training, create a classifier or regressor and set `num_workers` to a value less than or equal to the total number of Spark task slots on your cluster. To use all Spark task slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=sc.defaultParallelism)
regressor = XgboostRegressor(num_workers=sc.defaultParallelism)
```

### Limitations of Distributed Training

- You cannot use `mlflow.xgboost.autolog` with distributed XGBoost.
- You cannot use `baseMarginCol` with distributed XGBoost.
- You cannot use distributed XGBoost on a cluster with autoscaling enabled. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## GPU Training

Databricks Runtime 9.1 LTS ML and above support GPU clusters for XGBoost training. To use a GPU cluster, set `use_gpu` to `True`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=N, use_gpu=True)
regressor = XgboostRegressor(num_workers=N, use_gpu=True)
```

**Note:** Databricks Runtime 11.3 LTS ML includes XGBoost 1.6.1, which does not support GPU clusters with compute capability 5.2 and below. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Troubleshooting

During multi-node training, if you encounter a `NCCL failure: remote process exited or there was a network error` message, it typically indicates a problem with network communication among GPUs. This issue arises when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

To resolve, set the cluster's `sparkConf` for `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This essentially sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all of the workers in a node. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [XGBoost Spark Module](/concepts/xgboostspark-module.md) — The recommended replacement for `sparkdl.xgboost`
- [Spark ML Pipeline](/concepts/mllib-pipelines-api.md) — The pipeline framework these estimators integrate with
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Training machine learning models across multiple workers
- NCCL — NVIDIA Collective Communications Library for GPU communication
- [MLflow Autologging](/concepts/mlflow-autologging.md) — Automatic logging of ML experiments (not supported with distributed XGBoost)

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
