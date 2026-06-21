---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05d056e2f47065f72d3e37f38b2d66b97683c5e69dec84c810b1a79ffe4d8ea7
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-validation-before-deployment
    - MVBD
    - Validate models before deployment
    - validate models before deployment
    - validating models before deployment
    - mlflow-model-validation-before-deployment
    - MMVBD
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Model Validation Before Deployment
description: Using mlflow.models.predict to validate custom pyfunc models before deploying them to Model Serving endpoints
tags:
  - mlflow
  - deployment
  - testing
timestamp: "2026-06-18T12:00:30.216Z"
---

# Model Validation Before Deployment

**Model validation before deployment** is the process of verifying that a machine learning model is capable of being served correctly in a production environment before it is deployed to an endpoint. This validation step helps identify issues with model packaging, dependencies, and runtime behavior before they affect production workloads. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Overview

When deploying custom Python code using MLflow's Python function (`pyfunc`) format, it is beneficial to verify that the model can be served successfully prior to deployment to a [Model Serving](/concepts/model-serving.md) endpoint. Validation helps catch problems that might only surface during inference, such as missing dependencies, incorrect model loading, or runtime errors in preprocessing or postprocessing logic. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Validation with `mlflow.models.predict`

MLflow provides the `mlflow.models.predict` API as a tool for validating models before deployment. This function allows you to test that a logged model can make predictions in a simulated serving environment without deploying to a production endpoint. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

The typical workflow involves:

1. **Logging the model** using `mlflow.pyfunc.log_model()` with all required dependencies specified.
2. **Loading the model** from the logged artifact location.
3. **Calling `mlflow.models.predict`** with test input data to verify the model produces expected outputs without errors.

## Key Considerations for Validation

### Dependency Verification

When validating a custom `pyfunc` model, ensure that all required dependencies are correctly specified. On Databricks Runtime ML runtimes, `mlflow-skinny` is included by default rather than the full `mlflow` package. If `pip_requirements` is not specified when logging a `pyfunc` model, MLflow captures `mlflow-skinny` in the model's `conda.yaml`. [Model Serving](/concepts/model-serving.md) requires the full `mlflow` package and cannot build the container image otherwise. Always specify `mlflow==<version>` in `pip_requirements` when logging models on Databricks Runtime ML runtimes. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Testing the `load_context` and `predict` Functions

Custom `pyfunc` models define two required functions:

- **`load_context`**: Code that runs once when the model is loaded, such as loading model weights or tokenizers. Validation ensures this function executes without errors.
- **`predict`**: Code that runs for every inference request, including preprocessing, model inference, and postprocessing. Validation confirms all logic paths work correctly with representative inputs.

### Isolating Validation

Run validation in an environment that mirrors the production serving environment as closely as possible, including matching Python versions, library versions, and system dependencies. This reduces the risk of environment-specific issues surfacing only after deployment.

## Related Concepts

- MLflow pyfunc — The Python function format for packaging custom code as MLflow models
- [Model Serving](/concepts/model-serving.md) — The production endpoint for serving validated models
- Custom Python Models — Models built with arbitrary Python code using the `pyfunc` interface
- Model Logging — The process of recording model artifacts and metadata with MLflow
- [Dependency Management for Models](/concepts/dependency-management-for-databricks-model-serving.md) — Ensuring correct dependencies for model serving compatibility

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
