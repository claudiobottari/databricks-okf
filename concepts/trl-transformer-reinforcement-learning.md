---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 599224c8655dc0e0184c0c60495ce05156defa0de24db4e6f88813130b07cf4d
  pageDirectory: concepts
  sources:
    - lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trl-transformer-reinforcement-learning
    - T(RL
    - Transformer Reinforcement Learning (TRL)
    - Reinforcement Learning
    - Reinforcement Learning|reinforcement learning
    - Reinforcement learning
  citations:
    - file: lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
title: TRL (Transformer Reinforcement Learning)
description: A Hugging Face library for training language models using reinforcement learning and supervised fine-tuning, providing SFTTrainer and other abstractions.
tags:
  - machine-learning
  - library
  - fine-tuning
timestamp: "2026-06-19T19:17:49.274Z"
---

--- SOURCE: lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md ---

We are given the full content of that source file. We will rewrite the TRL page using only that source, keeping the existing YAML front matter but updating the body and the Sources section.

```markdown
---
title: TRL (Transformer Reinforcement Learning)
summary: A Hugging Face library for training language models with reinforcement learning and supervised fine-tuning (SFT), providing SFTConfig and SFTTrainer components.
sources:
  - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  - lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
  - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:02:17.746Z"
updatedAt: "2026-06-18T15:29:33.460Z"
tags:
  - reinforcement-learning
  - fine-tuning
  - huggingface
aliases:
  - trl-transformer-reinforcement-learning
  - T(RL
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# TRL (Transformer Reinforcement Learning)

**TRL (Transformer Reinforcement Learning)** is a library developed by Hugging Face for training language models using reinforcement learning and supervised fine-tuning (SFT). It provides high-level components such as `SFTConfig`, `SFTTrainer`, and `setup_chat_format` that simplify the configuration and execution of fine-tuning workflows. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Key Components

### SFTTrainer

`SFTTrainer` is the core trainer class for supervised fine-tuning. It accepts a model, training arguments, dataset, tokenizer, and an optional PEFT configuration. The trainer handles the training loop, evaluation, checkpointing, and logging. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

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

### SFTConfig

`SFTConfig` defines the hyperparameters and runtime settings for supervised fine-tuning, including batch size, learning rate, gradient accumulation steps, maximum steps, evaluation intervals, logging frequency, and output directory. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

```python
training_args = SFTConfig(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=8,
    learning_rate=2e-4,
    max_steps=200,
    use_liger_kernel=True,   # Enable Liger Kernel optimizations
    fp16=True,               # Mixed precision
    report_to="mlflow",
)
```

### setup_chat_format

`setup_chat_format` is a utility that applies a chat template (e.g., ChatML) to the model and tokenizer when no template is present. This ensures that conversation-style datasets are correctly formatted for instruction-following or dialogue fine-tuning tasks. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Usage

### Supervised Fine-Tuning with LoRA

TRL is commonly used alongside the PEFT library to apply LoRA adapters, which freeze the base model weights and only train small adapter matrices, reducing the number of trainable parameters by approximately 99%. The `peft_config` parameter of `SFTTrainer` accepts a LoraConfig object, allowing the trainer to manage adapter training seamlessly. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

### Memory Optimizations

TRL integrates with [[Liger Kernels]] for GPU‑optimized fused operations that can reduce memory usage by up to 80%. Setting `use_liger_kernel=True` in `SFTConfig` enables these optimizations. Additionally, TRL supports mixed-precision training (`fp16=True`) and gradient checkpointing to further reduce memory consumption. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

### Integration with MLflow and Unity Catalog

During training, TRL can report metrics to [[MLflow]] by setting `report_to="mlflow"` in `SFTConfig`. After training completes, the fine‑tuned model (including merged LoRA adapters) can be logged to [[Unity Catalog]] using `mlflow.transformers.log_model()`, storing model artifacts, tokenizer, and metadata for governance and deployment. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Related Concepts

- [[Supervised Fine-Tuning (SFT)]]
- [[Parameter-Efficient Fine-Tuning (PEFT)|PEFT (Parameter-Efficient Fine-Tuning)]]
- [[LoRA (Low-Rank Adaptation)]]
- [[Liger Kernels]]
- SFTConfig
- [[SFTTrainer]]
- [[Serverless GPU Compute]]
- [[Unity Catalog]]
- [[MLflow Tracking]]

## Sources

- lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
```

# Citations

1. [lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md](/references/lora-fine-tuning-of-qwen2-05b-databricks-on-aws-e40ade8f.md)
