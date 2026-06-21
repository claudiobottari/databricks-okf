---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc3f99f3ef19ba8290c8588cf4a44d42c41eb32b74261a5de41be0ab5870508d
  pageDirectory: concepts
  sources:
    - package-custom-artifacts-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-artifact-packaging-for-model-serving
    - MAPFMS
  citations:
    - file: package-custom-artifacts-for-model-serving-datatbricks-on-aws.md
    - file: package-custom-artifacts-for-model-serving-databricks-on-aws.md
title: MLflow Artifact Packaging for Model Serving
description: Using MLflow's log_model() artifacts parameter to bundle file dependencies (e.g., model weights, tokenizer caches) directly into the model artifact for deployment on Databricks Model Serving.
tags:
  - model-serving
  - mlflow
  - databricks
timestamp: "2026-06-19T19:54:14.370Z"
---

# MLflow Artifact Packaging for Model Serving

**MLflow Artifact Packaging for Model Serving** is the practice of bundling a model's file and artifact dependencies into the model artifact itself, using MLflow's `log_model()` interfaces, so that those dependencies are available on the [Model Serving](/concepts/model-serving.md) endpoint at inference time. This ensures that real‑time serving workloads have all required dependencies statically captured at deployment time, which is critical for production performance.^[package-custom-artifacts-for-model-serving-datatbricks-on-aws.md]

## Why Package Artifacts?

When a model depends on files such as model weights, cached tokenizers, or other artifacts that reside in Unity Catalog volumes or are fetched from the network (for example, HuggingFace tokenizer caches), those dependencies must be present on the serving endpoint. Real‑time workloads at scale perform best when all required dependencies are captured statically at deployment time rather than fetched dynamically at runtime. For this reason, [Model Serving](/concepts/model-serving.md) requires that artifacts from Unity Catalog volumes be packaged into the model artifact using MLflow interfaces.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Packaging Artifacts with `log_model()`

You package artifacts using the `artifacts` parameter of `mlflow.pyfunc.log_model()`. Each entry in the `artifacts` dictionary maps a logical name (used later in the `load_context` method) to a path on the local filesystem or in a Unity Catalog volume.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    ...
    artifacts={
        "model-weights": "/Volumes/catalog/schema/volume/path/to/file",
        "tokenizer_cache": "./tokenizer_cache"
    },
    ...
)
```

Artifacts can point to:
- Files stored in Unity Catalog volumes (for example, `/Volumes/catalog/schema/volume/path/to/file`).
- Local files created during the logging process (for example, `./tokenizer_cache`).

After logging, the paths are packaged into the model artifact and become accessible on the serving endpoint.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Accessing Packaged Artifacts in a PyFunc Model

In a custom MLflow PyFunc model, the packaged artifact paths are available from the `context` object under `context.artifacts`. You load them in the standard way for the file type.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

```python
class ModelPyfunc(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        self.tokenizer = transformers.BertweetTokenizer.from_pretrained(
            "model-base",
            local_files_only=True,
            cache_dir=context.artifacts["tokenizer_cache"]
        )
```

- `context.artifacts["model-weights"]` — the path to the model‑weight file that was packaged with the model.
- `context.artifacts["tokenizer_cache"]` — the path to the copied tokenizer cache directory.

After all files and artifacts are packaged within the model artifact, the model can be deployed to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md).^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Requirements

- [MLflow](/concepts/mlflow.md) version 1.29 or later.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Production serving of ML models.
- MLflow PyFunc – The Python function model flavor used for custom models.
- Unity Catalog volumes – Storage volumes that can hold model‑related files.
- Model artifacts – The set of files bundled with a logged model.

## Sources

- package-custom-artifacts-for-model-serving-databricks-on-aws.md

# Citations

1. package-custom-artifacts-for-model-serving-datatbricks-on-aws.md
2. [package-custom-artifacts-for-model-serving-databricks-on-aws.md](/references/package-custom-artifacts-for-model-serving-databricks-on-aws-e55bf1f8.md)
