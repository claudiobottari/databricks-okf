---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4db0e5786ef0542b13954d5eeeedb05bee105a83b1675a56a2dc7047c44811a
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
    - distributed-training-using-deepspeed-databricks-on-aws.md
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-data-parallel-ddp
    - DDP(
    - Data Distributed Parallel (DDP)
    - Distributed Data Parallel
    - Distributed Data Parallelism
    - Distributed Data Parallelism (DDP)
    - DistributedDataParallel
    - DistributedDataParallel (DDP)
    - PyTorch Distributed Data Parallel (DDP)
    - PyTorch distributed data parallel (DDP)
    - distributed data parallelism
    - DDP (Distributed Data Parallel)
    - Distributed Data Parallel|Distributed Data Parallel (DDP)
    - PyTorch Distributed Data Parallel
    - PyTorch DistributedDataParallel
    - Synchronous Data Parallelism
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: Distributed Data Parallel (DDP)
description: A parallelism technique for distributed training where the full model is replicated on each GPU and data batches are split across GPUs.
tags:
  - distributed-training
  - pytorch
  - parallelism
timestamp: "2026-06-19T18:31:58.711Z"
---

# Distributed Data Parallel (DDP)

**Distributed Data Parallel (DDP)** is the most common parallelism technique for distributed training of deep learning models. In DDP, the full model is replicated on each GPU, and data batches are split across GPUs for parallel processing. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When to Use DDP

Use DDP when: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

- Your model fits completely in a single GPU’s memory.
- You want to scale training by increasing data throughput.
- You need the simplest distributed training approach with automatic support in most frameworks (e.g., PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)).

For larger models that do not fit in a single GPU’s memory, consider [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md) instead. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Examples

The following notebook examples demonstrate DDP training on Databricks [AI Runtime](/concepts/ai-runtime.md) using serverless GPU resources. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

### Training a Simple Multilayer Perceptron (MLP) with PyTorch DDP

This notebook trains a simple multilayer perceptron (MLP) neural network using PyTorch’s `DistributedDataParallel` module. The model is small enough to fit entirely on each GPU, making DDP the natural choice for scaling by increasing batch size. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

### Training a Two-Tower Recommender System with PyTorch Lightning

[PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) provides a high-level interface that automatically handles DDP configuration for multi-GPU training. This notebook trains a two-tower recommendation model on AI Runtime, including data preparation in [Mosaic Streaming (MDS)](/concepts/mosaic-streaming-mds-format.md) format and distributed training across A10 GPUs or H100 GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – For models too large to fit in a single GPU; offers more memory efficiency than DDP. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- [DeepSpeed](/concepts/deepspeed.md) – Advanced memory optimization with ZeRO stages for large language models (1B to 100B+ parameters). ^[distributed-training-using-deepspeed-databricks-on-aws.md]
- [Data Parallelism](/concepts/data-parallelism-spark.md) – The general technique of distributing data across replicas.
- Model Parallelism – Splitting the model across GPUs instead of replicating it.
- Distributed Training Strategies – Comparison of parallelism techniques.
- [Serverless GPU](/concepts/serverless-gpu-compute.md) – On-demand GPU resources for DDP training on Databricks.

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- distributed-training-using-deepspeed-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
