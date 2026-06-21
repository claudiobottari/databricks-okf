---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04ee2b9ee308e0a6bf283089b6bc134c4b2501c84863dc68304484646ea35f5e
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - raytune
    - raytune-as-distributed-hyperopt-replacement-on-databricks
    - RADHROD
    - raytune-for-distributed-hyperparameter-tuning-on-databricks
    - RFDHTOD
    - Distributed Hyperparameter Tuning
    - Distributed hyperparameter tuning
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: RayTune
description: Recommended replacement on Databricks for distributed hyperparameter tuning, similar to deprecated Hyperopt SparkTrials functionality
tags:
  - hyperparameter-tuning
  - distributed-computing
  - ray
timestamp: "2026-06-19T14:20:01.689Z"
---

# RayTune

**RayTune** is a Python library for distributed hyperparameter tuning and experiment management, part of the broader [Ray](https://www.ray.io/) ecosystem for distributed computing. It provides a scalable, framework-agnostic API for optimizing machine learning model performance by systematically searching over hyperparameter configurations. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Overview

RayTune is designed to replace the functionality of the deprecated open-source [Hyperopt](https://github.com/hyperopt/hyperopt) library for distributed hyperparameter optimization. While Hyperopt is no longer maintained and is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML, RayTune offers a similar experience for distributed tuning workloads. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

Databricks recommends RayTune for users who previously relied on Hyperopt's `SparkTrials` for distributed hyperparameter tuning. For single-node optimization, Databricks recommends using [Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna) instead. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Key Features

- **Distributed execution** – Runs multiple trials in parallel across a cluster of machines or GPUs
- **Framework agnostic** – Works with any machine learning framework (PyTorch, TensorFlow, scikit-learn, XGBoost, etc.)
- **Multiple search algorithms** – Supports grid search, random search, Bayesian optimization (via HyperOptSearch), and population-based training
- **Early stopping** – Integrates with schedulers like ASHA, HyperBand, and MedianStoppingRule to terminate unpromising trials early
- **Integration with MLflow** – Automatic experiment tracking and result logging for every trial run

## Integration with MLflow

RayTune integrates with [MLflow](/concepts/mlflow.md) for automatic experiment tracking. When used on Databricks, MLflow automatically records every trial run, enabling comparison of results across different hyperparameter configurations in the MLflow UI. This integration provides full visibility into the tuning process, including parameters, metrics, artifacts, and model checkpoints for each trial. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Migration from Hyperopt

Organizations migrating from Hyperopt to RayTune should note the following considerations:

- RayTune provides a similar distributed tuning experience for hyperparameter optimization
- The transition requires updating trial execution code and result handling patterns
- The `tune.report()` API replaces Hyperopt's return value pattern for communicating results back to the optimizer
- MLflow experiment tracking remains available to monitor and compare results across trials
- RayTune's `Analysis` object provides comprehensive access to trial results, configuration, and metadata

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – The process of optimizing model parameters to improve performance
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model management platform
- Distributed Computing – Parallelizing computation across multiple workers
- Ray (computing framework) – The broader distributed computing framework for AI and Python applications
- [Hyperopt](/concepts/hyperopt.md) – The predecessor library no longer maintained
- [Optuna](/concepts/optuna.md) – Alternative library for single-node hyperparameter optimization
- [SparkTrials](/concepts/sparktrials.md) – The distributed execution mode in Hyperopt that RayTune replaces

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
