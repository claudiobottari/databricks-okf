---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ccf6d3c1a6b148b5daf7c1b1cb5eaf13cfadc6f516882560b5f08375421b3744
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: Horovod
description: A distributed deep learning framework that can be used on Databricks for scaling PyTorch and other ML models across multiple nodes.
tags:
  - distributed-training
  - deep-learning
  - framework
timestamp: "2026-06-19T17:26:29.647Z"
---

# Horovod

**Horovod** is an open‑source distributed deep learning training framework that supports TensorFlow, Keras, and PyTorch. It is used in conjunction with [HorovodRunner](/concepts/horovodrunner.md) on Databricks to scale single‑node training to multiple GPUs and multiple machines. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Overview

The recommended development workflow for distributed training on Databricks begins with training a model on a single node, then adapting the code to use HorovodRunner for distributed execution. A PyTorch MNIST example notebook demonstrates this workflow, first showing single‑node training followed by the adaptations needed to run with Horovod. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

Horovod itself is the underlying communication layer – it uses `hvd.allreduce` and `hvd.broadcast` operations to synchronize gradients across workers in a data‑parallel fashion. On Databricks, Horovod is pre‑installed on [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) clusters and can be invoked via HorovodRunner.

## Example Notebook

- **PyTorch MNIST example** – see [Adapt single node PyTorch to distributed deep learning](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/mnist-pytorch) ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – High‑level API for distributed training on Spark clusters
- PyTorch – Deep learning framework supported by Horovod
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) – General concepts for multi‑node training
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – Required runtime for Horovod
- [TorchDistributor](/concepts/torchdistributor.md) – Recommended replacement for PyTorch distributed training (for new projects)

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
