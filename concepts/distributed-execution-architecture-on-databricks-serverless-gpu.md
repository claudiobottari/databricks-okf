---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2fe0a4e70003121ffa3b0252bc12ea03e97ce59a7f4f9b85bc0f9469075ec246
  pageDirectory: concepts
  sources:
    - multi-gpu-workload-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-execution-architecture-on-databricks-serverless-gpu
    - DEAODSG
  citations:
    - file: multi-gpu-workload-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Distributed execution architecture on Databricks Serverless GPU
description: The underlying compute manager, runtime environment, and launcher components that orchestrate distributed training across multiple GPUs.
tags:
  - databricks
  - architecture
  - distributed-training
  - serverless-gpu
timestamp: "2026-06-19T19:48:35.704Z"
---

# Distributed Execution Architecture on Databricks Serverless GPU

The **Distributed execution architecture on Databricks Serverless GPU** describes how the platform coordinates multi-GPU workloads across a single node using the `serverless_gpu` Python API. The architecture is designed to abstract away the complexities of GPU provisioning, environment setup, and workload distribution, allowing users to move from single-GPU to multi-GPU distributed execution with minimal code changes. ^[multi-gpu-workload-databricks-on-aws.md]

## Core Components

The Serverless GPU distributed execution architecture consists of three key components: ^[multi-gpu-workload-databricks-on-aws.md]

- **Compute manager**: Handles resource allocation and management.
- **Runtime environment**: Manages Python environments and dependencies.
- **Launcher**: Orchestrates job execution and monitoring.

These components work together to serialize and distribute the user's function across the specified number of GPUs, synchronize the environment across all GPUs, collect results from all GPUs, and return them to the caller. ^[multi-gpu-workload-databricks-on-aws.md]

## The `@distributed` Decorator

The central abstraction in this architecture is the `@distributed` decorator from the `serverless_gpu` Python library. When applied to a function, the decorator transforms that function into the entrypoint for distributed execution — all training logic, data loading, and model initialization must be defined inside this decorated function. ^[multi-gpu-workload-databricks-on-aws.md]

### Parameters

The `@distributed` decorator accepts two key parameters: ^[multi-gpu-workload-databricks-on-aws.md]

- `gpus`: Specifies the number of GPUs to use (must be 8 for the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)).
- `gpu_type`: Must match the accelerator type the notebook is connected to (e.g., `'H100'`).

**Important**: The `gpu_type` parameter must exactly match the accelerator type your notebook is connected to. For example, `@distributed(gpus=8, gpu_type='H100')` requires your notebook to be connected to an H100 accelerator. Using a mismatched type (such as connecting to A10 while specifying H100) will cause the workload to fail. ^[multi-gpu-workload-databricks-on-aws.md]

## Execution Flow

When running in distributed mode, the architecture follows this sequence: ^[multi-gpu-workload-databricks-on-aws.md]

1. The user calls the distributed function (e.g., `run_train.distributed(...)`).
2. The function is serialized and distributed across 8 processes, one per GPU.
3. Each GPU runs a copy of the function with the same parameters.
4. The environment is synchronized across all GPUs.
5. Results are collected and returned from all GPUs.

Each process can access its local and global rank using the `runtime` module: `rt.get_local_rank()` returns the rank within the node, and `rt.get_global_rank()` returns the rank across all processes. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Supported Frameworks

The `@distributed` API integrates with major distributed training libraries: ^[multi-gpu-workload-databricks-on-aws.md]

- **[PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)** — Standard multi-GPU data parallelism.
- **[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)** — Memory-efficient training for large models.
- **[DeepSpeed](/concepts/deepspeed.md)** — Microsoft's optimization library for large model training.

## Comparison with TorchDistributor

The `serverless_gpu` API is the recommended approach for new deep learning workloads on Databricks. [TorchDistributor](/concepts/torchdistributor.md) remains available for workloads tightly coupled with Spark clusters. ^[multi-gpu-workload-databricks-on-aws.md]

## Data Loading Considerations

When using the distributed architecture, data loading code should be placed inside the `@distributed` decorator function. This is because the dataset size can exceed the maximum size allowed by pickle serialization, which is used to transfer data between processes. The recommended pattern is to generate or load the dataset inside the decorator. ^[multi-gpu-workload-databricks-on-aws.md]

For file-based data stored in Unity Catalog volumes, the `serverless_gpu` library provides `UCVolumeDataset` from `serverless_gpu.data`, which streams files with local caching and automatically partitions them across ranks and workers. For checkpointing distributed training to a volume, `UCVolumeWriter` and `UCVolumeReader` are available. ^[multi-gpu-workload-databricks-on-aws.md]

## Requirements

Distributed training requires an [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md), which provisions a single node with 8 H100 GPUs. The Serverless GPU API for distributed training is preinstalled when connected to a serverless GPU within Databricks notebooks and jobs. GPU environment 4 and above is recommended. ^[multi-gpu-workload-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The infrastructure that provisions GPU resources on demand.
- [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) — The runtime environment supporting GPU workloads.
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Scaling beyond a single node across multiple 8xH100 configurations.
- Model Checkpointing on Databricks — Saving and loading training state during distributed execution.

## Sources

- multi-gpu-workload-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [multi-gpu-workload-databricks-on-aws.md](/references/multi-gpu-workload-databricks-on-aws-c6af01f5.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
