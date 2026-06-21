---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7afe5d37bed17b07f53e545f7c75e05cd22caeb1ac689a7264cbc575868bed20
  pageDirectory: concepts
  sources:
    - pre-deployment-validation-for-model-serving-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  citations:
    - file: pre-deployment-validation-for-model-serving-databricks-on-aws.md
title: validate_serving_input
description: MLflow API to validate that model input conforms to the JSON format expected by Databricks Model Serving endpoints before deployment.
tags:
  - MLflow
  - model-serving
  - validation
  - input-validation
timestamp: "2026-06-19T19:56:43.498Z"
---

# validate_serving_input

`validate_serving_input` is an MLflow API that allows you to test whether your model input works correctly on a model serving endpoint *before* deployment. It simulates the serving environment by passing a JSON payload to the model and validating that the inference succeeds without errors. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Overview

Model serving endpoints expect a specific JSON input format. Using `validate_serving_input` helps catch formatting issues, data type mismatches, or model errors before you go through the endpoint deployment process. The function is part of the `mlflow.models` module and is designed for pre-deployment validation of MLflow models. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Usage

The function requires two arguments:

- `model_uri` – the URI of the logged model (e.g., a `runs:/` URI or a Unity Catalog model URI).
- `serving_payload` – a string containing a valid JSON payload that matches the input schema expected by the model.

Example (auto-generated code from a run’s artifacts tab):

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

## Related Function: `convert_input_example_to_serving_input`

For models that were logged with an input example, you can use `convert_input_example_to_serving_input` to automatically generate a valid JSON serving payload from that example, and then pass it to `validate_serving_input`. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

```python
from mlflow.models import validate_serving_input
from mlflow.models import convert_input_example_to_serving_input

model_uri = 'runs:/<run_id>/<artifact_path>'
# INPUT_EXAMPLE is a data instance suitable for pyfunc prediction
serving_payload = convert_input_example_to_serving_input(INPUT_EXAMPLE)
validate_serving_input(model_uri, serving_payload)
```

^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Benefits and Workflow

- **Catch issues early**: Validation runs locally (or in a notebook) without provisioning a serving endpoint, saving time and cost.
- **Environment simulation**: The validation runs using the model’s environment (e.g., conda or pip dependencies), ensuring compatibility.
- **Integration with CI/CD**: Can be included in automated pipelines to validate models before deployment.

Databricks recommends using `validate_serving_input` as part of a broader pre-deployment validation strategy that also includes testing offline predictions with `mlflow.models.predict` and verifying model dependencies. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow Model Serving – Deploying models to production endpoints.
- [mlflow.models.predict](/concepts/mlflowmodelspredict-api.md) – API for testing predictions with a virtual environment.
- [Model dependencies](/concepts/mlflow-model-dependency-logging.md) – Managing Python packages for a model.
- convert_input_example_to_serving_input – Helper to convert a model’s input example into a serving payload.
- [Pre-deployment validation](/concepts/pre-deployment-validation-for-model-serving.md) – The broader process of verifying model readiness.

## Sources

- pre-deployment-validation-for-model-serving-databricks-on-aws.md

# Citations

1. [pre-deployment-validation-for-model-serving-databricks-on-aws.md](/references/pre-deployment-validation-for-model-serving-databricks-on-aws-77a7c1ae.md)
