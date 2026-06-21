---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af58e45d157c687491afc8bd3c556f3099a9922ba8a2cd50175694f4dec221e0
  pageDirectory: concepts
  sources:
    - manage-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-status
    - MSES
    - Serving Endpoint States
    - Serving Endpoint Status
    - Serving endpoint state
  citations:
    - file: manage-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Status
description: The operational states of a Databricks model serving endpoint, including Ready, Not Ready, and Update Failed indicators.
tags:
  - model-serving
  - endpoint-management
  - monitoring
  - databricks
timestamp: "2026-06-19T19:25:46.873Z"
---

# Model Serving Endpoint Status

**Model Serving Endpoint Status** refers to the operational state of a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) on Databricks. The status indicates whether the endpoint can serve queries, whether the latest configuration update succeeded, and whether the endpoint is currently active or stopped. You can check endpoint status using the **Serving** UI, the REST API, the Databricks Workspace Client, or the MLflow Deployments SDK. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Possible Status Values

The following statuses are possible for a model serving endpoint: ^[manage-model-serving-endpoints-databricks-on-aws.md]

| Status | Meaning |
|--------|---------|
| **Ready** | The endpoint is fully operational and can accept and serve inference queries. |
| **Ready (Update failed)** | The endpoint can still serve queries (it is running a previous working configuration), but the most recent attempt to update the endpoint was unsuccessful. |
| **Not ready (Updating)** | The endpoint is undergoing a configuration update and cannot serve queries until the update completes. |
| **Not ready (Update failed)** | The endpoint cannot serve queries, and the latest update attempt was unsuccessful. |
| **Not ready (Stopped)** | The endpoint has been explicitly stopped and cannot serve queries until it is restarted. |

### Readiness

"Readiness" refers to whether or not an endpoint can be queried. An endpoint with any **Ready** status is queryable. An endpoint with any **Not ready** status is not queryable. ^[manage-model-serving-endpoints-databricks-on-aws.md]

### Update Failed

"Update failed" indicates that the latest change to the endpoint — such as a model update or configuration change — was unsuccessful and could not be applied. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Viewing Endpoint Status

### Using the Serving UI

You can view the endpoint status in the **Serving endpoint state** indicator at the top of an endpoint's details page. Status is also visible from the list of all endpoints. ^[manage-model-serving-endpoints-databricks-on-aws.md]

### Using the REST API

To programmatically check endpoint status, query the Serving Endpoints API endpoint:

```
GET /api/2.0/serving-endpoints/{name}
```

The response includes the `state` field, which contains the current status. ^[manage-model-serving-endpoints-databricks-on-aws.md]

### Using the Databricks Workspace Client and MLflow Deployments SDK

You can retrieve endpoint status using the `databricks.sdk` Python library or the `mlflow.deployments` SDK. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Additional Operational States

When an endpoint is **Stopped**:

- The resources provisioned for it are shut down.
- The endpoint cannot serve queries until it is started again.
- Only endpoints that serve [custom models](/concepts/custom-mlflow-pythonmodel.md) and have no in-progress updates can be stopped.
- Stopped endpoints do not count against resource quota.
- Queries sent to a stopped endpoint return a 400 error.

^[manage-model-serving-endpoints-databricks-on-aws.md]

## Endpoint Schema Availability

The endpoint's [OpenAPI schema](/concepts/serving-endpoint-openapi-schema.md) — which describes the request and response format — can only be retrieved when the endpoint is in a **Ready** state and the served model has a model signature logged. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The serving infrastructure that hosts models for inference.
- [Create Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — How to create endpoints for custom models.
- Create Foundation Model Serving Endpoints — How to create endpoints for Databricks foundation models.
- [Debug a Model Serving Endpoint](/concepts/model-serving-endpoint.md) — Troubleshooting using build logs and server logs.
- [Manage Permissions on a Model Serving Endpoint](/concepts/update-model-serving-endpoints.md) — Controlling access to endpoints.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controlling spending for serverless endpoints.

## Sources

- manage-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [manage-model-serving-endpoints-databricks-on-aws.md](/references/manage-model-serving-endpoints-databricks-on-aws-7247257b.md)
