---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4a95990e8306d771da04336b9238ac691c97b83f94229735538035e605c133e
  pageDirectory: concepts
  sources:
    - migrate-to-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-migration
    - MSM
    - Model Version Migration
  citations:
    - file: migrate-to-model-serving-databricks-on-aws.md
title: Model Serving Migration
description: The process of transitioning from Legacy MLflow Model Serving to the new Model Serving experience, including URL changes, scoring format changes, and endpoint reconfiguration.
tags:
  - migration
  - model-serving
  - databricks
timestamp: "2026-06-19T19:35:36.155Z"
---

Here is the wiki page for "Model Serving Migration".

---

## Model Serving Migration

**Model Serving Migration** refers to the process of transitioning machine learning model deployments from the Legacy MLflow Model Serving experience to the newer Databricks Model Serving, which is built on serverless compute. This migration is mandatory due to a scheduled end-of-life for the legacy service. ^[migrate-to-model-serving-databricks-on-aws.md]

### Background and Mandate

Databricks announced that starting August 22, 2025, users will no longer be able to create new serving endpoints using the Legacy MLflow Model Serving experience. On September 15, 2025, the legacy experience will reach end of life, and all existing endpoints using this service will no longer be functional. ^[migrate-to-model-serving-databricks-on-aws.md]

### Prerequisites

Before beginning the migration, ensure the following requirements are met:

- A registered model in the MLflow [Model Registry](/concepts/mlflow-model-registry.md).
- Appropriate permissions on the registered models, as described in the access control guide for [Serving Endpoints](/concepts/serving-endpoint-acls.md).
- Serverless compute is enabled on the workspace. ^[migrate-to-model-serving-databricks-on-aws.md]

### Key Differences Between Legacy and New Model Serving

The new Model Serving experience introduces several significant changes compared to the legacy version:

- **Request/Response Format:** The format of the request to the endpoint and the response from the endpoint are slightly different. Users should consult the documentation on [scoring a model endpoint](/concepts/foundation-model-serving-endpoints.md) for details on the new format protocol. ^[migrate-to-model-serving-databricks-on-aws.md]
- **Endpoint URL:** The endpoint URL now includes `serving-endpoints` instead of `model`. ^[migrate-to-model-serving-databricks-on-aws.md]
- **API Workflows:** Model Serving includes full support for managing resources with API workflows. ^[migrate-to-model-serving-databricks-on-aws.md]
- **Production Readiness:** Model Serving is production-ready and backed by the Databricks Service Level Agreement (SLA). ^[migrate-to-model-serving-databricks-on-aws.md]

### Identifying Legacy Endpoints

To identify serving endpoints that still use the Legacy MLflow Model Serving experience:

1.  Navigate to the **Models** UI in your workspace.
2.  Select the **Workspace Model Registry** filter.
3.  Select the **Legacy serving enabled only** filter.

### Migration Steps for Served Models

The following process allows you to flexibly transition model serving workflows without immediately disabling the legacy service.

1.  Register your model to [Unity Catalog](/concepts/unity-catalog.md).
2.  Navigate to **Serving endpoints** on the sidebar of your machine learning workspace.
3.  Create a new serving endpoint with your model.
4.  Transition your application to use the new URL provided by the serving endpoint and the new scoring format.
5.  After confirming that the new endpoint is fully operational, navigate to **Models** on the sidebar of your workspace.
6.  Select the model for which you want to disable Legacy MLflow Model Serving.
7.  On the **Serving** tab, select **Stop**.
8.  Confirm by selecting **Stop Serving** in the message that appears. ^[migrate-to-model-serving-databricks-on-aws.md]

### Migration Steps for Deployed Model Versions

In the legacy experience, the serving endpoint was created based on the registered model version's stage (e.g., `Staging` or `Production`). You can replicate this behavior in the new Model Serving experience by creating separate endpoints for each stage.

The following example uses the Serving Endpoints API. For a registered model named `modelA` with version 1 in `Production` and version 2 in `Staging`:

1.  **Create two endpoints**:
    - For `Staging`: Create an endpoint named `modelA-Staging` pointing to version 2.
    - For `Production`: Create an endpoint named `modelA-Production` pointing to version 1.

2.  **Verify** the status of both endpoints using `GET /api/2.0/serving-endpoints/{endpoint_name}`.

3.  **Query** the endpoints using the new format:
    - `POST /serving-endpoints/modelA-Staging/invocations`
    - `POST /serving-endpoints/modelA-Production/invocations`

4.  **Update** endpoints based on model version transitions. When a new version (e.g., version 3) is created and stages change, use the `PUT /api/2.0/serving-endpoints/{endpoint_name}/config` API to update the `entity_version` for each endpoint accordingly. For example, update `modelA-Production` to serve version 2 when it transitions from `Staging` to `Production`.

### Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [Legacy MLflow Model Serving](/concepts/legacy-mlflow-model-serving.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Serving Endpoints API
- Serverless Compute

### Sources

- migrate-to-model-serving-databricks-on-aws.md

# Citations

1. [migrate-to-model-serving-databricks-on-aws.md](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
