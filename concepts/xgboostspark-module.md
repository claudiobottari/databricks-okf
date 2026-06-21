---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ed1e5127ff72939f6b277eab2199349feb277b6c816d9a427e1921e88015883
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboostspark-module
    - XGBoost Spark Module
    - XGBoost
    - XGBoost Spark
    - XGBoost for PySpark Pipeline
    - XGBoost on GPU with PySpark
    - xgboost.spark
    - xgboostspark-module-api
    - XMA
    - xgboostspark-module-pyspark-xgboost-estimators
    - XM(XE
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: xgboost.spark Module
description: PySpark estimators (SparkXGBRegressor, SparkXGBClassifier, SparkXGBRanker) that support inclusion of XGBoost in SparkML Pipelines, available in xgboost>=1.7.
tags:
  - machine-learning
  - spark
  - xgboost
timestamp: "2026-06-19T18:35:46.621Z"
---

# xgboost.spark Module

The `xgboost.spark` module, available in `xgboost>=1.7`, provides PySpark estimators that integrate XGBoost into [SparkML Pipelines](/concepts/mllib-pipelines-api.md). The module includes three main estimator classes: `SparkXGBRegressor`, `SparkXGBClassifier`, and `SparkXGBRanker`. These classes support distributed training and full compatibility with the Spark MLlib ecosystem. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Requirements

The `xgboost.spark` module requires Databricks Runtime 12.0 ML and above. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Parameters

The estimators in `xgboost.spark` support most parameters from standard XGBoost. The class constructor, `fit` method, and `predict` method parameters are largely identical to those in the `xgboost.sklearn` module, with naming, values, and defaults consistent with the [XGBoost parameters documentation](https://xgboost.readthedocs.io/en/stable/parameter.html). ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

Unsupported parameters include `gpu_id`, `nthread`, `sample_weight`, and `eval_set`. The module adds PySpark-specific parameters such as `featuresCol`, `labelCol`, `use_gpu`, and `validationIndicatorCol`. For full details, see the [XGBoost Python Spark API documentation](https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.spark). ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Distributed Training

The `xgboost.spark` module supports distributed XGBoost training through the `num_workers` parameter. To use distributed training, create a classifier or regressor and set `num_workers` to the number of concurrent Spark tasks during training. To utilize all available Spark task slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier
classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism)
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Limitations

- `mlflow.xgboost.autolog` is not supported with distributed XGBoost. To log an XGBoost Spark model using [MLflow](/concepts/mlflow.md), use `mlflow.spark.log_model(spark_xgb_model, artifact_path)`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- Distributed XGBoost cannot be used on clusters with autoscaling enabled, as new worker nodes that start during elastic scaling cannot receive new tasks and remain idle. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Sparse Features Optimization

The module supports optimization for training on datasets with sparse features. To enable this, provide a dataset with a features column of type `pyspark.ml.linalg.SparseVector`, set `enable_sparse_data_optim=True`, and set `missing=0.0`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier
classifier = SparkXGBClassifier(enable_sparse_data_optim=True, missing=0.0)
classifier.fit(dataset_with_sparse_features_col)
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## GPU Training

Set `use_gpu=True` to enable GPU training. For each Spark task used in distributed training, only one GPU is used. Databricks recommends using the default value of `1` for the Spark cluster configuration `spark.task.resource.gpu.amount` to avoid idle GPUs. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier
classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism, use_gpu=True)
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Troubleshooting

During multi-node GPU training, a `NCCL failure: remote process exited or there was a network error` message typically indicates a network communication problem among GPUs. To resolve this, set the Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Migration from `sparkdl.xgboost`

The deprecated `sparkdl.xgboost` module has been replaced by `xgboost.spark`. Key migration steps include: ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

1. Replace imports from `sparkdl.xgboost` with `xgboost.spark` equivalents (e.g., `XgboostRegressor` becomes `SparkXGBRegressor`).
2. Change parameter names from camelCase to snake_case (e.g., `featuresCol` becomes `features_col`).
3. The `use_external_storage` and `external_storage_precision` parameters have been removed. For large datasets, increase `num_workers` instead.
4. With `num_workers=1`, training uses only the CPU cores specified by `spark.task.cpus` (default 1). The `nthread` and `n_jobs` parameters are not supported.

### Model Conversion

A utility function is available to convert saved `sparkdl.xgboost` models to `xgboost.spark` format. The function handles parameter mapping and booster conversion. For `pyspark.ml.PipelineModel` instances containing a `sparkdl.xgboost` model as the last stage, the stage can be replaced with the converted model. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- [SparkML Pipelines](/concepts/mllib-pipelines-api.md) — The pipeline framework into which XGBoost estimators integrate
- [MLflow](/concepts/mlflow.md) — For logging and managing XGBoost Spark models
- GPU Training on Databricks — Best practices for GPU-accelerated machine learning
- XGBoost Parameters — The full set of XGBoost configuration options

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
