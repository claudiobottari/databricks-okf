---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 63a0e6fd0466bd1524e5ef0d56eeb4cf046d0902d45ba9256499df7e9071613b
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-error-code-semantics-4xx-vs-5xx
    - MSECS(V5
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Model Serving Error Code Semantics (4xx vs 5xx)
description: Mapping of MLflowException to 4xx customer-caused errors and 5xx Databricks-responsibility errors in model serving endpoints.
tags:
  - model-serving
  - error-handling
  - http-status-codes
timestamp: "2026-06-18T15:11:32.032Z"
---

# Model Serving Error Code Semantics (4xx vs 5xx)

**Model Serving Error Code Semantics** describes the intended distinction between HTTP 4xx and 5xx status codes returned by [Model Serving](/concepts/model-serving.md) endpoints. Databricks reserves 4xx codes for customer-caused errors (such as misconfigured model code or quota limits) and 5xx codes for errors where Databricks infrastructure is at fault. This semantic helps users quickly determine the root cause and appropriate remediation path. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## 4xx Error Codes

A 4xx response indicates that the request or the model configuration contains an issue that the customer can resolve. The most common 4xx codes are `403 PERMISSION_DENIED`, `429 Too Many Requests`, and generic 4xx responses triggered by model code errors. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Model code exceptions

If the model’s `predict()` function raises an `MlflowException`, the endpoint maps the error to a 4xx response. Databricks classifies these as customer-caused errors because the error message (e.g., missing dependency, incompatible input) points to a fix the customer can make. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### 429 Too Many Requests

The endpoint returns `429` in two distinct scenarios:

- **Parallel requests limit exceeded** – The workspace has reached the maximum number of simultaneous requests allowed. The error message reads:  
  `Exceeded max number of parallel requests. Please contact your Databricks representative to increase the limit`.  
  To resolve, either reduce the number of concurrent clients or request a quota increase from your Databricks representative. Databricks also recommends migrating to [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md), where this limit is removed. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

- **Provisioned concurrency insufficient** – The endpoint’s current provisioned concurrency cannot handle the incoming traffic volume. The error message reads:  
  `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity.`  
  If autoscaling is enabled, the system will automatically scale up to the endpoint’s configured maximum. Otherwise, manually increase [Provisioned Concurrency](/concepts/provisioned-concurrency.md) or enable autoscaling. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Other 4xx responses

Other 4xx codes (e.g., `403`) may appear due to permission or policy issues that the customer can address. See 403 PERMISSION_DENIED Serverless Budget Policy Error for one such example. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## 5xx Error Codes

A 5xx response indicates that Databricks infrastructure is responsible for the failure. These errors typically require intervention from Databricks support. Examples include build failures caused by insufficient GPU availability or internal server errors during container creation. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

Customers should not see 5xx codes for issues they can fix themselves. If a 5xx error occurs, review the endpoint’s event logs (under the **Events** tab) for details, and contact Databricks support if the issue persists. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Troubleshooting aids

- **[Inference Tables](/concepts/inference-tables.md)** – Automatically log all requests and responses in a Unity Catalog table. Query the table by `status_code` to identify failed requests and perform root cause analysis. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Event logs** – Show container build progress and error events. A successful build logs `SERVED_ENTITY_CONTAINER_EVENT` with `Container image creation finished successfully`. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- Model Serving Limits and Regions
- [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md)
- Debugging guide for Model Serving
- MlflowException
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md)
- [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md)

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
