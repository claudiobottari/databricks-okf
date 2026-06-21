---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56ddddd22ed0dde26ec19f8f5796d3972d3546adbdb470b4f5d5031cb1589427
  pageDirectory: concepts
  sources:
    - organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - experiment-artifact-storage-locations
    - EASL
    - artifact location
  citations:
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
title: Experiment Artifact Storage Locations
description: MLflow experiment artifacts can be stored in MLflow-managed DBFS (default), Unity Catalog volumes (recommended), or S3 (not recommended). S3-stored artifacts don't appear in the MLflow UI and cannot be registered in Model Registry.
tags:
  - mlflow
  - artifacts
  - storage
  - unity-catalog
timestamp: "2026-06-19T19:53:12.051Z"
---

# Experiment Artifact Storage Locations

**Experiment Artifact Storage Locations** refer to the configurable destinations where [MLflow](/concepts/mlflow.md) stores artifacts generated during experiment runs, such as models, plots, and serialized objects. When creating an MLflow experiment, you can specify an artifact location; if none is provided, artifacts are stored in MLflow-managed default storage. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Default Storage

If you do not specify an artifact location when creating an experiment, artifacts are stored in MLflow-managed artifact storage at `dbfs:/databricks/mlflow-tracking/<experiment-id>`. This is the default behavior for workspaces not enabled for [Unity Catalog](/concepts/unity-catalog.md). ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Unity Catalog Volumes (Recommended)

For workspaces enabled for Unity Catalog, Databricks recommends storing artifacts in a Unity Catalog volume. To use a volume, specify a path of the form `dbfs:/Volumes/catalog_name/schema_name/volume_name/user/specified/path` as your MLflow experiment artifact location. This can be either a managed or external volume. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

The following Python code demonstrates setting a Unity Catalog volume as the artifact location:

```python
import mlflow

EXP_NAME = "/Users/first.last@databricks.com/my_experiment_name"
CATALOG = "my_catalog"
SCHEMA = "my_schema"
VOLUME = "my_volume"
ARTIFACT_PATH = f"dbfs:/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}"

mlflow.set_tracking_uri("databricks")
mlflow.set_registry_uri("databricks-uc")

if mlflow.get_experiment_by_name(EXP_NAME) is None:
    mlflow.create_experiment(name=EXP_NAME, artifact_location=ARTIFACT_PATH)

mlflow.set_experiment(EXP_NAME)
```

^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

Storing artifacts in a Unity Catalog volume requires MLflow 2.15.0 or above. If your workspace is not enabled for Unity Catalog, or you do not have access to MLflow 2.15.0 or above, specify a path in the format `dbfs:/path/to/artifacts`. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## DBFS Paths

If Unity Catalog volumes are not available, you can store artifacts in DBFS by specifying a path such as `dbfs:/path/to/artifacts`. This is a common alternative when Unity Catalog is not enabled. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## S3 Storage (Not Recommended)

You can also store artifacts directly to Amazon S3 by specifying a URI of the form `s3://<bucket>/<path>`. MLflow obtains credentials to access S3 from your cluster's instance profile. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

However, this approach has significant limitations:
- Artifacts stored in S3 do not appear in the MLflow UI.
- You must download them using an object storage client.
- Models stored in S3 cannot be registered in [Model Registry](/concepts/mlflow-model-registry.md).

^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Upload and Download Limits

The upload and download file size limits for artifacts are both 5 GB. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Important Considerations

When you store an artifact in a location other than MLflow-managed DBFS (default) or Unity Catalog volumes, the artifact does not appear in the MLflow UI. Additionally, models stored in locations other than these cannot be registered in Model Registry. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and artifact storage configuration.
- Unity Catalog Volumes — Recommended storage location for artifacts in Unity Catalog-enabled workspaces.
- DBFS — Default filesystem for Databricks workspaces.
- [Model Registry](/concepts/mlflow-model-registry.md) — Model management service that requires artifacts to be stored in compatible locations.
- Instance Profile — AWS IAM role used to grant S3 access for artifact storage.

## Sources

- organize-training-runs-with-mlflow-experiments-databricks-on-aws.md

# Citations

1. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
