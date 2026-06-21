---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b96ab9f6cef5c6599336d4140deb1b88862cac3178b29d044bc2b108256cb92c
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboostspark-module-api
    - XMA
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: xgboost.spark Module API
description: New PySpark estimators (SparkXGBRegressor, SparkXGBClassifier, SparkXGBRanker) that integrate XGBoost into SparkML Pipelines
tags:
  - machine-learning
  - xgboost
  - spark
  - API
timestamp: "2026-06-18T15:32:48.259Z"
---

# xgboost.spark Module API

The **`xgboost.spark` Module API** is a Python module introduced in `xgboost>=1.7` that provides PySpark estimators for integrating [XGBoost](/concepts/xgboostspark-module.md) models into [SparkML Pipelines](/concepts/mllib-pipelines-api.md). It includes three main estimator classes: `SparkXGBRegressor`, `SparkXGBClassifier`, and `SparkXGBRanker`. These classes support distributed training, GPU acceleration, and sparse data optimization. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Requirements

Using the `xgboost.spark` module requires **Databricks Runtime 12.0 ML or above**. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Parameters

The estimators in `xgboost.spark` support most of the same parameters and arguments used in standard XGBoost. The class constructor, `fit` method, and `predict` method parameters are largely identical to those in `xgboost.sklearn`, with the same naming, values, and defaults described in the [XGBoost Parameters](https://xgboost.readthedocs.io/en/stable/parameter.html) documentation. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Unsupported standard parameters

Several standard XGBoost parameters are **not supported** in the `xgboost.spark` module:
- `gpu_id`
- `nthread`
- `sample_weight`
- `eval_set`

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### PySpark‑specific parameters

PySpark‑specific parameters have been added, including:
- `featuresCol`
- `labelCol`
- `use_gpu`
- `validationIndicatorCol`

For a complete list, refer to the [XGBoost Python Spark API documentation](https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.spark). ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Distributed Training

The `xgboost.spark` estimators support **distributed training** via the `num_workers` parameter. Setting `num_workers` controls the number of concurrent Spark tasks used during training. To use all available task slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism)
```

### Limitations

- **MLflow autologging** is not supported with distributed XGBoost. To log an XGBoost Spark model using MLflow, use `mlflow.spark.log_model(spark_xgb_model, artifact_path)`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- **Autoscaling must be disabled** on the cluster. New worker nodes added during elastic scaling cannot receive tasks and remain idle. See the Databricks documentation on [enabling autoscaling](https://docs.databricks.com/aws/en/compute/configure#autoscaling) to disable it. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Sparse Data Optimization

For datasets with sparse features, the module provides an optimization mode. To enable it:
1. Provide a features column of type `pyspark.ml.linalg.SparseVector` to the `fit` method.
2. Set the estimator parameter `enable_sparse_data_optim` to `True`.
3. Set the `missing` parameter to `0.0`.

Example:

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(enable_sparse_data_optim=True, missing=0.0)
classifier.fit(dataset_with_sparse_features_col)
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## GPU Training

GPU training is enabled by setting the parameter `use_gpu` to `True`. Example:

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism, use_gpu=True)
```

### GPU resource allocation

When `use_gpu=True`, each Spark task used in distributed XGBoost training uses **only one GPU**. Databricks recommends using the default value of `1` for the Spark cluster configuration `spark.task.resource.gpu.amount`; setting a higher value results in idle GPU resources. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Troubleshooting

### NCCL network failure

During multi‑node GPU training, you may encounter the error:

```
NCCL failure: remote process exited or there was a network error
```

This indicates a network communication problem between GPUs, typically because NVIDIA Collective Communications Library (NCCL) cannot use certain network interfaces. To resolve it, set the cluster’s Spark configuration:

```
spark.executorEnv.NCCL_SOCKET_IFNAME=eth
```

This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Migration from Deprecated `sparkdl.xgboost`

The `xgboost.spark` module replaces the deprecated `sparkdl.xgboost` module. Key migration steps:

1. **Import changes**:
   - Replace `from sparkdl.xgboost import XgboostRegressor` with `from xgboost.spark import SparkXGBRegressor`.
   - Replace `from sparkdl.xgboost import XgboostClassifier` with `from xgboost.spark import SparkXGBClassifier`.

2. **Parameter naming**: Convert all camelCase parameter names to snake_case (e.g., `featuresCol` → `features_col`).

3. **Removed parameters**: `use_external_storage` and `external_storage_precision` are no longer available. The `xgboost.spark` estimators use the DMatrix data iteration API for more efficient memory usage. For extremely large datasets, Databricks recommends increasing `num_workers` (e.g., setting `num_workers = sc.defaultParallelism`) to partition data into smaller pieces.

4. **CPU control**: Setting `num_workers=1` runs training using a single Spark task. That task uses the number of CPU cores specified by `spark.task.cpus` (default 1). The `nthread` and `n_jobs` parameters are not supported in `xgboost.spark`. This differs from the deprecated `sparkdl.xgboost` package.

5. **Model conversion**: A utility function is provided to convert a saved `sparkdl.xgboost` model to an `xgboost.spark` model. It handles parameter key mapping, booster serialization, and configuration. The converted model can replace the last stage of a `pyspark.ml.PipelineModel`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Conversion utility function

```python
def convert_sparkdl_model_to_xgboost_spark_model(
    xgboost_spark_estimator_cls,
    sparkdl_xgboost_model,
):
    """Convert a sparkdl.xgboost model to an xgboost.spark model."""
    # (Implementation details as shown in the source)
    ...
```

Usage example:

```python
from xgboost.spark import SparkXGBRegressor

new_model = convert_sparkdl_model_to_xgboost_spark_model(
    xgboost_spark_estimator_cls=SparkXGBRegressor,
    sparkdl_xgboost_model=model,
)
```

For a `pyspark.ml.PipelineModel` containing a `sparkdl.xgboost` model as the last stage:

```python
pipeline_model.stages[-1] = convert_sparkdl_model_to_xgboost_spark_model(
    xgboost_spark_estimator_cls=SparkXGBRegressor,
    sparkdl_xgboost_model=pipeline_model.stages[-1],
)
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Example Notebook

The source material includes an example notebook titled **PySpark-XGBoost notebook** that demonstrates using the `xgboost.spark` module with Spark MLlib. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- XGBoost Parameters
- [SparkML Pipelines](/concepts/mllib-pipelines-api.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- GPU Training on Databricks
- NCCL (NVIDIA Collective Communications Library)
- MLflow Integration
- Sparse Vectors in PySpark
- [sparkdl.xgboost (deprecated)](/concepts/sparkdlxgboost-deprecation-and-migration-to-xgboostspark.md)

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
