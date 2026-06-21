---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f7690c6bee641dc75c4ae88beb2d6295140b58b64499ee108125587e428612b9
  pageDirectory: concepts
  sources:
    - pre-deployment-validation-for-model-serving-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-dependency-management
    - MMDM
  citations:
    - file: pre-deployment-validation-for-model-serving-databricks-on-aws.md
title: MLflow Model Dependency Management
description: Process of updating pip requirements of a logged MLflow model in-place without re-logging the model.
tags:
  - MLflow
  - model-management
  - dependencies
timestamp: "2026-06-19T19:57:22.989Z"
---

# MLflow Model Dependency Management

**MLflow Model Dependency Management** refers to the set of tools, APIs, and practices within [MLflow](/concepts/mlflow.md) for managing, validating, and updating the software dependencies (Python packages and libraries) that a machine learning model requires for prediction. Proper dependency management ensures that models can be deployed and served consistently across different environments.

## Overview

When a model is logged to MLflow, its dependencies are captured in a `pip_requirements.txt` file and a `conda.yaml` environment definition. These files specify the exact package versions needed to run the model. However, dependencies can become outdated, incompatible, or require updating after the model is logged. MLflow provides validation and update mechanisms to handle these scenarios without requiring the model to be re-logged. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Pre-Deployment Validation

Before deploying a model to a serving endpoint, MLflow offers validation APIs that simulate the deployment environment. Using `mlflow.models.predict` with a virtual environment manager (`env_manager="virtualenv"`), you can test whether the model's dependencies work correctly on the target infrastructure. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

### Key Parameters

The `mlflow.models.predict` API accepts:

- **`model_uri`**: The URI of the logged model (e.g., `runs:/<run_id>/model`).
- **`input_data`** or **`input_path`**: The input data to test predictions with.
- **`content_type`**: Either `"csv"` or `"json"`.
- **`env_manager`**: The environment manager used to build the serving environment. The default is `virtualenv`, recommended for serving validation. Use `local` only for rapid debugging.
- **`install_mlflow`**: Whether to install the current version of MLflow in the virtual environment. Defaults to `False`.
- **`pip_requirements_override`**: A list of dependency overrides for testing different package versions during debugging.

^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

### Example

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

## Updating Model Dependencies

If there are issues with the dependencies specified with a logged model, you can update the requirements in-place without logging a new model using the MLflow CLI or the `mlflow.models.model.update_model_requirements()` Python API. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

### Using the Python API

The `update_model_requirements` function modifies the `pip_requirements.txt` file within the MLflow model artifact at the specified `model_uri` location.

- **`operation`**: Either `"add"` to add new requirements or other operations for updating.
- **`requirement_list`**: A list of dependency strings to add or update.

```python
from mlflow.models.model import update_model_requirements

update_model_requirements(
    model_uri=model_uri,
    operation="add",
    requirement_list=["pillow==10.2.0", "scipy==1.12.0"],
)
```

^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Validating Serving Input

Model serving endpoints expect a specific JSON input format. MLflow provides `validate_serving_input` to verify that your model's input works correctly before deployment. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

### Example

```python
from mlflow.models import validate_serving_input

model_uri = 'runs:/<run_id>/<artifact_path>'

serving_payload = """{
  "messages": [
    {
      "content": "How many product categories are there?",
      "role": "user"
    }
  ]
}"""

validate_serving_input(model_uri, serving_payload)
```

^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

You can also generate valid serving payloads from input examples using `convert_input_example_to_serving_input`. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

```python
from mlflow.models import convert_input_example_to_serving_input

# Define INPUT_EXAMPLE with your own input example
model_uri = 'runs:/<run_id>/<artifact_path>'
serving_payload = convert_input_example_to_serving_input(INPUT_EXAMPLE)
validate_serving_input(model_uri, serving_payload)
```

^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Manual Testing

For manual testing outside of automated pipelines, you can load the model locally using MLflow: ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

```python
import os
import mlflow

os.environ["MLFLOW_TRACKING_URI"] = "databricks://PROFILE"
ARTIFACT_URI = "model_uri"

local_path = mlflow.artifacts.download_artifacts(ARTIFACT_URI)
# Then manually create the conda environment and load the model
```

^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow Models – The core abstraction for packaging machine learning models.
- [MLflow Model Deployment](/concepts/mlflow-model-serving-and-deployment.md) – The process of serving models to production endpoints.
- [Model Serving](/concepts/model-serving.md) – Production inference endpoints on Databricks.
- Conda Environment – The environment definition used alongside pip requirements.
- MLflow CLI – Command-line interface for model management operations.
- [PyFunc Model](/concepts/custom-mlflow-pyfunc-model.md) – The Python function model format used by MLflow.

## Sources

- pre-deployment-validation-for-model-serving-databricks-on-aws.md

# Citations

1. [pre-deployment-validation-for-model-serving-databricks-on-aws.md](/references/pre-deployment-validation-for-model-serving-databricks-on-aws-77a7c1ae.md)
