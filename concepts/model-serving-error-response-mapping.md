---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 52bdc80562d06c0ee6850e8668672fe2b182681166d3370a150c3140aaeee401
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-error-response-mapping
    - MSERM
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Model Serving Error Response Mapping
description: Databricks convention mapping MlflowException model code errors to 4xx responses (customer-caused) while reserving 5xx errors for Databricks infrastructure faults.
tags:
  - model-serving
  - error-handling
  - api
timestamp: "2026-06-19T18:17:01.635Z"
---

# Model Serving Error Response Mapping

**Model Serving Error Response Mapping** describes how [Model Serving](/concepts/model-serving.md) endpoints on Databricks translate model‑code errors, infrastructure errors, and policy violations into HTTP status codes. The mapping distinguishes between errors that are the customer’s responsibility (4xx) and errors that are Databricks’ responsibility (5xx), enabling faster triage and debugging.

## Mapping Philosophy

Databricks Model Serving follows a **customer‑vs‑platform fault** convention:

| Error origin | HTTP status range | Reasoning |
|--------------|------------------|-----------|
| Model code errors (e.g., `MlflowException`) | 4xx | The error is caused by the user’s code or configuration and can be resolved by fixing the model or its dependencies.^[debugging-guide-for-model-serving-databricks-on-aws.md] |
| Infrastructure or platform errors | 5xx | The error is caused by Databricks infrastructure and requires platform‑side intervention.^[debugging-guide-for-model-serving-databricks-on-aws.md] |

Specifically, if the model’s `predict()` function or related code raises an `MlflowException`, the endpoint returns a **4xx** response. Databricks considers these customer‑caused errors because the error message contains actionable information for the user.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Common Error Responses

### 4xx Errors (Customer‑Caused)

| HTTP code | Typical error message | Cause |
|-----------|----------------------|-------|
| `400` (implicit) | `MlflowException` variants | Model code errors, missing dependencies, or invalid inputs.^[debugging-guide-for-model-serving-databricks-on-aws.md] |
| `429` Too Many Requests | `Exceeded max number of parallel requests. Please contact your Databricks representative to increase the limit.` | Workspace‑level parallel request limit reached. This limit does not apply to [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md).^[debugging-guide-for-model-serving-databricks-on-aws.md] |
| `429` Too Many Requests | `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity.` | The endpoint’s [Provisioned Concurrency](/concepts/provisioned-concurrency.md) is insufficient for the current traffic volume. Autoscaling may mitigate this.^[debugging-guide-for-model-serving-databricks-on-aws.md] |
| `429` (implied) | `Workspace exceeded provisioned concurrency quota` | Workspace quota for provisioned concurrency exhausted. Free quota by deleting or stopping unused endpoints.^[debugging-guide-for-model-serving-databricks-on-aws.md] |

#### Mapping of `MlflowException`

When the model code throws an `MlflowException`, Model Serving **maps it to a 4xx response** rather than a 5xx. This mapping signals that the error is resolvable by the user—for example, by fixing a missing dependency, correcting input format, or updating the model code.^[debugging-guide-for-model-serving-databricks-on-aws.md]

#### Common 4xx‑triggering scenarios

- **Missing dependency**: `An error occurred while loading the model. No module named <module>.` This indicates the container build did not include the required Python package.^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Model evaluation failure**: `Encountered an unexpected error while evaluating the model. Verify that the input is compatible with the model for inference.` Usually caused by a bug in the `predict()` function.^[debugging-guide-for-model-serving-databricks-on-aws.md]

### 5xx Errors (Platform‑Caused)

Databricks reserves **5xx status codes** for errors where the platform is at fault—for example, infrastructure failures, build system errors, or resource unavailability. A 5xx response indicates that the user cannot resolve the issue without Databricks support.^[debugging-guide-for-model-serving-databricks-on-aws.md]

Examples from the documentation:
- Container build failures due to disk space (`OSError: [Errno 28] No space left on device`) or GPU availability. These manifest as build events, not directly as HTTP responses to inference requests, but if they prevent endpoint creation, the endpoint may return 503 or 500. The source does not explicitly define the status code but notes that such failures require Databricks intervention.^[debugging-guide-for-model-serving-databricks-on-aws.md]
- Internal errors during build: `Build could not start due to an internal error - please contact your Databricks representative.`^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Debugging with Error Codes

To determine whether an error is customer‑sourced or platform‑sourced:

1. **Check the HTTP status code** of the inference response. 4xx → check model code and dependencies; 5xx → contact Databricks support.
2. **Examine endpoint event logs** (Events tab) for build‑related errors.
3. **Use [Inference Tables](/concepts/inference-tables.md)** to query failed requests by `status_code` column:
   ```sql
   SELECT * FROM my-catalog.my-schema.my-table WHERE status_code != 200;
   ```
   This enables root‑cause analysis of 4xx and 5xx responses.^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md)
- [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md)
- [Inference Tables](/concepts/inference-tables.md)
- [MLflow](/concepts/mlflow.md)
- Model Serving Limits and Regions

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
