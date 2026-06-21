---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a31ab9485d912990dc4c6de1fa12ade2776ec8fc324fad2ac4a6fbdf42d40d48
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-for-gpu-fine-tuning
    - DARFGF
  citations:
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: Databricks AI Runtime for GPU Fine-Tuning
description: A pre-configured Databricks environment (AI v5) that bundles Unsloth, bitsandbytes, TRL, xformers, MLflow and other dependencies, optimized for running GPU-accelerated LLM fine-tuning workloads on serverless compute with A10 accelerators.
tags:
  - databricks
  - infrastructure
  - gpu-compute
timestamp: "2026-06-18T12:23:02.666Z"
---



# Databricks AI Runtime for GPU Fine-Tuning

**Databricks AI Runtime for GPU Fine-Tuning** is a purpose-built environment on Databricks that provides pre-configured GPU compute for fine-tuning large language models. It is designed to work with serverless GPU compute options and includes optimized libraries for parameter-efficient fine-tuning (PEFT) techniques like LoRA (Low-Rank Adaptation). ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Overview

The Databricks AI Runtime for GPU Fine-Tuning enables users to fine-tune models such as Llama-3.2-3B using the [Unsloth](/concepts/unsloth.md) library, which provides optimized implementations for faster training with reduced memory usage. The environment is available on Databricks clusters with specific GPU accelerator requirements. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

### Key Features

- **Pre-concluded environment**: The Databricks AI v5 base environment includes Unsloth and its dependencies (`unsloth`, `unsloth_zoo`, `bitsandbytes`, `trl`, `xformers`, and `mlflow`) — no additional installation is needed. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **GPU compute**: Requires an A10 accelerator, selected from the Hardware option in the environment panel. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **Model registration**: Fine-tuned models can be registered in [Unity Catalog](/concepts/unity-catalog.md) and deployed to model serving endpoints. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Compute Requirements

This fine-tuning workload requires GPU compute with an A10 accelerator. When configuring the environment:

1. Select **A10** as the accelerator from the Hardware option.
2. Select **AI v5** from the Base environment option.
3. Click **Apply**.

Compute provisioning can take up to 8 minutes. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Required Libraries

The Databricks AI v5 environment includes all necessary dependencies for fine-tuning:

- `unsloth` — Optimized PEFT implementations
- `unsloth_zoo` — Model and dataset utilities
- `bitsandbytes` — Quantization support
- `trl` — Transformer reinforcement learning
- `xformers` — Memory-efficient attention
- `mlflow` — Experiment tracking and model management

No additional installation is needed. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Fine-Tuning Workflow

A typical fine-tuning workflow using [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) for GPU Fine-Tuning involves:

1. **Configure Unity Catalog**: Set up catalog, schema, model name, and volume for storing checkpoints. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
2. **Load the base model**: Use `FastLanguageModel.from_pretrained()` from Unsloth to load models like `unsloth/Llama-3.2-3B-Instruct` with configurable sequence length (2048 tokens) and automatic dtype detection. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
3. **Apply LoRA adapters**: Convert the base model into a PEFT model by adding LoRA adapters to attention layers. Parameters include rank (`r`), `lora_alpha`, `lora_dropout`, and `bias`. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
4. **Process training data**: Load and format datasets (e.g., FineTome-100k) using the Llama-3.1 chat template. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
5. **Configure SFTTrainer**: Set up the [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md) trainer with training hyperparameters including batch size, learning rate, optimizer, and MLflow tracking. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
6. **Train**: Run the fine-tuning loop with MLflow tracking enabled for metrics and system monitoring. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
7. **Merge and register**: Combine LoRA adapter weights with the base model and register the merged model in Unity Catalog. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
# Example: Load model and apply LoRA
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-3.2-3B-Instruct",
    max_seq_length=2048,
    dtype=None,  # Auto detection
    load_in_4bit=False,
)
```

## Model Registration

After training, the model is logged to MLflow and registered in Unity Catalog with the chat task type (`llm/v1/chat`), making it ready for deployment to model serving endpoints. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Related Concepts

- [Unsloth](/concepts/unsloth.md) — The library providing optimized PEFT implementations
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) — Parameter-efficient fine-tuning technique
- [PEFT (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md) — Fine-tuning approach using adapters
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model management
- [Unity Catalog](/concepts/unity-catalog.md) — Model registry and governance
- [Model Serving](/concepts/model-serving.md) — Deployment of fine-tuned models for inference
- [SFTTrainer](/concepts/sfttrainer.md) — Supervised fine-tuning trainer from TRL

## Sources

- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md

# Citations

1. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
