---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d04a7c2edabdae28653fb4da28d9966125c6a208a327b4d4c0c53eac2ccbef5
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
    - lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - lora-low-rank-adaptation
    - L(A
    - LoRA (Low‑Rank Adaptation)
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - file: lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: LoRA (Low-Rank Adaptation)
description: A parameter-efficient fine-tuning technique that trains small low-rank adapter matrices while freezing the base model weights, drastically reducing the number of trainable parameters.
tags:
  - fine-tuning
  - parameter-efficiency
  - deep-learning
timestamp: "2026-06-19T18:32:46.514Z"
---

```yaml
---
title: LoRA (Low-Rank Adaptation)
summary: Parameter-efficient fine-tuning technique that trains small adapter layers while freezing the base model, dramatically reducing memory and compute requirements
sources:
  - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  - lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
  - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:01:53.817Z"
updatedAt: "2026-06-19T15:13:40.828Z"
tags:
  - machine-learning
  - fine-tuning
  - optimization
aliases:
  - lora-low-rank-adaptation
  - L(A
confidence: 0.98
provenanceState: merged
inferredParagraphs: 0
---

# LoRA (Low-Rank Adaptation)

**LoRA (Low-Rank Adaptation)** is a parameter-efficient fine-tuning (PEFT) technique that reduces the computational and memory requirements of training large language models by freezing the base model's weights and training only small, low-rank adapter matrices. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## How LoRA Works

LoRA decomposes the weight update ΔW for a given layer into the product of two low‑rank matrices: ΔW = A × B, where A has dimensions (d × r) and B has dimensions (r × d), and r ≪ d. The original pretrained weights W remain frozen; only A and B are updated during training. This reduces the number of trainable parameters by approximately 99% – typically to around 1–2% of the original model's parameter count – while the output quality remains comparable to full fine-tuning. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Key Hyperparameters

### Rank (r)

The rank r controls the size of the adapter matrices. A common value is `r=8`, which provides a good balance between performance and parameter count for models up to several billion parameters. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md] For larger models such as 120B-class architectures, a higher rank like `r=32` is used, sometimes with per-layer rank patterns (e.g., `rank_pattern` for mixture-of-experts layers) to further optimize memory. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Alpha (α)

The scaling factor α controls the influence of the LoRA update on the frozen base model. It is typically set to 2–4× the rank value; `lora_alpha=32` is a common choice when `r=8`, while `lora_alpha=16` is also used. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md] For very large models, α may be set equal to the rank (e.g., `lora_alpha=32` with `r=32`). ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Dropout

Dropout applies regularization to the LoRA adapter layers to prevent overfitting. Typical values are `lora_dropout=0.1` or `lora_dropout=0.05`. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md] For very large models, dropout may be set to 0.0 to avoid additional overhead. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Target Modules

LoRA is applied to specific layers in the transformer architecture. For models like Qwen2 and many other causal language models, the target modules typically include all linear projection layers in the attention and feed‑forward blocks:

- **Attention**: `q_proj`, `k_proj`, `v_proj`, `o_proj`
- **MLP**: `gate_proj`, `up_proj`, `down_proj`

Alternatively, the parameter `target_modules="all-linear"` can be used to apply LoRA to every linear layer in the model, which is common for large or custom architectures. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Memory and Performance Benefits

LoRA reduces gradient memory requirements by approximately 99% compared to full fine-tuning, enabling training on single GPUs (such as A10 or A100) that would otherwise be unable to hold the full model's gradients. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

When combined with [[Liger Kernels]] – fused GPU operations that reduce memory transfers – the overall memory savings can reach up to 80% on relevant operations. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

For very large models, LoRA can be combined with [[MXFP4 quantization]] to further reduce memory requirements during training. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

When used with [[Fully Sharded Data Parallel (FSDP)]], LoRA enables training of 120B parameter models on a single node of 8 H100 GPUs, sharding both the frozen base model weights and the LoRA adapters across devices. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Training with LoRA

### Using the PEFT Library

The PEFT library provides the `LoraConfig` and `get_peft_model` APIs to apply LoRA to any Hugging Face Transformers model. The following example shows a typical configuration for a causal language model: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

```python
from peft import LoraConfig, TaskType, get_peft_model

peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    inference_mode=False,
    r=8,
    lora_alpha=32,
    lora_dropout=0.1,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    bias="none",
)
model = get_peft_model(base_model, peft_config)
```

The learning rate is typically scaled 10× higher for LoRA training compared to full fine-tuning, as recommended by the LoRA paper. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

### Merging and Unloading

After training, the LoRA adapter can be merged into the base model using `merge_and_unload()`, producing a single weight matrix that can be served without the PEFT wrapper. Alternatively, adapters can be kept separate and loaded on top of the base model at inference time with `PeftModel.from_pretrained()`. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

### Unified Artifact Saving

When using [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md)'s `SFTTrainer`, the `trainer.save_model()` method saves only the LoRA adapter weights (not the full base model), and the tokenizer can be saved separately with `tokenizer.save_pretrained()`. Both are stored to a Unity Catalog volume for governance and later deployment. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

### Distributed Training with LoRA

For very large models, LoRA is frequently combined with distributed strategies. The `@distributed` decorator from the `serverless_gpu` library can orchestrate training across multiple GPUs, automatically handling data distribution and synchronization. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md] When using [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), LoRA adapters are sharded along with the base model; FSDP configuration parameters such as `fsdp_transformer_layer_cls_to_wrap` and `activation_checkpointing` are set to handle the additional memory demands. ^[fine-tune-openais-gpt-

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
2. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
3. [lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md](/references/lora-fine-tuning-of-qwen2-05b-databricks-on-aws-e40ade8f.md)
4. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
