---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ace8a13015d8e3f08828f92a7df1e94e0a175e43eafecfe37bbcf5bab1e6bbae
  pageDirectory: concepts
  sources:
    - manage-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-lifecycle-management
    - ELM
  citations:
    - file: manage-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Lifecycle Management
description: Operations to stop, start, and delete model serving endpoints, including constraints on when each operation is allowed.
tags:
  - model-serving
  - endpoint-management
  - lifecycle
  - databricks
timestamp: "2026-06-19T19:26:26.015Z"
---

# Endpoint Lifecycle Management

**Endpoint Lifecycle Management** refers to the set of operations that govern a model serving endpoint from creation through potential deletion, including starting, stopping, updating, debugging, and managing permissions. On the Databricks platform, these operations are performed through the **Serving** UI, REST API, and SDKs.

## Endpoint Statuses

An endpoint's status indicates its current operational state and whether it can serve queries. The possible statuses are: ^[manage-model-serving-endpoints-databricks-on-aws.md]

- `Ready` — The endpoint is operational and can serve queries.
- `Ready (Update failed)` — The endpoint is still serving the previous configuration, but the latest attempted change failed.
- `Not ready (Updating)` — A configuration change is in progress; the endpoint cannot serve queries.
- `Not ready (Update failed)` — The latest change failed, and the endpoint cannot serve queries.
- `Not ready (Stopped)` — The endpoint has been intentionally stopped and cannot serve queries.

Readiness refers to whether the endpoint can process inference requests. An update failure indicates that the most recent modification to the endpoint's configuration was unsuccessful. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Stopping and Starting Endpoints

You can temporarily stop an endpoint and start it later. When an endpoint is stopped: ^[manage-model-serving-endpoints-databricks-on-aws.md]

- All provisioned resources are shut down.
- The endpoint cannot serve queries until started again.
- Only endpoints serving [custom models](/concepts/custom-mlflow-pythonmodel.md) with no in-progress updates can be stopped.
- Stopped endpoints do not count against resource quotas.
- Queries sent to a stopped endpoint return a 400 error. ^[manage-model-serving-endpoints-databricks-on-aws.md]

Starting a stopped endpoint creates a new configuration version with the same properties as the existing stopped configuration. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Deleting Endpoints

Deleting an endpoint permanently disables usage and removes all associated data. This operation cannot be undone. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Debugging Endpoints

Two types of logs are available to help debug issues: ^[manage-model-serving-endpoints-databricks-on-aws.md]

- **Model server container build logs** — Generated during endpoint initialization. These capture the setup phase including model download, dependency installation, and runtime environment configuration. Use these logs to debug startup failures or deployment stalls.
- **Model server logs** — Generated during runtime when the endpoint is actively serving predictions. These capture incoming requests, model inference execution, runtime errors, and application-level logging. Use these logs to debug prediction issues or query failures.

Both log types are accessible from the **Endpoints** UI in the **Logs** tab and through the REST API. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Permissions Management

You must have at least the **CAN MANAGE** permission on a serving endpoint to modify its permissions. When you update an endpoint, Databricks re-validates the recorded creator's workspace membership and served entity grants. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Serverless Usage Policies

If your workspace uses serverless usage policies for granular billing attribution, you can assign a policy to a model serving endpoint. During endpoint creation, select the policy from the **Usage policy** menu. If you have been assigned a serverless usage policy, all endpoints you create are automatically assigned that policy. ^[manage-model-serving-endpoints-databricks-on-aws.md]

For existing endpoints, users with **MANAGE** permissions can edit and add a serverless usage policy from the **Endpoint details** page. Note that existing endpoints are *not* automatically tagged with a user's assigned policy — manual updates are required. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Query Schema

A serving endpoint query schema is a formal description of the endpoint using the OpenAPI specification in JSON format. It contains the endpoint path, request and response body format, and data types for each field. This is helpful for reproducibility and for understanding endpoint requirements when you are not the original creator. ^[manage-model-serving-endpoints-databricks-on-aws.md]

To retrieve the schema, the served model must have a logged model signature and the endpoint must be in a `Ready` state. The response includes fields such as `openapi`, `info` (with the endpoint name), `servers` (base URL), and `paths` (supported request formats). The schema supports multiple input formats listed under a `oneOf` field. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md)
- [Foundation Model Serving](/concepts/foundation-model-serving-modes.md)
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)
- Model Serving Debugging
- [Serving Endpoint ACLs](/concepts/serving-endpoint-acls.md)
- OpenAPI Specification

## Sources

- manage-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [manage-model-serving-endpoints-databricks-on-aws.md](/references/manage-model-serving-endpoints-databricks-on-aws-7247257b.md)
