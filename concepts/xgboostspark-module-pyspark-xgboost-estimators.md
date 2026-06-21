---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 635769ba87545f01213d059c25e429862638d19f5060788698f1c5c6655a8208
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboostspark-module-pyspark-xgboost-estimators
    - XM(XE
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: xgboost.spark Module (PySpark XGBoost Estimators)
description: A Python module in xgboost>=1.7 providing SparkXGBRegressor, SparkXGBClassifier, and SparkXGBRanker for integrating XGBoost into SparkML Pipelines
tags:
  - machine-learning
  - spark
  - xgboost
  - distributed-training
timestamp: "2026-06-19T10:17:30.421Z"
---

# xgboost.spark Module (PySpark XGBoost Estimators)

The **`xgboost.spark` module** provides PySpark estimators for distributed [XGBoost](/concepts/xgboostspark-module.md) training that integrate directly into [SparkML Pipelines](/concepts/mllib-pipelines-api.md). Introduced in XGBoost 1.7, the module replaces the deprecated `sparkdl.xgboost` package with native Spark-compatible classes. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Overview

The `xgboost.spark` module defines three primary estimator classes: ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

- `xgboost.spark.SparkXGBRegressor` — for regression tasks
- `xgboost.spark.SparkXGBClassifier` — for classification tasks
- `xgboost.spark.SparkXGBRanker` — for ranking tasks

These estimators support most XGBoost parameters from the standard API, with naming conventions using snake_case (e.g., `features_col`, `label_col`) rather than camelCase found in the deprecated `sparkdl.xgboost` module. Parameters from `xgboost.sklearn` are largely identical in naming, values, and defaults. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Requirements

Databricks Runtime 12.0 ML and above. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Distributed Training

The PySpark estimators support distributed training through the `num_workers` parameter. Set `num_workers` to the number of concurrent Spark tasks during training. To use all available Spark task slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism)
```

### Limitations

- [MLflow Autologging](/concepts/mlflow-autologging.md) with `mlflow.xgboost.autolog` is not supported for distributed XGBoost. Use `mlflow.spark.log_model(spark_xgb_model, artifact_path)` instead. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- Distributed XGBoost cannot be used on [autoscaling clusters](/concepts/fixed-size-vs-auto-scaling-ray-clusters.md), as new worker nodes cannot receive new task sets and remain idle. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Sparse Feature Optimization

The module supports optimization for training on datasets with sparse features. To enable this: ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

1. Ensure the features column contains values of type `pyspark.ml.linalg.SparseVector`
2. Set `enable_sparse_data_optim=True`
3. Set `missing=0.0`

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(enable_sparse_data_optim=True, missing=0.0)
classifier.fit(dataset_with_sparse_features_col)
```

## GPU Training

Set `use_gpu=True` to enable GPU training. For each Spark task in distributed training, only one GPU is used. Set `spark.task.resource.gpu.amount` to `1` in the cluster configuration to avoid idle GPUs. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism, use_gpu=True)
```

## Migration from `sparkdl.xgboost`

The `sparkdl.xgboost` module is deprecated. Migration involves: ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

- Changing import statements to `from xgboost.spark import SparkXGBRegressor` or `SparkXGBClassifier`
- Converting all parameter names from camelCase to snake_case (e.g., `featuresCol` → `features_col`)
- Removing `use_external_storage` and `external_storage_precision` parameters, as `xgboost.spark` uses the DMatrix data iteration API for memory efficiency
- Understanding that `num_workers=1` uses CPU cores specified by `spark.task.cpus` (default 1), and `nthread`/`n_jobs` parameters are not supported

The module provides a utility function to convert existing `sparkdl.xgboost` models to `xgboost.spark` format, preserving booster data and configuration. PipelineModel stages containing `sparkdl.xgboost` models can be replaced in-place with the converted `xgboost.spark` model. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Troubleshooting

Multi-node GPU training may produce the error `NCCL failure: remote process exited or there was a network error`, indicating communication problems between GPUs. Set the cluster Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth` to resolve this network issue. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) — The gradient boosting framework
- [SparkML Pipelines](/concepts/mllib-pipelines-api.md) — ML pipeline integration
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-worker training strategies
- GPU Scheduling — GPU resource allocation
- MLflow Integration — Model logging and tracking

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
