---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3fd236d2143074d56b33b3d91a6bb0aebd9922b991cce48abd5ac2da36d2da97
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - container-build-event-logs
    - CBEL
    - Container Build Failures
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Container Build Event Logs
description: Event logs available in the workspace UI's Events tab that track container build progress, with successful builds emitting a SERVED_ENTITY_CONTAINER_EVENT with a completion message.
tags:
  - model-serving
  - debugging
  - containers
timestamp: "2026-06-18T11:44:05.975Z"
---

# Container Build Event Logs

**Container Build Event Logs** are records of the container image creation process for [Model Serving](/concepts/model-serving.md) endpoints in Databricks. These logs provide visibility into the progress and outcome of container builds, helping users diagnose failures and verify successful deployments. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Overview

When deploying a model to a serving endpoint, Databricks builds a container image that packages the model code, dependencies, and runtime environment. The container build event logs capture the sequence of events during this build process, accessible through the **Events** tab in the workspace UI. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Viewing Container Build Event Logs

To access container build event logs:

1. Navigate to the **Serving** tab in your Databricks workspace.
2. Select the endpoint name.
3. Click the **Events** tab.

The event logs display information about the progress of the container build, including timestamps, event types, and status messages. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Successful Build Indicators

A successful container build is indicated by the following event: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

| Field | Value |
|-------|-------|
| Event type | `SERVED_ENTITY_CONTAINER_EVENT` |
| Message | `Container image creation finished successfully` |

If you do not see any build event or message within one hour of creating the endpoint, contact Databricks support for assistance. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Common Build Failures

### `OSError: [Errno 28] No space left on device`

This error occurs when too many large artifacts are logged alongside the model unnecessarily. To resolve: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

1. Check in [MLflow](/concepts/mlflow.md) that extraneous artifacts are not logged alongside the model.
2. Remove unnecessary artifacts.
3. Redeploy the slimmed-down package.

### Build Failure Due to Lack of GPU Availability

GPU builds may fail with the following error: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

```
Build could not start due to an internal error - please contact your Databricks representative.
```

This error is due to restrictions in GPU supply and availability. Contact your Databricks account team to provision more GPU resources, depending on region availability. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Missing Dependencies

If the build fails due to missing dependencies, verify that all required libraries are properly specified as model dependencies. Pay special attention to custom libraries and ensure that `.whl` files are included as artifacts. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### `flash-attn` Build Errors

Models requiring `flash-attn` may encounter build errors such as `ModuleNotFoundError: No module named 'torch'`. Databricks recommends using a custom wheel version of `flash-attn` and specifying all pip requirements as a list when calling `mlflow.transformers.log_model`. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

For example, for CUDA 11.8, use the following compatible versions: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

- PyTorch 2.0.1+cu118
- Torchvision 0.15.2+cu118
- Flash-Attn wheel: `flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl`

## Confirming Installed Package Versions

In the build logs, you can confirm the package versions that are installed correctly: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

- For [MLflow](/concepts/mlflow.md) versions, if no version is specified, Model Serving uses the latest version.
- For custom GPU serving, Model Serving installs the recommended versions of `cuda` and `cuDNN` according to public PyTorch and TensorFlow documentation.

## Post-Build Debugging

If the container build succeeds but the endpoint encounters runtime errors, see Debugging Guide for Model Serving for further troubleshooting steps, including: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

- Missing dependency errors at runtime
- Model prediction failures or timeouts
- Root cause analysis using [Inference Tables](/concepts/inference-tables.md)
- Concurrency and quota-related errors

## Best Practices

- **Define all important libraries as model dependencies** to ensure consistent and reproducible model behavior across environments. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Use pre-deployment validation** to catch common problems before they occur during container build. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Monitor build logs** after creating or updating endpoints to verify successful container image creation. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The serving infrastructure that uses container builds
- MLflow Models — The model format packaged into containers
- [Inference Tables](/concepts/inference-tables.md) — For runtime request/response logging and debugging
- Debugging Guide for Model Serving — Comprehensive troubleshooting for serving endpoints
- [Model Serving Pre-Deployment Validation](/concepts/model-serving-pre-deployment-testing-workflow.md) — Validation steps before deployment

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
