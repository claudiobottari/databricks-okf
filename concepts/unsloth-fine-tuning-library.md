---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e23a8648611d3f51b86f93502de3150233d9b84fac0a1f0f430432d4ecf4ce59
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsloth-fine-tuning-library
    - UFL
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Unsloth Fine-Tuning Library
description: An optimized library for faster LLM fine-tuning that supports LoRA/QLoRA, reduced memory usage, and integrated chat templates, included in Databricks AI v5 runtime.
tags:
  - llm
  - fine-tuning
  - optimization
timestamp: "2026-06-18T12:03:12.594Z"
---

# Unsloth Fine-Tuning Library

The **Unsloth Fine-Tuning Library** is an open-source framework designed to accelerate and optimize the fine-tuning of large language models (LLMs) through memory-efficient techniques, including LoRA (Low-Rank Adaptation), 4-bit quantization, and optimized kernel implementations. It is particularly well-suited for distributed training environments and integrates seamlessly with MLflow and Unity Catalog for model tracking and governance.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Overview

Unsloth provides a streamlined API built on top of popular libraries such as `transformers`, `peft`, `trl`, and `bitsandbytes`. It simplifies loading, fine-tuning, and saving large language models while reducing memory footprint and training time. The library supports multiple GPU architectures and can be used in both single-GPU and multi-GPU distributed setups.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Key Features

### FastLanguageModel API

The core interface for loading and preparing models is `FastLanguageModel`, which handles model loading, tokenizer setup, and LoRA adapter configuration. It automatically selects the optimal data type (`float16`, `bfloat16`) based on the available hardware and supports loading models in 4-bit precision to dramatically reduce memory usage.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from unsloth import FastLanguageModel, is_bfloat16_supported

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-3.2-3B-Instruct",
    max_seq_length=2048,
    load_in_4bit=False,
)
```

### LoRA and PEFT Support

Unsloth integrates with [PEFT (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md) to enable LoRA fine-tuning with minimal added parameters. Users can specify target modules, rank, alpha, dropout, and other LoRA hyperparameters. The library optimizes LoRA configurations, such as setting dropout to zero for maximum efficiency.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing=True,
    random_state=3407,
    use_rslora=False,
    loftq_config=None,
)
```

### Chat Template Integration

Unsloth provides utilities for handling chat templates through the `get_chat_template` and `standardize_sharegpt` functions. These tools simplify the conversion of conversational datasets into the format expected by instruction-tuned models, such as those following the Llama-3.1 chat template.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from unsloth.chat_templates import get_chat_template, standardize_sharegpt

tokenizer = get_chat_template(tokenizer, chat_template="llama-3.1")
```

### Training on Responses Only

The `train_on_responses_only` function allows the trainer to mask instruction parts during training, focusing the loss computation only on the assistant's responses. This improves training efficiency for instruction-following tasks and is applied after the `SFTTrainer` is created.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from unsloth.chat_templates import train_on_responses_only

trainer = train_on_responses_only(
    trainer,
    instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
    response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
)
```

## Distributed Training

Unsloth is compatible with distributed training frameworks. The library can be used alongside utilities like `serverless_gpu.distributed` to scale fine-tuning across multiple GPUs. In distributed settings, it is critical to import `unsloth` before any other library such as `trl` to ensure proper initialization.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Multi-GPU Setup

For multi-GPU training, the model is loaded with a device map that assigns each GPU a rank, and gradient checkpointing is disabled for non-reentrant mode to avoid errors in distributed data parallel (DDP) setups.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
local_rank = int(os.environ.get("LOCAL_RANK", 0))
torch.cuda.set_device(local_rank)
model, tokenizer = FastLanguageModel.from_pretrained(
    ..., device_map={'': local_rank},
)
model.gradient_checkpointing_enable(
    gradient_checkpointing_kwargs={"use_reentrant": False}
)
```

## Integration with MLflow and Unity Catalog

Unsloth fine-tuning workflows can be tracked using [MLflow](/concepts/mlflow.md) for experiment logging and artifact management. After training, models can be registered in [Unity Catalog](/concepts/unity-catalog.md) via `mlflow.transformers.log_model` with the `registered_model_name` parameter. The merged LoRA model (base model + adapter weights) is logged as a single unit to ensure deployment readiness.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
import mlflow
from peft import PeftModel

base_model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
peft_model = PeftModel.from_pretrained(base_model, adapter_dir)
merged_model = peft_model.merge_and_unload()

with mlflow.start_run():
    model_info = mlflow.transformers.log_model(
        transformers_model={"model": merged_model, "tokenizer": tokenizer},
        artifact_path="model",
        task="llm/v1/chat",
        registered_model_name=f"{catalog}.{schema}.{model_name}",
    )
```

## Environment Setup

Unsloth is included in the **AI v5** runtime environment on Databricks, which also provides supporting dependencies such as `unsloth_zoo`, `trl`, `peft`, `bitsandbytes`, `xformers`, and `einops`. For optimal performance, it is recommended to disable the `UNSLOTH_COMPILE_DISABLE` environment variable control if compilation is not desired.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Hardware Recommendations

The library supports a variety of GPU architectures:^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

- **T4 / V100**: Use `float16` precision with 4-bit quantization enabled
- **Ampere and newer (A100, H100)**: Use `bfloat16` for mixed precision training
- **Multiple H100s**: Distributed training across 8 H100 GPUs is supported for larger models

## Related Concepts

- LoRA Fine-Tuning — Low-rank adaptation for parameter-efficient LLM training
- [PEFT (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md) — The underlying library for adapter-based fine-tuning
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment logging for ML models
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and model registry for Databricks
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Scaling training across multiple GPUs
- 4-bit Quantization — Memory reduction technique via `bitsandbytes`
- [SFTTrainer](/concepts/sfttrainer.md) — Supervised fine-tuning trainer from the `trl` library

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
