---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 523b17c9273c13b348f4920fd95266634cccd7992823ff7e3c072525d65e4676
  pageDirectory: concepts
  sources:
    - multi-gpu-distributed-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ddp-distributed-data-parallel-on-databricks
    - D(DPOD
  citations:
    - file: multi-gpu-distributed-training-databricks-on-aws.md
title: DDP (Distributed Data Parallel) on Databricks
description: A parallelism technique for multi-GPU training that replicates the model on each GPU and synchronizes gradients across devices.
tags:
  - parallelism
  - deep-learning
  - databricks
timestamp: "2026-06-19T19:47:20.155Z"
---

# DDP (Distributed Data Parallel) on Databricks

**DDP (Distributed Data Parallel)** is a parallelism technique for scaling deep learning model training across multiple GPUs on Databricks. It replicates the entire model on each GPU, with each GPU processing a different subset of the training data, and synchronizes gradients across all GPUs during the backward pass. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Overview

DDP is one of several parallelism techniques available for multi-GPU distributed training on Databricks. It is best suited for models that fit entirely within a single GPU's memory, as each GPU maintains a complete copy of the model parameters, gradients, and optimizer states. ^[multi-gpu-distributed-training-databricks-on-aws.md]

The choice between DDP and other techniques depends on your model size, available GPU memory, and performance requirements. For models that fit in a single GPU, DDP offers a simpler implementation compared to more advanced techniques like [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Supported Hardware

Multi-GPU distributed training on Databricks is supported on H100 GPUs. This includes configurations such as the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) which provides eight H100 GPUs on a single node. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Comparison with Other Techniques

| Technique | Best For | Key Characteristic |
|-----------|----------|-------------------|
| DDP | Models that fit in a single GPU | Replicates entire model on each GPU |
| FSDP | Models that don't fit in a single GPU | Shards model parameters across GPUs |
| DeepSpeed | Advanced memory optimization needs | Additional optimization strategies |

^[multi-gpu-distributed-training-databricks-on-aws.md]

## When to Use DDP

DDP is appropriate when:
- Your model fits within a single GPU's memory
- You want a simpler implementation compared to FSDP or DeepSpeed
- You are scaling training across multiple GPUs for faster throughput

For models exceeding single-GPU memory capacity, consider [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md) instead. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Getting Started

Databricks provides example notebooks demonstrating DDP implementation. These examples show how to scale training across multiple GPUs and nodes for improved performance. The [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) Python library provides a `@distributed` decorator for running functions across multiple GPUs. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- H100 GPU Support on Databricks
- [Multi-GPU Distributed Training](/concepts/multi-gpu-distributed-training-api.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)

## Sources

- multi-gpu-distributed-training-databricks-on-aws.md

# Citations

1. [multi-gpu-distributed-training-databricks-on-aws.md](/references/multi-gpu-distributed-training-databricks-on-aws-acaa7a08.md)
