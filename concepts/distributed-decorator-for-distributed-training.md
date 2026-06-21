---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee32759f3db67551650dd9d0812da3940c06d46f30e06777f734ae32bb063dcf
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-decorator-for-distributed-training
    - "@DFDT"
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
title: "@distributed decorator for distributed training"
description: A Python decorator from the serverless_gpu library that handles data parallelism across multiple GPUs, automatically managing rank, local rank, and world size environment variables.
tags:
  - databricks
  - distributed-training
  - decorator
  - python
timestamp: "2026-06-19T10:15:00.012Z"
---

# @distributed Decorator for Distributed Training

The **`@distributed` decorator** is a Python decorator from the `serverless_gpu` library that enables seamless distributed training across multiple GPUs on Databricks serverless GPU compute. It provisions GPU resources on-demand and handles data parallelism automatically, allowing data scientists to scale training workloads without manually managing distributed training infrastructure. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Overview

The `@distributed` decorator abstracts away the complexity of setting up distributed training environments. When applied to a training function, it automatically provisions the specified number of GPUs, initializes the distributed communication backend, and handles data parallelism across all available devices. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Usage

The decorator accepts parameters to configure the distributed training environment:

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type="h100")
def run_train():
    # Training code here
    ...
```

^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Parameters

- **`gpus`**: The number of GPUs to provision (e.g., 8 for 8 H100 GPUs). ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **`gpu_type`**: The type of GPU to use. Common options include `"h100"` for NVIDIA H100 accelerators. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## How It Works

Inside the decorated function, the following environment variables are made available for distributed coordination: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
rank = int(os.environ.get("RANK", "0"))
local_rank = int(os.environ.get("LOCAL_RANK", "0"))
world_size = int(os.environ.get("WORLD_SIZE", str(torch.cuda.device_count())))
```

- **`RANK`**: Global rank of the current process across all nodes
- **`LOCAL_RANK`**: Local rank of the current process on its node
- **`WORLD_SIZE`**: Total number of processes across all nodes

To ensure each process uses the correct GPU, call `torch.cuda.set_device(local_rank)` early in the training function. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Key Features

### Automatic GPU Provisioning

The decorator provisions GPUs on-demand based on the specified configuration. For example, `@distributed(gpus=8, gpu_type="h100")` automatically provisions 8 H100 GPUs for the training run. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Data Parallelism

The decorator handles data parallelism across multiple GPUs automatically. The training function runs the same model on each GPU but processes different batches of data in parallel. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Environment Initialization

The decorator sets up the distributed communication backend (typically NCCL for NVIDIA GPUs) before calling the decorated function, so users don't need to manually initialize `torch.distributed`. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Best Practices

### Check for Main Process

Since the training function runs on every GPU, guard rank-specific operations (logging, model saving, metric reporting) behind a check for the main process: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
is_main = rank == 0
if is_main:
    logging.info("Training complete!")
    trainer.save_model(OUTPUT_DIR)
```

### Set CUDA Device

Always call `torch.cuda.set_device(local_rank)` at the beginning of the training function to ensure each process uses the correct GPU: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
local_rank = int(os.environ.get("LOCAL_RANK", "0"))
torch.cuda.set_device(local_rank)
```

### DDP Configuration

When using Hugging Face's `SFTTrainer` or `Trainer`, set `ddp_find_unused_parameters=False` for better performance: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
training_args = SFTConfig(
    ...
    ddp_find_unused_parameters=False,
)
```

## Example: Full Distributed Training Function

The following example demonstrates a complete training function using the `@distributed` decorator for fine-tuning a 20B parameter model: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type="h100")
def run_train():
    import os
    import torch
    
    rank = int(os.environ.get("RANK", "0"))
    local_rank = int(os.environ.get("LOCAL_RANK", "0"))
    torch.cuda.set_device(local_rank)
    world_size = int(os.environ.get("WORLD_SIZE", str(torch.cuda.device_count())))
    is_main = rank == 0
    
    # Load model with quantization and LoRA
    model = AutoModelForCausalLM.from_pretrained(
        "openai/gpt-oss-20b",
        dtype=torch.bfloat16,
        quantization_config=quantization_config,
    )
    peft_model = get_peft_model(model, peft_config)
    
    # Configure training
    trainer = SFTTrainer(
        model=peft_model,
        args=training_args,
        train_dataset=dataset,
    )
    
    result = trainer.train()
    
    if is_main:
        trainer.save_model(OUTPUT_DIR)
    
    return mlflow.last_active_run().info.run_id if mlflow.last_active_run() else None

# Execute training
run_id = run_train.distributed()[0]
```

## Execution

After defining the function with the `@distributed` decorator, call the `.distributed()` method on the function to execute the training across the provisioned GPUs: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
run_id = run_train.distributed()[0]
```

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – PyTorch's native distributed data parallelism framework
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) – Parameter-efficient fine-tuning technique commonly used with distributed training
- [Serverless GPU Compute on Databricks](/concepts/serverless-gpu-compute-on-databricks.md) – The compute infrastructure used with the @distributed decorator
- [MXFP4 Quantization](/concepts/mxfp4-quantization.md) – Memory-efficient model quantization format for large models
- [SFTTrainer](/concepts/sfttrainer.md) – Hugging Face's supervised fine-tuning trainer with DDP support
- GPU Memory Monitoring – Utility for tracking GPU memory usage during distributed training

## Sources

- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
