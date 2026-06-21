---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97014325beec78f6d6e87d65c2153bd6fbf44a6dbc92e17c2271fcd37e27409c
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alternatives-to-ddp-for-large-models
    - ATDFLM
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: Alternatives to DDP for large models
description: FSDP and DeepSpeed are alternatives to DDP when models do not fit in single GPU memory.
tags:
  - distributed-training
  - large-models
  - fsdp
  - deepspeed
timestamp: "2026-06-19T18:32:25.023Z"
---

# Alternatives to DDP for Large Models

**Alternatives to DDP for Large Models** are distributed training strategies designed for models that cannot fit entirely within a single GPU's memory. While [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) is the most common parallelism technique for distributed training — where the full model is replicated on each GPU and data batches are split across GPUs — it requires the model to fit completely in a single GPU's memory. For larger models that exceed this limitation, alternative approaches such as [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) and [DeepSpeed](/concepts/deepspeed.md) provide memory-efficient distributed training. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When DDP Is Insufficient

DDP is appropriate when your model fits completely in a single GPU's memory, you want to scale training by increasing data throughput, or you need the simplest distributed training approach with automatic support in most frameworks. However, when the model is too large to fit on a single GPU, DDP cannot be used because it requires replicating the entire model on each GPU. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Alternative Approaches

For larger models that do not fit in single GPU memory, Databricks recommends using FSDP or DeepSpeed instead of DDP. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

- **[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)** – A parallelism technique that shards model parameters, gradients, and optimizer states across multiple GPUs, enabling training of larger models.
- **[DeepSpeed](/concepts/deepspeed.md)** – A deep learning optimization library that provides memory and speed optimizations for large model training, including ZeRO (Zero Redundancy Optimizer).

These alternatives are supported on Databricks AI Runtime and can be used with serverless GPU resources. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Choosing the Right Approach

Select DDP when your model fits entirely on a single GPU and you want the simplest setup. Choose FSDP or DeepSpeed when your model is too large for a single GPU and you need to distribute memory across multiple devices. Both FSDP and DeepSpeed are available as alternatives in the Databricks environment. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP) Training](/concepts/distributed-data-parallel-ddp.md) – The standard approach for models that fit on a single GPU.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient sharding for large models.
- [DeepSpeed](/concepts/deepspeed.md) – Optimization library for large-scale training.
- GPU Training on Databricks – Overview of GPU-accelerated training options.
- Model Parallelism – Broader category of techniques for distributing model components.

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
