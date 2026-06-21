---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb2479a88a40b4e2b58a1510683ffdc4a5f3bc26bb2c7a22ae4f921762e9727d
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-ddp-implementation
    - PDI
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: PyTorch DDP Implementation
description: Using PyTorch's torch.nn.parallel.DistributedDataParallel module for distributed training of neural networks
tags:
  - pytorch
  - distributed-training
  - implementation
timestamp: "2026-06-19T15:12:24.550Z"
---

# PyTorch DDP Implementation

**PyTorch DDP (Distributed Data Parallel) Implementation** refers to the use of PyTorch's `torch.nn.parallel.DistributedDataParallel` module for distributed training on Databricks AI Runtime. DDP is the most common parallelism technique for distributed training, where the full model is replicated on each GPU and data batches are split across GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When to Use DDP

DDP is appropriate when:
- Your model fits completely in a single GPU's memory.
- You want to scale training by increasing data throughput.
- You need the simplest distributed training approach with automatic support in most frameworks.

For larger models that do not fit in a single GPU’s memory, consider [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md) instead. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Implementation Examples

Databricks provides notebook examples demonstrating DDP implementation on AI Runtime with serverless GPU resources.

### Training a Simple Multilayer Perceptron (MLP) Using PyTorch DDP

A notebook demonstrates distributed training of a simple MLP neural network using PyTorch's DDP module on Databricks with [Serverless GPU Compute](/concepts/serverless-gpu-compute.md). The example shows how to wrap a model with `DistributedDataParallel` and launch training across multiple GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

### Training a Two-Tower Recommender System Using PyTorch Lightning

This notebook illustrates how to train a two-tower recommendation model using [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), which provides a high-level interface that automatically handles DDP configuration for multi-GPU training. The example includes data preparation using [Mosaic Streaming (MDS)](/concepts/mosaic-streaming-mds-format.md) format and distributed training across A10 or H100 GPUs. For the complete notebooks, see the [Deep learning recommendation examples](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-recommendation) page. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Overview of the parallelism strategy.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient alternative for models exceeding single‑GPU memory.
- [DeepSpeed](/concepts/deepspeed.md) – Another advanced memory optimization library.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – High-level wrapper that simplifies DDP configuration.
- [AI Runtime](/concepts/ai-runtime.md) – Databricks runtime environment for machine learning workloads.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – On‑demand GPU infrastructure for distributed training.

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
