---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ff1daab785498dba8132960d01d24900ae8e6d23079461333ea61a8f0c83e55
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sftconfig-and-sfttrainer
    - SFTTrainer and SFTConfig
    - SAS
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: SFTConfig and SFTTrainer
description: Components from the TRL library that simplify supervised fine-tuning configuration and training, handling dataset loading, model initialization, checkpointing, and metric logging.
tags:
  - fine-tuning
  - trl
  - training-configuration
timestamp: "2026-06-18T15:29:46.021Z"
---

# SFTConfig and SFTTrainer

**SFTConfig** and **SFTTrainer** are components from the [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) library that simplify supervised fine-tuning (SFT) of language models. They provide a high-level API for configuring and executing training loops, handling data processing, checkpointing, and integration with experiment tracking tools like [MLflow](/concepts/mlflow.md).

## SFTConfig

SFTConfig is a configuration class that encapsulates all training hyperparameters and settings for supervised fine-tuning. It is instantiated with a dictionary of keyword arguments that define the training behavior. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Common Configuration Parameters

The following parameters are commonly set when creating an SFTConfig instance: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

| Parameter | Example Value | Description |
|-----------|---------------|-------------|
| `output_dir` | `/path/to/output` | Directory for saving model checkpoints and artifacts |
| `per_device_train_batch_size` | `8` | Number of examples per GPU per training step |
| `per_device_eval_batch_size` | `8` | Number of examples per GPU for evaluation |
| `gradient_accumulation_steps` | `4` | Accumulates gradients over multiple batches for effective larger batch size |
| `learning_rate` | `1e-4` | Learning rate for the optimizer |
| `num_train_epochs` | `1` | Number of passes through the training dataset |
| `eval_steps` | `100` | Frequency of evaluation steps |
| `logging_steps` | `25` | Frequency of logging training metrics |
| `save_steps` | `100` | Frequency of saving model checkpoints |
| `save_total_limit` | `2` | Maximum number of checkpoints to keep |
| `report_to` | `"mlflow"` | Experiment tracking destination |
| `run_name` | `"model_fine-tuning"` | Name for the training run |
| `warmup_steps` | `50` | Number of warmup steps for learning rate scheduler |
| `weight_decay` | `0.01` | Weight decay regularization |
| `metric_for_best_model` | `"eval_loss"` | Metric to use for selecting best model |
| `greater_is_better` | `False` | Whether higher metric values are better |
| `dataloader_pin_memory` | `False` | Whether to pin memory in data loader |
| `remove_unused_columns` | `False` | Whether to remove unused columns from dataset |
| `use_liger_kernel` | `True` | Enable [Liger Kernels](/concepts/liger-kernels.md) for memory-efficient training |
| `fp16` | `True` | Enable mixed precision training (FP16) |
| `gradient_checkpointing` | `True` | Enable gradient checkpointing to reduce memory |
| `gradient_checkpointing_kwargs` | `{"use_reentrant": False}` | Additional arguments for gradient checkpointing |

### Example Usage

```python
from trl import SFTConfig

training_args_dict = {
    "output_dir": OUTPUT_DIR,
    "per_device_train_batch_size": BATCH_SIZE,
    "per_device_eval_batch_size": BATCH_SIZE,
    "gradient_accumulation_steps": GRADIENT_ACCUMULATION_STEPS,
    "learning_rate": adjusted_lr,
    "num_train_epochs": NUM_EPOCHS,
    "eval_steps": EVAL_STEPS,
    "logging_steps": LOGGING_STEPS,
    "save_steps": SAVE_STEPS,
    "save_total_limit": 2,
    "report_to": "mlflow",
    "run_name": f"{MODEL_NAME}_fine-tuning",
    "warmup_steps": 50,
    "weight_decay": 0.01,
    "metric_for_best_model": "eval_loss",
    "greater_is_better": False,
    "dataloader_pin_memory": False,
    "remove_unused_columns": False,
    "use_liger_kernel": True,
    "fp16": True,
    "gradient_checkpointing": True,
    "gradient_checkpointing_kwargs": {"use_reentrant": False},
}

training_args = SFTConfig(**training_args_dict)
```

^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## SFTTrainer

SFTTrainer is the training class that orchestrates the supervised fine-tuning process. It accepts the model, training arguments, datasets, tokenizer, and optional [PEFT (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md) configuration such as [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Constructor Parameters

The SFTTrainer constructor accepts the following key arguments: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

| Parameter | Description |
|-----------|-------------|
| `model` | The model to fine-tune (can be a base model or PEFT-wrapped model) |
| `args` | An `SFTConfig` instance with training hyperparameters |
| `train_dataset` | The training dataset |
| `eval_dataset` | The evaluation/validation dataset |
| `processing_class` | The tokenizer for processing text data |
| `peft_config` | Optional PEFT configuration (e.g., `LoraConfig`) |

### Example Usage

```python
from trl import SFTTrainer

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

### Training Execution

Once configured, training is started by calling the `train()` method on the trainer instance: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
trainer.train()
```

### Saving Models

After training completes, the model and tokenizer can be saved using the `save_model()` method: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
trainer.save_model(training_args.output_dir)
tokenizer.save_pretrained(training_args.output_dir)
```

## Integration with Distributed Training

SFTConfig and SFTTrainer work seamlessly with distributed training frameworks. When used with the `@distributed` decorator from [Serverless GPU Compute](/concepts/serverless-gpu-compute.md), the training automatically distributes across multiple GPUs. The `gradient_checkpointing_kwargs` parameter with `"use_reentrant": False` is required when combining LoRA with [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Related Concepts

- [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) — The library that provides SFTConfig and SFTTrainer
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) — Parameter-efficient fine-tuning technique commonly used with SFTTrainer
- [Liger Kernels](/concepts/liger-kernels.md) — GPU-optimized kernels that can be enabled via SFTConfig
- [PEFT (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md) — Configuration passed to SFTTrainer for efficient training
- [MLflow](/concepts/mlflow.md) — Experiment tracking integration via `report_to` parameter
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Distributed training environment for running SFTTrainer
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Parallelism strategy compatible with SFTTrainer

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
