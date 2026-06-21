---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 129aa43f93f19a267978de1b9f83d63417a3c5dbc61b888e9d080f80a913044e
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lora-finetuning-with-unsloth-on-llama-32
    - LFWUOL3
    - Fine-tuning with Unsloth
    - finetune Llama 3.2 3B with Unsloth
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: LoRA Finetuning with Unsloth on Llama 3.2
description: The specific recipe for applying Low-Rank Adaptation (LoRA) to Llama-3.2-3B-Instruct using Unsloth's FastLanguageModel API, including hyperparameters like r=16, lora_alpha=16, and target module selection.
tags:
  - peft
  - lora
  - llama
  - finetuning
timestamp: "2026-06-19T18:34:53.545Z"
---

# LoRA Finetuning with Unsloth on Llama 3.2

**LoRA Finetuning with Unsloth on Llama 3.2** refers to the process of efficiently fine-tuning Meta's Llama 3.2 family of small language models using the Unsloth optimization library combined with Low-Rank Adaptation (LoRA). This approach enables distributed training across multiple GPUs, significantly reducing memory requirements and training time while maintaining model quality. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Overview

The technique applies [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) to Llama 3.2 models — specifically the 1B and 3B parameter variants. By using Unsloth's optimized implementations and 4-bit quantization, the fine-tuning process can run on consumer-grade hardware or scale efficiently across multiple H100 GPUs in a serverless environment. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Prerequisites

### Compute Configuration

Successful distributed fine-tuning requires:
- **8xH100 Single-Node Configuration**: Eight NVIDIA H100 80GB GPUs on a single compute node
- **AI v5 Environment**: A Databricks runtime environment that includes the complete Unsloth stack

The AI v5 environment comes pre-installed with all required dependencies:
- `unsloth` and `unsloth_zoo`
- `trl` (Transformer Reinforcement Learning)
- `peft` (Parameter-Efficient Fine-Tuning)
- `bitsandbytes` (quantization library)
- `xformers` (memory-efficient attention)
- `einops` (tensor operations)

Additional installation is not needed. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Environment Variables

The environment variable `UNSLOTH_COMPILE_DISABLE` should be set to `1` to disable model compilation, which may interfere with distributed training. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Implementation Steps

### 1. Model and Data Selection

Choose from the Llama 3.2 family:
- `unsloth/Llama-3.2-3B-Instruct` (3 billion parameters)
- `unsloth/Llama-3.2-1B-Instruct` (1 billion parameters)

Training can use datasets like `mlabonne/FineTome-100k`. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 2. Distributed Setup

The `serverless_gpu` library provides a `@distributed` decorator to orchestrate training across multiple GPUs on a single node. Within the decorated function, each process accesses its local rank and global rank to coordinate work. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type='h100')
def run_train():
    # Distributed training code here
```

### 3. Model Loading with LoRA Configuration

The fine-tuning process begins by loading the base model with [Unsloth](/concepts/unsloth.md)'s `FastLanguageModel`, applying 4-bit quantization to reduce memory footprint. A LoRA adapter is then configured with specified target modules, rank (`r`), and alpha scaling. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

Key LoRA parameters:
- `r=16`: The rank of the low-rank matrices
- `target_modules`: The attention and feed-forward projection layers
- `lora_alpha=16`: Scaling factor for LoRA updates
- `lora_dropout=0`: Disabled for optimization
- `use_gradient_checkpointing=True`: Reduces memory usage

For [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), non-reentrant gradient checkpointing must be enabled to avoid the "mark a variable ready only once" error. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 4. Data Preparation

The dataset is processed using Unsloth's chat template system. The `get_chat_template` function applies the Llama 3.1 chat format, and `standardize_sharegpt` ensures consistent data formatting. The `formatting_prompts_func` applies the chat template to each conversation in the dataset. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 5. Training Configuration

Training uses the [SFTTrainer](/concepts/sfttrainer.md) from the `trl` library with [TrainingArguments](/concepts/trainingarguments-configuration.md) configured for distributed GPU training:

- `per_device_train_batch_size=2`: Batch size per GPU
- `gradient_accumulation_steps=4`: Accumulates gradients before weight update
- `max_steps=25`: Number of training steps (or use `num_train_epochs=1` for full epoch)
- `learning_rate=2e-4`: Standard learning rate for fine-tuning
- `fp16`/`bf16`: Mixed precision training based on hardware support
- `report_to="mlflow"`: Logs metrics to [MLflow](/concepts/mlflow.md) for tracking

The `train_on_responses_only` utility focuses training on assistant responses rather than the full conversation, improving efficiency. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 6. Model Saving and Registration

After training, the model and tokenizer are saved to a Unity Catalog Volume for persistent storage. The LoRA adapters are saved separately from the base model. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Model Registration with MLflow and Unity Catalog

The complete workflow includes registering the fine-tuned model:

1. **Merge LoRA adapters**: The LoRA weights are merged into the base model using `merge_and_unload()`
2. **Log to MLflow**: The merged model and tokenizer are logged as a transformers pipeline with task `llm/v1/chat`
3. **Register in Unity Catalog**: The model is registered with versioning, metadata, and governance controls ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Performance Characteristics

| Aspect | Details |
|--------|---------|
| **Memory** | 4-bit quantization reduces memory usage significantly |
| **Speed** | LoRA trains only a small fraction of parameters, enabling faster iteration |
| **Quality** | LoRA adapters preserve base model capabilities while adapting to new tasks |
| **Scalability** | The `@distributed` decorator enables seamless scaling across 8 GPUs |

## Limitations

- The method is designed for single-node multi-GPU setups; cross-node distributed training requires additional configuration
- 4-bit quantization may slightly reduce final model quality compared to full-precision training
- The dataset must be in a [ShareGPT format](/concepts/sharegpt-dataset-format-standardization.md) for compatibility with Unsloth's standardization functions

## Related Concepts

- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md)
- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md)
- [Unsloth](/concepts/unsloth.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- 4-bit Quantization
- [SFTTrainer](/concepts/sfttrainer.md)
- [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
