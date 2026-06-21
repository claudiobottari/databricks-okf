---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6cc4352591c1275ec8405b168b1c7e545880592ae898bbeb70ccb310e9f34b2
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ddp-gradient-checkpointing-for-distributed-llm-training
    - DGCFDLT
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: 20b-to-120b-parameter-model-training.md
title: DDP Gradient Checkpointing for Distributed LLM Training
description: The requirement to use non-reentrant gradient checkpointing (use_reentrant=False) when combining Unsloth with Distributed Data Parallel (DDP) to avoid variable-ready errors during multi-GPU training.
tags:
  - distributed-training
  - memory-optimization
  - pytorch
timestamp: "2026-06-19T18:33:49.666Z"
---

# DDP Gradient Checkpointing for Distributed LLM Training

**DDP Gradient Checkpointing** refers to the use of gradient checkpointing (also known as activation checkpointing) alongside [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) to reduce the per‑GPU memory footprint during distributed training of [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md). Gradient checkpointing trades additional computation for lower memory usage by recomputing selected activations during the backward pass instead of storing them all. This technique is particularly useful when training LLMs with DDP, where model parameters and optimizer states fit on a single GPU but the activations from large batches or long sequences would otherwise exceed GPU memory. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Requirement for Non‑Reentrant Gradient Checkpointing

When [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) is used, the standard reentrant implementation of gradient checkpointing can cause the error *“mark a variable ready only once”* because DDP’s gradient synchronization logic expects each parameter’s gradient to be marked ready exactly once. To avoid this conflict, DDP requires gradient checkpointing to be configured with **non‑reentrant mode** (`use_reentrant=False`). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

The code snippet below shows the typical configuration:

```python
model.gradient_checkpointing_enable(
    gradient_checkpointing_kwargs={"use_reentrant": False}
)
```

This call must be placed *after* the model is loaded and before training begins. It is commonly used in frameworks such as [Unsloth](/concepts/unsloth.md) and Hugging Face Transformers when fine‑tuning LLMs with DDP. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Context: DDP vs. FSDP

DDP is best suited for models that fit within a single GPU’s memory, as it replicates the entire model (parameters, gradients, and optimizer states) across devices. For models that exceed single‑GPU memory, [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) is the standard choice; it shards model state across GPUs and can be combined with gradient checkpointing as well. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md, 20b-to-120b-parameter-model-training.md] The non‑reentrant checkpointing requirement does **not** apply to FSDP, which has its own activation checkpointing mechanisms.

## Practical Usage in Distributed Fine‑Tuning

A common pattern is to use DDP gradient checkpointing when fine‑tuning LLMs with LoRA adapters across multiple GPUs. For example, in the Unsloth‑based fine‑tuning of Llama‑3.2‑3B on 8×H100 GPUs, the trainer enables non‑reentrant gradient checkpointing after loading the model with `FastLanguageModel.from_pretrained()`. This allows training with a batch size of 2 per device and gradient accumulation steps of 4 on a model with 2048‑token sequences, keeping memory within the 80 GB per GPU limit. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Gradient Checkpointing](/concepts/activation-checkpointing.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Unsloth](/concepts/unsloth.md)
- LoRA
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- H100 GPU Support on Databricks

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- 20b-to-120b-parameter-model-training.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. 20b-to-120b-parameter-model-training.md
