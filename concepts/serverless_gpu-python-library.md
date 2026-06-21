---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a45ba8c3462468f0d89ef3d5f1336644f61bdba3f45fa60caa48f8f6ea99ad03
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless_gpu-python-library
    - SPL
    - serverless_gpu (Python library)
    - serverless_gpu library
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: serverless_gpu Python Library
description: A first-party Databricks Python library that provides decorators and runtime utilities for executing distributed GPU workloads seamlessly from Databricks notebooks.
tags:
  - python-library
  - databricks
  - distributed-computing
  - api
timestamp: "2026-06-19T18:59:52.281Z"
---

# serverless_gpu Python Library

The **serverless_gpu** Python library provides decorators and runtime utilities for distributed GPU computing on Databricks Serverless GPU compute, enabling seamless execution of GPU workloads directly from Databricks notebooks.^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Overview

The `serverless_gpu` library simplifies distributed GPU programming on Databricks by allowing users to run functions across multiple GPUs with minimal code changes, handling the underlying parallelism and resource management. The library is designed to work with Serverless GPU compute configurations, such as the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md).^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Core Components

### `@distributed` Decorator

The `@distributed` decorator is the primary mechanism for executing functions across multiple GPUs. It annotates a function to run on a specified number of processes, one per GPU on the node.^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

**Parameters:**
- `gpus` (int): Number of GPUs to use
- `gpu_type` (str): Type of GPU accelerator (e.g., `'h100'`)

**Example:**
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

### `runtime` Module

The `runtime` module provides utilities for accessing GPU rank information within distributed functions:^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

- `rt.get_local_rank()`: Returns the rank of the current process within the node (0-indexed). Used for coordinating node-local operations such as printing or logging.
- `rt.get_global_rank()`: Returns the global rank across all processes in the distributed job.

## Distributed Execution Model

When a function decorated with `@distributed` is called via `.distributed()`, it runs across the specified number of processes. Each process executes the function body independently, with access to its own GPU. The runtime module enables process coordination through rank identifiers.^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Configuration

To use the library, you must configure your Databricks compute:^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

1. Select **Serverless GPU** from the compute selector
2. Choose an accelerator (e.g., **8xH100** for 8 H100 chips on a single node)
3. Select an appropriate environment (e.g., **AI v5**) that includes the required libraries
4. Click **Apply**

## Use Cases

- **Large model training**: H100 GPUs are recommended for large model training where high throughput and large GPU memory are needed. For models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range, consider combining with frameworks like [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md).^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Distributed inference**: Running inference across multiple GPUs for latency-sensitive or high-throughput workloads.
- **Parallel computation**: Any GPU-accelerated workload that benefits from partitioning across multiple devices.

## Related Concepts

- Distributed GPU Programming – General patterns for multi-GPU computing
- H100 GPU Support on Databricks – Hardware capabilities and recommendations
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The underlying compute infrastructure
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Alternative approach for model-parallel training
- [AI Runtime on Databricks](/concepts/ai-runtime-on-databricks.md) – Runtime environments with GPU support
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – The compute configuration commonly used with this library

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
