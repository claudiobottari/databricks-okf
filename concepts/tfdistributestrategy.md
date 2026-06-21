---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f537d7d383d955e8e83788b6f84ed5e277c59c9e4382b9660d2c1a6ff61cca9
  pageDirectory: concepts
  sources:
    - distributed-training-with-tensorflow-2-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - tfdistributestrategy
  citations:
    - file: distributed-training-with-tensorflow-2-databricks-on-aws.md
title: tf.distribute.Strategy
description: Core TensorFlow 2 API for distributing training across multiple devices and machines
tags:
  - tensorflow
  - distributed-training
  - api
timestamp: "2026-06-19T18:38:18.545Z"
---

# tf.distribute.Strategy

**`tf.distribute.Strategy`** is a TensorFlow API for distributed training that provides a unified interface for running training workloads across multiple GPUs, multiple machines, or TPUs. It is the standard approach recommended by both TensorFlow and Databricks for distributed TensorFlow training. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Overview

`tf.distribute.Strategy` abstracts the distribution logic away from the model code, handling data parallelism, model replication, gradient aggregation, and synchronization. It is a core feature introduced in TensorFlow 2 that enables users to scale training from a single GPU to multi-node clusters with minimal code changes. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Key Components

### spark-tensorflow-distributor

The [spark-tensorflow-distributor](https://github.com/tensorflow/ecosystem/tree/master/spark/spark-tensorflow-distributor) is an open-source native package built on top of `tf.distribute.Strategy`. It helps users perform distributed training with TensorFlow on Spark clusters, integrating TensorFlow's distribution capabilities with Apache Spark infrastructure. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

### MirroredStrategyRunner

A key component of the spark-tensorflow-distributor is the `MirroredStrategyRunner`, which implements the `tf.distribute.MirroredStrategy` on Spark clusters. For detailed API documentation, see the [docstrings in the GitHub repository](https://github.com/tensorflow/ecosystem/blob/master/spark/spark-tensorflow-distributor/spark_tensorflow_distributor/mirrored_strategy_runner.py#L40). ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Common Strategies

`tf.distribute.Strategy` provides several built-in strategies for different distributed training scenarios:

- **MirroredStrategy** — Synchronous training across multiple GPUs on a single machine
- **MultiWorkerMirroredStrategy** — Synchronous training across multiple machines
- **TPUStrategy** — Training on TPUs
- **ParameterServerStrategy** — Asynchronous training with parameter servers
- **OneDeviceStrategy** — Single-device fallback strategy

## Integration with Databricks

`tf.distribute.Strategy` (via spark-tensorflow-distributor) integrates with Databricks clusters to enable distributed TensorFlow training on Spark infrastructure. For general documentation about distributed TensorFlow, see [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training). ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Related Concepts

- TensorFlow — The deep learning framework providing the `tf.distribute.Strategy` API
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concept of training models across multiple accelerators
- Apache Spark — Cluster computing framework used with spark-tensorflow-distributor
- [Horovod](/concepts/horovod.md) — Alternative distributed training framework
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training for very large models

## Sources

- distributed-training-with-tensorflow-2-databricks-on-aws.md

# Citations

1. [distributed-training-with-tensorflow-2-databricks-on-aws.md](/references/distributed-training-with-tensorflow-2-databricks-on-aws-32a7d205.md)
