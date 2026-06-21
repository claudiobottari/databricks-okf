---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9480831983e11feac66e27ead5b9e3365932e03f4e054011a16baf22f2217a95
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboost-classification-and-regression-on-databricks
    - regression on Databricks and XGBoost classification
    - XCAROD
    - Classification and Regression AutoML
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: XGBoost classification and regression on Databricks
description: Using XGBoost for both classification (with ML pipeline) and regression (with cross-validation) tasks in Scala notebooks on Databricks.
tags:
  - xgboost
  - classification
  - regression
  - databricks
timestamp: "2026-06-18T15:31:53.007Z"
---

# XGBoost Classification and Regression on Databricks

**XGBoost classification and regression on Databricks** refers to the use of the XGBoost gradient boosting library within the Databricks platform for supervised learning tasks. Databricks provides example notebooks that demonstrate how to train XGBoost models for classification and regression using Scala and integrate them with MLlib pipelines. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Classification with ML Pipeline

The classification example shows how to embed an XGBoost model into an [MLlib ML Pipeline](/concepts/mllib-pipelines-api.md). This approach allows you to chain feature transformers, an XGBoost classifier, and other stages into a single pipeline for reproducible training and inference. The notebook demonstrates the full workflow from data preparation to model evaluation. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Regression with Cross-Validation

The regression example demonstrates using MLlib [cross-validation](/concepts/crossvalidator.md) to tune an XGBoost model. By searching over a grid of hyperparameters (e.g., learning rate, max depth), the notebook shows how to select the best-performing XGBoost regressor using [Train-Validation Split](/concepts/trainvalidationsplit.md) or k-fold cross-validation. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Distributed Training in Scala

Both examples are written in Scala and leverage [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md), which includes pre-installed XGBoost libraries. The notebooks show how to train XGBoost models in a distributed fashion across a cluster using [Spark DataFrames](/concepts/saving-spark-dataframes-to-tfrecords.md) as input, enabling scaling to large datasets. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

For a broader overview of XGBoost on Databricks, refer to the [Use XGBoost on Databricks](/concepts/xgboost-on-databricks-runtime-ml.md) guide. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
