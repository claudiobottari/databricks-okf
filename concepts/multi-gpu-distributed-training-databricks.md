---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 488bdb0744018c5ad116af59e8a3993b06adc929ee6c22b92a79e745e8ea8c87
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-gpu-distributed-training-databricks
    - MDT(
    - Multi-GPU distributed training
    - Multi‑GPU distributed training
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Multi-GPU distributed training (Databricks)
description: Notebook examples for scaling training across multiple GPUs and nodes on Databricks using the Serverless GPU API.
tags:
  - databricks
  - distributed-training
  - multi-gpu
  - serverless-gpu
timestamp: "2026-06-19T22:04:44.729Z"
---

# Multi-GPU Distributed Training (Databricks)

**Multi-GPU Distributed Training (Databricks)** refers to scaling deep learning training workloads across multiple GPUs and compute nodes using the [AI Runtime](/concepts/ai-runtime.md)'s distributed training API and the [Serverless GPU API](/concepts/serverless-gpu-api.md). This approach enables practitioners to train large models that exceed the memory or compute capacity of a single GPU by distributing the workload across a cluster.

## Overview

Databricks provides a dedicated API for multi-GPU distributed training as part of the AI Runtime. The API supports scaling training jobs across multiple GPUs and nodes, enabling faster iteration and the ability to work with larger model sizes, batch sizes, and parameter counts. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

Example notebooks demonstrating multi-GPU distributed training are available in the Databricks documentation. These cover common scenarios such as training large language models, computer vision models, and deep learning-based recommender systems, as well as Classic ML tasks like XGBoost training and time series forecasting. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Status and Limitations

The distributed training API for multi-GPU workloads is currently in **Beta** status. In contrast, the AI Runtime for single-node tasks is in **Public Preview**. Users should expect potential changes, limited production support, and possible breaking changes while the API is in Beta. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Serverless GPU API

The multi-GPU distributed training examples use the [Serverless GPU API](/concepts/serverless-gpu-api.md) to provision and manage GPU resources. This API abstracts the underlying infrastructure, allowing users to focus on training logic rather than cluster configuration and resource management. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Hardware Configurations

For large-scale distributed training, Databricks offers configurations such as the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md), which provides eight NVIDIA H100 80GB HBM3 GPUs on a single node. This configuration delivers 640 GB of total GPU memory and substantial compute throughput for distributed training tasks. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Common Use Cases

- **Large Language Model Training**: Fine-tuning and pre-training large language models including parameter-efficient methods. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Computer Vision**: Object detection, image classification, and other vision tasks that benefit from distributed compute. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Recommender Systems**: Building recommendation systems using modern deep learning approaches like two-tower models. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Programming Model

The `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple GPUs. For single-node configurations, the `runtime` module provides access to local and global GPU ranks for coordinating work. For multi-node setups, additional orchestration handles communication across nodes. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The runtime environment that includes the distributed training API and example notebooks
- [Serverless GPU API](/concepts/serverless-gpu-api.md) — The API used to provision and launch multi-GPU training jobs
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concept of scaling training across multiple devices and nodes
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training strategy for very large models
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Common parallelism strategy for multi-GPU nodes
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) — Training scale that typically requires multi-GPU distributed approaches
- GPU Scheduling — Managing GPU resource allocation for distributed workloads
- Large Language Model Training — Common use case requiring multi-GPU distributed training

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
