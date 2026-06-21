---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a2935d38000118501a827603396e6316b3b7dc531c1cb01d1e6bd4319f6edf88
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - 8xh100-single-node-configuration
    - 8SC
    - 8xH100 Single‑Node Configuration
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: 8xH100 Single-Node Configuration
description: A Databricks Serverless GPU configuration providing 8 H100 GPUs on a single node for distributed workloads
tags:
  - databricks
  - gpu
  - configuration
  - distributed-computing
timestamp: "2026-06-19T10:44:59.232Z"
---

# 8xH100 Single-Node Configuration

**8xH100 Single-Node Configuration** refers to a serverless GPU compute setup on Databricks that provisions eight NVIDIA H100 80GB HBM3 GPUs on a single compute node. This configuration is designed for large model training workloads that benefit from high floating-point operations per second (FLOPS) and high-bandwidth memory (HBM). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Overview

The 8xH100 single-node configuration is available through Databricks Serverless GPU compute. When selected, a notebook session connects to eight H100 GPUs running on a single node, providing 640 GB of total GPU memory (8 × 80 GB) and substantial compute throughput for distributed training tasks. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Selection

To use this configuration from a Databricks notebook:

1. From the compute selector, choose **Serverless GPU**.
2. In the **Environment** tab on the right panel, select **8xH100** for your accelerator.
3. Choose the **AI v5** environment, which contains all required libraries for running distributed GPU workloads.
4. Click **Apply**.

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Use Cases

H100 GPUs offer larger FLOPS and HBM compared to A10 GPUs. Use the 8xH100 configuration for large model **training** where high throughput and/or large GPU memory is needed. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

Typical workloads include:
- Large language model (LLM) training
- Multi-GPU distributed training jobs
- Memory-intensive deep learning training tasks

## Verification

Use the `nvidia-smi` command to confirm connection to eight H100 GPUs. Each GPU reports as an NVIDIA H100 80GB HBM3 with 81,559 MiB of total memory and a maximum power draw of 700 W. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Distributed Programming with the `@distributed` Decorator

The `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple GPUs on a single node. The `runtime` module provides access to local and global GPU ranks for coordinating work. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(
    gpus=8,
    gpu_type='h100',
)
def hello_world(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()

result = hello_world.distributed('SGC')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

- `gpus=8` specifies that the function runs on 8 processes, one per GPU.
- `rt.get_local_rank()` returns the rank of the GPU within the node.
- `rt.get_global_rank()` returns the global rank across all processes.

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute infrastructure that provisions GPU resources on demand.
- H100 GPU Support on Databricks — General availability and capabilities of H100 GPUs on the platform.
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Scaling beyond a single node by coordinating across multiple 8xH100 nodes.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Common parallelism strategy suited for 8xH100 nodes.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training for very large models.

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
