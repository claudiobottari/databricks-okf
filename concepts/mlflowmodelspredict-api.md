---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd75c18eda3d59976881dd0d8e1686479e2529778bfb3e3d42e1718083c01b8a
  pageDirectory: concepts
  sources:
    - pre-deployment-validation-for-model-serving-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowmodelspredict-api
    - mlflow models predict
    - mlflow.models.predict
  citations:
    - file: pre-deployment-validation-for-model-serving-databricks-on-aws.md
title: mlflow.models.predict API
description: MLflow API for testing offline model predictions in a simulated serving environment before endpoint deployment.
tags:
  - MLflow
  - model-serving
  - validation
timestamp: "2026-06-19T19:56:42.963Z"
---

# mlflow.models.predict API

The `mlflow.models.predict` API is a pre-deployment validation function provided by MLflow. It allows you to test predictions from a logged model in a simulated serving environment before deploying it to a model serving endpoint. This helps catch issues with model dependencies, input formatting, or environment mismatches early in the development cycle. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Parameters

The API accepts the following parameters:

- **`model_uri`** – The URI of the model that will be deployed to model serving (e.g., `runs:/<run_id>/model`).
- **`input_data`** – The input data in the expected format for the model’s `pyfunc.predict()` call. Alternatively, use **`input_path`** to point to a file containing input data that will be loaded and used for the prediction.
- **`content_type`** – The format of the input data, either `"csv"` or `"json"`.
- **`output_path`** (optional) – Write the predictions to a file. If omitted, predictions are printed to `stdout`.
- **`env_manager`** – The environment manager used to build the serving environment. Default is `"virtualenv"`, which is recommended for serving validation. The `"local"` option is available but can be error‑prone for serving validation and is generally used only for rapid debugging.
- **`install_mlflow`** – Whether to install the current version of MLflow from your environment into the virtual environment. Defaults to `False`.
- **`pip_requirements_override`** – A list of string dependency overrides or additions for troubleshooting or debugging (e.g., `["pillow==10.3.0", "scipy==1.13.0"]`).

^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Usage Example

The following Python snippet demonstrates using `mlflow.models.predict` to test a model logged in a run:

```python
import mlflow

run_id = "..."
model_uri = f"runs:/{run_id}/model"

mlflow.models.predict(
  model_uri=model_uri,
  input_data={"col1": 34.2, "col2": 11.2, "col3": "green"},
  content_type="json",
  env_manager="virtualenv",
  install_mlflow=False,
  pip_requirements_override=["pillow==10.3.0", "scipy==1.13.0"],
)
```

^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Relationship to Other Validation Tools

The `mlflow.models.predict` API is one of two pre‑deployment validation options offered by MLflow. The other is the [MLflow CLI](https://mlflow.org/docs/latest/cli.html#mlflow-models-predict). Both rely on the same underlying logic. For validating that the model input works on a serving endpoint, Databricks recommends using the separate `validate_serving_input` function, which checks the special JSON format expected by model serving endpoints. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [MLflow model deployment](/concepts/mlflow-model-serving-and-deployment.md)
- [Pre-deployment model validation](/concepts/pre-deployment-validation-for-model-serving.md)
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)
- mlflow.pyfunc.PyFuncModel

## Sources

- pre-deployment-validation-for-model-serving-databricks-on-aws.md

# Citations

1. [pre-deployment-validation-for-model-serving-databricks-on-aws.md](/references/pre-deployment-validation-for-model-serving-databricks-on-aws-77a7c1ae.md)
