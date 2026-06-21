---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f1c8a2913349e5ab04985f8fabcb0b9bf0ef5ea2db7e9af514b4c78243ec9db
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - low-rank-adaptation-lora-for-parameter-efficient-fine-tuning
    - LA(FPF
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Low-Rank Adaptation (LoRA) for Parameter-Efficient Fine-Tuning
description: A technique that reduces the number of trainable parameters by adding small adapter layers to a frozen base model, making fine-tuning of large language models more memory and compute efficient.
tags:
  - fine-tuning
  - parameter-efficiency
  - llm
timestamp: "2026-06-18T12:22:06.976Z"
---

# Low-Rank Adaptation (LoRA) for Parameter-Efficient Fine-Tuning

**Low-Rank Adaptation (LoRA)** is a parameter-efficient fine-tuning (PEFT) technique that reduces the number of trainable parameters in large language models by injecting small, low-rank adapter matrices into the model's existing weight layers. Instead of updating all model parameters during fine-tuning, LoRA freezes the pre-trained weights and only trains the lightweight adapter modules, dramatically reducing memory and computational requirements while maintaining competitive performance. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Motivation and Core Idea

Fine-tuning large models with hundreds of billions of parameters is computationally prohibitive on standard hardware. Full fine-tuning requires storing and updating gradients, optimizer states, and all model weights for every parameter, quickly exhausting GPU memory. LoRA addresses this by observing that the weight updates needed for task-specific adaptation have low "intrinsic rank"—meaning they can be represented as the product of two much smaller matrices. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

Formally, for a pre-trained weight matrix $W \in \mathbb{R}^{d \times k}$, LoRA constrains its update $\Delta W$ to be:

$$\Delta W = B A$$

where $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times k}$, and the rank $r \ll \min(d, k)$. Only $A$ and $B$ are trained; the original $W$ remains frozen. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Typical Configuration

| Parameter | Common Value | Purpose |
|-----------|-------------|---------|
| r (rank) | 8–32 | Controls adapter capacity; lower r means fewer parameters but may limit expressiveness |
| lora_alpha | 16–32 | Scaling factor for the adapter update |
| lora_dropout | 0.0–0.1 | Regularization; often set to 0.0 for stability |
| bias | "none" | Whether to train bias terms alongside adapters |
| target_modules | "all-linear" | Which layers to apply adapters; often all attention and feed-forward projections |

In practice, `r=32` and `lora_alpha=32` with `target_modules="all-linear"` is a common starting configuration for large models. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Training with LoRA

### Using PEFT and TRL Libraries

The Hugging Face ecosystem provides the `peft` (Parameter-Efficient Fine-Tuning) library for LoRA configuration and the `trl` (Transformers Reinforcement Learning) library for training. These are typically combined with `accelerate` for distributed training orchestration. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM
from trl import SFTTrainer

peft_config = LoraConfig(
    r=32,
    lora_alpha=32,
    target_modules="all-linear",
    lora_dropout=0.0,
    bias="none",
    task_type="CAUSAL_LM",
)

model = AutoModelForCausalLM.from_pretrained("openai/gpt-oss-120b", dtype=torch.bfloat16)
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()
```

After wrapping with `get_peft_model`, only the adapter weights are trainable. The base model weights remain frozen. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### LoRA with FSDP

When combining LoRA with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), the LoRA adapter parameters (initialized in float32 by default) must be cast to the same dtype as the base model—typically bfloat16—so FSDP sees a uniform dtype across all parameters. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
model = model.to(torch.bfloat16)  # Cast LoRA adapters to bfloat16
```

## Advantages Over Full Fine-Tuning

- **Memory reduction**: LoRA reduces the number of trainable parameters from billions (for a 120B model) to tens of millions. The adapters typically consume <1% of the model's total parameters. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Faster training**: With fewer parameters to update, each training step completes faster, and gradient accumulation can be higher without exceeding GPU memory. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Portability**: LoRA adapters are small files (often <100 MB) that can be stored, shared, and swapped independently of the base model. A single base model can serve multiple tasks by loading different adapters. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- **Composability**: LoRA adapters can be merged or combined with other adapters, enabling multi-task learning without separate full model copies. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## When to Use LoRA

LoRA is most effective when:

- The target model is very large (10B+ parameters) and does not fit on a single GPU in full-precision mode
- The fine-tuning budget is limited to consumer-grade or mid-range GPU hardware (e.g., 8 × H100 GPUs)
- You need to maintain multiple task-specific adapters for the same base model
- The downstream task requires only moderate capacity (i.e., the weight update has low intrinsic rank)

LoRA is less suited for tasks that require extensive model-wide rewiring (e.g., changing the model's fundamental architecture) or when the full-model fine-tuning budget is already available. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md) — The family of techniques that includes LoRA, Adapters, and Prefix Tuning
- [Fully Shaded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — A complementary technique for distributing training across GPUs
- [Transformers Reinforcement Learning (TRL)](/concepts/trl-transformers-reinforcement-learning.md) — The training library that provides the `SFTTrainer`
- Hugging Face Transformers — The model architecture library used with LoRA
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Another distributed training strategy often combined with LoRA
- [Quantization](/concepts/mxfp4-quantization.md) — A technique that further reduces memory when combined with LoRA
- Model Adapters — The general concept of lightweight, task-specific modules added to pre-trained models

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
