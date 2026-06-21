---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a5b6831eea5731e2b5e261d42c08516fa7bd01b1c2cb34f76d2a6ef849c6ee8a
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-deployment-timeout
    - MDT
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Model Deployment Timeout
description: Timeout during container build and model deployment, with retry limits and duration limits based on CPU/GPU workload size.
tags:
  - model-serving
  - deployment
  - timeouts
timestamp: "2026-06-19T14:55:56.522Z"
---

```yaml
---
title: Model Deployment Timeout
summary: Timeouts during model container build and deployment to a serving endpoint, with retry logic and workload-specific time limits.
sources:
  - debug-model-serving-timeouts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:55:46.363Z"
updatedAt: "2026-06-19T09:55:46.363Z"
tags:
  - databricks
  - model-serving
  - deployment
  - timeouts
aliases:
  - model-deployment-timeout
  - MDT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Model Deployment Timeout

**Model Deployment Timeout** is an error that occurs when the process of deploying or updating a [Model Serving](/concepts/model-serving.md) endpoint does not complete within the maximum allowed duration. The timeout can arise from issues in either the container build phase or the model deployment phase, and the specific timeout duration depends on the endpoint’s workload configuration. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Timeout Durations

The deployment process consists of two sequential phases, each with its own timeout behavior:

- **Container build phase**: There is no hard time limit, but the build process retries up to 3 times before failing. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Model deployment phase** (after the container is built): The system waits for:
  - **30 minutes** for CPU workloads,
  - **60 minutes** for GPU small or medium workloads,
  - **120 minutes** for GPU large workloads. ^[debug-model-serving-timeouts-databricks-on-aws.md]

If either phase exceeds these limits, the overall deployment times out.

## Diagnosing Deployment Timeouts

To investigate a deployment timeout:

1. Open the **Events** tab of the model serving endpoint page and search for `"timed out"` messages. ^[debug-model-serving-timeouts-databricks-on-aws.md]
2. Navigate to the **Logs** tab and examine the build logs. Common issues include library dependency problems, resource constraints, configuration errors, and other build-related failures. ^[debug-model-serving-timeouts-databricks-on-aws.md]
3. Refer to [Debug after container build failure](/concepts/container-build-debugging-for-model-serving.md) for further troubleshooting steps. ^[debug-model-serving-timeouts-databricks-on-aws.md]

The Model Serving Limits page documents resource and payload limits that may also affect endpoint behavior.

## Related Timeout Types

Model deployment timeouts are distinct from other timeouts that can occur after the endpoint is healthy:

- **[Server-Side Timeouts](/concepts/server-side-timeouts.md)** – The endpoint is healthy, but individual request processing exceeds the default server-side timeout (e.g., 597 seconds for CPU/GPU endpoints). ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Client-side timeouts** – Caused by MLflow environment variables (e.g., `MLFLOW_HTTP_REQUEST_TIMEOUT` defaults to 120 seconds) or third‑party client APIs such as the OpenAI client. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **[Idle endpoint warm-up](/concepts/idle-endpoint-warm-up-delay.md)** – Endpoints scaled to zero may time out while warming up on the first request. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
