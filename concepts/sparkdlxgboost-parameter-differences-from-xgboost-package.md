---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 066c060e668e57bae354314b8db34139fea1641d0af20b5c63c8a21166b1ff25
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparkdlxgboost-parameter-differences-from-xgboost-package
    - SPDFXP
    - XGBoost Parameter Reference
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: sparkdl.xgboost Parameter Differences from xgboost Package
description: Important semantic differences in parameters between sparkdl.xgboost and the standard xgboost package, including handling of missing values in sparse vectors and unsupported parameters like gpu_id, output_margin, and validate_features
tags:
  - xgboost
  - spark
  - migration
  - compatibility
timestamp: "2026-06-19T18:35:34.842Z"
---

# sparkdl.xgboost Parameter Differences from xgboost Package

The `sparkdl.xgboost` module provides PySpark estimators (`XgboostRegressor` and `XgboostClassifier`) based on the Python `xgboost` package, but several parameters differ in behavior or are unsupported. Understanding these differences is essential when migrating code or building [ML Pipelines](/concepts/mllib-pipelines-api.md) with `sparkdl.xgboost`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Unsupported Parameters

The following parameters from the standard `xgboost` package are **not supported** in `sparkdl.xgboost`:

- `gpu_id`
- `output_margin`
- `validate_features`

^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Parameters Replaced by Spark-Specific Alternatives

Several `xgboost` parameters have no direct equivalent and must be replaced with Spark DataFrame column-based parameters:

| `xgboost` Parameter | `sparkdl.xgboost` Replacement | Description |
|---|---|---|
| `sample_weight` | `weightCol` | Specify a column in the DataFrame containing sample weights. |
| `eval_set` | `validationIndicatorCol` | Specify a column that indicates which rows belong to the validation set. |
| `sample_weight_eval_set` | `weightCol` (used with `validationIndicatorCol`) | Weights for evaluation samples are handled via the same weight column mechanism. |
| `base_margin` | `baseMarginCol` | Specify a column containing base margin values. |
| `base_margin_eval_set` | `baseMarginCol` | Base margin for evaluation sets is handled via the same column. |

^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Different Semantics: `missing` Parameter

The `missing` parameter has **different semantics** between the two packages:

- In the standard `xgboost` package, zero values in a SciPy sparse matrix are always treated as missing values, regardless of the value of `missing`.
- In `sparkdl.xgboost`, zero values in a Spark sparse vector are **not** treated as missing values unless you explicitly set `missing=0`.

If you have a sparse training dataset where most feature values are missing, Databricks recommends setting `missing=0` to reduce memory consumption and achieve better performance. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Distributed Training Parameter: `num_workers`

The `num_workers` parameter is specific to `sparkdl.xgboost` and enables [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) of XGBoost models across multiple Spark task slots. This parameter has no equivalent in the single-node `xgboost` package. To use all available Spark task slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## GPU Training Parameter: `use_gpu`

The `use_gpu` parameter is a `sparkdl.xgboost`-specific boolean that enables GPU training on supported clusters. This replaces the need to set `gpu_id` (which is unsupported) and instead uses all available GPUs on the cluster. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Deprecation Notice

The `sparkdl.xgboost` module has been deprecated since Databricks Runtime 12.0 ML. Databricks recommends migrating code to use the `xgboost.spark` module instead. See the XGBoost Spark Migration Guide for details. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [XGBoost for PySpark Pipeline](/concepts/xgboostspark-module.md)
- [ML Pipelines](/concepts/mllib-pipelines-api.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- GPU Training on Databricks
- [Spark MLlib](/concepts/apache-spark-mllib.md)

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
