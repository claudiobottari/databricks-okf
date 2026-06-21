---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4548807de174b0091314afb93ed70bfd034575904f3d551e794bcf526e30f05
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-pyfunc-load_context-pattern
    - MPLP
    - MLP
    - PyFunc load_context
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: MLflow pyfunc load_context Pattern
description: The design pattern of separating one-time initialization (load_context) from per-request prediction logic (predict) in custom MLflow pyfunc models
tags:
  - mlflow
  - design-pattern
  - model-serving
timestamp: "2026-06-19T10:12:02.734Z"
---

Here is the wiki page for "MLflow pyfunc load_context Pattern".

---

## MLflow pyfunc load_context Pattern

The **MLflow pyfunc load_context Pattern** is a method for packaging custom Python code as an [MLflow](/concepts/mlflow.md) model using the `mlflow.pyfunc` module. It separates one-time initialization logic from per-request inference logic by defining two required functions: `load_context` and `predict`. This pattern is the standard way to deploy any arbitrary Python code or model that is not natively supported by MLflow. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Overview

The `load_context` pattern is part of the [custom Python models format](/concepts/custom-mlflow-pythonmodel.md) in MLflow. It allows you to include preprocessing, postprocessing, or branching logic alongside your model. By separating expensive initialization from per-request execution, the pattern minimizes the overhead on each inference call, speeding up serving. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

Common use cases for this pattern include:

- Models that require preprocessing before inputs can be passed to the model's predict function.
- Models built with frameworks not natively supported by MLflow.
- Applications that need model outputs post-processed before consumption.
- Models with per-request branching logic.
- Deploying fully custom code as a model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Required Components

### load_context

The `load_context` function loads any artifacts or dependencies that are needed only once for the model to operate. This is critical for minimizing the number of artifacts loaded during the `predict` function, which keeps inference fast. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

Typical items initialized in `load_context` include:

- Pre-trained model weights (`torch.load`, `pickle.load`, etc.).
- Tokenizers, vectorizers, or other preprocessing objects.
- Database connections or external service clients.

### predict

The `predict` function contains the logic that runs on every input request. It receives a `context` object (which carries the artifacts and dependencies initialized in `load_context`) and the `model_input` from the caller. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Example Implementation

The following example demonstrates a custom `pyfunc` model that uses the `load_context` pattern: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
import mlflow
import torch

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

In this example:

- `load_context` loads PyTorch model weights and a custom tokenizer from artifacts passed via the `context` object.
- `predict` runs the formatting functions (preprocessing and postprocessing) and invokes the model's forward pass.
- The `context.artifacts` dictionary contains the paths to logged artifacts, allowing the model to locate its dependencies at load time.

## Logging the Model with pip_requirements

When logging a `pyfunc` model from a [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) environment, you must explicitly specify `mlflow` (not `mlflow-skinny`) in the `pip_requirements` parameter. Databricks Runtime ML ships with `mlflow-skinny` by default, and Model Serving cannot build the container image without the full `mlflow` package: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

## Sharing Code with code_path

Models can reference shared modules from other locations using the `code_path` parameter. When logged with `code_path`, those modules are available in the loaded context of the model via standard Python imports: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    CustomModel(),
    "model",
    code_path=["preprocessing_utils/"],
)
```

The shared code (e.g., `preprocessing_utils/my_custom_tokenizer.py`) can then be imported inside `load_context`, as shown in the example above.

## Serving the Model

After logging the custom `pyfunc` model, you can register it to [Unity Catalog](/concepts/unity-catalog.md) or the Workspace Registry and serve it to a [Model Serving](/concepts/model-serving.md) endpoint. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Best Practices

- **Load all heavy artifacts in `load_context`**, not in `predict`. Every second spent loading artifacts in `predict` is added to every request's latency.
- **Validate your model before deployment** using `mlflow.models.predict` to confirm that the model can be served.
- **Use shared modules** via `code_path` to avoid duplicating common preprocessing or utility code across multiple models.
- **Always specify `mlflow` in `pip_requirements`** when logging from Databricks Runtime ML environments to avoid the `mlflow-skinny` issue.

## Related Concepts

- [MLflow pyfunc Module](/concepts/custom-mlflow-pythonmodel.md) — The full Python API for creating custom pyfunc models.
- [Model Serving](/concepts/model-serving.md) — Deploying models to production endpoints.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built runtime that includes GPU support and common deep learning libraries.
- [Unity Catalog](/concepts/unity-catalog.md) — Managing model registries and permissions.
- [Custom Python Models (MLflow)](/concepts/custom-mlflow-pythonmodel.md) — Official MLflow documentation for the custom pyfunc format.

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
