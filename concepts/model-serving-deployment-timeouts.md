---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 588a24e53f1d9ad0883208abe570aafd2d1d454a0435b2d3da24f903d13c4b47
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-deployment-timeouts
    - MSDT
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Model Serving Deployment Timeouts
description: Timeouts that occur during the container build and model deployment phases of Databricks Model Serving, including retry logic and duration limits per workload type.
tags:
  - model-serving
  - deployment
  - timeouts
  - databricks
timestamp: "2026-06-18T15:11:01.128Z"
---

Here is the wiki page for "Model Serving Deployment Timeouts".

---

## Model Serving Deployment Timeouts

**Model Serving Deployment Timeouts** occur when deploying or updating a model on a [Model Serving](/concepts/model-serving.md) endpoint fails because the build and startup process exceeds a predefined duration. These timeouts prevent the endpoint from becoming ready to serve traffic.

## Identifying Deployment Timeouts

Deployment timeouts are recorded in the **Events** tab of the model serving endpoint page. You can search for messages containing `"timed out"` to identify them. ^[debug-model-serving-timeouts-databricks-on-aws.md]

![Screenshot of the Model Serving Endpoint Events tab showing a search for "timed out".](https://docs.databricks.com/aws/en/assets/images/model-serving-endpoint-events-tab-de9ed173c876cf1f950996697b33ce4b.png)

## Timeout Limits

The deployment process times out if the container build and model deployment exceed a duration that depends on the endpoint's workload configuration. ^[debug-model-serving-timeouts-databricks-on-aws.md]

- **Container Build**: Has no hard limit but retries up to 3 times. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Model Deployment** (after container build):
  - **CPU workload**: 30 minutes ^[debug-model-serving-timeouts-databricks-on-aws.md]
  - **GPU small/medium** workload: 60 minutes ^[debug-model-serving-timeouts-databricks-on-aws.md]
  - **GPU large** workload: 120 minutes ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Debugging a Deployment Timeout

If you find a `"timed out"` message, navigate to the **Logs** tab and examine the build logs to determine the cause. Common issues include:

- Library dependency problems
- Resource constraints
- Configuration errors

^[debug-model-serving-timeouts-databricks-on-aws.md]

![Screenshot of the Model Serving Endpoint Build Logs tab.](https://docs.databricks.com/aws/en/assets/images/model-serving-endpoint-build-logs-01cec0c5ea01909dc30c965c950385ba.png)

For further guidance on container build failures, see [Debug after container build failure](/concepts/container-build-debugging-for-model-serving.md). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Server-Side Timeouts](/concepts/server-side-timeouts.md) — Timeouts for inference requests after the endpoint is healthy.
- Client-Side Timeouts — Timeouts on the request-making side, often from MLflow or third-party client configurations.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The serving endpoint where deployment and inference occur.
- [Debug after container build failure](/concepts/container-build-debugging-for-model-serving.md) — Troubleshooting steps for a failed container build.

## Sources

This article is based on the following source document:

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
