---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a1658decb6de473d74342ead4363e6cd048a1fb138ff17de60d754442f21f1a6
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsloth-lora-configuration
    - ULC
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Unsloth LoRA Configuration
description: The specific pattern of applying LoRA adapters via `FastLanguageModel.get_peft_model()` in Unsloth, targeting q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj with rank 16 and zero dropout for optimized training.
tags:
  - lora
  - peft
  - unsloth
  - parameter-efficient-fine-tuning
timestamp: "2026-06-19T15:14:41.952Z"
---

# Unsloth LoRA Configuration

**Unsloth LoRA Configuration** refers to the set of parameters and options used when applying [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) to a language model through the Unsloth library, typically in a Databricks environment. Unsloth provides optimized implementations for efficient fine-tuning, and its LoRA configuration is exposed via the `FastLanguageModel.get_peft_model()` method. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Parameters

The core LoRA configuration in the Unsloth notebook uses the following settings:

- `r`: 16 – The rank of the adaptation matrices. Suggested values are 8, 16, 32, 64, 128.
- `lora_alpha`: 16 – The scaling factor for the LoRA updates.
- `lora_dropout`: 0 – Dropout rate applied to LoRA layers. A value of 0 is optimized for performance, but any value is supported.
- `bias`: "none" – Whether to train bias parameters. "none" is optimized.
- `use_gradient_checkpointing`: True – Enables gradient checkpointing to reduce memory usage during training.
- `random_state`: 3407 – Random seed for reproducibility.
- `use_rslora`: False – Disables rank-stabilized LoRA; Unsloth supports this feature but it is turned off by default.
- `loftq_config`: None – LoftQ initialization is not used in this configuration.

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

The `target_modules` parameter specifies which linear layers receive LoRA adapters:

```python
target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                "gate_proj", "up_proj", "down_proj"]
```

These modules correspond to the query, key, value, and output projections of the attention mechanism, as well as the feed-forward network gates and projections. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Quantization

Unsloth supports loading the base model in 4‑bit quantization via the `load_in_4bit` parameter of `FastLanguageModel.from_pretrained()`. In the example configuration this is set to `False` to use full precision (suitable for H100 GPUs). When enabled, 4‑bit quantization can significantly reduce memory usage. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Distributed Training Considerations

When using [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) on multiple GPUs, Unsloth’s LoRA configuration requires non‑reentrant gradient checkpointing to avoid errors such as “mark a variable ready only once”. This is enforced by calling:

```python
model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
```

The device placement is handled by setting `device_map={'': local_rank}` where `local_rank` is derived from the environment variable `LOCAL_RANK`. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Environment and Dependencies

The recommended environment on Databricks for Unsloth LoRA training is **AI v5**, which includes `unsloth`, `unsloth_zoo`, `trl`, `peft`, `bitsandbytes`, `xformers`, and `einops` — no additional installation is needed. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Usage with SFTTrainer

After applying the LoRA configuration with `get_peft_model()`, the model is passed to [SFTTrainer](/concepts/sfttrainer.md) from the `trl` library for supervised fine‑tuning. The trainer is further wrapped with `train_on_responses_only()` from Unsloth to train only on the assistant’s responses rather than the full conversation. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- FastLanguageModel – The Unsloth class used for loading and configuring models with LoRA.
- LoRA – General concept of low-rank adaptation.
- [SFTTrainer](/concepts/sfttrainer.md) – The TRL trainer used together with Unsloth models.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Parallelism strategy for multi‑GPU training.
- [Gradient Checkpointing](/concepts/activation-checkpointing.md) – Memory optimization technique required for DDP with Unsloth.
- [Unsloth](/concepts/unsloth.md) – The library providing efficient fine‑tuning implementations.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – Typical compute setup for distributed Unsloth training on Databricks.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
