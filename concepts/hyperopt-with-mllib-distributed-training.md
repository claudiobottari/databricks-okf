---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b68ae3520d2a3b16a3c6b69704f3fc272cdb8f0f189c81b7fe0e21fc2fac327
  pageDirectory: concepts
  sources:
    - use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-with-mllib-distributed-training
    - HWMDT
  citations:
    - file: use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
title: Hyperopt with MLlib Distributed Training
description: Example pattern for using Hyperopt to tune hyperparameters of Apache Spark MLlib's distributed training algorithms using the Trials class.
tags:
  - hyperopt
  - mllib
  - spark
  - distributed-training
timestamp: "2026-06-19T23:21:51.447Z"
---

Here is a clear, well-structured wiki page for "[Hyperopt](/concepts/hyperopt.md) with MLlib Distributed Training", based solely on the provided source material.

---

## [Hyperopt](/concepts/hyperopt.md) with MLlib Distributed Training

**Hyperopt with MLlib Distributed Training** is a [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) approach where [Hyperopt](/concepts/hyperopt.md) orchestrates trials on the driver node, but each trial is executed using a distributed training algorithm like [Apache Spark MLlib](/concepts/apache-spark-mllib.md). This differs from [Hyperopt](/concepts/hyperopt.md)'s `SparkTrials` class, which distributes the trials themselves.

### Overview

When using [Hyperopt](/concepts/hyperopt.md) with distributed training algorithms, [Hyperopt](/concepts/hyperopt.md) generates trials with different hyperparameter settings on the driver node. Each trial is then executed from the driver node, giving it access to the full cluster resources for distributed computation. This setup works with any distributed machine learning algorithm or library, including [Apache Spark MLlib](/concepts/apache-spark-mllib.md) and [HorovodRunner](/concepts/horovodrunner.md). ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

### Important Configuration

When using [Hyperopt](/concepts/hyperopt.md) with distributed training algorithms, do not pass a `trials` argument to `fmin()`. Specifically, do not use the [SparkTrials](/concepts/sparktrials.md) class. `SparkTrials` is designed to distribute trials for algorithms that are not themselves distributed. With distributed training algorithms, use the default `Trials` class, which runs on the cluster driver. [Hyperopt](/concepts/hyperopt.md) evaluates each trial on the driver node so that the ML algorithm itself can initiate distributed training. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

### [MLflow](/concepts/mlflow.md) Integration

Databricks does not support automatic logging to [MLflow](/concepts/mlflow.md) with the `Trials` class. When using distributed training algorithms, you must manually call [MLflow](/concepts/mlflow.md) to log trials for [Hyperopt](/concepts/hyperopt.md). ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

### Deprecation Note

The open-source version of [Hyperopt](/concepts/hyperopt.md) is no longer being maintained. [Hyperopt](/concepts/hyperopt.md) is not included in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) after 16.4 LTS ML. Databricks recommends using either [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for a similar experience to the deprecated [Hyperopt](/concepts/hyperopt.md) distributed [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) functionality. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

### Related Concepts

- Hyperopt `SparkTrials` — an alternative class for distributing trials (not recommended for distributed algorithms)
- HorovodRunner Distributed Training with Hyperopt
- [Optuna](/concepts/optuna.md) — recommended alternative for single-node optimization
- [RayTune](/concepts/raytune.md) — recommended alternative for distributed [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- [Hyperparameter tuning on Databricks](/concepts/hyperparameter-tuning-on-databricks.md)

### Sources

- use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md

# Citations

1. [use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md](/references/use-distributed-training-algorithms-with-hyperopt-databricks-on-aws-29b4f334.md)
