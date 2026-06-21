---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dea0caf23e1a405e356aa99cb7a3045ed17ca200a72b6d4d657ad04f80e68ef
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - supervised-fine-tuning-sft-workflow
    - SF(W
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: Supervised Fine-Tuning (SFT) Workflow
description: End-to-end pipeline for fine-tuning a causal language model on a conversational dataset, including loading data, applying chat templates, configuring training hyperparameters, and saving artifacts.
tags:
  - machine-learning
  - fine-tuning
  - nlp
timestamp: "2026-06-19T18:33:29.319Z"
---

# Supervised Fine-Tuning (SFT) Workflow

**Supervised Fine-Tuning (SFT) Workflow** refers to the process of adapting a pre-trained large language model (LLM) to a specific task or domain using labeled training data. This workflow typically involves applying parameter-efficient techniques like [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md), using memory-optimized GPU kernels, and leveraging distributed training infrastructure to reduce training time and memory requirements. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Overview

Supervised fine-tuning trains a pre-trained model on a curated dataset of input-output pairs, teaching the model to generate desired responses for specific tasks. The SFT workflow often employs [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md) methods to dramatically reduce the number of trainable parameters while maintaining model quality. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Key Components

### 1. LoRA Configuration

[LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) freezes the base model weights and trains small adapter layers, reducing trainable parameters by approximately 99%. Common configuration parameters include:

- **Rank (r)**: Controls the balance between performance and parameter count. A typical value is 8. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Alpha**: A scaling factor, typically set to 2-4× the rank value (e.g., alpha=32 for r=8). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Dropout**: Regularization to prevent overfitting, commonly set to 0.1. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

Target modules for attention-based models typically include key transformation layers: `q_proj`, `k_proj`, `v_proj`, `o_proj` for attention, and `gate_proj`, `up_proj`, `down_proj` for MLP layers. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### 2. Memory-Optimized GPU Kernels

[Liger Kernels](/concepts/liger-kernels.md) are GPU-optimized operations that fuse multiple computation steps into single kernels, reducing memory transfers and improving efficiency. Key benefits include:

- **Fused operations**: Combines operations (e.g., linear + loss) to reduce memory overhead by up to 80%. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Triton kernels**: Custom GPU kernels optimized for transformer operations including RMSNorm, RoPE, SwiGLU, and CrossEntropy. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Memory efficiency**: Enables larger batch sizes or models that would not otherwise fit in GPU memory. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### 3. Training Framework

The [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) library simplifies training configuration and automatically applies optimizations for supervised fine-tuning. It integrates with Hugging Face Transformers and PEFT libraries. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Training Configuration

### Hyperparameters

Key training parameters in an SFT workflow include:

- **Batch size**: Number of examples per GPU per training step (e.g., 8). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Gradient accumulation steps**: Accumulates gradients over multiple batches for larger effective batch sizes (e.g., 4 steps yields effective batch size of 32 with 8 GPUs). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Learning rate**: Typically conservative; often scaled 10× higher for LoRA training compared to full fine-tuning. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Epochs**: Single pass through the dataset is common to prevent overfitting. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Additional Optimizations

- **Mixed precision (FP16)**: Faster computation with lower memory footprint. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Gradient checkpointing**: Trades computation for memory to fit larger batches. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Warmup steps**: Gradually increases learning rate at the start of training (e.g., 50 steps). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Weight decay**: Regularization technique (e.g., 0.01). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Distributed Training Setup

The SFT workflow can leverage [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) with [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) for distributed training. The `@distributed` decorator from the `serverless_gpu` library configures multi-GPU training:

1. **GPU specification**: Distributes training across a specified number of GPUs (e.g., 8 H100 GPUs). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
2. **Automatic orchestration**: Handles GPU provisioning, data distribution, and synchronization. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
3. **Rank coordination**: Uses `rt.get_local_rank()` and `rt.get_global_rank()` for coordinating work across processes. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Workflow Steps

### Step 1: Environment Setup

Connect to [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) and install required libraries. The [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) environments (e.g., AI v5) include most necessary libraries such as `trl`, `peft`, `transformers`, and `mlflow`. Additional libraries like `liger-kernel` may need separate installation. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Step 2: Configuration

Configure [Unity Catalog](/concepts/unity-catalog.md) integration for model storage, governance, and deployment. Set training hyperparameters including batch size, learning rate, epochs, and logging intervals. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Step 3: Define Training Function

Create a distributed training function that:

1. Loads the dataset (e.g., conversational dataset like Capybara). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
2. Initializes the model and tokenizer with chat formatting. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
3. Applies LoRA adapter layers to reduce trainable parameters. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
4. Configures training arguments with Liger kernel optimizations. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
5. Trains the model with automatic checkpointing and logging. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
6. Saves artifacts (LoRA adapters and tokenizer) to Unity Catalog volume. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Step 4: Execute Training

Run the distributed training function, which provisions GPU resources, distributes the workload, and collects the [MLflow](/concepts/mlflow.md) run ID for model registration. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Step 5: Model Registration

Register the fine-tuned model in [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment:

1. Load the base model and LoRA adapter. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
2. Merge the LoRA weights into the base model. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
3. Log the model using `mlflow.transformers.log_model()` with task metadata (e.g., `llm/v1/chat`). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
4. Register with a fully qualified Unity Catalog path (`{catalog}.{schema}.{model_name}`). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Related Concepts

- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md)
- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md)
- [Liger Kernels](/concepts/liger-kernels.md)
- [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Model Serving](/concepts/model-serving.md)

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
