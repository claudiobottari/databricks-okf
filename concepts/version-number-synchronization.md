---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 76fd20c2a9cdac7bfb546ca141eba3d643d2e55568dc818968c0ea0bfd2d778c
  pageDirectory: concepts
  sources:
    - migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - version-number-synchronization
    - VNS
  citations:
    - file: migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
title: Version Number Synchronization
description: The process of ensuring Unity Catalog model version numbers match the corresponding workspace model version numbers by inserting placeholder versions for gaps
tags:
  - databricks
  - migration
  - versioning
timestamp: "2026-06-19T19:34:05.717Z"
---

# Version Number Synchronization

**Version Number Synchronization** is the process of ensuring that model version numbers in a destination [Unity Catalog](/concepts/unity-catalog.md) registered model match the version numbers of the corresponding source model in the [Workspace Model Registry](/concepts/workspace-model-registry.md). This is necessary when migrating model versions between registries, as version numbers in the destination registry may not align with those in the source after copying individual versions.

## Overview

When migrating model versions from the Workspace Model Registry to Unity Catalog, simply copying each version does not guarantee that the version numbers will match between the two registries. The destination registry may have been modified (e.g., versions created and deleted), causing its version counter to diverge from the source. To maintain consistency, version numbers must be actively synchronized during the migration process. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Standard Migration Without Synchronization

A standard migration copies only existing model versions from the source to the destination:

```python
latest_versions = workspace_client.get_latest_versions(src)
max_version_number = max(int(v.version) for v in latest_versions)

for v in range(1, max_version_number + 1):
    if workspace_model_exists(src, v):
        workspace_client.copy_model_version(f"models:/{src}/{str(v)}", dst)
```

This approach copies only versions that actually exist in the source. If the workspace registry has gaps in its version numbering (e.g., version 2 exists but version 1 was deleted), the destination registry's version counter will not reflect those gaps, causing a mismatch. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Synchronization Using Placeholder Models

The recommended synchronization technique uses placeholder model versions to fill gaps in the version number sequence. The process works as follows:

1. **Create a placeholder model**: A minimal PyFunc model with no predictive value is created using `mlflow.pyfunc.log_model`. This placeholder model is used solely to advance the version counter in the destination registry. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

2. **Iterate through all version numbers**: For each version number from 1 to the maximum version number in the source registry:
   - If the source version exists, copy it to the destination using `copy_model_version`.
   - If the source version does not exist, create a placeholder version in the destination registry and immediately delete it. This increments the version counter without leaving an actual model version behind.

3. **Result**: The destination registry's version counter matches the source, allowing both registries to have the same version numbers for corresponding model versions. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

### Example Code

The following code synchronizes version numbers while migrating:

```python
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

def copy_model_versions_to_uc(src: str, dst: str) -> None:
    latest_versions = workspace_client.get_latest_versions(src)
    max_version_number = max(int(v.version) for v in latest_versions)
    placeholder_model = make_placeholder_model()
    for v in range(1, max_version_number + 1):
        if workspace_model_exists(src, v):
            workspace_client.copy_model_version(f"models:/{src}/{str(v)}", dst)
        else:
            mv = uc_client.create_model_version(dst, placeholder_model)
            uc_client.delete_model_version(dst, mv.version)
```

This pattern ensures that version 3 in the workspace registry corresponds to version 3 in Unity Catalog, and so on for all versions. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Benefits

- **Consistency**: Maintains identical version numbering across registries, simplifying model references and lineage tracking.
- **Predictability**: Downstream systems that depend on specific version numbers continue to work after migration.
- **Traceability**: Makes it easier to correlate model versions across the old and new registries during the transition period.

## Related Concepts

- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The legacy model registry within a Databricks workspace.
- [Unity Catalog](/concepts/unity-catalog.md) — The cross-workspace governance and catalog solution for models.
- Model Version Migration — The broader process of moving model versions between registries.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — The underlying model versioning system.
- [PyFunc Model](/concepts/custom-mlflow-pyfunc-model.md) — The Python function model flavor used for placeholders.
- [Model Signature](/concepts/model-signatures-in-unity-catalog.md) — The input/output schema definition required for creating model versions.

## Sources

- migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md](/references/migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws-d3e98aed.md)
