---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f4675e9f63b533d9dd9e7faed282692bbebc215b1c3ba042208be5513b5ee0a
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepspeed-zero-stage-3
    - DZS3
    - DeepSpeed ZeRO
    - ZeRO Stage 3
    - deepspeed-zero-stage-3-optimization
    - DZS3O
    - DeepSpeed Zero Optimization
    - ZeRO Optimization
    - ZeRO optimization
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: DeepSpeed ZeRO Stage 3
description: A memory optimization technique that partitions model parameters, gradients, and optimizer states across GPUs to enable training of large models
tags:
  - optimization
  - distributed-training
  - memory
timestamp: "2026-06-19T10:33:42.614Z"
---

# DeepSpeed ZeRO Stage 3

**DeepSpeed ZeRO (Zero Redundancy Optimizer) Stage 3** is a memory optimization technique that partitions model parameters, gradients, and optimizer states across all GPUs during distributed training. By eliminating redundant copies of model states, Stage 3 dramatically reduces per-GPU memory consumption, enabling the training of large models that would otherwise exceed the memory capacity of a single GPU. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## How ZeRO Stage 3 Works

Standard data-parallel training replicates the entire model — parameters, gradients, and optimizer states — on every GPU. ZeRO Stage 3 shards all three components across the GPUs in a training job. Each GPU holds only a fraction of the total model state, and when a parameter is needed for a forward or backward pass, it is dynamically gathered from the other GPUs. This process is transparent to the user and is handled by the DeepSpeed runtime. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Typical Configuration

On [AI Runtime](/concepts/ai-runtime.md), a single-node DeepSpeed ZeRO Stage 3 configuration for 8 H100 GPUs often looks like:

- `bf16` enabled for reduced memory and faster arithmetic.
- `overlap_comm: True` — overlaps gradient communication with computation.
- `contiguous_gradients: True` — stores gradients in a contiguous buffer for efficiency.
- `sub_group_size: 1e9` — controls the granularity of parameter gathering.
- `stage3_prefetch_bucket_size` and `stage3_max_live_parameters` tuned to balance memory and communication overhead.
- `stage3_gather_16bit_weights_on_model_save: True` — ensures that when saving a checkpoint, 16-bit weights are gathered to produce a single full-precision copy.

CPU offloading (`offload_optimizer`, `offload_param`) can be set to `"cpu"` or left as `"none"` when GPU memory is sufficient. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Usage on Databricks

On [AI Runtime](/concepts/ai-runtime.md), DeepSpeed ZeRO Stage 3 is configured by writing a JSON configuration file and passing its path to the training arguments (e.g., `SFTConfig` or `TrainingArguments`). The [`@distributed` decorator](https://api-docs.databricks.com/python/serverless_gpu/index.html) provisions GPU resources and automatically launches the distributed job. The configuration object includes all Stage 3 parameters, which are later serialized to a temporary file and used by the trainer. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [DeepSpeed](/concepts/deepspeed.md) — The library providing ZeRO optimization
- ZeRO — The Zero Redundancy Optimizer family
- [AI Runtime](/concepts/ai-runtime.md) — Databricks-managed GPU compute
- bfloat16 — Half-precision floating point format used for efficient training
- H100 GPU — High-memory GPU commonly used for large-model training

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
