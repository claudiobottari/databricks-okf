---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 77993403829caa0cb92aae6a65946b5287be1016568fe3d74f69bbceaad87c5e
  pageDirectory: concepts
  sources:
    - hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt
  citations:
    - file: hyperparameter-tuning-databricks-on-aws.md
title: Hyperopt
description: A deprecated Python library for distributed hyperparameter tuning, not included in Databricks Runtime ML after 16.4 LTS ML.
tags:
  - machine-learning
  - python-library
  - hyperparameter-tuning
  - deprecated
timestamp: "2026-06-19T19:08:29.897Z"
---

# Hyperopt

**Hyperopt** is an open-source Python library for distributed hyperparameter tuning and model selection. It works with both distributed ML algorithms (e.g., [Apache Spark MLlib](/concepts/apache-spark-mllib.md), Horovod) and single‑machine models (e.g., scikit‑learn, TensorFlow). ^[hyperparameter-tuning-databricks-on-aws.md]

## Status and Deprecation

The open‑source version of Hyperopt is no longer being maintained. Starting with Databricks Runtime for Machine Learning 16.4 LTS ML, Hyperopt is not included. Databricks recommends using **[Optuna](/concepts/optuna.md)** for single‑node optimization or **[RayTune](/concepts/raytune.md)** for a distributed experience similar to Hyperopt. ^[hyperparameter-tuning-databricks-on-aws.md]

## Getting Started

Databricks directs users to the [Hyperopt documentation](https://github.com/hyperopt/hyperopt) for general usage, and to [Use distributed training algorithms with Hyperopt](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-distributed-ml) for using Hyperopt with distributed ML algorithms on Databricks. ^[hyperparameter-tuning-databricks-on-aws.md]

## Alternatives

| Library | Recommended Use | Notes |
|---------|----------------|-------|
| [Optuna](/concepts/optuna.md) | Single‑node optimization | Lightweight framework with dynamic search spaces and MLflow integration. |
| [RayTune](/concepts/raytune.md) | Distributed hyperparameter tuning | Runs on Ray, provides a similar experience to Hyperopt’s distributed functionality. |

For details on running Ray on Databricks, see [Ray on Databricks](/concepts/ray-on-databricks.md). ^[hyperparameter-tuning-databricks-on-aws.md]

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- [Optuna](/concepts/optuna.md)
- [RayTune](/concepts/raytune.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

## Sources

- hyperparameter-tuning-databricks-on-aws.md

# Citations

1. [hyperparameter-tuning-databricks-on-aws.md](/references/hyperparameter-tuning-databricks-on-aws-6d74646d.md)
