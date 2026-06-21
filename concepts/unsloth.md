---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 45e47f32fb6598d8a7795a647d30d44966908d039a09acbe5c0937c50ff1e14a
  pageDirectory: concepts
  sources:
    - large-language-models-llms-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsloth
  citations:
    - file: large-language-models-llms-databricks-on-aws.md
title: Unsloth
description: An optimization framework for efficiently fine-tuning large language models like Llama
tags:
  - machine-learning
  - fine-tuning
  - llm
  - optimization
timestamp: "2026-06-19T19:11:50.214Z"
---

# Unsloth

**Unsloth** is an open-source optimization library designed to accelerate the fine-tuning of large language models (LLMs) while significantly reducing memory consumption. It provides highly optimized implementations of parameter-efficient fine-tuning (PEFT) techniques, particularly [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md), and integrates seamlessly with the Hugging Face ecosystem. Unsloth is included in the Databricks AI Runtime v5 environment and is commonly used for single-node and multi-GPU distributed training workloads. ^[large-language-models-llms-databricks-on-aws.md]

## Overview

Unsloth focuses on making LLM fine-tuning faster and more memory-efficient through custom kernel implementations and optimized training strategies. It is designed to work with popular model architectures and supports both single-GPU and multi-GPU setups. The library is particularly well-suited for fine-tuning models in the 1B to 70B parameter range, including the Llama family of models. ^[large-language-models-llms-databricks-on-aws.md]

## Key Features

### Optimized LoRA Kernels

Unsloth provides custom, hand-optimized implementations of LoRA operations that are significantly faster and more memory-efficient than standard implementations. These optimized kernels reduce the computational overhead of LoRA training while maintaining model quality. ^[large-language-models-llms-databricks-on-aws.md]

### Gradient Checkpointing

The library offers an enhanced gradient checkpointing mode (`"unsloth"`) that reduces VRAM usage by approximately 30% compared to conventional checkpointing methods. This memory savings enables up to 2× larger batch sizes during training, allowing for more efficient use of available GPU memory. ^[large-language-models-llms-databricks-on-aws.md]

### 4-Bit Quantization

Unsloth supports loading models in 4-bit precision, further reducing memory consumption. This allows fine-tuning of larger models on GPUs with limited VRAM, making LLM fine-tuning more accessible. ^[large-language-models-llms-databricks-on-aws.md]

### Model Merging

After fine-tuning, Unsloth provides a `merge_and_unload()` function that combines trained LoRA adapter weights with the base model. This produces a single, deployable model that can be saved, logged to [MLflow](/concepts/mlflow.md), and registered in [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment. ^[large-language-models-llms-databricks-on-aws.md]

## Integration with Hugging Face Ecosystem

Unsloth integrates tightly with the Hugging Face ecosystem, including:

- **[trl](/concepts/trl-transformer-reinforcement-learning-library.md)** – The Transformer Reinforcement Learning library, particularly the `SFTTrainer` for supervised fine-tuning
- **PEFT** – The Parameter-Efficient Fine-Tuning library for LoRA adapter management
- **Transformers** – For model loading and tokenization

This integration allows users to leverage familiar APIs while benefiting from Unsloth's performance optimizations. ^[large-language-models-llms-databricks-on-aws.md]

## Usage

### Loading a Model

Unsloth's `FastLanguageModel` class provides a convenient interface for loading base models with automatic dtype detection for optimal GPU performance:

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-3.2-3B-Instruct",
    max_seq_length=2048,
    dtype=None,  # Auto-detect best dtype
    load_in_4bit=False,
)
```

^[large-language-models-llms-databricks-on-aws.md]

### Applying LoRA Adapters

The `FastLanguageModel.get_peft_model()` method wraps a loaded model in LoRA adapters, freezing the base weights and making only a small fraction of parameters trainable:

```python
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha=16,
    lora_dropout=0,           # 0 is optimized
    bias="none",              # "none" is optimized
    use_gradient_checkpointing="unsloth",
    random_state=3407,
    use_rslora=False,
    loftq_config=None,
)
```

^[large-language-models-llms-databricks-on-aws.md]

### Training

Unsloth works seamlessly with `SFTTrainer` from the `trl` library. It provides a `train_on_responses_only` helper that modifies the trainer to compute loss only on assistant responses, ignoring user prompt tokens. Training arguments such as batch size, number of steps, optimizer (`adamw_8bit`), and learning rate are passed via `TrainingArguments`. ^[large-language-models-llms-databricks-on-aws.md]

### Distributed Training

For multi-GPU setups, Unsloth can be used with the `@distributed` decorator from the `serverless_gpu` library. This enables scaling fine-tuning across multiple GPUs on a single node (e.g., 8×H100) or across multiple nodes. ^[large-language-models-llms-databricks-on-aws.md]

## Deployment

After fine-tuning, the trained LoRA adapters can be merged with the base model using `PeftModel.merge_and_unload()`. The resulting full-precision model is then logged to [MLflow](/concepts/mlflow.md) and registered in [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment. This workflow is commonly used in production ML pipelines on Databricks. ^[large-language-models-llms-databricks-on-aws.md]

## Use Cases

Unsloth is particularly well-suited for:

- **Parameter-efficient fine-tuning** of LLMs for domain-specific tasks
- **Instruction tuning** of base models to follow user instructions
- **Model customization** for specific use cases without full retraining
- **Resource-constrained environments** where GPU memory is limited

## Related Concepts

- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md)
- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md)
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md)
- [Quantization](/concepts/mxfp4-quantization.md)
- [Gradient Checkpointing](/concepts/activation-checkpointing.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)

## Sources

- large-language-models-llms-databricks-on-aws.md

# Citations

1. [large-language-models-llms-databricks-on-aws.md](/references/large-language-models-llms-databricks-on-aws-bfc38cd2.md)
