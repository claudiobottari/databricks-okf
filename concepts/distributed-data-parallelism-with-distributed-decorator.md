---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: afccce29f3a0e13e17b7aac1e11ee9f63ce261c014ac05d7009ef290021e00de
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-data-parallelism-with-distributed-decorator
    - DDPW@D
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Distributed Data Parallelism with @distributed Decorator
description: Pattern for distributing training across multiple GPUs using Databricks' serverless_gpu library, handling data parallelism, environment variables, and process coordination
tags:
  - machine-learning
  - distributed-training
  - pattern
timestamp: "2026-06-19T15:14:52.436Z"
---

# Distributed Data Parallelism with @distributed Decorator

**Distributed Data Parallelism with @distributed Decorator** is a pattern for scaling deep learning training workloads across multiple GPUs on a single node using Databricks Serverless GPU compute. The `@distributed` decorator, provided by the `serverless_gpu` Python library, automates the provisioning of GPU resources and handles data parallelism across processes without manual infrastructure management.

## Overview

The `@distributed` decorator enables distributed training by automatically spawning multiple processes, one per GPU, and coordinating their execution. When applied to a function, it provisions the specified GPUs on-demand, sets up the distributed environment variables (such as `RANK`, `LOCAL_RANK`, and `WORLD_SIZE`), and runs the function in parallel across all GPUs. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

This approach is particularly well-suited for [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training, where each GPU holds a copy of the model and processes a different subset of the training data, with gradients synchronized across all GPUs after each step. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Syntax

The `@distributed` decorator takes parameters to specify the GPU configuration: ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(
    gpus=8,
    gpu_type='h100',
)
def my_training_function(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('Starting training', name)
    return rt.get_global_rank()

result = my_training_function.distributed('my_run')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

### Parameters

- **`gpus`**: The number of GPUs to provision for the function. Each GPU runs one process. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **`gpu_type`**: The type of GPU to use (e.g., `'h100'` for NVIDIA H100 GPUs). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Runtime Module

The `serverless_gpu.runtime` module provides access to rank information within the distributed environment: ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

- **`rt.get_local_rank()`**: Returns the rank of the GPU within the current node (0 to `gpus-1`).
- **`rt.get_global_rank()`**: Returns the global rank across all processes in the distributed job.

In practice, the distributed environment variables `RANK`, `LOCAL_RANK`, and `WORLD_SIZE` are also set as environment variables and can be accessed directly using `os.environ`. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Usage Pattern

The typical workflow for using the `@distributed` decorator involves: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

1. **Defining the training function** with the `@distributed` decorator, specifying the GPU count and type.
2. **Setting up the distributed environment** inside the function by accessing rank and world size information.
3. **Initializing the model** on the correct device using `torch.cuda.set_device(local_rank)`.
4. **Loading and distributing data** across processes (handled by libraries like Hugging Face Transformers or [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)).
5. **Performing training** with gradient synchronization managed by DDP.
6. **Saving checkpoints or results** — typically only from the main process (`rank == 0`).
7. **Calling the function** via `function_name.distributed(*args)` to execute across all GPUs.

## Example: LoRA Fine-Tuning with gpt-oss-20b

The following example demonstrates a complete distributed training function for fine-tuning OpenAI's gpt-oss-20b model using LoRA and MXFP4 quantization across 8 H100 GPUs: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type="h100")
def run_train():
    import os
    import torch
    from datasets import load_dataset
    from transformers import AutoTokenizer, AutoModelForCausalLM, Mxfp4Config
    from peft import LoraConfig, get_peft_model
    from trl import SFTConfig, SFTTrainer

    rank = int(os.environ.get("RANK", "0"))
    local_rank = int(os.environ.get("LOCAL_RANK", "0"))
    torch.cuda.set_device(local_rank)

    # Load dataset and model
    dataset = load_dataset("HuggingFaceH4/Multilingual-Thinking", split="train")
    tokenizer = AutoTokenizer.from_pretrained("openai/gpt-oss-20b")

    quantization_config = Mxfp4Config(dequantize=True)
    model = AutoModelForCausalLM.from_pretrained(
        "openai/gpt-oss-20b",
        attn_implementation="eager",
        dtype=torch.bfloat16,
        quantization_config=quantization_config,
        use_cache=False,
    )

    # Apply LoRA
    peft_config = LoraConfig(
        r=8, lora_alpha=16, target_modules="all-linear",
        lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
    )
    peft_model = get_peft_model(model, peft_config)

    # Configure training
    training_args = SFTConfig(
        per_device_train_batch_size=1,
        gradient_accumulation_steps=2,
        gradient_checkpointing=True,
        output_dir="/path/to/output",
        ddp_find_unused_parameters=False,
    )

    trainer = SFTTrainer(
        model=peft_model, args=training_args,
        train_dataset=dataset, processing_class=tokenizer,
    )
    result = trainer.train()

    if rank == 0:
        trainer.save_model("/path/to/output")

    return result.training_loss

# Execute distributed training
results = run_train.distributed()
```

In this example, the `@distributed(gpus=8, gpu_type="h100")` decorator ensures that the function runs on 8 H100 GPUs with automatic data parallelism. The rank information is used to coordinate device assignment and control which process saves the final model. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Best Practices

When using the `@distributed` decorator for distributed data parallelism: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

- **Set the device explicitly** using `torch.cuda.set_device(local_rank)` to ensure each process uses the correct GPU.
- **Disable `ddp_find_unused_parameters`** in training configurations to improve performance when no parameters are intentionally unused.
- **Use gradient checkpointing** to reduce memory usage, especially for large models with limited per-GPU batch sizes.
- **Control I/O operations** by checking `rank == 0` before saving models, logging, or printing to avoid redundant writes.
- **Avoid reporting to external services** from all ranks — use a single rank for MLflow or other tracking.

## Limitations

The current implementation of the `@distributed` decorator supports single-node multi-GPU parallelism only. For multi-node distributed training, additional orchestration or a more advanced framework like [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) across nodes is required. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The infrastructure that provisions GPUs on demand.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The underlying parallelism strategy commonly used with the `@distributed` decorator.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — A supported configuration providing 8 H100 GPUs on a single node.
- LoRA Fine-Tuning — Parameter-efficient fine-tuning often combined with distributed training.
- Hugging Face Transformers — Library commonly used for model loading and training with the decorator.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — An alternative for multi-node or memory-constrained scenarios.

## Sources

- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
