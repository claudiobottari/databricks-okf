---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62a99119a0af870ce374fff38588ff3ec7b5fe470850234abc79103108894b63
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-with-hugging-face-transformers
    - MIWHFT
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: MLflow Integration with Hugging Face Transformers
description: The integration between MLflow and Hugging Face that automatically logs training metrics via MLflowCallback and provides mlflow.transformers.log_model for logging trained models and pipelines to the MLflow registry.
tags:
  - mlflow
  - huggingface
  - model-registry
  - databricks
timestamp: "2026-06-19T10:33:15.503Z"
---

# MLflow Integration with Hugging Face Transformers

**MLflow Integration with Hugging Face Transformers** enables seamless tracking, logging, and deployment of fine-tuned Hugging Face models within the MLflow ecosystem. This integration automatically captures training metrics during model training and provides standardized APIs for logging trained models and loading them for inference.

## Overview

The Hugging Face `transformers` library provides the Trainer API utility and AutoModel Classes for loading and fine-tuning Transformer models. MLflow integrates with these tools to automatically log metrics during model training using the MLflowCallback, which is built into the Hugging Face `transformers` library. However, you must manually log the trained model itself using MLflow APIs. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Logging Models to MLflow

After training a Hugging Face model, you log it to MLflow using `mlflow.transformers.log_model()`. This function accepts either a complete Transformers pipeline or a dictionary of model components. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Logging as a Pipeline

Wrap training in an [MLflow Run](/concepts/mlflow-run.md), construct a Transformers pipeline from the tokenizer and trained model, and log it: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

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

### Logging Without a Pipeline

If you don't need to create a pipeline, you can submit the training components in a dictionary: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
model_info = mlflow.transformers.log_model(
    transformers_model={"model": trainer.model, "tokenizer": tokenizer},
    task="text-classification",
    artifact_path="text_classifier",
    input_example=["MLflow is great!", "MLflow on Databricks is awesome!"],
)
```

## Loading Models for Inference

Logged models can be loaded for inference using standard MLflow APIs. You can load the model as a Spark UDF for batch inference: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
logged_model = "runs:/{run_id}/{model_artifact_path}".format(
    run_id=run.info.run_id,
    model_artifact_path=model_artifact_path
)

# Load model as a Spark UDF
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

## Training Integration

MLflow's integration with the Hugging Face Trainer is automatic for metrics logging. When you create a `Trainer` object, the MLflowCallback automatically logs training metrics such as loss and evaluation metrics during training. You do not need to add any additional configuration for this functionality. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Requirements

- MLflow 2.3 or later
- Hugging Face Transformers library
- The `mlflow.transformers` module (included in MLflow 2.3+) ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Related Concepts

- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Centralized model management
- [Model Serving](/concepts/model-serving.md) — Deploying models to production endpoints
- Spark UDF Inference — Loading models for distributed batch processing
- Trainer API — Hugging Face training utility
- AutoModel Classes — Pre-built model architectures

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
