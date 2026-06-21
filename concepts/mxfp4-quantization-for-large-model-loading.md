---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0bd2f62f467d513462fc8e8ffbae4c31188ce7581ef997a86051f367b2fc123d
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mxfp4-quantization-for-large-model-loading
    - MQFLML
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Mxfp4 Quantization for Large Model Loading
description: A 4-bit quantization format (Mxfp4Config) used to reduce memory footprint when loading large models, with dequantization happening during forward passes to maintain training fidelity.
tags:
  - model-compression
  - quantization
  - memory-optimization
timestamp: "2026-06-18T12:22:13.909Z"
---

# Mxfp4 Quantization for Large Model Loading

**Mxfp4 Quantization** is a technique for loading very large language models (hundreds of billions of parameters) by storing model weights in the MXFP4 (Microscaling Floating Point 4-bit) format. This dramatically reduces memory footprint during model loading and training, enabling models like the GPT‑OSS 120B to fit on a single GPU node with 8 H100 accelerators. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

In distributed training of large models, the primary bottleneck is GPU memory. Mxfp4 quantization addresses this by representing each weight with only 4 bits, compared to the normal 16 or 32 bits. The weights are stored in the quantized format and dequantized on the fly during computation. The `Mxfp4Config` class from the Hugging Face `transformers` library provides a configuration object that can be passed to `AutoModelForCausalLM.from_pretrained()` to load a model with MXFP4 quantization. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Usage

The typical usage pattern for large model loading with Mxfp4 quantization is:

```python
from transformers import AutoModelForCausalLM, Mxfp4Config

quantization_config = Mxfp4Config(dequantize=True)

model = AutoModelForCausalLM.from_pretrained(
    "openai/gpt-oss-120b",
    dtype=torch.bfloat16,
    quantization_config=quantization_config,
    attn_implementation="eager",
    use_cache=False,
    low_cpu_mem_usage=True,
)
```

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

The `dequantize=True` argument indicates that the quantized weights should be dequantized back to the working precision (e.g., `torch.bfloat16`) for computation. This allows the model to be loaded in a memory‑efficient way while still performing arithmetic at full precision. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Benefits in Distributed Training

When combined with [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md), [LoRA (Low‑Rank Adaptation)](/concepts/lora-low-rank-adaptation.md), and activation checkpointing, Mxfp4 quantization reduces the peak memory required to load a 120B parameter model. The quantized checkpoint occupies approximately one‑quarter of the normal size, which is critical when training on a single node with 8 H100 GPUs (each with 80 GB of HBM). ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Considerations

- **Dequantization overhead**: The `dequantize=True` setting introduces a small computational cost at model load time and during forward passes, as weights must be converted from 4‑bit to bfloat16. This overhead is typically negligible compared to the memory savings.
- **Precision**: MXFP4 is a 4‑bit floating‑point format with limited dynamic range. When used only for loading and storage (with dequantization to bfloat16 for arithmetic), it does not affect training accuracy.
- **Compatibility**: Mxfp4 quantization is supported by Hugging Face’s `transformers` library (version 4.40+). It requires a model that has been pre‑quantized to MXFP4 or that supports the conversion from original weights.

## Related Concepts

- [Quantization](/concepts/mxfp4-quantization.md) — Techniques for reducing model precision
- [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) — Fully Sharded Data Parallel for distributing model state across GPUs
- LoRA — Low‑Rank Adaptation for parameter‑efficient fine‑tuning
- [Activation Checkpointing](/concepts/activation-checkpointing.md) — Trade compute for memory by recomputing activations
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The infrastructure used to run the 120B model training
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi‑GPU training strategies for large models

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
