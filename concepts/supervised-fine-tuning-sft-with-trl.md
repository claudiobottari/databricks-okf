---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa3290620b966de9d9ab8864ec3bc5fa09a1a9ff0a20e8523aa13549157e0657
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supervised-fine-tuning-sft-with-trl
    - SF(WT
    - supervised-fine-tuning-sft-with-sfttrainer
    - SF(WS
    - supervised-fine-tuning-sft-with-trl-library
    - SF(WTL
    - supervised-fine-tuning-sft-with-trl-sfttrainer
    - SF(WTS
  citations:
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: Supervised Fine-Tuning (SFT) with TRL
description: The training paradigm used to fine-tune language models on instruction-following datasets, implemented via the SFTTrainer class from the transformers reinforcement learning (TRL) library.
tags:
  - machine-learning
  - training
  - transformers
timestamp: "2026-06-19T18:52:18.512Z"
---

# Supervised Fine-Tuning (SFT) with TRL

**Supervised Fine-Tuning (SFT)** is a method for adapting a pre-trained [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) to a specific task or domain by training it on a labeled dataset. In the TRL (Transformer Reinforcement Learning) library, the primary component for this is the `SFTTrainer`, which orchestrates the supervised fine-tuning process. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Overview

SFT in TRL is commonly used with [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md) techniques such as [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md), where only a small set of adapter parameters are trained while the base model remains frozen. This reduces memory requirements and training time compared to full fine-tuning. The `SFTTrainer` handles dataset formatting, loss calculation, and training loop management, and can be configured to train only on target token spans (e.g., assistant responses in a chat dataset). ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

In a typical workflow, the base model is loaded with a tokenizer, a PEFT configuration (e.g., LoRA adapters) is applied, the training dataset is tokenized and formatted, and then the `SFTTrainer` is instantiated with `TrainingArguments` to control hyperparameters such as batch size, learning rate, and optimizer. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Using SFTTrainer

The `SFTTrainer` from the `trl` library is configured with the model, tokenizer, training dataset, and `TrainingArguments`. Key hyperparameters set via `TrainingArguments` include:

- `per_device_train_batch_size`: the batch size per GPU
- `gradient_accumulation_steps`: number of steps to accumulate gradients
- `learning_rate`: learning rate (e.g., `2e-4`)
- `max_steps`: total training steps (or `num_train_epochs` for epoch-based training)
- `fp16`/`bf16`: mixed precision settings based on hardware capability
- `optim`: optimizer choice (e.g., `adamw_8bit` for 8-bit Adam)
- `report_to`: tracking service (e.g., `"mlflow"`)

When training with `SFTTrainer`, the training process is automatically tracked if `report_to` is set, enabling metrics (loss, learning rate) and system metrics (GPU utilization, memory) to be logged. The trainer is then executed via `trainer.train()`. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Response-Only Training

A common pattern in SFT for instruction-tuned models is to compute the loss only on the assistant’s response tokens, ignoring the user prompt tokens. This is achieved using the `train_on_responses_only` helper (provided by libraries like Unsloth), which modifies the trainer to mask the instruction part of each training example. The instruction and response parts are identified by token sequences such as `"<|start_header_id|>user<|end_header_id|>\n\n"` and `"<|start_header_id|>assistant<|end_header_id|>\n\n"` for Llama‑3 chat templates. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

This approach improves training efficiency by focusing the model’s learning on the tokens it is expected to generate. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Integration with MLflow and Unity Catalog

SFT training runs can be logged and tracked using [MLflow](/concepts/mlflow.md). By setting `report_to = "mlflow"` in `TrainingArguments` and wrapping the training call in an `mlflow.start_run()` context, all training metrics and system utilization are automatically recorded. After training, the model’s LoRA adapters can be merged with the base model and logged to MLflow for registration in [Unity Catalog](/concepts/unity-catalog.md). The registered model can then be deployed to a [Model Serving](/concepts/model-serving.md) endpoint for inference. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Related Concepts

- [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) – The library providing `SFTTrainer`.
- [Unsloth](/concepts/unsloth.md) – Optimized implementations for PEFT and SFT that accelerate training and reduce memory use.
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) – A PEFT technique commonly used with SFT.
- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md) – The family of methods that SFT with LoRA belongs to.
- [TrainingArguments](/concepts/trainingarguments-configuration.md) – The Hugging Face class for configuring training hyperparameters.
- [Supervised Fine-Tuning](/concepts/supervised-fine-tuning-sft.md) – The general technique of fine-tuning on labeled data.
- [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) – The environment (e.g., AI v5) that includes TRL, Unsloth, and dependencies.

## Sources

- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md

# Citations

1. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
