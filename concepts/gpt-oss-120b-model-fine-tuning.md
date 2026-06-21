---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: befee7556ff7b418d7350536dd34244c9b02f07a64f6ff4717d18df1fb45dc15
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpt-oss-120b-model-fine-tuning
    - G1MF
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: GPT-OSS 120B Model Fine-Tuning
description: The supervised fine-tuning of a 120 billion parameter GPT-OSS model using distributed training techniques on 8 H100 GPUs with Databricks Serverless GPU Compute.
tags:
  - fine-tuning
  - llm
  - databricks
timestamp: "2026-06-19T18:51:59.761Z"
---

# GPT-OSS 120B Model Fine-Tuning

**GPT-OSS 120B Model Fine-Tuning** refers to the process of supervised fine-tuning (SFT) of OpenAI's 120 billion parameter GPT-OSS model using distributed training techniques on Databricks Serverless GPU Compute. This approach enables efficient adaptation of the large language model for specific downstream tasks while managing memory constraints through advanced parallelism strategies. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

Fine-tuning a 120B parameter model presents significant memory and computational challenges, as the model cannot fit into the memory of a single GPU. The recommended approach combines multiple distributed training techniques to enable efficient training on 8 H100 GPUs, with the option to extend to multi-node configurations using 16 GPUs. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Key Technologies

### FSDP (Fully Sharded Data Parallel)

[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) shards model parameters, gradients, and optimizer states across GPUs, enabling training of large models that don't fit on a single GPU. The implementation uses FSDP2 with `full_shard auto_wrap` configuration and automatic transformer block detection for layer wrapping. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### DDP (Distributed Data Parallel)

[Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) distributes training across multiple GPUs for faster training throughput. The training function sets `ddp_find_unused_parameters=False` for optimal performance. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### LoRA (Low-Rank Adaptation)

[Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) reduces the number of trainable parameters by adding small adapter layers, making fine-tuning more memory-efficient. The configuration uses rank 32 with `all-linear` target modules and specialized rank patterns for MoE (Mixture of Experts) layers. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### TRL (Transformers Reinforcement Learning)

The TRL library provides the `SFTTrainer` class for supervised fine-tuning, which handles the training loop, gradient accumulation, and checkpointing. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Infrastructure Setup

### Compute Configuration

The training runs on Databricks Serverless GPU Compute with the following configuration:

- **Accelerator**: 8 H100 GPUs on a single node ([8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md))
- **Environment version**: 4
- **No base environment**: Required libraries are installed at runtime

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Required Libraries

The following packages are installed for distributed training:

- `trl==1.1.0`: Transformers Reinforcement Learning for SFT training
- `peft==0.19.1`: Parameter-Efficient Fine-Tuning for LoRA adapters
- `transformers==5.5.4`: Hugging Face transformers library
- `datasets==3.2.0`: For loading training datasets
- `accelerate==1.13.0`: For distributed training orchestration
- `hf_transfer`: For faster model downloads from Hugging Face

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Training Configuration

### Model Loading

The 120B parameter GPT-OSS model is loaded in bfloat16 precision with the following settings:

- `attn_implementation="eager"`: Standard attention implementation
- `use_cache=False`: Required for gradient checkpointing
- `low_cpu_mem_usage=True`: Helps with massive checkpoint loading
- `Mxfp4Config(dequantize=True)`: Optional quantization configuration

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Hyperparameters

Key training hyperparameters include:

| Parameter | Value |
|-----------|-------|
| Maximum sequence length | 2048 tokens |
| Per-device batch size | 1 |
| Gradient accumulation steps | 4 |
| Learning rate | 1.5e-4 |
| Number of epochs | 1 |
| Learning rate scheduler | Cosine with 3% warmup |
| Precision | bfloat16 |

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Dataset

The training uses the `HuggingFaceH4/Multilingual-Thinking` dataset for supervised fine-tuning. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Distributed Training Implementation

### The `@distributed` Decorator

The training function is decorated with `@distributed(gpus=8, gpu_type='H100')` from the `serverless_gpu` library, which handles orchestration of launching the training across all GPUs with proper distributed setup. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### FSDP Configuration

The FSDP configuration includes:

- **Version**: 2 (FSDP2)
- **Auto-wrap**: Automatic detection of transformer block classes for layer wrapping
- **Reshard after forward**: Enabled for memory efficiency
- **Activation checkpointing**: Enabled (not gradient checkpointing)
- **Limit all-gathers**: Enabled for communication optimization

^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Transformer Block Detection

The training function automatically detects transformer block classes for FSDP wrapping by checking common class names (LlamaDecoderLayer, MistralDecoderLayer, etc.) and falling back to heuristic detection based on naming patterns. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Output and Checkpointing

The fine-tuned model is saved to a Databricks Unity Catalog volume at the path `/Volumes/{catalog}/{schema}/{volume}/{model_name}`. The training uses `save_strategy="no"` to avoid intermediate checkpoints during the single-epoch run. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Extending to Multi-Node Training

By setting `remote=False` and specifying 16 GPUs, the same approach can be extended to multi-node training across 16 GPUs, enabling even larger effective batch sizes and faster training. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md)
- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md)
- Large Language Model Training
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
