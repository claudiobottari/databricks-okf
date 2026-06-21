---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: caaaad2522a3c139a79ec50d2113205c24a114b56b9b4c34863667154b79c920
  pageDirectory: concepts
  sources:
    - migrate-to-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-endpoints-databricks
    - SE(
  citations:
    - file: migrate-to-model-serving-databricks-on-aws.md
title: Serving Endpoints (Databricks)
description: REST API endpoints for Databricks Model Serving that use a 'serving-endpoints' URL path, with full API support for creation, configuration, and lifecycle management.
tags:
  - api
  - endpoints
  - model-serving
timestamp: "2026-06-19T19:35:35.537Z"
---

# Serving Endpoints (Databricks)

**Serving Endpoints (Databricks)** refers to the production-ready model serving experience built on serverless compute that replaces the legacy MLflow Model Serving. Starting August 22, 2025, customers can no longer create new serving endpoints using the legacy experience, and on September 15, 2025, the legacy service reaches end of life and all existing endpoints become unusable. ^[migrate-to-model-serving-databricks-on-aws.md]

## Overview

Model Serving endpoints allow you to deploy registered MLflow models as scalable REST APIs. The new Model Serving experience is built on [serverless compute](/concepts/serverless-gpu-compute.md) and is backed by the Databricks SLA. It provides full support for managing resources via API workflows, a new endpoint URL format (`serving-endpoints` instead of `model`), and a slightly different request/response protocol compared to the legacy service. ^[migrate-to-model-serving-databricks-on-aws.md]

## Requirements

- A registered model in the [MLflow Model Registry](/concepts/mlflow-model-registry.md).
- Appropriate permissions on the registered models as described in the access control guide for serving endpoints.
- Serverless compute must be enabled on the workspace. ^[migrate-to-model-serving-databricks-on-aws.md]

## Significant Changes from Legacy MLflow Model Serving

| Aspect | Legacy MLflow Model Serving | New Model Serving |
|--------|-----------------------------|-------------------|
| Request/response protocol | Original format | Different format; see [scoring a model endpoint](/concepts/foundation-model-serving-endpoints.md) for details |
| Endpoint URL | Includes `/model` | Includes `/serving-endpoints` |
| Resource management | Limited | Full support via API workflows |
| Production readiness | No SLA | Production-ready with Databricks SLA |

^[migrate-to-model-serving-databricks-on-aws.md]

## Migration from Legacy MLflow Model Serving

### Identifying Legacy Endpoints

To find endpoints still using the legacy service:

1. Go to the **Models** UI in your workspace.
2. Select the **Workspace Model Registry** filter.
3. Select the **Legacy serving enabled only** filter.

^[migrate-to-model-serving-databricks-on-aws.md]

### Migrating Served Models

The recommended migration path is to create new Model Serving endpoints and transition application traffic without immediately disabling the legacy endpoint. Steps:

1. Register your model to [Unity Catalog](/concepts/unity-catalog.md).
2. Navigate to **Serving endpoints** in the workspace sidebar.
3. Follow the workflow in create custom model serving endpoints to create a new endpoint with your model.
4. Update your application to use the new endpoint URL and scoring format.
5. After transition, navigate to **Models** in the sidebar, select the model, go to the **Serving** tab, click **Stop**, and confirm.

^[migrate-to-model-serving-databricks-on-aws.md]

### Migrating Deployed Model Versions (Stage-Based)

Previously, serving endpoints were created based on the model version stage (`Staging` or `Production`). To replicate this behavior:

1. Create two endpoints for the same registered model—one for staging versions, one for production versions—using the Serving Endpoints API.

   **Staging endpoint example:**
   ```bash
   POST /api/2.0/serving-endpoints
   {
       "name": "modelA-Staging",
       "config": {
           "served_entities": [
               {
                   "entity_name": "model-A",
                   "entity_version": "2",
                   "workload_size": "Small",
                   "scale_to_zero_enabled": true
               }
           ]
       }
   }
   ```

   **Production endpoint example:**
   ```bash
   POST /api/2.0/serving-endpoints
   {
       "name": "modelA-Production",
       "config": {
           "served_entities": [
               {
                   "entity_name": "model-A",
                   "entity_version": "1",
                   "workload_size": "Small",
                   "scale_to_zero_enabled": true
               }
           ]
       }
   }
   ```

2. Verify endpoint status with `GET /api/2.0/serving-endpoints/{endpoint_name}`.
3. Query the endpoint using `POST /serving-endpoints/{endpoint_name}/invocations`.
4. Update the endpoint configuration when model versions transition between stages using `PUT /api/2.0/serving-endpoints/{endpoint_name}/config`.

^[migrate-to-model-serving-databricks-on-aws.md]

## Related Concepts

- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Serverless Compute
- Access Control for Serving Endpoints
- [Scoring a model endpoint](/concepts/foundation-model-serving-endpoints.md)
- [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md)

## Sources

- migrate-to-model-serving-databricks-on-aws.md

# Citations

1. [migrate-to-model-serving-databricks-on-aws.md](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
