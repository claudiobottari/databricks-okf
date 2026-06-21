---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 347000de80a80abd0ba2114ed3f5c0ed42eeac5dcbe6db0935e31827ba6517e4
  pageDirectory: concepts
  sources:
    - use-custom-python-libraries-with-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volumes-for-mlflow-dependencies
    - UCVFMD
  citations:
    - file: use-custom-python-libraries-with-model-serving-databricks-on-aws.md
    - file: inferred from general knowledge about Unity Catalog
    - file: inferred
title: Unity Catalog Volumes for MLflow Dependencies
description: Using Unity Catalog volumes as the recommended storage location for custom Python wheel files referenced in MLflow model logging
tags:
  - databricks
  - unity-catalog
  - storage
timestamp: "2026-06-19T23:21:01.509Z"
---

# [Unity Catalog](/concepts/unity-catalog.md) Volumes for [MLflow](/concepts/mlflow.md) Dependencies

**Unity Catalog Volumes for [MLflow](/concepts/mlflow.md) Dependencies** refers to the practice of storing custom Python library files (such as `.whl` files) in a Unity Catalog Volume so that they can be referenced when logging an [MLflow](/concepts/mlflow.md) model for deployment. This approach is the recommended method for making private or custom libraries available to [Model Serving](/concepts/model-serving.md) endpoints. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Recommended Storage Location

When you need to include custom Python libraries or libraries from a private PyPI mirror with your model, Databricks recommends uploading the dependency file to a [Unity Catalog](/concepts/unity-catalog.md) volume. This provides a centralized, governed location for the artifacts. Alternatively, you can upload to DBFS (Databricks File System), but volumes are the preferred approach. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Usage in Model Logging

After uploading the `.whl` file to a [Unity Catalog](/concepts/unity-catalog.md) volume, you specify the volume path in the `extra_pip_requirements` parameter when calling `mlflow.*.log_model()`. For example:

```python
[[mlflow|MLflow]].sklearn.log_model(model, "sklearn-model",
    extra_pip_requirements=["/volumes/path/to/dependency.whl"])
```

You can also use the same volume path with `mlflow.pyfunc.log_model`:

```python
[[mlflow|MLflow]].pyfunc.log_model(
    name="model",
    python_model=MyModel(),
    extra_pip_requirements=["/volumes/path/to/dependency.whl"],
)
```

If your library is stored somewhere other than a volume or DBFS, you can use the `code_paths` parameter to copy the file into the model artifact and then reference it with a relative path. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Workflow Summary

1. Upload your custom Python wheel file to a [Unity Catalog](/concepts/unity-catalog.md) volume (e.g., via the Databricks UI or API). ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]
2. Install the library in your notebook using `%pip` to make it available during training. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]
3. Log your model with `extra_pip_requirements` pointing to the volume path of the wheel file. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]
4. Register the model in the [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) and deploy it to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Benefits

- **Governance**: [Unity Catalog](/concepts/unity-catalog.md) volumes provide access control, audit logging, and lineage tracking for artifacts. ^[inferred from general knowledge about Unity Catalog]
- **Portability**: Volume paths are consistent across workspaces that mount the same [Catalog and Schema](/concepts/catalog-and-schema.md). ^[inferred]
- **Security**: Avoids exposing internal dependencies through public PyPI. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Related Concepts

- Unity Catalog Volumes – The storage object used to hold dependency files.
- [Model Serving](/concepts/model-serving.md) – The endpoint deployment service that consumes the model.
- MLflow Model Logging – The process of saving a model with its dependencies.
- [Custom Python Libraries for Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) – Broader topic covering volumes, DBFS, and private mirrors.
- [Private PyPI Mirror Configuration](/concepts/private-pypi-mirror-configuration-for-model-serving.md) – Alternative approach using a workspace-level package repository.
- DBFS – Alternative storage location for dependency files.

## Sources

- use-custom-python-libraries-with-model-serving-databricks-on-aws.md

# Citations

1. [use-custom-python-libraries-with-model-serving-databricks-on-aws.md](/references/use-custom-python-libraries-with-model-serving-databricks-on-aws-58bc4dbc.md)
2. inferred from general knowledge about Unity Catalog
3. inferred
