---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7eabb5863e0691f01b3f9b04fb8dd64110b9ad746d614ac690ce70ec58ee85d0
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-gpu-fine-tuning
    - single-GPU
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: Single-GPU Fine-tuning
description: Techniques and configurations for fine-tuning Hugging Face transformer models on a single GPU, including batch size reduction, FP16 training, and gradient accumulation.
tags:
  - gpu
  - fine-tuning
  - performance
timestamp: "2026-06-19T18:49:28.057Z"
---

# Single-GPU Fine-tuning

**Single-GPU Fine-tuning** refers to the process of adapting a pre-trained Hugging Face Transformers model (such as a text classifier) to a specific task using a single GPU. On Databricks, this is typically done with the Hugging Face `transformers` library, using its `Trainer` utility and `AutoModel` classes to load, configure, train, and log the fine-tuned model to [MLflow](/concepts/mlflow.md). The approach assumes a single-node cluster with one GPU on the driver. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

This article describes both the general workflow and Databricks-specific recommendations for loading data from the lakehouse and logging models to MLflow, enabling governance and reuse of models on the platform. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Requirements

- A single-node Databricks cluster with one GPU on the driver.
- The GPU version of Databricks Runtime 13.0 ML and above. The required packages (`transformers`, `datasets`, `evaluate`) are included in that runtime.
- MLflow 2.3.
- Data prepared and loaded for fine-tuning (see the [Loading data for Hugging Face fine-tuning](/concepts/spark-dataframe-to-hugging-face-dataset-conversion.md) article).

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Steps

### Tokenize the dataset

Hugging Face Transformers models expect tokenized input. Use an [AutoTokenizer](/concepts/autotokenizer-for-transformers.md) loaded from the base model, then apply it to the dataset with Hugging Face `datasets`’ `.map()` method:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(base_model)

def tokenize_function(examples):
    return tokenizer(examples["text"], padding=False, truncation=True)

train_test_tokenized = train_test_dataset.map(tokenize_function, batched=True)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Set up the training configuration

1. **Define evaluation metrics** – The `Trainer` computes the default `loss` metric. Additional metrics (e.g., `accuracy`) can be added using the `evaluate` library:

    ```python
    import numpy as np
    import evaluate

    metric = evaluate.load("accuracy")

    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        return metric.compute(predictions=predictions, references=labels)
    ```

2. **Load the model** – Use an appropriate AutoModel class for the task. For text classification, use [AutoModelForSequenceClassification](/concepts/automodelforsequenceclassification.md):

    ```python
    from transformers import AutoModelForSequenceClassification

    model = AutoModelForSequenceClassification.from_pretrained(
        base_model,
        num_labels=len(label2id),
        label2id=label2id,
        id2label=id2label
    )
    ```

3. **Configure training arguments** – Use [TrainingArguments](/concepts/trainingarguments-configuration.md) to set the output directory, evaluation strategy, learning rate, and other parameters:

    ```python
    from transformers import TrainingArguments, Trainer

    training_args = TrainingArguments(output_dir=training_output_dir, evaluation_strategy="epoch")
    ```

4. **Optionally use a data collator** – [DataCollatorWithPadding](/concepts/datacollatorwithpadding.md) batches input and gives good baseline performance for text classification:

    ```python
    from transformers import DataCollatorWithPadding
    data_collator = DataCollatorWithPadding(tokenizer)
    ```

5. **Create the Trainer** – Combine the model, arguments, dataset, metrics, and collator:

    ```python
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

### Train and log to MLflow

Wrap training in an [MLflow Run](/concepts/mlflow-run.md). The Hugging Face `Trainer` automatically logs metrics via MLflowCallback. After training, log the model to MLflow using `mlflow.transformers.log_model()`:

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

Alternatively, pass the model and tokenizer directly as a dictionary:

```python
model_info = mlflow.transformers.log_model(
    transformers_model={"model": trainer.model, "tokenizer": tokenizer},
    task="text-classification",
    artifact_path="text_classifier",
    input_example=["MLflow is great!", "MLflow on Databricks is awesome!"],
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Load the model for inference

After logging, load the model as a Spark UDF for batch scoring:

```python
logged_model = "runs:/{run_id}/{model_artifact_path}".format(
    run_id=run.info.run_id,
    model_artifact_path=model_artifact_path
)

loaded_model_udf = mlflow.pyfunc.spark_udf(spark, model_uri=logged_model, result_type='string')
test = test.select(test.text, test.label, loaded_model_udf(test.text).alias("prediction"))
display(test)
```

See [Deploy models using Model Serving](/concepts/mlflow-model-serving-and-deployment.md) for production deployment. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Troubleshooting common CUDA errors

### CUDA out of memory

Error: `CUDA out of memory. Tried to allocate...`

Recommended fixes:

- Reduce the `per_device_train_batch_size` in [TrainingArguments](/concepts/trainingarguments-configuration.md).
- Use lower precision training by setting `fp16=True` in `TrainingArguments`.
- Increase effective batch size with `gradient_accumulation_steps` in `TrainingArguments`.
- Use the 8-bit Adam optimizer.
- Clean GPU memory before training:

    ```python
    from numba import cuda
    device = cuda.get_current_device()
    device.reset()
    ```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### CUDA kernel errors

Error: `CUDA kernel errors might be asynchronously reported...`

Troubleshooting steps:

- Run the code on CPU to check if the error is reproducible.
- Set `CUDA_LAUNCH_BLOCKING=1` to get a better traceback:

    ```python
    import os
    os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
    ```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Related concepts

- Hugging Face Transformers – The library providing models and training utilities.
- [MLflow](/concepts/mlflow.md) – Used for experiment tracking and model logging.
- [AutoModelForSequenceClassification](/concepts/automodelforsequenceclassification.md) – Specific auto model for text classification.
- [TrainingArguments](/concepts/trainingarguments-configuration.md) – Configuration class for the Trainer.
- Data Collator – Utility for batching tokenized inputs.
- [Deploy models using Model Serving](/concepts/mlflow-model-serving-and-deployment.md) – Deploying logged models.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime environment that includes required packages.

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
