---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dffbe56a0df73e090cf42f47777db9c8f6d9c3a8f63c686628b21345cf670f88
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trl-sfttrainer
    - TRL's SFTTrainer
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: TRL SFTTrainer
description: A library component from Transformer Reinforcement Learning (TRL) that simplifies supervised fine-tuning configuration, integrates with LoRA via PEFT, and supports Liger kernel optimizations.
tags:
  - machine-learning
  - fine-tuning
  - trl-library
timestamp: "2026-06-19T10:15:37.608Z"
---

# TRL SFTTrainer

**TRL SFTTrainer** is a component of the [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl) library that simplifies supervised fine-tuning (SFT) of large language models. It provides a high-level interface for configuring and running fine-tuning workflows, including support for parameter-efficient techniques and memory optimization kernels.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Overview

The `SFTTrainer` class wraps standard training configurations and automatically applies key optimizations such as mixed precision training, gradient checkpointing, and gradient accumulation. It integrates closely with the `SFTConfig` class, which accepts training hyperparameters including batch size, learning rate, evaluation steps, and reporting targets.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

The trainer supports both full fine-tuning and parameter-efficient approaches like LoRA (Low-Rank Adaptation). When combined with LoRA, the `SFTTrainer` works with a `peft_config` (from the PEFT library) to freeze the base model and train only small adapter layers, reducing trainable parameters by approximately 99%.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Key Features

- **LoRA integration**: Accepts a `peft_config` parameter to enable parameter-efficient fine-tuning with reduced memory requirements.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Liger Kernel support**: Enables memory-efficient training through fused GPU operations by setting `use_liger_kernel=True` in the training arguments. Liger kernels reduce memory usage by up to 80% through optimized Triton kernels for transformer operations such as RMSNorm, RoPE, SwiGLU, and CrossEntropy.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Mixed precision training**: Supports FP16 computation for faster training with lower memory footprint.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Gradient checkpointing**: Trades computation for memory to fit larger batch sizes on available GPUs.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Gradient accumulation**: Simulates larger effective batch sizes for more stable training.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **MLflow integration**: Set `report_to="mlflow"` in the training arguments to automatically log training metrics and model artifacts.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Basic Usage

The following example demonstrates how to configure and use the `SFTTrainer` for LoRA-based fine-tuning:^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
from trl import SFTConfig, SFTTrainer

training_args = SFTConfig(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    gradient_accumulation_steps=4,
    learning_rate=1e-4,
    num_train_epochs=1,
    eval_steps=100,
    logging_steps=25,
    save_steps=100,
    save_total_limit=2,
    report_to="mlflow",
    run_name=f"{MODEL_NAME}_fine-tuning",
    warmup_steps=50,
    weight_decay=0.01,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    dataloader_pin_memory=False,
    remove_unused_columns=False,
    use_liger_kernel=True,       # Enable Liger kernel optimizations
    fp16=True,                    # Mixed precision training
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},  # Required for LoRA with DDP
)

trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    processing_class=tokenizer,
    peft_config=peft_config,      # LoRA configuration
)

trainer.train()
```

## Configuration Parameters

The `SFTConfig` class accepts a wide range of training hyperparameters. Key parameters demonstrated in distributed fine-tuning workflows include:^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `per_device_train_batch_size` | 8 | Number of examples per GPU per training step |
| `gradient_accumulation_steps` | 4 | Accumulates gradients over multiple batches for effective batch size of 32 |
| `learning_rate` | 1e-4 | Conservative rate, often scaled 10x higher for LoRA training |
| `num_train_epochs` | 1 | Single pass through the dataset to prevent overfitting |
| `logging_steps` | 25 | Frequency of metric logging |
| `save_steps` | 100 | Frequency of checkpoint saving |
| `use_liger_kernel` | True | Enables Liger kernel memory optimizations |
| `gradient_checkpointing` | True | Memory-saving technique trading computation for memory |

## Integration with Distributed Training

The `SFTTrainer` is commonly used within distributed training frameworks. On [Databricks Serverless GPU Compute](/concepts/databricks-serverless-gpu.md), it can be wrapped in a `@distributed` decorator function that provisions multiple GPUs (e.g., 8 H100 GPUs) and handles automatic data distribution and synchronization. After training completes, the trainer's `save_model()` method stores LoRA adapters and the tokenizer to the specified output directory.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Related Concepts

- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) — Parameter-efficient fine-tuning technique integrated with SFTTrainer
- [Liger Kernels](/concepts/liger-kernels.md) — GPU-optimized kernels for memory-efficient transformer training
- PEFT Library — Library providing LoRA and other parameter-efficient methods
- SFTConfig — Configuration class for SFTTrainer hyperparameters
- TRL Library — The parent library for Transformer Reinforcement Learning
- [Supervised Fine-Tuning](/concepts/supervised-fine-tuning-sft.md) — The training paradigm that SFTTrainer implements
- [Databricks Serverless GPU Compute](/concepts/databricks-serverless-gpu.md) — Managed compute platform for distributed training

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
