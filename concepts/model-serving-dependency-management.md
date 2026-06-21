---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 496c6e21ff9ed77e84885c9ff20a938e2dd4356188347c77cbd6c3793990ba95
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-dependency-management
    - MSDM
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Model Serving Dependency Management
description: Ensuring all required libraries and custom artifacts (whl files) are properly declared as model dependencies to prevent container build and runtime failures.
tags:
  - model-serving
  - dependency-management
  - mlflow
timestamp: "2026-06-19T18:17:15.049Z"
---

# Model Serving Dependency Management

**Model Serving Dependency Management** refers to the practices for specifying, verifying, and troubleshooting the software dependencies (Python packages, system libraries, custom wheels, and artifacts) used by custom model containers in [Model Serving](/concepts/model-serving.md) on Databricks. Proper dependency management ensures consistent and reproducible model behavior when the container is built and deployed as an endpoint. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Specifying Dependencies

Databricks recommends defining all important libraries as model dependencies when logging the model. For [MLflow](/concepts/mlflow.md) models, dependencies are typically declared in the `conda.yaml` or `pip_requirements` arguments of the `log_model` function. If no version is specified for an MLflow library, Model Serving uses the latest available version. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

For custom GPU serving, Model Serving installs the recommended versions of `cuda` and `cuDNN` according to public PyTorch and TensorFlow documentation. These do not need to be declared explicitly unless a specific version is required. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Handling Custom Libraries

Custom libraries packaged as `.whl` files must be included as artifacts alongside the model. A common cause of runtime errors is a missing dependency: the error message `No module named <module-name>` indicates that a required package was not installed in the container. Pay special attention to custom wheels and ensure they are properly listed in the dependency specification. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Version Pinning

To ensure reproducibility, all important library versions should be pinned. The build logs can be inspected to confirm which package versions were installed. If a dependency mismatch is suspected, check the logs for the actual versions and redeploy with the correct pins. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Logging Models That Require `flash-attn`

Models that depend on the `flash-attn` library require special handling. Databricks recommends using a custom wheel version of `flash-attn` to avoid build errors such as `ModuleNotFoundError: No module named 'torch'`. All pip requirements should be passed as a list to `mlflow.transformers.log_model`, including the PyTorch, Torch, and Torchvision versions compatible with the CUDA version specified in the `flash-attn` wheel. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

A recommended configuration for CUDA 11.8 includes:

- PyTorch 2.0.1+cu118
- Torchvision 0.15.2+cu118
- `flash_attn` wheel: `flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl`

Example specification in Python:
```python
logged_model = mlflow.transformers.log_model(
    transformers_model=test_pipeline,
    artifact_path="artifact_path",
    pip_requirements=[
        "--extra-index-url https://download.pytorch.org/whl/cu118",
        "mlflow==2.13.1",
        "torch==2.0.1+cu118",
        "torchvision==0.15.2+cu118",
        "https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl",
        # ... other dependencies
    ],
    input_example=input_example,
    registered_model_name=registered_model_name,
)
```
^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Avoiding Large Artifacts

A container build may fail with `OSError: [Errno 28] No space left on device` if too many large artifacts are logged alongside the model unnecessarily. To resolve this, check the MLflow artifact store and remove extraneous files, then redeploy the slimmed-down package. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Troubleshooting Missing Dependencies

If a model fails to load with a `ModuleNotFoundError`:

1. Verify that the dependency is declared in the model's environment specification.
2. Ensure custom `.whl` files are included as artifacts.
3. Check the container build logs to confirm that the package was installed.
4. Use [pre-deployment validation](/concepts/pre-deployment-validation-for-model-serving.md) to catch common issues before creating the endpoint.

If the endpoint is already running and fails on requests, [Inference Tables](/concepts/inference-tables.md) can be used to log and query request/response data for root cause analysis. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- Container Build for Model Serving
- MLflow Model Logging
- [Pre-Deployment Validation](/concepts/pre-deployment-validation-for-model-serving.md)
- [Inference Tables](/concepts/inference-tables.md)
- Model Serving Endpoint Events

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
