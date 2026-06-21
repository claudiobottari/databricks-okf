---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d982e41fe1f5bde504edeaa8238bbd5076472a12ce7be6614690f26ff78845e0
  pageDirectory: concepts
  sources:
    - manage-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-server-debugging-logs
    - MSDL
    - Model server logs
  citations:
    - file: manage-model-serving-endpoints-databricks-on-aws.md
title: Model Server Debugging Logs
description: "Two types of logs for troubleshooting model serving endpoints: container build logs (initialization phase) and model server logs (runtime phase)."
tags:
  - model-serving
  - debugging
  - logging
  - databricks
timestamp: "2026-06-19T19:25:52.529Z"
---

#Model Server Debugging Logs

**Model Server Debugging Logs** are diagnostic logs provided by Databricks Model Serving to help investigate issues with model serving endpoints. Two distinct types of logs are available: container build logs and model server runtime logs. Both log types can be accessed from the **Serving** UI or programmatically through the REST API. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Types of Logs

### Model Server Container Build Logs

Container build logs are generated during endpoint initialization when the container is being created. They capture the setup phase, including downloading the model, installing dependencies, and configuring the runtime environment. Use these logs to debug why an endpoint failed to start or is stuck during deployment. ^[manage-model-serving-endpoints-databricks-on-aws.md]

### Model Server Logs

Model server logs are generated during runtime when the endpoint is actively serving predictions. They capture incoming requests, model inference execution, runtime errors, and application-level logging from your model code. Use these logs to debug issues with predictions or investigate query failures. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Accessing Logs

Both log types are accessible from the **Endpoints** UI in the **Logs** tab. They can also be retrieved programmatically via the REST API:

- **Build logs:** `GET /api/2.0/serving-endpoints/{name}/served-models/{served-model-name}/build-logs`
- **Server logs:** `GET /api/2.0/serving-endpoints/{name}/served-models/{served-model-name}/logs`

Both API endpoints accept an optional `config_version` parameter. For more details, see the Debugging guide for Model Serving. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — Overview of deploying models on Databricks.
- [Serving Endpoints](/concepts/serving-endpoint-acls.md) — The REST API for managing endpoints.
- [Serving UI](/concepts/serving-ui.md) — The user interface for monitoring endpoints.
- Custom Models — Models deployed via MLflow or custom containers.
- [Foundation Model Serving Endpoints](/concepts/foundation-model-serving-endpoints.md) — Managed endpoints for foundation models.
- Debugging guide for Model Serving — Extended troubleshooting documentation.

## Sources

- manage-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [manage-model-serving-endpoints-databricks-on-aws.md](/references/manage-model-serving-endpoints-databricks-on-aws-7247257b.md)
