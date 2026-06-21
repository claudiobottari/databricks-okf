---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe0d98bd642cf4edeac9cf11286dfb792fbba3182d0b030f93506a40c4f8585c
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-ml-models
    - UCFMM
    - Unity Catalog Models
    - Train and Register Unity Catalog–Compatible Models
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: Unity Catalog for ML Models
description: Databricks Unity Catalog provides a namespace (catalog/schema/model name) for organizing, registering, and versioning machine learning models, enabling model deployment to serving endpoints or batch inference.
tags:
  - databricks
  - mlops
  - model-registry
  - governance
timestamp: "2026-06-18T12:21:26.737Z"
---

# Unity Catalog for ML Models

**Unity Catalog for ML Models** refers to the set of features in [Unity Catalog](/concepts/unity-catalog.md) that enable you to store, register, version, and govern machine learning models as first-class governed assets alongside tables, views, and functions. By unifying model management with the same catalog, schema, and governance infrastructure used for data, Unity Catalog provides a single source of truth for model artifacts across your organization.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Overview

Unity Catalog extends its three-level namespace (`catalog.schema.object`) to models, treating each registered model as a securable entity. This allows administrators to apply fine-grained access controls, audit lineage, and manage model lifecycles using the same policies and tools as any other governed asset. When you train a model, you can log it to MLflow and register it directly in Unity Catalog, making it immediately discoverable and deployable by downstream teams.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Storing Models

During training, model checkpoints and intermediate artifacts can be saved to a Unity Catalog Volume, providing durable, governed storage. Volumes are mounted as directories and accessible via the `/Volumes/<catalog>/<schema>/<volume>/<path>` pattern. This approach eliminates the need for external blob storage and ensures that all training artifacts are under the same governance umbrella as the rest of your data.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

The volume path is typically configured through notebook widgets or environment variables, and the volume can be created on demand using `CREATE VOLUME IF NOT EXISTS` SQL.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Registering Models

After training, a model can be logged to MLflow and registered in Unity Catalog by setting the MLflow registry URI to `"databricks-uc"`. The registration call includes the model components (e.g., model and tokenizer), the task type (such as `"llm/v1/chat"` for conversational AI), and an input example. The registered model name follows the three-level format `catalog.schema.model_name`.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

```python
mlflow.set_registry_uri("databricks-uc")
with mlflow.start_run(run_id=run_id) as run:
    logged_model = mlflow.transformers.log_model(
        transformers_model=components,
        name="model",
        task="llm/v1/chat",
        input_example={
            "messages": [
                {"role": "user", "content": "What is machine learning?"}
            ]
        },
        registered_model_name=REGISTERED_MODEL_NAME
    )
```

Once registered, the model appears in the Unity Catalog under the specified [Catalog and Schema](/concepts/catalog-and-schema.md). It can then be deployed to [Model Serving](/concepts/model-serving.md) endpoints or used for batch inference.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Model Versioning

Unity Catalog automatically maintains version history for registered models. Each call to `log_model` with `registered_model_name` creates or updates a model version. This enables teams to track changes, roll back to previous versions, and promote specific versions across environments (e.g., staging to production) using Unity Catalog's staging and aliases features.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Access Control and Governance

Because models are first-class objects in Unity Catalog, administrators can apply [ABAC GRANT Policy](/concepts/abac-grant-policy.md) policies (such as granting `EXECUTE` on models based on governed tags) and use row filter or column mask policies on model-related metadata tables. This ensures that only authorized principals can read or invoke a model, supporting compliance and security requirements.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Requirements

To use Unity Catalog for ML models, you need:

- A Unity Catalog [Metastore](/concepts/metastore.md) attached to your Databricks workspace.
- A [Catalog and Schema](/concepts/catalog-and-schema.md) where you have the `CREATE MODEL` privilege (or equivalent).
- For storing checkpoints, a volume with write permissions.
- For registration, the MLflow registry URI set to `"databricks-uc"`.

## Best Practices

- **Use a consistent naming convention** for model names, linking them to use cases or team names.
- **Store all training artifacts in Unity Catalog volumes** rather than external storage, ensuring a complete governance trail.
- **Set up MLflow experiments** in Unity Catalog to track runs and link them to registered models.
- **Apply ABAC policies** (e.g., GRANT policies) to control model execution access based on tags, rather than using direct grants for each model.
- **Version models frequently** and use aliases (e.g., `"prod"`, `"staging"`) to indicate deployment stage.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data and AI governance platform powering model management
- MLflow Models — The model format used to package models
- [Model Serving](/concepts/model-serving.md) — Deployment of Unity Catalog registered models to endpoints
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based access control for model execution (Beta)
- Unity Catalog Volumes — Governed storage for model checkpoints and artifacts
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Run tracking tied to model registration

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
