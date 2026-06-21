---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f7d00155524fc27ee4d4a3a306978b59ddde06aa56fb09a21c1bd82977a2de7
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-api-for-distributed-training
    - SGAFDT
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Serverless GPU API for Distributed Training
description: A Databricks API for scaling machine learning training across multiple GPUs and nodes in a serverless manner, still in Beta.
tags:
  - databricks
  - distributed-training
  - gpu
timestamp: "2026-06-19T13:58:48.671Z"
---

Here is the wiki page for "Serverless GPU API for Distributed Training", written based solely on the provided source material.

---

## Serverless GPU API for Distributed Training

**Serverless GPU API for Distributed Training** is a Databricks API for scaling training workloads across multiple GPUs and nodes using the `serverless_gpu` Python library. The API provides a `@distributed` decorator and a `runtime` module that together allow users to run functions in parallel across multiple GPU processes on a single node or across multiple nodes. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

The distributed training API for multi-GPU workloads is currently in **Beta**. By contrast, [AI Runtime](/concepts/ai-runtime.md) for single-node tasks is in Public Preview. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

### Core Components

#### The `@distributed` Decorator

The `@distributed` decorator is used to mark a function for execution across multiple GPUs. It accepts parameters such as `gpus` (the number of GPU processes to spawn) and `gpu_type` (e.g., `'h100'`). When called with `.distributed(...)`, the decorator launches the function on each GPU process and collects the results. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

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

#### The `runtime` Module

The `runtime` module provides access to the rank of each process within a distributed job. Key functions include:

- `rt.get_local_rank()` — Returns the rank of the GPU within the current node.
- `rt.get_global_rank()` — Returns the global rank across all processes in the job.

These functions are used inside the distributed function body to coordinate work across GPUs. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Example Notebooks

Databricks provides several example notebooks demonstrating the Serverless GPU API for different tasks:

- **Multi-GPU distributed training** — Examples for scaling training across multiple GPUs and nodes.^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Large language models (LLMs)** — Fine-tuning LLMs including parameter-efficient methods.^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Computer vision** — Object detection and image classification.^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Deep learning based recommender systems** — Two-tower models and other modern approaches.^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Classic ML** — XGBoost training and time series forecasting.^[ai-runtime-example-notebooks-databricks-on-aws.md]

### Related Concepts

- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — A specific Serverless GPU configuration providing 8 H100 GPUs on one node.
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Scaling distributed training across multiple nodes.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — A memory-efficient parallelism strategy often used alongside the distributed API.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — A common parallelism strategy for multi-GPU training.
- [AI Runtime](/concepts/ai-runtime.md) — The runtime environment that includes the Serverless GPU API and pre-installed deep learning libraries.

### Sources

- ai-runtime-example-notebooks-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
