---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84c1d1f2405d8eea97c9ccb131cf52350291911fb643b62d14d24c25fdceebc9
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-deployment
    - MSED
    - Model Serving Deployment
    - Model Deployment
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Model Serving Endpoint Deployment
description: The process of registering a custom pyfunc model to Unity Catalog or Workspace Registry and serving it via a Model Serving endpoint on Databricks.
tags:
  - databricks
  - model-serving
  - deployment
timestamp: "2026-06-19T15:10:51.397Z"
---

# Model Serving Endpoint Deployment

**Model Serving Endpoint Deployment** refers to the process of deploying custom Python code or machine learning models as a scalable serving endpoint on Databricks Model Serving. This enables real-time inference with preprocessing, postprocessing, and custom logic integrated into the serving pipeline.

## Overview

Model Serving endpoints allow you to deploy any piece of Python code or Python model using MLflow's Python function (`pyfunc`) format. This approach provides flexibility for scenarios where standard model deployment is insufficient. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

Common use cases include:
- Models requiring preprocessing before inputs can be passed to the model's predict function
- Model frameworks not natively supported by MLflow
- Applications requiring post-processing of raw model outputs for consumption
- Models with per-request branching logic
- Deployment of fully custom code as a model

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Constructing a Custom MLflow Python Function Model

MLflow supports logging Python code using the [custom Python models format](/concepts/custom-mlflow-pythonmodel.md). When packaging arbitrary Python code with MLflow, two required functions must be defined: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `load_context`

This function handles anything that needs to be loaded once for the model to operate. Defining initialization logic here is critical to minimize the number of artifacts loaded during the `predict` function, which speeds up inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `predict`

This function contains all the logic executed every time an input request is made. It receives the model input and returns the processed output. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Logging Your Python Function Model

When logging a `pyfunc` model on Databricks Runtime ML runtimes, it is important to note that these runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. Model Serving requires `mlflow` (not `mlflow-skinny`) in the model's `conda.yaml` to build the container image. Always specify `mlflow==<version>` in `pip_requirements` when calling `mlflow.pyfunc.log_model()`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],
    registered_model_name="catalog.schema.model_name",
)
```

### Using Shared Code Modules

Custom `pyfunc` models can leverage shared modules from your organization using the `code_path` parameter. This allows authors to log full code references that load into the path and are usable from other custom `pyfunc` models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path=["preprocessing_utils/"])
```

### Example Custom Model

The following example demonstrates a custom model that uses shared code and implements preprocessing and postprocessing logic: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])

    def format_inputs(self, model_input):
        # insert some code that formats your inputs
        pass

    def format_outputs(self, outputs):
        predictions = (torch.sigmoid(outputs)).data.numpy()
        return predictions

    def predict(self, context, model_input):
        model_input = self.format_inputs(model_input)
        outputs = self.model.predict(model_input)
        return self.format_outputs(outputs)
```

## Validation Before Deployment

Prior to deploying custom code as a model, it is recommended to verify that the model is capable of being served. MLflow provides `mlflow.models.predict` for [validating models before deployment](/concepts/model-validation-before-deployment.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serving the Model

After logging a custom `pyfunc` model, you can register it to [Unity Catalog](/concepts/unity-catalog.md) or [Workspace Registry](/concepts/workspace-model-registry.md) and serve the model to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow PyFunc — The Python function format for custom model deployment
- [Model Serving](/concepts/model-serving.md) — The serving infrastructure for real-time inference
- [Unity Catalog](/concepts/unity-catalog.md) — Model registry for managing and governing models
- [Workspace Registry](/concepts/workspace-model-registry.md) — Alternative model registry for workspace-scoped models
- [Custom Python Models Format](/concepts/custom-mlflow-pythonmodel.md) — MLflow's format for packaging arbitrary Python code
- [Model Validation](/concepts/model-validation-pipeline.md) — Pre-deployment validation of model serving capability

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
