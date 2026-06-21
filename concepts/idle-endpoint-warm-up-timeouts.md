---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a3adf3c9f3267be79bd51fed12c8b727153055e25d80bb0373e4f450a0aded6
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idle-endpoint-warm-up-timeouts
    - IEWT
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Idle Endpoint Warm-Up Timeouts
description: Timeouts that can occur when a Model Serving endpoint that has scaled to 0 receives a request and takes too long to warm up.
tags:
  - model-serving
  - scaling
  - timeouts
  - warm-up
timestamp: "2026-06-19T18:16:46.389Z"
---

# Idle Endpoint Warm-Up Timeouts

**Idle Endpoint Warm-Up Timeouts** occur when a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) that has been scaled to 0 receives a request and takes too long to become operational, causing the client request to time out before the endpoint finishes warming up. This is a common source of timeout errors in complex inference pipelines that depend on multiple downstream services.

## Overview

Model Serving endpoints can be configured to scale to zero when they are not receiving traffic, as a cost optimization measure. When such an endpoint receives a new request, it must warm up — provisioning compute resources and loading the model — before it can serve the request. If this warm-up process takes longer than the client's timeout window, the request fails with a timeout error.^[debug-model-serving-timeouts-databricks-on-aws.md]

## Impact on Inference Pipelines

The effect of idle endpoint warm-up is especially visible in pipelines that chain multiple steps together. For example, a pipeline might call a [Provisioned Throughput Endpoint](/concepts/provisioned-throughput-endpoint.md) or an AI Search index as part of its processing chain. If any of these downstream services are cold-starting simultaneously, the cumulative warm-up time can exceed the client's timeout threshold.^[debug-model-serving-timeouts-databricks-on-aws.md]

## Diagnosis

To determine if an idle endpoint warm-up is causing timeouts:

1. Check the endpoint's **Events** tab for any warnings or errors related to scaling activity.
2. Examine the **Service Logs** for the endpoint to see if request processing times correlate with cold-start delays.
3. If [Inference Tables](/concepts/inference-tables.md) are enabled, review the request timing data for patterns consistent with cold starts — particularly requests that take significantly longer than subsequent requests to the same endpoint.

## Mitigation Strategies

### Adjust Endpoint Scaling Configuration

Configure the endpoint to maintain a minimum number of warm instances (scale to 1 or higher) rather than scaling to zero. This eliminates cold starts entirely but increases baseline cost. The trade-off between cost and latency should be evaluated based on workload requirements.^[debug-model-serving-timeouts-databricks-on-aws.md]

### Increase Client-Side Timeouts

If the endpoint must scale to zero, ensure that client-side timeouts are configured to accommodate the expected warm-up duration:

- For [MLflow](/concepts/mlflow.md) clients, adjust the `MLFLOW_HTTP_REQUEST_TIMEOUT` environment variable beyond its default of 120 seconds.
- For [OpenAI client](/concepts/openai-client-compatibility.md) or other third-party client APIs, configure the `timeout` parameter with a value that accounts for the warm-up period.

### Use Warm-Up Requests

Implement a health-check or warm-up mechanism that sends periodic requests to the endpoint to prevent it from scaling to zero during expected usage periods.

## Related Concepts

- [Model Serving Endpoint Scaling](/concepts/model-serving-endpoint-scaling.md) — Configuration options for scaling behavior
- [Model Deployment Timeouts](/concepts/model-deployment-timeouts.md) — Timeouts during the initial model deployment process
- [Server-Side Timeouts](/concepts/server-side-timeouts.md) — Timeout limits on the serving infrastructure side
- [Client-Side Timeouts: MLflow Configuration](/concepts/client-side-timeout-mlflow-configuration.md) — Configuring MLflow timeout environment variables
- [Client-Side Timeouts: Third Party Client APIs](/concepts/client-side-timeout-third-party-client-apis.md) — Configuring timeouts for external API clients
- [Connection Timeout](/concepts/connection-timeout.md) — Timeout for establishing TCP connections

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
