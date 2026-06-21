---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71e180768ec65729515f62c554e24e7e519f3016db885d0706940f3332fd16ed
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsloth-optimized-llm-finetuning
    - UOLF
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Unsloth Optimized LLM Finetuning
description: An optimization library that accelerates LLM fine-tuning through memory-efficient kernels, LoRA/QLoRA support, and reduced memory footprint.
tags:
  - machine-learning
  - llm-finetuning
  - optimization
timestamp: "2026-06-19T18:33:18.146Z"
---

# Unsloth Optimized LLM Finetuning

**Unsloth Optimized LLM Finetuning** refers to the practice of fine-tuning large language models (LLMs) using the Unsloth library, which provides performance optimizations for parameter-efficient fine-tuning (PEFT) techniques like LoRA and [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md). Unsloth is designed to reduce memory usage and accelerate training through optimized kernels, efficient gradient checkpointing, and seamless integration with the Hugging Face ecosystem. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Overview

Unsloth provides a streamlined workflow for fine-tuning LLMs, with support for models ranging from 1B to 120B+ parameters. It is distributed as part of the Databricks AI Runtime (AI v5 environment), which includes the full Unsloth stack: `unsloth`, `unsloth_zoo`, `trl`, `peft`, `bitsandbytes`, `xformers`, and `einops`. No additional installation steps are required when using this environment. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Key Features

### Model Loading and Configuration

Unsloth provides the `FastLanguageModel` class for loading pre-trained models with optimal settings for fine-tuning. Key parameters include:

- **max_seq_length**: Configurable sequence length (e.g., 2048 tokens)
- **dtype**: Automatic detection of optimal precision (FP16 for Tesla T4, V100; BF16 for Ampere+ architectures)
- **load_in_4bit**: Support for 4-bit quantization to reduce memory usage
- **device_map**: Per-device mapping for distributed training scenarios

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### LoRA Configuration

Unsloth's `get_peft_model` method applies LoRA adapters with optimized defaults:

- **r**: Rank parameter (suggested values: 8, 16, 32, 64, 128)
- **target_modules**: Configurable attention and projection modules (e.g., q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj)
- **lora_alpha**: Scaling factor for LoRA updates
- **lora_dropout**: Supports any value, but 0 is optimized for performance
- **bias**: "none" is optimized
- **use_gradient_checkpointing**: Enables memory savings during training
- **use_rslora**: Supports rank-stabilized LoRA
- **loftq_config**: Supports LoftQ initialization

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Chat Template Processing

Unsloth provides chat template utilities for processing conversational datasets:

- `get_chat_template`: Applies a specified chat template (e.g., "llama-3.1")
- `standardize_sharegpt`: Standardizes ShareGPT-format conversation data
- `train_on_responses_only`: Configures the trainer to focus loss computation only on response tokens, using `instruction_part` and `response_part` markers

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Distributed Training Integration

Unsloth integrates with the [serverless_gpu](/concepts/serverless-gpu-compute.md) library for distributed training across multiple GPUs. The `@distributed` decorator enables running functions across multiple GPUs, with runtime utilities for rank coordination:

- **local_rank**: GPU rank within a single node
- **global_rank**: Rank across all processes

For [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training, Unsloth requires non-reentrant gradient checkpointing to avoid "mark a variable ready only once" errors. This is configured by setting `gradient_checkpointing_kwargs={"use_reentrant": False}`. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Training with SFTTrainer

Unsloth works with the [TRL](/concepts/trl-transformer-reinforcement-learning-library.md) library's `SFTTrainer` for supervised fine-tuning. The trainer supports:

- **per_device_train_batch_size**: Batch size per GPU (e.g., 2)
- **gradient_accumulation_steps**: Accumulation steps (e.g., 4)
- **warmup_steps**: Learning rate warmup
- **max_steps**: Maximum training steps
- **learning_rate**: Optimizer learning rate (e.g., 2e-4)
- **fp16/bf16**: Mixed precision training based on hardware support
- **optim**: Optimizer choice (e.g., "adamw_8bit")
- **report_to**: Integration with experiment trackers like [MLflow](/concepts/mlflow.md)

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Model Saving and Registration

Unsloth supports saving trained models to multiple destinations:

- **Unity Catalog Volumes**: Checkpoints are saved to specified volume paths
- **Unity Catalog Model Registry**: Models can be registered with full metadata for governance and deployment
- **MLflow Tracking**: Training metrics and artifacts are logged automatically

After training, LoRA adapters can be merged back into the base model using `PeftModel.merge_and_unload()`, and registered with [Unity Catalog](/concepts/unity-catalog.md) for serving. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Optimized Environment Variables

To disable Unsloth's compilation step during distributed training, set the environment variable `UNSLOTH_COMPILE_DISABLE` to `"1"`. This is recommended to avoid compilation overhead when running on multiple GPUs. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) – The parameter-efficient technique Unsloth optimizes
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) – Quantized LoRA for further memory reduction
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Alternative distributed training approach
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – Recommended hardware for Unsloth distributed training
- MLflow Integration – Experiment tracking and model logging
- [Unity Catalog](/concepts/unity-catalog.md) – Model governance and deployment

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
