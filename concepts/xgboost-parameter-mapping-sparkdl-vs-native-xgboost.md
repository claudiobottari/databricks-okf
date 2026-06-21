---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c9d73cda80f0dcaeef98c9bd6f60a721d8f0b1a88a4f369b6c76a3cf57fc4efe
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboost-parameter-mapping-sparkdl-vs-native-xgboost
    - XPMSVNX
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: "XGBoost Parameter Mapping: sparkdl vs Native xgboost"
description: The mapping and semantic differences between sparkdl.xgboost parameters and native Python xgboost package parameters, including missing, weightCol, baseMarginCol, and unsupported parameters like gpu_id and output_margin.
tags:
  - machine-learning
  - api-reference
  - xgboost
  - spark
timestamp: "2026-06-19T10:17:29.658Z"
---

# XGBoost Parameter Mapping: sparkdl vs Native xgboost

**XGBoost Parameter Mapping: sparkdl vs Native xgboost** documents the differences in parameter names, semantics, and support between the `sparkdl.xgboost` module (deprecated since Databricks Runtime 12.0 ML) and the native Python `xgboost` package. Understanding these mappings is essential for migrating or troubleshooting code that uses the `sparkdl.xgboost` estimators (`XgboostRegressor`, `XgboostClassifier`). ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Unsupported Native Parameters

The following native `xgboost` parameters are **not supported** in `sparkdl.xgboost`:

| Native parameter    | Status in sparkdl.xgboost |
|---------------------|---------------------------|
| `gpu_id`            | Not supported             |
| `output_margin`     | Not supported             |
| `validate_features` | Not supported             |

^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Parameter Replacement Mapping

Several native parameters must be replaced with Spark DataFrame column–based equivalents when using `sparkdl.xgboost`:

| Native parameter                 | sparkdl equivalent | Notes |
|----------------------------------|--------------------|-------|
| `sample_weight`                  | `weightCol`        | Specify a column name in the DataFrame containing instance weights. |
| `eval_set`                       | `validationIndicatorCol` | Use a boolean column that indicates which rows belong to the validation set. |
| `sample_weight_eval_set`         | Not directly supported; use `validationIndicatorCol` with `weightCol` | Combine the weight column and validation indicator column. |
| `base_margin` / `base_margin_eval_set` | `baseMarginCol` | Provide a column name for base margin values. **Note:** `baseMarginCol` cannot be used with distributed training. |
| `missing` (semantics differ)     | `missing` (with different semantics) | See "Different Semantics for `missing`" section below. |

^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Different Semantics for `missing`

The `missing` parameter behaves differently between native `xgboost` and `sparkdl.xgboost`:

- **Native `xgboost`**: In a SciPy sparse matrix, zero values are **always treated as missing** regardless of the value of `missing`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- **`sparkdl.xgboost`**: Zero values in a Spark sparse vector are **not treated as missing** unless you explicitly set `missing=0`. If the training dataset is sparse (most feature values are missing), Databricks recommends setting `missing=0` to reduce memory consumption and achieve better performance. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Distributed Training Limitations Affecting Parameters

When using distributed XGBoost training (`num_workers > 1`), the following caveats apply:

- **`mlflow.xgboost.autolog`** cannot be used with distributed XGBoost. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- **`baseMarginCol`** cannot be used with distributed XGBoost. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]
- Distributed training is not supported on clusters with autoscaling enabled. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Migration Guidance

Since `sparkdl.xgboost` is deprecated since Databricks Runtime 12.0 ML, Databricks recommends migrating to the `xgboost.spark` module. The migration guide provides a step-by-step process. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [Distributed XGBoost Training on Databricks](/concepts/distributed-xgboost-training-on-databricks.md) – Best practices for multi-node XGBoost.
- [sparkdl.xgboost Module](/concepts/sparkdlxgboost-module.md) – Legacy PySpark estimator for XGBoost.
- [xgboost.spark Module](/concepts/xgboostspark-module.md) – The recommended replacement for sparkdl.xgboost.
- MLflow xgboost autolog – Limitations with distributed training.
- [NCCL Socket Configuration for XGBoost](/concepts/nccl-socket-configuration-for-xgboost.md) – Troubleshooting GPU communication.

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
