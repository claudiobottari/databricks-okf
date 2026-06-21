---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bac28312e4386b9f74c54193bfcc0259b1b6a5ed3475ecedd257bf0028e121e1
  pageDirectory: concepts
  sources:
    - machine-learning-lifecycle-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-registry-in-unity-catalog
    - MMRIUC
    - MLflow Models in Unity Catalog
    - Model Registry in Unity Catalog
    - Migrate workflows and models to Unity Catalog
    - Model Registration in Unity Catalog
  citations:
    - file: machine-learning-lifecycle-databricks-on-aws.md
title: MLflow Model Registry in Unity Catalog
description: A governed model registry in Unity Catalog for managing model versions, aliases (Staging, Production), staging-to-production promotion, rollback, and audit trails.
tags:
  - machine-learning
  - mlops
  - governance
  - unity-catalog
timestamp: "2026-06-19T19:19:16.073Z"
---

# MLflow Model Registry in Unity Catalog

The **MLflow Model Registry in Unity Catalog** is the central governance and lifecycle management layer for machine learning models on Databricks. It integrates the lineage and experiment tracking capabilities of MLflow with the data governance features of Unity Catalog, allowing teams to manage, version, audit, and promote models through development, staging, and production stages. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Key Capabilities

### Model Versions

When a model or pipeline is registered in the registry, it becomes a **registered model** with one or more **versions**. Each version is automatically linked to the original MLflow training run that produced it, providing full provenance: the dataset, code, and environment that generated that specific model artifact. This linkage simplifies auditing, reproducibility, and troubleshooting. ^[machine-learning-lifecycle-databricks-on-aws.md]

### Aliases for Lifecycle State

Model versions can be labeled with **aliases** such as `Staging` or `Production` to signal their current lifecycle stage without renaming artifacts or moving them between folders. Aliases enable safe deployment workflows by clearly indicating which version is under testing and which is serving production traffic. ^[machine-learning-lifecycle-databricks-on-aws.md]

### Test, Promote, and Rollback

The registry supports a structured promotion pipeline:

- Test a candidate version in **staging** under realistic conditions before it serves production traffic.
- After validation, promote the version to **production** (e.g., by changing its alias to `Production`).
- If quality degrades, roll back to a previous version to restore service quickly. ^[machine-learning-lifecycle-databricks-on-aws.md]

### Audit Trail

Every action on a registered model version is recorded, providing a complete audit trail of what was deployed, when, and by whom. This governance is essential for compliance and operational transparency. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Role in the ML Lifecycle

The MLflow Model Registry in Unity Catalog is used in step 6 (“Register, stage and test models”) of the end‑to‑end machine learning lifecycle on Databricks. After training and evaluation, models are registered here to be managed, governed, and promoted toward production. The registry serves as a bridge between experimentation (tracked in MLflow runs) and production serving (via [Model Serving](/concepts/model-serving.md) for real‑time or [batch inference](/concepts/batch-inference-on-databricks.md)). ^[machine-learning-lifecycle-databricks-on-aws.md]

## Related Concepts

- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – The underlying model storage and versioning system.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that provides data and model lineage, discoverability, and access control.
- [Model Serving](/concepts/model-serving.md) – Real‑time deployment of registered models as REST endpoints.
- Batch Inference – Offline scoring using registered models, often via `ai_query` or Spark UDFs.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Logging parameters, metrics, artifacts, and model metadata during training runs.
- MLOps workflows – Best practices for promoting models through staging and production.

## Sources

- machine-learning-lifecycle-databricks-on-aws.md

# Citations

1. [machine-learning-lifecycle-databricks-on-aws.md](/references/machine-learning-lifecycle-databricks-on-aws-d195211f.md)
