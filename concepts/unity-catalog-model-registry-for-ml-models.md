---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: da81b01d2d42501467dfd4e3f0a1270c7b8b7bacdefe8d4cf3b75b1271adae69
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-model-registry-for-ml-models
    - UCMRFMM
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: Unity Catalog Model Registry for ML Models
description: A Unity Catalog namespace for organizing, storing, registering, and deploying ML models, using catalog/schema/volume structure for model checkpoints and registered model serving.
tags:
  - databricks
  - model-registry
  - unity-catalog
timestamp: "2026-06-19T18:50:54.984Z"
---

# Unity Catalog Model Registry for ML Models

The **Unity Catalog Model Registry for ML Models** is a central repository within [Unity Catalog](/concepts/unity-catalog.md) for managing machine learning models, their versions, and their lifecycle. It enables teams to organize, discover, and govern models across workspaces by leveraging the Unity Catalog three-level namespace (`catalog.schema.model_name`). The registry integrates with [MLflow](/concepts/mlflow.md) for model logging and tracking, allowing models trained on Databricks to be registered directly into Unity Catalog for deployment and serving. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Registration Process

Models are registered to the Unity Catalog Model Registry through MLflow’s `log_model` functions. The typical workflow involves:

1. Training a model (for example, using DeeSpeed or [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) on serverless GPU compute).
2. Setting the MLflow registry URI to `databricks-uc` with `mlflow.set_registry_uri("databricks-uc")` ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md].
3. Logging the model with `mlflow.transformers.log_model()` (or other flavor-specific log functions) and specifying the `registered_model_name` as the fully qualified Unity Catalog name, e.g., `catalog.schema.model_name`. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

When the model is logged, MLflow automatically registers it in the specified Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md). The registered model can then be deployed to [Model Serving](/concepts/model-serving.md) endpoints or used for batch inference. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Example (from Supervised Fine-Tuning)

```python
mlflow.set_registry_uri("databricks-uc")
with mlflow.start_run(run_id=run_id) as run:
    components = {
        "model": model,
        "tokenizer": tokenizer
    }
    logged_model = mlflow.transformers.log_model(
        transformers_model=components,
        name="model",
        task="llm/v1/chat",
        input_example={"messages": [{"role": "user", "content": "What is machine learning?"}]},
        registered_model_name=REGISTERED_MODEL_NAME
    )
```

After this call, the model is stored in Unity Catalog at the path defined by `REGISTERED_MODEL_NAME`. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Checkpoint Storage

During training, model checkpoints can be stored in a Unity Catalog Volume to persist intermediate states. The volume path is specified as part of the training configuration, e.g., `/Volumes/{catalog}/{schema}/{volume}/{model_name}`. The final model is then registered from those checkpoints. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Integration with AI Runtime

The Unity Catalog Model Registry works seamlessly with [AI Runtime](/concepts/ai-runtime.md) on Databricks. When using serverless GPU compute (such as the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)), the registry provides a governed location to store models after training. The registry URI `databricks-uc` is set within the training environment, and the registered model name is constructed from widget parameters. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for data and AI assets.
- [MLflow](/concepts/mlflow.md) – Open-source platform for machine learning lifecycle.
- Unity Catalog Volume – Storage volume for files, including model checkpoints.
- [Model Serving](/concepts/model-serving.md) – Deployment of registered models to inference endpoints.
- [AI Runtime](/concepts/ai-runtime.md) – Managed GPU compute for training workloads.
- Fine-tuning – Supervised fine-tuning workflows that use the registry.
- [DeepSpeed](/concepts/deepspeed.md) – Memory optimization framework often used before registration.

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
