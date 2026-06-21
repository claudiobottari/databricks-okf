---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0048493608b2bef73ca8c431eb3a103cc12e66381f7a93748a6ea398382bf1a
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dependency-management-for-databricks-model-serving
    - DMFDMS
    - Dependency Management for Models
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Dependency Management for Databricks Model Serving
description: Best practices for managing dependencies in model serving containers, including custom libraries, flash-attn, and version pinning.
tags:
  - model-serving
  - dependencies
  - python
  - packaging
  - databricks
timestamp: "2026-06-19T09:56:19.298Z"
---

# Dependency Management for Databricks Model Serving

**Dependency Management for Databricks Model Serving** refers to the practices and tooling required to define, specify, and resolve the software dependencies that a custom model needs to serve inferences reliably within the Databricks Model Serving environment. Proper dependency management ensures that the container image built for an endpoint contains the correct libraries, versions, and operating system components, preventing runtime failures.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Overview

When you deploy a model to a Model Serving endpoint, Databricks builds a container image that includes the model artifacts, the MLflow model server, and the dependencies declared during model logging. If dependencies are missing, incorrectly versioned, or incompatible, the container build may fail, or the model may error at inference time. Databricks recommends testing the model locally before deployment using [pre-deployment validation](/concepts/pre-deployment-validation-for-model-serving.md) to catch common issues early.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Specifying Dependencies

Dependencies are specified when you log a model using `mlflow.<flavor>.log_model()` via the `pip_requirements` parameter. This parameter accepts a list of pip-style requirement strings, including version constraints and references to custom wheels.

```python
logged_model = mlflow.transformers.log_model(
    transformers_model=test_pipeline,
    artifact_path="artifact_path",
    pip_requirements=[
        "--extra-index-url https://download.pytorch.org/whl/cu118",
        "mlflow==2.13.1",
        "torch==2.0.1+cu118",
        "transformers==4.41.2",
        "https://github.com/.../flash_attn-2.5.8+cu118torch2.0...whl"
    ],
    input_example=input_example,
    registered_model_name=registered_model_name
)
```

^[debugging-guide-for-model-serving-databricks-on-aws.md]

For models that require `flash-attn`, Databricks recommends using a custom wheel version of `flash-attn` rather than having the build system compile it from source. When doing so, you must also specify the PyTorch, torch, and torchvision versions that are compatible with the CUDA version used in the wheel.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Build Process and Validation

After an endpoint is created, the build progress is visible in the **Events** tab of the workspace UI. A successful build is indicated by an event of type `SERVED_ENTITY_CONTAINER_EVENT` with the message `Container image creation finished successfully`. If no build event appears after one hour, contact Databricks support.^[debugging-guide-for-model-serving-databricks-on-aws.md]

You can also confirm the installed package versions in the build logs. If no version is specified for MLflow, Model Serving uses the latest available version. For custom GPU serving, the recommended versions of `cuda` and `cuDNN` are installed according to public PyTorch and TensorFlow documentation.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Common Dependency Issues and Solutions

### Missing Module Error

If you receive an error like `An error occurred while loading the model. No module named <module-name>.`, a dependency is missing from the container. Verify that all required libraries are listed in `pip_requirements`. Pay special attention to custom libraries and ensure that `.whl` files are included as artifacts.^[debugging-guide-for-model-serving-databricks-on-aws.md]

### `OSError: [Errno 28] No space left on device`

This error occurs when too many large artifacts are logged alongside the model. Check that extraneous files are not included in the [MLflow Run](/concepts/mlflow-run.md), then redeploy the slimmed-down package.^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Build Failure Due to GPU Availability

A GPU build may fail with `Build could not start due to an internal error - please contact your Databricks representative.` This indicates a lack of GPU resources. Contact your account team to request provisioning.^[debugging-guide-for-model-serving-databricks-on-aws.md]

### `flash-attn` Build Errors

If `flash-attn` is compiled from source during the build, errors such as `ModuleNotFoundError: No module named 'torch'` can occur. This happens because the compilation step may precede the installation of PyTorch. Using a pre-built wheel version of `flash-attn` avoids this issue.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Best Practices

- **Define all important libraries** as model dependencies to ensure reproducible behavior across environments.^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Use version-pinned requirements** to avoid unexpected upgrades that may break inference.^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Include custom wheels as artifacts** in the [MLflow Run](/concepts/mlflow-run.md), rather than relying on external URLs that may become unavailable.
- **Test dependencies locally** by loading the model from MLflow in a notebook and calling it before deploying.^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Minimize artifact size** by logging only the essential model files to avoid disk space issues during build.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- MLflow Model Logging
- Container Builds for Model Serving
- [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md)
- Model Serving Limits and Regions

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
