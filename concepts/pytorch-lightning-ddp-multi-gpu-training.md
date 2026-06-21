---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12c80fd51ca921feb128fb8d5b21b1e0e3efe48611a78858443611ca43c29f62
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-lightning-ddp-multi-gpu-training
    - PLDMT
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: PyTorch Lightning DDP multi-GPU training
description: Using PyTorch Lightning's high-level interface that automatically handles DDP configuration for multi-GPU training on Databricks AI Runtime.
tags:
  - pytorch-lightning
  - distributed-training
  - databricks
timestamp: "2026-06-18T15:28:33.580Z"
---

# PyTorch Lightning DDP multi-GPU training

**PyTorch Lightning DDP multi-GPU training** refers to using the PyTorch Lightning high-level API to automate distributed data parallel (DDP) training across multiple GPUs on platforms such as Databricks. PyTorch Lightning abstracts away the boilerplate configuration of raw PyTorch DDP, allowing users to focus on model and data logic.

## Overview

PyTorch Lightning provides a high-level interface that automatically handles DDP configuration for multi-GPU training.^[distributed-data-parallel-ddp-training-databricks-on-aws.md] This means that instead of manually setting up process groups, synchronising gradients, and launching training processes with `torch.distributed`, a Lightning `Trainer` with the appropriate `accelerator` and `devices` arguments handles the distribution transparently.

Key aspects of PyTorch Lightning DDP on Databricks include:

- The framework automatically selects the DDP strategy when multiple GPUs are available.
- It is well-suited for models that fit within a single GPU’s memory but benefit from increased data throughput across multiple GPUs.
- It integrates with Databricks AI Runtime, which provides pre-configured PyTorch Lightning environments.

## Example use case: two-tower recommender system

A notebook example on Databricks demonstrates training a two-tower recommendation model using PyTorch Lightning on AI Runtime. The example includes data preparation using Mosaic Streaming (MDS) format and distributed training across A10 or H100 GPUs.^[distributed-data-parallel-ddp-training-databricks-on-aws.md] The complete notebooks are available on the Deep learning recommendation examples page.

## When to use PyTorch Lightning DDP

PyTorch Lightning DDP is appropriate when:

- Your model fits completely in a single GPU’s memory.
- You want to scale training by increasing data throughput with minimal code changes.
- You prefer a high-level API that abstracts distributed configuration.

For larger models that do not fit in a single GPU, consider [Fully Sharded Data Parallel (FSDP) training](/concepts/fully-sharded-data-parallel-fsdp.md) or DeepSpeed training instead.^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Related concepts

- [Distributed Data Parallel (DDP) Training](/concepts/distributed-data-parallel-ddp-training.md) – The underlying parallelism technique that Lightning abstracts.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – The framework providing the high-level trainer API.
- [AI Runtime](/concepts/ai-runtime.md) – The Databricks runtime that includes pre-installed deep learning libraries.
- [Fully Sharded Data Parallel (FSDP) training](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient alternative for larger models.
- DeepSpeed training – Another advanced alternative for very large models.

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
