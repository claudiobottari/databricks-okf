---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37fa63c5de025ca6a0d11a99d3c1c3bd4ce7be7892e57d5781ccddddb7e77dda
  pageDirectory: concepts
  sources:
    - migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy_model_version-api
    - Copy Model Version
    - ML model versions
  citations:
    - file: migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
title: copy_model_version API
description: An MLflow API method used to copy a specific model version from a source registry (workspace) to a destination registry (Unity Catalog)
tags:
  - databricks
  - mlflow
  - migration
  - api
timestamp: "2026-06-19T19:33:57.728Z"
---

# copy_model_version API

The **`copy_model_version`** API is a method on the MlflowClient that copies a specific version of a registered model from the [Workspace Model Registry](/concepts/workspace-model-registry.md) to a destination in [Unity Catalog](/concepts/unity-catalog.md). It is commonly used as part of a migration workflow to move model versions while preserving their version numbers. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Usage

The API is invoked on an `MlflowClient` instance that is configured with the `registry_uri="databricks"` (pointing to the source Workspace Model Registry). The destination is specified as a Unity Catalog model name in the form `catalog.schema.model_name`. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

```python
workspace_client.copy_model_version(
    src_model_version_source_uri,
    dst_model_name
)
```

### Parameters

- **`src_model_version`** (`str`): The source model version URI, formatted as `models:/<model_name>/<version>`. For example, `"models:/my_workspace_model/3"`. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]
- **`dst_name`** (`str`): The destination registered model name in Unity Catalog, e.g., `"mycatalog.myschema.my_uc_model"`. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

### Return Value

The method does not return a documented value in the provided source; the example script calls it without capturing the return. It likely returns information about the newly created model version in Unity Catalog. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Example

The following excerpt from a migration script shows how `copy_model_version` is used to copy every existing version of a source model to a destination Unity Catalog model: ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

```python
from mlflow import MlflowClient

workspace_client = MlflowClient(registry_uri="databricks")
uc_client = MlflowClient(registry_uri="databricks-uc")

def copy_model_versions_to_uc(src: str, dst: str) -> None:
    latest_versions = workspace_client.get_latest_versions(src)
    max_version_number = max(int(v.version) for v in latest_versions)
    for v in range(1, max_version_number + 1):
        if workspace_model_exists(src, v):
            workspace_client.copy_model_version(f"models:/{src}/{str(v)}", dst)
        else:
            # Create and immediately delete a placeholder model version to
            # increment the version counter on the UC model, so the version
            # numbers on the UC model match those on the workspace model.
            mv = uc_client.create_model_version(dst, placeholder_model)
            uc_client.delete_model_version(dst, mv.version)

copy_model_versions_to_uc("my_workspace_model", "mycatalog.myschema.my_uc_model")
```

In this pattern, the script iterates through all version numbers (1 to the maximum) and copies each existing version. For any missing versions in the source, a placeholder version is created and immediately deleted in Unity Catalog to maintain matching version numbering. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- MlflowClient – The client class that provides this method.
- [Workspace Model Registry](/concepts/workspace-model-registry.md) – The source model registry for the copy operation.
- [Unity Catalog](/concepts/unity-catalog.md) – The destination model registry.
- Model Version – A specific iteration of a registered model.
- [Migrate model versions from Workspace Model Registry to Unity Catalog](/concepts/databricks-model-registry-with-unity-catalog.md) – The full migration workflow that uses this API.

## Sources

- migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md](/references/migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws-d3e98aed.md)
