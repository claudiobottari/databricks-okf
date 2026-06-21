---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b20933828eec6b8a7d0cd2cc2f5f3ac511d3f269494547f9f27a8d188e4852af
  pageDirectory: concepts
  sources:
    - distributed-training-with-tensorflow-2-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  citations:
    - file: distributed-training-with-tensorflow-2-databricks-on-aws.md
title: spark-tensorflow-distributor
description: An open-source native TensorFlow package for distributed training on Spark clusters
tags:
  - tensorflow
  - spark
  - distributed-training
timestamp: "2026-06-19T18:38:18.751Z"
---

# Spark TensorFlow Distributor

**Spark TensorFlow Distributor** (`spark-tensorflow-distributor`) is an open-source native TensorFlow package that enables distributed training of TensorFlow models on Apache Spark|Spark clusters. It is built on top of `tensorflow.distribute.Strategy`, which is one of the major features in TensorFlow 2. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Overview

The package serves as a bridge between Spark's resource management and TensorFlow's distribution API, allowing users to run TensorFlow training workloads directly on their existing Spark infrastructure without requiring separate cluster management. The package is hosted in the TensorFlow ecosystem repository on GitHub and works with TensorFlow 2.x. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Documentation

Detailed API documentation is available in the [docstrings](https://github.com/tensorflow/ecosystem/blob/master/spark/spark-tensorflow-distributor/spark_tensorflow_distributor/mirrored_strategy_runner.py#L40) of the `MirroredStrategyRunner`. For general guidance on distributed TensorFlow, see the [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training) guide. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Example

The Databricks documentation includes an example notebook titled **Distributed Training with TensorFlow 2** that demonstrates the usage of `spark-tensorflow-distributor`. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Related Concepts

- [tensorflow.distribute.Strategy](/concepts/tensorflowdistributestrategy.md) — The underlying API for distributing computation across devices and machines.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Broader context for scaling machine learning workloads.
- Apache Spark — Cluster computing framework used with this package.
- [HorovodRunner](/concepts/horovodrunner.md) — Alternative approach for distributed training on Spark (non-native TensorFlow).
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — GPU configuration suitable for running distributed TensorFlow workloads.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Advanced distributed training strategy for very large models.

## Sources

- distributed-training-with-tensorflow-2-databricks-on-aws.md

# Citations

1. [distributed-training-with-tensorflow-2-databricks-on-aws.md](/references/distributed-training-with-tensorflow-2-databricks-on-aws-32a7d205.md)
