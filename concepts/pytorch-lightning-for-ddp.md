---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b736ee18c944f5dacb6f0d9cd87fa33d50b26466e5a76f006737a73e60555fb
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-lightning-for-ddp
    - PLFD
    - PyTorch Lightning
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: PyTorch Lightning for DDP
description: A high-level interface that automatically handles DDP configuration for multi-GPU training
tags:
  - pytorch-lightning
  - distributed-training
  - high-level-api
timestamp: "2026-06-19T15:12:25.678Z"
---

# PyTorch Lightning for DDP

**PyTorch Lightning for DDP** refers to using the PyTorch Lightning high-level interface to implement [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training. PyTorch Lightning automatically handles DDP configuration for multi-GPU training, simplifying the distributed training workflow.

## Overview

PyTorch Lightning provides a high-level abstraction over PyTorch that automatically manages DDP configuration when training across multiple GPUs. This eliminates the need for manual DDP setup code, making distributed training more accessible and reducing boilerplate. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When to Use PyTorch Lightning for DDP

PyTorch Lightning for DDP is appropriate when:

- Your model fits completely in a single GPU's memory
- You want to scale training by increasing data throughput
- You need a simpler distributed training approach compared to manual DDP configuration
- You are building applications that benefit from PyTorch Lightning's built-in training loop management, checkpointing, and logging

For larger models that don't fit in single GPU memory, consider [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md) instead. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Use Case Example: Two-Tower Recommender System

A common use case for PyTorch Lightning with DDP is training a two-tower recommendation model. This approach is demonstrated on Databricks AI Runtime with serverless GPU resources, including data preparation using Mosaic Streaming (MDS) format and distributed training across A10 or H100 GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

The complete workflow includes:
- Data preparation and MDS format conversion
- Two-tower recommender training with PyTorch Lightning
- Automatic DDP configuration for multi-GPU training

## Advantages

PyTorch Lightning simplifies DDP training by:
- Automatically handling DDP initialization and process group setup
- Managing gradient synchronization across GPUs
- Providing built-in support for distributed samplers
- Integrating with logging and checkpointing systems
- Reducing the amount of boilerplate code required for distributed training

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The underlying parallelism technique that PyTorch Lightning wraps
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Alternative for models that don't fit in single GPU memory
- [DeepSpeed](/concepts/deepspeed.md) — Alternative with advanced memory optimization features
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) — The framework providing the high-level interface
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Infrastructure for running distributed GPU workloads
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Example hardware configuration for multi-GPU training
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — GPU support for deep learning workloads

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
