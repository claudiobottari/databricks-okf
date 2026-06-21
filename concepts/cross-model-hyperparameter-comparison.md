---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82d6fb0b12004a39645bc21cc6e5ea342adbc413987ddd09f0ba3cf047ec26ee
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-model-hyperparameter-comparison
    - CHC
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: Cross-model hyperparameter comparison
description: Technique of tuning hyperparameters for multiple model types (e.g., different scikit-learn models) in parallel to select the best overall model
tags:
  - model-selection
  - hyperparameter-tuning
  - machine-learning
timestamp: "2026-06-19T14:19:57.613Z"
---

# Cross-model hyperparameter comparison

**Cross-model hyperparameter comparison** is a technique for comparing multiple distinct model types (e.g., linear regression, random forest, gradient boosting) by tuning each with its own set of hyperparameters and selecting the best overall model. This approach moves beyond simple model selection on default parameters, allowing practitioners to fairly evaluate the performance ceiling of each architecture.

## Overview

When building a machine learning solution, choosing the right model architecture is as important as finding the right hyperparameters. A naïve comparison using default parameters may unfairly disadvantage models that benefit from careful tuning. Cross-model hyperparameter comparison addresses this by performing a separate hyperparameter optimization for each candidate model type, then comparing the best-found configurations on a consistent evaluation metric. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

The process involves:
1. Defining a list of candidate model types (e.g., from scikit‑learn or other libraries).
2. For each model type, specifying a search space of hyperparameters that are appropriate for that architecture.
3. Running a hyperparameter optimization (e.g., with [Hyperopt](/concepts/hyperopt.md) or [Optuna](/concepts/optuna.md)) to find the best configuration for each model type.
4. Comparing the best models across all types using the same validation or test metric.
5. Selecting the best overall model and registering it for production.

This methodology is demonstrated in a Databricks notebook that uses Hyperopt with `SparkTrials` to compare three model types, evaluating performance with hyperparameters specific to each model type. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Recommended Tools

### Hyperopt (legacy)

The classic implementation, `hyperopt`, combined with `SparkTrials` for distributed tuning, is the approach shown in the Databricks example. However, the open‑source version of Hyperopt is no longer maintained. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### Optuna and Ray Tune

Databricks recommends using [Optuna](/concepts/optuna.md) for single‑node optimization or [Ray Tune](/concepts/ray-tune.md) for distributed hyperparameter tuning. Ray Tune provides a similar experience to the deprecated Hyperopt distributed functionality. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

| Tool | Recommended for |
|------|----------------|
| Optuna | Single‑node hyperparameter optimization |
| Ray Tune | Distributed hyperparameter tuning; similar to deprecated Hyperopt |

## Best Practices

- **Per‑model search spaces**: Each model type should have a search space that reflects its own hyperparameter sensitivities. For example, a random forest’s `n_estimators` and `max_depth` would be tuned, while a logistic regression would tune `C` and penalty type.
- **Consistent evaluation metric**: Use the same metric (e.g., F1 score, RMSE, log loss) across all model types to enable fair comparison.
- **Fair resource budget**: Allocate similar computational budgets (number of trials, number of Spark workers) to each model type to avoid under‑tuning any candidate.
- **Tracking with MLflow**: Log all hyperparameters and results to [MLflow](/concepts/mlflow.md) to enable reproducibility and easy retrieval of the best-performing configuration.

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – The general practice of optimizing model hyperparameters.
- [Model selection](/concepts/custom-judge-model-selection.md) – The broader task of choosing the best algorithm and configuration.
- [Optuna](/concepts/optuna.md) – A modern hyperparameter optimization framework.
- [Ray Tune](/concepts/ray-tune.md) – A distributed hyperparameter tuning library.
- [SparkTrials](/concepts/sparktrials.md) – Hyperopt’s distributed execution engine on Apache Spark.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry used to record cross-model comparisons.

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
