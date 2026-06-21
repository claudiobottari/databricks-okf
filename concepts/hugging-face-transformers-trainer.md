---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec81079fd84eb4363c75342ea0d652bb7e5fce8ff3ae134f6a2116eccb7f2fa6
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hugging-face-transformers-trainer
    - HFTT
    - Hugging Face Transformers
    - HuggingFace Transformers
    - Fine-tuning Hugging Face models with Transformers
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: Hugging Face Transformers Trainer
description: A high-level training utility from the Hugging Face transformers library that orchestrates model fine-tuning, evaluation, and checkpointing with minimal boilerplate.
tags:
  - machine-learning
  - huggingface
  - fine-tuning
timestamp: "2026-06-19T10:32:15.173Z"
---

# Hugging Face Transformers Trainer

The **Hugging Face Transformers Trainer** is a utility class provided by the Hugging Face `transformers` library that simplifies the training and fine-tuning of Transformer models. It handles the training loop, evaluation, logging, and checkpointing, allowing users to focus on model configuration and data preparation. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Overview

The `Trainer` class works with Auto Model classes from Hugging Face to load and fine-tune pretrained models for tasks such as text classification, sequence labeling, and question answering. It is designed to integrate with the Hugging Face ecosystem, including `datasets` and `evaluate` libraries. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Requirements

To use the Trainer, a user must provide:

- **Metrics** – Evaluation metrics (e.g., accuracy) beyond the default `loss` metric that the Trainer computes. Metrics are typically defined using the `evaluate` library and passed via the `compute_metrics` parameter. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- **A base model** – A pretrained model loaded via an Auto Model class, such as `AutoModelForSequenceClassification`. When creating the model, the user must specify the number of classes and label mappings. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- **A training configuration** – An instance of [TrainingArguments](/concepts/trainingarguments-configuration.md) that defines hyperparameters like output directory, evaluation strategy, learning rate, batch size, and whether to use mixed precision (`fp16`). ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Usage

### 1. Define a metric function

The following example adds `accuracy` as an evaluation metric:

```python
import numpy as np
import evaluate

metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### 2. Load a base model

For text classification, use `AutoModelForSequenceClassification`:

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    base_model,
    num_labels=len(label2id),
    label2id=label2id,
    id2label=id2label
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### 3. Configure training arguments

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir=training_output_dir,
    evaluation_strategy="epoch"
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### 4. Prepare a data collator

A DataCollator batches input from training and evaluation datasets. `DataCollatorWithPadding` provides good baseline performance for text classification:

```python
from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### 5. Instantiate the Trainer

```python
from transformers import Trainer

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_test_dataset["train"],
    eval_dataset=train_test_dataset["test"],
    compute_metrics=compute_metrics,
    data_collator=data_collator,
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### 6. Train and save the model

```python
trainer.train()
trainer.save_model(model_output_dir)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Integration with MLflow

The Trainer integrates with [MLflow](/concepts/mlflow.md) through the `MLflowCallback`, which automatically logs training metrics during training. However, the trained model must be logged manually using `mlflow.transformers.log_model`. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import pipeline
import mlflow

with mlflow.start_run() as run:
    trainer.train()
    trainer.save_model(model_output_dir)
    pipe = pipeline(
        "text-classification",
        model=AutoModelForSequenceClassification.from_pretrained(model_output_dir),
        batch_size=1,
        tokenizer=tokenizer,
    )
    mlflow.transformers.log_model(
        transformers_model=pipe,
        artifact_path="classification",
        input_example="Hi there!",
    )
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

Alternatively, the model components can be submitted as a dictionary without creating a pipeline:

```python
mlflow.transformers.log_model(
    transformers_model={"model": trainer.model, "tokenizer": tokenizer},
    task="text-classification",
    artifact_path="text_classifier",
    input_example=["MLflow is great!", "MLflow on Databricks is awesome!"],
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Troubleshooting CUDA Errors

### CUDA Out of Memory

This common error occurs when training large models on a single GPU. Recommended mitigations include:

- Reduce `per_device_train_batch_size` in [TrainingArguments](/concepts/trainingarguments-configuration.md).
- Enable lower‑precision training with `fp16=True`.
- Use `gradient_accumulation_steps` to effectively increase overall batch size without growing per‑device memory.
- Use the 8‑bit Adam optimizer.
- Clean up GPU memory before training with `numba.cuda.get_current_device().reset()`. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### CUDA Kernel Errors

If asynchronous CUDA kernel errors occur, debugging can be aided by setting the environment variable `CUDA_LAUNCH_BLOCKING=1` to get a better stack trace, or by running the code on CPU to check reproducibility. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Related Concepts

- AutoModel – Classes for loading pretrained models by name.
- [TrainingArguments](/concepts/trainingarguments-configuration.md) – Configuration object for training hyperparameters.
- DataCollator – Functions that batch and pad inputs.
- MLflow Callback – Automatic logging of training metrics.
- Fine-tuning on Databricks – End‑to‑end workflows for single‑GPU fine‑tuning.
- Hugging Face Evaluate – Library for defining evaluation metrics.

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
