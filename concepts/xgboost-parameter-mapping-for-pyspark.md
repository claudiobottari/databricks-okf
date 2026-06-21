---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a58dbd9a60955215d96ed8b8f756e7b8e23eba1911106d43f87676e483dd24a2
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboost-parameter-mapping-for-pyspark
    - XPMFP
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: XGBoost Parameter Mapping for PySpark
description: Parameter differences between the standard xgboost package and sparkdl.xgboost, including unsupported parameters and alternative column-based parameters like weightCol, validationIndicatorCol, and baseMarginCol.
tags:
  - parameter-mapping
  - xgboost
  - pyspark
  - migration
timestamp: "2026-06-18T15:32:40.869Z"
---

# XGBoost Parameter Mapping for PySpark

**XGBoost Parameter Mapping for PySpark** describes how the native Python `xgboost` package parameters map to the PySpark estimators `XgboostRegressor` and `XgboostClassifier` in the `sparkdl.xgboost` module, as well as their supported and unsupported counterparts in the Spark distributed training environment.

## Overview

Databricks Runtime ML provides PySpark estimators based on the Python `xgboost` package: `sparkdl.xgboost.XgboostRegressor` and `sparkdl.xgboost.XgboostClassifier`. These estimators enable XGBoost training within ML pipelines and support distributed training via the `num_workers` parameter. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

> **Deprecation notice**: The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks recommends migrating to the `xgboost.spark` module instead. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Parameter Mapping

### Unsupported Parameters

The following parameters from the native `xgboost` package are **not supported** in `sparkdl.xgboost` estimators: ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

| Native Parameter | Status | Replacement |
|------------------|--------|-------------|
| `gpu_id` | Not supported | Use `use_gpu=True` instead |
| `output_margin` | Not supported | — |
| `validate_features` | Not supported | — |
| `sample_weight` | Not supported | Use `weightCol` instead |
| `eval_set` | Not supported | Use `validationIndicatorCol` instead |
| `sample_weight_eval_set` | Not supported | Use `validationIndicatorCol` instead |
| `base_margin` | Not supported | Use `baseMarginCol` instead |
| `base_margin_eval_set` | Not supported | Use `baseMarginCol` instead |

### Missing Value Semantics

The `missing` parameter has **different semantics** between native `xgboost` and `sparkdl.xgboost`. In native `xgboost`, zero values in a SciPy sparse matrix are always treated as missing values regardless of the `missing` parameter value. In `sparkdl.xgboost`, zero values in a Spark sparse vector are **not** treated as missing values unless you explicitly set `missing=0`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

If you have a sparse training dataset where most feature values are missing, Databricks recommends setting `missing=0` to reduce memory consumption and achieve better performance. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### Parameter Substitutions

| Spark Parameter | Purpose | Native Replacement |
|-----------------|---------|-------------------|
| `weightCol` | Sample weights | `sample_weight`, `sample_weight_eval_set` |
| `validationIndicatorCol` | Validation set specification | `eval_set`, `sample_weight_eval_set` |
| `baseMarginCol` | Base margin values | `base_margin`, `base_margin_eval_set` |

## Distributed Training Parameters

To use distributed training, set the `num_workers` parameter to a value less than or equal to the total number of Spark task slots on your cluster. To use all Spark task slots, set `num_workers=sc.defaultParallelism`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=sc.defaultParallelism)
regressor = XgboostRegressor(num_workers=sc.defaultParallelism)
```

## GPU Training Parameters

Databricks Runtime 9.1 LTS ML and above support GPU clusters for XGBoost training. To use a GPU cluster, set `use_gpu=True`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

```python
classifier = XgboostClassifier(num_workers=N, use_gpu=True)
regressor = XgboostRegressor(num_workers=N, use_gpu=True)
```

> **Note**: Databricks Runtime 11.3 LTS ML includes XGBoost 1.6.1, which does not support GPU clusters with compute capability 5.2 and below. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Limitations

- `mlflow.xgboost.autolog` is incompatible with distributed XGBoost.
- `baseMarginCol` cannot be used with distributed XGBoost.
- Distributed XGBoost does not work on clusters with autoscaling enabled. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Version Requirements

Databricks strongly recommends using Databricks Runtime 11.3 LTS ML or above for `sparkdl.xgboost`. Previous versions are affected by bugs in older versions of `sparkdl.xgboost`. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [XGBoost for Spark Pipeline](/concepts/xgboost-with-mllib-ml-pipeline.md) — Extended documentation on the `sparkdl.xgboost` module
- [xgboost.spark](/concepts/xgboostspark-module.md) — The recommended replacement module (migration target)
- [Distributed XGBoost Training](/concepts/distributed-xgboost-training-on-databricks.md) — Multi-node training considerations and limitations
- GPU Training on Databricks — GPU cluster configuration for XGBoost
- NCCL Troubleshooting — Resolving NCCL communication errors in multi-node GPU training

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
