---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3a66518a1800787358aba4e423b813a4a3d0cb494ea528a1c1b5acef378c513
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-error-classification
    - MSEC
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Model Serving Error Classification
description: Classification of error codes in Databricks Model Serving, distinguishing between customer-caused errors (4xx) and platform errors (5xx).
tags:
  - model-serving
  - error-handling
  - debugging
  - databricks
timestamp: "2026-06-19T09:56:31.349Z"
---

# Model Serving Error Classification

**Model Serving Error Classification** categorizes the common errors that occur when deploying and running models on [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints. Understanding these error types helps operators diagnose failures quickly, determine whether the root cause is a model code issue, an infrastructure limitation, or a configuration problem.

## Overview

Errors during model serving can be grouped by the phase in which they occur: container build, runtime after a successful build, or concurrency and quota limits. Databricks recommends using the **Events** tab in the endpoint UI and [Inference Tables](/concepts/inference-tables.md) for Query-Based Root Cause Analysis to investigate failures.^[debugging-guide-for-model-serving-databricks-on-aws.md]

The source distinguishes between customer-caused errors (returning `4xx` HTTP status codes) and Databricks-caused errors (`5xx` codes). `MlflowException` from model code maps to a `4xx` response; `5xx` errors indicate Databricks infrastructure faults.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Pre‑deployment Validation

Before deploying, run the [pre-deployment validation](/concepts/pre-deployment-validation-for-model-serving.md) checklist to catch common problems early. This step is essential to reduce build and runtime failures.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Container Build Errors

### Build Failure – No Space Left on Device

`OSError: [Errno 28] No space left on device` – Caused by too many large artifacts logged alongside the model. Remove extraneous artifacts and redeploy.^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Build Failure – GPU Unavailability

`Build could not start due to an internal error - please contact your Databricks representative.` – Occurs when GPU resources are constrained. Contact your Databricks account team to provision more GPU capacity.^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Build Failure – Missing or Incompatible Dependencies

- **Missing modules**: `No module named <module-name>` – Indicates a dependency omitted from the model’s `requirements.txt` or `conda.yaml`. Ensure all custom libraries (`.whl` files) are included.^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **`flash-attn` errors** (`ModuleNotFoundError: No module named 'torch'`): When logging models that require `flash-attn`, use a custom wheel with explicit pip requirements that include compatible PyTorch, torchvision, and CUDA versions.^[debugging-guide-for-model-serving-databricks-on-aws.md]

Container build progress is shown via event logs. A successful build produces a `SERVED_ENTITY_CONTAINER_EVENT` with the message “Container image creation finished successfully.” If no build event appears after one hour, contact Databricks support.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Runtime Errors (After Successful Build)

### Missing Dependency at Load Time

`An error occurred while loading the model. No module named <module-name>.` – The container was built without a required Python package. Verify that all dependencies are declared in the model’s environment specification.^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Model Evaluation Failure or Timeout

`Encountered an unexpected error while evaluating the model. Verify that the input is compatible with the model for inference.` – Usually a bug in the `predict()` function. Reproduce by loading the model from [MLflow](/concepts/mlflow.md) in a notebook and calling it directly to isolate the error.^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Root Cause Analysis via Inference Tables

When an endpoint returns a non‑200 status, use inference tables to query the logged request and response data. Filter on `status_code != 200` and examine columns such as `request`, `response`, `request_time`, and `status_code`. For AI agents with [agent tracing](/concepts/autogen-auto-tracing.md), the **Response** column contains detailed traces.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Concurrency and Quota Errors

| Error Message (approx.) | Cause | Resolution |
|--------------------------|-------|------------|
| `Workspace exceeded provisioned concurrency quota` | Workspace‑level provisioned concurrency limit reached. | Delete or stop unused endpoints; request a limit increase from your Databricks account team.^[debugging-guide-for-model-serving-databricks-on-aws.md] |
| `Exceeded max number of parallel requests. Please contact your Databricks representative to increase the limit.` | Workspace limit on maximum parallel requests (HTTP 429). | Migrate to [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md) (which remove this limit), reduce client concurrency, or request a quota increase.^[debugging-guide-for-model-serving-databricks-on-aws.md] |
| `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity.` | Endpoint’s provisioned concurrency cannot handle incoming traffic. | Enable autoscaling for the endpoint or manually increase provisioned concurrency.^[debugging-guide-for-model-serving-databricks-on-aws.md] |

## Summary Table

| Error Category | Typical HTTP Status | Common Symptoms |
|----------------|---------------------|-----------------|
| Container build failure | N/A (endpoint fails to start) | `No space left`, GPU unavailability, missing modules in build logs |
| Runtime – dependency | `4xx` | `No module named` at load time |
| Runtime – `predict()` error | `4xx` | `Encountered an unexpected error while evaluating` |
| Concurrency – endpoint | `429` | `Too many concurrent requests` |
| Concurrency – workspace | `429` | `Exceeded max number of parallel requests` |
| Provisioned concurrency quota | N/A (endpoint may not scale) | `Workspace exceeded provisioned concurrency quota` |

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
