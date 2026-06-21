---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8419dab438bc069e6b6661c93563139f7b3c71490bb998811da8700ef637c6c6
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsloth-library
  citations:
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: Unsloth Library
description: An optimized library for parameter-efficient fine-tuning (PEFT) of large language models, providing faster training and reduced memory usage through techniques like LoRA.
tags:
  - machine-learning
  - fine-tuning
  - deep-learning
timestamp: "2026-06-19T18:52:02.951Z"
---

# Unsloth Library

**Unsloth** is a library that provides optimized implementations for parameter-efficient fine-tuning (PEFT) techniques, such as LoRA (Low-Rank Adaptation), enabling faster training with reduced memory usage compared to standard PEFT workflows. It is designed to work with Hugging Face models and is particularly suited for fine-tuning large language models. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Overview

Unsloth accelerates fine-tuning by offering memory‑efficient alternatives to standard training components. It can be used to convert a base model into a PEFT model with LoRA adapters, targeting specific layers (e.g., attention and feed‑forward projections). The library supports a range of rank values (commonly 8, 16, 32, 64, 128) and provides options for 4‑bit quantization to further reduce memory footprint. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Key Features

- **Memory Optimization** – Unsloth’s gradient checkpointing mode, activated by setting `use_gradient_checkpointing = "unsloth"`, uses 30% less VRAM and can fit 2× larger batch sizes than standard checkpointing. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **Quantization** – Supports loading models in 4‑bit precision (`load_in_4bit = True`) to reduce memory usage. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **LoRA Variants** – Supports standard LoRA, rank‑stabilized LoRA (`use_rslora`), and LoftQ (`loftq_config`). ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **Hyperparameter Control** – Users can set LoRA rank (`r`), alpha (`lora_alpha`), dropout (`lora_dropout`), bias (`bias`), and target modules. Dropout = 0 and bias = "none" are optimized for performance. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **Integration with Hugging Face Ecosystem** – Works with `FastLanguageModel`, `SFTTrainer` from TRL, and standard Hugging Face tokenizers and data collators. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **Chat Template Support** – Provides utilities like `get_chat_template` and `standardize_sharegpt` to format conversational datasets for instruction tuning. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Usage on Databricks

On Databricks, Unsloth is included in the **AI v5** base environment. No additional installation is required; the environment provides `unsloth`, `unsloth_zoo`, `bitsandbytes`, `trl`, `xformers`, and `mlflow`. Fine‑tuning with Unsloth can be performed on GPU compute (e.g., A10 accelerators) and the resulting model can be logged to [MLflow](/concepts/mlflow.md) and registered in [Unity Catalog](/concepts/unity-catalog.md) for serving. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

A typical workflow involves:

1. Loading the base model with `FastLanguageModel.from_pretrained()`.
2. Applying LoRA adapters with `FastLanguageModel.get_peft_model()`.
3. Preparing the dataset (e.g., using the [FineTome-100k Dataset](/concepts/finetome-100k-dataset.md) or other conversational data).
4. Training with `SFTTrainer` and response‑only masking.
5. Merging adapters and logging the model to MLflow and Unity Catalog.

## Related Concepts

- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md)
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- Quantization (4-bit)
- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)

## Sources

- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md

# Citations

1. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
