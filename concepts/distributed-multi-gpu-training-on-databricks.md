---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed6ce82a9714da1b2cd68d59b3a181037b35d96e60ffd46fcae7437faf86f19f
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-multi-gpu-training-on-databricks
    - DMTOD
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: computer-vision-databricks-on-aws.md
title: Distributed Multi-GPU Training on Databricks
description: A Beta API in AI Runtime for distributing training workloads across multiple GPUs, separate from the single-node preview.
tags:
  - databricks
  - distributed-training
  - multi-gpu
  - beta
timestamp: "2026-06-19T17:49:21.691Z"
---

Here is the wiki page for "Distributed Multi-GPU Training on Databricks", based solely on the provided source material.

---

## Distributed Multi-GPU Training on Databricks

**Distributed Multi-GPU Training** on Databricks refers to the practice of scaling deep learning and large language model (LLM) training workloads across multiple Graphics Processing Units (GPUs) on a single node or across multiple nodes. This approach is essential for training models that are too large to fit into the memory of a single GPU.

### Overview

Databricks provides infrastructure and tools for distributed training across many GPUs. The primary methods for distributing training include [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) and [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), with FSDP being the preferred choice for very large models. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Infrastructure Options

Databricks offers multiple compute options for distributed multi-GPU training:

- **Serverless GPU Compute**: Provides on-demand GPU clusters. For example, the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) offers eight NVIDIA H100 80GB HBM3 GPUs on a single node, which is suitable for large model training. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Classic Compute**: Standard clusters with [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) and other GPU types for traditional distributed training setups. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Training Frameworks

#### Fully Sharded Data Parallel (FSDP)

FSDP is a strategy that shards model parameters, gradients, and optimizer states across the available GPUs, significantly reducing the per-GPU memory footprint. This technique is crucial for training models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

Key characteristics of FSDP in Databricks:
- It enables the training of models with 20 billion to over 120 billion parameters by overcoming single-GPU memory limitations. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- It offers a better trade-off for memory efficiency compared to standard DDP. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- It is the standard choice for training models that do not fit in a single GPU. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

#### Distributed Data Parallel (DDP)

DDP is a simpler but less memory-efficient approach. It is best suited for models that can fit within a single GPU's memory. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

#### `@distributed` Decorator (Serverless GPU)

For serverless GPU compute, the `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple GPUs on a single node. The `runtime` module provides access to local and global GPU ranks for coordinating work. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Multi-Node Training

Databricks supports multi-node distributed training where a workload is distributed across multiple compute nodes, each with multiple GPUs (e.g., multiple [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) nodes). This architecture is critical for scaling training to the largest model sizes. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Use Cases

- **Training large language models (LLMs)** such as those in the 20B to 120B+ parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **Memory-intensive deep learning training** tasks. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Object detection and image classification** using models like RetinaNet and YOLO11n. ^[computer-vision-databricks-on-aws.md]

### Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- GPU Scheduling

### Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- computer-vision-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
3. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
4. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
