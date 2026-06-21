---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f69b11918f8282fb295d2e731192075c4bced13af78495b9391d901afc4d32da
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nvidia-h100-gpu-on-databricks
    - NHGOD
    - NVIDIA H100
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: NVIDIA H100 GPU on Databricks
description: The NVIDIA H100 80GB HBM3 accelerator available as a serverless GPU option on Databricks, offering 8 chips per node with 80GB memory each for large model training.
tags:
  - nvidia
  - h100
  - hardware
  - gpu-accelerator
timestamp: "2026-06-19T18:59:53.633Z"
---

# NVIDIA H100 GPU on Databricks

**NVIDIA H100 GPU on Databricks** refers to the availability and usage of NVIDIA H100 80GB HBM3 graphics processing units through Databricks Serverless GPU compute. These GPUs provide high floating-point operations per second (FLOPS) and high-bandwidth memory (HBM), making them suitable for large model training workloads. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Overview

The H100 GPU is available on Databricks as part of the [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) offering. Each H100 GPU has 81,559 MiB (approximately 80 GB) of HBM3 memory and a maximum power draw of 700 W. The standard single-node configuration provides 8 H100 GPUs on one compute node, delivering 640 GB of total GPU memory for distributed training tasks. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Configuration

### Selecting H100 GPUs

To use H100 GPUs from a Databricks notebook:

1. From the compute selector, choose **Serverless GPU**.
2. In the **Environment** tab on the right panel, select **8xH100** for your accelerator.
3. Choose the **AI v5** environment, which contains all required libraries for running GPU workloads.
4. Click **Apply**.

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Use Cases

Compared to A10 GPUs, H100s offer larger FLOPS and HBM. Use H100 GPUs for large model **training** where high throughput and/or large GPU memory is needed. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Distributed Programming

The `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple H100 GPUs on a single node. The `runtime` module provides access to local and global GPU ranks for coordinating work. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

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

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

- `gpus=8` specifies that the function runs on 8 processes, one per GPU.
- `rt.get_local_rank()` returns the rank of the GPU within the node.
- `rt.get_global_rank()` returns the global rank across all processes.

## Verification

Use the `nvidia-smi` command to confirm connection to H100 GPUs. Each GPU reports as an NVIDIA H100 80GB HBM3 with 81,559 MiB of total memory and a maximum power draw of 700 W. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — The standard configuration providing 8 H100 GPUs on one node.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute infrastructure that provisions GPU resources on demand.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient distributed training for large models on H100 GPUs.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) — Model scale range that benefits from H100 GPU memory and throughput.
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Scaling beyond a single node by coordinating across multiple 8xH100 nodes.

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
