---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37deb57a391a2934044278b7d5c19e73f976a508ce73b5c8077118243edc8b94
  pageDirectory: concepts
  sources:
    - distributed-training-with-tensorflow-2-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - tensorflow-on-spark-clusters
    - TOSC
  citations:
    - file: distributed-training-with-tensorflow-2-databricks-on-aws.md
title: TensorFlow on Spark clusters
description: Pattern for integrating TensorFlow 2 distributed training with Apache Spark clusters via the TensorFlow ecosystem package
tags:
  - tensorflow
  - spark
  - distributed-training
  - infrastructure
timestamp: "2026-06-18T15:34:32.431Z"
---

# TensorFlow on Spark Clusters

**TensorFlow on Spark Clusters** refers to the practice of training TensorFlow models using the distributed computing capabilities of Apache Spark. This integration is enabled by an open-source package called `spark-tensorflow-distributor`, which allows users to leverage Spark clusters for distributed deep learning workflows. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Overview

The `spark-tensorflow-distributor` is a TensorFlow-native package that simplifies distributed training on Spark clusters. It is built on top of TensorFlow 2’s `tensorflow.distribute.Strategy`, a core API for distributing training across multiple devices. This means that users familiar with TensorFlow's distributed strategies can apply the same concepts in a Spark environment without needing to manage the underlying cluster infrastructure manually. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## How It Works

The distributor uses TensorFlow’s `MirroredStrategy` (a type of `tf.distribute.Strategy`) to synchronously replicate model computations across multiple GPUs or CPUs available on the Spark cluster. Under the hood, it coordinates the Spark executors to act as workers in a TensorFlow cluster, enabling data-parallel training. The package handles the communication between Spark and TensorFlow, allowing gradients to be aggregated efficiently. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Getting Started

To use TensorFlow on a Spark cluster, you typically:

1. Install the `spark-tensorflow-distributor` package on your Spark cluster.
2. Define your TensorFlow model using standard Keras or the low-level API.
3. Use the distributor's `MirroredStrategyRunner` (or equivalent) to launch training across Spark executors.

The official documentation provides detailed API usage and examples. See the [docstrings](https://github.com/tensorflow/ecosystem/blob/master/spark/spark-tensorflow-distributor/spark_tensorflow_distributor/mirrored_strategy_runner.py#L40) for method signatures and parameters. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Example Notebook

A dedicated example notebook titled **Distributed Training with TensorFlow 2** is available in the Databricks documentation archive. This notebook walks through the setup and execution of a distributed training job using `spark-tensorflow-distributor` on a Databricks cluster. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Related Concepts

- TensorFlow – The core deep learning framework.
- Spark – The distributed processing engine that provides the cluster.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General concept for training models across multiple devices.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) – TensorFlow’s abstraction for distribution.
- [MirroredStrategy](/concepts/mirroredstrategyrunner.md) – The specific strategy used by `spark-tensorflow-distributor`.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime that can simplify TensorFlow on Spark setups.

## Sources

- distributed-training-with-tensorflow-2-databricks-on-aws.md

# Citations

1. [distributed-training-with-tensorflow-2-databricks-on-aws.md](/references/distributed-training-with-tensorflow-2-databricks-on-aws-32a7d205.md)
