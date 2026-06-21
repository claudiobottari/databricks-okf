---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 96913fc282ef3890a63128d938aaf2ab46d6826d6595c183e0651f78b9fa8d03
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mllib-cross-validation-for-xgboost-hyperparameter-tuning
    - MCFXHT
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: MLlib Cross-Validation for XGBoost Hyperparameter Tuning
description: Using Spark MLlib's cross-validation functionality to tune XGBoost model hyperparameters
tags:
  - machine-learning
  - xgboost
  - hyperparameter-tuning
  - spark-mllib
timestamp: "2026-06-19T10:17:00.898Z"
---

#MLlib Cross-Validation for XGBoost Hyperparameter Tuning

**MLlib Cross-Validation for XGBoost Hyperparameter Tuning** refers to the practice of using Apache Spark's MLlib cross-validation functionality to tune the hyperparameters of an [XGBoost](/concepts/xgboostspark-module.md) model within a [Spark ML Pipeline](/concepts/mllib-pipelines-api.md). This approach combines the distributed computing capabilities of Spark with the gradient boosting power of XGBoost, enabling scalable hyperparameter optimization on large datasets.

## Overview

MLlib provides built-in cross-validation tools that can be applied to any Estimator in a Spark ML pipeline, including XGBoost estimators. By wrapping an XGBoost model inside an MLlib pipeline, users can leverage standard cross-validation to search over a grid of hyperparameters (e.g., `maxDepth`, `eta`, `nrounds`) and select the best performing configuration based on a chosen evaluation metric. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## How It Works

1. **Embed XGBoost in a Pipeline**: The XGBoost classifier or regressor is included as a stage in an ML Pipeline, often alongside feature transformers (e.g., VectorAssembler).

2. **Define a Parameter Grid**: A `ParamGridBuilder` is used to specify the hyperparameters to search over (e.g., `maxDepth`, `learningRate`).

3. **Set Up Cross-Validator**: An `CrossValidator` object is created with the pipeline estimator, the parameter grid, and an evaluator (such as `BinaryClassificationEvaluator` or `RegressionEvaluator`). The number of folds (e.g., 3 or 5) is set.

4. **Fit and Tune**: The cross-validator is fitted to the training data. MLlib trains the XGBoost model on each fold's training partition and evaluates on the validation partition. The combination of hyperparameters that yields the best average metric is selected.

5. **Apply Best Model**: The fitted cross-validator returns a model that uses the optimal hyperparameters. This model can then be used for predictions on test data or deployed for inference.

## Example Notebooks

The Databricks documentation provides two example notebooks: ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

- **XGBoost classification with ML pipeline notebook** – Demonstrates embedding an XGBoost classifier into an MLlib pipeline.
- **XGBoost regression with cross-validation notebook** – Shows how to use MLlib cross-validation specifically for tuning an XGBoost regression model.

These notebooks, written in Scala, illustrate the full workflow from data preparation to model evaluation.

## Benefits

- **Scalability**: Cross-validation runs in parallel across Spark executors, making it feasible to tune models on large datasets.
- **Integration**: Seamlessly works with other MLlib components (pipelines, feature transformers, evaluators).
- **Reproducibility**: Uses Spark's deterministic random seed for fold splits, ensuring consistent results.

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – The broader practice of optimizing model parameters.
- [Cross-Validation](/concepts/crossvalidator.md) – The statistical method used to evaluate model generalization.
- [Spark ML Pipeline](/concepts/mllib-pipelines-api.md) – The unifying API for assembling ML workflows.
- XGBoost on Databricks – General guidance for using XGBoost in the Databricks environment.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-configured runtime that includes XGBoost and Spark MLlib.
- Model Training Examples – Other training examples available in Databricks.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
