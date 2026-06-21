---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 232486a52befe78f8b453ffc75e34c3eaee1b616018b7868098346c572cded8d
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - supervised-fine-tuning-sft
    - SF(
    - Supervised Fine-Tuning
    - Supervised Fine‑Tuning (SFT)
    - Fine-Tuning
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Supervised Fine-Tuning (SFT)
description: A training technique that fine-tunes a pre-trained language model on labeled instruction-following data to improve task performance
tags:
  - machine-learning
  - fine-tuning
  - llm
timestamp: "2026-06-19T10:33:28.131Z"
---

# Supervised Fine-Tuning (SFT)

**Supervised Fine-Tuning (SFT)** is a training paradigm in which a pre-trained [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) is further trained on a curated dataset of instruction-output pairs or conversational examples to adapt its behavior for specific tasks or domains. In the context of Databricks AI Runtime and serverless GPU compute, SFT can be implemented using either full fine-tuning or parameter-efficient techniques such as [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md). ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

SFT builds on an existing base model (e.g., Llama 3.2 1B Instruct or GPT-OSS 120B) and trains it on a labeled conversational dataset such as `trl-lib/Capybara` or `HuggingFaceH4/Multilingual-Thinking`. The training is performed using the Transformers Reinforcement Learning (TRL) library's [SFTTrainer](/concepts/sfttrainer.md), which handles the supervised learning loop. Databricks provides serverless GPU compute with H100 accelerators to run such training workloads, automatically provisioning and scaling GPU resources. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Distributed Training Approaches

### DeepSpeed ZeRO Stage 3

For fully fine-tuning models like Llama 3.2 1B, DeepSpeed ZeRO (Zero Redundancy Optimizer) Stage 3 partitions model parameters, gradients, and optimizer states across all GPUs to reduce memory consumption per GPU. This enables training of large models that would not fit in a single GPU's memory. Key configuration settings include bfloat16 precision for faster training, no CPU offloading for maximum performance on H100 hardware, and overlapping gradient communication with computation for efficiency. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

```python
def create_deepspeed_config(stage: int):
    deepspeed_config = {
        "bf16": {"enabled": True},
        "zero_optimization": {
            "stage": stage,
            "offload_optimizer": {"device": "none"},
            "offload_param": {"device": "none"},
            "overlap_comm": True,
            "contiguous_gradients": True,
        },
    }
    return deepspeed_config
```

### FSDP with LoRA

For very large models such as GPT-OSS 120B, SFT typically combines [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) with LoRA adapters. FSDP shards model parameters, gradients, and optimizer states across GPUs using `full_shard auto_wrap` configuration, while LoRA reduces the number of trainable parameters by adding small adapter layers. The FSDP configuration also uses activation checkpointing to further reduce memory usage. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

Key FSDP configuration parameters include:
- `fsdp="full_shard auto_wrap"`: Enables full sharding with automatic layer wrapping
- `fsdp_transformer_layer_cls_to_wrap`: Specifies which transformer block classes to wrap
- `activation_checkpointing`: Enables activation checkpointing to reduce memory
- `reshard_after_forward`: Reshards parameters after each forward pass ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Key Components

### Base Model and Tokenizer

The base model is loaded using Hugging Face's `AutoModelForCausalLM.from_pretrained()` with bfloat16 precision. For very large models, `low_cpu_mem_usage=True` helps with massive checkpoints. The tokenizer is configured with a maximum sequence length (e.g., 2048 tokens) and padding set to the EOS token if no pad token exists. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### LoRA Adapters (Parameter-Efficient Approach)

When using LoRA, adapters are configured via the PEFT library's `LoraConfig`. Common hyperparameters include a rank (`r`) of 32, `lora_alpha` of 32, and targeting all linear modules. Only the adapter weights are trainable, keeping the base model frozen and significantly reducing memory usage. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
peft_config = LoraConfig(
    r=32,
    lora_alpha=32,
    target_modules="all-linear",
    lora_dropout=0.0,
    bias="none",
    task_type="CAUSAL_LM",
)
model = get_peft_model(model, peft_config)
```

### Dataset

The training dataset is loaded from Hugging Face Datasets (e.g., `trl-lib/Capybara` or `HuggingFaceH4/Multilingual-Thinking`). Datasets are typically split into training and evaluation sets for tracking model performance during training. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### SFTTrainer Configuration

The [SFTTrainer](/concepts/sfttrainer.md) from `trl` is configured with training arguments including:
- `per_device_train_batch_size`: Batch size per GPU (e.g., 2 for smaller models, 1 for 120B models)
- `gradient_accumulation_steps`: Number of steps to accumulate gradients (e.g., 1 or 4)
- `learning_rate`: Learning rate (e.g., 2e-4 for smaller models, 1.5e-4 for 120B models)
- `lr_scheduler_type`: Learning rate scheduler (e.g., "cosine" with warmup)
- `bf16`: Enables bfloat16 precision for training
- `max_steps`: Number of training steps (for demonstration, typically 60+)
- `report_to`: MLflow tracking integration (`"mlflow"` or `"none"`)

For DeepSpeed-based training, a separate DeepSpeed configuration file is passed to the trainer. For FSDP-based training, FSDP-specific arguments are passed directly in the `SFTConfig`. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Distributed Training Execution

Training is launched using the `@distributed` decorator from the `serverless_gpu` library, which provisions GPU resources and handles distributed training setup automatically. The decorator specifies the number of GPUs and GPU type (e.g., `gpus=8, gpu_type='H100'`). ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def run_distributed_trl_sft():
    # Training logic here
    trainer = SFTTrainer(
        model=model_config["model_name"],
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        processing_class=tokenizer,
    )
    trainer.train()

# Execute the distributed training
results = run_distributed_trl_sft.distributed()
```

## Model Registration and Deployment

After training, the fine-tuned model (or merged LoRA adapters) is saved to a Unity Catalog volume. The model is then logged to MLflow and registered in [Unity Catalog](/concepts/unity-catalog.md) via `mlflow.transformers.log_model()` with the task type `llm/v1/chat` for conversational AI. This makes the model available for deployment to model serving endpoints. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md) — The family of techniques LoRA belongs to
- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) — Efficient fine-tuning method
- [SFTTrainer](/concepts/sfttrainer.md) — The TRL trainer class used for supervised fine-tuning
- [DeepSpeed](/concepts/deepspeed.md) — Memory optimization library for distributed training
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Sharding strategy for large model training
- [AI Runtime](/concepts/ai-runtime.md) — Databricks-managed GPU compute for training workloads
- [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) — Central repository for model versioning and deployment
- MLflow Integration — Tracking experiments and system metrics during training

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
2. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
