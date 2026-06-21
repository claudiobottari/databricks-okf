---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5958344e7534a7b0a18b3e5a0e0b3672f7f81a53ca6e61940ae54cf5df5278f6
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fully-sharded-data-parallel-fsdp-for-large-model-training
    - FSDP(FLMT
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Fully Sharded Data Parallel (FSDP) for Large Model Training
description: A distributed training technique that shards model parameters, gradients, and optimizer states across GPUs to enable training of large models that exceed single GPU memory capacity.
tags:
  - distributed-training
  - deep-learning
  - gpu-optimization
timestamp: "2026-06-18T12:21:58.505Z"
---

# Fully Sharded Data Parallel (FSDP) for Large Model Training

**Fully Sharded Data Parallel (FSDP)** is a distributed training strategy that shards model parameters, gradients, and optimizer states across multiple GPUs, enabling the training of large models that cannot fit into the memory of a single GPU. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

FSDP is designed for training very large models (e.g., 120B+ parameters) by distributing the memory footprint across devices. Unlike standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), which replicates the entire model on each GPU, FSDP partitions the model’s state so that each GPU holds only a fraction of the total parameters. During the forward and backward passes, the required shards are gathered on demand, then reshared after use. This allows models to scale far beyond single-GPU memory limits. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## How FSDP Works

### Sharding Strategy

FSDP employs a *full_shard* strategy (also known as `FSDP2`) that shards parameters, gradients, and optimizer states across all participating GPUs. The key operations are:

- **All-gather**: Before a transformer layer’s forward pass, the full parameters for that layer are gathered from all GPUs so each GPU has a complete copy for computation.
- **Reshard after forward**: After the forward pass, the gathered parameters are freed, keeping only the local shard to conserve memory.
- **Gradient sharding**: During backpropagation, gradients are computed locally and then reduced across GPUs, with each GPU retaining only its assigned shard of the gradients.

This approach minimizes peak memory usage at the cost of additional communication. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Automatic Layer Wrapping

FSDP can automatically wrap transformer decoder layers as individual FSDP units. The `auto_wrap` policy inspects the model’s named modules and identifies common decoder layer class names (e.g., `LlamaDecoderLayer`, `MistralDecoderLayer`) to decide where to apply sharding boundaries. If no known class names are found, a fallback heuristic matches any module whose name contains “Block”, “DecoderLayer”, or “Layer” (excluding embeddings). ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Activation Checkpointing

FSDP supports *activation checkpointing* (also known as gradient checkpointing) to trade compute for memory. Instead of storing all intermediate activations for the backward pass, selected activations are recomputed on the fly. In FSDP2 this is enabled with `activation_checkpointing: True` in the config, which is distinct from Hugging Face’s `gradient_checkpointing` flag. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## FSDP Configuration

When using FSDP with a training framework such as Hugging Face’s `SFTTrainer` (from [TRL](/concepts/trl-transformer-reinforcement-learning.md)), the following configuration knobs are commonly set:

| Config Field | Description | Example Value |
|--------------|-------------|---------------|
| `fsdp` | Sharding strategy and wrapping policy; often set to `"full_shard auto_wrap"` to enable FSDP2 with automatic layer wrapping. | `"full_shard auto_wrap"` |
| `version` | FSDP version; set to `2` for the newer, more efficient FSDP2 implementation. | `2` |
| `fsdp_transformer_layer_cls_to_wrap` | List of transformer block class names to wrap. FSDP uses these to decide layer boundaries for sharding. | `["LlamaDecoderLayer", ...]` |
| `reshard_after_forward` | When `True`, parameters are freed after the forward pass and re-gathered before the backward pass, reducing memory usage. | `True` |
| `activation_checkpointing` | Enables activation checkpointing within FSDP, recomputing activations during backward pass instead of storing them. | `True` |
| `xla` | Whether to use XLA compilation; typically `False` for GPU training. | `False` |
| `limit_all_gathers` | When `True`, limits the number of simultaneous all-gather operations to reduce peak memory. | `True` |

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Integration with Training Frameworks

FSDP is integrated with the Transformers library and [TRL](/concepts/trl-transformer-reinforcement-learning.md)’s `SFTTrainer` through the `SFTConfig`’s `fsdp` and `fsdp_config` parameters. The trainer automatically initializes the distributed environment and applies FSDP wrapping. The model must be loaded without a `device_map` or explicit `.to(device)` calls — FSDP and the accelerator handle placement. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Databricks Serverless GPU Compute

On Databricks, the distributed training function is decorated with `@distributed(gpus=8, gpu_type='H100')` to orchestrate multi-GPU execution. The function includes FSDP configuration inside the training arguments and uses the serverless GPU infrastructure with H100 accelerators. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Example: Fine-Tuning a 120B Model

The provided notebook demonstrates supervised fine-tuning of OpenAI’s GPT-OSS 120B model on 8 H100 GPUs using FSDP2. Key highlights:

- **Model**: loaded in bfloat16 precision with `attn_implementation="eager"`, `use_cache=False`, and `low_cpu_mem_usage=True`.
- **LoRA**: Low-Rank Adaptation (rank 32, `target_modules="all-linear"`) reduces the number of trainable parameters.
- **FSDP**: full_shard with automatic wrapping of decoder layers, activation checkpointing enabled.
- **Batch size**: 1 per device with gradient accumulation (4 steps) to maintain effective batch size.
- **Training**: uses the `HuggingFaceH4/Multilingual-Thinking` dataset for 1 epoch.

The training function is launched via `train_gpt_oss_fsdp_120b.distributed()`. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Best Practices

- **Uniform dtype**: Cast all parameters (including LoRA adapters, which are initialized in float32) to the same dtype (e.g., bfloat16) before FSDP wrapping to avoid dtype mismatches. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Disable `use_cache`**: For training, set `use_cache=False` in the model config to avoid caching overhead when gradient checkpointing is active. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Choose activation checkpointing over gradient checkpointing**: FSDP2 provides its own activation checkpointing flag (`activation_checkpointing: True`) rather than relying on the Hugging Face `gradient_checkpointing` parameter. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Set `ddp_find_unused_parameters=False`** to avoid unnecessary overhead when using LoRA, since not all parameters are trained. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Use conservative batch sizes** initially (e.g., `per_device_batch_size=1`) for very large models and increase via gradient accumulation. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- [Transformers Reinforcement Learning (TRL)](/concepts/trl-transformer-reinforcement-learning.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Bfloat16 Precision
- [Activation Checkpointing](/concepts/activation-checkpointing.md)

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
