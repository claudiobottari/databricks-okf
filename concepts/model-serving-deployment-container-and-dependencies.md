---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60efc428054f67c2c0bf29ae98a68c4363f15432d1ea25ef1d40a829b4e9a84b
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-deployment-container-and-dependencies
    - Dependencies and Model Serving Deployment Container
    - MSDCAD
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Model Serving Deployment Container and Dependencies
description: How a production-grade container is built during deployment, including how to specify package dependencies via pip_requirements, conda_env, and extra_pip_requirements, and code dependencies via code_path for custom pyfunc models.
tags:
  - deployment
  - dependencies
  - mlflow
  - containers
timestamp: "2026-06-19T14:40:02.334Z"
---

# Model Serving Deployment Container and Dependencies

When a [custom model](/concepts/custom-mlflow-pythonmodel.md) is deployed on [Databricks Model Serving](/concepts/databricks-model-serving.md), a production-grade container is built and deployed as the endpoint. This container includes libraries that are automatically captured or explicitly specified in the [MLflow](/concepts/mlflow.md) model that was logged prior to deployment. Understanding what the container contains and how to manage dependencies is essential for successful endpoint creation and operation. ^[custom-models-overview-databricks-on-aws.md]

## Container Contents

The deployment container is built from a base image that may include some system-level dependencies. However, application-level dependencies — such as Python packages — must be explicitly provided in the MLflow model. If not all required dependencies are included, you might encounter dependency errors during deployment. Databricks recommends testing the model locally before attempting deployment to catch such issues early. ^[custom-models-overview-databricks-on-aws.md]

## Package and Code Dependencies

Custom or private libraries can be added to a deployment. For detailed guidance, see [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md). ^[custom-models-overview-databricks-on-aws.md]

For MLflow native flavor models (e.g., `sklearn`, `pytorch`, `transformers`), the necessary package dependencies are automatically captured at log time. For custom `pyfunc` models, dependencies must be explicitly added. The recommended approach is to consult the MLflow Models documentation and the MLflow Python API reference for best practices. ^[custom-models-overview-databricks-on-aws.md]

### Specifying Dependencies

You can add package dependencies to a logged PyFunc model using any of the following MLflow parameters:

| Parameter | Description |
|-----------|-------------|
| `pip_requirements` | A list of pip requirements strings. |
| `conda_env` | A dictionary specifying a Conda environment, including channels and dependencies. |
| `extra_pip_requirements` | Additional requirements beyond those automatically captured by MLflow. |

^[custom-models-overview-databricks-on-aws.md]

Examples for each approach:

**Using `pip_requirements`:**
```python
mlflow.sklearn.log_model(model, "sklearn-model",
    pip_requirements=["scikit-learn", "numpy"])
```
^[custom-models-overview-databricks-on-aws.md]

**Using `conda_env`:**
```python
conda_env = {
    'channels': ['defaults'],
    'dependencies': [
        'python=3.7.0',
        'scikit-learn=0.21.3'
    ],
    'name': 'mlflow-env'
}
mlflow.sklearn.log_model(model, "sklearn-model", conda_env=conda_env)
```
^[custom-models-overview-databricks-on-aws.md]

**Using `extra_pip_requirements`:**
```python
mlflow.sklearn.log_model(model, "sklearn-model",
    extra_pip_requirements=["sklearn_req"])
```
^[custom-models-overview-databricks-on-aws.md]

### Code Dependencies

If your model depends on additional Python modules or helper files, you can specify them using the `code_path` parameter:

```python
mlflow.sklearn.log_model(model, "sklearn-model",
    code_path=["path/to/helper_functions.py"])
```
^[custom-models-overview-databricks-on-aws.md]

For guidance on validating and updating dependencies before deployment, see [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md). ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- Custom Models – Overview of deploying Python models on Databricks.
- MLflow Logging – How to log models with dependencies.
- [Model Serving Endpoint Creation](/concepts/model-serving-endpoint-creation-options.md) – The process of creating serving endpoints.
- Model Serving Debugging – Troubleshooting deployment issues.
- [Private Libraries for Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) – Adding custom or proprietary packages.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Alternative serving option for large language models.
- [External Models](/concepts/external-models.md) – Serving models hosted outside Databricks.

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
