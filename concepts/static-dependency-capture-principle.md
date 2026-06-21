---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 299d1831670349374320061facb33a76956c9a3697b9d89a0f9e81d26b8bbf5c
  pageDirectory: concepts
  sources:
    - package-custom-artifacts-for-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - static-dependency-capture-principle
    - SDCP
  citations:
    - file: package-custom-artifacts-for-model-serving-databricks-on-aws.md
title: Static Dependency Capture Principle
description: The principle that real-time model serving workloads perform best when all file and artifact dependencies are statically packaged into the model at deployment time, rather than loaded dynamically from networks or external sources.
tags:
  - model-serving
  - deployment
  - best-practices
timestamp: "2026-06-19T19:53:45.430Z"
---

## Static Dependency Capture Principle

The **Static Dependency Capture Principle** is a design guideline for machine learning model deployment that mandates capturing all file and artifact dependencies into the model artifact **at deployment time**, rather than resolving them dynamically at runtime. It ensures that the model is self-contained and does not rely on external storage (e.g., Unity Catalog volumes) or network resources during inference. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

### Rationale

Real-time model serving workloads at scale perform best when all required dependencies are statically captured at deployment time. Dynamic resolution—such as loading files from Unity Catalog volumes or downloading tokenizers from the internet at runtime—introduces latency, network failures, and permission issues. By packaging every dependency into the model artifact, the serving endpoint can load the model quickly and reliably without external calls. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

### Implementation

The principle is implemented using [MLflow](/concepts/mlflow.md)'s `log_model()` function, which accepts an `artifacts` parameter. This parameter maps logical artifact names to file paths on disk—either in Unity Catalog volumes, local files, or other accessible locations. During model logging, MLflow copies those files into the model artifact, making them permanently available. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

```python
import mlflow

mlflow.pyfunc.log_model(
    ...
    artifacts={
        "model-weights": "/Volumes/catalog/schema/volume/path/to/file",
        "tokenizer_cache": "./tokenizer_cache",
    },
    ...
)
```

In a custom PyFunc model, the packaged artifacts are accessible through the `context.artifacts` dictionary inside `load_context()`. For example, a model can load weights from the packaged artifact and force a HuggingFace tokenizer to use only the local cache: ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

```python
class ModelPyfunc(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        self.tokenizer = transformers.BertweetTokenizer.from_pretrained(
            "model-base",
            local_files_only=True,
            cache_dir=context.artifacts["tokenizer_cache"],
        )
```

After packaging, the model artifact is self-contained and can be served to a [Model Serving](/concepts/model-serving.md) endpoint without additional external dependencies.

### Relationship with Other Practices

- **Unity Catalog Volumes**: Although volumes are a recommended location for storing large files during development, the Static Dependency Capture Principle requires that those files be **copied into the model artifact** before deployment. The serving endpoint does not access Unity Catalog volumes at inference time. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]
- **Network Artifacts**: Models that load artifacts from the internet (e.g., HuggingFace tokenizers) should be configured to use a local cache directory and that cache should be packaged as an artifact. The `local_files_only=True` flag in HuggingFace ensures no network calls occur at serving time. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

### Related Concepts

- [Model Serving](/concepts/model-serving.md) – The deployment infrastructure that benefits from static dependency capture.
- [MLflow](/concepts/mlflow.md) – The framework used to log models and package artifacts.
- Unity Catalog Volumes – A common source of artifact files during development.
- [Custom PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md) – The model type that accesses packaged artifacts via `context.artifacts`.
- Deployment Best Practices – General guidelines for reliable model serving.

### Sources

- package-custom-artifacts-for-model-serving-databricks-on-aws.md

# Citations

1. [package-custom-artifacts-for-model-serving-databricks-on-aws.md](/references/package-custom-artifacts-for-model-serving-databricks-on-aws-e55bf1f8.md)
