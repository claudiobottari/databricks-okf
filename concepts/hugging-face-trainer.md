---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18dd8a53bbd11b8a73a694819365192a7a751232d29e87757fa1863ea5ed4607
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hugging-face-trainer
    - HFT
    - HuggingFace Trainer API
    - Hugging Face
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: Hugging Face Trainer
description: The Trainer utility from Hugging Face transformers library for fine-tuning models, including metrics, data collators, and training configuration.
tags:
  - huggingface
  - fine-tuning
  - machine-learning
timestamp: "2026-06-19T18:49:29.854Z"
---

# Hugging Face Trainer

**Hugging Face Trainer** is a utility class provided by the Hugging Face `transformers` library that simplifies the training and evaluation of Transformer models. It handles the training loop, evaluation, and logging, allowing users to focus on model architecture, data preparation, and configuration. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Overview

The `Trainer` class abstracts away much of the boilerplate code required for training deep learning models. It is part of the Hugging Face ecosystem and works seamlessly with other components such as AutoModel classes, [AutoTokenizer](/concepts/autotokenizer-for-transformers.md), and Datasets. The Trainer is designed for both single-GPU and multi-GPU training scenarios. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Requirements for Trainer Setup

To use the `Trainer`, users must provide three core components:

1. **Metrics**: Evaluation metrics beyond the default `loss` metric that the Trainer computes automatically.
2. **A base model**: A pre-trained model loaded using Hugging Face Auto Model classes.
3. **A training configuration**: Training parameters specified through the [TrainingArguments](/concepts/trainingarguments-configuration.md) class.

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Configuring the Trainer

### Defining Evaluation Metrics

In addition to the default `loss` metric, users can configure custom evaluation metrics. The following example demonstrates adding `accuracy` as a metric using the `evaluate` library:

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

### Loading the Base Model

For text classification, use [AutoModelForSequenceClassification](/concepts/automodelforsequenceclassification.md) to load a base model. When creating the model, provide the number of classes and label mappings prepared during dataset preparation:

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

### Creating TrainingArguments

The [TrainingArguments](/concepts/trainingarguments-configuration.md) class allows specification of training parameters such as output directory, evaluation strategy, learning rate, and batch size:

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir=training_output_dir,
    evaluation_strategy="epoch"
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Using a Data Collator

A [data collator](/concepts/datacollatorwithpadding.md) batches input in training and evaluation datasets. [DataCollatorWithPadding](/concepts/datacollatorwithpadding.md) provides good baseline performance for text classification tasks:

```python
from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Instantiating the Trainer

With all components prepared, the Trainer is instantiated as follows:

```python
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

## Training and Logging with MLflow

Hugging Face integrates well with [MLflow](/concepts/mlflow.md). The MLflowCallback automatically logs metrics during model training. However, the trained model must be logged manually. Training is wrapped in an [MLflow Run](/concepts/mlflow-run.md), and the model can be logged using `mlflow.transformers.log_model`:

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

Alternatively, components used in training can be submitted as a dictionary:

```python
model_info = mlflow.transformers.log_model(
    transformers_model={"model": trainer.model, "tokenizer": tokenizer},
    task="text-classification",
    artifact_path="text_classifier",
    input_example=["MLflow is great!", "MLflow on Databricks is awesome!"],
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Loading the Model for Inference

Once logged, the model can be loaded for inference as a Spark UDF:

```python
logged_model = "runs:/{run_id}/{model_artifact_path}".format(
    run_id=run.info.run_id,
    model_artifact_path=model_artifact_path
)

loaded_model_udf = mlflow.pyfunc.spark_udf(
    spark,
    model_uri=logged_model,
    result_type='string'
)

test = test.select(
    test.text,
    test.label,
    loaded_model_udf(test.text).alias("prediction")
)
display(test)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Common CUDA Troubleshooting

### OutOfMemoryError: CUDA Out of Memory

This error occurs when training large models on GPUs with limited memory. Recommended solutions include:

- **Reduce batch size**: Decrease `per_device_train_batch_size` in [TrainingArguments](/concepts/trainingarguments-configuration.md).
- **Use lower precision training**: Set `fp16=True` in [TrainingArguments](/concepts/trainingarguments-configuration.md).
- **Use gradient accumulation**: Increase `gradient_accumulation_steps` in [TrainingArguments](/concepts/trainingarguments-configuration.md) to effectively increase overall batch size.
- **Use 8-bit Adam optimizer**: Reduce memory footprint with the 8-bit Adam optimizer.
- **Clean up GPU memory**: Use `numba.cuda` to reset the device before training.

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### CUDA Kernel Errors

CUDA kernel errors may be reported asynchronously, making debugging difficult. Troubleshooting steps include:

- Run the code on CPU to check if the error is reproducible.
- Set `CUDA_LAUNCH_BLOCKING=1` to get better tracebacks:

```python
import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Related Concepts

- AutoModel — Classes for loading pre-trained Transformer models
- [AutoTokenizer](/concepts/autotokenizer-for-transformers.md) — Tokenizer loading for model compatibility
- [TrainingArguments](/concepts/trainingarguments-configuration.md) — Configuration class for training parameters
- [DataCollatorWithPadding](/concepts/datacollatorwithpadding.md) — Collator for batching padded inputs
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model logging platform
- Text Classification — Common task for fine-tuning with Trainer
- Fine-tuning — The process of adapting a pre-trained model to a specific task

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
