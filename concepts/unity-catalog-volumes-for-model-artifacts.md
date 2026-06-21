---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c2920b9b4f5f4b58e22e21f358140bcdc432406736453ab93cca3b270a626fc
  pageDirectory: concepts
  sources:
    - package-custom-artifacts-for-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volumes-for-model-artifacts
    - UCVFMA
  citations:
    - file: package-custom-artifacts-for-model-serving-databricks-on-aws.md
title: Unity Catalog Volumes for Model Artifacts
description: Using Unity Catalog volumes as a repository for model dependency files, with the requirement that these files be packaged into the MLflow model artifact for real-time serving on Databricks.
tags:
  - unity-catalog
  - databricks
  - model-serving
timestamp: "2026-06-19T19:53:49.316Z"
---

# Unity Catalog Volumes for Model Artifacts

**Unity Catalog Volumes for Model Artifacts** refers to the practice of packaging files and dependencies stored in Unity Catalog volumes directly into the MLflow model artifact when deploying models to [Model Serving](/concepts/model-serving.md) on Databricks. This ensures that all required artifacts are statically captured at deployment time, which is critical for real‑time inference workloads at scale.

## Requirements

- [MLflow](/concepts/mlflow.md) 1.29 and above ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Why Package Unity Catalog Volume Artifacts?

Models often require additional files during inference, such as pre‑trained weights or tokenizer caches. A common workflow is to store these files in Unity Catalog volumes. However, for production Model Serving endpoints, real‑time workloads perform best when all dependencies are **statically captured at deployment time** rather than resolved dynamically at inference time. For this reason, **Model Serving requires that Unity Catalog volume artifacts be packaged into the model artifact itself** using MLflow interfaces. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

Network artifacts (e.g., those downloaded from the internet, such as HuggingFace tokenizers) should also be packaged with the model whenever possible.

## Packaging Artifacts with the Model

Use the `mlflow.pyfunc.log_model()` command and pass the `artifacts` parameter to log a model together with its dependent files. The `artifacts` parameter is a dictionary where keys are logical names and values are paths to the files. Unity Catalog volume paths follow the format `/Volumes/<catalog>/<schema>/<volume>/<path>`. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

```python
import mlflow

mlflow.pyfunc.log_model(
    ...
    artifacts={
        'model-weights': "/Volumes/catalog/schema/volume/path/to/file",
        'tokenizer_cache': "./tokenizer_cache"
    },
    ...
)
```

When working with Databricks notebooks, a common practice is to have these files reside in Unity Catalog volumes before referencing them in the `artifacts` parameter.

## Accessing Artifacts in a Custom PyFunc Model

Inside a custom PyFunc model, the packaged artifact paths are accessible from the `context` object via `context.artifacts`. Load the files using the standard method for that file type. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

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

After packaging, the model can be deployed to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md).

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Deploying models for real‑time inference.
- [MLflow](/concepts/mlflow.md) – Managing the machine learning lifecycle.
- Unity Catalog volumes – Storage of files and artifacts in Unity Catalog.
- PyFunc model – A custom MLflow model format.
- [Deploy models using Model Serving](/concepts/mlflow-model-serving-and-deployment.md) – End‑to‑end guide for serving models.

## Sources

- package-custom-artifacts-for-model-serving-databricks-on-aws.md

# Citations

1. [package-custom-artifacts-for-model-serving-databricks-on-aws.md](/references/package-custom-artifacts-for-model-serving-databricks-on-aws-e55bf1f8.md)
