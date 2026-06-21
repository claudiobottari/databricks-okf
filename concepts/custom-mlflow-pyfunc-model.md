---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 119398d74cc3f0ef317f8783ae7aa8471f9a4963303e2b893aaf43805f6fe72d
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-mlflow-pyfunc-model
    - CMPM
    - Custom MLflow PyFunc Models
    - MLflow PyFunc Model
    - MLflow PyFunc model
    - custom PyFunc model
    - Custom MLflow Python Function Model
    - Custom PyFunc Model Creation
    - Custom PyFunc Models
    - Custom PyFunc models
    - MLflow PyFunc Models
    - MLflow Pyfunc
    - MLflow pyfunc Module
    - MLflow pyfunc interface
    - PyFunc Model
    - PyFunc Model Flavor
    - PyFunc Model Logging
    - PyFunc models
    - custom PyFunc models
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Custom MLflow PyFunc Model
description: A pattern for packaging arbitrary Python code as an MLflow model using mlflow.pyfunc.PythonModel, requiring implementations of load_context and predict methods.
tags:
  - mlflow
  - model-serving
  - python
timestamp: "2026-06-19T18:30:20.987Z"
---

---
title: Custom MLflow PyFunc Model
summary: A pattern for packaging arbitrary Python code as an MLflow model using pyfunc, requiring load_context and predict functions.
sources:
  - deploy-python-code-with-model-serving-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:11:56.657Z"
updatedAt: "2026-06-19T15:10:51.650Z"
tags:
  - mlflow
  - model-serving
  - python
aliases:
  - custom-mlflow-pyfunc-model
  - CMPM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Custom MLflow PyFunc Model

**Custom MLflow PyFunc Model** refers to the ability to package arbitrary Python code as an MLflow model using the `pyfunc` (Python function) flavor. This approach allows you to deploy fully custom logic, including preprocessing, postprocessing, per-request branching, or models built with frameworks not natively supported by MLflow. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Overview

MLflow's Python function (`pyfunc`) flavor provides flexibility to deploy any piece of Python code or any Python model. It is particularly useful in scenarios where:

- Your model requires preprocessing before inputs can be passed to the model's predict function.
- Your model framework is not natively supported by MLflow.
- The model's raw outputs need to be post-processed for consumption.
- The model has per-request branching logic.
- You are looking to deploy fully custom code as a model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

The resulting custom model can be registered in [Unity Catalog](/concepts/unity-catalog.md) or [Workspace Registry](/concepts/workspace-model-registry.md) and served via [Model Serving](/concepts/model-serving.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Constructing a Custom PyFunc Model

To package arbitrary Python code with MLflow, you create a class that inherits from `mlflow.pyfunc.PythonModel` and implement two required functions:

### `load_context(context)`
This method is called once when the model is loaded. It should contain any one-time initialization logic, such as loading model weights, tokenizers, or other artifacts. Keeping heavy initialization out of the `predict` function speeds up inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `predict(context, model_input)`
This method is called for every inference request. It houses all the logic that runs each time an input is received, including preprocessing, model inference, and postprocessing. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

You can validate your custom model before deployment using `mlflow.models.predict`; see the MLflow validation documentation. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Logging the Model

Use `mlflow.pyfunc.log_model()` to log your custom model. Note an important requirement when running on [Databricks Runtime ML](/concepts/databricks-runtime-ml.md): those runtimes ship `mlflow-skinny` rather than the full `mlflow` package. If you log a `pyfunc` model without explicitly specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model's `conda.yaml`. Model Serving requires the full `mlflow` package to build the container image — therefore you must always specify `mlflow==<version>` in `pip_requirements`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],   # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

### Reusing Shared Code Modules

You can include shared Python code via the `code_path` parameter. This allows the custom model to reference utility modules from other parts of your codebase. For example:

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path=["preprocessing_utils/"])
```

After logging, modules from `preprocessing_utils/` become importable inside the model's `load_context` and `predict` methods. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serving the Model

After logging and registering the custom `pyfunc` model to Unity Catalog or Workspace Registry, you can deploy it to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). The serving infrastructure automatically loads the model, calls `load_context` once at startup, and then routes each inference request through the `predict` method. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Example: Custom PyFunc Model with Preprocessing and Postprocessing

The following example from the Databricks documentation demonstrates a custom model that preprocesses inputs and postprocesses outputs:

```python
class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])

    def format_inputs(self, model_input):
        # code that formats inputs
        pass

    def format_outputs(self, outputs):
        predictions = (torch.sigmoid(outputs)).data.numpy()
        return predictions

    def predict(self, context, model_input):
        model_input = self.format_inputs(model_input)
        outputs = self.model.predict(model_input)
        return self.format_outputs(outputs)
```

This pattern enables full control over the inference pipeline while remaining compatible with MLflow's deployment infrastructure. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow pyfunc — The core MLflow flavor for Python models.
- [Model Serving](/concepts/model-serving.md) — Deployment endpoint for serving pyfunc models.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — Pre-built runtime that includes MLflow (skinny) and deep learning libraries.
- [Unity Catalog](/concepts/unity-catalog.md) — Model registry for managing and governing models.
- [Workspace Registry](/concepts/workspace-model-registry.md) — Alternative model registry for workspace-scoped models.

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
