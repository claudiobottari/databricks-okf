---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78735790db31144f658a0988d2b3aecbc59219a086b16243d030f97828dc2c29
  pageDirectory: concepts
  sources:
    - pre-deployment-validation-for-model-serving-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - local-model-serving-simulation
    - LMSS
    - Local Model Serving
  citations:
    - file: pre-deployment-validation-for-model-serving-databricks-on-aws.md
title: Local Model Serving Simulation
description: Manual approach to test model serving behavior by loading the model on an all-purpose cluster or local PC with a matching environment before endpoint deployment.
tags:
  - Databricks
  - model-serving
  - debugging
timestamp: "2026-06-19T19:57:06.647Z"
---

# Local Model Serving Simulation

**Local Model Serving Simulation** refers to the practice of testing and validating a machine learning model's behavior in a local environment before deploying it to a production [Model Serving](/concepts/model-serving.md) endpoint. This pre-deployment validation process helps identify potential issues with model dependencies, input formatting, and serving behavior early in the development cycle. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Overview

Before deploying a model to a serving endpoint, Databricks recommends testing offline predictions using [MLflow](/concepts/mlflow.md)'s validation APIs. These tools simulate the deployment environment and allow you to verify that modified dependencies work correctly with the model, reducing the risk of deployment failures. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Validation Methods

MLflow provides two main approaches for local model serving simulation:

### MLflow Python API

The `mlflow.models.predict()` function provides the primary method for testing predictions before deployment. It simulates the serving environment and allows testing with modified dependencies. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

Key parameters include:
- `model_uri`: The model URI to be deployed
- `input_data`: Input in the expected format for the model's `predict()` call
- `input_path`: File path containing input data
- `content_type`: Either `csv` or `json`
- `env_manager`: Environment manager for serving validation (default is `virtualenv`, recommended for serving)
- `install_mlflow`: Whether to install the current MLflow version in the virtual environment
- `pip_requirements_override`: List of dependency overrides for troubleshooting

### MLflow CLI

The MLflow command-line interface provides an alternative method for testing predictions and updating model dependencies. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Validating Serving Input

Model serving endpoints expect a specific JSON input format. The `validate_serving_input()` function in MLflow can validate that your model input works correctly on a serving endpoint before deployment. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

You can also use `convert_input_example_to_serving_input()` to generate valid JSON serving input from existing input examples.

## Updating Model Dependencies

If dependencies in a logged model need updates, you can modify them without re-logging the model using:

- `mlflow.models.model.update_model_requirements()` (Python API)
- `mlflow models update-pip-requirements` (CLI)

This allows updating `pip_requirements.txt` in-place with specified package versions. ^[pre-deployment-validation-for-model-serving-databricks-on-aws.md]

## Manual Testing

For additional validation, you can:

1. Load the model using MLflow in a notebook attached to an All-Purpose cluster (using Databricks Runtime, not Machine Learning Runtime)
2. Load the model locally on your PC using `mlflow.artifacts.download_artifacts()` and `mlflow.pyfunc.load_model()` for local debugging

## Related Concepts

- [Model Serving](/concepts/model-serving.md) - Production deployment of ML models
- [MLflow](/concepts/mlflow.md) - Machine learning lifecycle management
- [Pre-deployment Validation](/concepts/pre-deployment-validation-for-model-serving.md) - Comprehensive validation before deployment
- Model Dependencies - Package requirements for model serving

## Sources

- pre-deployment-validation-for-model-serving-databricks-on-aws.md

# Citations

1. [pre-deployment-validation-for-model-serving-databricks-on-aws.md](/references/pre-deployment-validation-for-model-serving-databricks-on-aws-77a7c1ae.md)
