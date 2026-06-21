---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6749d8ac2e6370059358de16eec1d288421811d7eb7093d4296ed666b020446
  pageDirectory: concepts
  sources:
    - upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clone-workflow-pattern-for-uc-migration
    - CWPFUM
  citations:
    - file: upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
title: Clone Workflow Pattern for UC Migration
description: Pattern of cloning existing training, deployment, and inference jobs as a starting point for building Unity Catalog-compatible parallel pipelines
tags:
  - workflows
  - migration
  - databricks-jobs
  - best-practice
timestamp: "2026-06-19T23:19:54.586Z"
---

# Clone Workflow Pattern for UC Migration

The **Clone Workflow Pattern for UC Migration** is a recommended incremental migration strategy for upgrading existing Databricks ML workflows to use models in [Unity Catalog](/concepts/unity-catalog.md). The core idea is to clone existing training, deployment, and batch inference workflows, update the clones to target [Unity Catalog](/concepts/unity-catalog.md), and then gradually switch downstream consumers to the new pipeline. This approach minimises disruption by keeping the original workflow running in parallel until the migration is validated. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Why Use the Clone Pattern

Migrating model workflows from the [Workspace Model Registry](/concepts/workspace-model-registry.md) to [Unity Catalog](/concepts/unity-catalog.md) involves changes to code, permissions, and compute configurations. Directly modifying a production workflow can introduce risk. The clone pattern allows you to:

- Create a parallel pipeline that mirrors the existing one.
- Verify that the Unity Catalog–based pipeline produces correct results.
- Switch downstream consumers (e.g., batch inference consumers or [Model Serving](/concepts/model-serving.md) traffic) to the new pipeline at a controlled pace.
- Keep the original workflow as a fallback. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Prerequisites

Before cloning and updating a workflow, ensure the following requirements are met:

- The principal running the workflow must have `USE CATALOG` and `USE SCHEMA` privileges on the [Catalog and Schema](/concepts/catalog-and-schema.md) that hold the model.
- Additional privileges depend on the operation: `CREATE MODEL` to create a model, `EXECUTE` to load or deploy a model, `CREATE MODEL VERSION` (or ownership) to create new versions, and ownership to set aliases.
- The compute resource (cluster or SQL warehouse) used by the workflow must have access to [Unity Catalog](/concepts/unity-catalog.md). See [Access Modes](/concepts/standard-access-mode.md) for details. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Steps by Workflow Type

### Model Training Workflow

1. Clone the existing model training workflow using Job Cloning.  
2. Confirm that the cloned job meets the privilege and compute requirements.  
3. Update the training code in the cloned workflow (e.g., clone the notebook or target a new git branch) to:
   - Install the required version of [MLflow](/concepts/mlflow.md) and configure the client to target [Unity Catalog](/concepts/unity-catalog.md).
   - Register models to [Unity Catalog](/concepts/unity-catalog.md) instead of the [Workspace Model Registry](/concepts/workspace-model-registry.md).  
4. The cloned workflow now trains and registers [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) while the original continues to operate unchanged. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### Model Deployment Workflow

1. Clone the existing model deployment workflow.  
2. Verify that the principal and compute meet the requirements.  
3. Update the deployment logic to:
   - Load model versions from [Unity Catalog](/concepts/unity-catalog.md).
   - Use [Model Aliases](/concepts/model-aliases.md) (e.g., `Champion`, `Candidate`) to manage production rollouts instead of stage-based promotion.  
4. The cloned deployment workflow promotes model versions using [Unity Catalog](/concepts/unity-catalog.md) aliases. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### Model Inference Workflow

#### Batch Inference

1. Clone the batch inference workflow.  
2. Ensure the principal and compute have the necessary [Unity Catalog](/concepts/unity-catalog.md) access.  
3. Update the inference code to load models from [Unity Catalog](/concepts/unity-catalog.md).  
4. After validation, switch downstream consumers to read the batch inference output produced by the cloned workflow. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

#### [Model Serving](/concepts/model-serving.md) (Real‑Time Inference)

For [Model Serving](/concepts/model-serving.md) endpoints, a clone of the endpoint itself is not needed. Instead, use the [Traffic Split](/concepts/traffic-splitting-between-models.md) feature on the existing serving endpoint to gradually route a small fraction of inference traffic to models hosted in [Unity Catalog](/concepts/unity-catalog.md). As you review the results, increase the traffic proportion until all traffic is rerouted. This avoids creating a separate endpoint and allows a smooth, reversible transition. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Manual Approval for Model Deployment (Optional)

If automated deployment is not possible and manual approval is required, you can combine the clone pattern with Job Webhooks. After a training job completes successfully, use job notifications to call an external CI/CD system to request manual approval. Once approval is given, the CI/CD system can set the [Unity Catalog](/concepts/unity-catalog.md) model alias (e.g., `Champion`) to deploy the new model version to serve traffic. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)
- Job Cloning
- [Model Aliases](/concepts/model-aliases.md)
- [Traffic Split](/concepts/traffic-splitting-between-models.md)
- [Model Serving](/concepts/model-serving.md)
- Batch Inference
- [Model Deployment](/concepts/model-serving-endpoint-deployment.md)
- [Model Training](/concepts/databricks-model-training.md)
- [Access Modes](/concepts/standard-access-mode.md)
- Job Webhooks

## Sources

- upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md](/references/upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws-c3150366.md)
