---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 551c830e7dadf38179849bb5dd30c82f618256b4b1d6b2d8f3f2e0ff2cd8abc7
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tfdistributestrategy-for-distributed-tensorflow
    - TFDT
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: tf.distribute.Strategy for Distributed TensorFlow
description: Databricks-recommended replacement for Horovod when performing distributed training with TensorFlow.
tags:
  - distributed-training
  - tensorflow
  - databricks
timestamp: "2026-06-19T10:48:41.242Z"
---

# tf.distribute.Strategy for Distributed TensorFlow

**`tf.distribute.Strategy`** is a TensorFlow API for distributed training that Databricks recommends as the primary approach for training TensorFlow models across multiple GPUs, TPUs, or machines. It replaces the now-deprecated [Horovod](/concepts/horovod.md) and [HorovodRunner](/concepts/horovodrunner.md) packages. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Overview

Distributed training is essential for scaling deep learning workloads to large datasets and models. `tf.distribute.Strategy` provides a high-level interface that abstracts distribution logic, allowing users to write training code that runs seamlessly on a single GPU, multiple GPUs, or multiple nodes without manual parallelism management.

## Databricks Recommendation

Databricks has deprecated Horovod and HorovodRunner. Starting from Databricks Runtime 15.4 LTS ML, these packages are no longer pre‑installed. For distributed deep learning with TensorFlow, Databricks recommends using the `tf.distribute.Strategy` API. For PyTorch workloads, the recommended alternative is [TorchDistributor](/concepts/torchdistributor.md). ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

This recommendation follows the broader TensorFlow ecosystem, where `tf.distribute.Strategy` is the standard approach for distributed training. It integrates natively with Keras and other TensorFlow components.

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General strategies for scaling training across multiple accelerators.
- [TorchDistributor](/concepts/torchdistributor.md) – The recommended API for distributed PyTorch training on Databricks.
- [Horovod (deprecated)](/concepts/horovod-deprecation-on-databricks.md) – The legacy distributed training library that `tf.distribute.Strategy` replaces.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime environment that includes TensorFlow and related libraries.

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
