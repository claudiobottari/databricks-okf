---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60c70c6bc9df861f0ea2a997e46f502d2422c416ab51810c931dc86af063f138
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless_gpuruntime-module
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: serverless_gpu.runtime Module
description: A runtime module within the serverless_gpu library that provides utilities like get_local_rank() and get_global_rank() for identifying GPU processes in a distributed setting.
tags:
  - python-runtime
  - gpu
  - distributed-computing
  - rank-identification
timestamp: "2026-06-19T18:59:53.598Z"
---

## serverless_gpu.runtime Module

The **`serverless_gpu.runtime`** module is a subpackage of the `serverless_gpu` Python library that provides runtime utilities for distributed GPU computing on Databricks Serverless GPU compute. It gives access to the distributed process context, including local and global GPU ranks, which are needed to coordinate work across multiple GPUs within a node or across nodes. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Functions

The module exposes two primary functions for determining process identity in a distributed job:

- **`get_local_rank()`** — Returns the rank (index) of the GPU within the current node. This is useful for node‑local operations such as printing or logging only on the rank‑0 GPU. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **`get_global_rank()`** — Returns the global rank of the process across all GPUs participating in the distributed job. This rank is unique across all nodes in a multi‑node setup. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Usage

The `runtime` module is typically used together with the serverless_gpu @distributed API|`@distributed`|serverless_gpu.distributed decorator. The decorator launches the annotated function on multiple GPU processes, and the runtime functions allow each process to identify itself and act accordingly.

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

In this example, only the process with local rank 0 prints the message, while every process returns its global rank, producing a list of all ranks from 0 to 7.

### Related Concepts

- [serverless_gpu](/concepts/serverless-gpu-compute.md) — The parent library for serverless GPU computing on Databricks.
- serverless_gpu @distributed decorator|serverless_gpu.distributed decorator|@distributed — The decorator used to launch distributed GPU functions.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — The hardware configuration used in the example.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The infrastructure that provisions GPU resources on demand.
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Scaling beyond a single node, where global rank becomes important.

### Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
