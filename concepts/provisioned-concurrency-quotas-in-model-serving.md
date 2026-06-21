---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0859d636c71439758fb17a9925324a793880a68d82c2747e83232a5fd2e4674
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-concurrency-quotas-in-model-serving
    - PCQIMS
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Provisioned Concurrency Quotas in Model Serving
description: Workspace-level limits on provisioned concurrency for model serving endpoints, including how to free quota by deleting/stopping endpoints and requesting increases.
tags:
  - model-serving
  - scaling
  - limits
timestamp: "2026-06-19T18:16:45.664Z"
---

## Provisioned Concurrency Quotas in Model Serving

**Provisioned Concurrency Quotas** define the maximum number of concurrent inference requests that a single model serving endpoint can handle simultaneously. When an endpoint is created without autoscaling, you specify a fixed provisioned concurrency value. This value determines how many request slots are reserved for the endpoint at any time. If the incoming request volume exceeds this value, requests may be rejected or queued depending on the system configuration. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Exceeding the Provisioned Concurrency Quota

When a workspace’s aggregate provisioned concurrency across all endpoints reaches the account-level quota, a user may encounter the error: `Workspace exceeded provisioned concurrency quota`. This indicates that the total concurrency allocated to existing endpoints has consumed the workspace’s entire allowance. To free up quota, you can either **delete** unused endpoints or **stop** endpoints that are not needed. If the quota is still insufficient, contact your Databricks account team with your workspace ID to request a concurrency increase, subject to region availability. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Too Many Concurrent Requests

An individual endpoint that receives more concurrent requests than its provisioned concurrency can serve will return a `429 Too Many Concurrent Requests` error with the message: `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity.` If autoscaling is enabled on the endpoint, the system will automatically increase the concurrency up to the endpoint’s configured maximum to absorb the load. If autoscaling is not enabled, you must manually raise the provisioned concurrency value or enable autoscaling to handle traffic spikes. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Relationship to Parallel Requests Limit

The workspace also enforces a global **parallel requests limit**, which caps the total number of requests that can be sent to all endpoints at once. Exceeding this limit produces a different 429 error: `Exceeded max number of parallel requests.` Databricks recommends migrating to [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md) where this parallel requests limit is removed. If migration is not possible, either reduce the number of clients sending inference requests or contact your Databricks representative for a quota increase. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Troubleshooting and Best Practices

- To diagnose provisioned concurrency issues, review the endpoint’s **Events** tab in the UI for relevant error messages and build events. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- Use [Inference Tables](/concepts/inference-tables.md) to log all requests and responses, and query the `status_code` column to identify non‑200 responses. This helps pinpoint which requests are being throttled. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- If you consistently see `429 Too Many Concurrent Requests`, consider enabling autoscaling on the endpoint, or increase the provisioned concurrency value directly.
- Monitor your workspace’s aggregate concurrency usage and clean up idle endpoints to avoid hitting the workspace quota.

### Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Autoscaling for Model Serving](/concepts/queuing-and-autoscaling-in-model-serving.md)
- [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md)
- [Inference Tables](/concepts/inference-tables.md)
- Model Serving Limits and Regions
- 429 Error Handling

### Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
