---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e940b322eced8d898d8a8e7f40df4c1c7be32b9178779f5dee91269691c76030
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsloth-distributed-finetuning-on-databricks
    - UDFOD
    - Distributed Fine-Tuning
    - distributed fine-tuning
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Unsloth Distributed Finetuning on Databricks
description: Methodology for fine-tuning large language models like Llama-3.2-3B across multiple GPUs using the Unsloth library within the Databricks environment on AWS.
tags:
  - machine-learning
  - fine-tuning
  - distributed-training
  - databricks
timestamp: "2026-06-18T15:30:06.626Z"
---

# Unsloth Distributed Finetuning on Databricks

**Unsloth Distributed Finetuning on Databricks** refers to the practice of using the [Unsloth](/concepts/unsloth.md) library together with serverless GPU compute on Databricks to perform distributed fine-tuning of large language models (LLMs) across multiple GPUs. This approach leverages Unsloth’s optimized kernels and LoRA adapters to reduce memory usage and training time while scaling across up to eight H100 GPUs using the `serverless_gpu` library. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Overview

Databricks provides a notebook-based workflow that demonstrates fine-tuning a Llama-3.2-3B model using Unsloth on eight H100 GPUs. The environment uses the **AI v5** base environment, which includes all necessary dependencies (`unsloth`, `unsloth_zoo`, `trl`, `peft`, `bitsandbytes`, `xformers`, `einops`) without additional installation. The training is executed on serverless GPU compute with a `@distributed` decorator that handles process spawning, device assignment, and inter-GPU communication. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Setup

### Compute Configuration

The notebook requires selecting **8xH100** as the accelerator in the Databricks environment panel and choosing **AI v5** as the base environment. Applying this configuration can take up to eight minutes. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Environment Variables and Widgets

Before running training, users set the environment variable `UNSLOTH_COMPILE_DISABLE=1` and configure Databricks widgets for Unity Catalog parameters: catalog, schema, model name, and a volume path for checkpoint storage. The model can be selected from Unsloth’s model zoo, with examples including `unsloth/Llama-3.2-3B-Instruct` or `unsloth/Llama-3.2-1B-Instruct`. The dataset used in the example is `mlabonne/FineTome-100k`. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Distributed Training Architecture

### Process Management

The `serverless_gpu.distributed` decorator is applied to a function `run_train`, specifying 8 GPUs of type H100. Distributed process rank is obtained via the `LOCAL_RANK` environment variable, and each process sets its CUDA device accordingly. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Model Loading and LoRA Configuration

The model is loaded with `FastLanguageModel.from_pretrained`, which auto-detects the dtype (bfloat16 on Ampere+, float16 on older GPUs) and supports optional 4-bit quantization. The model is assigned to the correct GPU using `device_map={'': local_rank}`. A LoRA adapter is then applied via `FastLanguageModel.get_peft_model` with target modules (`q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`), rank 16, and other standard Hyperparameters. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Gradient Checkpointing for DDP

For distributed data parallelism, the notebook sets non-reentrant gradient checkpointing: `model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})`. This avoids the "mark a variable ready only once" error common in DDP. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Data Processing

The tokenizer is configured with the Llama 3.1 chat template. A formatting function applies the template to each conversation example. The dataset is loaded and standardized using `standardize_sharegpt`, then mapped with the formatting function. The training uses `SFTTrainer` from `trl` with a `DataCollatorForSeq2Seq` and no packing (`packing=False`). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Training Configuration

Key training arguments:

| Argument | Value |
|----------|-------|
| `per_device_train_batch_size` | 2 |
| `gradient_accumulation_steps` | 4 |
| `max_steps` | 25 |
| `learning_rate` | 2e-4 |
| `optim` | `adamw_8bit` |
| `weight_decay` | 0.01 |
| `lr_scheduler_type` | `linear` |
| `report_to` | `mlflow` |

The trainer also applies `train_on_responses_only` to mask the instruction part during loss computation, using `<|start_header_id|>user<|end_header_id|>\n\n` and `<|start_header_id|>assistant<|end_header_id|>\n\n` as delimiters. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Saving Checkpoints

Only the rank-0 process saves the trained model and tokenizer to the output directory (a Unity Catalog volume). The [MLflow Run](/concepts/mlflow-run.md) ID is captured and returned by the distributed function. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Model Registration

After training completes, the notebook loads the base model and tokenizer from Hugging Face, then loads the LoRA adapter from the saved checkpoint. The adapter is merged into the base model using `merge_and_unload()` to produce a standalone model. The model is then logged to MLflow with `mlflow.transformers.log_model`, specifying the task `llm/v1/chat` and registering it in Unity Catalog under the given catalog, schema, and model name. Metadata includes the pretrained model name and `databricks_model_family: "Llama3.2"`. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Unsloth](/concepts/unsloth.md) – Optimized LLM training library with fast kernels and LoRA support.
- PEFT LoRA – Parameter-efficient fine-tuning via low-rank adapters.
- [SFTTrainer](/concepts/sfttrainer.md) – `trl` trainer for supervised fine-tuning.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Databricks ephemeral GPU clusters for training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Alternative distributed strategy for larger models.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and model registry for ML assets.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment logging and model versioning.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
