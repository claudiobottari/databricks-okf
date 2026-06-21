---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40ac2fb14b6dd30cea1601d0578af09a57da06331f5a9ae57880de4a5397a560
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepspeed-zero-stage-3-optimization
    - DZS3O
    - DeepSpeed Zero Optimization
    - ZeRO Optimization
    - ZeRO optimization
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: DeepSpeed ZeRO Stage 3 Optimization
description: A memory optimization technique that partitions model parameters, gradients, and optimizer states across all GPUs to reduce per-GPU memory consumption, enabling training of large models that wouldn't fit on a single GPU.
tags:
  - deepspeed
  - gpu-optimization
  - distributed-training
timestamp: "2026-06-19T18:51:06.213Z"
---

## DeepSpeed ZeRO Stage 3 Optimization

**DeepSpeed ZeRO Stage 3** (Zero Redundancy Optimizer Stage 3) is a memory optimization technique that partitions model parameters, gradients, and optimizer states across all available GPUs in a distributed training setup. By eliminating redundant copies of these state elements, ZeRO Stage 3 drastically reduces the per‑GPU memory footprint, enabling the training of large language models (LLMs) that would otherwise exceed the memory capacity of a single GPU. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### How It Works

ZeRO Stage 3 belongs to the [DeepSpeed](/concepts/deepspeed.md) library’s family of [ZeRO Optimization](/concepts/deepspeed-zero-stage-3-optimization.md) stages, each offering increasing levels of memory savings at the cost of additional communication overhead. Stage 3 shards all three model state components across the GPUs in the training cluster:

- **Model parameters** – distributed across devices
- **Gradients** – computed locally and then communicated in sharded form
- **Optimizer states** (e.g., momentum, variance) – held only on the GPU that owns the corresponding parameter shard

During forward and backward passes, ZeRO Stage 3 dynamically gathers the full parameter and gradient values on demand using efficient communication primitives (e.g., all‑gather, reduce‑scatter). After the parameter update, the optimizer states are updated only on the owning GPU, and the sharded parameters are stored back. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Key Configuration Settings

A typical DeepSpeed ZeRO Stage 3 configuration (as used in the Databricks AI Runtime example for Llama 3.2 1B fine-tuning) includes the following settings:

| Setting | Value | Purpose |
|---|---|---|
| `bf16.enabled` | `true` | Uses bfloat16 precision for faster training and reduced memory |
| `zero_optimization.stage` | `3` | Activates Stage 3 partitioning |
| `offload_optimizer.device` | `"none"` | Keeps optimizer states on GPU (no CPU offloading) |
| `offload_param.device` | `"none"` | Keeps parameters on GPU for maximum H100 performance |
| `overlap_comm` | `true` | Overlaps gradient communication with computation |
| `contiguous_gradients` | `true` | Allocates gradients in contiguous memory for efficiency |
| `reduce_bucket_size` | `"auto"` | Automatically sizes communication buckets |
| `stage3_prefetch_bucket_size` | `"auto"` | Pre‑fetching bucket size for parameter gathering |
| `stage3_gather_16bit_weights_on_model_save` | `true` | Gathers full weights before saving the checkpoint |

These settings are designed for single‑node 8×H100 training where CPU offloading is unnecessary. The `overlap_comm` and `contiguous_gradients` flags are particularly important for hiding communication latency behind computation. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Usage Example: Fine‑Tuning Llama 3.2 1B on AI Runtime

In the Databricks AI Runtime environment, DeepSpeed ZeRO Stage 3 is used together with the `@distributed` decorator from the `serverless_gpu` library to run supervised fine‑tuning (SFT) on a single node of eight H100 GPUs. The training function:

1. Loads the base model and tokenizer from HuggingFace.
2. Configures the [TRL (Transformers Reinforcement Learning)](/concepts/trl-transformers-reinforcement-learning.md) `SFTTrainer` with a DeepSpeed configuration file.
3. Trains the model and saves checkpoints to a [Unity Catalog](/concepts/unity-catalog.md) volume.
4. Logs metrics to [MLflow](/concepts/mlflow.md) for tracking.

The DeepSpeed configuration is written to a temporary JSON file and passed to the `SFTConfig` via the `deepspeed` argument. The trainer then automatically initializes the distributed environment and manages the sharding of model states. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Benefits

- **Memory efficiency**: Reduces per‑GPU memory by eliminating redundant copies of parameters, gradients, and optimizer states.
- **Scalability**: Enables training models that are larger than the memory of a single GPU, such as the 1‑billion‑parameter Llama 3.2 model.
- **Performance**: With high‑bandwidth GPUs (e.g., H100) and appropriate settings (no CPU offloading, overlap communication), ZeRO Stage 3 can achieve near‑linear scaling without significant overhead.

### Limitations

- **Communication overhead**: Sharding requires additional all‑gather and reduce‑scatter operations, which can become a bottleneck on slower interconnects.
- **Single‑node vs. multi‑node**: The configuration shown uses no CPU offloading, making it suitable for single‑node (8×H100) setups. Multi‑node training may require tuning of bucket sizes and possibly enabling offload to CPU layers.

### Related Concepts

- [DeepSpeed](/concepts/deepspeed.md) – The library that provides ZeRO optimization stages.
- [ZeRO Optimization](/concepts/deepspeed-zero-stage-3-optimization.md) – Overview of all three ZeRO stages (1, 2, 3).
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General paradigm for scaling model training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – An alternative sharding strategy available in PyTorch.
- [AI Runtime](/concepts/ai-runtime.md) – Databricks’ managed GPU compute that integrates with DeepSpeed.
- [TRL (Transformers Reinforcement Learning)](/concepts/trl-transformers-reinforcement-learning.md) – Library used for supervised fine‑tuning and RLHF.

### Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
