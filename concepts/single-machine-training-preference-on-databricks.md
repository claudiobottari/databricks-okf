---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb64779f177dce79cb29223edb2f2256c8f0f6ce1a83a51a01a1a03a70784a01
  pageDirectory: concepts
  sources:
    - distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-machine-training-preference-on-databricks
    - STPOD
  citations:
    - file: distributed-training-databricks-on-aws.md
title: Single-Machine Training Preference on Databricks
description: Databricks recommends training neural networks on a single machine when possible, as distributed training adds complexity and communication overhead
tags:
  - best-practice
  - training
  - performance
timestamp: "2026-06-19T10:16:15.844Z"
---

# Single-Machine Training Preference on Databricks

**Single-Machine Training Preference** refers to Databricks’ recommendation to train neural networks on a single machine when possible, due to the added complexity and communication overhead of distributed training.

## Overview

Databricks recommends training neural networks on a single machine whenever the model and data can fit in memory on that machine. Single-machine code is simpler to write and debug, and does not incur the communication overhead that slows down distributed training. ^[distributed-training-databricks-on-aws.md]

Distributed training and inference are inherently more complex than single-machine equivalents. The communication required to synchronize gradients or model parameters across multiple nodes adds latency and can reduce overall throughput, especially for smaller models. ^[distributed-training-databricks-on-aws.md]

## When to Prefer Single-Machine Training

- **Model fits in memory**: If a single GPU or machine can hold the model parameters, gradients, and optimizer states along with a reasonable batch of data, single-machine training is the straightforward choice.
- **Data fits in memory**: When the training dataset can be fully or efficiently loaded on one machine without requiring data parallelism across nodes.
- **Simpler development lifecycle**: Prototyping, debugging, and iteration are easier when the code runs on a single node. Distributed frameworks add complexity in environment setup, error handling, and reproducibility.

## When to Consider Distributed Training

Distributed training should be considered when the model or the data exceed the memory capacity of a single machine. Even then, Databricks provides purpose-built tools such as [TorchDistributor](/concepts/torchdistributor.md), [DeepSpeed Distributor](/concepts/deepspeed-distributor.md), and Ray to manage the complexity. ^[distributed-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) – Overview of available distributed training methods.
- [TorchDistributor](/concepts/torchdistributor.md) – PySpark module for distributed PyTorch training.
- [DeepSpeed Distributor](/concepts/deepspeed-distributor.md) – Memory-optimized distributed training using the DeepSpeed library.
- [Ray on Databricks](/concepts/ray-on-databricks.md) – Parallel compute framework for scaling ML workloads.
- Neural Networks – The primary class of models discussed in the context of this preference.
- GPU Memory Management – Understanding when model size exceeds single-GPU memory.

## Sources

- distributed-training-databricks-on-aws.md

# Citations

1. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
