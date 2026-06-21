---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e33881e81f9ea1bc2633515443257fd6550146b74937133c01cdbf5a217f75fb
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboost-with-mllib-integration
    - XWMI
    - PySpark XGBoost integration
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: XGBoost with MLlib Integration
description: Using XGBoost models within Apache Spark MLlib pipelines for distributed training on Databricks
tags:
  - machine-learning
  - xgboost
  - spark-mllib
  - databricks
timestamp: "2026-06-18T12:04:38.300Z"
---

# XGBoost with MLlib Integration

**XGBoost with MLlib Integration** refers to the practice of using [XGBoost](/concepts/xgboostspark-module.md) models within [Apache Spark MLlib](/concepts/apache-spark-mllib.md) pipelines on Databricks. This integration enables distributed training and hyperparameter tuning of XGBoost models using familiar MLlib abstractions such as `Pipeline`, `CrossValidator`, and `ParamGridBuilder`. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Overview

Databricks provides example notebooks that demonstrate two primary integration patterns:

1. **Embedding an XGBoost model into an MLlib ML pipeline** – This pattern allows you to include XGBoost as one stage in a multi-stage pipeline that may include feature transformations, vector assembly, and other preprocessing steps. The pipeline can then be saved, loaded, and deployed as a single unit.

2. **Using MLlib cross-validation to tune an XGBoost model** – This pattern leverages `CrossValidator` and `ParamGridBuilder` from MLlib to perform grid search over XGBoost hyperparameters. The cross-validation process runs in a distributed manner across the Spark cluster, evaluating multiple parameter combinations in parallel.

Both examples are written in Scala and are designed for [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## XGBoost Classification with ML Pipeline

The first notebook demonstrates how to build a classification pipeline that includes an XGBoost classifier. Users define feature columns, apply any necessary transformers (e.g., `StringIndexer`, `VectorAssembler`), and set the XGBoost classifier as the final estimator. The pipeline can then be fitted to a training DataFrame using `fit()`, and the resulting `PipelineModel` can be used for predictions. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

### Key Steps

- Load and prepare training data.
- Configure an XGBoostClassifier (or `XGBoostRegressor` for regression).
- Assemble features using `VectorAssembler`.
- Chain all stages in a `Pipeline`.
- Train the pipeline with `.fit()`.
- Evaluate the model on test data. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## XGBoost Regression with Cross-Validation

The second notebook extends the integration by wrapping an XGBoost regressor inside an MLlib `CrossValidator`. A parameter grid is defined for hyperparameters such as `maxDepth`, `eta`, `numRound`, and others. The cross-validator splits the training data into folds, trains a model for each combination of parameters, and selects the best model based on a chosen evaluator (e.g., `RegressionEvaluator`). ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

### Key Steps

- Define an XGBoost regressor with initial parameters.
- Create a `ParamGridBuilder` with candidate hyperparameter values.
- Set up an `Evaluator` (e.g., `RegressionEvaluator` with `rmse` metric).
- Instantiate a `CrossValidator` with the estimator, evaluator, and parameter grid.
- Run the cross-validation using `.fit()`.
- Retrieve the best model from the `CrossValidatorModel`. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related Concepts

- ML Pipeline — The pipeline abstraction used to combine multiple stages.
- [CrossValidator](/concepts/crossvalidator.md) — MLlib’s tool for hyperparameter tuning via k-fold cross-validation.
- ParamGridBuilder — Utility for constructing a grid of hyperparameter values.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — How XGBoost leverages Spark for parallelized training.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime environment that includes optimized XGBoost and MLlib libraries.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
