---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94612a1500de1cf32597b28604ecbd33cee214f14531b929213152fc225ab4e8
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless_gpu-distributed-decorator
    - S@D
    - serverless_gpu.distributed decorator|@distributed
    - serverless-gpu-distributed-training-api
    - SGDTA
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: serverless_gpu @distributed decorator
description: A Python decorator from Databricks' serverless_gpu library that handles provisioning GPUs, setting up the distributed training environment, and managing the lifecycle of remote compute resources for multi-GPU training.
tags:
  - databricks
  - distributed-training
  - api
timestamp: "2026-06-18T12:07:33.514Z"
---

# `@distributed` Decorator (serverless_gpu)

The **`@distributed` decorator** is a function-level annotation from the `serverless_gpu` Python package that enables distributed training on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) in Databricks. It provisions GPU resources, sets up the distributed training environment, manages remote compute lifecycle, and executes the decorated function across the specified number of GPUs. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Overview

The `@distributed` decorator is designed to simplify running [multi-GPU training](/concepts/multi-gpu-distributed-training-api.md) workloads without manually managing cluster provisioning or distributed communication setup. When applied to a function, the decorator transforms it into a remote-execution callable with a `.distributed()` method that triggers execution on serverless GPU infrastructure. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Key Responsibilities

The `@distributed` decorator handles the following tasks automatically: ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

- **Resource provisioning**: Spins up the specified number of GPUs (e.g., 8 H100 GPUs) on serverless compute.
- **Environment setup**: Configures environment variables such as `RANK`, `WORLD_SIZE`, and `LOCAL_RANK` that distributed frameworks like [PyTorch FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) require.
- **Lifecycle management**: Tears down remote compute resources after the function completes or fails.
- **Remote execution**: Runs the decorated function on the provisioned infrastructure rather than the notebook's local driver.

## Basic Usage

### Import and Decorator Syntax

```python
from serverless_gpu import distributed
from serverless_gpu.compute import GPUType

@distributed(gpus=NUM_WORKERS, gpu_type=GPUType.H100)
def run_training(num_workers=8):
    # Training logic here
    ...
    return results
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `gpus` | `int` | The number of GPUs to allocate for the distributed job (e.g., `8` for 8 H100 GPUs) |
| `gpu_type` | `GPUType` | The GPU hardware type, drawn from the `GPUType` enum (e.g., `GPUType.H100`) |

### Triggering Remote Execution

After defining the decorated function, call its `.distributed()` method to launch the job:

```python
result = run_training.distributed()
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Practical Example: PyTorch FSDP Training

The following example demonstrates the decorator applied to a function that trains a Transformer model using [PyTorch Fully Sharded Data Parallel (FSDP)](/concepts/fsdp-fully-sharded-data-parallel.md): ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu.compute import GPUType

NUM_WORKERS = 8
CHECKPOINT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{MODEL_NAME}"

@distributed(gpus=NUM_WORKERS, gpu_type=GPUType.H100)
def run_fsdp_training(num_workers=NUM_WORKERS):
    """Self-contained FSDP training demo using PyTorch 2.0+

    Trains a simple neural network on synthetic data using FSDP
    """
    import mlflow
    mlflow.start_run(run_name='fsdp_example')

    def main_training():
        # Setup distributed training
        rank, world_size, device = setup()
        # ... model creation, FSDP wrapping, dataloader, training loop ...
        cleanup()
        mlflow.end_run()
        return { 'initial_loss': ..., 'final_loss': ..., ... }

    return main_training()
```

### Explicit Connection to Compute

Before running the decorated function, the notebook user must manually connect to serverless GPU compute:

1. Click the notebook's compute selector and select **Serverless GPU**.
2. On the right side, click the environment button.
3. Select **8xH100** as the **Accelerator**.
4. Choose **AI v5** environment (contains all required libraries).
5. Click **Apply**.

This step is performed once per notebook session, not per decorated function call. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Environment Variables for Distributed Setup

The decorator sets the following environment variables that the training code can inspect to initialize the distributed process group: ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

| Variable | Description |
|----------|-------------|
| `RANK` | Global rank of the current process (0-indexed) |
| `WORLD_SIZE` | Total number of processes across all nodes |
| `LOCAL_RANK` | Rank of the process on the current node |

These variables are used by the `setup()` function in the training code to initialize the communication backend:

```python
def setup():
    if 'RANK' in os.environ and 'WORLD_SIZE' in os.environ:
        rank = int(os.environ['RANK'])
        world_size = int(os.environ['WORLD_SIZE'])
        local_rank = int(os.environ.get('LOCAL_RANK', 0))
    else:
        rank = 0
        world_size = 1
        local_rank = 0

    if world_size > 1:
        if not dist.is_initialized():
            dist.init_process_group(backend='nccl', rank=rank, world_size=world_size)

    if torch.cuda.is_available():
        device = torch.device(f'cuda:{local_rank}')
        torch.cuda.set_device(device)
    else:
        device = torch.device('cpu')

    return rank, world_size, device
```

## Integration with Other Services

### [MLflow Tracking](/concepts/mlflow-tracking.md)

The decorated function can log metrics and artifacts with MLflow as part of the training run. In the example above, the decorator-wrapped function starts and ends an [MLflow Run](/concepts/mlflow-run.md), logs loss metrics per batch, and saves checkpoints as MLflow artifacts. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### [Unity Catalog](/concepts/unity-catalog.md) Volumes

Checkpoints and model files can be saved to Unity Catalog volumes using the `/Volumes/` path syntax within the decorated function. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### [PyTorch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md)

The decorator supports distributed checkpointing via `torch.distributed.checkpoint`, enabling saving and loading of [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md)-sharded model states across multiple GPUs. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Limitations

- The decorator is specific to Databricks serverless GPU compute; it does not work on classic clusters or other cloud platforms.
- GPU type is fixed per call (set via the `gpu_type` parameter); heterogeneous GPU configurations are not supported.
- The decorated function must be self-contained — all imports, helper functions, and data loading logic must be defined within the function body or be importable from the pre-installed environment (AI v5).

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The underlying infrastructure that the decorator provisions
- [PyTorch FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) — The distributed training strategy commonly used with this decorator
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) — The broader category of multi-GPU training techniques
- GPUType enum — The allowed GPU hardware types for serverless execution
- [Multi-GPU training on Databricks](/concepts/multi-gpu-distributed-training-on-databricks.md) — General overview of distributed training options

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
