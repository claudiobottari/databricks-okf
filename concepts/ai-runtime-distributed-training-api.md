---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0e560e66fdd3a751989a0e76d19e7ef1e113a12308bf3aa0b3c45aff97e78527
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
    - user-guides-for-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ai-runtime-distributed-training-api
    - ARDTA
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Distributed Training API
description: A Beta API using the @distributed decorator for multi-GPU workloads on single-node AI Runtime with PyTorch DDP, FSDP, or DeepSpeed.
tags:
  - distributed-training
  - api
  - deep-learning
timestamp: "2026-06-19T13:57:51.093Z"
---

# AI Runtime Distributed Training API

The **AI Runtime Distributed Training API** (currently in **Beta**) is a high‑level Python API that enables multi‑GPU distributed training on a single [AI Runtime](/concepts/ai-runtime.md) node. ^[ai-runtime-databricks-on-aws.md]

By applying the `@distributed` decorator from the `serverless_gpu` Python package, you can launch workloads that use [PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), [PyTorch Fully Sharded Data Parallel (FSDP)](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md), or [DeepSpeed](/concepts/deepspeed.md) with minimal configuration — no need to manually set up a distributed launcher or manage cluster processes. ^[ai-runtime-databricks-on-aws.md]

## Availability and scope

This API is designed for single‑node, multi‑GPU scenarios. The node your notebook or job is connected to determines the GPU count; the API distributes the workload across all GPUs on that node. ^[ai-runtime-databricks-on-aws.md]

The feature is in **Beta** and requires that a workspace admin enable the **AI Runtime Beta Feature** preview from the **Previews** page. See Manage Databricks previews. ^[ai-runtime-databricks-on-aws.md]

## How it works

The `@distributed` decorator wraps a training function so that it runs on every GPU of the current node, passing the appropriate `rank`, `world_size`, `local_rank`, and `master_addr`/`master_port` environment variables that torchrun or DeepSpeed launcher expect. ^[ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed
def train():
    # Your training code here
    # The decorator sets up distributed process group and ranks
    pass
```

Calling the decorated function launches the function on each GPU with the correct process group configuration. ^[ai-runtime-databricks-on-aws.md]

## Supported frameworks

| Framework | Example use case |
|---|---|
| [PyTorch DDP](/concepts/pytorch-ddp-on-databricks.md) | Data‑parallel training with one GPU per process |
| [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) | Fully sharded data parallel training for large models |
| [DeepSpeed](/concepts/deepspeed.md) | ZeRO‑stage 1/2/3, mixed‑precision training |

All three frameworks work via the same `@distributed` entry point; the API does not require you to choose a launcher upfront. ^[ai-runtime-databricks-on-aws.md]

## Integration with AI Runtime

The training function runs on the AI Runtime node's GPU(s) and can read data from [Unity Catalog](/concepts/unity-catalog.md) volumes, log metrics to [MLflow](/concepts/mlflow.md), and write checkpoints back to the workspace’s DBFS root or a Unity Catalog volume. ^[ai-runtime-databricks-on-aws.md]

## Limitations

- The API is **single‑node only**. Multi‑node distributed training (e.g., across two or more separate nodes) is not supported by this decorator. ^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for a single workload is **seven days**. For longer training, implement checkpointing and restart the job. ^[ai-runtime-databricks-on-aws.md]
- Only A10 and H100 accelerators are supported. ^[ai-runtime-databricks-on-aws.md]
- Cross‑region GPU capacity may be used during high demand, which can incur egress costs and limit network connectivity. ^[ai-runtime-databricks-on-aws.md]

## Related concepts

- [AI Runtime](/concepts/ai-runtime.md) – the underlying compute offering providing GPU support for serverless Databricks
- [PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – a framework‑level data‑parallel strategy
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – a sharded data‑parallel strategy for large model memory efficiency
- [DeepSpeed](/concepts/deepspeed.md) – a Microsoft‑developed optimization library for large‑scale training
- torchrun – the standard PyTorch distributed launcher used under the hood
- [Unity Catalog](/concepts/unity-catalog.md) – the governance layer for storing training datasets and model checkpoints
- [MLflow](/concepts/mlflow.md) – experiment tracking integrated with AI Runtime

## Sources

- ai-runtime-databricks-on-aws.md
- user-guides-for-ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
