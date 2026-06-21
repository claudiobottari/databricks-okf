---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2cfb31a9d0907bb4e553bb95f9dc24ed7f5dbca801a0329b4149189407391a8b
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-for-hyperparameter-tuning
    - MIFHT
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: MLflow integration for hyperparameter tuning
description: The practice of using MLflow to track and compare hyperparameter tuning runs across different model types, enabling systematic model selection and experiment tracking.
tags:
  - machine-learning
  - mlflow
  - experiment-tracking
  - databricks
timestamp: "2026-06-18T14:40:43.431Z"
---

## MLflow Integration for Hyperparameter Tuning

The **MLflow integration for hyperparameter tuning** refers to the use of MLflow to track and compare hyperparameter optimization experiments — such as those performed with [Hyperopt](/concepts/hyperopt.md), [Optuna](/concepts/optuna.md), or [RayTune](/concepts/raytune.md) — enabling systematic model selection and reproducibility.

### Overview

On Databricks, hyperparameter tuning workflows have historically used [Hyperopt](/concepts/hyperopt.md) with [SparkTrials](/concepts/sparktrials.md) to search over a parameter space across multiple model types, logging results to [MLflow experiments](/concepts/mlflow-experiment.md). The end-to-end process includes tuning hyperparameters for several model architectures and selecting the best overall model by comparing the logged metrics. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### Usage with Hyperopt

The notebook *Compare models using scikit-learn, Hyperopt, and MLflow* demonstrates how to tune the hyperparameters for multiple models and arrive at a best model overall. It uses Hyperopt with `SparkTrials` to compare three model types, evaluating model performance with a different set of hyperparameters appropriate for each model type. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### Deprecation and Alternative Tools

Hyperopt is no longer maintained and is not included in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) starting with version 16.4 LTS ML. Databricks recommends using the following alternatives for hyperparameter tuning: ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

- [Optuna](/concepts/optuna.md) — for single-node optimization.
- [RayTune](/concepts/raytune.md) — for a similar distributed experience to Hyperopt with SparkTrials.

For guidance on using RayTune with MLflow on Databricks, see the documentation on [RayTune](/concepts/raytune.md) integration. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### Related Concepts

- [Hyperopt](/concepts/hyperopt.md) — The open-source library for hyperparameter optimization (no longer maintained).
- [Optuna](/concepts/optuna.md) — Recommended alternative for single-node tuning.
- [RayTune](/concepts/raytune.md) — Recommended alternative for distributed tuning.
- [SparkTrials](/concepts/sparktrials.md) — Distributed backend for Hyperopt on Spark.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for tracking tuning runs.
- Model Selection — The broader practice of comparing and choosing the best model.

### Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
