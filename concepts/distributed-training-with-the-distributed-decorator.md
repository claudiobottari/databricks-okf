---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3427dc4a904762bae8f3a50ed93778d6543f95fb44e96de990cb89688ca8af76
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-with-the-distributed-decorator
    - DTWT@D
    - Distributed training with TorchDistributor
    - distributed training with TorchDistributor
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Distributed Training with the @distributed Decorator
description: A Databricks Serverless GPU Compute API that uses the @distributed decorator to orchestrate multi-GPU training across a specified number of accelerators, handling distributed setup coordination automatically.
tags:
  - distributed-training
  - databricks
  - api
timestamp: "2026-06-18T12:22:23.073Z"
---

# Distributed Training with the @distributed Decorator

The **`@distributed` decorator** is a Databricks Serverless GPU Compute API that enables distributed training of large machine learning models across multiple GPUs with minimal code changes. By decorating a Python function with `@distributed`, you can orchestrate multi-GPU training using frameworks like [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md) and [DDP (Distributed Data Parallel)](/concepts/distributed-data-parallel-ddp.md) without manually managing distributed process groups or cluster communication. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

The `@distributed` decorator handles the orchestration of launching training across all specified GPUs with proper distributed setup. It is imported from the `serverless_gpu` module and accepts parameters to specify the number of GPUs and their type. The decorated function runs on each GPU with environment variables like `LOCAL_RANK`, `RANK`, and `WORLD_SIZE` automatically set, allowing the function to coordinate distributed training internally. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Basic Usage

### Import and Decorate

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def train_gpt_oss_fsdp_120b():
    # Training logic here
    pass
```

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Execute the Distributed Function

After defining the decorated function, call the `.distributed()` method to launch the training job across all GPUs:

```python
train_gpt_oss_fsdp_120b.distributed()
```

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Parameters

The `@distributed` decorator accepts the following parameters:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `gpus` | Number of GPUs to use for distributed training | `8` |
| `gpu_type` | Type of GPU accelerator | `'H100'` |

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Environment Variables

When the decorated function executes, the following environment variables are automatically set for each GPU process:

- `LOCAL_RANK`: The local rank of the GPU on the current node (e.g., `0` through `7` for an 8-GPU node)
- `RANK`: The global rank of the process across all nodes
- `WORLD_SIZE`: The total number of processes (GPUs) across all nodes

These variables enable the training function to set up distributed communication using `torch.distributed` and bind each process to the correct CUDA device. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Internal Function Structure

A function decorated with `@distributed` typically follows this structure:

1. **Imports inside the function**: All imports are placed inside the function body for pickle safety during distributed serialization.
2. **CUDA device binding**: Set the CUDA device using `torch.cuda.set_device(local_rank)`.
3. **Environment variable configuration**: Set environment variables like `NCCL_DEBUG`, `CUDA_LAUNCH_BLOCKING`, and `TORCH_NCCL_ASYNC_ERROR_HANDLING`.
4. **Model loading**: Load the model without a `device_map` — let the Trainer and FSDP handle placement.
5. **Distributed training setup**: Configure FSDP or DDP settings through the training framework (e.g., Hugging Face `SFTConfig`).
6. **Training execution**: Call the trainer's `.train()` method.

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Example: FSDP Training with LoRA

The following example demonstrates a complete distributed training function for fine-tuning a 120B parameter model using FSDP, LoRA, and the TRL `SFTTrainer`:

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def train_gpt_oss_fsdp_120b():
    import os, torch, torch.distributed as dist
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import SFTTrainer, SFTConfig
    from datasets import load_dataset
    from peft import LoraConfig, get_peft_model

    local_rank = int(os.environ.get("LOCAL_RANK", "0"))
    torch.cuda.set_device(local_rank)

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("openai/gpt-oss-120b")
    model = AutoModelForCausalLM.from_pretrained(
        "openai/gpt-oss-120b",
        dtype=torch.bfloat16,
        attn_implementation="eager",
        use_cache=False,
        low_cpu_mem_usage=True,
    )

    # Configure LoRA
    peft_config = LoraConfig(
        r=32,
        lora_alpha=32,
        target_modules="all-linear",
        lora_dropout=0.0,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, peft_config)
    model = model.to(torch.bfloat16)

    # Load dataset
    dataset = load_dataset("HuggingFaceH4/Multilingual-Thinking", split="train")

    # Configure FSDP
    training_args = SFTConfig(
        output_dir="/path/to/output",
        num_train_epochs=1,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        learning_rate=1.5e-4,
        bf16=True,
        fsdp="full_shard auto_wrap",
        fsdp_config={
            "version": 2,
            "fsdp_transformer_layer_cls_to_wrap": ["LlamaDecoderLayer"],
            "reshard_after_forward": True,
            "activation_checkpointing": True,
        },
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
    )

    result = trainer.train()
```

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Multi-Node Training

By setting `remote=False` and specifying a larger number of GPUs (e.g., 16), the `@distributed` decorator can be extended to multi-node training across multiple compute nodes. This allows scaling to even larger models or datasets that require more than a single node's GPU memory. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Best Practices

- **Place imports inside the function** to avoid pickle serialization issues when distributing the function across processes. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Do not set `device_map` or call `.to(device)` on the model** — let the Trainer and FSDP handle device placement automatically. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Use `low_cpu_mem_usage=True`** when loading large models to reduce host memory requirements during checkpoint loading. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Set `use_cache=False`** when using gradient checkpointing, as caching is incompatible with activation checkpointing. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Cast all parameters to a uniform dtype** (e.g., `bfloat16`) after applying LoRA, since LoRA adapters are initialized in `float32` by default. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Infer transformer block classes dynamically** for FSDP wrapping, or specify them explicitly if the automatic detection fails. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Related Concepts

- [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md) — Shards model parameters, gradients, and optimizer states across GPUs
- [DDP (Distributed Data Parallel)](/concepts/distributed-data-parallel-ddp.md) — Distributes training across multiple GPUs for faster training
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) — Reduces trainable parameters by adding small adapter layers
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The Databricks compute environment for GPU-accelerated workloads
- [SFTTrainer](/concepts/sfttrainer.md) — The TRL trainer for supervised fine-tuning
- Multi-GPU and Multi-Node Distributed Training — Scaling distributed training across nodes

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
