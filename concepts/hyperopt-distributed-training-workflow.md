---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee820299fd36d26ec6a4625e7f581d61df5a37fede110a51e2ba4a0c60d09559
  pageDirectory: concepts
  sources:
    - use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-distributed-training-workflow
    - HDTW
  citations:
    - file: use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
title: Hyperopt Distributed Training Workflow
description: Guidance on using Hyperopt with distributed machine learning algorithms on Databricks, where trials run on the driver node so the algorithm itself can initiate distributed training.
tags:
  - hyperparameter-tuning
  - distributed-training
  - databricks
timestamp: "2026-06-19T23:21:39.716Z"
---

# [Hyperopt](/concepts/hyperopt.md) Distributed Training Workflow

> **Deprecation notice:** The open-source version of [Hyperopt](/concepts/hyperopt.md) is no longer being maintained. [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) versions after 16.4 LTS ML no longer include [Hyperopt](/concepts/hyperopt.md). Databricks recommends using [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for a distributed [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) experience similar to the deprecated [Hyperopt](/concepts/hyperopt.md) functionality. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

**Hyperopt Distributed Training Workflow** refers to the pattern of using [Hyperopt](/concepts/hyperopt.md) to tune hyperparameters for distributed machine learning algorithms—such as those from [Apache Spark MLlib](/concepts/apache-spark-mllib.md) or [HorovodRunner](/concepts/horovodrunner.md)—rather than for single‑node algorithms. In this workflow, [Hyperopt](/concepts/hyperopt.md) generates trials on the driver node, and each trial is executed on the driver so that the underlying algorithm can itself initiate distributed training across the cluster. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Prerequisite: Understanding [SparkTrials](/concepts/sparktrials.md) vs. Trials

[Hyperopt](/concepts/hyperopt.md) provides two trial classes: `SparkTrials` and the default `Trials`. `SparkTrials` is designed for **non‑distributed** training algorithms—it distributes individual trial executions across Spark workers. In the distributed training workflow, the training algorithm is already distributed (e.g., it uses all cluster resources), so distributing trials again would be counterproductive. Therefore, you must use the default `Trials` class, which runs on the cluster driver, giving each trial full access to the cluster’s resources. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Workflow Steps

1. **Do not pass a `trials` argument to `fmin()`.** Specifically, do not use `SparkTrials`. [Hyperopt](/concepts/hyperopt.md) will use the default `Trials` class automatically when no `trials` argument is provided. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]
2. **Each trial executes on the driver node.** Because the distributed training algorithm itself manages parallel work (e.g., Spark MLlib or [HorovodRunner](/concepts/horovodrunner.md)), [Hyperopt](/concepts/hyperopt.md) runs each hyperparameter configuration on the driver so the algorithm can launch distributed tasks. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]
3. **Manually log trials to [MLflow](/concepts/mlflow.md).** Databricks does not support automatic [MLflow](/concepts/mlflow.md) logging with the `Trials` class. You must explicitly call the [MLflow](/concepts/mlflow.md) API within your objective function or training code to record parameters and metrics. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Supported Distributed Algorithms

The workflow works with any distributed machine learning library that can be invoked from the driver. Two primary examples are documented:

- **Apache Spark MLlib** – Use [Hyperopt](/concepts/hyperopt.md) to tune hyperparameters for models built with MLlib’s distributed algorithms, such as logistic regression or random forests. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]
- **HorovodRunner** – [HorovodRunner](/concepts/horovodrunner.md) integrates [Horovod](/concepts/horovod.md) with Spark’s barrier mode to run distributed deep learning training. [Hyperopt](/concepts/hyperopt.md) can tune hyperparameters across [HorovodRunner](/concepts/horovodrunner.md) runs. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

Example notebooks for both approaches were provided in the Databricks documentation. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Related Concepts

- [SparkTrials](/concepts/sparktrials.md) – Used for distributing trials of non‑distributed algorithms (the opposite of the distributed training workflow).
- Trials – The default [Hyperopt](/concepts/hyperopt.md) trial class, used in the distributed training workflow.
- fmin – Hyperopt’s function minimization API, which takes an optional `trials` argument.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – Algorithms that use multiple nodes or GPUs to train a single model (e.g., MLlib, [HorovodRunner](/concepts/horovodrunner.md)).
- [MLflow logging](/concepts/mlflow-autologging.md) – Manual logging is required with the `Trials` class.
- [Optuna](/concepts/optuna.md) – Databricks’ recommended alternative for single‑node hyperparameter optimization.
- [RayTune](/concepts/raytune.md) – Databricks’ recommended alternative for distributed hyperparameter optimization.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime that historically included [Hyperopt](/concepts/hyperopt.md) (up to version 16.4 LTS ML).

## Sources

- use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md

# Citations

1. [use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md](/references/use-distributed-training-algorithms-with-hyperopt-databricks-on-aws-29b4f334.md)
