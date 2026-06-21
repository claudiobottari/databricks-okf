---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e1285fecf3dbcac513bd2526f5fbe8447ac592ef6f117bae7e09593d6f629d3
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-error-code-semantics
    - MSECS
    - model-serving-error-code-semantics-4xx-vs-5xx
    - MSECS(V5
    - model-serving-error-response-mapping
    - MSERM
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Model Serving Error Code Semantics
description: Databricks Model Serving maps MlflowException model code errors to 4xx (customer-caused) responses and reserves 5xx for Databricks infrastructure errors, helping users determine responsibility.
tags:
  - model-serving
  - error-handling
  - api
timestamp: "2026-06-18T11:44:41.318Z"
---

# Model Serving Error Code Semantics

**Model Serving Error Code Semantics** define how Databricks [Model Serving](/concepts/model-serving.md) classifies HTTP response codes returned by an endpoint. Understanding these semantics helps operators distinguish between client-correctable errors (4xx) and infrastructure errors (5xx), and points to the appropriate debugging steps.

## General Principles

Databricks Model Serving uses the following convention for HTTP status codes: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

- **4xx (Client Error)** — These codes indicate a problem that the client can resolve. They are returned when the model’s own code raises an `MlflowException`. Because the error originates from customer-written logic (e.g., a `predict()` function), the error message typically contains actionable information. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **5xx (Server Error)** — These codes are reserved for errors where Databricks infrastructure is at fault. They are not expected when the model code itself is correct. If you receive a 5xx error and suspect it is not a transient infrastructure issue, contact Databricks support. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

This mapping means that a 4xx response from an endpoint does **not** always reflect a malformed HTTP request; it can be a business-logic error exposed by the model. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Common Error Codes and Causes

### 403 – Permission Denied (Serverless Budget Policy)

When [MLflow](/concepts/mlflow.md) tries to launch a serverless workload (e.g., scheduled scorer, synthetic evaluation) on a workspace where the default serverless budget policy is disabled and no fallback policy exists, the endpoint returns a `403 PERMISSION_DENIED` error. This is a separate category of error covered in the 403 PERMISSION_DENIED Serverless Budget Policy Error page. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### 429 – Too Many Requests

Two distinct 429 errors may appear:

1. **Workspace exceeds max number of parallel requests**  
   Message: `Exceeded max number of parallel requests. Please contact your Databricks representative to increase the limit.`  
   This indicates the workspace has hit its global parallel‑request quota. The recommended fix is to migrate to [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md), where this limit is removed. Alternatively, reduce the number of concurrent clients or request a quota increase. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

2. **Too many concurrent requests**  
   Message: `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity.`  
   This means the endpoint’s current provisioned concurrency cannot keep up with incoming traffic. If autoscaling is enabled, the system automatically adds concurrency up to the endpoint’s configured limit. Otherwise, manually increase provisioned concurrency or enable autoscaling. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Workspace Exceeded Provisioned Concurrency Quota

Message: `Workspace exceeded provisioned concurrency quota.`  
This is a resource‑level limit, not necessarily a 429. Free up quota by stopping or deleting unused endpoints. If the limit is still too low, contact your Databricks account team for an increase (subject to region availability). ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Model Evaluation Error (4xx)

When the model’s `predict()` method fails, the endpoint returns a 4xx error with a message like:  
`Encountered an unexpected error while evaluating the model. Verify that the input is compatible with the model for inference.`  
This is a customer‑caused error. Debug it by loading the model from MLflow in a notebook and calling `predict()` directly to reproduce the failure. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Missing Dependency (4xx or Container Build Failure)

If the container build fails with `No module named <module-name>`, it is a customer‑caused issue caused by an incomplete dependency specification. Ensure all required libraries, especially custom `.whl` files, are listed as model dependencies. This error surfaces during the container build phase (4xx-like semantics because the client can fix it). ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Diagnostic Tools

### Inference Tables

If [Inference Tables](/concepts/inference-tables.md) are enabled, all requests and responses are logged to a Unity Catalog table. Query the table to analyze failed requests:

```sql
SELECT * FROM my-catalog.my-schema.my-table WHERE status_code != 200;
```

Filter by `request_time`, `status_code`, and `response` columns to understand error patterns. For AI agents with tracing enabled, the **Response** column contains detailed traces. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Event Logs

The **Events** tab in the workspace UI shows container‑build progress. A successful build logs `SERVED_ENTITY_CONTAINER_EVENT` with message `Container image creation finished successfully`. If no build event appears after one hour, contact Databricks support. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving Pre-Deployment Validation](/concepts/model-serving-pre-deployment-testing-workflow.md) — Catch common errors before creating an endpoint.
- Monitor Model Quality and Endpoint Health — Logs and metrics for ongoing monitoring.
- [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md) — Eliminate the parallel‑requests limit.
- MLflowException — Custom exception that maps to 4xx responses.
- [Inference Tables](/concepts/inference-tables.md) — Automatic request/response logging.

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
