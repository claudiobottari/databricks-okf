---
title: Distributed training of XGBoost models using xgboost.spark | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/xgboost-spark
ingestedAt: "2026-06-18T08:13:48.012Z"
---

The Python package xgboost>=1.7 contains a new module `xgboost.spark`. This module includes the xgboost PySpark estimators `xgboost.spark.SparkXGBRegressor`, `xgboost.spark.SparkXGBClassifier`, and `xgboost.spark.SparkXGBRanker`. These new classes support the inclusion of XGBoost estimators in SparkML Pipelines. For API details, see the [XGBoost python spark API doc](https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.spark).

## Requirements[​](#requirements "Direct link to Requirements")

Databricks Runtime 12.0 ML and above.

## `xgboost.spark` parameters[​](#xgboostspark-parameters "Direct link to xgboostspark-parameters")

The estimators defined in the `xgboost.spark` module support most of the same parameters and arguments used in standard XGBoost.

*   The parameters for the class constructor, `fit` method, and `predict` method are largely identical to those in the `xgboost.sklearn` module.
*   Naming, values, and defaults are mostly identical to those described in [XGBoost parameters](https://xgboost.readthedocs.io/en/stable/parameter.html).
*   Exceptions are a few unsupported parameters (such as `gpu_id`, `nthread`, `sample_weight`, `eval_set`), and the `pyspark` estimator specific parameters that have been added (such as `featuresCol`, `labelCol`, `use_gpu`, `validationIndicatorCol`). For details, see [XGBoost Python Spark API documentation](https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.spark).

## Distributed training[​](#distributed-training "Direct link to Distributed training")

PySpark estimators defined in the `xgboost.spark` module support distributed XGBoost training using the `num_workers` parameter. To use distributed training, create a classifier or regressor and set `num_workers` to the number of concurrent running Spark tasks during distributed training. To use the all Spark task slots, set `num_workers=sc.defaultParallelism`.

For example:

Python

    from xgboost.spark import SparkXGBClassifierclassifier = SparkXGBClassifier(num_workers=sc.defaultParallelism)

note

*   You cannot use `mlflow.xgboost.autolog` with distributed XGBoost. To log an xgboost Spark model using MLflow, use `mlflow.spark.log_model(spark_xgb_model, artifact_path)`.
*   You cannot use distributed XGBoost on a cluster that has autoscaling enabled. New worker nodes that start in this elastic scaling paradigm cannot receive new sets of tasks and remain idle. For instructions to disable autoscaling, see [Enable autoscaling](https://docs.databricks.com/aws/en/compute/configure#autoscaling).

## Enable optimization for training on sparse features dataset[​](#enable-optimization-for-training-on-sparse-features-dataset "Direct link to Enable optimization for training on sparse features dataset")

PySpark Estimators defined in `xgboost.spark` module support optimization for training on datasets with sparse features. To enable optimization of sparse feature sets, you need to provide a dataset to the `fit` method that contains a features column consisting of values of type `pyspark.ml.linalg.SparseVector` and set the estimator parameter `enable_sparse_data_optim` to `True`. Additionally, you need to set the `missing` parameter to `0.0`.

For example:

Python

    from xgboost.spark import SparkXGBClassifierclassifier = SparkXGBClassifier(enable_sparse_data_optim=True, missing=0.0)classifier.fit(dataset_with_sparse_features_col)

## GPU training[​](#gpu-training "Direct link to GPU training")

PySpark estimators defined in the `xgboost.spark` module support training on GPUs. Set the parameter `use_gpu` to `True` to enable GPU training.

note

For each Spark task used in XGBoost distributed training, only one GPU is used in training when the `use_gpu` argument is set to `True`. Databricks recommends using the default value of `1` for the Spark cluster configuration `spark.task.resource.gpu.amount`. Otherwise, the additional GPUs allocated to this Spark task are idle.

For example:

Python

    from xgboost.spark import SparkXGBClassifierclassifier = SparkXGBClassifier(num_workers=sc.defaultParallelism, use_gpu=True)

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

During multi-node training, if you encounter a `NCCL failure: remote process exited or there was a network error` message, it typically indicates a problem with network communication among GPUs. This issue arises when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication.

To resolve, set the cluster's sparkConf for `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This essentially sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all of the workers in a node.

## Example notebook[​](#example-notebook "Direct link to Example notebook")

This notebook shows the use of the Python package `xgboost.spark` with Spark MLlib.

#### PySpark-XGBoost notebook

## Migration guide for the deprecated `sparkdl.xgboost` module[​](#migration-guide-for-the-deprecated-sparkdlxgboost-module "Direct link to migration-guide-for-the-deprecated-sparkdlxgboost-module")

*   Replace `from sparkdl.xgboost import XgboostRegressor` with `from xgboost.spark import SparkXGBRegressor` and replace `from sparkdl.xgboost import XgboostClassifier` with `from xgboost.spark import SparkXGBClassifier`.
*   Change all parameter names in the estimator constructor from camelCase style to snake\_case style. For example, change `XgboostRegressor(featuresCol=XXX)` to `SparkXGBRegressor(features_col=XXX)`.
*   The parameters `use_external_storage` and `external_storage_precision` have been removed. `xgboost.spark` estimators use the DMatrix data iteration API to use memory more efficiently. There is no longer a need to use the inefficient external storage mode. For extremely large datasets, Databricks recommends that you increase the `num_workers` parameter, which makes each training task partition the data into smaller, more manageable data partitions. Consider setting `num_workers = sc.defaultParallelism`, which sets `num_workers` to the total number of Spark task slots in the cluster.
*   For estimators defined in `xgboost.spark`, setting `num_workers=1` executes model training using a single Spark task. This utilizes the number of CPU cores specified by the Spark cluster configuration setting `spark.task.cpus`, which is 1 by default. To use more CPU cores to train the model, increase `num_workers` or `spark.task.cpus`. You cannot set the `nthread` or `n_jobs` parameter for estimators defined in `xgboost.spark`. This behavior is different from the previous behavior of estimators defined in the deprecated `sparkdl.xgboost` package.

### Convert `sparkdl.xgboost` model into `xgboost.spark` model[​](#convert-sparkdlxgboost-model-into-xgboostspark-model "Direct link to convert-sparkdlxgboost-model-into-xgboostspark-model")

`sparkdl.xgboost` models are saved in a different format than `xgboost.spark` models and have [different parameter settings](#xgboost-spark-parameters). Use the following utility function to convert the model:

Python

    def convert_sparkdl_model_to_xgboost_spark_model(  xgboost_spark_estimator_cls,  sparkdl_xgboost_model,):  """  :param xgboost_spark_estimator_cls:      `xgboost.spark` estimator class, e.g. `xgboost.spark.SparkXGBRegressor`  :param sparkdl_xgboost_model:      `sparkdl.xgboost` model instance e.g. the instance of       `sparkdl.xgboost.XgboostRegressorModel` type.  :return      A `xgboost.spark` model instance  """  def convert_param_key(key):    from xgboost.spark.core import _inverse_pyspark_param_alias_map    if key == "baseMarginCol":      return "base_margin_col"    if key in _inverse_pyspark_param_alias_map:      return _inverse_pyspark_param_alias_map[key]    if key in ['use_external_storage', 'external_storage_precision', 'nthread', 'n_jobs', 'base_margin_eval_set']:      return None    return key  xgboost_spark_params_dict = {}  for param in sparkdl_xgboost_model.params:    if param.name == "arbitraryParamsDict":      continue    if sparkdl_xgboost_model.isDefined(param):      xgboost_spark_params_dict[param.name] = sparkdl_xgboost_model.getOrDefault(param)  xgboost_spark_params_dict.update(sparkdl_xgboost_model.getOrDefault("arbitraryParamsDict"))  xgboost_spark_params_dict = {    convert_param_key(k): v    for k, v in xgboost_spark_params_dict.items()    if convert_param_key(k) is not None  }  booster = sparkdl_xgboost_model.get_booster()  booster_bytes = booster.save_raw("json")  booster_config = booster.save_config()  estimator = xgboost_spark_estimator_cls(**xgboost_spark_params_dict)  sklearn_model = estimator._convert_to_sklearn_model(booster_bytes, booster_config)  return estimator._copyValues(estimator._create_pyspark_model(sklearn_model))# Examplefrom xgboost.spark import SparkXGBRegressornew_model = convert_sparkdl_model_to_xgboost_spark_model(  xgboost_spark_estimator_cls=SparkXGBRegressor,  sparkdl_xgboost_model=model,)

If you have a `pyspark.ml.PipelineModel` model containing a `sparkdl.xgboost` model as the last stage, you can replace the stage of `sparkdl.xgboost` model with the converted `xgboost.spark` model.

Python

    pipeline_model.stages[-1] = convert_sparkdl_model_to_xgboost_spark_model(  xgboost_spark_estimator_cls=SparkXGBRegressor,  sparkdl_xgboost_model=pipeline_model.stages[-1],)
