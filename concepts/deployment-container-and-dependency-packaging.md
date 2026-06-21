---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d710cf38f7cfcf0e1f2a67d8c9eaee91d3f43e997dd5577adb42a20fbeec570
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deployment-container-and-dependency-packaging
    - dependency packaging and Deployment container
    - DCADP
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Deployment container and dependency packaging
description: Model Serving builds a production-grade container from the MLflow model log; native flavor models capture dependencies automatically while pyfunc models require explicit specification via pip_requirements, conda_env, extra_pip_requirements, or code_path parameters.
tags:
  - deployment
  - dependencies
  - mlflow
  - containerization
timestamp: "2026-06-19T18:03:43.539Z"
---

# Deployment Container and Dependency Packaging

**Deployment Container and Dependency Packaging** refers to the process of building and deploying a production-grade container for Model Serving endpoints that includes the model, its dependencies, and any custom code required for inference. When a model is deployed, the container is automatically built and deployed as the serving endpoint. ^[custom-models-overview-databricks-on-aws.md]

## Overview

During deployment, Model Serving constructs a container that includes libraries automatically captured from the MLflow model or explicitly specified by the user. The base image may include some system-level dependencies, but application-level dependencies must be explicitly included in the MLflow model. ^[custom-models-overview-databricks-on-aws.md] If required dependencies are missing, deployment errors may occur. Databricks recommends testing the model locally when troubleshooting deployment issues ^[custom-models-overview-databricks-on-aws.md] ^[custom-models-overview-databricks-on-aws.md] (second citation covers testing recommendation separately.)

For information about validating and updating dependencies before deployment, see [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md) ^[custom-models-overview-databricks-on-aws.md] ^[custom-models-overview-databricks-on-aws.md] (the source references this page.)

## Package and Code Dependencies

### For MLflow Native Flavor Models

When using MLflow's built-in flavors, the necessary package dependencies are automatically captured during the logging process. Users do not need to manually specify standard dependencies for flavors like scikit-learn, PyTorch, or Transformers. ^[custom-models-overview-databricks-on-aws.md]

### For Custom pyfunc Models

Custom MLflow PyFunc models require dependencies to be explicitly added. There are several methods for including package dependencies: ^[custom-models-overview-databricks-on-aws.md]

- **`pip_requirements` parameter**: Specify a list of required packages directly in the `log_model()` call.

```python
mlflow.sklearn.log_model(model, "sklearn-model", pip_requirements = ["scikit-learn", "numpy"])
```

^[custom-models-overview-databricks-on-aws.md]

- **`conda_env` parameter**: Define a conda environment dictionary specifying channels, Python version, and dependencies.

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

^[custom-models-overview-databricks-on-aws.md]

- **`extra_pip_requirements` parameter**: Include additional requirements beyond those automatically captured by MLflow.

```python
mlflow.sklearn.log_model(model, "sklearn-model", extra_pip_requirements = ["sklearn_req"])
```

^[custom-models-overview-databricks-on-aws.md]

### Code Dependencies

Custom or private libraries can be added to the deployment. Code dependencies (such as helper functions) can be specified using the `code_path` parameter ^[custom-models-overview-databricks-on-aws.md]:

```python
mlflow.sklearn.log_model(model, "sklearn-model", code_path=["path/to/helper_functions.py"])
```

^[custom-models-overview-databricks-on-aws.md]

For more information about using custom or private libraries, see [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md). ^[custom-models-overview-databricks-on-aws.md]

## Container Build Considerations

- **GPU workloads**: Container image creation for GPU serving takes longer than CPU serving due to model size and increased installation requirements. ^[custom-models-overview-databricks-on-aws.md]
- **Large models**: Deployment might timeout if container build and model deployment exceed 60 minutes. The build might also fail with "No space left on device" error due to storage limitations. For large language models, use [Foundation Model APIs](/concepts/foundation-model-apis.md) instead. ^[custom-models-overview-databricks-on-aws.md]

## Endpoint Creation and Update Expectations

- **Deployment time**: Deploying a newly registered model version typically takes approximately 10 minutes, but may take longer depending on model complexity, size, and dependencies. ^[custom-models-overview-databricks-on-aws.md]
- **Zero-downtime updates**: Databricks performs zero-downtime updates by keeping the existing endpoint configuration active until the new one is ready. During updates, you are billed for both old and new configurations. ^[custom-models-overview-databricks-on-aws.md]
- **System maintenance**: Databricks performs occasional zero-downtime system updates and maintenance that reload models. Customized models must be robust enough to reload at any time. If a model fails to reload, the update is marked as failed and the existing configuration continues serving. ^[custom-models-overview-databricks-on-aws.md]

## Best Practices

- Log the model or code in MLflow format using either native MLflow built-in flavors or pyfunc. ^[custom-models-overview-databricks-on-aws.md]
- Add a signature and input example to the MLflow model, as signatures are necessary for logging models to Unity Catalog ^[custom-models-overview-databricks-on-aws.md].
- For GPU deployments, ensure code is set up to run predictions on the GPU using framework-specific methods. MLflow does this automatically for PyTorch and Transformers flavors. ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- [Custom Models on Databricks](/concepts/custom-models-on-databricks.md)
- MLflow PyFunc
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [GPU Workload Limitations with Model Serving](/concepts/gpu-workload-limitations-in-model-serving.md)
- [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md)

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
