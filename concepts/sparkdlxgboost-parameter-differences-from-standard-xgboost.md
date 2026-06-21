---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88d6ad8e5360eb4f13deab2785631b2bb767c9c926c480bd05b1c55bfcf8f124
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparkdlxgboost-parameter-differences-from-standard-xgboost
    - SPDFSX
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: sparkdl.xgboost Parameter Differences from Standard xgboost
description: Key parameter discrepancies between sparkdl.xgboost and the standard xgboost package, including missing, baseMarginCol, weightCol, and validationIndicatorCol.
tags:
  - parameters
  - xgboost
  - sparkdl
  - compatibility
timestamp: "2026-06-18T12:05:38.422Z"
---

# sparkdl.xgboost Parameter Differences from Standard xgboost

The `sparkdl.xgboost` module provides PySpark estimators (`XgboostRegressor` and `XgboostClassifier`) based on the Python `xgboost` package, but several parameters differ in name, semantics, or availability compared to the standard `xgboost` API. These differences affect how you configure training, handle missing values, and manage evaluation data. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Unsupported Parameters

The following parameters from the standard `xgboost` package are **not supported** in `sparkdl.xgboost`: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

| Unsupported Parameter | Notes |
|-----------------------|-------|
| `gpu_id` | Not supported |
| `output_margin` | Not supported |
| `validate_features` | Not supported |
| `sample_weight` | Use `weightCol` instead |
| `eval_set` | Use `validationIndicatorCol` instead |
| `sample_weight_eval_set` | Use `validationIndicatorCol` instead |
| `base_margin` | Use `baseMarginCol` instead |
| `base_margin_eval_set` | Use `baseMarginCol` instead |

## Parameter Mapping

### Sample Weight and Evaluation Sets

Instead of `sample_weight`, `eval_set`, and `sample_weight_eval_set`, use the following Spark DataFrame column-based parameters: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

- **`weightCol`** — Specifies a column in the training DataFrame containing sample weights. Replaces `sample_weight`.
- **`validationIndicatorCol`** — Specifies a column that indicates which rows belong to the evaluation set. Replaces both `eval_set` and `sample_weight_eval_set`.

### Base Margin

Instead of `base_margin` and `base_margin_eval_set`, use the **`baseMarginCol`** parameter, which specifies a column in the DataFrame containing the base margin values. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Missing Value Semantics

The `missing` parameter has **different semantics** in `sparkdl.xgboost` compared to the standard `xgboost` package: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

- In standard `xgboost`, zero values in a SciPy sparse matrix are treated as missing values **regardless** of the value of `missing`.
- In `sparkdl.xgboost`, zero values in a Spark sparse vector are **not** treated as missing values unless you explicitly set `missing=0`.

If you have a sparse training dataset where most feature values are missing, Databricks recommends setting `missing=0` to reduce memory consumption and achieve better performance. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Distributed Training Parameters

### num_workers

The `num_workers` parameter enables distributed XGBoost training. Set it to a value less than or equal to the total number of Spark task slots on your cluster. To use all Spark task slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=sc.defaultParallelism)
regressor = XgboostRegressor(num_workers=sc.defaultParallelism)
```

### Limitations with Distributed Training

When using distributed training with `num_workers`, the following limitations apply: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

- You **cannot** use `mlflow.xgboost.autolog` with distributed XGBoost.
- You **cannot** use `baseMarginCol` with distributed XGBoost.
- You **cannot** use distributed XGBoost on a cluster with autoscaling enabled.

## GPU Training Parameter

### use_gpu

To enable GPU training, set `use_gpu=True`. This parameter is available in Databricks Runtime 9.1 LTS ML and above. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=N, use_gpu=True)
regressor = XgboostRegressor(num_workers=N, use_gpu=True)
```

Note that Databricks Runtime 11.3 LTS ML includes XGBoost 1.6.1, which does not support GPU clusters with compute capability 5.2 and below. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Deprecation Notice

The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks recommends migrating code to use the `xgboost.spark` module instead. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [XGBoost for PySpark Pipeline](/concepts/xgboostspark-module.md) — The official documentation for `sparkdl.xgboost` estimators
- [xgboost.spark Module](/concepts/xgboostspark-module.md) — The recommended replacement for `sparkdl.xgboost`
- [Distributed XGBoost Training](/concepts/distributed-xgboost-training-on-databricks.md) — Using `num_workers` for multi-node training
- [GPU Training with XGBoost](/concepts/gpu-training-with-xgboostspark.md) — Using `use_gpu` for GPU-accelerated training
- MLflow XGBoost Autologging — Note: not compatible with distributed training

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
