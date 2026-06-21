---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d26a1d6ceb6a03a42ee490efe8021903c17eb59740dbde3fb473b6f5e4cfb9b
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sfttrainer-trl
    - SFTTrainer from TRL
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
title: SFTTrainer (TRL)
description: A supervised fine-tuning trainer from the Transformer Reinforcement Learning (TRL) library that streamlines instruction tuning of language models with built-in support for LoRA, gradient checkpointing, and mixed precision.
tags:
  - fine-tuning
  - huggingface
  - trl
timestamp: "2026-06-19T18:32:38.709Z"
---

---

title: SFTTrainer (TRL)
summary: Supervised fine-tuning trainer from the Transformer Reinforcement Learning (TRL) library, used with Hugging Face models for instruction tuning
sources:
  - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:29:14.873Z"
updatedAt: "2026-06-18T15:29:14.873Z"
tags:
  - machine-learning
  - training
  - huggingface
aliases:
  - sfttrainer-trl
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1

---

# SFTTrainer (TRL)

**SFTTrainer** is a trainer class from the [TRL](/concepts/trl-transformer-reinforcement-learning-library.md) (Transformer Reinforcement Learning) library that simplifies supervised fine-tuning (SFT) of language models. It handles the training loop, loss computation, logging, and integrates with Hugging Face Transformers and PEFT (Parameter-Efficient Fine-Tuning) libraries. It is commonly used alongside techniques like LoRA and [MXFP4 Quantization](/concepts/mxfp4-quantization.md) to reduce memory requirements during training.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Usage

SFTTrainer is instantiated with a model, training arguments (SFTConfig), a training dataset, and a tokenizer (or processor). The following example from a distributed training notebook demonstrates its usage:^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
from trl import SFTTrainer

trainer = SFTTrainer(
    model=peft_model,
    args=training_args,
    train_dataset=dataset,
    processing_class=tokenizer,
)
```

After instantiation, calling `trainer.train()` runs the training loop. The trainer also supports saving the model with `trainer.save_model()`.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Configuration with SFTConfig

Training hyperparameters are passed via an SFTConfig object. Common parameters shown in the source include:^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

- `learning_rate` – initial learning rate (e.g., `2e-4`).
- `num_train_epochs` – number of training epochs (e.g., `1`).
- `logging_steps` – frequency of logging steps (e.g., `1`).
- `per_device_train_batch_size` – batch size per device (e.g., `1`).
- `gradient_accumulation_steps` – steps to accumulate gradients before updating (e.g., `2`).
- `gradient_checkpointing` – enables gradient checkpointing to reduce memory.
- `max_length` – maximum sequence length for tokenization (e.g., `2048`).
- `warmup_ratio` – ratio of warmup steps (e.g., `0.03`).
- `lr_scheduler_type` – scheduler type, e.g., `"cosine_with_min_lr"`.
- `lr_scheduler_kwargs` – additional scheduler arguments, e.g., `{"min_lr_rate": 0.1}`.
- `output_dir` – directory for saving checkpoints.
- `report_to` – reporting destination, e.g., `"mlflow"`.
- `push_to_hub` – whether to push the model to Hugging Face Hub.
- `logging_dir` – directory for TensorBoard logs.
- `disable_tqdm` – disable progress bars.
- `ddp_find_unused_parameters` – option for distributed training.

## Integration with Distributed Training

SFTTrainer supports distributed data parallelism (DDP) natively. In the source notebook, the trainer is used inside a function decorated with `@distributed(gpus=8, gpu_type="h100")`, which provisions 8 H100 GPUs and automatically handles data parallelism across them. The trainer’s `gradient_accumulation_steps` and `per_device_train_batch_size` are set to accommodate multi-GPU training.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Related Concepts

- [TRL](/concepts/trl-transformer-reinforcement-learning-library.md) – The library containing SFTTrainer and other RLHF tools.
- SFTConfig – Configuration class for training hyperparameters.
- LoRA – Parameter-efficient fine-tuning method often used with SFTTrainer.
- [MXFP4 Quantization](/concepts/mxfp4-quantization.md) – Memory reduction technique used in conjunction with SFTTrainer.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Parallelism strategy supported by SFTTrainer.
- Hugging Face Transformers – Base model and tokenizer interface.

## Sources

- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
