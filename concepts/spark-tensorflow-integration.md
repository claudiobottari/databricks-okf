---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2faf02005965e40b12931a2b56ba83c100d874cd2e3d5f79887214c2ca07cb6c
  pageDirectory: concepts
  sources:
    - distributed-training-with-tensorflow-2-databricks-on-aws.md
  confidence: 0.75
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - spark-tensorflow-integration
  citations:
    - file: distributed-training-with-tensorflow-2-databricks-on-aws.md
title: Spark-TensorFlow Integration
description: The pattern of combining Apache Spark's distributed data processing with TensorFlow's deep learning capabilities for scalable ML workflows
tags:
  - spark
  - tensorflow
  - integration
  - machine-learning
timestamp: "2026-06-19T10:19:33.369Z"
---

---
title: Spark-TensorFlow Integration
summary: The spark-tensorflow-distributor is an open-source native package in TensorFlow that enables distributed training of TensorFlow models on Spark clusters, built on top of `tensorflow.distribute.Strategy`.
sources:
  - distributed-training-with-tensorflow-2-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:03:09.487Z"
updatedAt: "2026-06-18T08:03:09.487Z"
tags:
  - tensorflow
  - spark
  - distributed-training
aliases:
  - spark-tensorflow-integration
  - spark-tensorflow-distributor
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Spark-TensorFlow Integration

**Spark-TensorFlow Integration** refers to the use of the `spark-tensorflow-distributor`, an open-source native package in TensorFlow that enables distributed training of TensorFlow models directly on Apache Spark clusters. This integration is built on top of `tensorflow.distribute.Strategy`, a core TensorFlow 2 API for distributed computation. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Overview

The spark-tensorflow-distributor package allows data scientists and engineers to run TensorFlow distributed training workloads on existing Spark infrastructure without needing separate cluster managers. By leveraging Spark's executor model, the package coordinates the distribution of training across multiple nodes while using TensorFlow's native distribution strategies for gradient synchronization and model replication. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

The package is part of the TensorFlow ecosystem repository on GitHub. For detailed API documentation, refer to the docstrings in the source code, and for general information about distributed TensorFlow, see the official TensorFlow guide on distributed training. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## How It Works

The spark-tensorflow-distributor wraps TensorFlow's `tf.distribute.Strategy` (such as `MirroredStrategy`) and runs it across the Spark executors. When a training function is launched, the package distributes the TensorFlow cluster configuration to each executor, allowing the strategy to manage communication and synchronization. This approach provides a familiar TensorFlow experience while benefiting from Spark's resource management and scheduling. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Example Notebook

Databricks provides an example notebook titled "Distributed Training with TensorFlow 2" that demonstrates how to use the spark-tensorflow-distributor on the Databricks platform. The notebook covers setup, model definition, and execution of distributed training on a Spark cluster. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General paradigm for training models across multiple devices or machines.
- [TensorFlow Distribution Strategies](/concepts/tensorflowdistributestrategy.md) – The underlying APIs (`MirroredStrategy`, `MultiWorkerMirroredStrategy`, etc.) used by the spark-tensorflow-distributor.
- Apache Spark – The cluster computing framework that provides the execution environment.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-configured runtime that includes TensorFlow and Spark integration.

## Sources

- distributed-training-with-tensorflow-2-databricks-on-aws.md

# Citations

1. [distributed-training-with-tensorflow-2-databricks-on-aws.md](/references/distributed-training-with-tensorflow-2-databricks-on-aws-32a7d205.md)
