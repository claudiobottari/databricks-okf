---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65cd3b88fcab05af857c65d46a51966a803616ca47f4078d6bbf065925cde8dc
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - gradient-checkpointing-with-liger-kernels-in-distributed-training
    - GCWLKIDT
    - Checkpointing in Distributed Training
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: Gradient Checkpointing with Liger Kernels in Distributed Training
description: A memory optimization technique that trades computation for memory by recomputing intermediate activations during backpropagation, combined with Liger kernel optimizations to fit larger models on GPU.
tags:
  - memory-optimization
  - distributed-training
  - gradient-checkpointing
  - fine-tuning
timestamp: "2026-06-19T15:14:22.369Z"
---

# Gradient Checkpointing with Liger Kernels in Distributed Training

**Gradient checkpointing with Liger Kernels in distributed training** refers to the combined use of activation checkpointing and kernel-level memory optimizations to train large language models across multiple GPUs, as demonstrated in the distributed fine-tuning of Qwen2‑0.5B with LoRA on Serverless GPU Compute.

## Overview

Gradient checkpointing reduces GPU memory usage by storing only selected intermediate activations during the forward pass and recomputing the missing ones during the backward pass. This trades additional computation for lower memory consumption, allowing larger batch sizes or larger models to fit on a given GPU. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

Liger Kernels are GPU-optimized Triton kernels that fuse multiple operations (e.g., linear + loss) into single kernels, reducing memory transfers and overhead by up to 80%. They provide optimised implementations of RMSNorm, RoPE, SwiGLU, and CrossEntropy. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

When used together in a distributed setting, gradient checkpointing and Liger kernels complement each other: checkpointing reduces activation memory, while Liger kernels reduce the memory footprint of individual operations, enabling models to train on more GPUs with larger effective batch sizes.

## Configuration in a Distributed LoRA Workflow

In the example of fine-tuning Qwen2‑0.5B with LoRA on 8 H100 GPUs, both gradient checkpointing and Liger kernels are enabled through the training arguments:

```python
training_args_dict = {
    ...
    "gradient_checkpointing": True,
    "gradient_checkpointing_kwargs": {"use_reentrant": False},
    "use_liger_kernel": True,
    "fp16": True,
    ...
}
```

- `gradient_checkpointing` is set to `True` to activate the trade-off. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- `use_reentrant` is set to `False` because the default reentrant checkpointing mechanism is incompatible with `LoRA` when used with `Distributed Data Parallel (DDP)`. Setting it to `False` uses a non-reentrant implementation that works correctly in that scenario. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- `use_liger_kernel` is set to `True` to replace standard PyTorch operations with Liger’s fused Triton kernels. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- Mixed precision (`fp16`) is also enabled for additional memory savings. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Benefits in Distributed Training

- **Memory efficiency**: Gradient checkpointing reduces activation memory, and Liger kernels reduce per‑operation memory. Together they can fit larger batches or larger models across multiple GPUs. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Larger effective batch size**: Gradient accumulation is used in conjunction (4 steps in the example) to further simulate a larger total batch size. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Limitations and Considerations

- **Computation overhead**: Gradient checkpointing increases total FLOPs because activations are recomputed. The trade‑off is worthwhile when GPU memory is the bottleneck.
- **Compatibility**: The `use_reentrant=False` argument is specifically required when combining LoRA with DDP. Without it, the training may fail with a reentrancy error. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Related Concepts

- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) – Parameter‑efficient fine‑tuning technique that freezes base weights and trains small adapters.
- [Liger Kernel](/concepts/liger-kernels.md) – Fused GPU kernels for memory‑efficient transformer training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Alternative distributed strategy that shards model states across GPUs.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Data parallelism strategy used with gradient checkpointing in this setup.
- [Gradient Accumulation](/concepts/gradient-accumulation-fusion.md) – Simulating larger batch sizes by accumulating gradients over multiple steps.

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
