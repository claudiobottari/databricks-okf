---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c75f1e38487b59db42cbe6d1a6b4b83dc30b96475a4d7c4c76ae1deb08d7144f
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-ddp-on-databricks
    - PDOD
    - PyTorch DDP
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: PyTorch DDP on Databricks
description: Using PyTorch's torch.nn.parallel.DDP module to train a multilayer perceptron (MLP) on Databricks with serverless GPU resources.
tags:
  - pytorch
  - databricks
  - gpu-training
timestamp: "2026-06-18T15:28:24.588Z"
---

# PyTorch DDP on Databricks

**PyTorch DDP on Databricks** refers to using PyTorch's Distributed Data Parallel (DDP) module (`torch.nn.parallel.DistributedDataParallel`) to perform distributed training on Databricks clusters, particularly with serverless GPU resources. DDP is the most common parallelism technique for distributed training, where the full model is replicated on each GPU and data batches are split across GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Overview

PyTorch DDP enables efficient distributed training by synchronizing gradients across multiple GPUs. On Databricks, DDP training can leverage serverless GPU resources, including [A10 and H100 GPUs](/concepts/a100-gpu-support-on-databricks.md), through [AI Runtime](/concepts/ai-runtime.md). The framework handles process group initialization, gradient synchronization, and model parameter updates automatically. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When to Use DDP

DDP is appropriate for the following scenarios: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

- Your model fits completely in a single GPU's memory
- You want to scale training by increasing data throughput
- You need the simplest distributed training approach with automatic support in most frameworks

For larger models that do not fit in single GPU memory, consider [FSDP (Fully Sharded Data Parallel)](/concepts/20b-to-120b-parameter-model-training.md) or [DeepSpeed](/concepts/deepspeed.md) instead. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## How DDP Works

In DDP training, the complete model is replicated on each GPU. During each training step: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

1. Data batches are split across GPUs
2. Each GPU performs forward and backward propagation independently
3. Gradients are synchronized across all GPUs
4. Model parameters are updated identically on all GPUs

## Training Examples

### Simple Multilayer Perceptron (MLP) with PyTorch DDP

Databricks provides a notebook example demonstrating distributed training of a simple multilayer perceptron (MLP) neural network using PyTorch's DDP module on Databricks with serverless GPU resources. This example covers the core DDP setup, including process group initialization, model wrapping with `DistributedDataParallel`, and distributed data loading. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

### Two-Tower Recommender System with PyTorch Lightning

A second notebook example demonstrates how to train a two-tower recommendation model using [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) on AI Runtime. PyTorch Lightning provides a high-level interface that automatically handles DDP configuration for multi-GPU training. The example includes: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

- Data preparation using Mosaic Streaming (MDS) format
- Distributed training across A10 or H100 GPUs
- Complete two-tower recommender training workflow

See the [Deep learning recommendation examples](/concepts/deep-learning-based-recommender-systems.md) page for the complete notebooks. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Databricks Integration

Databricks [AI Runtime](/concepts/ai-runtime.md) includes optimized PyTorch builds and automatic DDP configuration for multi-GPU training. When using [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), the framework handles DDP setup automatically, reducing boilerplate code. Serverless GPU resources provide on-demand access to A10 and H100 GPUs without requiring dedicated cluster management. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Best Practices

- **Use PyTorch Lightning** for simpler DDP configuration and reduced boilerplate code
- **Prepare data in MDS format** for efficient streaming during distributed training
- **Choose appropriate GPU types** (A10 or H100) based on model size and throughput requirements
- **Monitor GPU utilization** to ensure efficient resource usage across all GPUs
- **Ensure model fits in single GPU memory** before using DDP; consider [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) for larger models

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concepts for training across multiple GPUs
- [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md) — Alternative for models that don't fit in single GPU memory
- [DeepSpeed](/concepts/deepspeed.md) — Microsoft's optimization library for large-scale distributed training
- [AI Runtime](/concepts/ai-runtime.md) — Databricks' optimized runtime for machine learning workloads
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) — High-level framework that simplifies DDP configuration
- GPU Clusters on Databricks — Infrastructure for GPU-accelerated training
- Serverless GPU Training — On-demand GPU resources for distributed training
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — GPU instance types available on Databricks

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
