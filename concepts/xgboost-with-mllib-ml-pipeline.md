---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36da51f1c5ef57aa525a4320397a5d2940332c7f749c7e320c953f986b9d3b59
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboost-with-mllib-ml-pipeline
    - XWMMP
    - XGBoost for Spark Pipeline
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: XGBoost with MLlib ML Pipeline
description: Embedding XGBoost models into Apache Spark MLlib ML pipelines for distributed training
tags:
  - machine-learning
  - xgboost
  - spark-mllib
  - databricks
timestamp: "2026-06-19T10:16:57.884Z"
---

# XGBoost with MLlib ML Pipeline

**XGBoost with MLlib ML Pipeline** refers to the integration of [XGBoost](/concepts/xgboostspark-module.md) models within the MLlib ML Pipeline framework on Databricks. This combination allows users to leverage the high-performance gradient boosting capabilities of XGBoost while benefiting from the structured pipeline workflow, feature transformers, and evaluation utilities provided by MLlib. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Embedding XGBoost into an ML Pipeline

The first of the example notebooks demonstrates how to embed an XGBoost model as a stage in an MLlib ML Pipeline. This enables seamless chaining of data preprocessing, feature engineering, and model training within a single [Pipeline](/concepts/mllib-pipelines-api.md) object. The model can then be used for both training and inference in a consistent manner. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Cross-Validation Tuning

The second example notebook shows how to use MLlib [CrossValidator](/concepts/crossvalidator.md) to tune hyperparameters of an XGBoost model. By integrating with MLlib's cross‑validation infrastructure, users can search over a grid of parameters – such as learning rate, max depth, or number of rounds – and select the best performing configuration using metrics like AUC or RMSE. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Implementation Notes

- Both examples are written in Scala and are designed to run on Databricks with [Databricks Runtime ML](/concepts/databricks-runtime-ml.md).
- The notebooks cover both classification and regression tasks.
- The source material does not detail the exact API calls; refer to the Databricks documentation for the complete notebook code.

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) – The gradient boosting library at the core of the integration.
- MLlib – Apache Spark's scalable machine learning library.
- ML Pipeline – The pipeline abstraction for composing data transformations and estimators.
- [CrossValidator](/concepts/crossvalidator.md) – MLlib's tool for hyperparameter tuning via cross-validation.
- Scala API in Databricks – Language support for Spark ML pipelines.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
