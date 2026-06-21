---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8fd7ab16f93842e4dfb52c36f7ecf740cb52af67b4aeb7218c702a9973be45a4
  pageDirectory: concepts
  sources:
    - fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
    - migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
    - model-registry-improvements-with-mlflow-3-databricks-on-aws.md
    - tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog-model-registry
    - UCMR
  citations:
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
    - file: migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
    - file: model-registry-improvements-with-mlflow-3-databricks-on-aws.md
    - file: tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
title: Unity Catalog Model Registry
description: A Databricks feature for storing model checkpoints, registering trained models, and managing model lifecycle using a catalog schema naming convention within Unity Catalog volumes.
tags:
  - databricks
  - model-management
  - mlops
timestamp: "2026-06-19T18:50:17.544Z"
---

# Unity Catalog Model Registry

The **Unity Catalog Model Registry** is a centralized model governance service within [Unity Catalog](/concepts/unity-catalog.md) that manages the full lifecycle of machine learning models — from training and versioning through deployment and monitoring. Built on the [MLflow Model Registry](/concepts/mlflow-model-registry.md), it stores model metadata, versions, and artifacts in Unity Catalog, enabling fine-grained access control, lineage tracking, and discoverability across an organization. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md, finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

Models in the registry are organized by a three-level namespace (`catalog.schema.model_name`) and can be registered directly from training code or migrated from the legacy Workspace Model Registry. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md, finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Key Capabilities

### Version Management

Every time a model is registered or updated, the Unity Catalog Model Registry creates a new version. Versions are sequentially numbered and can be managed independently, allowing teams to track changes over time and roll back if needed. Versions can be set to different stages such as Staging, Production, or Archived to manage the model lifecycle. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

### Metrics and Parameters Visibility

In MLflow 3, when you register a `LoggedModel` to the Unity Catalog model registry, all of its metrics and parameters are available in the model registry UI and from the API. You can see model performance metrics across all MLflow experiments and workspaces on a single page. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

### Trace Integration

From the **Traces** panel on a model version page, you can see traces associated with the Model ID from development and evaluation (`mlflow.evaluate()` runs) alongside traces from online serving in endpoints. You can use the search box to filter traces and click on a trace to see the full set of spans. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

### Discoverability and Governance

Models registered in Unity Catalog are searchable across the organization and benefit from [Data Classification](/concepts/data-classification.md) for sensitivity tagging, lineage tracking, and audit logging. Model metadata — including task type, model family, and size parameters — can be stored alongside the model. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md, finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Registering Models

### From Training Code

Models can be registered directly during training by using `mlflow.transformers.log_model()` with a `registered_model_name` parameter set to the Unity Catalog path (`catalog.schema.model_name`). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md, finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

The following example demonstrates registering a fine-tuned model in Unity Catalog: ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
import mlflow

full_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"

with mlflow.start_run(run_name="finetune-run"):
    # ... training code ...
    
    model_info = mlflow.transformers.log_model(
        transformers_model={'model': merged_model, 'tokenizer': tokenizer},
        name='model',
        registered_model_name=full_model_name,
        await_registration_for=3600,
        task='llm/v1/chat',
    )
```

### Migrating from Workspace Model Registry

The Unity Catalog Model Registry supports copying model versions from the legacy workspace-level Model Registry. The copy preserves version numbering so that migration does not break version-dependent references. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

The migration process involves:
1. Creating a placeholder model in Unity Catalog to increment version numbers
2. Copying each existing version from the workspace registry to Unity Catalog
3. Handling missing version numbers by creating and immediately deleting placeholder versions to maintain version alignment ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Serving Models

Models registered in Unity Catalog can be deployed to [Model Serving](/concepts/model-serving.md) endpoints for real-time inference. The model must be registered in Unity Catalog or in the workspace model registry to be served. ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

From the **Serving** UI, you can create a serving endpoint by selecting the registered model, choosing the model version, and configuring compute scale-out and traffic routing. The endpoint state shows as **Not Ready** during provisioning and transitions to **Ready** once deployed. ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform underlying the model registry
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — The open-source foundation of the Unity Catalog Model Registry
- [Model Serving](/concepts/model-serving.md) — Deploying models from Unity Catalog to serving endpoints
- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The legacy model registry (pre-migration)
- [Data Classification](/concepts/data-classification.md) — Tagging sensitive data in models and tables
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Monitoring deployed models from the registry
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) — The model representation that exposes metrics and parameters in the registry UI

## Sources

- fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
- migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
- model-registry-improvements-with-mlflow-3-databricks-on-aws.md
- tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md

# Citations

1. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
2. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
3. [migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md](/references/migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws-d3e98aed.md)
4. [model-registry-improvements-with-mlflow-3-databricks-on-aws.md](/references/model-registry-improvements-with-mlflow-3-databricks-on-aws-260d0089.md)
5. [tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md](/references/tutorial-deploy-and-query-a-custom-model-databricks-on-aws-16c7ace5.md)
