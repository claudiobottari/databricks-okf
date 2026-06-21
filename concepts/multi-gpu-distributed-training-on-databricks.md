---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 130be475d05a4efd13b708b4d4be3402c59b0b474428495a16102b03882b3b80
  pageDirectory: concepts
  sources:
    - multi-gpu-distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-gpu-distributed-training-on-databricks
    - MDTOD
    - Multi-GPU Training on Databricks
    - Multi-GPU training on Databricks
  citations:
    - file: multi-gpu-distributed-training-databricks-on-aws.md
title: Multi-GPU Distributed Training on Databricks
description: Scaling model training across multiple GPUs and nodes using Databricks AI Runtime, with support for H100 GPUs, parallelism techniques (DDP, FSDP, DeepSpeed), and serverless GPU Python library tutorials.
tags:
  - distributed-training
  - databricks
  - gpu
timestamp: "2026-06-19T19:47:29.730Z"
---

# Multi-GPU Distributed Training on Databricks

**Multi-GPU distributed training on Databricks** uses the [AI Runtime](/concepts/ai-runtime.md) to scale deep learning model training across multiple GPUs and nodes, improving performance for large-scale workloads. The approach is particularly suited for models that exceed the memory capacity of a single GPU. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Supported Hardware

Multi-GPU distributed training on Databricks is supported on H100 GPU Support on Databricks|H100 GPUs. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Parallelism Techniques

Choosing the right parallelism technique depends on the model size, available GPU memory, and performance requirements. Databricks documentation provides detailed guidance for the following techniques:

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)

Each technique has dedicated example notebooks and documentation to help users select and implement the appropriate strategy. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Example Notebooks

The Databricks documentation includes example notebooks organized by the framework or library used and the parallelism technique applied. These notebooks demonstrate how to configure and run multi-GPU distributed training across multiple nodes. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Getting Started

To begin with multi-GPU distributed training, Databricks provides tutorials that use the serverless GPU Python library. These tutorials walk through the process of setting up and running distributed training jobs on serverless GPU compute. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- H100 GPU Support on Databricks
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)

## Sources

- multi-gpu-distributed-training-databricks-on-aws.md

# Citations

1. [multi-gpu-distributed-training-databricks-on-aws.md](/references/multi-gpu-distributed-training-databricks-on-aws-acaa7a08.md)
