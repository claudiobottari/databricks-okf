---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47c091639946befaf718bb1b8614505b79aefc76a707c196a4d6c4679ece51ac
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automodelforsequenceclassification-for-fine-tuning
    - AFF
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: AutoModelForSequenceClassification for Fine-tuning
description: Loading and configuring pre-trained sequence classification models with label mappings for fine-tuning tasks
tags:
  - hugging-face
  - nlp
  - classification
timestamp: "2026-06-18T12:20:33.215Z"
---

# AutoModelForSequenceClassification for Fine-tuning

## Overview

`AutoModelForSequenceClassification` is a Hugging Face Transformers class that loads a pre-trained transformer model with a sequence classification head on top. It is designed for tasks such as sentiment analysis, topic labeling, or any text classification problem where the model must assign a label (or multiple labels) to an input sequence. On Databricks, this class is commonly used in fine-tuning workflows that leverage single-GPU clusters and the Hugging Face `Trainer` utility. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

The class is part of the [Auto Model](https://huggingface.co/docs/transformers/model_doc/auto) family, which automatically selects the correct model architecture based on the checkpoint name. Together with `AutoTokenizer` and `DataCollatorWithPadding`, it provides a streamlined path from a pre-trained checkpoint to a task-specific fine-tuned model. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Loading the Model

To load a model for fine-tuning, call `from_pretrained` with the name of the base checkpoint and task-specific parameters:

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    base_model,
    num_labels=len(label2id),
    label2id=label2id,
    id2label=id2label
)
```

- `num_labels`: The number of output classes.
- `label2id`, `id2label`: Dictionaries that map label names to indices and vice versa. These are created during dataset preparation and ensure the model can map predicted indices to meaningful labels. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

The base model must support sequence classification; common choices include `bert-base-uncased`, `distilbert-base-uncased`, `roberta-base`, or any other compatible checkpoint from the [Hugging Face Hub](https://huggingface.co/models?pipeline_tag=text-classification). ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Setting Up the Training Configuration

The Hugging Face `Trainer` class orchestrates the training loop. Before instantiating the trainer, you need to provide:

- **Tokenized dataset**: Use `AutoTokenizer` to tokenize raw text, then apply the tokenizer with `dataset.map()`.
- **Metrics**: Define a `compute_metrics` function that evaluates predictions. For example, using the `evaluate` library for accuracy:

```python
import numpy as np
import evaluate

metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)
```

- **Training arguments**: Use `TrainingArguments` to set the output directory, evaluation strategy, learning rate, batch size, and other hyperparameters. For single-GPU fine-tuning, pay special attention to `per_device_train_batch_size` and `fp16` to fit within GPU memory.
- **Data collator**: Use `DataCollatorWithPadding` to dynamically pad batches to the longest sequence, improving efficiency.

```python
from transformers import TrainingArguments, Trainer, DataCollatorWithPadding

training_args = TrainingArguments(
    output_dir=training_output_dir,
    evaluation_strategy="epoch",
    per_device_train_batch_size=8,
    fp16=True,
    gradient_accumulation_steps=2
)

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

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Training and Logging to MLflow

Wrap the training call inside an [MLflow Run](/concepts/mlflow-run.md) to automatically log metrics (loss, accuracy, etc.) via the built-in `MLflowCallback`. After training, save the model and log it to the MLflow Model Registry for governance and deployment.

```python
import mlflow
from transformers import pipeline

with mlflow.start_run() as run:
    trainer.train()
    trainer.save_model(model_output_dir)

    # Create a pipeline for inference
    pipe = pipeline(
        "text-classification",
        model=AutoModelForSequenceClassification.from_pretrained(model_output_dir),
        tokenizer=tokenizer,
        batch_size=1
    )

    model_info = mlflow.transformers.log_model(
        transformers_model=pipe,
        artifact_path="classification",
        input_example="Hi there!",
    )
```

Alternatively, you can log the components separately:

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

Once logged, load the model as a PyFunc Spark UDF for batch inference or deploy it via [Model Serving](/concepts/model-serving.md):

```python
logged_model = "runs:/{run_id}/{artifact_path}".format(
    run_id=run.info.run_id,
    model_artifact_path="classification"
)
loaded_model_udf = mlflow.pyfunc.spark_udf(spark, model_uri=logged_model, result_type='string')
```

You can then apply the UDF to a Spark DataFrame:

```python
test = test.select(test.text, test.label, loaded_model_udf(test.text).alias("prediction"))
display(test)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Troubleshooting Common CUDA Errors

When fine-tuning on a single GPU, you may encounter:

- **CUDA out of memory**: Reduce `per_device_train_batch_size`, enable `fp16=True`, use gradient accumulation, adopt the 8-bit Adam optimizer, or clear GPU memory with `cuda.get_current_device().reset()`.
- **CUDA kernel errors**: Run the code on CPU to isolate the issue, or set `CUDA_LAUNCH_BLOCKING=1` for a better traceback.

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Related Concepts

- Hugging Face Transformers — The library providing `AutoModelForSequenceClassification` and the `Trainer`
- [AutoTokenizer](/concepts/autotokenizer-for-transformers.md) — Required for tokenizing input text before fine-tuning
- Trainer — The Hugging Face utility that manages the training loop
- [DataCollatorWithPadding](/concepts/datacollatorwithpadding.md) — Efficient batching with dynamic padding
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Automatic logging of metrics and models during training
- GPU Fine-tuning on Databricks — Best practices for single-GPU training
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying fine-tuned models for continuous evaluation

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
