---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5d2bee8f49cff8b6114b75d440f028adfca1ca338da926a8e8dc926a4b91a45
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trainingarguments-for-hugging-face
    - TFHF
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: TrainingArguments for Hugging Face
description: A configuration class in the transformers library used to specify training parameters such as output directory, evaluation strategy, learning rate, batch size, and mixed precision training.
tags:
  - huggingface
  - training-configuration
  - fine-tuning
timestamp: "2026-06-19T10:33:19.068Z"
---

# TrainingArguments for Hugging Face

**TrainingArguments** is a configuration class in the Hugging Face `transformers` library that specifies parameters for training models using the Trainer utility. It controls the output directory, evaluation strategy, learning rate, batch size, precision, and other training hyperparameters.^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Overview

The `TrainingArguments` class is a core component of the Hugging Face training workflow. When creating a Trainer, users must provide a `TrainingArguments` instance that defines how training should proceed. The class accepts numerous parameters that govern every aspect of the training loop.^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Basic Configuration

At minimum, `TrainingArguments` requires an output directory. Additional common parameters include the evaluation strategy and learning rate:^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir=training_output_dir,
    evaluation_strategy="epoch"
)
```

The `evaluation_strategy` parameter controls how often evaluation is performed during training. Setting it to `"epoch"` runs evaluation after each training epoch.^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Key Parameters for GPU Training

When training on a single GPU, several `TrainingArguments` parameters help manage memory and optimize performance:^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Batch Size

The `per_device_train_batch_size` parameter controls the number of samples processed per training step on each device. Reducing this value can help resolve CUDA out-of-memory errors:^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
training_args = TrainingArguments(
    output_dir=output_dir,
    per_device_train_batch_size=8  # Reduce if CUDA out of memory
)
```

### Mixed Precision Training

Setting `fp16=True` enables half-precision (16-bit) floating point training, which reduces GPU memory usage and can speed up training:^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
training_args = TrainingArguments(
    output_dir=output_dir,
    fp16=True
)
```

### Gradient Accumulation

The `gradient_accumulation_steps` parameter allows effective batch sizes larger than the per-device batch size by accumulating gradients over multiple steps before performing an optimizer update:^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
training_args = TrainingArguments(
    output_dir=output_dir,
    gradient_accumulation_steps=4  # Effectively multiplies batch size
)
```

## Troubleshooting with TrainingArguments

When encountering CUDA errors, adjusting `TrainingArguments` parameters is often the first line of defense:^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

- **CUDA OutOfMemoryError**: Reduce `per_device_train_batch_size`, enable `fp16=True`, or increase `gradient_accumulation_steps`.
- **Slow training**: Consider using 8-bit Adam optimizer as an alternative to the default optimizer.

## Integration with MLflow

When using Hugging Face on Databricks, models trained with `TrainingArguments` automatically log metrics during training via the `MLflowCallback`. Users should wrap the training call in an [MLflow Run](/concepts/mlflow-run.md) context to capture the full training history:^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
import mlflow
from transformers import Trainer

with mlflow.start_run() as run:
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        compute_metrics=compute_metrics,
        data_collator=data_collator,
    )
    trainer.train()
```

## Usage with the Trainer

`TrainingArguments` is passed directly to the Trainer constructor alongside the model, datasets, metrics function, and data collator. The Trainer then uses the arguments to configure the training loop, evaluation schedule, and logging behavior.^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Related Concepts

- Trainer Utility — The Hugging Face training wrapper that consumes TrainingArguments
- [AutoModelForSequenceClassification](/concepts/automodelforsequenceclassification.md) — Common model class used with Trainer
- [DataCollatorWithPadding](/concepts/datacollatorwithpadding.md) — Batching utility for padded inputs
- [AutoTokenizer](/concepts/autotokenizer-for-transformers.md) — Tokenizer used to prepare data for training
- [MLflow Integration with Hugging Face](/concepts/mlflow-integration-with-hugging-face.md) — Automatic metric logging during training
- Fine-tuning Hugging Face Models on Databricks — End-to-end workflow guide

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
