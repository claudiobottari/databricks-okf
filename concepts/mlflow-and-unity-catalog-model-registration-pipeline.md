---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18dc63e4b0b3407ca3f941cc8422e09c6aad3be60bd9004682ff0c0f3eae9f1e
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-and-unity-catalog-model-registration-pipeline
    - Unity Catalog Model Registration Pipeline and MLflow
    - MAUCMRP
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: MLflow and Unity Catalog Model Registration Pipeline
description: Workflow for logging fine-tuned models to MLflow Tracking and registering them in Databricks Unity Catalog with versioning, metadata, and deployment readiness.
tags:
  - mlops
  - model-registry
  - databricks
  - mlflow
  - unity-catalog
timestamp: "2026-06-18T15:30:42.157Z"
---

Here is the wiki page for "MLflow and Unity Catalog Model Registration Pipeline".

---

## MLflow and Unity Catalog Model Registration Pipeline

The **MLflow and Unity Catalog Model Registration Pipeline** is the process of saving a trained machine learning model, logging its artifacts and metadata via [MLflow Tracking](/concepts/mlflow-tracking.md), and registering it as a governed asset in [Unity Catalog](/concepts/unity-catalog.md). This pipeline combines MLflow's experiment-tracking capabilities with Unity Catalog's governance, discovery, and access control features.

## Overview

After a model is trained, the pipeline handles the complete lifecycle of making the model available for consumption, deployment, and monitoring. The registration process includes logging model artifacts, associating metadata, creating a versioned model entry in Unity Catalog, and ensuring full reproducibility of the training run. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Pipeline Steps

### 1. Load and Prepare the Model

The trained model (and its tokenizer, if applicable) is loaded from its saved location. For LoRA-style fine-tuned models, the base model and the adapter weights are loaded separately, then merged into a single, self-contained model object. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 2. Define the Unity Catalog Model Name

The full Unity Catalog path is constructed using the catalog, schema, and model name:

```python
full_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"
```

This path uniquely identifies the model within Unity Catalog's three-level namespace (`catalog.schema.model`). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 3. Start an [MLflow Run](/concepts/mlflow-run.md) and Log the Model

Inside an active [MLflow Run](/concepts/mlflow-run.md), the model is logged using `mlflow.transformers.log_model()`. This step:

- Logs the model and tokenizer components as an MLflow artifact.
- Registers the model in Unity Catalog under the specified name.
- Captures metadata, such as the model's task type, base model identifier, and model family.
- Generates a new model version automatically.

A typical registration call:

```python
with mlflow.start_run(run_id=run_id):
    model_info = mlflow.transformers.log_model(
        transformers_model=components,
        name="model",
        task="llm/v1/chat",
        registered_model_name=full_model_name,
        metadata={
            "task": task,
            "pretrained_model_name": MODEL_NAME,
            "databricks_model_family": "Llama3.2",
        },
    )
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 4. Capture Registration Outputs

The `model_info` object returned by `log_model` contains key identifiers:

- `model_info.model_uri`: The MLflow model URI for referencing the logged model.
- `model_info.registered_model_version`: The version number assigned by Unity Catalog.

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Benefits

This pipeline provides:

- **Governance**: Models registered in Unity Catalog benefit from its unified access control, lineage tracking, and discovery features.
- **Versioning**: Each registration creates a new version, supporting model lifecycle management such as staging, approval, and deployment.
- **Reproducibility**: All model artifacts, hyperparameters, and metadata are captured in the [MLflow Run](/concepts/mlflow-run.md), enabling full traceability back to the training process.
- **Deployment readiness**: Registered models can be loaded by serving endpoints or batch inference jobs using the Unity Catalog path.

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) – The core experiment-tracking component that logs parameters, metrics, and artifacts.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks' governance solution for managing data and AI assets.
- [Model Registration and Deployment](/concepts/automl-model-registration-and-deployment.md) – The broader workflow for putting models into production.
- LoRA Fine-Tuning – A parameter-efficient fine-tuning method often used with this pipeline.
- [MLflow Transformers Flavor](/concepts/mlflow-transformers-flavor.md) – The MLflow flavor used for logging Hugging Face transformer models.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
