---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 273c43e35a1a10ab778b5fba198aa901b3f9229a9025507133649d7ae138d792
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - xgboost-on-databricks-runtime-ml
    - XODRM
    - Use XGBoost on Databricks
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: XGBoost on Databricks Runtime ML
description: Using XGBoost within Databricks Runtime ML which includes pre-installed ML libraries and optimizations
tags:
  - machine-learning
  - xgboost
  - databricks
  - runtime-ml
timestamp: "2026-06-19T10:17:01.702Z"
---

# XGBoost on Databricks Runtime ML

**XGBoost on Databricks Runtime ML** refers to the support and usage of the [XGBoost](https://xgboost.readthedocs.io/) library within the [Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml). Databricks provides example notebooks that demonstrate distributed training of XGBoost models using **Scala** and integration with [MLlib](https://spark.apache.org/mllib/), Spark’s machine learning library.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Distributed Training with Scala

The primary mechanism for distributed XGBoost training on Databricks is through the Scala API, which allows XGBoost models to be embedded into [MLlib ML pipelines](https://spark.apache.org/docs/latest/ml-pipeline.html). This enables users to leverage Spark’s distributed computing framework for large-scale data processing alongside XGBoost’s gradient boosting algorithm.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

### XGBoost Classification with ML Pipeline

One example notebook shows how to embed an XGBoost classification model into an MLlib ML pipeline. This approach allows seamless integration of feature transformers, vector assemblers, and the XGBoost classifier into a single pipeline that can be fit, evaluated, and persisted.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

### XGBoost Regression with Cross-Validation

A second example notebook demonstrates how to use MLlib’s cross-validation utilities to tune hyperparameters for an XGBoost regression model. The cross-validation process selects optimal parameters (e.g., learning rate, max depth, number of estimators) by evaluating the model on multiple folds of the training data, all within a distributed Spark environment.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related Concepts

- MLlib – Apache Spark’s machine learning library for distributed training.
- [XGBoost](/concepts/xgboostspark-module.md) – The underlying gradient boosting framework.
- [ML Pipelines](/concepts/mllib-pipelines-api.md) – The concept of chaining transformers and estimators in Spark ML.
- [Cross-Validation in Spark ML](/concepts/crossvalidator.md) – Using `CrossValidator` for hyperparameter tuning.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The pre-configured runtime environment that includes XGBoost and related dependencies.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
