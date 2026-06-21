---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48c6241158e9e1cf320e99d39fb4368a09ab237a6a68245e12e2c00e5088b55c
  pageDirectory: concepts
  sources:
    - use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-deprecation-and-migration-on-databricks
    - Migration on Databricks and Hyperopt Deprecation
    - HDAMOD
  citations:
    - file: use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
title: Hyperopt Deprecation and Migration on Databricks
description: Hyperopt is deprecated in Databricks Runtime for ML 16.4 LTS and later; recommended replacements are Optuna for single-node optimization and RayTune for distributed hyperparameter tuning.
tags:
  - deprecation
  - migration
  - databricks
  - hyperopt
timestamp: "2026-06-19T23:21:47.688Z"
---

# [Hyperopt deprecation and migration](/concepts/hyperopt-deprecation-and-migration.md) on Databricks

**Hyperopt Deprecation and Migration on Databricks** describes the end‑of‑life status of the open‑source [Hyperopt](/concepts/hyperopt.md)](https://github.com/[Hyperopt](/concepts/hyperopt.md)/[Hyperopt](/concepts/hyperopt.md)) library on the Databricks platform and the recommended alternatives for hyperparameter optimization.

## Overview

[Hyperopt](/concepts/hyperopt.md) is an open‑source library for [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) that was previously included in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). The open‑source version of [Hyperopt](/concepts/hyperopt.md) is no longer being maintained. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Deprecation Status

[Hyperopt](/concepts/hyperopt.md) is not included in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) starting from **16.4 LTS ML** and later. This means that users who rely on [Hyperopt](/concepts/hyperopt.md) for [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) must migrate their workloads. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Migration Paths

Databricks recommends two alternative libraries depending on the type of optimization needed:

### [Optuna](/concepts/optuna.md) for Single‑Node Optimization

[Optuna](/concepts/optuna.md)](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/[Optuna](/concepts/optuna.md)) is recommended for single‑node hyperparameter optimization tasks. It is a modern hyperparameter optimization framework that is actively maintained and integrates well with Databricks. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

### [RayTune](/concepts/raytune.md) for Distributed [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)

[RayTune](/concepts/raytune.md)](https://docs.ray.io/en/latest/tune/index.html) is recommended for workloads that require distributed [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md), providing a similar experience to the deprecated [Hyperopt](/concepts/hyperopt.md) distributed functionality. Databricks provides documentation for using [RayTune](/concepts/raytune.md)](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow) on the platform. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Using [Hyperopt](/concepts/hyperopt.md) with Distributed Training Algorithms (Legacy Guidance)

For users still running [Hyperopt](/concepts/hyperopt.md) in older runtimes, the following guidance applies when using [Hyperopt](/concepts/hyperopt.md) with distributed training algorithms (e.g., [Apache Spark MLlib](/concepts/apache-spark-mllib.md) or [HorovodRunner](/concepts/horovodrunner.md)):

- Do **not** pass a `trials` argument to `fmin()`. In particular, do not use the `SparkTrials` class. `SparkTrials` is designed for trials that are not themselves distributed; with distributed training algorithms, use the default `Trials` class. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]
- [Hyperopt](/concepts/hyperopt.md) evaluates each trial on the driver node so that the ML algorithm itself can initiate distributed training across the cluster. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

### Important Note on [MLflow](/concepts/mlflow.md) Logging

Databricks does not support automatic logging to [MLflow](/concepts/mlflow.md) when using the `Trials` class with [Hyperopt](/concepts/hyperopt.md). Users must manually call [MLflow](/concepts/mlflow.md) to log trials for [Hyperopt](/concepts/hyperopt.md) when using distributed training algorithms. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Related Concepts

- [Optuna](/concepts/optuna.md) — Recommended replacement for single‑node optimization.
- [RayTune](/concepts/raytune.md) — Recommended replacement for distributed [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md).
- [Hyperopt](/concepts/hyperopt.md) — The deprecated library.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — General topic.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Context for using [Hyperopt](/concepts/hyperopt.md) with MLlib / [HorovodRunner](/concepts/horovodrunner.md).
- [HorovodRunner](/concepts/horovodrunner.md) — Distributed deep learning API that worked with [Hyperopt](/concepts/hyperopt.md).

## Sources

- use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md

# Citations

1. [use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md](/references/use-distributed-training-algorithms-with-hyperopt-databricks-on-aws-29b4f334.md)
