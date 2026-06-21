---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cba5625641c2b3d37c280be00c9d880376478434f9cd14f3171a9211fd6a6999
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-gpu-workload-python-api
    - MWPA
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
    - file: 8xH100 Single-Node Configuration.md
title: Multi-GPU workload Python API
description: In-notebook Python API using `@distributed` and `@ray_launch` decorators as an alternative to the AI Runtime CLI for distributed training.
tags:
  - python-api
  - distributed-training
  - ray
  - notebook
timestamp: "2026-06-19T17:30:38.602Z"
---

## Multi-GPU Workload Python API

The **Multi-GPU workload Python API** provides in-notebook decorators and utilities for submitting distributed training workloads on Databricks serverless GPU compute. The API supports both the `@distributed` decorator (from the `serverless_gpu` library) and the `@ray_launch` decorator (for Ray-based workloads), allowing you to parallelize functions across multiple GPUs without leaving the notebook environment. ^[ai-runtime-cli-databricks-on-aws.md]

### `@distributed` decorator

The `@distributed` decorator is part of the `serverless_gpu` Python library. It enables you to run a function across multiple GPUs on a single node by spawning one process per GPU. The decorator accepts parameters such as `gpus` (number of GPUs) and `gpu_type` (e.g., `'h100'`). ^[8xH100 Single-Node Configuration.md]

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

* `rt.get_local_rank()` returns the rank of the GPU within the node (0-indexed).
* `rt.get_global_rank()` returns the global rank across all processes. ^[8xH100 Single-Node Configuration.md]

In the example above, the function runs on 8 processes, one per GPU. The result is a list of global ranks `[0, 1, 2, 3, 4, 5, 6, 7]`.

### `@ray_launch` decorator

The `@ray_launch` decorator is the Ray-based counterpart for distributed training. The source material does not provide specific implementation details for this decorator, but it is mentioned as an alternative in-notebook Python API for multi-GPU workloads. ^[ai-runtime-cli-databricks-on-aws.md]

### Runtime module

The `serverless_gpu.runtime` module provides utilities to coordinate distributed execution. The `get_local_rank()` and `get_global_rank()` functions help identify which GPU a process is running on and its position in the overall distributed job. ^[8xH100 Single-Node Configuration.md]

### Environment and prerequisites

To use the Multi-GPU workload Python API, you must select a **Serverless GPU** compute type in the notebook and choose an accelerator configuration (such as **8xH100**) with the **AI v5** environment. The AI v5 environment includes all required libraries for distributed GPU workloads. ^[8xH100 Single-Node Configuration.md]

### When to use the Python API vs. the CLI

The Python API is intended for in-notebook use when you want to write distributed training logic directly in Python. For laptop-based or YAML-defined workflows, use the [AI Runtime CLI](/concepts/ai-runtime-cli.md) instead. ^[ai-runtime-cli-databricks-on-aws.md]

### Related concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – Command-line alternative for submitting distributed training jobs.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The on-demand infrastructure that provisions GPU resources.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific configuration with eight H100 GPUs on one node.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – A common parallelism strategy that can be used with the Python API.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient training for very large models.

### Sources

- ai-runtime-cli-databricks-on-aws.md
- 8xH100 Single-Node Configuration.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
2. 8xH100 Single-Node Configuration.md
