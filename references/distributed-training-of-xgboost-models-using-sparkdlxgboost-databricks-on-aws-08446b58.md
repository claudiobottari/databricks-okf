---
title: Distributed training of XGBoost models using sparkdl.xgboost | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/sparkdl-xgboost
ingestedAt: "2026-06-18T08:13:38.294Z"
---

Databricks Runtime ML includes PySpark estimators based on the Python `xgboost` package, `sparkdl.xgboost.XgboostRegressor` and `sparkdl.xgboost.XgboostClassifier`. You can create an ML pipeline based on these estimators. For more information, see [XGBoost for PySpark Pipeline](https://databricks.github.io/spark-deep-learning/#module-sparkdl.xgboost).

Databricks strongly recommends that `sparkdl.xgboost` users use Databricks Runtime 11.3 LTS ML or above. Previous Databricks Runtime versions are affected by bugs in older versions of `sparkdl.xgboost`.

note

*   The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks recommends that you migrate your code to use the `xgboost.spark` module instead. See [the migration guide](https://docs.databricks.com/aws/en/machine-learning/train-model/xgboost-spark#xgboost-migration).
*   The following parameters from the `xgboost` package are not supported: `gpu_id`, `output_margin`, `validate_features`.
*   The parameters `sample_weight`, `eval_set`, and `sample_weight_eval_set` are not supported. Instead, use the parameters `weightCol` and `validationIndicatorCol`. See [XGBoost for PySpark Pipeline](https://databricks.github.io/spark-deep-learning/#module-sparkdl.xgboost) for details.
*   The parameters `base_margin`, and `base_margin_eval_set` are not supported. Use the parameter `baseMarginCol` instead. See [XGBoost for PySpark Pipeline](https://databricks.github.io/spark-deep-learning/#module-sparkdl.xgboost) for details.
*   The parameter `missing` has different semantics from the `xgboost` package. In the `xgboost` package, the zero values in a SciPy sparse matrix are treated as missing values regardless of the value of `missing`. For the PySpark estimators in the `sparkdl` package, zero values in a Spark sparse vector are not treated as missing values unless you set `missing=0`. If you have a sparse training dataset (most feature values are missing), Databricks recommends setting `missing=0` to reduce memory consumption and achieve better performance.

## Distributed training[​](#distributed-training "Direct link to Distributed training")

Databricks Runtime ML supports distributed XGBoost training using the `num_workers` parameter. To use distributed training, create a classifier or regressor and set `num_workers` to a value less than or equal to the total number of Spark task slots on your cluster. To use the all Spark task slots, set `num_workers=sc.defaultParallelism`.

For example:

Python

    classifier = XgboostClassifier(num_workers=sc.defaultParallelism)regressor = XgboostRegressor(num_workers=sc.defaultParallelism)

## Limitations of distributed training[​](#limitations-of-distributed-training "Direct link to Limitations of distributed training")

*   You cannot use `mlflow.xgboost.autolog` with distributed XGBoost.
*   You cannot use `baseMarginCol` with distributed XGBoost.
*   You cannot use distributed XGBoost on an cluster with autoscaling enabled. See [Enable autoscaling](https://docs.databricks.com/aws/en/compute/configure#autoscaling) for instructions to disable autoscaling.

## GPU training[​](#gpu-training "Direct link to GPU training")

note

Databricks Runtime 11.3 LTS ML includes XGBoost 1.6.1, which does not support GPU clusters with [compute capability](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#compute-capability) 5.2 and below.

Databricks Runtime 9.1 LTS ML and above support GPU clusters for XGBoost training. To use a GPU cluster, set `use_gpu` to `True`.

For example:

Python

    classifier = XgboostClassifier(num_workers=N, use_gpu=True)regressor = XgboostRegressor(num_workers=N, use_gpu=True)

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

During multi-node training, if you encounter a `NCCL failure: remote process exited or there was a network error` message, it typically indicates a problem with network communication among GPUs. This issue arises when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication.

To resolve, set the cluster's sparkConf for `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This essentially sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all of the workers in a node.

## Example notebook[​](#example-notebook "Direct link to Example notebook")

This notebook shows the use of the Python package `sparkdl.xgboost` with Spark MLlib. The `sparkdl.xgboost` package is deprecated since Databricks Runtime 12.0 ML.

#### PySpark-XGBoost notebook
