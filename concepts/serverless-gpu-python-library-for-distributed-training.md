---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe1b7dc0489685f382ec39301f674b45ebc220cc6de5991e9211dc64e0bff496
  pageDirectory: concepts
  sources:
    - multi-gpu-distributed-training-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-python-library-for-distributed-training
    - SGPLFDT
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: multi-gpu-distributed-training-databricks-on-aws.md
title: Serverless GPU Python Library for Distributed Training
description: A serverless GPU Python library on Databricks that simplifies distributed training workflows across multiple GPUs.
tags:
  - serverless
  - gpu
  - databricks
  - python
timestamp: "2026-06-19T19:47:52.462Z"
---

# Serverless GPU Python Library for Distributed Training

The **Serverless GPU Python Library** is a Python library provided by Databricks that enables distributed training on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md). It includes a `@distributed` decorator and a `runtime` module for coordinating work across multiple GPUs on a single node. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md] The library is intended for use with [Multi-GPU Distributed Training](/concepts/multi-gpu-distributed-training-api.md) workloads, and tutorial notebooks are available to help users get started. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Key Components

### The `@distributed` Decorator

The `@distributed` decorator from the `serverless_gpu` package allows a Python function to be executed in parallel across multiple GPUs on a single node. It accepts parameters to specify the number of GPUs and the GPU type. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='h100')
def my_function(name: str) -> list[int]:
    ...
```

- `gpus`: Number of processes to launch, typically one per GPU. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- `gpu_type`: The type of GPU to use (e.g., `'h100'`). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- The decorated function is called by invoking its `.distributed()` method. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### The `runtime` Module

The `serverless_gpu.runtime` module provides functions to query the rank of the current process, enabling coordination of work across GPUs. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

- `rt.get_local_rank()` – Returns the rank of the GPU within the node (0-indexed). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- `rt.get_global_rank()` – Returns the global rank across all processes. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Usage Example

The following example launches eight GPU processes, prints a message on rank 0, and returns a list of global ranks for all processes. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type='h100')
def hello_world(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()

result = hello_world.distributed('SGC')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

## Supported GPU Configurations

The library supports [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md), which provisions eight NVIDIA H100 80GB HBM3 GPUs on a single node. When using this configuration from a notebook, select the **Serverless GPU** compute type, **8xH100** accelerator, and **AI v5** environment. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Getting Started

Tutorials for the serverless GPU Python library are available in the Databricks documentation. These tutorials demonstrate how to use the library for [larger model training](/concepts/20b-to-120b-parameter-model-training.md) with [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) and [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) techniques on H100 GPUs. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Multi-GPU Distributed Training](/concepts/multi-gpu-distributed-training-api.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- H100 GPU Support on Databricks
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- multi-gpu-distributed-training-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
2. [multi-gpu-distributed-training-databricks-on-aws.md](/references/multi-gpu-distributed-training-databricks-on-aws-acaa7a08.md)
