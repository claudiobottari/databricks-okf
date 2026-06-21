---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4382b60943f37b5513e700cd80409bb2f9dda7109facf482d644cdd7be493057
  pageDirectory: concepts
  sources:
    - migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - placeholder-model-version-technique
    - PMVT
  citations:
    - file: migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
title: Placeholder Model Version Technique
description: A technique using a dummy PythonModel to fill gaps in version numbers, ensuring version parity between workspace and Unity Catalog model registries
tags:
  - databricks
  - migration
  - workaround
  - versioning
timestamp: "2026-06-19T19:33:48.614Z"
---

# Placeholder Model Version Technique

The **Placeholder Model Version Technique** is a method used during model migration to synchronize version numbers between the [Workspace Model Registry](/concepts/workspace-model-registry.md) and [Unity Catalog](/concepts/unity-catalog.md) when some version numbers are missing in the source. It ensures that the version counters on the destination Unity Catalog (UC) model match exactly those on the source workspace-registered model, preserving consistency in versioned model lineage. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Purpose

When migrating model versions from a workspace-registered model to a Unity Catalog–registered model, a one-to-one copy of each existing version is straightforward. However, if the workspace model has gaps in its version numbering (for example, version 2 exists but version 1 was deleted), simply copying existing versions would cause the UC model’s auto‑incrementing version counter to produce different numbers. The placeholder technique fills those gaps by creating a dummy version and then immediately deleting it, bumping the UC version counter without leaving a permanent entry. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Implementation

The technique consists of two steps:

1. **Create a placeholder model** – a minimal [MLflow](/concepts/mlflow.md) PyFunc model that takes any input and returns `None`. This placeholder is logged and its URI is stored for later use.
2. **Insert placeholders for missing versions** – for each version number in the range `[1, max_version_number]` that does not exist in the source workspace, create a model version using the placeholder URI, then immediately delete it. The creation increments the UC version counter, and the deletion removes the placeholder, leaving a gap that matches the source’s gap. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

### Code Example

The following snippet (adapted from the Databricks migration guide) demonstrates the technique:

```python
import mlflow
from mlflow import MlflowClient
from mlflow.models import ModelSignature
from mlflow.types.schema import Schema, ColSpec, AnyType

uc_client = MlflowClient(registry_uri="databricks-uc")

def make_placeholder_model() -> str:
    class _Placeholder(mlflow.pyfunc.PythonModel):
        def predict(self, ctx, x):
            return None
    with mlflow.start_run() as run:
        schema = Schema([ColSpec(AnyType())])
        model = mlflow.pyfunc.log_model(
            name="m",
            python_model=_Placeholder(),
            signature=ModelSignature(inputs=schema, outputs=schema),
        )
        return f"models:/{model.model_id}"

# Usage within a migration loop:
placeholder_model = make_placeholder_model()
for v in range(1, max_version_number + 1):
    if not workspace_model_exists(src, v):
        mv = uc_client.create_model_version(dst, placeholder_model)
        uc_client.delete_model_version(dst, mv.version)
```

^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Key Details

- The placeholder model is never registered as a permanent version in UC. It exists only momentarily to advance the sequence counter. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]
- The technique depends on the fact that MlflowClient.create_model_version automatically assigns the next available version number, and MlflowClient.delete_model_version removes it without creating a gap in the numbering (the deleted number is not reused). ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]
- The migration process should check each version number before copying or inserting a placeholder. Use the `get_model_version` method and catch the `RESOURCE_DOES_NOT_EXIST` error to determine absence. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Model Registry](/concepts/mlflow-model-registry.md) – Central repository for managing MLflow model versions.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ governance catalog for data and AI assets.
- MLflow Model Version – A numbered iteration of a registered model.
- Model Migration – The broader process of transferring models across registries.
- PyFunc – MLflow’s Python function model flavor.

## Sources

- migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md](/references/migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws-d3e98aed.md)
