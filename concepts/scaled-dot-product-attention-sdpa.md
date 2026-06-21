---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7ec278331e93cb71407b080f76e275d292770a6980895d37afee24f4c6e92ca6
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scaled-dot-product-attention-sdpa
    - SDPA(
    - SDPA
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: Scaled Dot Product Attention (SDPA)
description: An attention implementation alternative to Flash Attention offering broader GPU compatibility in Axolotl configurations
tags:
  - machine-learning
  - attention
  - optimization
timestamp: "2026-06-18T12:21:32.896Z"
---

# Scaled Dot Product Attention (SDPA)

**Scaled Dot Product Attention (SDPA)** is an attention mechanism implementation used in transformer-based models that computes attention scores as the scaled dot product between query and key vectors. SDPA is specified in PyTorch as the `attn_implementation="sdpa"` parameter and is often used as an alternative to flash attention for broader GPU compatibility. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Overview

SDPA computes attention using the standard scaled dot-product formula:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

where $Q$ represents queries, $K$ keys, $V$ values, and $d_k$ is the dimension of the key vectors. The scaling factor $\sqrt{d_k}$ prevents the dot products from growing too large in magnitude, which would push the softmax function into regions with extremely small gradients. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## SDPA vs. Flash Attention

SDPA and [Flash Attention](/concepts/flash-attention.md) are two different attention implementations with distinct characteristics: ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

| Feature | SDPA | Flash Attention |
|---------|------|-----------------|
| GPU compatibility | Broader compatibility across GPU types | Requires specific GPU architectures (e.g., Ampere or newer) |
| Memory efficiency | Standard implementation | More memory-efficient through tiling and recomputation |
| Speed | Generally slower for long sequences | Faster, especially for long sequences |

## Use Cases

### When to Use SDPA

SDPA is recommended when: ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

- Running models on GPUs that do not support Flash Attention
- Prioritizing compatibility over maximum performance
- Working with shorter sequence lengths where memory optimization is less critical

### Configuration Example

SDPA is configured in training frameworks such as [Axolotl](/concepts/axolotl.md) by setting the attention implementation parameter: ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

```python
config = DictDefault(
    # ... other configuration ...
    attn_implementation="sdpa",
    sdpa_attention=True,
    flash_attention=False,
    # ... other configuration ...
)
```

## Performance Considerations

When training large language models, SDPA may require more GPU memory than Flash Attention for the same sequence lengths and batch sizes. For long-context training or when GPU memory is constrained, Flash Attention is generally preferred if the hardware supports it. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Transformer architecture — The neural network architecture that uses attention mechanisms
- [Flash Attention](/concepts/flash-attention.md) — A memory-efficient attention implementation alternative to SDPA
- [Axolotl](/concepts/axolotl.md) — A training framework that supports configuring attention implementations
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) — A fine-tuning technique that can use either SDPA or Flash Attention
- Multi-GPU training — Distributed training configurations where attention implementation choice affects memory usage

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
