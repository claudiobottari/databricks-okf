---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 267646e3b740c59e63f4d6ec8222fba4e0d422ab9a923e368d6660276087f4ac
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supervised-fine-tuning-sft-with-trl-library
    - SF(WTL
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: Supervised Fine-Tuning (SFT) with TRL Library
description: A technique for fine-tuning large language models using the TRL SFTTrainer, which provides tools for supervised fine-tuning and reinforcement learning training of LLMs.
tags:
  - fine-tuning
  - llm
  - trl
timestamp: "2026-06-19T18:50:40.168Z"
---

# Supervised Fine-Tuning (SFT) with TRL Library

**Supervised Fine-Tuning (SFT) with TRL Library** refers to the use of the Transformers Reinforcement Learning (TRL) library to perform full-parameter supervised fine-tuning of large language models (LLMs) on a single multi-GPU node. The approach combines TRL's [`SFTTrainer`](https://huggingface.co/docs/trl/sft_trainer) with DeepSpeed ZeRO Stage 3 memory optimization and Databricks AI Runtime to efficiently train models such as Llama 3.2 1B on 8×H100 GPUs. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Overview

SFT with TRL applies the standard supervised fine-tuning loss to a language model using a labeled conversational dataset. The TRL library provides the `SFTTrainer`, which wraps Hugging Face `transformers` training loops and supports data formatting, packing, and integration with custom training arguments. On Databricks AI Runtime, training is orchestrated by the `serverless_gpu` library, which provides a `@distributed` decorator to provision GPU resources and run the training function across multiple GPUs. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Key Components

- **[TRL (Transformers Reinforcement Learning)](/concepts/trl-transformers-reinforcement-learning.md)**: A Hugging Face library that includes the `SFTTrainer` for supervised fine-tuning. It provides built-in support for chat templates, dataset formatting, and DeepSpeed integration. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **DeepSpeed ZeRO Stage 3**: Partitions model parameters, gradients, and optimizer states across all GPUs to reduce per-GPU memory usage. The configuration typically enables bfloat16 precision, overlaps communication with computation, and does not offload to CPU for maximum throughput on H100 hardware. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **AI Runtime**: Databricks-managed GPU compute that automatically provisions and scales GPU resources. An AI Runtime environment (e.g., AI v5) preinstalls most required libraries except for `deepspeed`, which is installed separately. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **`@distributed` decorator**: From the `serverless_gpu` Python library. When applied to a training function, it requests 8 GPUs of a specified type (e.g., `H100`) and executes the function across those GPUs. The decorator handles distributed process setup and communication. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Typical Configuration

A DeepSpeed configuration for SFT with TRL on a single 8×H100 node usually includes: ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

- `bf16: {"enabled": true}` – uses bfloat16 precision.
- `zero_optimization.stage: 3` – enables ZeRO Stage 3.
- `offload_optimizer.device: "none"` and `offload_param.device: "none"` – keeps data on GPU.
- `overlap_comm: true`, `contiguous_gradients: true` – improves communication efficiency.
- `stage3_gather_16bit_weights_on_model_save: true` – ensures full-precision weights are saved.

Training arguments for the `SFTConfig` (or `SFTTrainer`) include: ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

- `per_device_train_batch_size: 2` (effective batch size determined by gradient accumulation).
- `gradient_accumulation_steps: 1`.
- `learning_rate: 2e-4` with cosine scheduler and warmup.
- `max_steps: 60` (for demonstration; full training uses many more steps).
- `bf16: true`, `fp16: false`.
- `optim: "adamw_torch"`.
- `report_to: "mlflow"`.

## Training Workflow

The distributed SFT training function typically performs the following steps inside the `@distributed`‑decorated function: ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

1. Set Hugging Face environment variables (token, etc.).
2. Load the tokenizer (`AutoTokenizer.from_pretrained`) and add a pad token if missing.
3. Load the dataset (e.g., `trl-lib/Capybara`).
4. Write the DeepSpeed configuration to a temporary JSON file.
5. Create an `SFTConfig` or pass training arguments to `SFTTrainer`, including the path to the DeepSpeed config.
6. Initialize `SFTTrainer` with the model name, training arguments, dataset, and tokenizer.
7. Call `trainer.train()`.
8. Save the model with `trainer.save_model()`.
9. Return training results (final loss, [MLflow Run](/concepts/mlflow-run.md) ID, etc.).

The training function is invoked by calling `.distributed()` on the decorated function, which triggers resource provisioning and execution. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Model Saving and Registration

After training, the fine-tuned model can be loaded from the checkpoint directory and tested with a sample prompt. The model and tokenizer can be logged to MLflow and registered in [Unity Catalog](/concepts/unity-catalog.md) using `mlflow.transformers.log_model` with the task set to `"llm/v1/chat"` for conversational use. Unity Catalog volumes are used to store checkpoints during training. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Requirements

The training setup requires: ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

- Databricks AI Runtime with 8×H100 GPU (e.g., AI v5 environment).
- A Unity Catalog catalog, schema, and volume to store checkpoints.
- A Hugging Face access token stored in Databricks secrets to download the base model and dataset.
- The `deepspeed` Python package (version 0.19.1 in the example).

## Related Concepts

- [TRL (Transformers Reinforcement Learning)](/concepts/trl-transformers-reinforcement-learning.md)
- [DeepSpeed ZeRO Stage 3](/concepts/deepspeed-zero-stage-3.md)
- [SFTTrainer](/concepts/sfttrainer.md)
- [Databricks AI Runtime](/concepts/databricks-ai-runtime.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- H100 GPU Support on Databricks
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
