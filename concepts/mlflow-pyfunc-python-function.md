---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3e8d122d9d1a6460f33e177cc0e0396f3f9a5b22eed074c4b1fa81dd8a5e6a4
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-pyfunc-python-function
    - MP(F
    - MLflow Python Function (pyfunc)
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: MLflow pyfunc (Python Function)
description: MLflow's Python function format that allows deploying any Python code or model as a serveable model on Databricks Model Serving
tags:
  - mlflow
  - model-serving
  - python
timestamp: "2026-06-18T11:59:28.324Z"
---

# MLflow pyfunc (Python Function)

**MLflow pyfunc** (Python function) is a flexible model flavor within [MLflow](/concepts/mlflow.md) that allows you to package and deploy arbitrary Python code as a model. It is designed for scenarios where your model requires preprocessing or postprocessing logic, uses a framework not natively supported by MLflow, or needs custom per‑request branching logic. Any Python callable that follows the `pyfunc` interface can be served through [Model Serving](/concepts/model-serving.md) on Databricks. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Construct a custom pyfunc model

To create a custom pyfunc model, define a class that inherits from `mlflow.pyfunc.PythonModel` and implements two required methods:

1. **`load_context(self, context)`** – This method is called once when the model is loaded. Use it to set up resources that persist across prediction calls, such as loading model weights, initialising tokenizers, or importing shared modules. Keeping such initialization outside `predict` minimises per‑request overhead and speeds up inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

2. **`predict(self, context, model_input)`** – This method contains the logic that runs for every input request. It receives the model input and should return the prediction output. Any preprocessing, inference, and postprocessing steps can be orchestrated here.

```python
import mlflow.pyfunc

class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        # One-time setup: load model, tokenizers, etc.
        pass

    def predict(self, context, model_input):
        # Per-request logic
        return model_input
```

Before deploying, you can validate the model locally using `mlflow.models.predict()` to ensure it behaves as expected. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Log the pyfunc model

Once the model class is defined, log it with `mlflow.pyfunc.log_model()`. This registers the model in the MLflow tracking server and can also register it in [Unity Catalog](/concepts/unity-catalog.md) or the workspace registry.

**Important:** When running on Databricks Runtime ML (which ships `mlflow-skinny` instead of the full `mlflow`), you must explicitly include `mlflow` in the `pip_requirements` parameter. Model Serving requires the full `mlflow` package to build the container image. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=my_custom_model_instance,
    pip_requirements=["mlflow==3.8.1"],   # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

### Reusing shared code with `code_path`

If your model depends on helper modules or utilities, you can include them using the `code_path` parameter. MLflow packages the specified directories or files so they are available when the model is loaded. For example, if you log with `code_path=["preprocessing_utils/"]`, modules from that directory can be imported inside your `PythonModel` class. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serve the model

After logging and registering the model, you can create a [Model Serving](/concepts/model-serving.md) endpoint. Model Serving automatically loads the logged pyfunc model and serves inference requests through a REST API. No additional containerisation steps are required; Databricks handles the deployment. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Example notebook

A notebook example illustrating how to customize model output with pyfunc is available in the Databricks documentation. It demonstrates postprocessing raw model outputs so they are ready for consumption by downstream applications. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related concepts

- [Model Serving](/concepts/model-serving.md)
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Workspace Registry](/concepts/workspace-model-registry.md)
- [Custom MLflow PythonModel](/concepts/custom-mlflow-pythonmodel.md)

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
