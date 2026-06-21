---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73527b1889a943c6a2ab80620f0e97cb664c203ab1dde402913cf0d7d9196972
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-model-management
    - UCFMM
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: Unity Catalog for Model Management
description: Databricks Unity Catalog namespace used to organize, store, register, and deploy fine-tuned models with MLflow
tags:
  - databricks
  - model-registry
  - catalog
timestamp: "2026-06-19T10:34:11.034Z"
---

# Unity Catalog for Model Management

**Unity Catalog for Model Management** refers to the use of [Unity Catalog](/concepts/unity-catalog.md) as the central governance layer for storing, registering, and serving machine learning models within the Databricks platform. It enables teams to manage model artifacts, track lineage, and enforce access controls across the entire model lifecycle—from training through deployment.

## Overview

Unity Catalog provides a unified namespace (catalog → schema → model) for organizing models alongside tables, volumes, and other data assets. This integration allows data and AI teams to apply consistent governance rules—such as row filters, column masks, and attribute-based access control—to models, treating them as governed first-class objects. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

In practice, a fine-tuning workflow on [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) saves model checkpoints to a Unity Catalog volume and then registers the final model in Unity Catalog via [MLflow](/concepts/mlflow.md). Once registered, the model can be served through [Model Serving](/concepts/model-serving.md) endpoints or used for batch inference, all under the same governance umbrella. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Model Storage and Registration

### Checkpoint Storage

During distributed training (e.g., with [DeepSpeed ZeRO Stage 3](/concepts/deepspeed-zero-stage-3.md) on [A100 or H100 GPUs](/concepts/a100-gpu-support-on-databricks.md)), intermediate checkpoints are saved to a Unity Catalog volume. Volumes provide a governed, scalable file system location that is accessible from both training jobs and downstream consumption. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

The checkpoint directory path follows the Unity Catalog volume structure:

```python
CHECKPOINT_DIR = f"/Volumes/{catalog}/{schema}/{volume}/{model_name}"
```

^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Model Registration

After training completes, the model and tokenizer are logged to MLflow and registered in Unity Catalog using `mlflow.transformers.log_model()` with a `registered_model_name` parameter. The model is automatically available as a Unity Catalog model under the specified [Catalog and Schema](/concepts/catalog-and-schema.md). ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

```python
mlflow.set_registry_uri("databricks-uc")

with mlflow.start_run(run_id=run_id) as run:
    components = {"model": model, "tokenizer": tokenizer}
    mlflow.transformers.log_model(
        transformers_model=components,
        task="llm/v1/chat",
        input_example={"messages": [{"role": "user", "content": "What is machine learning?"}]},
        registered_model_name=f"{catalog}.{schema}.{model_name}"
    )
```

^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Configuration for Training

Before training, the Unity Catalog catalog, schema, and volume must exist. A volume can be created with SQL: `CREATE VOLUME IF NOT EXISTS catalog.schema.volume`. The trained model name is specified as a widget, and MLflow is configured to track the experiment under the user's workspace directory. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Benefits

- **Unified governance**: Models reside alongside tables and volumes in the same catalog, enabling consistent policies (e.g., [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) and [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md)).
- **Lineage and auditability**: MLflow runs automatically capture model artifacts, hyperparameters, and training metrics, all linked to the registered model.
- **Simplified deployment**: Models registered in Unity Catalog can be immediately deployed to serving endpoints without manual artifact transfer.
- **Access control**: Fine-grained permissions (SELECT, EXECUTE, MANAGE) control who can view, use, or modify models.

## Best Practices

1. **Use a consistent namespace**: Choose a [Catalog and Schema](/concepts/catalog-and-schema.md) for models that mirrors your data organization (e.g., `prod_ml.llm_models`).  
2. **Store checkpoints in volumes**: Use Unity Catalog volumes for intermediate checkpoints instead of ephemeral cluster storage to preserve artifacts.  
3. **Register the model with MLflow**: Always use `registered_model_name` to automatically register the model in Unity Catalog during training.  
4. **Set the experiment name early**: Configure the MLflow experiment before the training function begins to ensure all metrics are captured.  

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – Managed GPU compute that integrates with Unity Catalog for model training.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – The underlying mechanism for model versioning and stage transitions.
- [DeepSpeed ZeRO Stage 3](/concepts/deepspeed-zero-stage-3.md) – Memory optimization technique used in conjunction with Unity Catalog checkpoints.
- [Model Serving](/concepts/model-serving.md) – Deploying Unity Catalog–registered models to REST endpoints.
- ABAC for Models – Attribute-based access control applied to Unity Catalog models.

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
