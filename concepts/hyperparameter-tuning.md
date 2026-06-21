---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1d34257d094078c8030ae0a083abd65d5f97ad39eea3e12da920ed2d4dc2ba0
  pageDirectory: concepts
  sources:
    - hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperparameter-tuning
    - Hyperparam tuning
    - Parameter tuning
    - Hyperparameter search
  citations:
    - file: hyperparameter-tuning-databricks-on-aws.md
title: Hyperparameter Tuning
description: The process of optimizing model hyperparameters using automated libraries like Optuna, Ray Tune, and Hyperopt to efficiently find optimal settings for ML models.
tags:
  - machine-learning
  - optimization
  - model-tuning
timestamp: "2026-06-19T19:08:52.245Z"
---

# Hyperparameter Tuning

**Hyperparameter tuning** (also called hyperparameter optimization) is the process of systematically searching for the optimal set of hyperparameters for a machine learning model to maximize its performance. Python libraries such as Optuna, Ray Tune, and Hyperopt simplify and automate this process, enabling efficient exploration of the hyperparameter search space. ^[hyperparameter-tuning-databricks-on-aws.md]

## Overview

Hyperparameter tuning involves selecting the best combination of hyperparameters — configuration settings that are not learned from data but set before training begins, such as learning rate, number of layers, or regularization strength. Automated tuning libraries scale across multiple compute resources to quickly find optimal hyperparameters with minimal manual orchestration and configuration. ^[hyperparameter-tuning-databricks-on-aws.md]

These libraries can be integrated with model tracking tools like [MLflow](/concepts/mlflow.md) to log hyperparameters and evaluation metrics across tuning trials, enabling experiment comparison and reproducibility. ^[hyperparameter-tuning-databricks-on-aws.md]

## Optuna

Optuna is a lightweight framework that makes it easy to define a dynamic search space for hyperparameter tuning and model selection. It includes some of the latest optimization and machine learning algorithms. ^[hyperparameter-tuning-databricks-on-aws.md]

Key features include:
- Easy parallelization with [Joblib](https://joblib.readthedocs.io/) to scale workloads across multiple computes
- Integration with MLflow to track hyperparameters and metrics across trials
- Dynamic search space definition capabilities

To get started with Optuna, see [Hyperparameter tuning with Optuna](/concepts/optuna-for-hyperparameter-tuning.md). ^[hyperparameter-tuning-databricks-on-aws.md]

## Ray Tune

Databricks Runtime ML includes [Ray](https://docs.ray.io/en/latest/), an open-source framework used for parallel compute processing. Ray Tune is a hyperparameter tuning library that comes with Ray and uses Ray as a backend for distributed computing. ^[hyperparameter-tuning-databricks-on-aws.md]

Ray Tune is recommended as an alternative to the deprecated Hyperopt library for distributed hyperparameter tuning, particularly on [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) clusters. ^[hyperparameter-tuning-databricks-on-aws.md]

For more information, see [Ray on Databricks](/concepts/ray-on-databricks.md) or the [Ray Tune documentation](https://docs.ray.io/en/latest/tune/tutorials/tune-distributed.html).

## Hyperopt

Hyperopt is a Python library used for distributed hyperparameter tuning and model selection. It works with both distributed ML algorithms (such as [Apache Spark MLlib](/concepts/apache-spark-mllib.md) and Horovod) and single-machine ML models (such as scikit-learn and TensorFlow). ^[hyperparameter-tuning-databricks-on-aws.md]

> **Note:** The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained. Hyperopt is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. Databricks recommends using Optuna for single-node optimization or Ray Tune for distributed hyperparameter tuning as a replacement. ^[hyperparameter-tuning-databricks-on-aws.md]

To get started with Hyperopt, see Use distributed training algorithms with Hyperopt. ^[hyperparameter-tuning-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — Experiment tracking for hyperparameter tuning trials
- [Optuna](/concepts/optuna.md) — Lightweight hyperparameter optimization framework
- [Ray Tune](/concepts/ray-tune.md) — Distributed hyperparameter tuning with Ray
- [Hyperopt](/concepts/hyperopt.md) — Distributed hyperparameter tuning library (deprecated)
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — ML-optimized runtime environment
- Automated Machine Learning (AutoML)

## Sources

- hyperparameter-tuning-databricks-on-aws.md

# Citations

1. [hyperparameter-tuning-databricks-on-aws.md](/references/hyperparameter-tuning-databricks-on-aws-6d74646d.md)
