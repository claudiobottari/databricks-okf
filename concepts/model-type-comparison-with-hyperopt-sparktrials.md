---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c34d059852cfa3ef963d75e019ed2c23937ecd518c06b9524044b2c9483b06de
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-type-comparison-with-hyperopt-sparktrials
    - MTCWHS
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: Model type comparison with Hyperopt SparkTrials
description: Using Hyperopt with SparkTrials to tune hyperparameters for and compare multiple model types to select the best overall model
tags:
  - databricks
  - hyperparameter-tuning
  - spark
  - model-selection
timestamp: "2026-06-19T17:48:40.462Z"
---

# Model type comparison with Hyperopt SparkTrials

**Model type comparison with Hyperopt SparkTrials** is a technique for tuning hyperparameters across multiple model types simultaneously using the [Hyperopt](/concepts/hyperopt.md) library's `SparkTrials` class on Databricks. This approach allows data scientists to compare different model families—each with its own appropriate set of hyperparameters—in a single optimization run and select the best overall model. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Overview

When building a machine learning pipeline, it is often unclear which model type will perform best for a given dataset. Traditional approaches require training each model type separately with its own hyperparameter search, then comparing results. With Hyperopt `SparkTrials`, you can define multiple search spaces—one for each model type—and let Hyperopt evaluate them in parallel across a Spark cluster, selecting the configuration that yields the best performance metric. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## How it works

1. **Define model-specific search spaces**: Create a dictionary or list of hyperparameter configurations where each top-level key corresponds to a model type (e.g., `'random_forest'`, `'xgboost'`, `'linear_regression'`). The values are the hyperparameter domains for that model. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]
2. **Create an evaluation function**: Write a function that accepts a hyperparameter configuration, instantiates the corresponding model, trains it, and returns a loss value (e.g., negative accuracy, RMSE). The function must return the loss and a status dictionary. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]
3. **Use `SparkTrials`**: Pass the search space and evaluation function to `fmin()` with `algo=hyperopt.tpe.suggest` and `trials=SparkTrials()`. `SparkTrials` distributes evaluations across worker nodes in the cluster. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]
4. **Log results with [MLflow](/concepts/mlflow.md)**: Inside the evaluation function, use `mlflow.log_param()` and `mlflow.log_metric()` to record hyperparameters and performance metrics. This enables comparison of all trials in the [MLflow UI](/concepts/mlflow.md). ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Benefits

- **Parallelized search**: `SparkTrials` evaluates many hyperparameter combinations concurrently, significantly speeding up the model selection process compared to sequential tuning. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]
- **Fair comparison**: All model types are evaluated under the same computational budget and using the same loss metric, providing an unbiased basis for model selection. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]
- **Unified tracking**: Every trial is logged to a single MLflow experiment, making it easy to inspect performance across model types and hyperparameter choices. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Limitations and migration note

The open-source version of **Hyperopt** is no longer being maintained. Starting with [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) 16.4 LTS ML, Hyperopt is not included. For single-node optimization, Databricks recommends using [Optuna](/concepts/optuna.md). For distributed hyperparameter tuning with a similar experience to the deprecated Hyperopt `SparkTrials` functionality, Databricks recommends using [RayTune](/concepts/raytune.md) on Ray. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) – The hyperparameter optimization library.
- [SparkTrials](/concepts/sparktrials.md) – The `Trials` subclass that distributes evaluations across a Spark cluster.
- [Optuna](/concepts/optuna.md) – Alternative single-node optimization library.
- [RayTune](/concepts/raytune.md) – Alternative distributed tuning library.
- [MLflow](/concepts/mlflow.md) – Tracking and logging platform for machine learning experiments.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – General process of searching for optimal model hyperparameters.
- [Model selection](/concepts/custom-judge-model-selection.md) – The task of choosing the best model family for a given problem.

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
