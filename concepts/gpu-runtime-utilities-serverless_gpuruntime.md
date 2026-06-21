---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c5dffb51794a70e3256e163fc416b0404d892b65bb28bdab71cbc1f08fc3a86
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-runtime-utilities-serverless_gpuruntime
    - GRU(
    - GRU
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: GPU Runtime Utilities (serverless_gpu.runtime)
description: Runtime module providing get_local_rank() and get_global_rank() for managing multi-GPU process identity
tags:
  - gpu
  - runtime
  - distributed-computing
timestamp: "2026-06-19T10:44:50.578Z"
---

# GPU Runtime Utilities (serverless_gpu.runtime)

**GPU Runtime Utilities** refers to the `runtime` module within the `serverless_gpu` Python library, which provides functions for accessing GPU rank information during distributed execution on [Databricks Serverless GPU Compute](/concepts/databricks-serverless-gpu-compute.md). The module is imported as `from serverless_gpu import runtime as rt` and is used inside functions decorated with `@distributed` to identify which GPU process is executing. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Overview

The `serverless_gpu.runtime` module enables distributed GPU workloads to coordinate across multiple processes by exposing rank information. When a function is decorated with `@distributed(gpus=N)`, the runtime spawns one process per GPU. Each process can use the runtime utilities to determine its position within the distributed group, enabling conditional logic (e.g., only printing from rank 0) and result collection. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Key Functions

### `get_local_rank()`

Returns the local rank of the current GPU process within a single node. Local ranks are zero-indexed and correspond to the GPU index on the node. For example, on an 8-GPU node, local ranks range from 0 to 7. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### `get_global_rank()`

Returns the global rank of the current GPU process across all nodes in a multi-node distributed job. In a single-node configuration, global ranks are identical to local ranks. The function is commonly used to return ordered results from distributed execution. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Usage Pattern

The runtime utilities are used inside functions decorated with `@distributed`. The typical pattern is:

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type='h100')
def my_function(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()

result = my_function.distributed('SGC')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

In this example, the function runs on 8 processes (one per GPU). Only the process with local rank 0 prints a message, while all processes return their global rank. The collected results form an ordered list from 0 to 7. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- serverless_gpu @distributed API|@distributed Decorator (serverless_gpu.distributed) — The decorator that creates distributed GPU processes
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The underlying infrastructure for running GPU workloads
- H100 GPU Support on Databricks — GPU accelerator type commonly used with serverless GPU compute
- [Multi-GPU Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Advanced patterns for distributed model training
- [Serverless GPU API Documentation](/concepts/serverless-gpu-api.md) — Official API reference for the `serverless_gpu` library

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
