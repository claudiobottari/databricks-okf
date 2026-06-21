---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 935c1de9919a965e03c3c377b5cb6264706ba7719eb7d41780120c349a44d4c4
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-versioning-and-stage-transitions
    - Stage Transitions and Model Versioning
    - MVAST
    - Model Version Stage Transitions
    - Model Stage Transitions
    - Model version stages
    - Stage Transitions
  citations:
    - file: manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
title: Model Versioning and Stage Transitions
description: "A system within the Workspace Model Registry that tracks distinct versions of a registered model and allows transitioning them through lifecycle stages: None, Staging, Production, and Archived, with optional approval workflows."
tags:
  - model-lifecycle
  - versioning
  - mlflow
  - deployment
timestamp: "2026-06-19T19:25:08.300Z"
---

# Model Versioning and Stage Transitions

**Model Versioning and Stage Transitions** are core features of the [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md) that allow teams to manage the lifecycle of machine learning models. Every registered model can have multiple versions, each representing a distinct snapshot of the model artifacts, and each version can be moved through a set of predefined stages to reflect its maturity and readiness for deployment. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Model Versioning

When a model is registered in the Workspace Model Registry, each subsequent upload of a new model artifact creates a new **model version** with an incrementing version number. Versions are immutable snapshots: once created, the artifacts and metadata for a specific version cannot be modified (though the version can be deleted or transitioned to a different stage). ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

Versioning provides chronological lineage, linking each version back to the MLflow experiment and run that produced it. This lineage is visible in the registry UI and can be queried via the API. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

### Quota Limits

Starting May 2024, the Workspace Model Registry imposes quota limits on the total number of registered models and model versions per workspace. If quotas are exceeded, Databricks recommends deleting unused models and versions or adjusting the registration and retention strategy. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Model Stages

A model version can be assigned one of four stages:

- **None** – The default stage for a newly registered version.
- **Staging** – Intended for testing and validation.
- **Production** – For versions that have completed testing and are deployed in live scoring.
- **Archived** – For inactive versions that are no longer in use.

A registered model can have multiple versions in the same stage simultaneously. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Stage Transitions

### Permissions

Only users with the appropriate model permission can transition a version between stages. Workspace administrators can set permission levels on individual models or across all models in the registry. Model versions inherit permissions from their parent model. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

### Transitioning via the UI

On a model version page, the **Stage:** dropdown shows the available target stages. The user selects the desired stage, optionally adds a comment, and confirms. If transitioning a version to **Production**, the UI offers an option to automatically transition all other Production versions to **Archived**. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

### Transitioning via the API

The `transition_model_version_stage()` method of the MLflow Client API performs stage transitions programmatically. The method accepts the model name, version number, target stage, and an optional description. Accepted stage values are case-insensitive strings: `"Staging"`, `"Production"`, `"Archived"`, `"None"`. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

```python
client = MlflowClient()
client.transition_model_version_stage(
    name="<model-name>",
    version=<model-version>,
    stage="Production",
    description="Ready for deployment"
)
```

### Requesting Stage Transitions

If a user lacks the permission to transition a version to a particular stage, they can **request** the transition instead. The request appears in the **Pending Requests** section of the model version page. Users with appropriate permission can then **approve**, **reject**, or **cancel** the request. The original requester can also cancel their own request. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

### Activity Log

All stage transitions (requests, approvals, rejections, cancellations) are recorded in the model version's **Activities** section, providing an auditable lineage of the model’s lifecycle. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Recommended Workflow

A typical lifecycle for a model version is: **None** → **Staging** (for testing and validation) → **Production** (for live scoring) → **Archived** (when no longer needed). Archived versions can be safely deleted, but deletion is irreversible. After transitioning a version to Archived, it can still be restored to a different stage if needed, though deletion removes it permanently. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Related Concepts

- [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md) – The overall system that provides model versioning and stage management.
- [MLflow](/concepts/mlflow.md) – The open-source platform used to log experiments and models.
- [Model Serving](/concepts/model-serving.md) – Deploying models to REST API endpoints for real-time inference.
- Model permissions – Access control for models and model versions.
- [Webhooks for Workspace Model Registry](/concepts/workspace-model-registry-webhooks.md) – Automated triggers based on registry events.
- [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) – The modern alternative to the Workspace Model Registry.

## Sources

- manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md](/references/manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws-666e92b6.md)
