---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 927d066c8b7bb7ebd3513b837ba2733cf7d1c1dacaf9963aefaeb900d91173fc
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limits-and-model-serving-endpoint-throttling
    - Model Serving Endpoint Throttling and Rate Limits
    - RLAMSET
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Rate Limits and Model Serving Endpoint Throttling
description: How exceeding rate limits on model serving endpoints can cause request failures and timeouts, including references to resource and payload limits.
tags:
  - model-serving
  - rate-limiting
  - timeouts
timestamp: "2026-06-18T11:44:02.444Z"
---

# Rate Limits and Model Serving Endpoint Throttling

**Rate Limits and Model Serving Endpoint Throttling** refers to the restrictions on the number of requests a model serving endpoint can accept within a given time window. When the rate limit is exceeded, additional requests may fail, leading to errors or timeouts for clients.

## Overview

Model serving endpoints in Databricks enforce rate limits to protect backend resources and ensure fair usage among tenants. Each endpoint type (CPU, GPU small/medium/large) has its own rate limit, which is documented in the resource and payload limits for the service. Exceeding the rate limit causes the endpoint to throttle incoming requests, rejecting or delaying further traffic. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Effect of Rate Limits

When the rate of requests sent to an endpoint surpasses its configured limit, the endpoint begins to reject additional requests. This can manifest as HTTP 429 (Too Many Requests) errors or, if combined with client-side retry logic, may appear as timeout failures. Multiple requests made above the rate limit can ultimately lead to failures for subsequent requests. ^[debug-model-serving-timeouts-databricks-on-aws.md]

For third-party clients integrated into a model pipeline (for example, an OpenAI client used within a custom PyFunc model), rate limiting behavior is determined by the respective third-party service. Databricks recommends reviewing the third-party client’s documentation for rate limit details and configuring appropriate timeouts and retry strategies. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Distinction from Timeouts

While rate limiting and timeouts are both common failure modes when calling model serving endpoints, they are distinct issues:

- **Rate limits** control the *frequency* of requests; exceeding the limit causes immediate rejection.
- **Timeouts** control the *duration* a client or server waits for a response; hitting a timeout indicates the request was accepted but did not complete within the allowed window.

Rate limit failures can also lead to client-side timeouts if the client retries aggressively without backoff. See [Debug model serving timeouts](/concepts/model-serving-endpoint-timeouts.md) for more details on timeout handling. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Recommendations

- **Know your endpoint’s rate limit.** Refer to the [Resource and payload limits](/concepts/model-serving-resource-and-payload-limits.md) documentation for the specific limits of your endpoint type (CPU, GPU). ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Design clients with backoff and retry logic.** When a rate-limit error (429) is received, clients should pause and retry after a delay, reducing the chance of overwhelming the endpoint again.
- **Monitor endpoint events and logs.** The **Events** and **Logs** tabs of the model serving endpoint page may contain indicators of rate limiting, such as repeated request failures or timeouts.
- **Review third-party client settings.** For pipelines that call external services (e.g., OpenAI), configure the client’s timeout and retry parameters according to the third-party’s rate limit documentation. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Resource and payload limits](/concepts/model-serving-resource-and-payload-limits.md)
- [Debug model serving timeouts](/concepts/model-serving-endpoint-timeouts.md)
- Client-side timeouts
- Model Serving Endpoint Events

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
