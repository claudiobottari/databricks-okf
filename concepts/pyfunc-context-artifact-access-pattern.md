---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c97550f37148b90853dca0aebcadf858e35f30c3ee67e923b909b5c0748e870e
  pageDirectory: concepts
  sources:
    - package-custom-artifacts-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pyfunc-context-artifact-access-pattern
    - PCAAP
  citations:
    - file: package-custom-artifacts-for-model-serving-databricks-on-aws.md
title: PyFunc Context Artifact Access Pattern
description: Custom PyFunc models access packaged artifacts through the context.artifacts dictionary inside load_context(), enabling static loading of model weights, tokenizers, and other files at deployment time.
tags:
  - mlflow
  - pyfunc
  - model-serving
timestamp: "2026-06-19T19:53:40.506Z"
---

# PyFunc Context Artifact Access Pattern

The **PyFunc Context Artifact Access Pattern** is the mechanism by which a custom MLflow PyFunc model retrieves file dependencies that were packaged into the model artifact at logging time. This pattern ensures that models deployed to [Model Serving](/concepts/model-serving.md) endpoints have all required files—such as model weights, tokenizer caches, or configuration files—available locally during inference without relying on external network calls or Unity Catalog volumes at runtime.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Why Package Artifacts

Real‑time serving workloads perform best when all required dependencies are statically captured at deployment time. For this reason, Model Serving requires that artifacts from Unity Catalog volumes are packaged into the model artifact itself using MLflow interfaces. Network artifacts that are loaded with the model should also be packaged whenever possible.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Logging Artifacts with the Model

The `mlflow.pyfunc.log_model()` function accepts an `artifacts` parameter, a dictionary that maps logical artifact names to file paths. These paths can point to files in a Unity Catalog volume or to local files (e.g., a pre‑downloaded tokenizer cache).^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    ...
    artifacts={
        'model-weights': "/Volumes/catalog/schema/volume/path/to/file",
        "tokenizer_cache": "./tokenizer_cache"
    },
    ...
)
```

After logging, the artifact files are stored inside the model artifact (the MLflow model directory) and are available on the serving endpoint.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Accessing Artifacts in a Custom PyFunc Model

In a custom `PythonModel` subclass, the `load_context` method receives a `context` object. The artifact paths are accessible through `context.artifacts`, which is a dictionary keyed by the names provided in the `artifacts` parameter. Each value is the local path to the file on the serving node.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

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

In this example, the model weights are loaded via `torch.load` and the tokenizer is loaded using a local cache directory that was packaged as an artifact. The `local_files_only=True` flag prevents a network download at serving time.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Requirements

- [MLflow](/concepts/mlflow.md) version 1.29 and above.^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow PyFunc – The Python function model flavor used for custom model logic.
- [Model Serving](/concepts/model-serving.md) – The Databricks service that hosts models for real‑time inference.
- Unity Catalog volumes – A storage location often used for model files before packaging.
- log_model() – The MLflow API for logging a model and its artifacts.
- PythonModel.load_context – The lifecycle method where artifacts are accessed.

## Sources

- package-custom-artifacts-for-model-serving-databricks-on-aws.md

# Citations

1. [package-custom-artifacts-for-model-serving-databricks-on-aws.md](/references/package-custom-artifacts-for-model-serving-databricks-on-aws-e55bf1f8.md)
