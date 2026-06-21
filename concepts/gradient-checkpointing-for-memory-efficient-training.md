---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 98c9d84f3793350f9ae9e9877e8589774c0e1cfb0bab3cad5d67d9c77bce8ac2
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gradient-checkpointing-for-memory-efficient-training
    - GCFMT
    - Memory-Efficient Training
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: Gradient Checkpointing for Memory-Efficient Training
description: A memory optimization technique that trades computation for memory by not storing intermediate activations during forward pass, instead recomputing them during backward pass, enabling larger batch sizes on limited GPU memory.
tags:
  - machine-learning
  - memory-optimization
  - training
timestamp: "2026-06-19T10:16:00.343Z"
---

---
title: Gradient Checkpointing for Memory-Efficient Training
summary: A technique that trades computation for memory by recomputing intermediate activations during the backward pass instead of storing them all, enabling training of larger models or batch sizes on limited GPU memory.
sources:
  - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T12:00:00.000Z"
updatedAt: "2026-06-20T12:00:00.000Z"
tags:
  - memory-optimization
  - distributed-training
  - fine-tuning
aliases:
  - gradient-checkpointing-for-memory-efficient-training
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Gradient Checkpointing for Memory-Efficient Training

**Gradient Checkpointing** (also known as activation checkpointing) is a memory optimization technique for deep learning training that trades computation for memory. Instead of storing all intermediate activations produced during the forward pass (which is required for the backward pass), gradient checkpointing selectively recomputes them during backpropagation, significantly reducing GPU memory usage at the cost of additional compute. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## How It Works

During a standard forward pass, every intermediate activation between layers is stored in GPU memory so the backward pass can compute gradients. For large models — such as [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — these activations can consume more memory than the model parameters themselves. Gradient checkpointing identifies certain "checkpoint" points in the model graph, discards the activations between checkpoints during the forward pass, and recomputes them on the fly during the backward pass. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

The trade-off is straightforward: memory consumption is reduced, but training time increases because the recomputation adds extra forward passes for those segments. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## When to Use Gradient Checkpointing

Gradient checkpointing is particularly useful when:

- You want to train a model that does not fit in GPU memory with full activation storage. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- You need to increase batch size beyond what memory would normally allow. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- You are using techniques like LoRA that already reduce parameter memory but still hit activation memory limits. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Configuration

In practice, gradient checkpointing is typically enabled through framework-specific arguments. For example, when using the [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) library's `SFTTrainer` or Hugging Face `Trainer`, you enable it by setting the `gradient_checkpointing` training argument to `True`. A common pattern also includes setting `gradient_checkpointing_kwargs` to `{"use_reentrant": False}`, which is required for compatibility with certain distributed training setups like [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Example (SFTTrainer-like configuration)

```python
training_args_dict = {
    # ... other arguments ...
    "gradient_checkpointing": True,
    "gradient_checkpointing_kwargs": {"use_reentrant": False},
}
```

This configuration is frequently used alongside [Liger Kernels](/concepts/liger-kernels.md) (fused GPU operations that reduce memory by up to 80%) and mixed precision training (e.g., FP16) to maximize memory efficiency. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Relationship to Other Memory Optimizations

Gradient checkpointing is one of several complementary techniques for memory-efficient training:

| Technique | Memory Savings | Speed Impact | Use Case |
|-----------|----------------|--------------|----------|
| **Gradient Checkpointing** | Reduces activation storage | Adds recomputation overhead | Large models, large batch sizes |
| **LoRA** | Reduces trainable parameters | Faster fine-tuning | Parameter-efficient fine-tuning |
| **Liger Kernels** | Fuses operations, reduces transfer | Faster per-step | Single/multi-GPU training |
| **Mixed Precision (FP16)** | Halves memory for parameters/grads | Faster math | General speed & memory |

These methods are often combined — for instance, the Distributed fine-tuning of Qwen2-0.5B with LoRA notebook enables gradient checkpointing alongside LoRA, Liger Kernels, and FP16 to fit training on 8× H100 GPUs. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Advantages

- **Enables larger models**: Models that would otherwise exceed GPU memory become trainable. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Larger batch sizes**: Allows bigger effective batch sizes for more stable training. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Broad framework support**: Supported in PyTorch, Hugging Face Transformers, TRL, DeepSpeed, and FSDP. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Disadvantages

- **Slower training**: Recomputation adds forward-pass time for checkpointed segments, typically increasing total training time by 15–30%. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Tuning required**: The number and placement of checkpoints must be balanced between memory savings and speed loss. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Related Concepts

- [Gradient Accumulation](/concepts/gradient-accumulation-fusion.md) — Another technique that simulates larger batch sizes without increasing memory per step.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Distributes model states across GPUs, often used together with gradient checkpointing.
- DeepSpeed Zero Optimization — Shards optimizer states, gradients, and parameters; can be augmented with checkpointing.
- Mixed Precision Training — Using FP16/BF16 to reduce memory and speed computation.
- [Liger Kernels](/concepts/liger-kernels.md) — Fused GPU operations for memory-efficient transformer training.

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
