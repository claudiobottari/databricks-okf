---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42e4bd876b0a01beb67d5342b50caa08cc878354565e3c86530919b8fe7b04a5
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sfttrainer-and-trl-library
    - TRL Library and SFTTrainer
    - SATL
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
title: SFTTrainer and TRL Library
description: Supervised Fine-Tuning Trainer from the Transformer Reinforcement Learning (TRL) library used to fine-tune causal language models with support for LoRA, gradient checkpointing, and mixed precision
tags:
  - machine-learning
  - library
  - fine-tuning
timestamp: "2026-06-19T15:13:47.619Z"
---

## SFTTrainer and TRL Library

**SFTTrainer** is a component of the **TRL (Transformer Reinforcement Learning)** library, a Hugging Face library designed for supervised fine-tuning and reinforcement learning with transformer models. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Overview

TRL is described as a "Transformer Reinforcement Learning library for supervised fine-tuning." ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md] Its `SFTTrainer` class provides a high-level API for supervised fine-tuning (SFT) of language models, integrating with Hugging Face transformers and supporting advanced techniques such as [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) and quantization. The trainer is configurable via the `SFTConfig` class, which accepts arguments similar to Hugging Face's `TrainingArguments` (e.g., learning rate, batch size, gradient accumulation, scheduler settings). ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Usage in Distributed Fine‑Tuning

In the context of distributed training on Databricks serverless GPU compute, SFTTrainer is used within a function decorated with `@distributed(gpus=8, gpu_type='h100')`. Key aspects of its usage include:

- **Model preparation**: The base model is loaded with [MXFP4 Quantization](/concepts/mxfp4-quantization.md) and a LoRA adapter is applied via PEFT before passing to the trainer. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **Training configuration**: `SFTConfig` is instantiated with arguments such as `learning_rate`, `per_device_train_batch_size`, `gradient_accumulation_steps`, `gradient_checkpointing`, `max_length`, `warmup_ratio`, and `lr_scheduler_type`. The `report_to` parameter is set to `"mlflow"` to log metrics to [MLflow](/concepts/mlflow.md). ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **Training execution**: The trainer is instantiated with the PEFT model, SFTConfig, training dataset, and tokenizer. Calling `trainer.train()` runs the supervised fine‑tuning loop across multiple GPUs using distributed data parallelism. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Key Components

| Component | Description |
|-----------|-------------|
| `SFTTrainer` | Trainer class for supervised fine‑tuning, supporting LoRA, quantization, and integration with MLflow. |
| `SFTConfig` | Configuration class that defines training hyperparameters and behavior. |

Both are imported from the `trl` package: `from trl import SFTConfig, SFTTrainer`. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Related Concepts

- [TRL](/concepts/trl-transformer-reinforcement-learning.md) — The parent library providing SFTTrainer and reinforcement learning utilities.
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) — Parameter‑efficient fine‑tuning technique used with SFTTrainer.
- PEFT — Library for applying LoRA and other adapter methods.
- [MXFP4 Quantization](/concepts/mxfp4-quantization.md) — 4‑bit floating point format that reduces memory during training.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Parallelism strategy used by SFTTrainer across GPUs.
- [MLflow](/concepts/mlflow.md) — Experiment tracking system used to log training metrics.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Databricks compute environment where the trainer runs.
- [Unity Catalog](/concepts/unity-catalog.md) — Model registry for storing fine‑tuned models.

### Sources

- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
