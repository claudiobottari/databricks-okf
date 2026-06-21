---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ce89c9b5b8b2e6a81ea5b3230897d7e3b49e94edd3ab889be79c952aebc6611
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - single-gpu-fine-tuning-with-hugging-face-on-databricks
    - SFWHFOD
    - Fine-tuning Hugging Face Models
    - Fine-tuning Hugging Face models
    - Fine‑tuning Hugging Face Models
    - fine-tune a Hugging Face model
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: Single-GPU Fine-Tuning with Hugging Face on Databricks
description: The end-to-end workflow for fine-tuning Hugging Face transformer models on a single GPU node in Databricks, covering cluster setup, tokenization, training configuration, MLflow logging, and inference loading.
tags:
  - databricks
  - huggingface
  - gpu
  - fine-tuning
timestamp: "2026-06-19T10:32:55.250Z"
---

# Single-GPU Fine-Tuning with Hugging Face on Databricks

**Single-GPU Fine-Tuning with Hugging Face on Databricks** describes how to fine-tune a Hugging Face model using the `transformers` library on a single GPU within the Databricks environment. The process leverages the Hugging Face [Trainer](https://huggingface.co/docs/transformers/main_classes/trainer) utility and [Auto Model](https://huggingface.co/docs/transformers/model_doc/auto) classes, and includes Databricks-specific recommendations for loading data from the lakehouse and logging models to MLflow, enabling governance and model serving. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Requirements

- A single‑node cluster with one GPU on the driver.
- Databricks Runtime 13.0 ML or above (GPU version).
- The `🤗 Transformers`, `🤗 Datasets`, and `🤗 Evaluate` packages (included in Databricks Runtime 13.0 ML and above).
- MLflow 2.3.
- Data prepared and loaded for fine‑tuning with transformers. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Tokenize a Hugging Face Dataset

Hugging Face Transformers models expect tokenized input. Use an [AutoTokenizer](https://huggingface.co/docs/transformers/v4.26.1/en/autoclass_tutorial#autotokenizer) loaded from the base model to convert text into tokens. The `datasets` library allows you to apply the tokenizer consistently to both training and testing data using the `.map()` function. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(base_model)

def tokenize_function(examples):
    return tokenizer(examples["text"], padding=False, truncation=True)

train_test_tokenized = train_test_dataset.map(tokenize_function, batched=True)
```

## Set up the Training Configuration

### Metrics

In addition to the default `loss` metric, you can add custom evaluation metrics such as accuracy. The `evaluate` library can be used to load and compute metrics. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
import numpy as np
import evaluate

metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)
```

### Base Model

For text classification, load a model using [AutoModelForSequenceClassification](https://huggingface.co/docs/transformers/v4.26.1/en/model_doc/auto#transformers.AutoModelForSequenceClassification). Provide the number of classes and the label mappings created during dataset preparation. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    base_model,
    num_labels=len(label2id),
    label2id=label2id,
    id2label=id2label
)
```

### Training Arguments

Use [TrainingArguments](https://huggingface.co/docs/transformers/v4.26.1/en/main_classes/trainer#transformers.TrainingArguments) to specify the output directory, evaluation strategy, learning rate, and other parameters. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir=training_output_dir,
    evaluation_strategy="epoch"
)
```

### Data Collator

A data collator batches inputs in the training and evaluation datasets. [DataCollatorWithPadding](https://huggingface.co/docs/transformers/v4.26.1/en/main_classes/data_collator#transformers.DataCollatorWithPadding) provides good baseline performance for text classification. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer)
```

### Trainer

With all components ready, create a [Trainer](https://huggingface.co/docs/transformers/main_classes/trainer) instance. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

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

## Train and Log to MLflow

Hugging Face integrates with MLflow through the [MLflowCallback](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.MLflowCallback), which automatically logs metrics during training. The trained model must be logged manually using [mlflow.transformers.log_model](https://mlflow.org/docs/latest/models.html#transformers-transformers-experimental). ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

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

Alternatively, you can submit the components used in training as a dictionary without creating a pipeline: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
model_info = mlflow.transformers.log_model(
    transformers_model={"model": trainer.model, "tokenizer": tokenizer},
    task="text-classification",
    artifact_path="text_classifier",
    input_example=["MLflow is great!", "MLflow on Databricks is awesome!"],
)
```

## Load the Model for Inference

After logging, load the model for inference using MLflow. The example below loads the model as a Spark UDF and applies it to a test DataFrame. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
logged_model = "runs:/{run_id}/{model_artifact_path}".format(
    run_id=run.info.run_id,
    model_artifact_path=model_artifact_path
)

loaded_model_udf = mlflow.pyfunc.spark_udf(spark, model_uri=logged_model, result_type='string')
test = test.select(test.text, test.label, loaded_model_udf(test.text).alias("prediction"))
display(test)
```

See [Deploy models using Model Serving](/concepts/mlflow-model-serving-and-deployment.md) for more information. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Troubleshoot Common CUDA Errors

### OutOfMemoryError: CUDA out of memory

This error occurs when GPU memory is insufficient. Recommended mitigations: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

- Reduce `per_device_train_batch_size` in `TrainingArguments`.
- Set `fp16=True` for lower precision training.
- Use `gradient_accumulation_steps` to effectively increase overall batch size.
- Use the [8‑bit Adam optimizer](https://huggingface.co/docs/transformers/main/en/perf_train_gpu_one#8bit-adam).
- Clean up GPU memory before training with `numba.cuda`:

```python
from numba import cuda
device = cuda.get_current_device()
device.reset()
```

### CUDA kernel errors

CUDA kernel errors may be reported asynchronously. To debug: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

- Run the code on CPU to check reproducibility.
- Set `CUDA_LAUNCH_BLOCKING=1` for a better traceback:

```python
import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
```

## Notebook: Fine-tune Text Classification on a Single GPU

A complete example notebook is available to get started quickly. The notebook covers all the steps described in this article. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

> **Fine‑tuning Hugging Face text classification models notebook**

## Additional Resources

- What are Hugging Face Transformers?
- Model inference using Hugging Face Transformers for NLP

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
