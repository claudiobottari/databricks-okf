---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85878bb5ecf7cb4576745dd77a11489460d013bdf521275123fbc0b745962305
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - qwen2-05b-language-model
    - QLM
    - Qwen2-0.5B
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: Qwen2-0.5B Language Model
description: A 0.5 billion parameter large language model from the Qwen2 family, used as the base model for parameter-efficient fine-tuning with LoRA in this tutorial.
tags:
  - llm
  - qwen
  - transformer
  - open-source
timestamp: "2026-06-19T15:14:31.952Z"
---

# Qwen2-0.5B Language Model

**Qwen2-0.5B** is a 0.5 billion parameter large language model (LLM) developed by Alibaba Cloud under the Qwen2 series. It is designed for parameter-efficient fine-tuning and distributed training on serverless GPU compute infrastructure, notably on Databricks platform using [NVIDIA H100](/concepts/nvidia-h100-gpu-on-databricks.md) GPUs. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Overview

Qwen2-0.5B is a relatively small language model that enables efficient fine-tuning using [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md). By freezing the base model weights and training only small adapter matrices, LoRA reduces trainable parameters by approximately 99% compared to full fine-tuning, dramatically reducing memory requirements and training time. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Key Optimizations

### LoRA Configuration

When fine-tuning Qwen2-0.5B, LoRA is configured with the following typical parameters:
- **Rank (r=8)**: Provides a good balance between performance and number of parameters
- **Alpha (32)**: Scaling factor, typically set 2-4 times the rank
- **Dropout (0.1)**: Regularization to prevent overfitting
- **Target modules**: Attention layers (`q_proj`, `k_proj`, `v_proj`, `o_proj`) and MLP layers (`gate_proj`, `up_proj`, `down_proj`)

^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Liger Kernel Support

The model can leverage [Liger Kernels](/concepts/liger-kernels.md), GPU-optimized operations that fuse multiple steps into single kernels, reducing memory transfers and improving efficiency. Liger kernels can reduce memory usage by up to 80% through fused operations and are particularly effective for single-GPU training scenarios on A100 or A10 GPUs. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Training Framework

Qwen2-0.5B fine-tuning uses the [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) library for supervised fine-tuning, combined with:
- Mixed precision training (FP16) for faster computation
- [Gradient checkpointing](/concepts/activation-checkpointing.md) to trade computation for memory
- Gradient accumulation to simulate larger batch sizes

^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Training Configuration on Serverless GPU Compute

On Databricks Serverless GPU Compute, Qwen2-0.5B can be trained using an **8xH100** single-node configuration, which provides 8 H100 GPUs with 80GB HBM3 memory each (640GB total). The training function uses a `@distributed` decorator to automatically distribute work across all 8 GPUs. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

Typical training hyperparameters include:
- **Batch size**: 8 per GPU
- **Gradient accumulation steps**: 4 (effective batch size of 32)
- **Learning rate**: 1×10⁻⁴ (with 10× scaling for LoRA)
- **Epochs**: 1 (single pass to prevent overfitting)
- **Evaluation and logging**: Every 25-100 steps

^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Model Registration and Deployment

After fine-tuning, Qwen2-0.5B models can be registered in [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment using [MLflow](/concepts/mlflow.md). The registration process:
1. Loads the base model and LoRA adapter
2. Merges LoRA into the base model (merging and unloading the PEFT wrapper)
3. Logs the model with MLflow using `mlflow.transformers.log_model()`
4. Registers it as a Unity Catalog model (e.g., `main.default.qwen2_liger_lora_assistant`)

^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Dataset and Use Case

The typical dataset used for Qwen2-0.5B fine-tuning is the **Capybara** conversational dataset from TRL, which is split into 90% training and 10% validation sets. The model uses a ChatML format for structured conversation formatting. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Related Concepts

- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- [Liger Kernels](/concepts/liger-kernels.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [LLM (Large Language Model)](/concepts/large-language-models-llms-on-databricks.md)
- Qwen2 Series
- [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md)
- [Peft (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
