---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2de80e86f63c5f0728ca58321a0b491dd0979611d19fa33bd13d6a20525a269d
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-distributed-decorator
    - D@D
    - databricks-distributed-decorator-for-multi-gpu-training
    - D@DFMT
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Databricks @distributed Decorator
description: A Python decorator in Databricks Serverless GPU Compute that orchestrates multi-GPU distributed training by launching a function across all GPUs with proper distributed setup.
tags:
  - databricks
  - distributed-training
  - orchestration
timestamp: "2026-06-19T18:52:27.738Z"
---

# Databricks `@distributed` Decorator

The **Databricks `@distributed` decorator** is a Python decorator from the `serverless_gpu` module that orchestrates distributed training across multiple GPUs on [Databricks Serverless GPU](/concepts/databricks-serverless-gpu.md) compute. It handles multi-GPU orchestration and compute allocation across connected serverless resources, enabling functions to execute in a distributed fashion across multiple GPUs simultaneously. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

The `@distributed` decorator is used to wrap training functions that require multi-GPU execution. It handles the low-level orchestration of distributed training across the connected serverless GPU compute resources, including distributed process launch, GPU binding, and communication setup. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Syntax

```python
from serverless_gpu import distributed

@distributed(gpus=<number>, gpu_type='<GPU model>')
def my_training_function():
    # Training logic here
    return result
```

### Parameters

- **`gpus`**: An integer specifying the number of GPUs to use for the distributed run. Common values include `8` for single-node training or higher numbers for multi-node configurations. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **`gpu_type`**: A string specifying the type of GPU. Supported values include `'H100'`, `'A100'`, or other GPU types available on the platform. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Usage Example

The decorator is used to wrap training functions that perform distributed training. The function is then called using the `.distributed()` method:

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def train_gpt_oss_fsdp_120b():
    # Imports inside the function for pickle safety
    import os, torch, torch.distributed as dist
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import SFTTrainer, SFTConfig
    from datasets import load_dataset
    from peft import LoraConfig, get_peft_model
    
    # DDP / CUDA binding
    local_rank = int(os.environ.get("LOCAL_RANK", "0"))
    torch.cuda.set_device(local_rank)
    
    # Training configuration
    # ... model loading, FSDP setup, training logic ...
    
    result = trainer.train()
    return result

# Execute the distributed training
train_gpt_oss_fsdp_120b.distributed()
```

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Requirements

- The decorated function must be defined in a notebook cell with access to [Serverless GPU Compute](/concepts/serverless-gpu-compute.md). ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- All imports required for the training logic must be placed **inside** the function body, as the decorator serializes and executes the function on remote GPU workers. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- Environment variables and configuration must be set within the function or passed via configuration objects, as the function executes in a separate process context. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Distributed Environment Variables

When the `@distributed` decorator launches a function, it sets standard distributed environment variables that the function can access:

- **`LOCAL_RANK`**: The rank of the GPU within the local node (0 to number of GPUs - 1). ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **`RANK`**: The global rank across all processes. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **`WORLD_SIZE`**: The total number of processes across all nodes. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

These variables are used for CUDA device binding and distributed process coordination:

```python
local_rank = int(os.environ.get("LOCAL_RANK", "0"))
torch.cuda.set_device(local_rank)
world_size = int(os.environ.get("WORLD_SIZE", "1"))
is_main = int(os.environ.get("RANK", "0")) == 0
```

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Use Cases

The `@distributed` decorator is commonly used for:

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) training of large language models with configurations like `fsdp="full_shard auto_wrap"`. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training for faster throughput across multiple GPUs. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) fine-tuning combined with FSDP for efficient training of models with 20B to 120B+ parameters. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- Multi-node distributed training by setting `gpus=16` or higher, extending training across multiple serverless GPU nodes. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The underlying compute infrastructure for distributed training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient sharding strategy often used with the decorator.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Parallelism strategy for distributing training across GPUs.
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) — Parameter-efficient fine-tuning technique.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Common GPU configuration used with the decorator.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) — Model scale range where this decorator is particularly useful.

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
