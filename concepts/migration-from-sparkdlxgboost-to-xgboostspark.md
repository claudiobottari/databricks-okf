---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 512ce92c60f51c4ebe4cbd59307106932a0fb2a825d0d8a9d5add0e312eda24d
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migration-from-sparkdlxgboost-to-xgboostspark
    - MFSTX
    - migration guide from sparkdl.xgboost to xgboost.spark
    - Migration from sparkdl.xgboost
    - sparkdl.xgboost vs xgboost.spark Migration
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: Migration from sparkdl.xgboost to xgboost.spark
description: Guide for replacing deprecated sparkdl.xgboost estimators with xgboost.spark equivalents, including parameter name changes (camelCase to snake_case) and removal of use_external_storage.
tags:
  - migration
  - spark
  - xgboost
timestamp: "2026-06-19T18:36:06.082Z"
---

```markdown
---
title: Migration from sparkdl.xgboost to xgboost.spark
summary: Migration guide for replacing the deprecated sparkdl.xgboost module with xgboost.spark, including import changes, parameter name changes (camelCase to snake_case), removal of `use_external_storage`, and a utility function to convert saved models.
sources:
  - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:06:58.446Z"
updatedAt: "2026-06-19T10:18:03.306Z"
tags:
  - migration
  - deprecation
  - xgboost
  - spark
aliases:
  - migration-from-sparkdlxgboost-to-xgboostspark
  - MFSTX
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Migration from sparkdl.xgboost to xgboost.spark

The `sparkdl.xgboost` module has been deprecated since Databricks Runtime 12.0 ML. Users should migrate to the `xgboost.spark` module, which is available in `xgboost>=1.7` and provides PySpark estimators that support inclusion in [[MLlib Pipelines API|SparkML Pipelines]]. The new module includes `xgboost.spark.SparkXGBRegressor`, `xgboost.spark.SparkXGBClassifier`, and `xgboost.spark.SparkXGBRanker`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Requirements

`xgboost.spark` requires Databricks Runtime 12.0 ML and above. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Import Changes

Replace the deprecated import statements with their `xgboost.spark` equivalents:

- Replace `from sparkdl.xgboost import XgboostRegressor` with `from xgboost.spark import SparkXGBRegressor`.
- Replace `from sparkdl.xgboost import XgboostClassifier` with `from xgboost.spark import SparkXGBClassifier`.

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Parameter Name Changes

All parameter names in the estimator constructor must be changed from camelCase style to snake_case style. For example, change `XgboostRegressor(featuresCol=XXX)` to `SparkXGBRegressor(features_col=XXX)`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Removed Parameters

The parameters `use_external_storage` and `external_storage_precision` have been removed. `xgboost.spark` estimators use the DMatrix data iteration API to use memory more efficiently, eliminating the need for external storage mode. For extremely large datasets, Databricks recommends increasing the `num_workers` parameter so that each training task partitions the data into smaller, more manageable partitions. Consider setting `num_workers = sc.defaultParallelism`, which sets `num_workers` to the total number of Spark task slots in the cluster. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Changes in CPU Core Usage

For estimators defined in `xgboost.spark`, setting `num_workers=1` executes model training using a single Spark task. This utilizes the number of CPU cores specified by the Spark cluster configuration setting `spark.task.cpus`, which is 1 by default. To use more CPU cores to train the model, increase `num_workers` or `spark.task.cpus`. You cannot set the `nthread` or `n_jobs` parameter for estimators defined in `xgboost.spark`. This behavior differs from the deprecated `sparkdl.xgboost` package. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Converting sparkdl.xgboost Models to xgboost.spark Models

`sparkdl.xgboost` models are saved in a different format than `xgboost.spark` models and have different parameter settings. Use the following utility function to convert a model:

```python
def convert_sparkdl_model_to_xgboost_spark_model(
    xgboost_spark_estimator_cls,
    sparkdl_xgboost_model,
):
    """
    :param xgboost_spark_estimator_cls:
        `xgboost.spark` estimator class, e.g. `xgboost.spark.SparkXGBRegressor`
    :param sparkdl_xgboost_model:
        `sparkdl.xgboost` model instance e.g. the instance of 
        `sparkdl.xgboost.XgboostRegressorModel` type.
    :return
        A `xgboost.spark` model instance
    """
    def convert_param_key(key):
        from xgboost.spark.core import _inverse_pyspark_param_alias_map
        if key == "baseMarginCol":
            return "base_margin_col"
        if key in _inverse_pyspark_param_alias_map:
            return _inverse_pyspark_param_alias_map[key]
        if key in ['use_external_storage', 'external_storage_precision', 'nthread', 'n_jobs', 'base_margin_eval_set']:
            return None
        return key

    xgboost_spark_params_dict = {}
    for param in sparkdl_xgboost_model.params:
        if param.name == "arbitraryParamsDict":
            continue
        if sparkdl_xgboost_model.isDefined(param):
            xgboost_spark_params_dict[param.name] = sparkdl_xgboost_model.getOrDefault(param)
    xgboost_spark_params_dict.update(sparkdl_xgboost_model.getOrDefault("arbitraryParamsDict"))
    xgboost_spark_params_dict = {
        convert_param_key(k): v
        for k, v in xgboost_spark_params_dict.items()
        if convert_param_key(k) is not None
    }
    booster = sparkdl_xgboost_model.get_booster()
    booster_bytes = booster.save_raw("json")
    booster_config = booster.save_config()
    estimator = xgboost_spark_estimator_cls(**xgboost_spark_params_dict)
    sklearn_model = estimator._convert_to_sklearn_model(booster_bytes, booster_config)
    return estimator._copyValues(estimator._create_pyspark_model(sklearn_model))

# Example
from xgboost.spark import SparkXGBRegressor
new_model = convert_sparkdl_model_to_xgboost_spark_model(
    xgboost_spark_estimator_cls=SparkXGBRegressor,
    sparkdl_xgboost_model=model,
)
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Converting a PipelineModel

If you have a `pyspark.ml.PipelineModel` containing a `sparkdl.xgboost` model as the last stage, replace that stage with the converted `xgboost.spark` model:

```python
pipeline_model.stages[-1] = convert_sparkdl_model_to_xgboost_spark_model(
    xgboost_spark_estimator_cls=SparkXGBRegressor,
    sparkdl_xgboost_model=pipeline_model.stages[-1],
)
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- [[Distributed Training with xgboost.spark|Distributed Training of XGBoost Models]] — Using `num_workers` for distributed training
- [[GPU-Accelerated XGBoost Training|XGBoost GPU Training]] — Enabling GPU training with `use_gpu=True`
- [[MLlib Pipelines API|SparkML Pipelines]] — Integrating XGBoost estimators into ML pipelines
- XGBoost Parameters — API documentation for available parameters

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
```

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
