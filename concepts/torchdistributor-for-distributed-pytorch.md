---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f18702998236f4ce26765d47169d63125a71efc30204d98f6ff4047ec38a98e5
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-for-distributed-pytorch
    - TFDP
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: TorchDistributor for Distributed PyTorch
description: Databricks-recommended replacement for Horovod when performing distributed training with PyTorch.
tags:
  - distributed-training
  - pytorch
  - databricks
timestamp: "2026-06-19T10:48:35.999Z"
---

# TorchDistributor for Distributed PyTorch

**TorchDistributor** is a distributed training tool on Databricks designed specifically for PyTorch workloads. It provides a simple API to scale PyTorch training across multiple GPUs and nodes.

## Overview

TorchDistributor is the recommended approach for distributed training with PyTorch on Databricks. It serves as a replacement for the now-deprecated [Horovod](/concepts/horovod.md) and [HorovodRunner](/concepts/horovodrunner.md) packages, which are no longer installed by default in Databricks Runtime ML releases after 15.4 LTS ML. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

For distributed training with TensorFlow, Databricks recommends using the `tf.distribute.Strategy` API instead. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Usage Recommendation

Databricks advises users to migrate existing Horovod-based PyTorch training code to TorchDistributor. This ensures compatibility with future Databricks Runtime ML versions and access to ongoing support. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General strategies for scaling model training across multiple accelerators.
- [PyTorch DDP](/concepts/pytorch-ddp-on-databricks.md) — The native Distributed Data Parallel module in PyTorch.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — A memory-efficient sharding strategy for large models.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime environment that includes TorchDistributor.
- [Horovod](/concepts/horovod.md) — The deprecated distributed training framework that TorchDistributor replaces.

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
