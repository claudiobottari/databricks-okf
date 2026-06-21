---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3cd452e81093887d490880360b8d2edc0e7e23c4d4e5e8cc317ee3fa8bd0bc46
  pageDirectory: concepts
  sources:
    - distributed-training-with-tensorflow-2-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - spark-cluster-integration-for-ml-training
    - SCIFMT
  citations:
    - file: distributed-training-with-tensorflow-2-databricks-on-aws.md
title: Spark Cluster Integration for ML Training
description: The pattern of leveraging Apache Spark clusters to orchestrate distributed machine learning training jobs with TensorFlow.
tags:
  - spark
  - machine-learning
  - cluster-computing
timestamp: "2026-06-18T12:09:10.458Z"
---

# Spark Cluster Integration for ML Training

**Spark Cluster Integration for ML Training** refers to the practice of using Apache Spark clusters to distribute machine learning training workloads across multiple nodes. The primary native integration for TensorFlow with Spark is the `spark-tensorflow-distributor` package, an open-source library that enables distributed TensorFlow training directly on Spark clusters. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Overview

The spark-tensorflow-distributor is a native TensorFlow package designed to help users perform distributed training using TensorFlow 2 on their existing Spark infrastructure. It is built on top of `tensorflow.distribute.Strategy`, a core TensorFlow 2 feature for distributing computation across devices and machines. This allows data scientists and engineers to leverage Spark’s resource management and cluster orchestration for scalable deep learning without leaving the familiar TensorFlow ecosystem. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## How It Works

The spark-tensorflow-distributor runs TensorFlow training tasks as distributed jobs on a Spark cluster. It uses the Spark driver to coordinate worker nodes, each of which executes a copy of the training script. Under the hood, the package wraps TensorFlow’s `tf.distribute.MirroredStrategy` (or other strategies) to synchronize gradients and update model parameters across workers. The library handles the setup of communication channels (e.g., gRPC, NCCL) between Spark executors, abstracting the complexity of distributed session management. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Usage

To use the spark-tensorflow-distributor, you include the package in your Spark environment and invoke it from a Python notebook or script. A typical workflow involves:

1. Defining a TensorFlow model using the Keras API.
2. Creating a `MirroredStrategyRunner` from `spark_tensorflow_distributor`.
3. Passing a training function to the runner, which distributes it across the Spark cluster.

For detailed API documentation, see the official [docstrings](https://github.com/tensorflow/ecosystem/blob/master/spark/spark-tensorflow-distributor/spark_tensorflow_distributor/mirrored_strategy_runner.py#L40). ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

### Example Notebook

A complete example notebook titled **Distributed Training with TensorFlow 2** is available in the Databricks documentation. It demonstrates end-to-end usage on a Databricks cluster. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Prerequisites

- A Spark cluster (e.g., Databricks cluster) with sufficient resources.
- TensorFlow 2.x installed on all cluster nodes.
- Network connectivity between Spark executors for inter-worker communication.

## Benefits

- **Unified infrastructure**: Use the same Spark cluster for data preprocessing, feature engineering, and model training.
- **Scalability**: Easily scale training from a single node to hundreds of workers by adjusting cluster size.
- **Integration with MLflow**: Combine distributed training with [MLflow](/concepts/mlflow.md) for experiment tracking, model logging, and deployment.

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General techniques for training models across multiple machines.
- TensorFlow — The deep learning framework used with the spark-tensorflow-distributor.
- Spark Cluster — The underlying compute infrastructure managed by Apache Spark.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) — TensorFlow’s native API for distributed computation.
- [MLflow](/concepts/mlflow.md) — Platform for managing the ML lifecycle, including tracking distributed training runs.
- Databricks — Cloud platform that supports Spark cluster integration for ML.

## Sources

- distributed-training-with-tensorflow-2-databricks-on-aws.md

# Citations

1. [distributed-training-with-tensorflow-2-databricks-on-aws.md](/references/distributed-training-with-tensorflow-2-databricks-on-aws-32a7d205.md)
