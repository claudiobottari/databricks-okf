---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42a9ab108f505d020c4f1eb04c92a4380d016d741f08b5a78af9c2a5b4c87d3a
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deploying-non-natively-supported-frameworks-with-mlflow
    - DNSFWM
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Deploying Non-Natively Supported Frameworks with MLflow
description: Using MLflow pyfunc to deploy models whose frameworks are not natively supported by MLflow's built-in flavors
tags:
  - mlflow
  - model-serving
  - databricks
timestamp: "2026-06-19T10:13:11.425Z"
---

# Deploying Non-Natively Supported Frameworks with MLflow

**Deploying Non-Natively Supported Frameworks with MLflow** refers to the process of using MLflow's Python function (`pyfunc`) format to package, log, and serve machine learning models built with frameworks that are not natively supported by MLflow's built-in model flavors. This approach enables organizations to deploy any arbitrary Python code, including custom preprocessing, postprocessing, and branching logic, as a production-grade model serving endpoint.

## Overview

MLflow provides native support for several popular machine learning frameworks. However, many production use cases require the ability to deploy models built with unsupported frameworks, custom inference logic, or complex data transformations. The `pyfunc` format offers a flexible mechanism to package any Python code as an MLflow model, making it suitable for deployment on platforms like Databricks Model Serving. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Common Use Cases

Organizations typically use the `pyfunc` approach for the following scenarios: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

- **Framework incompatibility**: The model is built with a framework not natively supported by MLflow (e.g., custom PyTorch models, specialized libraries).
- **Preprocessing requirements**: Input data must be transformed before being passed to the model's `predict` function.
- **Postprocessing requirements**: Raw model outputs must be converted into a consumable format for the application.
- **Per-request branching logic**: The model needs to make decisions during inference that vary by request.
- **Fully custom code deployment**: The "model" is entirely custom Python code with no underlying ML framework.

## Constructing a Custom MLflow Python Function Model

To package arbitrary Python code with MLflow, you create a class that extends `mlflow.pyfunc.PythonModel` and implements two required functions: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `load_context`

This function handles any initialization that should occur only once when the model is loaded. It is critical for minimizing the number of artifacts loaded during the `predict` function, which speeds up inference. Common use cases include loading model weights, initializing tokenizers, and establishing connections. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `predict`

This function houses all the logic that runs every time an input request is made. It receives the model context and the input data, and returns the prediction output. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Example

```python
class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])

    def format_inputs(self, model_input):
        # preprocessing logic
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

## Logging the Model

When logging a custom `pyfunc` model, you must pay attention to the runtime environment. Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. When you log a `pyfunc` model on one of these runtimes without specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model's `conda.yaml`. Model Serving requires `mlflow` (not `mlflow-skinny`) in `conda.yaml` to build the container image successfully. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
# DBR ML ships with mlflow-skinny by default, so specify mlflow explicitly
# to ensure Model Serving compatibility.
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Using Shared Code Modules

Custom `pyfunc` models can leverage shared modules from your organization using the `code_path` parameter. This allows authors to log full code references that load into the path and are usable from other custom `pyfunc` models. For example, if a model is logged with `mlflow.pyfunc.log_model(CustomModel(), "model", code_path=["preprocessing_utils/"])`, code from the `preprocessing_utils` directory is available in the loaded context of the model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Validating the Model Before Deployment

Prior to deploying custom code as a model, it is beneficial to verify that the model is capable of being served. MLflow provides tools through `mlflow.models.predict` to validate models before deployment. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serving the Model

After logging a custom `pyfunc` model, you can register it to [Unity Catalog](/concepts/unity-catalog.md) or Workspace Registry and serve it to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). The standard process for creating and managing serving endpoints applies to custom `pyfunc` models just as it does for natively supported frameworks. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- [MLflow Pyfunc](/concepts/custom-mlflow-pyfunc-model.md) — The Python function model format for custom models
- [Model Serving](/concepts/model-serving.md) — Deploying models to production endpoints
- [Unity Catalog](/concepts/unity-catalog.md) — Managing models with Unity Catalog
- [MLflow Model Flavors](/concepts/mlflow-model-flavors.md) — Natively supported model formats
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built runtime environment

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
