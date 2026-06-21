---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a7aa4df4bbab03209d6fc13bbd58bdbbe292aeb19afae3527951c5337cb0649
  pageDirectory: concepts
  sources:
    - distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepspeed-distributor
    - deepspeed-distributor-databricks
    - DD(
    - deepspeed-distributor-on-databricks
    - DDOD
    - torchdistributor-databricks
  citations:
    - file: distributed-training-databricks-on-aws.md
title: DeepSpeed Distributor
description: A Databricks distributed training solution built on TorchDistributor, using Microsoft's DeepSpeed library for optimized memory usage, reduced communication overhead, and advanced pipeline parallelism.
tags:
  - deep-learning
  - distributed-training
  - memory-optimization
timestamp: "2026-06-19T18:34:15.024Z"
---

# DeepSpeed Distributor

The **DeepSpeed Distributor** is a distributed training framework built on top of [TorchDistributor](/concepts/torchdistributor.md) that enables users to train large PyTorch models across multiple GPU nodes on a Databricks cluster. It is a recommended solution for workloads that require higher compute power but are limited by memory constraints. ^[distributed-training-databricks-on-aws.md]

## Overview

The DeepSpeed Distributor is part of the [DeepSpeed](/concepts/deepspeed.md) ecosystem, an open-source library developed by Microsoft that provides optimized memory usage, reduced communication overhead, and advanced pipeline parallelism. It is available in Databricks Runtime 10.4 ML and above. ^[distributed-training-databricks-on-aws.md]

Under the hood, the DeepSpeed Distributor uses TorchDistributor to initialize the environment and communication channels between workers, and it leverages the `torch.distributed.run` CLI command to execute distributed training across worker nodes. ^[distributed-training-databricks-on-aws.md]

## Key Features

- **Optimized memory usage**: Reduces the per-GPU memory footprint, enabling training of models that would otherwise exceed GPU memory limits. ^[distributed-training-databricks-on-aws.md]
- **Reduced communication overhead**: Improves scaling efficiency by minimizing the cost of gradient synchronization across workers. ^[distributed-training-databricks-on-aws.md]
- **Advanced pipeline parallelism**: Splits model layers across multiple devices to further reduce memory pressure and improve throughput. ^[distributed-training-databricks-on-aws.md]

## When to Use the DeepSpeed Distributor

The DeepSpeed Distributor is beneficial in the following scenarios: ^[distributed-training-databricks-on-aws.md]

- Low GPU memory available per worker.
- Training very large models (e.g., billions of parameters).
- Large input data, such as during batch inference.

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The underlying PySpark module that the DeepSpeed Distributor builds upon.
- [DeepSpeed](/concepts/deepspeed.md) – The open-source library that powers the memory and communication optimizations.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General strategies for training models across multiple machines.
- PyTorch – The deep learning framework used with the distributor.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime that includes the DeepSpeed Distributor package.

## Sources

- distributed-training-databricks-on-aws.md

# Citations

1. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
