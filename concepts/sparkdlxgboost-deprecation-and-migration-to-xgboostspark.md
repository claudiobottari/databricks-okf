---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0f69b9b42a44ff5e4e22d0195497c78ea50ab46e73c7b4b05e5e5ab41ca846db
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparkdlxgboost-deprecation-and-migration-to-xgboostspark
    - Migration to xgboost.spark and sparkdl.xgboost Deprecation
    - SDAMTX
    - sparkdl.xgboost (deprecated)
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: sparkdl.xgboost Deprecation and Migration to xgboost.spark
description: The sparkdl.xgboost module is deprecated since Databricks Runtime 12.0 ML; users should migrate to the xgboost.spark module.
tags:
  - deprecation
  - migration
  - xgboost
  - databricks
timestamp: "2026-06-18T12:05:41.859Z"
---

# sparkdl.xgboost Deprecation and Migration to xgboost.spark

The `sparkdl.xgboost` module, which provided PySpark estimators for distributed XGBoost training, was deprecated starting in Databricks Runtime 12.0 ML. Databricks strongly recommends that users migrate their code to the `xgboost.spark` module for ongoing support and access to the latest XGBoost features. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Deprecation Scope

| Item | Details |
|------|---------|
| Deprecated module | `sparkdl.xgboost` (both `XgboostClassifier` and `XgboostRegressor`) |
| Deprecated since | Databricks Runtime 12.0 ML |
| Recommended replacement | `xgboost.spark` module |
| Migration guidance | See the [official migration guide](https://docs.databricks.com/aws/en/machine-learning/train-model/xgboost-spark#xgboost-migration) |

^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Migration Overview

The `xgboost.spark` module is the native Spark integration provided by the upstream `xgboost` Python package. It offers a more modern API, better integration with Spark MLlib pipelines, and active maintenance. Moving your code from `sparkdl.xgboost` to `xgboost.spark` requires updating import statements, adjusting parameter names, and verifying pipeline logic. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### Old (sparkdl.xgboost) vs. New (xgboost.spark) API

| Aspect | `sparkdl.xgboost` | `xgboost.spark` |
|--------|-------------------|-----------------|
| Import | `from sparkdl.xgboost import XgboostClassifier` | `from xgboost.spark import SparkXGBClassifier` |
| Estimator class (classification) | `XgboostClassifier` | `SparkXGBClassifier` |
| Estimator class (regression) | `XgboostRegressor` | `SparkXGBRegressor` |
| Distribution parameter | `num_workers` | `n_workers` |
| GPU control | `use_gpu=True` | `device="cuda"` or `tree_method="hist"` + `device="cuda"` |
| Validation indicator | `validationIndicatorCol` | See migration guide |
| Weights | `weightCol` | Supported similarly |
| Base margin | `baseMarginCol` | Supported differently |

^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Unsupported Parameters in sparkdl.xgboost

While using the deprecated `sparkdl.xgboost` module, be aware of these unsupported or differently-behaved parameters:

- `gpu_id`, `output_margin`, `validate_features` – **not supported**.
- `sample_weight`, `eval_set`, `sample_weight_eval_set` – not supported; use `weightCol` and `validationIndicatorCol` instead.
- `base_margin`, `base_margin_eval_set` – not supported; use `baseMarginCol` instead.
- `missing` – semantics differ: in the `xgboost` package, zero values in a SciPy sparse matrix are treated as missing regardless of the `missing` argument. In `sparkdl.xgboost`, zero values in a Spark sparse vector are **not** treated as missing unless you explicitly set `missing=0`. For sparse datasets, setting `missing=0` can reduce memory consumption and improve performance.

^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Distributed Training

`sparkdl.xgboost` supports distributed training via the `num_workers` parameter (mapped to Spark task slots). Key limitations: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

- `mlflow.xgboost.autolog` cannot be used with distributed training.
- `baseMarginCol` is incompatible with distributed training.
- Distributed training does not work on clusters with autoscaling enabled. Autoscaling must be disabled manually.

When migrating to `xgboost.spark`, distributed training is configured through the `n_workers` parameter, and many of these limitations are resolved or handled differently.

## GPU Training

`sparkdl.xgboost` supports GPU training when `use_gpu=True` is set. Databricks Runtime 11.3 LTS ML (which bundles XGBoost 1.6.1) does not support GPU clusters with NVIDIA compute capability 5.2 or below. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

When migrating to `xgboost.spark`, GPU acceleration is enabled via the `device` parameter (e.g., `device="cuda"`) or by setting `tree_method` and `device` accordingly. Consult the `xgboost.spark` documentation for the exact syntax.

## Troubleshooting NCCL Errors in Distributed GPU Training

When using `sparkdl.xgboost` with multi-node GPU clusters, the error `NCCL failure: remote process exited or there was a network error` may appear. This is caused by NCCL (NVIDIA Collective Communications Library) being unable to select the correct network interface for GPU communication. The workaround is to set the Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME=eth` on the cluster, which forces NCCL to use the `eth` interface for all workers on each node. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Best Practices

- **Plan migration early.** As of Databricks Runtime 12.0 ML, `sparkdl.xgboost` is deprecated. New features, performance improvements, and bug fixes will only land in `xgboost.spark`.
- **Use Databricks Runtime 11.3 LTS ML or above** if you must temporarily stay on `sparkdl.xgboost` (due to bugs in older runtimes), but aim to migrate quickly.
- **Test with equivalent hyperparameters.** Parameter names and defaults may differ between the two modules. Use the migration guide to map your existing configuration.
- **Update pipeline code end-to-end.** If you are using `Spark ML Pipeline` objects, replace the estimator stages, retrain, and revalidate the pipeline.

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) – The underlying gradient boosting framework.
- [PySpark MLlib](/concepts/apache-spark-mllib.md) – The machine learning library that both estimators integrate with.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Autologging for XGBoost is not supported with the deprecated module.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime that bundles both modules.
- NCCL – The NVIDIA communication library that can cause errors in multi-GPU setups.

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
