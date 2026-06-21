---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aef767530e2c88ac78f8daf9bcc69b7436a433b94a680cea3d98397df2ea8372
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - preprocessing-and-postprocessing-with-pyfunc
    - Postprocessing with PyFunc and Preprocessing
    - PAPWP
    - Preprocessing and Postprocessing
    - preprocessing
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Preprocessing and Postprocessing with PyFunc
description: Using custom pyfunc models to add preprocessing (input formatting) and postprocessing (output formatting) logic around model inference.
tags:
  - mlflow
  - preprocessing
  - postprocessing
timestamp: "2026-06-19T15:10:52.928Z"
---

# Preprocessing and Postprocessing with PyFunc

**Preprocessing and Postprocessing with PyFunc** refers to the practice of using MLflow's Python function (`pyfunc`) model format to encapsulate custom data transformation logic before and after model inference. This approach enables deployment of arbitrary Python code as a model, allowing for flexible input formatting and output transformation.

## Overview

MLflow's `pyfunc` provides flexibility to deploy any piece of Python code or any Python model. This is particularly useful when your application requires preprocessing before inputs can be passed to the model's predict function, or when the model's raw outputs need to be post-processed for consumption. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

Common scenarios where preprocessing and postprocessing with PyFunc is beneficial include:

- Models that require preprocessing before inputs can be passed to the model's predict function
- Model frameworks not natively supported by MLflow
- Applications requiring the model's raw outputs to be post-processed for consumption
- Models with per-request branching logic
- Deploying fully custom code as a model

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Constructing a Custom MLflow Python Function Model

MLflow offers the ability to log Python code with the [custom Python models format](/concepts/custom-mlflow-pythonmodel.md). There are two required functions when packaging arbitrary Python code with MLflow: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `load_context`

The `load_context` function defines anything that needs to be loaded just one time for the model to operate. This is critical so that the system minimizes the number of artifacts loaded during the `predict` function, which speeds up inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `predict`

The `predict` function houses all the logic that is run every time an input request is made. This is where preprocessing and postprocessing logic is typically implemented. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Example Implementation

The following example demonstrates a custom PyFunc model that includes both preprocessing and postprocessing logic:

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

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Using Shared Code Modules

Even when writing a model with custom code, it is possible to use shared modules of code from your organization. With the `code_path` parameter, authors of models can log full code references that load into the path and are usable from other custom `pyfunc` models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

For example, if a model is logged with:

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path = ["preprocessing_utils/"])
```

Code from the `preprocessing_utils` directory becomes available in the loaded context of the model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Logging the Model

When logging a `pyfunc` model on Databricks Runtime ML runtimes, it is important to note that these runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. Model Serving requires `mlflow` (not `mlflow-skinny`) in `conda.yaml` and cannot build the container image otherwise. Always specify `mlflow==<version>` in `pip_requirements` when calling `mlflow.pyfunc.log_model()` on a Databricks Runtime ML runtime: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],
    registered_model_name="catalog.schema.model_name",
)
```

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serving the Model

After logging a custom `pyfunc` model, it can be registered to [Unity Catalog](/concepts/unity-catalog.md) or [Workspace Registry](/concepts/workspace-model-registry.md) and served to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Validation

Prior to deploying custom code as a model, it is beneficial to verify that the model is capable of being served. MLflow provides `mlflow.models.predict` to [validate models before deployment](/concepts/model-validation-before-deployment.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow PyFunc – The underlying model format for custom Python code deployment
- [Model Serving](/concepts/model-serving.md) – The infrastructure for deploying models to endpoints
- [Custom Python Models Format](/concepts/custom-mlflow-pythonmodel.md) – MLflow's format for packaging arbitrary Python code
- [Unity Catalog](/concepts/unity-catalog.md) – Model registry for managing and deploying models
- [Workspace Registry](/concepts/workspace-model-registry.md) – Alternative model registry for workspace-scoped models

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
