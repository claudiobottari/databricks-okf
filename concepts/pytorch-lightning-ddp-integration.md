---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4a4551603133483de0cd9c3467eaa00860a60684c767cef4967ae29e4d64521
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-lightning-ddp-integration
    - PLDI
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: PyTorch Lightning DDP integration
description: PyTorch Lightning provides a high-level interface that automatically handles DDP configuration for multi-GPU training.
tags:
  - pytorch-lightning
  - distributed-training
  - framework
timestamp: "2026-06-19T18:32:13.432Z"
---

# PyTorch Lightning DDP Integration

**PyTorch Lightning DDP Integration** refers to the use of [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) to automatically configure [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training for multi-GPU workloads. PyTorch Lightning provides a high-level interface that handles DDP configuration, allowing you to scale distributed training without manually managing process groups or gradient synchronization. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## How It Works

Distributed Data Parallel (DDP) is the most common parallelism technique for distributed training. The full model is replicated on each GPU, and data batches are split across GPUs. PyTorch Lightning abstracts away the low-level DDP configuration—such as process group initialization, gradient all-reduce, and synchronization—so you only need to define the model, data modules, and trainer. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When to Use

Use PyTorch Lightning DDP when:

- Your model fits completely in a single GPU's memory.
- You want to scale training by increasing data throughput (simply adding more GPUs to process more data per step).
- You need the simplest distributed training approach with automatic support in most frameworks.

For larger models that do not fit in a single GPU, consider [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md) instead. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Example: Two-Tower Recommender System

The following notebook demonstrates how to train a two-tower recommendation model using PyTorch Lightning on [AI Runtime](/concepts/ai-runtime.md). PyTorch Lightning automatically handles DDP configuration for multi-GPU training across A10 GPU Support on Databricks|A10 or H100 GPU Support on Databricks|H100 GPUs. The example includes data preparation using [Mosaic Streaming (MDS) format](/concepts/mosaic-streaming-mds-format.md) and distributed training. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

For the complete notebook and related examples, see the [Deep learning recommendation examples](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-recommendation) page. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Key Benefits

- **Automatic configuration**: PyTorch Lightning handles DDP setup, including process group initialization and gradient synchronization, without manual intervention. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]
- **Simplified code**: You write standard PyTorch Lightning code (model, data modules, trainer) and the framework manages distributed training details. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]
- **Multi-GPU scaling**: Easily scale training across multiple GPUs for increased data throughput. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The underlying parallelism strategy
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) — The framework providing the high-level API
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Alternative for models that exceed single-GPU memory
- [DeepSpeed](/concepts/deepspeed.md) — Another alternative for large model training
- [Mosaic Streaming (MDS) format](/concepts/mosaic-streaming-mds-format.md) — Data format used in the example for efficient data loading
- [AI Runtime](/concepts/ai-runtime.md) — The Databricks runtime that supports GPU workloads
- A10 GPU Support on Databricks — GPU hardware available for distributed training
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — High-performance GPU configuration for distributed workloads
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) — Scale where FSDP becomes necessary over DDP

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
