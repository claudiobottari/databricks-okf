---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57400e92b57aa836b1f806bfb20df00514b064f2f77fb79d8153d3b687a3d66d
  pageDirectory: concepts
  sources:
    - multi-gpu-distributed-training-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - choosing-parallelism-techniques-for-multi-gpu-training
    - CPTFMT
  citations:
    - file: multi-gpu-distributed-training-databricks-on-aws.md
title: Choosing Parallelism Techniques for Multi-GPU Training
description: The process of selecting between DDP, FSDP, and DeepSpeed based on model size, GPU memory capacity, and performance requirements.
tags:
  - best-practices
  - parallelism
  - optimization
timestamp: "2026-06-19T19:47:26.974Z"
---

# Choosing Parallelism Techniques for Multi-GPU Training

When scaling model training across multiple GPUs, selecting the right parallelism technique is critical. The choice depends on the model size, available GPU memory, and performance requirements. The three primary techniques are [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), and [DeepSpeed](/concepts/deepspeed.md). ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Parallelism Techniques

### Distributed Data Parallel (DDP)

DDP replicates the entire model on each GPU. Each GPU processes a different batch of data and synchronizes gradients across all GPUs. This technique is best suited for models that fit entirely into a single GPU’s memory. It offers simplicity and high efficiency when the model size does not exceed the per-GPU memory limit. ^[multi-gpu-distributed-training-databricks-on-aws.md]

### Fully Sharded Data Parallel (FSDP)

FSDP shards the model parameters, gradients, and optimizer states across GPUs. This dramatically reduces the memory footprint per GPU, enabling training of larger models than would be possible with DDP. FSDP is the recommended approach for models in the 20B to 120B+ parameter range. ^[multi-gpu-distributed-training-databricks-on-aws.md]

### DeepSpeed

DeepSpeed provides advanced memory optimization strategies beyond FSDP, such as ZeRO stages and gradient checkpointing. It is considered when more sophisticated memory optimization features are required. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Supported Hardware

Multi-GPU distributed training is supported on **H100 GPUs** on Databricks. These GPUs offer larger FLOPS and high-bandwidth memory (HBM) suitable for distributed workloads. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Getting Started

Use the serverless GPU Python library to run distributed training workloads on Databricks. The library provides a `@distributed` decorator for launching functions across multiple GPUs on a single node, with access to local and global ranks for coordination. ^[multi-gpu-distributed-training-databricks-on-aws.md]

For detailed documentation on each technique, refer to the following pages:
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)

## Related Concepts

- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A common configuration for multi-GPU training on Databricks.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – The parameter range where FSDP is particularly useful.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The infrastructure that provisions GPU resources on demand.

## Sources

- multi-gpu-distributed-training-databricks-on-aws.md

# Citations

1. [multi-gpu-distributed-training-databricks-on-aws.md](/references/multi-gpu-distributed-training-databricks-on-aws-acaa7a08.md)
