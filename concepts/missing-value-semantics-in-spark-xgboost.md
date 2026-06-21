---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e732781e022670fb908d382a02ab3123cc6a3eab2c3cdf6f541db5940e4b619a
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing-value-semantics-in-spark-xgboost
    - MVSISX
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: Missing Value Semantics in Spark XGBoost
description: Difference in how the 'missing' parameter is handled in sparkdl.xgboost vs standard xgboost, particularly regarding sparse matrix zero values not being treated as missing by default.
tags:
  - xgboost
  - pyspark
  - data-processing
  - sparse-data
timestamp: "2026-06-18T15:32:25.954Z"
---

# Missing Value Semantics in Spark XGBoost

**Missing Value Semantics in Spark XGBoost** refers to the distinct behavior of how missing values are handled when using the `sparkdl.xgboost` module compared to the standard Python `xgboost` package. Understanding these differences is critical to avoid unexpected model behavior when training on sparse datasets.

## Overview

The `sparkdl.xgboost` module (deprecated since Databricks Runtime 12.0 ML) provides PySpark estimators based on the Python `xgboost` package. The `missing` parameter in this module has different semantics from the standard `xgboost` package, particularly regarding how zero values in sparse representations are treated. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Key Differences in `missing` Parameter Semantics

### Standard `xgboost` Package

In the standard Python `xgboost` package, zero values in a SciPy sparse matrix are **always treated as missing values**, regardless of the value specified for the `missing` parameter. This is a subtle but important default behavior that users familiar with standard XGBoost may expect. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### `sparkdl.xgboost` Module

For the PySpark estimators in the `sparkdl` package, zero values in a Spark sparse vector are **not treated as missing values** unless you explicitly set `missing=0`. This means that by default, Spark XGBoost will interpret zero-valued entries in sparse vectors as valid feature values rather than missing data. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Recommendation for Sparse Datasets

If you have a sparse training dataset where most feature values are missing, Databricks recommends setting `missing=0` when using the `sparkdl.xgboost` module. This configuration reduces memory consumption and achieves better performance by properly treating the zero-valued sparse entries as missing values. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Practical Implications

- **Inconsistent behavior**: Users migrating from standard XGBoost to Spark XGBoost must be aware that the same code may produce different results due to the differing missing value semantics.
- **Performance impact**: Failing to set `missing=0` on sparse datasets may lead to increased memory usage and degraded model performance, as XGBoost will attempt to learn from zero-valued features that should be treated as missing.
- **Migration to `xgboost.spark`**: Since `sparkdl.xgboost` is deprecated, users should refer to the [migration guide from sparkdl.xgboost to xgboost.spark](/concepts/migration-from-sparkdlxgboost-to-xgboostspark.md) for updated handling of missing values.

## Related Concepts

- XGBoost Parameter Configuration — Detailed documentation on the `missing` parameter and other XGBoost configuration options.
- Sparse Vectors in Spark MLlib — Understanding sparse vector representations and their implications for machine learning.
- sparkdl.xgboost Module Deprecation — Guidance on migrating from the deprecated `sparkdl.xgboost` module.
- [XGBoost Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) — General guidance for distributed XGBoost training.
- [GPU Training with XGBoost](/concepts/gpu-training-with-xgboostspark.md) — GPU-accelerated XGBoost training on Databricks.

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
