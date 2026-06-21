---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b874b225e49181ccae4f3a56239860289e77264f7b74b92bf3ce97b5f89b8da
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
    - use-xgboost-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-xgboost-training-on-databricks
    - DXTOD
    - Distributed XGBoost Training
  citations:
    - file: use-xgboost-on-databricks-databricks-on-aws.md
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: Distributed XGBoost Training on Databricks
description: Running XGBoost model training at scale across a Spark cluster using Scala on the Databricks platform
tags:
  - distributed-training
  - xgboost
  - databricks
  - scala
timestamp: "2026-06-19T18:35:07.215Z"
---

# Distributed XGBoost Training on Databricks

**Distributed XGBoost Training on Databricks** enables you to train XGBoost models across multiple workers in a cluster, leveraging Spark’s parallel computing capabilities to process large datasets efficiently. Databricks Runtime ML includes PySpark estimators based on the Python `xgboost` package, `sparkdl.xgboost.XgboostRegressor` and `sparkdl.xgboost.XgboostClassifier`, as well as a pre-installed XGBoost library for both Python and Scala. ^[use-xgboost-on-databricks-databricks-on-aws.md] ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

**Note:** The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks recommends migrating your code to use the `xgboost.spark` module instead. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md] For Databricks Runtime 12.0 ML and above, use the [xgboost.spark](/concepts/xgboostspark-module.md) library for distributed training. ^[use-xgboost-on-databricks-databricks-on-aws.md]

## Available Estimators

Databricks Runtime ML includes two primary PySpark estimators from the `sparkdl.xgboost` package: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

- `sparkdl.xgboost.XgboostRegressor` — For regression tasks
- `sparkdl.xgboost.XgboostClassifier` — For classification tasks

You can create an ML pipeline based on these estimators. Databricks strongly recommends using Databricks Runtime 11.3 LTS ML or above, as earlier versions are affected by bugs in older versions of `sparkdl.xgboost`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Enabling Distributed Training

To enable distributed training, set the `num_workers` parameter when creating a classifier or regressor. The value must be less than or equal to the total number of Spark task slots on your cluster. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
from sparkdl.xgboost import XgboostClassifier, XgboostRegressor

# Use all available Spark task slots
classifier = XgboostClassifier(num_workers=sc.defaultParallelism)
regressor = XgboostRegressor(num_workers=sc.defaultParallelism)
```

## GPU Training

Databricks Runtime 9.1 LTS ML and above support GPU clusters for XGBoost training. To use a GPU cluster, set `use_gpu` to `True`: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=N, use_gpu=True)
regressor = XgboostRegressor(num_workers=N, use_gpu=True)
```

**Note:** Databricks Runtime 11.3 LTS ML includes XGBoost 1.6.1, which does not support GPU clusters with compute capability 5.2 and below. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Limitations

### Distributed Training Limitations

- You cannot use `mlflow.xgboost.autolog` with distributed XGBoost training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- You cannot use `baseMarginCol` with distributed XGBoost. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- You cannot use distributed XGBoost on a cluster with autoscaling enabled. You must disable autoscaling to use distributed training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### Unsupported Parameters

The following parameters from the `xgboost` package are not supported in `sparkdl.xgboost`: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

- `gpu_id`
- `output_margin`
- `validate_features`
- `sample_weight`, `eval_set`, `sample_weight_eval_set` — use `weightCol` and `validationIndicatorCol` instead
- `base_margin`, `base_margin_eval_set` — use `baseMarginCol` instead

### Sparse Matrix Handling

The `missing` parameter has different semantics in `sparkdl.xgboost` compared to the standard `xgboost` package. In the standard package, zero values in a SciPy sparse matrix are treated as missing values regardless of the value of `missing`. In `sparkdl.xgboost`, zero values in a Spark sparse vector are not treated as missing values unless you set `missing=0`. For sparse training datasets where most feature values are missing, Databricks recommends setting `missing=0` to reduce memory consumption and achieve better performance. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Troubleshooting

### GPU Communication Errors

During multi-node training, you may encounter the error: `NCCL failure: remote process exited or there was a network error`. This typically indicates a problem with network communication among GPUs, occurring when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

To resolve this issue, set the cluster’s Spark configuration for `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers in a node: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```
spark.executorEnv.NCCL_SOCKET_IFNAME eth
```

## Installing XGBoost on Databricks

XGBoost is included in Databricks Runtime ML. You can use these libraries in Databricks Runtime ML without installing any packages. ^[use-xgboost-on-databricks-databricks-on-aws.md] To install a different version on Databricks Runtime ML, install XGBoost as a Databricks PyPI library: ^[use-xgboost-on-databricks-databricks-on-aws.md]

```
xgboost==<xgboost version>
```

On Databricks Runtime (non-ML), you can install the Python package using `%pip install xgboost==<xgboost version>`. For Scala/Java packages, install the Spark Package `xgboost-linux64` as a Databricks library. ^[use-xgboost-on-databricks-databricks-on-aws.md]

For the version of XGBoost installed in the Databricks Runtime ML version you are using, see the release notes. ^[use-xgboost-on-databricks-databricks-on-aws.md]

## Related Concepts

- XGBoost on Databricks — Overview of using XGBoost with Databricks
- [xgboost.spark](/concepts/xgboostspark-module.md) — The recommended replacement for `sparkdl.xgboost`
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) — Creating ML pipelines with Spark estimators
- GPU Training on Databricks — Using GPU clusters for accelerated machine learning
- Autoscaling — Cluster autoscaling behavior and configuration
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking for machine learning workflows

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
- use-xgboost-on-databricks-databricks-on-aws.md

# Citations

1. [use-xgboost-on-databricks-databricks-on-aws.md](/references/use-xgboost-on-databricks-databricks-on-aws-87750cc6.md)
2. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
