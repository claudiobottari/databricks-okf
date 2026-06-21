---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b67547fdab48dc15c2f034d1526398a2add446be7aef25e564f27a3d1b12fee
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-endpoint-deployment-container-and-dependencies
    - Dependencies and Serving Endpoint Deployment Container
    - SEDCAD
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Serving Endpoint Deployment Container and Dependencies
description: Production-grade container built during deployment that includes libraries captured in the MLflow model; application-level dependencies must be explicitly specified via pip_requirements, conda_env, or extra_pip_requirements.
tags:
  - deployment
  - dependencies
  - databricks
timestamp: "2026-06-18T14:57:33.341Z"
---

# Serving Endpoint Deployment Container and Dependencies

When you deploy a custom model on Databricks Model Serving, a production‑grade container is built and deployed as the serving endpoint. This container includes the libraries that were automatically captured or explicitly specified in the MLflow model’s environment definition. The base image may contain some system‑level dependencies, but application‑level dependencies **must** be explicitly provided in the MLflow model; otherwise, deployment errors can occur. Databricks recommends testing the model locally if you encounter dependency issues during deployment. ^[custom-models-overview-databricks-on-aws.md]

## Package and Code Dependencies

The way dependencies are captured depends on how the model was logged:

- **MLflow native flavor models** (e.g., `sklearn`, `pytorch`, `transformers`): The necessary Python packages are automatically captured by MLflow. ^[custom-models-overview-databricks-on-aws.md]
- **Custom `pyfunc` models**: Dependencies must be added explicitly. You can specify them using one of the following parameters when calling `log_model()`: ^[custom-models-overview-databricks-on-aws.md]

| Parameter | Description |
|-----------|-------------|
| `pip_requirements` | List of pip‑installable packages. Example: `["scikit-learn", "numpy"]` |
| `conda_env` | Dictionary describing a Conda environment (channels, dependencies, Python version). |
| `extra_pip_requirements` | Additional packages beyond those automatically captured by MLflow. |

For example, to include explicit pip requirements: ^[custom-models-overview-databricks-on-aws.md]

```python
mlflow.sklearn.log_model(model, "sklearn-model",
                         pip_requirements = ["scikit-learn", "numpy"])
```

To define a full Conda environment: ^[custom-models-overview-databricks-on-aws.md]

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

To include packages beyond what is automatically captured, use `extra_pip_requirements`: ^[custom-models-overview-databricks-on-aws.md]

```python
mlflow.sklearn.log_model(model, "sklearn-model",
                         extra_pip_requirements = ["sklearn_req"])
```

### Code Dependencies

If your model depends on additional Python files, you can include them using the `code_path` parameter: ^[custom-models-overview-databricks-on-aws.md]

```python
mlflow.sklearn.log_model(model, "sklearn-model",
                         code_path=["path/to/helper_functions.py"])
```

### Custom or Private Libraries

Custom or private Python libraries can be added to the deployment. For detailed guidance, see the [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) documentation.

## Pre‑deployment Validation

Before deploying, you can validate that all dependencies are correctly specified using [Pre‑deployment validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md).

## Container Build and Endpoint Creation

During endpoint creation, the container image is built by packaging the model and its environment. This process typically takes about **10 minutes** but may take longer for large or complex models. For GPU workloads, container image creation takes additional time due to model size and the increased installation requirements of GPU‑compatible libraries. ^[custom-models-overview-databricks-on-aws.md]

### GPU Deployment Limitations

- Container build for GPU serving takes longer than for CPU serving.
- Very large models may cause the build to timeout after 60 minutes or fail with a "No space left on device" error due to storage limits. For large language models, Databricks recommends using [Foundation Model APIs](/concepts/foundation-model-apis.md) instead of custom model serving. ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- Custom Models Overview
- [MLflow Pyfunc](/concepts/custom-mlflow-pythonmodel.md)
- [Model Serving](/concepts/model-serving.md)
- Package custom artifacts for Model Serving
- Deploy Python code with Model Serving
- [Express deployments for model serving endpoints](/concepts/express-deployments-databricks.md)

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
