---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 13b60dc8a6c9f50b58354cf745150f5c26594376d062e53d9f409d58290f5007
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limit-induced-request-failure
    - RLIRF
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Rate Limit Induced Request Failure
description: Request failures caused by exceeding the rate limit of a model serving endpoint, leading to additional request rejections.
tags:
  - model-serving
  - rate-limiting
  - timeouts
timestamp: "2026-06-19T14:56:05.472Z"
---

# Rate Limit Induced Request Failure

**Rate Limit Induced Request Failure** occurs when a model serving endpoint receives more requests than its configured rate limit allows, causing additional requests to fail. This type of failure is distinct from other timeout types, such as server-side timeouts or connection timeouts, and requires different debugging and mitigation approaches.

## Overview

Rate limits are enforced on model serving endpoints to protect system resources and ensure fair usage. When the number of requests to an endpoint exceeds these limits, the system begins rejecting additional requests. These rejections appear as failures to the client, returning error messages rather than successful inference results. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Identifying Rate Limit Failures

Rate limit induced request failures typically occur when multiple requests are made over the allowed rate limit of an endpoint. These failures can be identified through error messages containing the terms **_"timed out"_** or **_"timeout"_** in [model serving logs], though the underlying cause is rate limiting rather than the request taking too long to process. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Rate Limits by Endpoint Type

The specific rate limits that trigger these failures vary depending on the type of model serving endpoint being used. For details on the exact rate limits applicable to different endpoint configurations, see the documentation on [resource and payload limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#resource-and-payload-limits). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Third-Party Client Considerations

For model serving endpoints that incorporate third-party clients — such as through [Custom PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md) or PyFunc Custom Schema Agents — rate limit induced failures can originate from the third-party service as well. Databricks recommends reviewing the documentation of any third-party client used in your model pipeline to understand their specific rate limiting behavior. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Model Serving Timeouts](/concepts/model-serving-endpoint-timeouts.md) — The broader category of timeout errors during model serving.
- [Server-Side Timeouts](/concepts/server-side-timeouts.md) — Timeouts caused by the server processing time exceeding limits.
- Client-Side Timeouts — Timeouts caused by client configuration, including MLflow environment variables.
- [Connection Timeout](/concepts/connection-timeout.md) — Timeouts related to establishing a connection with the server.
- [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md) — The specific rate limits and payload size constraints for different endpoint types.
- [Custom PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md) — Custom Python functions that may incorporate third-party APIs with their own rate limits.

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
