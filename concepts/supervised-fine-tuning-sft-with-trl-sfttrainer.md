---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86e85341730e230c8758710407b460119dce4a2f199e6f4c9991c0b94aa6f0a9
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supervised-fine-tuning-sft-with-trl-sfttrainer
    - SF(WTS
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Supervised Fine-Tuning (SFT) with TRL SFTTrainer
description: A supervised fine-tuning method for language models using the Transformer Reinforcement Learning (TRL) library's SFTTrainer, which streamlines the process of fine-tuning causal language models on instruction-following datasets.
tags:
  - fine-tuning
  - transformers
  - trl
timestamp: "2026-06-18T12:22:39.947Z"
---

Here is the wiki page for **Supervised Fine-Tuning (SFT) with TRL SFTTrainer**.

---

# Supervised Fine-Tuning (SFT) with TRL SFTTrainer

**Supervised Fine-Tuning (SFT)** is a technique used to adapt a pre-trained large language model (LLM) to a specific downstream task using a labeled dataset. The **SFTTrainer** from the **Transformers Reinforcement Learning (TRL)** library provides a streamlined interface for this process, enabling practitioners to fine-tune models with distributed training strategies like [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), and parameter-efficient methods such as [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md).^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

SFT is the first step in many multi-stage training pipelines, including [Reinforcement Learning from Human Feedback (RLHF)](/concepts/trl-transformers-reinforcement-learning.md). The TRL `SFTTrainer` class builds on the Hugging Face `transformers` `Trainer` and `SFTConfig` to handle the details of dataset formatting, tokenization, and model training, making it suitable for high-throughput distributed environments.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Key Concepts and Components

### The TRL Library

The `trl` library provides both `SFTTrainer` and `SFTConfig`, which configure the training loop. It is designed to work with the `transformers`, `peft` (for LoRA), `datasets`, and `accelerate` libraries, allowing the training to scale across multiple GPUs and nodes.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Training Strategy: FSDP

When fine-tuning very large models (e.g., 120B parameters), **FSDP** is the primary distributed strategy. FSDP shards model parameters, gradients, and optimizer states across GPUs, and can be configured with `auto_wrap` to wrap transformer decoder layers for efficient computation. The `SFTConfig` exposes `fsdp` and `fsdp_config` arguments to control this behavior.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Training Strategy: LoRA

**LoRA** reduces the number of trainable parameters by inserting small, trainable adapter matrices into the model layers. By setting `target_modules="all-linear"` and using a `LoraConfig` with a low rank (e.g., `r=32` or `r=16`), practitioners can fine-tune a large model on a limited number of GPUs. The `SFTTrainer` automatically applies the LoRA configuration when passed as a `peft_config`.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### The Distributed Training Function

In a Databricks environment, the training function is typically defined as a Python function decorated with `@distributed`. This decorator handles the orchestration of launching the training across multiple GPUs with proper distributed setup (including `LOCAL_RANK` and `WORLD_SIZE`). The SFTTrainer is instantiated inside this function with the model, tokenizer, dataset, and training arguments.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Workflow

1. **Environment Setup**: Install `trl`, `peft`, `transformers`, `datasets`, and `accelerate`. Restart the Python kernel to ensure the libraries are properly linked.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

2. **Model Preparation**: Load the base model with `torch.bfloat16` precision and `attn_implementation="eager"`. Disable `device_map` and `.to(device)` calls, allowing the `Trainer`/`Accelerate`+`FSDP` to handle placement.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

3. **PEFT Configuration**: Create a `LoraConfig` with the desired rank, `lora_alpha`, and `target_modules`. Apply the configuration to the model using `get_peft_model` and cast all parameters to `bfloat16` to maintain a uniform dtype for FSDP.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

4. **Training Configuration**: Use `SFTConfig` to set hyperparameters such as `per_device_train_batch_size`, `gradient_accumulation_steps`, `learning_rate`, and `num_train_epochs`. Enable FSDP by setting `fsdp="full_shard auto_wrap"` and provide an `fsdp_config` dictionary.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

5. **Training Execution**: Instantiate the `SFTTrainer` with the model, `training_args`, `train_dataset`, and `tokenizer`. Call `trainer.train()` to begin the fine-tuning. The training loop tracks `logging_steps` and `report_to` for observability.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Configuration Details

### SFTConfig

The `SFTConfig` object defines the training parameters. Key arguments include:

- `bf16=True`: Enable bfloat16 training for H100 GPUs.
- `max_length`: The maximum sequence length for the tokenizer.
- `dataloader_pin_memory`: Improves data transfer speed.
- `ddp_find_unused_parameters=False`: Disables DDP parameter scanning (required for FSDP).
- `fsdp_config`: A dictionary containing `version`, `fsdp_transformer_layer_cls_to_wrap`, `activation_checkpointing`, and `limit_all_gathers`.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Auto-Wrapping for FSDP

To determine the correct `fsdp_transformer_layer_cls_to_wrap` classes, the `SFTTrainer` inspects the model's modules and searches for common decoder layer class names (e.g., `LlamaDecoderLayer`, `MistralDecoderLayer`). If no known classes are found, the function falls back to a heuristic that matches any module name containing `"Block"`, `"DecoderLayer"`, or `"Layer"`.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Example: 120B Parameter Fine-Tuning

The following notebook demonstrates SFT of the 120B parameter GPT-OSS model on 8 H100 GPUs using TRL SFTTrainer with FSDP and LoRA:^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
# Install required packages
%pip install "trl==1.1.0"
%pip install "peft==0.19.1"
%pip install "transformers==5.5.4"
%restart_python

# Define the training function
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def train_model():
    import torch
    from trl import SFTTrainer, SFTConfig
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import LoraConfig, get_peft_model
    
    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        "openai/gpt-oss-120b",
        torch_dtype=torch.bfloat16,
    )
    
    # Configure LoRA
    peft_config = LoraConfig(
        r=32,
        target_modules="all-linear",
    )
    model = get_peft_model(model, peft_config)
    
    # Configure SFT
    training_args = SFTConfig(
        output_dir="/Volumes/checkpoints",
        bf16=True,
        fsdp="full_shard auto_wrap",
        fsdp_config={"version": 2},
    )
    
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
    )
    
    trainer.train()

train_model.distributed()
```

## Related Concepts

- [TRL (Transformers Reinforcement Learning)](/concepts/trl-transformers-reinforcement-learning.md) — The library providing the SFTTrainer
- [SFTTrainer](/concepts/sfttrainer.md) — The main trainer class for supervised fine-tuning
- LoRA — Parameter-efficient fine-tuning method for reducing trainable parameters
- [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md) — Distributed training strategy for sharding model state
- [DDP (Distributed Data Parallel)](/concepts/distributed-data-parallel-ddp.md) — Traditional data parallelism across GPUs
- Chat Template — The tokenizer configuration used by SFTTrainer for chat models
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — The broader concept of multi-GPU training orchestration

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
