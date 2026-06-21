---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6147e987872fcaed7a829c718ec04b26e7576e3c9188cd2ad4c6326fb4d5cb84
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-decorator
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: "@distributed Decorator"
description: A decorator from the serverless_gpu library that annotates functions to run across multiple GPUs, accepting parameters for GPU count and type.
tags:
  - python
  - decorator
  - distributed-computing
  - gpu
timestamp: "2026-06-19T19:00:20.514Z"
---

# @distributed Decorator

The **`@distributed` decorator** is a function-level annotation from the `serverless_gpu` Python library that enables seamless execution of GPU workloads directly from Databricks notebooks. It provides a declarative way to distribute a single function across multiple processes, one per GPU, on the node the notebook is attached to. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Overview

The decorator is used with [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) on Databricks, particularly with H100 accelerators. It is imported from the `serverless_gpu` package:

```python
from serverless_gpu import distributed
```

The decorated function must be called using the `.distributed()` method (e.g., `my_function.distributed(args)`) to execute the distributed workload. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Parameters

The `@distributed` decorator accepts two keyword arguments:

- **`gpus`** – The number of GPU processes to spawn. In the documented example, this is set to `8`.
- **`gpu_type`** – The GPU accelerator type. In the documented example, this is set to `'h100'`.

The combination of these parameters determines how the function is parallelised across the available GPUs. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Runtime Module

Inside the decorated function, the `serverless_gpu.runtime` module provides access to process ranks:

- `rt.get_local_rank()` returns the rank of the process within the current node (0‑indexed).
- `rt.get_global_rank()` returns the rank of the process across all nodes in the job.

These rank identifiers allow each process to perform distinct work and aggregate results. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Example

The following "Hello World" example demonstrates the decorator:

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
```

The distributed call returns a list of global ranks, one per process:

```python
assert result == [0, 1, 2, 3, 4, 5, 6, 7]
```

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Return Value

The return value of `function.distributed()` is a list where each element corresponds to the return value of one process. In the example above, each process returns its global rank, resulting in a list of integers from 0 to 7. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- serverless_gpu Python Library|serverless_gpu library – The package that provides the `@distributed` decorator and runtime utilities.
- H100 GPU – The recommended accelerator for large-scale training workloads using this decorator.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The Databricks compute environment that hosts H100 GPUs.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Broader topic of parallel model training across multiple GPUs.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific configuration using 8 H100 GPUs on a single node.

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
