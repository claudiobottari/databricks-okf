---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6cec4e4d7bf8008918174dfb679b8a3db487b2664733e8e0edcdcf3c2b7acc0a
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - sfttrainer-supervised-fine-tuning-trainer
    - S(FT
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: SFTTrainer (Supervised Fine-Tuning Trainer)
description: A TRL library component that simplifies supervised fine-tuning configuration by automatically applying optimizations like Liger kernels, mixed precision, gradient checkpointing, and chat format setup.
tags:
  - huggingface
  - fine-tuning
  - trl
  - training-pipeline
timestamp: "2026-06-18T12:06:04.186Z"
---

# SFTTrainer (Supervised Fine-Tuning Trainer)

**SFTTrainer** is a high-level training class from the [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl) library, designed for supervised fine-tuning of causal language models. It simplifies training setup by automatically handling dataset formatting, tokenization, checkpointing, and integration with parameter‑efficient methods like LoRA.

SFTTrainer is used extensively in distributed fine‑tuning workflows on Databricks Serverless GPU Compute, where it runs inside a `@distributed` function across multiple GPUs. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Configuration with `SFTConfig`

Training hyperparameters are passed to SFTTrainer via an `SFTConfig` object. Common fields include:

| Parameter | Description | Example Value |
|-----------|-------------|---------------|
| `output_dir` | Path to save model checkpoints (often a Unity Catalog volume) | `/Volumes/catalog/schema/volume/qwen2-lora` |
| `per_device_train_batch_size` | Batch size per GPU | `8` |
| `gradient_accumulation_steps` | Steps to accumulate gradients | `4` |
| `learning_rate` | Peak learning rate (often scaled 10x for LoRA) | `1e-4` |
| `num_train_epochs` | Number of epochs | `1` |
| `eval_steps` | Evaluation interval | `100` |
| `logging_steps` | Metric logging interval | `25` |
| `save_steps` | Checkpoint saving interval | `100` |
| `save_total_limit` | Maximum number of checkpoints to keep | `2` |
| `report_to` | Experiment tracking destination | `"mlflow"` |
| `run_name` | [MLflow Run](/concepts/mlflow-run.md) name | `"Qwen2-0.5B_fine-tuning"` |
| `fp16` | Mixed‑precision training (half‑precision) | `True` |
| `use_liger_kernel` | Enable Liger Kernel fused operations | `True` |
| `gradient_checkpointing` | Trade compute for memory | `True` |
| `remove_unused_columns` | Whether to strip unused dataset columns | `False` |
| `dataloader_pin_memory` | Memory pinning setting | `False` |

^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Learning Rate Adjustment for LoRA

When using LoRA, the learning rate is often increased by a factor of 10 compared to full fine‑tuning to compensate for the much smaller number of trainable parameters. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
adjusted_lr = LEARNING_RATE * 10 if use_lora else LEARNING_RATE
training_args_dict["learning_rate"] = adjusted_lr
```

## Key Features

### LoRA Integration

SFTTrainer accepts a `peft_config` parameter (a `LoraConfig` object) to attach LoRA adapters to the base model. When LoRA is enabled, only a small fraction (≈1%) of parameters are trainable, dramatically reducing memory and compute requirements. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Liger Kernel Optimizations

Setting `use_liger_kernel=True` in `SFTConfig` enables fused GPU kernels that reduce memory usage by up to 80%. These kernels optimise transformer operations (RMSNorm, RoPE, SwiGLU, CrossEntropy) by combining multiple steps into a single kernel. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Distributed Training Support

SFTTrainer is designed to work with PyTorch Distributed Data Parallel (DDP). When used inside a Databricks `@distributed` decorator that provisions multiple GPUs, each GPU automatically receives a shard of the data and synchronises gradients. The `run_train` function typically returns the [MLflow Run](/concepts/mlflow-run.md) ID for later model registration. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Chat Template Formatting

SFTTrainer can work with tokenizers that have a chat template. The dataset is pre‑processed with `apply_chat_template` (via `formatting_prompts_func`) to convert conversations into the required text format, and the `processing_class` is set to the tokenizer. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### `train_on_responses_only`

A helper function `train_on_responses_only` can be applied to the trainer so that the loss is computed only on the assistant response tokens, ignoring the instruction and user messages. This is especially useful for instruct‑tuned models. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Basic Workflow

A typical SFTTrainer workflow consists of the following steps:

1. **Load model and tokenizer** – using `AutoModelForCausalLM` and `AutoTokenizer`, optionally applying a chat template.
2. **Configure LoRA (optional)** – create a `LoraConfig` with target modules (`q_proj`, `k_proj`, `v_proj`, etc.).
3. **Prepare dataset** – load a conversational dataset and map it with a formatting function that produces a `"text"` column.
4. **Create SFTConfig** – define all training arguments, including output path, batch size, optimiser, and logging.
5. **Instantiate SFTTrainer** – pass model, tokenizer (as `processing_class`), dataset, and training arguments.
6. **Train** – call `trainer.train()`.
7. **Save artifacts** – save the LoRA adapter weights and tokenizer to the output directory.

Example instantiation from the Qwen notebook:

```python
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    processing_class=tokenizer,
    peft_config=peft_config,
)
```

^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Distributed Execution on Serverless GPU

SFTTrainer runs inside a `@distributed`-decorated function. The decorator provisions, for example, 8 H100 GPUs and automatically distributes the data and model shards. Inside the function, the trainer uses the local rank to set the device:

```python
@distributed(gpus=8, gpu_type="H100")
def run_train():
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    torch.cuda.set_device(local_rank)
    # ... load model, tokenizer, create SFTTrainer, train ...
    return mlflow_run_id
```

Only rank 0 saves the final model and tokenizer to prevent race conditions. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Logging and Model Registration

SFTTrainer integrates with MLflow via `report_to="mlflow"`. After training, the [MLflow Run](/concepts/mlflow-run.md) ID is returned and used to log the model to [Unity Catalog](/concepts/unity-catalog.md) using `mlflow.transformers.log_model`. The model is registered with a task (e.g., `"llm/v1/chat"`) and metadata. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) – The PEFT method typically used with SFTTrainer for memory‑efficient fine‑tuning.
- [Liger Kernels](/concepts/liger-kernels.md) – GPU‑optimised fused kernels enabled via `use_liger_kernel`.
- TRL Library – The library that provides SFTTrainer.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance catalog where fine‑tuned models are registered.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Databricks managed compute running the distributed training.
- SFTConfig – The configuration object used to pass hyperparameters to SFTTrainer.

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
2. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
