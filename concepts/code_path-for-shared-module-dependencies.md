---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04f498acdd34d2ab394f89d324a606b99643575b2dd8cade49569f4baefe8855
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code_path-for-shared-module-dependencies
    - CFSMD
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: code_path for Shared Module Dependencies
description: The code_path parameter in mlflow.pyfunc.log_model() allows logging full code references (shared modules) that load into the model's context and are usable from custom pyfunc models.
tags:
  - mlflow
  - python
  - dependencies
timestamp: "2026-06-18T15:26:59.131Z"
---

Based on the provided material, here is the wiki page for "code_path for Shared Module Dependencies".

---

## `code_path` for Shared Module Dependencies

**`code_path` for Shared Module Dependencies** refers to a feature of MLflow's `pyfunc` model format that allows developers to bundle additional Python source code directories with their model. When a model is logged using `mlflow.pyfunc.log_model()`, the `code_path` parameter specifies a list of directories containing shared modules (e.g., preprocessing utilities, custom tokenizers, or other helper code) that are included in the model's deployment artifact. This ensures that the custom code is available in the model's runtime environment. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Purpose and Benefits

The `code_path` parameter enables the reuse of shared organizational code across multiple custom `pyfunc` models. By logging a full code reference via `code_path`, authors can package modules that other custom models can load and use. This avoids duplicating code and simplifies maintaining shared dependencies. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### How to Use

When logging a model, pass a list of directory paths to the `code_path` parameter. The following example logs a custom model and includes the `preprocessing_utils/` directory:

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path = ["preprocessing_utils/"])
```

The code from `preprocessing_utils` becomes available in the loaded context of the model. Inside a custom model class, you can import and use these modules as needed. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Example Model

The following example shows a custom model that uses a shared tokenizer module from the `code_path` directory:

```python
class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])
```

This pattern allows multiple `pyfunc` models to share common logic such as preprocessing, tokenization, or post-processing steps. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Important Considerations

- **Runtime compatibility**: When logging a `pyfunc` model on a Databricks Runtime ML runtime (which includes `mlflow-skinny` by default), you must explicitly specify `mlflow` in `pip_requirements`. This is because `Model Serving` requires the full `mlflow` package to build the container image. Without this step, the deployment will fail. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],
    registered_model_name="catalog.schema.model_name",
)
```

### Related Concepts

- MLflow PyFunc – The model format that enables custom Python code deployment.
- [Model Serving](/concepts/model-serving.md) – The platform for serving models logged with `pyfunc`.
- Preprocessing and Postprocessing – Common use cases for `code_path` in model pipelines.
- MLflow Skinny – The minimal MLflow package; full `mlflow` is required for serving.

### Sources

- `deploy-python-code-with-model-serving-databricks-on-aws.md`

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
