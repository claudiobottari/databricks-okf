---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 272e2398c337574d9442bbff88c0e33f4639c47e24a02fa59ef1aa201fdc0b13
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lora-configuration-parameters
    - LCP
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: LoRA Configuration Parameters
description: Key hyperparameters for configuring LoRA including rank (r=8) balancing performance vs parameters, alpha (32) as scaling factor, dropout (0.1) for regularization, and target module selection for attention and MLP layers.
tags:
  - hyperparameters
  - lora
  - fine-tuning
timestamp: "2026-06-18T15:30:17.867Z"
---

# LoRA Configuration Parameters

**LoRA Configuration Parameters** control how [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) is applied to a base model during [parameter-efficient fine-tuning](/concepts/parameter-efficient-fine-tuning-peft.md). These parameters define the structure and behavior of the small adapter layers that are trained while the base model weights remain frozen.

## Overview

LoRA (Low-Rank Adaptation) freezes the base model weights and trains only small adapter matrices, dramatically reducing memory requirements and training time. The configuration parameters determine the rank, scaling, regularization, and target modules for these adapters. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Core Parameters

### Rank (`r`)

The rank parameter controls the dimensionality of the low-rank matrices. A higher rank allows the adapter to capture more information but increases the number of trainable parameters. The recommended value provides a good balance of performance versus parameter count:

- **Recommended value**: `r=8` ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Alpha (`lora_alpha`)

The alpha parameter is a scaling factor applied to the LoRA adapter outputs. It controls the contribution of the adapter to the base model. The value is typically set to 2–4 times the rank:

- **Recommended value**: `lora_alpha=32` ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Dropout (`lora_dropout`)

Dropout provides regularization to prevent overfitting during fine-tuning. It randomly drops a proportion of the adapter connections during training:

- **Recommended value**: `lora_dropout=0.1` ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Target Modules

The `target_modules` parameter specifies which layers of the base model receive LoRA adapter matrices. For transformer-based models like Qwen2, targeting both attention and MLP layers is common.

### Example Configuration

The following configuration targets all key transformation layers for a causal language model: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
LORA_R = 8
LORA_ALPHA = 32
LORA_DROPOUT = 0.1
LORA_TARGET_MODULES = [
    "q_proj", "k_proj", "v_proj", "o_proj",
    "gate_proj", "up_proj", "down_proj"
]
```

### Attention Modules

For transformer attention mechanisms, the following projection layers are commonly targeted:

- `q_proj` – Query projection
- `k_proj` – Key projection
- `v_proj` – Value projection
- `o_proj` – Output projection

### MLP Modules

For the feed-forward network (MLP) component of transformers:

- `gate_proj` – Gate projection
- `up_proj` – Up projection
- `down_proj` – Down projection

## Additional Parameters

### Task Type (`task_type`)

Specifies the type of task for the LoRA configuration. For causal language modeling:

- **Value**: `TaskType.CAUSAL_LM` ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Inference Mode (`inference_mode`)

Controls whether the adapter is configured for inference or training:

- **Training value**: `False` ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Bias (`bias`)

Controls how bias parameters are handled. Setting to `"none"` keeps the original bias parameters unchanged:

- **Recommended value**: `"none"` ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Use RSLoRA (`use_rslora`)

Controls whether to use Rank-Stabilized LoRA (RSLoRA), a variant that adjusts scaling based on rank:

- **Recommended value**: `False` ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Modules to Save (`modules_to_save`)

Specifies additional modules to train fully (not through low-rank adaptation) alongside the LoRA adapters:

- **Recommended value**: `None` ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Integration with Training Frameworks

### PEFT Library Configuration

When using the [PEFT (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md) library, the LoRA parameters are passed via a `LoraConfig` object: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
from peft import LoraConfig, TaskType, get_peft_model

peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    inference_mode=False,
    r=LORA_R,
    lora_alpha=LORA_ALPHA,
    lora_dropout=LORA_DROPOUT,
    target_modules=LORA_TARGET_MODULES,
    bias="none",
    use_rslora=False,
    modules_to_save=None,
)

model = get_peft_model(model, peft_config)
```

### Learning Rate Adjustment

When using LoRA, the learning rate is typically adjusted higher than for full fine-tuning. A common practice is to multiply the standard learning rate by 10: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
adjusted_lr = LEARNING_RATE * 10 if use_lora else LEARNING_RATE
```

## Memory Efficiency

LoRA dramatically reduces the number of trainable parameters. For a model like [Qwen2-0.5B](/concepts/qwen2-05b-language-model.md), applying LoRA reduces trainable parameters to approximately 1% of the original model parameters. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Parameter Comparison

The training function can report the efficiency of the LoRA configuration: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

| Metric | Value |
|--------|-------|
| Original parameters | Full model parameter count |
| Trainable parameters | LoRA adapter parameters |
| Efficiency ratio | ~1% of original parameters |
| Memory savings | ~99% reduction in gradient memory |

## Related Concepts

- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md)
- [Parameter-Efficient Fine-Tuning](/concepts/parameter-efficient-fine-tuning-peft.md)
- PEFT Configuration
- Qwen2 Model Architecture
- [Distributed Fine-Tuning](/concepts/unsloth-distributed-finetuning-on-databricks.md)
- Mixed Precision Training
- [Gradient Checkpointing](/concepts/activation-checkpointing.md)

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
