---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6ea3edad7add0d51081bcd1ce7c35ea2f5c5c533e7d4d45c2db0c77676119c5
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - container-build-debugging-for-model-serving
    - CBDFMS
    - Container Build for Model Serving
    - Container Builds for Model Serving
    - Debug After Container Build Failure
    - Debug after container build failure
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Container Build Debugging for Model Serving
description: Debugging container build failures and successes using event logs, including interpreting SERVED_ENTITY_CONTAINER_EVENT types and resolving build errors like OSError and GPU unavailability.
tags:
  - model-serving
  - debugging
  - containers
timestamp: "2026-06-19T14:57:42.574Z"
---

```markdown
---
title: Container Build Debugging for Model Serving
summary: Techniques and tools for debugging container builds in Databricks Model Serving, including event logs, build status tracking, and common build failures.
sources:
  - debugging-guide-for-model-serving-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:56:08.802Z"
updatedAt: "2026-06-19T09:56:08.802Z"
tags:
  - model-serving
  - debugging
  - containers
  - databricks
aliases:
  - container-build-debugging-for-model-serving
  - CBDFMS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Container Build Debugging for Model Serving

**Container Build Debugging for Model Serving** refers to the systematic process of diagnosing and resolving issues that occur during the container image creation phase when deploying a model to a [[Model Serving]] endpoint on Databricks. Container build failures can prevent an endpoint from initializing or starting, requiring targeted debugging steps. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Overview

When a model serving endpoint is created or updated, Databricks builds a container image that packages the model code, dependencies, and runtime environment. The build process generates event logs that contain information about its progress. Successful builds are indicated by a `SERVED_ENTITY_CONTAINER_EVENT` event type with the message `Container image creation finished successfully`. If no build event or message appears within an hour of creating the endpoint, contact Databricks support for assistance. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Reviewing Build Logs

Databricks recommends reviewing logs for debugging container build issues. The event logs can be accessed through the **Events** tab in the workspace UI. These logs provide visibility into the build process and can help identify the root cause of failures. See Monitor model quality and endpoint health for detailed information about viewing and interpreting logs. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Common Build Failures

### `OSError: [Errno 28] No space left on device`

This error occurs when too many large artifacts are logged alongside the model unnecessarily. To resolve this, check in [[MLflow]] that extraneous artifacts are not logged with the model, then redeploy the slimmed-down package. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Build Failure Due to Lack of GPU Availability

GPU builds may fail with the error: `Build could not start due to an internal error - please contact your Databricks representative.` This is due to restrictions in GPU supply and availability. Contact your Databricks account team to resolve the issue; depending on region availability, they can provision more GPU resources. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Installed Library Package Versions

Databricks recommends that you define all important libraries as model dependencies to ensure consistent and reproducible model behavior across environments. The build logs confirm which package versions were installed correctly. Key behaviors include:

- If no MLflow version is specified, Model Serving uses the latest version.
- For custom GPU serving, Model Serving installs the recommended versions of `cuda` and `cuDNN` according to public PyTorch and TensorFlow documentation. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Models That Require `flash-attn`

If logging a model that requires `flash-attn`, Databricks recommends using a custom wheel version of `flash-attn`. Without this, build errors such as `ModuleNotFoundError: No module named 'torch'` can occur. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

To use a custom wheel version of `flash-attn`, specify all pip requirements as a list and pass it as a parameter into the `mlflow.transformers.log_model` function. You must also specify the PyTorch, Torch, and TorchVision versions that are compatible with the CUDA version specified in your `flash-attn` wheel. For example, for CUDA 11.8, the recommended configuration includes:

- PyTorch from `https://download.pytorch.org/whl/cu118`
- Torch 2.0.1+cu118
- Torchvision 0.15.2+cu118
- Flash-Attn wheel from `https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl` ^[debugging-guide-for-model-serving-databricks-on-aws.md]

```python
logged_model = mlflow.transformers.log_model(
    transformers_model=test_pipeline,
    artifact_path="artifact_path",
    pip_requirements=[
        "--extra-index-url https://download.pytorch.org/whl/cu118",
        "mlflow==2.13.1",
        "setuptools<70.0.0",
        "torch==2.0.1+cu118",
        "accelerate==0.31.0",
        "astunparse==1.6.3",
        "bcrypt==3.2.0",
        "boto3==1.34.39",
        "configparser==5.2.0",
        "defusedxml==0.7.1",
        "dill==0.3.6",
        "google-cloud-storage==2.10.0",
        "ipython==8.15.0",
        "lz4==4.3.2",
        "nvidia-ml-py==12.555.43",
        "optree==0.12.1",
        "pandas==1.5.3",
        "pyopenssl==23.2.0",
        "pytesseract==0.3.10",
        "scikit-learn==1.3.0",
        "sentencepiece==0.1.99",
        "torchvision==0.15.2+cu118",
        "transformers==4.41.2",
        "https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl",
    ],
    input_example=input_example,
    registered_model_name=registered_model_name,
)
```

## Debugging After Container Build Succeeds

Even if the container builds successfully, issues may occur when running the model or during endpoint operation. Common post-build problems include:

- **Missing dependency**: Error like `An error occurred while loading the model. No module named <module-name>.` indicates a missing dependency. Verify all dependencies are properly specified and that custom library `.whl` files are included as artifacts. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Model fails or times out**: Error like `Encountered an unexpected error while evaluating the model.` when `predict()` is called suggests a code issue. Load the model from MLflow in a notebook and call it directly to isolate the failure within the `predict()` method. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Root cause analysis of failed requests**: Use inference tables (if enabled) to log all request and response data. Query the inference table (e.g., `my-catalog.my-schema.my-table`) and filter on `status_code` to identify failed requests. For AI agents, check the `Response` column for detailed traces. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Workspace exceeds provisioned concurrency**: Error message: `Workspace exceeded provisioned concurrency quota`. Free up quota by deleting or stopping unused endpoints, or contact your Databricks account team for a quota increase. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Workspace exceeds parallel requests limit**: `429` error: `Exceeded max number of parallel requests`. Switch to [[Route optimized endpoints]] (which remove this limit), reduce client count, or request a quota increase. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Too many concurrent requests**: `429` error: `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity.` Enable autoscaling or manually increase provisioned concurrency. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

Note: If model code returns `MlflowException` errors, the response code maps to a `4xx` response (customer-caused). `5xx` error codes indicate Databricks-caused issues. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Best Practices

- Validate before deployment using [[Pre-deployment Validation for Model Serving|pre-deployment validation]] to catch common problems early. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- Define all important libraries as model dependencies for consistent behavior. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- For `flash-attn` models, use custom wheel versions with compatible PyTorch and CUDA versions to avoid build errors. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- Remove extraneous artifacts from MLflow model logs to prevent "No space left on device" errors. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [[Model Serving]]
- MLflow Model Logging
- [[Model Serving Pre-deployment Testing Workflow|Model Serving Pre-Deployment Validation]]
- Monitor Model Quality and Endpoint Health
- GPU Scheduling
- [[Databricks Runtime for Machine Learning]]

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md
```

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
