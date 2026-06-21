---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30816d104c892778be6bb5ff1530e759da59433a4dc78cc8b6aadb12dd5c7802
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
  confidence: 0.98
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - liger-kernels
    - Liger Kernel
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - file: lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
title: Liger Kernels
description: GPU-optimized Triton kernels that fuse multiple operations (e.g., linear + loss) to reduce memory usage by up to 80%, optimized for transformer operations like RMSNorm, RoPE, SwiGLU, and CrossEntropy.
tags:
  - deep-learning
  - optimization
  - gpu
timestamp: "2026-06-19T18:33:09.751Z"
---

# Liger Kernels

**Liger Kernels** are a collection of GPU-optimized Triton kernels that fuse multiple transformer operations into single, memory-efficient compute units. Originally released by LinkedIn as an open-source library, Liger Kernels reduce GPU memory usage by up to 80% during training while preserving model quality. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Overview

Liger Kernels target the most memory-intensive operations in [Transformer](/concepts/mlflow-transformers-flavor.md)-based models. By fusing operations such as the linear projection and cross-entropy loss into a single kernel, they eliminate intermediate memory allocations that would otherwise consume GPU memory. The kernels are implemented using Triton, a domain-specific language for writing custom GPU kernels, and are optimized for both single-GPU (e.g., A10, A100) and multi-GPU training scenarios. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

A technical paper (arXiv:2410.10989) provides detailed benchmarks showing significant performance improvements across various model sizes and architectures. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Key Benefits

- **Memory reduction**: Fused operations reduce memory overhead by up to 80% compared to unfused implementations. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]
- **Larger batch sizes**: The freed memory allows training with larger batch sizes or models that would otherwise not fit in GPU memory. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]
- **Single-GPU focus**: Particularly effective on A10 and A100 single-GPU training setups, though also beneficial in distributed settings. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Supported Fused Operations

Liger Kernels provide optimized Triton implementations for the following transformer operations: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

| Operation | Description |
|-----------|-------------|
| **RMSNorm** | Root Mean Square Layer Normalization, fused with subsequent linear layers |
| **RoPE** | Rotary Position Embedding, applied as part of the attention mechanism |
| **SwiGLU** | Swish-gated Linear Unit activation, commonly used in modern LLMs |
| **CrossEntropy** | Cross-entropy loss fused with the final linear projection (LM head) |

The fusion of the linear projection and cross-entropy loss is a primary contributor to the memory savings, as it avoids materializing the full logit matrix. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Usage in Training

### Installation

Liger Kernels are not included in the Databricks AI v5 base environment and must be installed manually: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

```python
%pip install liger-kernel==0.8.0
%restart_python
```

After installation, the Python interpreter must be restarted to ensure the package is properly loaded. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Enabling in Training Config

In the [TRL](/concepts/trl-transformer-reinforcement-learning.md) library's `SFTConfig`, set `use_liger_kernel = True` to enable all applicable fused kernels: ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

```python
training_args_dict = {
    "use_liger_kernel": True,
    # other training arguments...
}
training_args = SFTConfig(**training_args_dict)
```

The library automatically replaces compatible operations with their Liger Kernel equivalents at model initialization time. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Performance

In practical fine-tuning scenarios using LoRA on a Qwen2-0.5B model, Liger Kernels enable training that would otherwise exceed GPU memory constraints, particularly when combined with mixed precision (FP16) and gradient checkpointing. Benchmarks from the associated paper show consistent memory and throughput improvements across multiple model families. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md, distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Compatibility

Liger Kernels work with PyTorch-based transformer training pipelines that use standard operations like `nn.RMSNorm`, rotary embeddings, SwiGLU activations, and `CrossEntropyLoss`. They are compatible with the [Hugging Face](/concepts/hugging-face-trainer.md) `transformers` and `peft` libraries, as well as the [TRL](/concepts/trl-transformer-reinforcement-learning.md) training framework. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md, distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Related Concepts

- LoRA — Parameter-efficient fine-tuning technique often combined with Liger Kernels
- [TRL](/concepts/trl-transformer-reinforcement-learning.md) — Transformer Reinforcement Learning library that supports `use_liger_kernel`
- [Transformer](/concepts/mlflow-transformers-flavor.md) — The neural architecture whose operations Liger Kernels optimize
- Triton — The GPU programming language used to implement Liger Kernels
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Databricks-managed GPU compute where Liger Kernels are commonly used
- Mixed Precision Training — Training technique that pairs with Liger Kernels for additional memory savings
- GPU Memory Optimization — Broader category of techniques for reducing memory footprint

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
- lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
2. [lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md](/references/lora-fine-tuning-of-qwen2-05b-databricks-on-aws-e40ade8f.md)
