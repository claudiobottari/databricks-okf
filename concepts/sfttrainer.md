---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d5586248b7aad39bae979c47d86002d2c6876a16274cbcb4a06d50e6e333c0a
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sfttrainer
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: SFTTrainer
description: A TRL trainer class for supervised fine-tuning that handles dataset formatting, tokenization, and training loop with optional DeepSpeed optimization
tags:
  - machine-learning
  - library
  - training
timestamp: "2026-06-19T10:34:31.829Z"
---

# SFTTrainer

**SFTTrainer** is a class from the [Transformers Reinforcement Learning (TRL)](/wiki/trl) library that provides tools for training language models with supervised fine-tuning (SFT). In the context of Databricks AI Runtime, it is used to efficiently fine-tune large language models like Llama 3.2 1B on GPU hardware, often combined with [DeepSpeed](/wiki/deepspeed) ZeRO Stage 3 optimization for memory efficiency. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Overview

SFTTrainer extends the Hugging Face `Trainer` class to simplify supervised fine-tuning of causal language models. It handles dataset formatting (e.g., chat templates), tokenization, and training loops, while integrating with distributed training frameworks. The example notebook uses SFTTrainer with DeepSpeed ZeRO Stage 3 to partition model parameters, gradients, and optimizer states across 8 H100 GPUs, enabling full fine-tuning of a 1B-parameter model on a single node. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Key Features (from the example)

- **Dataset loading**: Supports Hugging Face datasets; the example uses the `trl-lib/Capybara` conversational dataset. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **Chat formatting**: Automatically applies the model’s chat template via the `processing_class` (tokenizer). ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **DeepSpeed integration**: Accepts a DeepSpeed configuration file (JSON) via the `deepspeed` argument in `SFTConfig`. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **Training arguments**: Configured through `SFTConfig`, which supports all standard Hugging Face `TrainingArguments` plus SFT-specific fields. The example sets batch size, learning rate (2e-4), cosine scheduler, warmup steps, and evaluation strategy. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **Checkpointing and logging**: Saves model checkpoints to a Unity Catalog volume and logs metrics to MLflow via `report_to="mlflow"`. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **Distributed execution**: Wrapped inside a function decorated with `@distributed` (from `serverless_gpu`) that provisions 8 H100 GPUs on Databricks AI Runtime. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Usage in the Example

The notebook initializes SFTTrainer with:

- `model`: the Hugging Face model name (or pre-loaded model).
- `args`: an `SFTConfig` object containing training parameters.
- `train_dataset` / `eval_dataset`: loaded from the Hugging Face dataset.
- `processing_class`: the tokenizer (with pad token added if missing).

Training is started with `trainer.train()`, and after completion the model is saved via `trainer.save_model()`. The fine-tuned model is then logged to MLflow and registered in Unity Catalog using `mlflow.transformers.log_model()`. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Configuration Example

The example defines a DeepSpeed ZeRO Stage 3 config with bfloat16 precision, no CPU offloading, overlap communication, and contiguous gradients. The `SFTConfig` includes settings such as:

```python
SFTConfig(
    output_dir=CHECKPOINT_DIR,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=1,
    learning_rate=2e-4,
    max_steps=60,
    bf16=True,
    deepspeed=deepspeed_config_path,
    report_to="mlflow",
    ...
)
```

^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [TRL](/concepts/trl-transformer-reinforcement-learning.md) – The library that provides SFTTrainer.
- [DeepSpeed](/concepts/deepspeed.md) – Memory optimization strategy used alongside SFTTrainer.
- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md) – The training paradigm implemented by SFTTrainer.
- [AI Runtime](/concepts/ai-runtime.md) – Databricks-managed GPU compute that provisions hardware for training.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry used in conjunction with SFTTrainer.
- [Unity Catalog](/concepts/unity-catalog.md) – Storage and governance for model checkpoints and registered models.
- Hugging Face Transformers – The base library for model loading and tokenization.

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
