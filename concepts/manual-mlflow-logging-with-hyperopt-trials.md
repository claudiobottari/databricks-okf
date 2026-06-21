---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0032ed9e5746b26a06107d6bd1227a349e2a27180dcb1cfbbe2b9964b9f77fb4
  pageDirectory: concepts
  sources:
    - use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manual-mlflow-logging-with-hyperopt-trials
    - MMLWHT
  citations:
    - file: use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
title: Manual MLflow Logging with Hyperopt Trials
description: When using the Trials class with distributed training algorithms on Databricks, automatic MLflow logging is not supported; users must manually call MLflow to log trials.
tags:
  - mlflow
  - hyperopt
  - logging
  - databricks
timestamp: "2026-06-19T23:21:53.302Z"
---

# Manual [MLflow](/concepts/mlflow.md) Logging with [Hyperopt](/concepts/hyperopt.md) Trials

**Manual [MLflow](/concepts/mlflow.md) Logging with [Hyperopt](/concepts/hyperopt.md) Trials** refers to the practice of explicitly calling [MLflow](/concepts/mlflow.md) logging APIs within [Hyperopt](/concepts/hyperopt.md) objective functions when using distributed training algorithms, rather than relying on automatic logging. This approach is required when using [Hyperopt](/concepts/hyperopt.md)'s default `Trials` class with distributed machine learning algorithms on Databricks. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Overview

When using [Hyperopt](/concepts/hyperopt.md) with distributed training algorithms such as [Apache Spark MLlib](/concepts/apache-spark-mllib.md) or [HorovodRunner](/concepts/horovodrunner.md), [Hyperopt](/concepts/hyperopt.md) generates trials with different hyperparameter settings on the driver node. Each trial is executed from the driver node, giving it access to the full cluster resources. In this configuration, [Hyperopt](/concepts/hyperopt.md) uses the default `Trials` class rather than `SparkTrials`. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Why Manual Logging Is Required

Databricks does not support automatic logging to [MLflow](/concepts/mlflow.md) with the `Trials` class. When using distributed training algorithms, you must manually call [MLflow](/concepts/mlflow.md) to log trials for [Hyperopt](/concepts/hyperopt.md). ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

The `SparkTrials` class is designed to distribute trials for algorithms that are not themselves distributed. With distributed training algorithms, you should use the default `Trials` class, which runs on the cluster driver. [Hyperopt](/concepts/hyperopt.md) evaluates each trial on the driver node so that the ML algorithm itself can initiate distributed training. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Implementation

When using [Hyperopt](/concepts/hyperopt.md) with distributed training algorithms, do not pass a `trials` argument to `fmin()`, and specifically, do not use the `SparkTrials` class. Instead, within your objective function, manually call [MLflow](/concepts/mlflow.md) logging functions to record parameters, metrics, and artifacts for each trial. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) — The hyperparameter optimization framework used for trial generation.
- [SparkTrials](/concepts/sparktrials.md) — A [Hyperopt](/concepts/hyperopt.md) trials class for distributing trials across a Spark cluster (not used with distributed training algorithms).
- Trials — The default [Hyperopt](/concepts/hyperopt.md) trials class that runs on the driver node.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The system for logging parameters, metrics, and artifacts.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Training algorithms that leverage multiple nodes or GPUs.
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — A distributed machine learning library that can be tuned with [Hyperopt](/concepts/hyperopt.md).
- [HorovodRunner](/concepts/horovodrunner.md) — A Databricks API for running distributed deep learning workloads.

## Sources

- use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md

# Citations

1. [use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md](/references/use-distributed-training-algorithms-with-hyperopt-databricks-on-aws-29b4f334.md)
