---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: deac8a576dc45ce6d64e9b230d9d7fd9f0e0c74fe08f8e685e785c046ae967bd
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sdpa-scaled-dot-product-attention
    - S(DPA
    - SDPA Attention
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: SDPA (Scaled Dot Product Attention)
description: Flash Attention alternative used for broader GPU compatibility in transformer model training
tags:
  - machine-learning
  - attention-mechanism
  - optimization
timestamp: "2026-06-19T10:34:50.478Z"
---

# SDPA (Scaled Dot Product Attention)

**SDPA (Scaled Dot Product Attention)** is an attention mechanism implementation used in transformer-based models. In the context of the Databricks Axolotl fine‑tuning framework, SDPA is configured as an alternative to Flash Attention, offering broader GPU compatibility. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Overview

Scaled Dot Product Attention is the core attention operation defined in the original transformer architecture. It computes the attention scores as:

\[
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

where \(Q\), \(K\), \(V\) are the query, key, and value matrices, and \(d_k\) is the dimension of the keys. The scaling factor \(\frac{1}{\sqrt{d_k}}\) prevents the dot products from growing too large in magnitude, maintaining stable gradients.

Many deep learning frameworks, including PyTorch, provide an optimized implementation of this operation, often referred to as SDPA. This implementation uses memory‑efficient kernels that can accelerate training and inference on a wide range of GPU architectures.

## Usage in Axolotl

When fine‑tuning large language models with [Axolotl](/concepts/axolotl.md), practitioners can choose between different attention back‑ends. The configuration for fine‑tuning the Olmo3 7B model using QLoRA explicitly sets:

- `attn_implementation="sdpa"` – selects the SDPA backend,
- `sdpa_attention=True` – enables the SDPA attention variant.

The source material notes that SDPA is used “instead of Flash Attention for broader GPU compatibility.” This makes SDPA a practical choice when the target GPU infrastructure does not support the hardware‑specific optimizations required by Flash Attention, or when maximum portability across different GPU generations is desired. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Considerations

- **GPU compatibility**: SDPA works on a wider range of GPU accelerators compared to Flash Attention, which may require specific GPU architectures (e.g., Ampere or newer) or specific CUDA versions.
- **Performance**: While SDPA is efficient, Flash Attention can offer additional speed and memory savings on supported hardware. The choice depends on the specific compute environment and model size.

## Related Concepts

- [Flash Attention](/concepts/flash-attention.md) – an alternative, memory‑efficient attention implementation.
- [Axolotl](/concepts/axolotl.md) – the fine‑tuning framework that exposes the SDPA configuration.
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) – quantization‑aware parameter‑efficient fine‑tuning method used alongside SDPA.
- [Multi‑GPU Training](/concepts/multi-gpu-distributed-training-api.md) – distributed training on multiple GPUs, where attention implementation choice matters.
- [LLM Fine‑Tuning](/concepts/llm-fine-tuning-on-databricks.md) – the overall process of adapting large language models.

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
