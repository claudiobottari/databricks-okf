---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dfcb8b121bbce731d3e8bff4fa0ade2bf00744f0f1f627f7a9a4e7e63541b277
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ddp-applicability-criteria
    - DAC
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: DDP Applicability Criteria
description: "Conditions under which DDP is appropriate: model fits in single GPU memory, scaling data throughput is the goal, and simplest distributed approach is desired"
tags:
  - distributed-training
  - best-practices
timestamp: "2026-06-18T12:01:22.342Z"
---

# DDP Applicability Criteria

**Distributed Data Parallel (DDP) training** is a parallelism technique for distributed training where the full model is replicated on each GPU and data batches are split across GPUs. DDP is the most common parallelism technique for distributed training. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When to Use DDP

Use DDP when all of the following conditions are met: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

| Criterion | Description |
|----------|-------------|
| **Model fits in single GPU memory** | Your model fits completely in a single GPU's memory |
| **Goal is to scale data throughput** | You want to scale training by increasing data throughput |
| **Need simplest distributed approach** | You need the simplest distributed training approach with automatic support in most frameworks |

For larger models that do not fit in a single GPU's memory, consider alternative approaches such as [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md) instead. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## How DDP Works

DDP works by: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

- Replicating the full model on each GPU
- Splitting data batches across GPUs
- Synchronizing gradients across all GPUs during training

## Supported Frameworks

DDP provides automatic support in most frameworks, including: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

- [PyTorch DDP](/concepts/pytorch-ddp-on-databricks.md) — The native PyTorch module for distributed data parallel training
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) — A high-level interface that automatically handles DDP configuration for multi-GPU training

## Examples

### Training a Simple Multilayer Perceptron (MLP) Using PyTorch DDP

The following example demonstrates distributed training of a simple multilayer perceptron (MLP) neural network using PyTorch's DDP module on Databricks with serverless GPU resources: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

- **Notebook**: PyTorch DDP

### Training a Two-Tower Recommender System Using PyTorch Lightning

This example demonstrates how to train a two-tower recommendation model using PyTorch Lightning on [AI Runtime](/concepts/ai-runtime.md). PyTorch Lightning provides a high-level interface that automatically handles DDP configuration for multi-GPU training. The example includes: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

- Data preparation using Mosaic Streaming (MDS) format
- Distributed training across A10 or H100 GPUs

See the [Deep learning recommendation examples](/concepts/deep-learning-based-recommender-systems.md) page for the complete notebooks, including: ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

- Data preparation and MDS format conversion
- Two-tower recommender training with PyTorch Lightning

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — The broader category of training techniques that DDP belongs to
- [Data Parallelism](/concepts/data-parallelism-spark.md) — The parallelism strategy that DDP implements
- Model Parallelism — An alternative strategy for models that do not fit in single GPU memory
- [GPU Memory](/concepts/gpu-utilization-monitoring-dashboard.md) — The limiting factor that determines whether DDP is appropriate
- [Mosaic Streaming (MDS) format](/concepts/mosaic-streaming-mds-format.md) — A data format used in DDP training examples

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
