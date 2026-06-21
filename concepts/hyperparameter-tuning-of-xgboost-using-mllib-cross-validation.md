---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 534a147028405b08795cf797cba90852a2665a58e2d3685294a730759d6f72d7
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperparameter-tuning-of-xgboost-using-mllib-cross-validation
    - HTOXUMC
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: Hyperparameter Tuning of XGBoost using MLlib Cross-Validation
description: Using Spark MLlib's cross-validation framework to tune XGBoost model hyperparameters at scale
tags:
  - xgboost
  - mllib
  - cross-validation
  - hyperparameter-tuning
timestamp: "2026-06-19T18:35:31.474Z"
---

# Hyperparameter Tuning of XGBoost using MLlib Cross-Validation

**Hyperparameter Tuning of XGBoost using MLlib Cross-Validation** refers to the technique of leveraging Apache Spark's MLlib cross-validation utilities to search for optimal hyperparameters of an XGBoost model. This approach is demonstrated in a Databricks example notebook that shows how to perform such tuning as part of distributed XGBoost training using Scala. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Overview

The example notebook is one of two provided in the Databricks documentation for distributed training of XGBoost models using Scala. The first notebook demonstrates embedding an XGBoost model into an MLlib ML pipeline, while the second notebook specifically focuses on using MLlib cross-validation to tune an XGBoost model. The second notebook is titled **"XGBoost regression with cross-validation notebook"**, indicating that the tuning is applied to a regression task. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Workflow

The general workflow for hyperparameter tuning with MLlib cross-validation involves:

1. Defining an XGBoost estimator (e.g., `XGBoostRegressor` or `XGBoostClassifier`).
2. Specifying a grid of hyperparameters to search over.
3. Setting up a cross-validator from `org.apache.spark.ml.tuning.CrossValidator` with a chosen evaluator (such as `RegressionEvaluator` for regression tasks).
4. Fitting the cross-validator on the training data, which automatically performs k-fold cross-validation for each parameter combination.
5. Selecting the best model based on the evaluation metric.

While the source material does not provide the full notebook code, the documented example illustrates this pattern within a Databricks environment using Scala. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Benefits

Using MLlib cross-validation for XGBoost hyperparameter tuning provides built-in parallelism across Spark executors, making the search process scalable for large datasets. It also integrates cleanly with MLlib pipelines, enabling seamless transition from data preprocessing to model selection and evaluation. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) – A gradient-boosted tree algorithm widely used for supervised learning.
- MLlib – Apache Spark’s scalable machine learning library.
- Cross-validation – A resampling method for evaluating model performance and tuning hyperparameters.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – The process of searching for the best set of model configuration parameters.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The Databricks runtime environment that includes pre-installed XGBoost and Spark ML libraries.
- Scala – The programming language used in the example notebooks.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
