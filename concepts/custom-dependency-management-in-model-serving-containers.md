---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cdd357dac9b309ad904836082ca0f11dfe40f9d79e054b135e0f22ef33ad16db
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-dependency-management-in-model-serving-containers
    - CDMIMSC
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Custom Dependency Management in Model Serving Containers
description: Ensuring correct specification of model dependencies including custom .whl artifacts, GPU libraries (CUDA, cuDNN), and flash-attn wheel versions to avoid build and runtime errors like ModuleNotFoundError.
tags:
  - model-serving
  - dependencies
  - mlflow
timestamp: "2026-06-19T14:56:33.154Z"
---

# Custom Dependency Management in Model Serving Containers

**Custom Dependency Management in Model Serving Containers** refers to the practices and techniques for specifying, packaging, and troubleshooting software dependencies when building custom containers for [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints. Proper dependency management ensures that models can be loaded and served reliably in production environments.

## Overview

When deploying models using custom containers in Databricks Model Serving, all dependencies required by the model must be included in the container build. Missing or incompatible dependencies can cause build failures or runtime errors when the endpoint attempts to serve requests. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Specifying Dependencies

### Using `pip_requirements` in MLflow

When logging models with MLflow, you should define all important libraries as model dependencies to ensure consistent and reproducible model behavior across environments. The `pip_requirements` parameter in functions like `mlflow.transformers.log_model` allows you to specify dependencies as a list of pip requirements. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

For example, to log a model with specific dependencies:

```python
logged_model = mlflow.transformers.log_model(
    transformers_model=test_pipeline,
    artifact_path="artifact_path",
    pip_requirements=[
        "--extra-index-url https://download.pytorch.org/whl/cu118",
        "mlflow==2.13.1",
        "torch==2.0.1+cu118",
        "transformers==4.41.2",
    ],
    input_example=input_example,
    registered_model_name=registered_model_name
)
```

^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Custom Library Dependencies

Pay special attention to custom libraries and ensure that `.whl` files are included as artifacts alongside the model. Dependencies from private repositories or custom builds must be explicitly included in the deployment package. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Managing `flash-attn` Dependencies

Models that require `flash-attn` need special handling. Databricks recommends using a custom wheel version of `flash-attn` rather than relying on pip to build it from source. Otherwise, build errors such as `ModuleNotFoundError: No module named 'torch'` can result. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

When specifying `flash-attn` as a dependency:

1. Use a pre-built wheel compatible with your CUDA version
2. Specify PyTorch and torchvision versions compatible with the CUDA version in your `flash-attn` wheel
3. Include all pip requirements as a list passed to `mlflow.transformers.log_model`

For CUDA 11.8, Databricks recommends:
- PyTorch from `https://download.pytorch.org/whl/cu118`
- Torch 2.0.1+cu118
- Torchvision 0.15.2+cu118
- Flash-Attn wheel: `flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl`

^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Version Management

### MLflow Versions

For MLflow versions, if you do not have a version specified, Model Serving uses the latest version. To ensure reproducibility, always specify the exact MLflow version your model requires. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### GPU Serving Dependencies

For custom GPU serving, Model Serving installs the recommended versions of `cuda` and `cuDNN` according to public PyTorch and TensorFlow documentation. If your model requires specific CUDA or cuDNN versions, ensure these are compatible with the versions installed by the serving infrastructure. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Troubleshooting Dependency Issues

### Missing Dependency Errors

If you encounter an error like `An error occurred while loading the model. No module named <module-name>.`, this indicates a dependency is missing from the container. Verify that you properly denoted all dependencies in the build configuration, with special attention to custom libraries. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Container Build Failures

#### Insufficient Disk Space

The error `OSError: [Errno 28] No space left on device` can result from too many large artifacts being logged alongside the model unnecessarily. Check in MLflow that extraneous artifacts are not logged alongside the model and try to redeploy a slimmed-down package. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

#### `flash-attn` Build Errors

When logging a model that requires `flash-attn`, build errors such as `ModuleNotFoundError: No module named 'torch'` can occur if `flash-attn` is not specified as a custom wheel. Using a pre-built wheel resolves this issue. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Runtime Errors

If model code returns `MlflowException` errors, the response code is mapped to a `4xx` response. Databricks considers these model code errors to be customer-caused errors, since they can be resolved based on the resulting error message. `5xx` error codes are reserved for errors where Databricks is at fault. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Best Practices

1. **Define all important libraries as model dependencies** to ensure consistent and reproducible model behavior across environments. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
2. **Use pre-built wheels** for complex dependencies like `flash-attn` rather than relying on pip to build from source. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
3. **Specify exact versions** for critical dependencies, including MLflow, PyTorch, and transformers. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
4. **Minimize artifact size** by logging only necessary files alongside the model to avoid disk space issues during build. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- Model Serving Container Build — The process of building custom containers for serving endpoints
- Model Serving Debugging — General debugging strategies for model serving endpoints
- MLflow Model Logging — How to log models with MLflow, including dependency specification
- GPU Serving on Databricks — Considerations for GPU-accelerated model serving
- Custom Container Specifications — Requirements for custom containers in Databricks Model Serving

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
