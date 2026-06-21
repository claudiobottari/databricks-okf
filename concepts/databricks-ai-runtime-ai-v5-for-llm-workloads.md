---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6f5fd622e7b86474c43101debdcd1fa6e4c39745d38f61eca02b91c5df7b8b0
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-ai-v5-for-llm-workloads
    - DAR(VFLW
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Databricks AI Runtime (AI v5) for LLM Workloads
description: A curated Databricks runtime environment (AI v5) that bundles Unsloth, TRL, PEFT, bitsandbytes, xformers, and other LLM finetuning dependencies, accessible via serverless GPU clusters with accelerator selection.
tags:
  - databricks
  - runtime-environment
  - infrastructure
timestamp: "2026-06-19T18:33:44.847Z"
---

# Databricks AI Runtime (AI v5) for LLM Workloads

**Databricks AI Runtime (AI v5)** is a pre-configured environment included with Databricks Serverless GPU compute that is optimized for large language model (LLM) workloads, particularly fine-tuning. It bundles a curated set of libraries for distributed training, memory-efficient fine-tuning, and GPU acceleration, eliminating the need for manual package installation. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Overview

The AI v5 environment is available through Databricks Serverless GPU compute when using the 8xH100 single-node configuration. It is designed to support distributed fine-tuning of models such as Llama 3.2 3B and Llama 3.2 1B. By selecting AI v5, users gain immediate access to the full [Unsloth](/concepts/unsloth.md) stack and supporting libraries. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Included Libraries

The AI v5 runtime includes the following packages as part of its base environment:

- `unsloth` – Optimized LLM fine-tuning library
- `unsloth_zoo` – Pre-trained model zoo for Unsloth
- `trl` – Transformer Reinforcement Learning library
- `peft` – Parameter-Efficient Fine-Tuning
- `bitsandbytes` – 4-bit and 8-bit quantization
- `xformers` – Memory-efficient attention kernels
- `einops` – Tensor operations and reshaping

No additional installation steps are required. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Typical Workloads

AI v5 is commonly used for:

- Distributed fine-tuning of LLMs using LoRA or [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) adapters
- Multi-GPU training with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md)
- Training with 4-bit or 8-bit quantization to reduce memory usage
- Applying chat template standardization and training on response-only tokens

The environment supports both single-node multi-GPU training (e.g., 8×H100) and can be extended to multi-node setups. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Selecting AI v5

To use the AI v5 environment with serverless GPU compute:

1. From a Databricks notebook, open the compute selector and choose **Serverless GPU**.
2. In the **Environment** tab, select **AI v5** as the base environment.
3. Choose **8xH100** as the accelerator.
4. Click **Apply**.

Clusters may take up to 8 minutes to launch. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Example: Distributed Fine-Tuning

A typical workflow using AI v5 involves loading a model via `FastLanguageModel.from_pretrained()` from `unsloth`, applying LoRA adapters, and training with `trl.SFTTrainer`. The `@distributed` decorator from the `serverless_gpu` library handles process spawning across GPUs. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type='h100')
def run_train():
    from unsloth import FastLanguageModel, is_bfloat16_supported
    from trl import SFTTrainer
    # ... training code ...
```

The AI v5 environment includes all necessary dependencies, so imports work immediately without explicit installation. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Infrastructure that provisions GPU resources on demand.
- [Unsloth](/concepts/unsloth.md) – Optimized library for fast LLM fine-tuning.
- LoRA – Parameter-efficient fine-tuning technique used in AI v5 examples.
- [SFTTrainer](/concepts/sfttrainer.md) – Trainer from the `trl` library for supervised fine-tuning.
- H100 GPU – High-performance GPU commonly paired with AI v5.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – The typical accelerator choice for LLM workloads.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
