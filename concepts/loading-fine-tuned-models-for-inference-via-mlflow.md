---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48238062deb8dec8a2a906792f3f5d16e34a001b51c03039bd2de60b5e574593
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - loading-fine-tuned-models-for-inference-via-mlflow
    - LFMFIVM
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: Loading Fine-tuned Models for Inference via MLflow
description: Loading logged Hugging Face models from MLflow as Spark UDFs for batch inference on Databricks
tags:
  - mlflow
  - inference
  - spark
  - databricks
timestamp: "2026-06-18T12:20:42.274Z"
---



# Loading Fine-tuned Models for Inference via MLflow

**Loading fine-tuned models for inference via MLflow** is the standard workflow for retrieving a Hugging Face Transformers model that has been fine-tuned and logged to [MLflow](/concepts/mlflow.md) using the `mlflow.transformers.log_model()` API, then loading it back as a deployable artifact for batch or real-time inference. This process applies to both single-GPU fine-tuning workloads (e.g., text classification) and any [Hugging Face](/concepts/hugging-face-trainer.md) pipeline logged as an MLflow Transformers model. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Overview

After you train a model with the Hugging Face Transformers library and log it to MLflow (typically with `mlflow.transformers.log_model()`), the logged artifact contains everything needed for inference: the model weights, tokenizer, and configuration. Loading the model for inference is identical to loading any MLflow-wrapped pre-trained model, regardless of the underlying framework. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Loading a Fine-Tuned Model

### 1. Identify the Model URI

The model is stored in an [MLflow Run](/concepts/mlflow-run.md). The model URI can be expressed in two ways:

- **Run‑relative URI** – using the `run_id` and `artifact_path`: `runs:/<run_id>/<artifact_path>`
- **Registered Model URI** – using the registered model name and version: `models:/<model_name>/<version>`

### 2. Load as a Spark UDF (Batch Inference)

The recommended way to load a Transformers model for batch inference on Databricks is via `mlflow.pyfunc.spark_udf()`. This creates a Spark UDF that can be applied to a DataFrame column: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

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

The `result_type` parameter must override the default return type if the model does not return double values (e.g., text classification outputs a string label). ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### 3. Load as a pyfunc Model (Programmatic Inference)

Use `mlflow.pyfunc.load_model()` to obtain a Python function that accepts inputs and returns predictions. This is suitable for small-scale testing or REST API endpoints: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
import mlflow

model = mlflow.pyfunc.load_model(model_uri)
predictions = model.predict(["Sample input text"])
```

## Model Artifact Content

When a Transformers model is logged via `mlflow.transformers.log_model()`, the artifact contains:

- The `transformers` pipeline object (e.g., `pipeline("text-classification", model=..., tokenizer=...)`)
- The tokenizer state
- The model configuration (class labels, label mappings)
- The MLflow conda environment for reproducibility

If the model was logged without a pipeline (via a dictionary of components), the artifact still includes all necessary components: `{"model": trainer.model, "tokenizer": tokenizer}`. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Deploying the Model

Loaded models can be deployed for Real-Time Inference via Model Serving or [Batch Inference on Spark DataFrames](/concepts/batch-inference-on-databricks.md):

- **Real-time**: Use Model Serving endpoints on Databricks with the MLflow model URI.
- **Batch**: Apply the Spark UDF to large-scale DataFrame transformations.

See [Deploy models using Model Serving](/concepts/mlflow-model-serving-and-deployment.md) for full deployment instructions. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Supported Model Types

Any Hugging Face Transformers model fine-tuned for any task can be loaded for inference via MLflow, including but not limited to:

| Task | Model Class |
|------|-------------|
| Text classification | `AutoModelForSequenceClassification` |
| Named entity recognition | `AutoModelForTokenClassification` |
| Question answering | `AutoModelForQuestionAnswering` |
| Summarization | `AutoModelForSeq2SeqLM` |

## Related Concepts

- [MLflow Transformers Flavor](/concepts/mlflow-transformers-flavor.md) – The `mlflow.transformers.log_model()` API
- Hugging Face Transformers – The fine-tuning framework
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) – Deploying the loaded model for inference
- PyFunc Spark UDF – Loading model for distributed batch inference
- [MLflow Run](/concepts/mlflow-run.md) – The run that stores the model artifact
- Registered Model – Versioned model in the Model Registry

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
