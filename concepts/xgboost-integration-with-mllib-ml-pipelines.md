---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3fa076c061ca620cdb3eaff0135e397d4b09a65492333e591e7509ba70d07b1f
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboost-integration-with-mllib-ml-pipelines
    - XIWMMP
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: XGBoost integration with MLlib ML pipelines
description: Embedding an XGBoost model as a stage within an MLlib Pipeline for end-to-end machine learning workflows on Databricks.
tags:
  - xgboost
  - mllib
  - pipeline
  - databricks
timestamp: "2026-06-18T15:31:47.658Z"
---

# XGBoost Integration with MLlib ML Pipelines

**XGBoost integration with MLlib ML pipelines** refers to the ability to embed [XGBoost](/concepts/xgboostspark-module.md) models into Apache Spark’s MLlib ML Pipeline framework using the Scala API on Databricks. This integration allows users to combine XGBoost’s high-performance gradient boosting with the standard pipeline stages (transformers, estimators, evaluators) provided by MLlib, enabling seamless preprocessing, training, and evaluation within a single pipeline.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Examples

The Databricks documentation provides two notebook examples demonstrating the integration:

1. **XGBoost classification with ML pipeline** – This notebook shows how to embed an XGBoost model as a stage in an MLlib ML pipeline, allowing features to be transformed and passed to the XGBoost classifier as part of a unified workflow.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

2. **XGBoost regression with cross‑validation** – This notebook demonstrates how to use MLlib’s cross‑validation tools (e.g., `CrossValidator`) to tune hyperparameters of an XGBoost regression model within an ML pipeline, leveraging built-in parameter grids and evaluation metrics.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

Both examples use the Scala API and are intended for use with [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md).

## Related Concepts

- ML Pipeline – The core abstraction for chaining data transformations and model training.
- Cross-validation – A technique for hyperparameter tuning, integrated with MLlib pipelines.
- [XGBoost](/concepts/xgboostspark-module.md) – The gradient boosting library used as the estimator in the pipeline.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The pre‑configured runtime that includes XGBoost and MLlib.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Leveraging Spark clusters for scalable model training.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
