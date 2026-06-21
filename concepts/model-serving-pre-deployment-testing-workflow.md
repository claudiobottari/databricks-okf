---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 54cea3148b6a03b85505b75f960a5c1b89bc62c2482af529b6d4b95df7d17f22
  pageDirectory: concepts
  sources:
    - pre-deployment-validation-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-serving-pre-deployment-testing-workflow
    - MSPTW
    - Model Serving Pre-Deployment Validation
  citations:
    - file: pre-deployment-validation-for-model-serving-databricks-on-aws.md
title: Model Serving Pre-deployment Testing Workflow
description: Databricks-recommended validation steps to catch model issues before endpoint deployment, including offline prediction testing, dependency checks, input validation, and local serving simulation.
tags:
  - Databricks
  - model-serving
  - workflow
  - validation
timestamp: "2026-06-19T19:56:58.858Z"
---

# Model Serving Pre-deployment Testing Workflow

The **Model Serving Pre-deployment Testing Workflow** is a set of validation steps that help catch issues with a model before initiating the endpoint deployment process. Databricks recommends going through these steps to ensure a better development experience when using model serving. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Test Predictions Before Deployment

Before deploying a model to a serving endpoint, test offline predictions using `mlflow.models.predict` with input examples. MLflow provides validation APIs that simulate the deployment environment and allow testing of modified dependencies. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

Two pre-deployment validation options are available: the MLflow Python API and the MLflow CLI. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

You can specify the following parameters when testing predictions:

- `model_uri` — The URI of the model deployed to model serving.
- One of the following input sources:
  - `input_data` — Data in the expected format for the `mlflow.pyfunc.PyFuncModel.predict()` call.
  - `input_path` — Path to a file containing input data to be loaded for the `predict` call.
- `content_type` — Format of the input data (`csv` or `json`).
- `output_path` — (Optional) File path to write predictions; if omitted, predictions print to `stdout`.
- `env_manager` — Environment manager for building the serving environment. The default is `virtualenv`, which is recommended for serving validation. The `local` option is available but potentially error prone and generally used only for rapid debugging.
- `install_mlflow` — Whether to install the current version of MLflow in the virtual environment. Defaults to `False`.
- `pip_requirements_override` — A list of string dependency overrides or additions for troubleshooting or debugging. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

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

## Update Model Dependencies

If issues arise with the dependencies specified in a logged model, you can update the requirements using the MLflow CLI or `mlflow.models.model.update_model_requirements()` in the MLflow Python API without logging another model. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

The following example updates the `pip_requirements.txt` of a logged model in-place. You can update existing definitions with specified package versions or add non-existent requirements to the file:

```python
from mlflow.models.model import update_model_requirements

update_model_requirements(
    model_uri=model_uri,
    operation="add",
    requirement_list=["pillow==10.2.0", "scipy==1.12.0"],
)
```

## Validate Model Input Before Deployment

Model serving endpoints expect a special format of JSON input. You can validate that model input works on a serving endpoint before deployment using `validate_serving_input` in MLflow. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

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

You can also test input examples against the logged model by using the `convert_input_example_to_serving_input` API to generate a valid JSON serving input: ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

```python
from mlflow.models import validate_serving_input
from mlflow.models import convert_input_example_to_serving_input

model_uri = 'runs:/<run_id>/<artifact_path>'

# Define INPUT_EXAMPLE with your own input example
serving_payload = convert_input_example_to_serving_input(INPUT_EXAMPLE)

validate_serving_input(model_uri, serving_payload)
```

## Manually Test Serving the Model

You can manually test the serving behavior of the model using the following approach:

1. Open a notebook and attach it to an All-Purpose cluster that uses a Databricks Runtime version (not Databricks Runtime for Machine Learning).
2. Load the model using MLflow and debug from there.

You can also load the model locally on your PC: ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

```python
import os
import mlflow

os.environ["MLFLOW_TRACKING_URI"] = "databricks://PROFILE"
ARTIFACT_URI = "model_uri"

if '.' in ARTIFACT_URI:
    mlflow.set_registry_uri('databricks-uc')

local_path = mlflow.artifacts.download_artifacts(ARTIFACT_URI)
print(local_path)

# Then create environment and load model:
# conda env create -f local_path/artifact_path/conda.yaml
# conda activate mlflow-env
# mlflow.pyfunc.load_model(local_path/artifact_path)
```

## Related Concepts

- MLflow Model Serving
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- MLflow Python API
- MLflow CLI
- Model Dependencies
- Serving Payload Format

## Sources

- pre-deployment-validation-for-model-serving-databricks-on-aws.md

# Citations

1. [pre-deployment-validation-for-model-serving-databricks-on-aws.md](/references/pre-deployment-validation-for-model-serving-databricks-on-aws-77a7c1ae.md)
