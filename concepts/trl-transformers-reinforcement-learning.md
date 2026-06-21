---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 977bc1969d9c35e77474168ecdf6724daa743dd159887f93d3c03954139d7052
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trl-transformers-reinforcement-learning
    - T(RL
    - Transformers Reinforcement Learning (TRL)
    - Reinforcement Learning from Human Feedback (RLHF)
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: TRL (Transformers Reinforcement Learning)
description: A Hugging Face library providing tools for training language models with reinforcement learning and supervised fine-tuning
tags:
  - machine-learning
  - library
  - llm-training
timestamp: "2026-06-19T10:34:02.278Z"
---

# TRL (Transformers Reinforcement Learning)

**TRL (Transformers Reinforcement Learning)** is a Python library that provides tools for training language models with reinforcement learning and supervised fine-tuning (SFT).^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Overview

TRL is designed to fine-tune large language models using techniques such as Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF). It is part of the [Hugging Face](/concepts/hugging-face-trainer.md) ecosystem and works seamlessly with Transformers and Datasets libraries.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

In the context of [Databricks AI Runtime](/concepts/databricks-ai-runtime.md), TRL is used with [DeepSpeed](/concepts/deepspeed.md) ZeRO Stage 3 optimization to efficiently train models like Llama 3.2 1B on multiple GPUs.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Key Components

### SFTTrainer

`SFTTrainer` is the primary class for supervised fine-tuning of language models. It handles dataset formatting, tokenization, and training loops.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

```python
from trl import SFTTrainer
```

### SFTConfig

`SFTConfig` is used to configure training arguments such as batch size, learning rate, and evaluation strategy.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

```python
from trl import SFTConfig
```

### Datasets

TRL provides or integrates with datasets for conversational AI training, such as the Capybara dataset (`trl-lib/Capybara`).^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Usage Example (from Databricks Notebook)

The following example illustrates a typical setup for SFT training using TRL with DeepSpeed on 8 H100 GPUs:

1. Load the tokenizer and dataset.
2. Create a DeepSpeed configuration (ZeRO Stage 3).
3. Initialize `SFTTrainer` with the model name, `SFTConfig`, and dataset.
4. Call `trainer.train()`.
5. Save the trained model and log metrics to [MLflow](/concepts/mlflow.md).

```python
from trl import SFTTrainer, SFTConfig

training_args = SFTConfig(
    output_dir=CHECKPOINT_DIR,
    per_device_train_batch_size=2,
    learning_rate=2e-4,
    max_steps=60,
    deepspeed=deepspeed_config_path,
    report_to="mlflow",
)

trainer = SFTTrainer(
    model=model_config["model_name"],
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    processing_class=tokenizer,
)

trainer.train()
trainer.save_model()
```

^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Integration with DeepSpeed

TRL integrates with DeepSpeed ZeRO optimization stages to reduce memory consumption and enable distributed training of large models. In production usage, ZeRO Stage 3 partitions model parameters, gradients, and optimizer states across GPUs, allowing training of models that would otherwise exceed a single GPU's memory.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

TRL's `SFTConfig` accepts a `deepspeed` parameter pointing to a configuration file. The library handles the distributed setup when executed on multi-GPU hardware.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md)
- [DeepSpeed ZeRO](/concepts/deepspeed-zero-stage-3.md)
- Hugging Face Transformers
- [Databricks AI Runtime](/concepts/databricks-ai-runtime.md)
- [MLflow](/concepts/mlflow.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

## Sources

- `fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md`

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
