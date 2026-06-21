---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6d47b5ac137199e097d8366a061f25fb7f72a65eda4be375f51a5cffdf57c25
  pageDirectory: concepts
  sources:
    - large-language-models-llms-databricks-on-aws.md
    - lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - parameter-efficient-fine-tuning-peft
    - PF(
    - LoRA & Parameter-Efficient Fine-Tuning
    - PEFT (Parameter-Efficient Fine-Tuning)
    - Parameter-Efficient Fine-Tuning
    - Parameter-efficient fine-tuning
    - Parameter‑Efficient Fine‑Tuning (PEFT)
    - Parameter‑efficient fine‑tuning
    - Peft (Parameter-Efficient Fine-Tuning)
    - parameter-efficient fine-tuning
    - parameter-efficient fine-tuning methods
    - parameter-efficient-fine-tuning-for-llms
    - PFFL
    - parameter-efficient-fine-tuning-peft-for-llms
    - PF(FL
  citations:
    - file: large-language-models-llms-databricks-on-aws.md
    - file: lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
title: Parameter-Efficient Fine-Tuning (PEFT)
description: A category of techniques that fine-tune LLMs by updating only a small subset of parameters, reducing computational cost
tags:
  - machine-learning
  - fine-tuning
  - llm
timestamp: "2026-06-19T19:11:55.712Z"
---

# Parameter-Efficient Fine-Tuning (PEFT)

**Parameter-Efficient Fine-Tuning (PEFT)** refers to a family of techniques that adapt a pre-trained large language model (LLM) to a downstream task by updating only a small subset of parameters while keeping most of the original model frozen. PEFT dramatically reduces the memory footprint and training time compared to full fine-tuning, and is particularly useful in single‑GPU or memory‑constrained environments. ^[large-language-models-llms-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## LoRA (Low‑Rank Adaptation)

The most widely used PEFT method is **LoRA** (Low‑Rank Adaptation). LoRA freezes the base model’s weights and injects small, trainable adapter matrices into the attention and MLP layers. This reduces the number of trainable parameters by approximately 99% while preserving model quality. As a result, training becomes faster and requires significantly less GPU memory. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

In a typical LoRA configuration, key hyperparameters include:

- **Rank (`r`)**: determines the dimension of the low‑rank matrices; `r=8` offers a good balance between performance and parameter count.
- **Alpha (`lora_alpha`)**: a scaling factor, usually set to 2–4× the rank (e.g., 32 for rank 8).
- **Dropout**: applied to the adapter weights for regularization (commonly 0.1).

Target modules for LoRA in transformer‑based LLMs typically include query, key, value, and output projections (`q_proj`, `k_proj`, `v_proj`, `o_proj`) as well as MLP projections (`gate_proj`, `up_proj`, `down_proj`). ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

After training with LoRA, the adapter weights can be merged back into the base model using `merge_and_unload()` for deployment, or kept separate for modular serving. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Liger Kernels for Memory Efficiency

**Liger Kernels** are GPU‑optimized Triton kernels that complement PEFT techniques by fusing common transformer operations (e.g., linear layer + loss computation). They can reduce memory usage by up to 80% through fused operations, allowing larger batch sizes or models that would otherwise not fit in GPU memory. Liger Kernels are particularly effective for single‑GPU A10/A100 training scenarios and are automatically enabled in the training loop by setting `use_liger_kernel=True` in the SFT configuration. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Supervised Fine‑Tuning with TRL

PEFT methods are often combined with the **TRL** (Transformer Reinforcement Learning) library, which provides the `SFTTrainer` class for supervised fine‑tuning. TRL seamlessly integrates with LoRA and Liger Kernels, handling configuration of the training loop, mixed precision (FP16), gradient accumulation, and MLflow logging. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## PEFT on Databricks AI Runtime

Databricks’ AI Runtime provides ready‑to‑use notebook examples for both PEFT (via LoRA) and full supervised fine‑tuning. As of the documentation date, AI Runtime for single‑node tasks is in **Public Preview**, while the distributed training API for multi‑GPU workloads remains in **Beta**. These examples demonstrate how to fine‑tune models such as Qwen2‑0.5B using PEFT, register the resulting model in [Unity Catalog](/concepts/unity-catalog.md), and deploy it to [Model Serving](/concepts/model-serving.md). ^[large-language-models-llms-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Related Concepts

- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md)
- [Liger Kernels](/concepts/liger-kernels.md)
- [AI Runtime](/concepts/ai-runtime.md)
- [Supervised Fine-Tuning](/concepts/supervised-fine-tuning-sft.md)
- [Full Fine-Tuning](/concepts/full-supervised-fine-tuning.md)
- [Transformer Reinforcement Learning (TRL)](/concepts/trl-transformer-reinforcement-learning.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Model Serving](/concepts/model-serving.md)

## Sources

- large-language-models-llms-databricks-on-aws.md
- lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md

# Citations

1. [large-language-models-llms-databricks-on-aws.md](/references/large-language-models-llms-databricks-on-aws-bfc38cd2.md)
2. [lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md](/references/lora-fine-tuning-of-qwen2-05b-databricks-on-aws-e40ade8f.md)
