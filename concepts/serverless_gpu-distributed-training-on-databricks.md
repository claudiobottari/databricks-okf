---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dc41f3697338dd996be1c2e311fa7c5045bb10bce016f6c10dd09f00af80f7bc
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless_gpu-distributed-training-on-databricks
    - SDTOD
    - Serverless GPU Distributed Training on Databricks
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: serverless_gpu Distributed Training on Databricks
description: A Python library providing a @distributed decorator pattern for scaling LLM finetuning across multiple GPUs (e.g., 8×H100) on Databricks serverless compute.
tags:
  - distributed-training
  - databricks
  - gpu-compute
timestamp: "2026-06-19T18:33:24.911Z"
---

# serverless_gpu Distributed Training on Databricks

**serverless_gpu distributed training** refers to the use of the `serverless_gpu` Python library to run distributed training workloads across multiple GPUs on Databricks serverless compute. The library provides a simple decorator-based API that abstracts the orchestration of multi-GPU training, allowing users to scale fine-tuning and other training tasks without manually managing distributed infrastructure. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Overview

The `serverless_gpu` library is included in the Databricks AI v5 environment, which also contains supporting libraries such as [Unsloth](/concepts/unsloth.md), `unsloth_zoo`, `trl`, `peft`, `bitsandbytes`, `xformers`, and `einops`. No additional installation is required when using this environment. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Usage

### Import and Decorator

The primary entry point is the `@distributed` decorator from `serverless_gpu`. It is applied to a function that contains the training logic and accepts parameters such as `gpus` (number of GPUs) and `gpu_type` (e.g., `'h100'`). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='h100')
def run_train():
    # training code here
    pass
```

### Runtime Utilities

The `serverless_gpu.runtime` module provides helper functions for distributed execution. For example, `rt.get_global_rank()` returns the rank of the current process in the distributed job, which can be used to conditionally run operations (e.g., saving model checkpoints) only on the primary process. `rt.get_local_rank()` returns the rank of the GPU within the node. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from serverless_gpu import runtime as rt

if rt.get_global_rank() == 0:
    # save model only on rank 0
```

### Executing the Distributed Function

After defining the decorated function, it is invoked via the `.distributed()` method. The method launches the training across the specified GPUs and returns a list of results, one per distributed process. Typically, the result from the primary process (rank 0) is used. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
results = run_train.distributed()
primary_result = results[0]
```

### Environment and Device Setup

Within the distributed function, users set the local device using `torch.cuda.set_device(local_rank)`, where `local_rank` is obtained from the `LOCAL_RANK` environment variable set by the distributed runtime. This ensures each GPU process uses the correct device. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Configuration

To use serverless GPU compute from a Databricks notebook:

1. From the compute selector, choose **Serverless GPU**.
2. In the **Environment** tab, select the desired accelerator (e.g., **8xH100**).
3. Choose the **AI v5** base environment.
4. Click **Apply**.

The environment setup can take up to 8 minutes. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Example: Fine-Tuning Llama-3.2-3B

A typical use case is distributed fine-tuning of a large language model such as Llama 3.2-3B. In the Databricks notebook example, the `@distributed(gpus=8, gpu_type='h100')` decorator enables training across 8 H100 GPUs. The training function: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

1. Loads the model using [Unsloth](/concepts/unsloth.md) with `FastLanguageModel.from_pretrained()`.
2. Applies LoRA adapters via `FastLanguageModel.get_peft_model()`.
3. Enables gradient checkpointing with `use_reentrant=False` to avoid DDP conflicts.
4. Processes the dataset (e.g., "mlabonne/FineTome-100k") using chat template formatting.
5. Runs the [SFTTrainer](/concepts/sfttrainer.md) with MLflow logging (`report_to="mlflow"`).
6. Saves the trained model from rank 0 only.
7. Registers the model in [Unity Catalog](/concepts/unity-catalog.md).

## Distributed Programming with the `@distributed` Decorator

The `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple GPUs on a single node. When using an [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) with `gpus=8`, the function runs on 8 processes, one per GPU. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

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

## Key Features

- **Simple decorator API**: No need to manually set up Torch Distributed or [Horovod](/concepts/horovod.md).
- **GPU count and type specification**: Choose the number and type of GPUs (e.g., H100, A100) directly in the decorator.
- **Automatic process management**: The library spawns the required number of processes and handles communication.
- **Runtime utilities**: Access to global rank, local rank, and other distributed context via `serverless_gpu.runtime`.
- **Integration with MLflow and Unity Catalog**: Distributed training runs are automatically tracked when `report_to="mlflow"` is set in training arguments, and model artifacts can be saved from the primary process.
- **No additional installation**: The library is pre-installed in the Databricks AI v5 environment.

## Related Concepts

- [Unsloth](/concepts/unsloth.md) – Library for fast LLM fine-tuning with LoRA.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General concept of splitting workloads across multiple devices.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – Provides 8 H100 GPUs on a single node.
- H100 GPU – The GPU type used in the example.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Runtime that includes necessary dependencies.
- Fine-tuning – The task performed in the distributed training scenario.
- LoRA – Parameter-efficient fine-tuning method.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Alternative distributed training strategy for larger models.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Common parallelism strategy suited for multi-GPU training.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and model registration platform.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
