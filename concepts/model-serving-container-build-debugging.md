---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 972d8c0a832cd3b95111c88f70eac50639c1c7f89a20d64e1930a34a74694b77
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-container-build-debugging
    - MSCBD
    - Model Serving Container Build
    - Model Container Build
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Model Serving Container Build Debugging
description: Process of diagnosing and resolving failures during container image creation for Databricks Model Serving endpoints, including event log inspection and common build errors.
tags:
  - model-serving
  - debugging
  - containers
timestamp: "2026-06-19T18:16:54.067Z"
---

# Model Serving Container Build Debugging

**Model Serving Container Build Debugging** covers the common issues and troubleshooting steps for container builds during Databricks [Model Serving](/concepts/model-serving.md) endpoint deployment. Container builds can fail due to environment constraints, missing dependencies, or resource limitations, and debugging them requires systematic log inspection and targeted fixes. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Overview

When a model serving endpoint fails to initialize or start, the root cause is often a container build failure. Databricks recommends starting with [pre-deployment validation](/concepts/pre-deployment-validation-for-model-serving.md) to catch common problems before they occur, then reviewing event logs to understand build progress and errors. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

The event logs, accessible via the **Events** tab in the workspace UI, contain information about container build progress. A successful build is indicated by a `SERVED_ENTITY_CONTAINER_EVENT` event type with the message `Container image creation finished successfully`. If no build event or message appears within an hour of creating the endpoint, contact Databricks support for assistance. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Debug After Container Build Success

Even when a container builds successfully, runtime issues can occur during model execution or endpoint operation. The following subsections address common post-build problems.

### Missing Dependency

An error like `An error occurred while loading the model. No module named <module-name>.` typically indicates that a required dependency is missing from the container. Verify that all dependencies are properly included in the build specification. Pay special attention to custom libraries and ensure that `.whl` files are included as artifacts. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Model Fails or Times Out During Requests

An error such as `Encountered an unexpected error while evaluating the model. Verify that the input is compatible with the model for inference.` when `predict()` is called suggests a code issue in the `predict()` function. Load the model from MLflow in a notebook and call it directly — this highlights issues in the function and reveals exactly where the failure occurs. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Root Cause Analysis of Failed Requests

For endpoint request failures, use [Inference Tables](/concepts/inference-tables.md) to perform root cause analysis. Inference tables automatically log all requests and responses to a [Unity Catalog](/concepts/unity-catalog.md) table for querying:

1. In the workspace, go to the **Serving** tab and select the endpoint.
2. In the **Inference tables** section, note the table's fully-qualified name (e.g., `my-catalog.my-schema.my-table`).
3. Query the table in a notebook:
   ```sql
   SELECT * FROM my-catalog.my-schema.my-table WHERE status_code != 200
   ```
4. Filter on columns like `request`, `response`, `request_time`, and `status_code` to narrow down problematic requests. If [agent tracing](/concepts/autogen-auto-tracing.md) is enabled for AI agents, the **Response** column contains detailed traces. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Workspace Exceeds Provisioned Concurrency

A `Workspace exceeded provisioned concurrency quota` error indicates the workspace has reached its limit for provisioned concurrency. Free up quota by deleting or stopping unused endpoints. For a permanent increase, contact the Databricks account team with the workspace ID, noting that increases depend on region availability. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Workspace Exceeds Parallel Requests Limit

A 429 error — `Exceeded max number of parallel requests. Please contact your Databricks representative to increase the limit` — indicates the workspace limit on maximum parallel requests has been reached. Databricks recommends moving to [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md), where this limit is removed. If that is not possible, either reduce the number of clients sending inference requests or contact your Databricks representative for a quota increase. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Too Many Concurrent Requests

A 429 error — `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity` — indicates the endpoint's current provisioned concurrency cannot handle the traffic volume. If autoscaling is enabled, the system automatically provisions additional concurrency up to the endpoint's configured limit. If autoscaling is not enabled, manually increase provisioned concurrency or enable autoscaling to handle traffic spikes. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Debug After Container Build Failure

The following sections detail issues that specifically cause container build failures.

### No Space Left on Device

An `OSError: [Errno 28] No space left on device` error is often caused by logging too many large artifacts alongside the model unnecessarily. Check in MLflow that extraneous artifacts are not included, then redeploy the slimmed-down package. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Build Failure Due to GPU Availability

Due to GPU supply restrictions, a build may fail with: `Build could not start due to an internal error - please contact your Databricks representative.`. Contact the Databricks account team for resolution; depending on region availability, the team can provision more GPU resources. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Installed Library Package Versions

Databricks recommends defining all important libraries as model dependencies to ensure consistent and reproducible behavior across environments. Review build logs to confirm the package versions that were installed correctly:

- If no MLflow version is specified, Model Serving uses the latest version.
- For custom GPU serving, Model Serving installs the recommended versions of `cuda` and `cuDNN` according to public PyTorch and TensorFlow documentation. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Logging Models That Require flash-attn

If logging a model that requires `flash-attn`, Databricks recommends using a custom wheel version of `flash-attn`. Without this, build errors such as `ModuleNotFoundError: No module named 'torch'` can result. Specify all pip requirements as a list and pass them to `mlflow.transformers.log_model`, including compatible PyTorch, torch, and torchvision versions for the target CUDA version. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

For example, for CUDA 11.8, use the following versions:
- PyTorch 2.0.1+cu118
- Torchvision 0.15.2+cu118
- flash-attn: `flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl`

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
        "torchvision==0.15.2+cu118",
        "transformers==4.41.2",
        "https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl"
    ],
    input_example=input_example,
    registered_model_name=registered_model_name
)
```

## Response Code Mapping

If model code returns `MlflowException` errors, the response code maps to a `4xx` response. Databricks considers these customer-caused errors since they can be resolved based on the error message. `5xx` error codes are reserved for errors where Databricks is at fault. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving Pre-Deployment Validation](/concepts/model-serving-pre-deployment-testing-workflow.md)
- Monitor Model Quality and Endpoint Health
- [Inference Tables](/concepts/inference-tables.md)
- [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md)
- Model Serving Limits and Regions
- MLflow Model Logging
- [GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
