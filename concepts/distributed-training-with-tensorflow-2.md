---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8021223eec97bd1d5c6a1bb006cd7b2b0f0b8a952d19aceb846d017dce2455ea
  pageDirectory: concepts
  sources:
    - distributed-training-with-tensorflow-2-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-with-tensorflow-2
    - DTWT2
    - Distributed training with TensorFlow
    - Distributed Training with TensorFlow (tf.distribute.Strategy)
  citations:
    - file: distributed-training-with-tensorflow-2-databricks-on-aws.md
title: Distributed training with TensorFlow 2
description: Approach to scaling TensorFlow model training across multiple workers using tf.distribute.Strategy
tags:
  - tensorflow
  - distributed-training
  - deep-learning
timestamp: "2026-06-19T18:38:12.759Z"
---

# Distributed training with TensorFlow 2

**Distributed training with TensorFlow 2** refers to the use of the `spark-tensorflow-distributor`, an open-source native package in TensorFlow that enables distributed training on Spark clusters. The package is built on top of `tensorflow.distribute.Strategy`, a major feature introduced in TensorFlow 2 for distributing training across multiple devices. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Overview

The `spark-tensorflow-distributor` integrates TensorFlow’s native distributed strategy API with Spark’s cluster management, allowing users to scale TensorFlow training workflows without leaving the Spark ecosystem. It provides a `MirroredStrategyRunner` that coordinates `tf.distribute.MirroredStrategy` across Spark executors. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

Detailed API documentation is available in the [docstrings](https://github.com/tensorflow/ecosystem/blob/master/spark/spark-tensorflow-distributor/spark_tensorflow_distributor/mirrored_strategy_runner.py#L40). For general guidance on distributed TensorFlow, see the [official TensorFlow documentation](https://www.tensorflow.org/guide/distributed_training). ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Example

A companion notebook titled **Distributed Training with TensorFlow 2** demonstrates the usage of the package within a Databricks environment. Users are directed to that notebook for a concrete walkthrough. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – An alternative memory‑efficient parallelism strategy for large models.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – A common parallelism technique suitable for models that fit in single‑GPU memory.
- TensorFlow – The deep learning framework that provides `tensorflow.distribute.Strategy`.
- [Data parallelism](/concepts/data-parallelism-spark.md) – The underlying paradigm that replicates the model across devices and splits the data.

## Sources

- distributed-training-with-tensorflow-2-databricks-on-aws.md

# Citations

1. [distributed-training-with-tensorflow-2-databricks-on-aws.md](/references/distributed-training-with-tensorflow-2-databricks-on-aws-32a7d205.md)
