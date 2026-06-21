---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ec9f1ac67eef8fdb5726208a4eb5f9c9eecb8ab09b67f88acb6be6610449f06
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trl-sfttrainer-for-supervised-fine-tuning
    - TSFSF
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: TRL SFTTrainer for Supervised Fine-Tuning
description: A trainer from the Transformers Reinforcement Learning library that simplifies supervised fine-tuning of large language models with built-in support for LoRA, FSDP, and distributed training.
tags:
  - fine-tuning
  - llm
  - training-framework
timestamp: "2026-06-19T18:51:46.183Z"
---

# TRL SFTTrainer for Supervised Fine-Tuning

The **TRL SFTTrainer** is a component of the [Transformers Reinforcement Learning (TRL)](/concepts/trl-transformer-reinforcement-learning.md) library that provides a supervised fine-tuning (SFT) trainer for causal language models. It is designed to work with Hugging Face Transformers and supports integration with [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) and [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) for efficient distributed training of large language models. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

The SFTTrainer streamlines the fine-tuning process by handling model loading, dataset preparation, training orchestration, and distributed setup coordination. It is part of the TRL ecosystem, which extends the Hugging Face Transformers library with reinforcement learning and fine-tuning capabilities. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

The trainer accepts configuration through SFTConfig, which controls training hyperparameters such as batch size, learning rate, gradient accumulation steps, optimizer settings, and FSDP configuration. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Key Features

- **Distributed Training Support**: Works with FSDP and [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) to scale training across multiple GPUs. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Parameter-Efficient Fine-Tuning**: Integrates with [PEFT (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md) methods like LoRA to reduce the number of trainable parameters. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Automatic Tokenization**: Accepts a `processing_class` parameter (typically a tokenizer) to handle dataset tokenization during training. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Accelerate Integration**: Leverages Hugging Face's Accelerate library for distributed training orchestration. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Basic Usage

The SFTTrainer is instantiated with a model, training arguments (SFTConfig), a training dataset, and a tokenizer: ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
from trl import SFTTrainer, SFTConfig

training_args = SFTConfig(
    output_dir="/path/to/output",
    num_train_epochs=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=1.5e-4,
    bf16=True,
    logging_steps=5,
)

trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    processing_class=tokenizer,
)

result = trainer.train()
```

## FSDP Configuration with SFTTrainer

When training very large models (e.g., 120B Parameter Models), the SFTTrainer supports FSDP2 through the SFTConfig's `fsdp` and `fsdp_config` parameters. This enables sharding of model parameters, gradients, and optimizer states across GPUs. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Automatic Transformer Layer Detection

For FSDP auto-wrapping, the SFTTrainer requires identifying transformer decoder layer classes. A common approach is to inspect the model's named modules to discover layer types and pass them via the `fsdp_transformer_layer_cls_to_wrap` key in the FSDP configuration. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
def infer_transformer_blocks_for_fsdp(model):
    COMMON = {
        "LlamaDecoderLayer", "MistralDecoderLayer", "MixtralDecoderLayer",
        "Qwen2DecoderLayer", "Gemma2DecoderLayer", "Phi3DecoderLayer",
        "GPTNeoXLayer", "MPTBlock", "BloomBlock", "FalconDecoderLayer",
        "DecoderLayer", "GPTJBlock", "OPTDecoderLayer"
    }
    hits = set()
    for _, m in model.named_modules():
        name = m.__class__.__name__
        if name in COMMON:
            hits.add(name)
    return sorted(hits)
```

### FSDP Configuration Example

```python
fsdp_wrap_classes = infer_transformer_blocks_for_fsdp(model)

training_args = SFTConfig(
    # ... other arguments ...
    fsdp="full_shard auto_wrap",
    fsdp_config={
        "version": 2,
        "fsdp_transformer_layer_cls_to_wrap": fsdp_wrap_classes,
        "reshard_after_forward": True,
        "activation_checkpointing": True,
        "limit_all_gathers": True,
    },
)
```

## Verifying Distributed Setup

After creating the trainer, you can verify that distributed initialization and FSDP are properly configured: ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
import torch.distributed as dist

print(f"dist.is_initialized() -> {dist.is_initialized()}")
acc = getattr(trainer, "accelerator", None)
print(f"distributed_type = {getattr(getattr(acc,'state',None),'distributed_type','n/a')}")
print(f"num_processes = {getattr(acc, 'num_processes', 'n/a')}")
```

## Best Practices

- **Model Placement**: Do not use `device_map` or `.to(device)` on the model; let the Trainer and Accelerate handle placement. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Precision**: Use `torch.bfloat16` for efficient training on H100 GPUs with FSDP. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Memory Management**: Set `low_cpu_mem_usage=True` and `use_cache=False` when loading large models to optimize memory consumption. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Transformers Reinforcement Learning (TRL)](/concepts/trl-transformer-reinforcement-learning.md)
- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- [Parameter-Efficient Fine-Tuning](/concepts/parameter-efficient-fine-tuning-peft.md)
- SFTConfig
- Hugging Face Transformers
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
