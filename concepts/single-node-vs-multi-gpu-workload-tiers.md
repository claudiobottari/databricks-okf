---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08116e5960b3aa277c203078d62276d82b90077cb6608e3f72bbc4087a08f8c5
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-node-vs-multi-gpu-workload-tiers
    - SVMWT
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: Single-Node vs Multi-GPU Workload Tiers
description: Databricks distinguishes between single-node tasks (Public Preview) and multi-GPU distributed training (Beta), each with different stability and availability guarantees.
tags:
  - databricks
  - workload-management
  - gpu-computing
timestamp: "2026-06-19T18:18:47.234Z"
---

# Single-Node vs Multi-GPU Workload Tiers

**Single-Node vs Multi-GPU Workload Tiers** describes the two primary GPU compute scales offered by Databricks: workloads that run entirely on a single compute node (possibly using multiple GPUs within that node), and workloads that span multiple nodes through distributed training APIs. The choice between tiers depends on model size, memory requirements, and training parallelism strategy.

## Overview

Databricks provides distinct workload tiers optimized for different GPU compute scales. The **single-node tier** is designed for tasks that fit within the memory and compute of one node, while the **multi-GPU tier** (distributed training across nodes) is intended for models that exceed single-node capacity. Each tier has its own supported APIs and release maturity levels. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Single-Node Workload Tier

The single-node tier encompasses both single-GPU and multi-GPU configurations within a single compute node. Key characteristics:

- **AI Runtime** – The AI Runtime for single-node tasks is available in **Public Preview**. It provides a curated environment for GPU-accelerated workloads on a single node. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]
- **Multi-GPU on a single node** – Configurations such as the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) provision eight NVIDIA H100 GPUs (80 GB HBM3 each) on one node, offering 640 GB of total GPU memory. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Single-node distributed programming** – The `@distributed` decorator from the `serverless_gpu` library enables running functions across multiple GPUs on a single node, using local and global rank APIs for coordination. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Use cases** – Large model **training** that requires high FLOPS and large GPU memory but can be contained within one node (e.g., many [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) fine-tuning jobs). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Multi-GPU Workload Tier (Distributed Training)

The multi-GPU tier refers to training that spans **multiple nodes**, each potentially containing multiple GPUs. Key characteristics:

- **Distributed Training API** – The distributed training API for multi-GPU workloads is currently in **Beta**. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]
- **Scaling to very large models** – For models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range, single-node memory is insufficient. Frameworks such as [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) shard parameters, gradients, and optimizer states across GPUs, often requiring multi-node clusters. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **Advanced memory optimization** – When FSDP is not enough, alternatives like [DeepSpeed](/concepts/deepspeed.md) provide additional memory-saving features for multi-node training. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **Use cases** – Pre-training or fine-tuning models with 20 billion or more parameters, where even a single copy of model states exceeds one node’s GPU memory. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Comparison

| Aspect | Single-Node Tier | Multi-GPU (Multi-Node) Tier |
|---|---|---|
| **Release status** | AI Runtime: Public Preview | Distributed training API: Beta |
| **GPU count** | Up to 8 GPUs per node (e.g., 8xH100) | Arbitrary number of nodes × GPUs per node |
| **Memory per GPU** | Up to 80 GB (H100) | Same per GPU, but total is sum across nodes |
| **Parallelism strategy** | Single-process or `@distributed` for intra-node | FSDP, DeepSpeed, DDP across nodes |
| **Typical model size** | Up to ~20B parameters (depending on GPU memory) | 20B to 120B+ parameters |
| **Communication** | High-bandwidth NVLink within node | Network (e.g., InfiniBand) between nodes |
| **Best for** | Models that fit in node memory, rapid prototyping | Largest models, pre-training from scratch |

## Choosing a Workload Tier

- Use the **single-node tier** when your model and optimizer states can fit within the aggregate GPU memory of a single 8xH100 node (640 GB) and you want the simplicity of a single-node environment with the AI Runtime. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- Use the **multi-GPU tier** (distributed training across nodes) when the model exceeds single-node capacity or when you need to scale to hundreds of GPUs efficiently. Frameworks like FSDP are the standard choice for 20B to 120B+ parameter models. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- For workloads requiring the most advanced memory optimization (e.g., offloading, gradient checkpointing beyond FSDP), consider DeepSpeed within the multi-node tier. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – On-demand GPU resources that support both single-node and multi-node configurations.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific single-node multi-GPU setup.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – A simpler parallelism strategy for models that fit in a single GPU.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – The recommended approach for large models requiring memory sharding.
- [DeepSpeed](/concepts/deepspeed.md) – An alternative framework with advanced memory optimization features.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – The model size range where multi-node FSDP is typically required.

## Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
3. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
