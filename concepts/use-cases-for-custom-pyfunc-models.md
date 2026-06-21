---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58f9b0e932bb73bca72e3e5c363e80519fe8d13e93e8520c30bc51f9817c6ea4
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - use-cases-for-custom-pyfunc-models
    - UCFCPM
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Use Cases for Custom PyFunc Models
description: "Scenarios where custom pyfunc is needed: unsupported frameworks, preprocessing/postprocessing, per-request branching logic, and fully custom code deployment."
tags:
  - mlflow
  - model-serving
  - use-cases
timestamp: "2026-06-19T15:11:29.737Z"
---

## Use Cases for Custom PyFunc Models

Custom [PyFunc models](/concepts/custom-mlflow-pythonmodel.md) in MLflow provide a flexible way to deploy any piece of Python code or Python-based model through [Model Serving](/concepts/model-serving.md). The `pyfunc` format gives you full control over the prediction pipeline, allowing you to embed custom logic that runs before or after the core model inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### When to Use a Custom PyFunc

MLflow recommends custom `pyfunc` models in several common scenarios:

- **Model framework not natively supported.** If your training framework or model library is not one of MLflow's built-in flavors (e.g., `sklearn`, `pytorch`, `keras`), `pyfunc` lets you wrap arbitrary Python code as a deployable model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Preprocessing is required before inference.** When raw inputs must be transformed, cleaned, or formatted before they can be passed to the model's `predict` function, you can encode that logic inside the custom `pyfunc`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Postprocessing of raw outputs.** If your application needs the model's raw predictions to be decoded, thresholded, or restructured before they are consumed by the end user, the postprocessing step belongs in the `predict` method of the custom model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Per-request branching logic.** When different input requests require different processing paths – for example, routing some inputs through a specialized sub-model – the branching logic can be implemented inside the custom `pyfunc`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Deploying fully custom code.** You can use `pyfunc` to deploy code that has no direct relationship to a pre-trained model, such as a custom business logic engine, an image processing pipeline, or a bespoke scoring algorithm. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Required Functions for Custom PyFunc

When you package arbitrary Python code with MLflow, you must implement two methods on a class that inherits from `mlflow.pyfunc.PythonModel`:

- **`load_context(self, context)`** – This method is called once when the model is loaded. It is the right place to set up expensive or shared resources that should be initialized only a single time, such as loading model weights from disk, instantiating a tokenizer, or connecting to a database. Keeping these operations in `load_context` minimizes the work done inside `predict` and speeds up inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **`predict(self, context, model_input)`** – This method is invoked on every input request. It contains all the logic that must run per-request, including formatting inputs, calling a model, and formatting outputs. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Using Shared Code with `code_path`

Custom `pyfunc` models can import shared utility modules from your organization. When you log a model with the `code_path` parameter, MLflow copies the referenced code into the model's artifact directory. That code is then available for import inside `load_context` or `predict` from any other custom `pyfunc` model that depends on the same module. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

Example:

```python
mlflow.pyfunc.log_model(
    CustomModel(),
    "model",
    code_path=["preprocessing_utils/"]
)
```

Inside the model class, you can then import from that path:

```python
from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
```

### Logging and Registration Requirements

When you log a `pyfunc` model on a Databricks Runtime ML instance (which ships `mlflow-skinny` by default), you must explicitly include `mlflow==<version>` in the `pip_requirements` argument. Without this, MLflow captures `mlflow-skinny` in the model's `conda.yaml`, and [Model Serving](/concepts/model-serving.md) cannot build the container image because it requires the full `mlflow` package. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Related Concepts

- [MLflow PythonModel](/concepts/custom-mlflow-pythonmodel.md) – The base class for custom `pyfunc` implementations.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – Where logged custom models are deployed for real-time inference.
- [Unity Catalog](/concepts/unity-catalog.md) – Registry for managing and governing custom pyfunc models.
- mlflow-skinny – The minimal MLflow distribution that should be avoided in serving artifacts.
- [preprocessing](/concepts/preprocessing-and-postprocessing-with-pyfunc.md) and postprocessing – Common pipeline stages implemented inside custom pyfunc models.

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
