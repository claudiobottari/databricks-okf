---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0703364a8aa82249967836922c6ea665b08f9e9bd7aca66392635be6b21b604d
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deployment-container-and-dependencies
    - Dependencies and Deployment Container
    - DCAD
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Deployment Container and Dependencies
description: Production-grade container built during deployment includes MLflow-captured or specified libraries; dependencies can be added via pip_requirements, conda_env, extra_pip_requirements, and code_path.
tags:
  - deployment
  - dependencies
  - model-serving
timestamp: "2026-06-18T11:26:33.447Z"
---

# Deployment Container and Dependencies

When deploying a custom model to Databricks Model Serving, a production-grade container is built and deployed as the serving endpoint. This container includes libraries that are automatically captured from the MLflow model or explicitly specified by the user. The base image provides some system-level dependencies, but application-level dependencies must be fully declared in the MLflow model. ^[custom-models-overview-databricks-on-aws.md]

If not all required dependencies are included in the model, deployment may produce dependency errors. Databricks recommends testing the model locally before deployment to catch missing packages. ^[custom-models-overview-databricks-on-aws.md]

## Specifying Package Dependencies

For models logged with MLflow’s built-in flavors (such as scikit-learn, PyTorch, or Transformers), the necessary package dependencies are captured automatically. For custom PyFunc models, dependencies must be explicitly added. ^[custom-models-overview-databricks-on-aws.md]

Dependencies can be specified using the `pip_requirements` parameter:

```python
mlflow.sklearn.log_model(model, "sklearn-model", pip_requirements = ["scikit-learn", "numpy"])
```

Or with a `conda_env` dictionary:

```python
conda_env = {
    'channels': ['defaults'],
    'dependencies': [
        'python=3.7.0',
        'scikit-learn=0.21.3'
    ],
    'name': 'mlflow-env'
}
mlflow.sklearn.log_model(model, "sklearn-model", conda_env = conda_env)
```

To include additional requirements beyond those automatically captured, use `extra_pip_requirements`:

```python
mlflow.sklearn.log_model(model, "sklearn-model", extra_pip_requirements = ["sklearn_req"])
```

^[custom-models-overview-databricks-on-aws.md]

## Code Dependencies

Code dependencies such as helper functions can be included using the `code_path` parameter when logging the model:

```python
mlflow.sklearn.log_model(model, "sklearn-model", code_path=["path/to/helper_functions.py"])
```

^[custom-models-overview-databricks-on-aws.md]

Custom or private libraries that are not available on public repositories can also be added to the deployment. See [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) for details. ^[custom-models-overview-databricks-on-aws.md]

## Testing and Validation

Databricks recommends testing the model locally before deployment to verify that all dependencies resolve correctly. For guidance on validating and updating dependencies prior to deployment, see [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md). ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- MLflow Models
- PyFunc
- [Model Serving](/concepts/model-serving.md)
- Custom Models Overview
- [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md)
- [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md)

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
