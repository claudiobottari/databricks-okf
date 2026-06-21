---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6c28b18c8452f731d65da82b29187b5d5ce3404326f3f610e921edd92f5df16
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-for-xgboost
    - DRMFX
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: Databricks Runtime ML for XGBoost
description: The pre-configured Databricks Runtime ML environment that includes XGBoost libraries and dependencies for Scala-based training.
tags:
  - databricks
  - runtime-ml
  - xgboost
timestamp: "2026-06-18T15:31:50.792Z"
---

# Databricks Runtime ML for XGBoost

**Databricks Runtime ML for XGBoost** provides built-in support for training and tuning [XGBoost](/concepts/xgboostspark-module.md) models at scale within the Databricks environment. The runtime integrates XGBoost with [Apache Spark MLlib](/concepts/apache-spark-mllib.md), allowing users to embed XGBoost into standard ML pipelines and perform distributed cross-validation. The primary examples are provided in Scala, demonstrating the tight coupling between Databricks Runtime ML and Spark's native APIs. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Integration with MLlib

Databricks Runtime ML ships with XGBoost compiled for Spark, enabling users to use XGBoost classifiers and regressors as estimators in MLlib pipelines. This integration means that all standard MLlib features—such as pipeline stages, parameter grids, and evaluators—work seamlessly with XGBoost models. Users can apply MLlib's cross-validation functionality to tune XGBoost hyperparameters across a distributed cluster, with no additional configuration required. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Example Notebooks

The official documentation includes two example notebooks that illustrate these capabilities:

- **XGBoost classification with ML pipeline** – Shows how to embed an XGBoost classifier into an MLlib ML Pipeline, chaining it with feature transformers and evaluators. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
- **XGBoost regression with cross-validation** – Demonstrates how to use MLlib's [CrossValidator](/concepts/crossvalidator.md) to tune an XGBoost regression model, specifying a parameter grid and a validation metric. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

Both notebooks are written in Scala and are designed to run on Databricks clusters that have Databricks Runtime ML installed. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The pre-configured runtime that includes XGBoost and other deep learning libraries.
- XGBoost on Databricks – General guidance for using XGBoost across languages (Python, R, Scala).
- MLlib – Spark's distributed machine learning library that provides pipeline and cross-validation APIs.
- Cross-validation – Technique for hyperparameter tuning supported directly with XGBoost in MLlib.
- Scala on Databricks – How Scala notebooks and libraries work within the platform.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
