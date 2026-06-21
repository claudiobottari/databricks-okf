---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dcb935df3b4b053e7e800c7a6cb07cafe31b03288b1f564c5c4e3433f5b21f66
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-debugging-workflow
    - MSEDW
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Model Serving Endpoint Debugging Workflow
description: Systematic approach to debugging Databricks Model Serving endpoints, starting with pre-deployment validation, then container build logs, followed by build-success or build-failure debugging paths.
tags:
  - model-serving
  - debugging
  - workflow
timestamp: "2026-06-18T11:44:04.107Z"
---

# Model Serving Endpoint Debugging Workflow

**Model Serving Endpoint Debugging Workflow** is a systematic approach to identifying and resolving issues that arise when deploying and running models on [Model Serving](/concepts/model-serving.md) endpoints in Databricks. The workflow covers container build failures, runtime errors, dependency problems, and performance limitations. Databricks recommends starting with [pre-deployment validation](/concepts/pre-deployment-validation-for-model-serving.md) to catch common issues before they occur. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Validate Before Debugging

Before investing time in debugging, run the pre-deployment validation checks provided by Databricks. These checks verify that your model artifact, dependencies, and endpoint configuration are compatible with Model Serving, preventing many deployment-time errors. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Debug Your Container Build

The primary tool for debugging container builds is the event log, accessible via the **Events** tab in the workspace UI. A successful container build is indicated by a `SERVED_ENTITY_CONTAINER_EVENT` event type with the message `Container image creation finished successfully`. If no build event appears after an hour of creating the endpoint, contact Databricks support. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

Depending on whether the container build succeeds or fails, follow the appropriate debugging path below.

## Debug After Container Build Succeeds

Even when the container image is built successfully, issues may arise during model inference or endpoint operation. The following subsections cover common runtime problems.

> **Note on error codes**: If your model code raises `MlflowException`, the response is mapped to a `4xx` error code. Databricks considers these customer-caused errors. `5xx` error codes indicate Databricks-caused errors. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Missing Dependency

If you see `An error occurred while loading the model. No module named <module-name>.`, a required Python dependency is missing from the container. Verify that all dependencies are correctly specified in the model’s `conda.yaml` or `requirements.txt`. Pay special attention to custom libraries: ensure `.whl` files are included as artifacts in the MLflow Model. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Model Fails or Times Out When Requests Are Sent

An error like `Encountered an unexpected error while evaluating the model. Verify that the input is compatible with the model for inference.` usually indicates a bug in the `predict()` function. Databricks recommends loading the model from MLflow in a notebook and calling it directly to isolate the failure. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Root Cause Analysis of Failed Requests

For in-depth root cause analysis, enable [Inference Tables](/concepts/inference-tables.md). Inference tables automatically log all requests and responses to a Unity Catalog table. To query the table:

1. In your workspace, go to **Serving** and select your endpoint.
2. In the **Inference tables** section, note the fully-qualified table name (e.g., `my-catalog.my-schema.my-table`).
3. Run a SQL query to inspect the data:

   ```sql
   SELECT * FROM my-catalog.my-schema.my-table
   WHERE status_code != 200;
   ```

4. Filter on columns such as `request`, `response`, `request_time`, and `status_code` to narrow down failing requests. If agent tracing is enabled, the **Response** column contains detailed traces for AI agents. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Workspace Exceeds Provisioned Concurrency

Receiving `Workspace exceeded provisioned concurrency quota` means you have reached the workspace-level limit for provisioned concurrency. Free up quota by Managing serving endpoints|deleting or stopping unused endpoints. For a permanent increase, contact your Databricks account team with your workspace ID. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Workspace Exceeds Parallel Requests Limit

A `429` error `Exceeded max number of parallel requests` indicates the maximum number of simultaneous requests allowed for the workspace has been hit. Databricks recommends moving to [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md), where this limit is removed. If migration is not possible, reduce the number of concurrent clients or contact your Databricks representative for a quota increase. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Too Many Concurrent Requests

If you receive `429 Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity.`, the endpoint’s current provisioned concurrency is insufficient for the traffic. If autoscaling is enabled, the system will automatically add capacity up to the endpoint’s configured maximum. Without autoscaling, manually increase the provisioned concurrency or enable autoscaling. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Debug After Container Build Failure

If the container build itself fails, review the build log for specific error messages. Common failures and their solutions are described below.

### `OSError: [Errno 28] No space left on device`

This error often results from logging too many large artifacts alongside the model. Check the [MLflow Run](/concepts/mlflow-run.md) and remove any unnecessary files, then redeploy the slimmed-down model artifact. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Build Failure Due to Lack of GPU Availability

GPU builds may fail with `Build could not start due to an internal error - please contact your Databricks representative.`. This is due to GPU resource constraints. Contact your Databricks account team to request GPU provisioning in your region. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Installed Library Package Versions

Define all important libraries as model dependencies to ensure reproducible behavior. In the build logs you can confirm which package versions were installed. For [MLflow](/concepts/mlflow.md) versions, if none is specified, Model Serving uses the latest. For custom GPU serving, Model Serving installs recommended versions of `cuda` and `cuDNN` per public PyTorch and TensorFlow documentation. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Logging Models That Require `flash-attn`

If your model depends on `flash-attn`, build errors like `ModuleNotFoundError: No module named 'torch'` can occur unless a custom wheel is used. Databricks recommends using a `flash-attn` wheel and specifying all pip requirements as a list passed to `mlflow.transformers.log_model`. The example below shows recommended versions for CUDA 11.8:

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
        "https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/"
        "flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl"
    ],
    input_example=input_example,
    registered_model_name=registered_model_name
)
```

^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
