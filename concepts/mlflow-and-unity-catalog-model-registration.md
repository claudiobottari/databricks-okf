---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b35a35e3a1512a1bb4fdf0953865d398c51e65333714904317f326355da2af80
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-and-unity-catalog-model-registration
    - Unity Catalog Model Registration and MLflow
    - MAUCMR
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: MLflow and Unity Catalog Model Registration
description: The workflow for logging fine-tuned LLM artifacts with MLflow and registering them in Unity Catalog for governance, versioning, and deployment as an 'llm/v1/chat' task.
tags:
  - mlops
  - model-registry
  - databricks
timestamp: "2026-06-18T12:03:46.595Z"
---

# MLflow and Unity Catalog Model Registration

**MLflow and Unity Catalog Model Registration** is the process of saving trained ML models as registered models in [Unity Catalog](/concepts/unity-catalog.md) using [MLflow Tracking](/concepts/mlflow-tracking.md). This workflow provides centralized governance, automatic versioning, and lifecycle management for machine learning models within a Databricks environment.

## Overview

After training a model (for example, a fine-tuned LLM), you can register it in Unity Catalog so that it becomes discoverable, governed by access policies, and deployable through a three-level namespace (`catalog.schema.model_name`). The registration is performed via the MLflow Tracking API, which logs model artifacts, metadata, and the model itself to the Unity Catalog registry in a single step. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Model Registration Strategy

The registration process consists of four key objectives: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

- **MLflow Tracking** – Log model artifacts and all associated metadata during a training run.
- **Unity Catalog** – Register the model into a Unity Catalog namespace for governance and deployment readiness.
- **Model Versioning** – Automatic versioning is handled by the registry, enabling clear model lifecycle management (staging, production, archived).
- **Metadata** – Complete model information (task type, base model name, framework family) is recorded for reproducibility and discovery.

## Prerequisites

- A Unity Catalog [Metastore](/concepts/metastore.md) and a target [Catalog and Schema](/concepts/catalog-and-schema.md) must exist.
- The training environment must have the necessary permissions to create registered models in the target catalog.
- For MLflow Transformers integration, the model should be logged using `mlflow.transformers.log_model()`.

## Registration Workflow

After a training run completes (in the example, a distributed fine-tuning job using Unsloth on 8 H100 GPUs), the following steps register the model: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

1. **Load the trained model** – For LoRA‑fine‑tuned models, load the base model and the adapter, then merge and unload the PEFT wrapper to obtain a single model object.
2. **Construct the Unity Catalog model name** – Combine catalog, schema, and model name into the three‑level name (e.g., `main.default.llama-3_2-3b`).
3. **Log the model** – Within an active [MLflow Run](/concepts/mlflow-run.md), call `mlflow.transformers.log_model()` with the model components (model and tokenizer), specifying the `registered_model_name` and `task` (e.g., `llm/v1/chat`). Optionally, add a `metadata` dictionary with additional attributes such as the pretrained model name and model family.

```python
# Construct the Unity Catalog model name
full_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"

task = "llm/v1/chat"

with mlflow.start_run(run_id=run_id):
    model_info = mlflow.transformers.log_model(
        transformers_model=components,
        name="model",
        task=task,
        registered_model_name=full_model_name,
        metadata={
            "task": task,
            "pretrained_model_name": MODEL_NAME,
            "databricks_model_family": "Llama3.2",
        },
    )
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

After execution, the model is registered in Unity Catalog with a version number. The returned `model_info` object contains the `.model_uri` (usable for inference with MLflow) and `.registered_model_version`. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Benefits

- **Centralized governance** – Models live under the same access control framework as other data assets in Unity Catalog.
- **Automatic versioning** – Each registration creates a new version, allowing rollbacks and staging promotions.
- **Reproducibility** – All training parameters, environment metadata, and artifacts are captured in the [MLflow Run](/concepts/mlflow-run.md).
- **Discoverability** – Data scientists and engineers can browse registered models via Catalog Explorer or the API.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for data and AI assets.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The API used to log parameters, metrics, and artifacts.
- Registered Model — A named model in the registry with versioning and stage transitions.
- [MLflow Transformers](/concepts/mlflow-transformers-flavor.md) — The flavor used for logging Hugging Face transformer models.
- LoRA Fine-Tuning — The fine‑tuning technique used in the example registration.
- Serverless GPU Training — Distributed training environment used before registration.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
