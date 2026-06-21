---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dbe98e3c7e4eac8743ae9b4c35550d5352ee8cecc9e4ad6c0fe581ae853d1b84
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-deployment-timeouts
    - MDT
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Model Deployment Timeouts
description: Timeouts that occur during container build and model deployment for Databricks Model Serving endpoints, including retry limits and workload-specific time limits.
tags:
  - model-serving
  - deployment
  - timeouts
  - container-build
timestamp: "2026-06-19T18:16:30.331Z"
---

# Model Deployment Timeouts

**Model Deployment Timeouts** occur when deploying or updating a model using [Model Serving](/concepts/model-serving.md) on Databricks, and the container build or deployment process exceeds a certain duration. These timeouts are recorded in the **Events** tab of the model serving endpoint page and can be found by searching for the term **_"timed out"_**. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Timeout Durations by Workload Type

The deployment process times out if the container build and model deployment exceed a duration that depends on the endpoint workload configuration. The container build has no hard limit but retries up to 3 times. After the container is built, the deployment waits for the following durations before timing out: ^[debug-model-serving-timeouts-databricks-on-aws.md]

- **CPU workloads**: 30 minutes
- **GPU small or medium workloads**: 60 minutes
- **GPU large workloads**: 120 minutes

## Debugging Deployment Timeouts

If you find a **_"timed out"_** message in the **Events** tab, navigate to the **Logs** tab and examine the build logs to determine the cause. Common causes include: ^[debug-model-serving-timeouts-databricks-on-aws.md]

- Library dependency issues
- Resource constraints
- Configuration issues

For further debugging after container build failure, see the documentation on [Debug after container build failure](/concepts/container-build-debugging-for-model-serving.md). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Best Practices

Before deploying, check your configuration and compare it to previous successful deployments. This can help identify configuration changes that might cause the deployment to exceed the timeout limit. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform for deploying and serving models on Databricks
- [Server-Side Timeouts](/concepts/server-side-timeouts.md) — Timeouts that occur when making requests to a healthy endpoint
- Client-Side Timeouts — Timeouts caused by MLflow or third-party client API configurations
- Model Serving Endpoint Events — The interface for monitoring deployment and serving events
- [Model Serving Build Logs](/concepts/model-serving-build-logs-troubleshooting.md) — Logs that provide details about container build processes

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
