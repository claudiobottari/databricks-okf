---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8120ad6d8dbabb78d228597ab2fc0bfb49b05c76b101fb9c7e6063bcba4b21c4
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-concurrency-and-parallel-request-limits
    - Parallel Request Limits and Provisioned Concurrency
    - PCAPRL
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Provisioned Concurrency and Parallel Request Limits
description: Managing Databricks Model Serving concurrency quotas, parallel request limits, and the 'too many concurrent requests' 429 error, including mitigation strategies like autoscaling, route-optimized endpoints, and quota increases.
tags:
  - model-serving
  - scaling
  - quotas
  - performance
timestamp: "2026-06-19T14:56:28.617Z"
---

# Provisioned Concurrency and Parallel Request Limits

**Provisioned Concurrency** and **Parallel Request Limits** are two distinct capacity constraints that affect [Model Serving](/concepts/model-serving.md) endpoints on Databricks. Provisioned concurrency controls how many simultaneous requests an endpoint can process, while parallel request limits govern the maximum number of concurrent requests a workspace can handle.

## Provisioned Concurrency

Provisioned concurrency defines the number of parallel inference requests a single model serving endpoint can handle at once. Each endpoint has a provisioned concurrency quota that determines its capacity to serve incoming traffic. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Quota Exhaustion

A workspace may exceed its provisioned concurrency quota, resulting in the error: `Workspace exceeded provisioned concurrency quota`. This indicates the workspace has reached its limit for provisioned concurrency across all endpoints. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Freeing Up Quota

You can free up provisioned concurrency quota by deleting or stopping unused endpoints. Reach out to your Databricks account team and provide your workspace ID to request a concurrency increase. Availability of increases depends on region capacity. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Parallel Request Limits

Parallel request limits control the maximum number of requests that can be sent to a workspace simultaneously. When this limit is exceeded, you receive a 429 error: `Exceeded max number of parallel requests. Please contact your Databricks representative to increase the limit`. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Route Optimized Endpoints

Databricks recommends moving to [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md) where this parallel request limit has been removed. If you cannot migrate to route optimized endpoints, you can reduce the number of clients sending inference requests or contact your Databricks representative for a quota increase. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Too Many Concurrent Requests

When an endpoint's current provisioned concurrency cannot handle incoming traffic volume, you may receive a 429 error: `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity.` If you have enabled autoscaling for your endpoint, the system automatically provisions additional concurrency up to the endpoint's configured limit. If autoscaling is not enabled, consider manually increasing provisioned concurrency or enabling autoscaling to handle traffic spikes. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Relationship Between Limits

Provisioned concurrency and parallel request limits work together to control endpoint capacity. **Provisioned concurrency** limits how many requests a single endpoint can process simultaneously, while **parallel request limits** control the total number of concurrent requests across all endpoints in a workspace. When both limits are exceeded, the system returns appropriate error codes (429 for parallel requests, and the provisioned concurrency error for endpoint-level limits). ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- Model Serving limits and regions
- [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md)
- [Serving endpoint management](/concepts/feature-serving-endpoint-lifecycle-management.md)
- Autoscaling

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
