---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df7d0e1a57f711bbc3ffb512aa14a345e456c977e258e0d4cda54305006e896c
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code_path-parameter-for-shared-modules
    - CPFSM
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: code_path parameter for shared modules
description: MLflow pyfunc log_model's code_path parameter allows packaging shared code modules alongside custom models for reuse across deployments
tags:
  - mlflow
  - python
  - code-organization
timestamp: "2026-06-18T11:59:46.486Z"
---

# code_path parameter for shared modules

The **`code_path`** parameter is an optional argument of [`mlflow.pyfunc.log_model()`](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model) that allows authors to capture and package shared Python modules alongside a custom MLflow PyFunc model. When a model is logged with a reference to a local directory of shared code, that code is bundled into the model artifact and becomes importable at inference time — both during local testing and when served via [Model Serving](/concepts/model-serving.md).^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## How it works

Even though a model’s prediction logic is implemented as custom Python code, the `code_path` parameter lets that model depend on reusable modules from the organization’s codebase, rather than requiring all logic to be inlined in the model class.^[deploy-python-code-with-model-serving-databricks-on-aws.md]

When `log_model()` is called with `code_path = ["path/to/shared_module/"]`, the listed directories are copied into the MLflow model artifact. At load time (in the model’s `load_context` method), Python’s import system automatically includes these paths, making the shared modules available for import within the model.^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Example

The following example logs a custom PyFunc model that uses a shared tokenizer from `preprocessing_utils/`. The shared code is made available via the `code_path` parameter:^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
import mlflow

# Log the model, bundling shared module code
mlflow.pyfunc.log_model(
    python_model=CustomModel(),
    artifact_path="model",
    code_path=["preprocessing_utils/"],
)
```

Inside the model, the shared module is imported in `load_context` and used during inference:^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])

    def predict(self, context, model_input):
        # preprocessing and inference logic
        ...
```

After logging, the model can be registered to [Unity Catalog](/concepts/unity-catalog.md) or the Workspace Registry and deployed to a Model Serving endpoint. All shared modules are automatically available in the serving environment.^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Best practices

- **Organize shared code into well‑defined packages.** Use directories that can stand alone and have a clear purpose (e.g., `preprocessing_utils/`, `postprocessing/`).
- **Minimize the dependency surface.** Include only the modules actually needed by the model to keep the artifact size small and deployment fast.
- **Version your shared modules.** If the shared code changes, log a new model version to ensure consistency between the model and its dependencies.

## Related concepts

- MLflow PyFunc – The generic Python function model format used with `code_path`
- [Model Serving](/concepts/model-serving.md) – Deployment target for logged PyFunc models
- Custom MLflow model deployment – Full guide on packaging and deploying custom code
- [Unity Catalog](/concepts/unity-catalog.md) – Registry for logged models that supports `code_path`

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
