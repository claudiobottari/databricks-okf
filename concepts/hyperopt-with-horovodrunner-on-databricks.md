---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ced4f9067ee8cd88b0ec90702a8711ce294a552db219d897bf04a760da8e0bbf
  pageDirectory: concepts
  sources:
    - use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-with-horovodrunner-on-databricks
    - HWHOD
  citations:
    - file: use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
title: Hyperopt with HorovodRunner on Databricks
description: Integration of Hyperopt with HorovodRunner to tune distributed deep learning workloads on Databricks, leveraging Spark's barrier mode for stability.
tags:
  - hyperopt
  - horovod
  - deep-learning
  - databricks
timestamp: "2026-06-19T23:22:06.076Z"
---

# [Hyperopt](/concepts/hyperopt.md) with [HorovodRunner](/concepts/horovodrunner.md) on Databricks

**Hyperopt with [HorovodRunner](/concepts/horovodrunner.md) on Databricks** refers to the integration of the [Hyperopt](/concepts/hyperopt.md) [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) library with [HorovodRunner](/concepts/horovodrunner.md) for distributed deep learning training workloads. This combination allows users to optimize hyperparameters for distributed training jobs that leverage [Horovod](/concepts/horovod.md)'s multi-GPU and multi-node capabilities on Databricks clusters.

## Overview

[HorovodRunner](/concepts/horovodrunner.md) is a general API used to run distributed deep learning workloads on Databricks. It integrates [Horovod](/concepts/horovod.md)](https://github.com/[Horovod](/concepts/horovod.md)/[Horovod](/concepts/horovod.md)) with Spark's barrier mode to provide higher stability for long-running deep learning training jobs on Spark. When combined with [Hyperopt](/concepts/hyperopt.md), users can perform [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) on distributed training algorithms. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

In this scenario, [Hyperopt](/concepts/hyperopt.md) generates trials with different hyperparameter settings on the driver node. Each trial is executed from the driver node, giving it access to the full cluster resources. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Important Considerations

### Deprecation Notice

The open-source version of [Hyperopt](/concepts/hyperopt.md) is no longer being maintained. [Hyperopt](/concepts/hyperopt.md) is not included in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) after 16.4 LTS ML. Databricks recommends using either [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for a similar experience to the deprecated [Hyperopt](/concepts/hyperopt.md) distributed [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) functionality. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

### Trial Class Requirements

When using [Hyperopt](/concepts/hyperopt.md) with [HorovodRunner](/concepts/horovodrunner.md), do not pass a `trials` argument to `fmin()`, and specifically, do not use the `SparkTrials` class. `SparkTrials` is designed to distribute trials for algorithms that are not themselves distributed. With distributed training algorithms like [HorovodRunner](/concepts/horovodrunner.md), use the default `Trials` class, which runs on the cluster driver. [Hyperopt](/concepts/hyperopt.md) evaluates each trial on the driver node so that the ML algorithm itself can initiate distributed training. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

### [MLflow](/concepts/mlflow.md) Logging

Databricks does not support automatic logging to [MLflow](/concepts/mlflow.md) with the `Trials` class. When using distributed training algorithms with [Hyperopt](/concepts/hyperopt.md), you must manually call [MLflow](/concepts/mlflow.md) to log trials for [Hyperopt](/concepts/hyperopt.md). ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Relationship to Other Distributed Training Approaches

This approach works with any distributed machine learning algorithms or libraries, including [Apache Spark MLlib](/concepts/apache-spark-mllib.md) and [HorovodRunner](/concepts/horovodrunner.md). The same principles apply whether tuning MLlib's distributed training algorithms or Horovod-based deep learning models. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Implementation

A typical implementation involves:

1. Defining a hyperparameter search space
2. Creating an objective function that uses [HorovodRunner](/concepts/horovodrunner.md) to execute distributed training
3. Calling `fmin()` with the default `Trials` class
4. Manually logging each trial to [MLflow](/concepts/mlflow.md) within the objective function

The example notebook "[Hyperopt](/concepts/hyperopt.md) and [HorovodRunner](/concepts/horovodrunner.md) distributed training" demonstrates this workflow.

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) — The hyperparameter optimization library
- [HorovodRunner](/concepts/horovodrunner.md) — Distributed deep learning API on Databricks
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-node and multi-GPU training approaches
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment logging and tracking
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — General hyperparameter optimization concepts

## Sources

- use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md

# Citations

1. [use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md](/references/use-distributed-training-algorithms-with-hyperopt-databricks-on-aws-29b4f334.md)
