---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 894835598bea0d752234299abe52cc118ce2aaf40ae6a3d551404f30101d72af
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trl-transformers-reinforcement-learning-sfttrainer
    - T(RLS
    - reinforcement learning from human feedback (RLHF)
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: TRL (Transformers Reinforcement Learning) SFTTrainer
description: A library and trainer class from Hugging Face for supervised fine-tuning of transformer models, supporting integration with LoRA, FSDP, and distributed training.
tags:
  - library
  - fine-tuning
  - huggingface
timestamp: "2026-06-19T10:36:12.247Z"
---

# TRL (Transformers Reinforcement Learning) SFTTrainer

**TRL (Transformers Reinforcement Learning) SFTTrainer** is a supervised fine-tuning component from the Hugging Face `trl` library that provides a streamlined interface for fine-tuning large language models using parameter-efficient and distributed training techniques. The library integrates with Hugging Face Transformers, PEFT, and Accelerate to support training on single and multi-GPU setups. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

The SFTTrainer is designed to simplify supervised fine-tuning (SFT) of large causal language models. It works in conjunction with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), and [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) to enable training of models that would otherwise exceed the memory capacity of a single GPU. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Usage with FSDP

When combined with FSDP, the SFTTrainer can shard model parameters, gradients, and optimizer states across multiple GPUs. The typical setup involves:

1. Loading the base model with `AutoModelForCausalLM.from_pretrained()` using bfloat16 precision and optional quantization (e.g., `Mxfp4Config`). ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
2. Applying a LoRA configuration to reduce the number of trainable parameters. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
3. Distributing training with Accelerate and configuring the FSDP strategy within `SFTConfig`. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

For FSDP, the model's transformer block class must be identified so it can be passed to the `fsdp_transformer_layer_cls_to_wrap` parameter in `SFTConfig.fsdp_config`. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## SFTConfig

The `SFTConfig` class controls training hyperparameters and distributed settings. Key configuration fields include: ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

| Field | Purpose |
|-------|---------|
| `output_dir` | Directory for saving checkpoints and model |
| `per_device_train_batch_size` | Batch size per GPU |
| `gradient_accumulation_steps` | Steps to accumulate gradients before updating |
| `bf16` | Whether to use bfloat16 precision |
| `fsdp` | FSDP strategy (e.g., `"full_shard auto_wrap"`) |
| `fsdp_config` | Dictionary with FSDP-specific settings |
| `max_length` | Maximum sequence length for tokenization |

Within `fsdp_config`, users can set: ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

- `version`: Set to `2` for FSDP2
- `fsdp_transformer_layer_cls_to_wrap`: List of transformer block class names for automatic wrapping
- `activation_checkpointing`: Enable activation checkpointing to reduce memory (set to `True` instead of using `gradient_checkpointing`)
- `limit_all_gathers`: Reduce peak memory by limiting simultaneous all-gather operations

## Training Flow

The training process follows this general sequence: ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

1. **Load tokenizer**: Load the model's tokenizer via `AutoTokenizer.from_pretrained()`.
2. **Prepare tokenizer**: Set padding token (usually to EOS), model max length, and truncation side.
3. **Load model**: Load the base model in the desired precision (bfloat16) with optional quantization.
4. **Apply LoRA**: Create a LoraConfig and wrap the model using `get_peft_model()`.
5. **Prepare dataset**: Load a training dataset (e.g., from Hugging Face Datasets).
6. **Configure SFTConfig**: Set training arguments including FSDP configuration.
7. **Initialize SFTTrainer**: Pass model, args, dataset, and tokenizer.
8. **Train**: Call `trainer.train()`.

## Example with GPT-OSS 120B

A production example using SFTTrainer with FSDP to fine-tune the 120B parameter GPT-OSS model on 8 H100 GPUs demonstrates: ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Mxfp4Config
from trl import SFTTrainer, SFTConfig
from peft import LoraConfig, get_peft_model

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("openai/gpt-oss-120b")
tokenizer.pad_token = tokenizer.eos_token

# Load model with quantization and bfloat16
model = AutoModelForCausalLM.from_pretrained(
    "openai/gpt-oss-120b",
    dtype=torch.bfloat16,
    quantization_config=Mxfp4Config(dequantize=True),
)

# Apply LoRA
peft_config = LoraConfig(r=32, target_modules="all-linear")
model = get_peft_model(model, peft_config)

# Configure SFTConfig with FSDP
training_args = SFTConfig(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    bf16=True,
    fsdp="full_shard auto_wrap",
    fsdp_config={
        "version": 2,
        "fsdp_transformer_layer_cls_to_wrap": ["DecoderLayer"],
        "activation_checkpointing": True,
    },
    max_length=2048,
)

# Initialize and train
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    processing_class=tokenizer,
)
trainer.train()
```

## Related Concepts

- [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md)
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- Accelerate Library
- [PEFT (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md)
- Hugging Face Transformers
- SFTConfig
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
