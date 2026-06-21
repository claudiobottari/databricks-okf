---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 728e3c152736cab7b5bf142ff51bae844a7852027c1fc51a05f39391355e45c3
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-conversion-from-sparkdlxgboost-to-xgboostspark
    - MCFSTX
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: Model Conversion from sparkdl.xgboost to xgboost.spark
description: Utility function to convert saved sparkdl.xgboost models into xgboost.spark format, handling parameter mapping and booster serialization.
tags:
  - migration
  - model-serialization
  - spark
  - xgboost
timestamp: "2026-06-19T18:36:11.498Z"
---

# Model Conversion from `sparkdl.xgboost` to `xgboost.spark`

The `sparkdl.xgboost` module has been deprecated in favor of the `xgboost.spark` module (available in XGBoost 1.7+ and Databricks Runtime 12.0 ML and above). Models saved by `sparkdl.xgboost` use a different format and parameter set. A migration guide and utility function are provided to convert existing models and update code. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Required Code Changes

To migrate from `sparkdl.xgboost` to `xgboost.spark`, apply the following changes:

- **Import statements:** Replace `from sparkdl.xgboost import XgboostRegressor` with `from xgboost.spark import SparkXGBRegressor`, and replace `from sparkdl.xgboost import XgboostClassifier` with `from xgboost.spark import SparkXGBClassifier`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- **Parameter naming:** Change all parameter names from camelCase style to snake_case style. For example, `XgboostRegressor(featuresCol=XXX)` becomes `SparkXGBRegressor(features_col=XXX)`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- **Removed parameters:** `use_external_storage` and `external_storage_precision` are no longer supported. The `xgboost.spark` estimators use the DMatrix data iteration API for efficient memory usage. For very large datasets, increase the `num_workers` parameter (e.g., `num_workers = sc.defaultParallelism`) so each training task processes smaller partitions. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- **CPU core usage:** In `xgboost.spark`, setting `num_workers=1` runs a single Spark task using the number of CPU cores specified by `spark.task.cpus` (default 1). To use more cores, increase `num_workers` or `spark.task.cpus`. The `nthread` and `n_jobs` parameters are not supported, unlike in `sparkdl.xgboost`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Converting a Saved Model

The following utility function converts a `sparkdl.xgboost` model instance into an equivalent `xgboost.spark` model: ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

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
```

The function:

- Extracts parameters from the `sparkdl.xgboost` model, excluding `arbitraryParamsDict` (which is merged separately). ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- Converts camelCase parameter keys to snake_case using an internal alias map (`_inverse_pyspark_param_alias_map`) and drops unsupported parameters. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- Reads the underlying booster, saves it in JSON format, and then creates a new `xgboost.spark` estimator with the converted parameters. The booster is converted into a scikit-learn model via `_convert_to_sklearn_model`, and finally a `pyspark` model is created and its values are copied from the estimator. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Example usage

```python
from xgboost.spark import SparkXGBRegressor

new_model = convert_sparkdl_model_to_xgboost_spark_model(
    xgboost_spark_estimator_cls=SparkXGBRegressor,
    sparkdl_xgboost_model=model,
)
```

### Converting a PipelineModel

If you have a `pyspark.ml.PipelineModel` that contains a `sparkdl.xgboost` model as the last stage, replace that stage directly: ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
pipeline_model.stages[-1] = convert_sparkdl_model_to_xgboost_spark_model(
    xgboost_spark_estimator_cls=SparkXGBRegressor,
    sparkdl_xgboost_model=pipeline_model.stages[-1],
)
```

## Related Concepts

- [Distributed Training of XGBoost Models](/concepts/distributed-training-with-xgboostspark.md) – Overview of the `xgboost.spark` module and distributed training with `num_workers`.
- [SparkML Pipelines](/concepts/mllib-pipelines-api.md) – Framework for building ML pipelines on Apache Spark.
- XGBoost Parameters – Reference for parameter naming, values, and defaults.
- Model Migration – General strategies for upgrading ML model code between library versions.

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
