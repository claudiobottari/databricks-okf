---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 304db9f4257ab856af8217fcbadeebdc53253e8c1220f52450889d59a840b388
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hugging-face-trainer-utility-on-databricks
    - HFTUOD
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: Hugging Face Trainer Utility on Databricks
description: How to use the Hugging Face Transformers Trainer class for fine-tuning on single-GPU Databricks clusters
tags:
  - machine-learning
  - hugging-face
  - databricks
timestamp: "2026-06-18T12:20:16.572Z"
---

# Hugging Face `Trainer` Utility on Databricks

The **Hugging Face `Trainer` Utility** is a built‑in class in the `transformers` library that simplifies fine‑tuning and evaluation of transformer models. On Databricks, it integrates naturally with [MLflow](/concepts/mlflow.md) for experiment tracking and model logging, and it can leverage single‑GPU clusters to train models on data from the lakehouse. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Overview

The `Trainer` class handles the training loop, evaluation, checkpointing, and logging. Users provide a model, training arguments, datasets, tokenizers, and optional metrics. Databricks recommends wrapping the training call in an [MLflow Run](/concepts/mlflow-run.md) so that metrics and the trained model are automatically tracked and can be served later. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Requirements

- A single‑node cluster with one GPU on the driver. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- Databricks Runtime 13.0 ML (GPU version) or above (includes `transformers`, `datasets`, and `evaluate`). ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- MLflow 2.3 or later. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- Data prepared and loaded for fine‑tuning (see Load data for Hugging Face fine‑tuning). ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Workflow

### 1. Tokenize the Dataset

Hugging Face models expect tokenized input. Use `AutoTokenizer.from_pretrained(base_model)` and apply the tokenizer to the training and test datasets via the `.map()` method. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model)

def tokenize_function(examples):
    return tokenizer(examples["text"], padding=False, truncation=True)

train_test_tokenized = train_test_dataset.map(tokenize_function, batched=True)
```

### 2. Configure Training

Define evaluation metrics (e.g., accuracy), load the appropriate Auto Model (e.g., `AutoModelForSequenceClassification`), and create a `TrainingArguments` object to specify the output directory, evaluation strategy, learning rate, batch size, and other hyperparameters. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
import numpy as np
import evaluate

metric = evaluate.load("accuracy")
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained(
    base_model,
    num_labels=len(label2id),
    label2id=label2id,
    id2label=id2label
)

from transformers import TrainingArguments, Trainer
training_args = TrainingArguments(
    output_dir=training_output_dir,
    evaluation_strategy="epoch"
)
```

Use `DataCollatorWithPadding` to batch inputs for training and evaluation. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import DataCollatorWithPadding
data_collator = DataCollatorWithPadding(tokenizer)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_test_tokenized["train"],
    eval_dataset=train_test_tokenized["test"],
    compute_metrics=compute_metrics,
    data_collator=data_collator,
)
```

### 3. Train and Log to MLflow

Wrap the training in an [MLflow Run](/concepts/mlflow-run.md) using `mlflow.start_run()`. After calling `trainer.train()`, save the model and log it with `mlflow.transformers.log_model`. You can log either a pipeline or the raw model and tokenizer dictionary. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import pipeline

with mlflow.start_run() as run:
    trainer.train()
    trainer.save_model(model_output_dir)
    pipe = pipeline(
        "text-classification",
        model=AutoModelForSequenceClassification.from_pretrained(model_output_dir),
        batch_size=1,
        tokenizer=tokenizer
    )
    model_info = mlflow.transformers.log_model(
        transformers_model=pipe,
        artifact_path="classification",
        input_example="Hi there!",
    )
```

Alternatively, log the model and tokenizer dictionary directly. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### 4. Load the Model for Inference

Load the logged model as a Spark UDF or as a regular PyFunc model for batch or real‑time inference. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
logged_model = "runs:/{run_id}/{artifact_path}"
loaded_model_udf = mlflow.pyfunc.spark_udf(spark, model_uri=logged_model, result_type='string')
test = test.select(test.text, test.label, loaded_model_udf(test.text).alias("prediction"))
```

## Troubleshooting CUDA Errors

### OutOfMemoryError

Reduce the `per_device_train_batch_size` in `TrainingArguments`, enable FP16 (`fp16=True`), increase `gradient_accumulation_steps`, or use the 8‑bit Adam optimizer. Clearing GPU memory with Numba’s `cuda.reset()` may also help. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### CUDA Kernel Errors

Set the environment variable `CUDA_LAUNCH_BLOCKING=1` to get a detailed stack trace, or rerun on CPU to isolate the issue. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Additional Resources

- What are Hugging Face Transformers?
- Model inference using Hugging Face Transformers for NLP
- [MLflow Tracking on Databricks](/concepts/mlflow-tracing-in-databricks.md)
- [Deploy models using Model Serving](/concepts/mlflow-model-serving-and-deployment.md)

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
