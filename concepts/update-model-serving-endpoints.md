---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71f9db7890d0e5d08d927c8f294fff507156dbc2146d8121ce20e299fd22f4ee
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - update-model-serving-endpoints
    - UMSE
    - Create model serving endpoints
    - Manage model serving endpoints
    - Manage Permissions on a Model Serving Endpoint
    - deploy the model to a serving endpoint
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Update Model Serving Endpoints
description: Process and constraints for updating model serving endpoint configurations, including compute configuration changes and the rule that external_model endpoints cannot be converted to or from non-external_model types.
tags:
  - model-serving
  - configuration
  - update
timestamp: "2026-06-19T18:01:56.088Z"
---

# Update Model Serving Endpoints

**Update Model Serving Endpoints** refers to the process of modifying the configuration of an existing model serving endpoint after it has been created. This allows you to adjust compute resources, swap served model versions, or change external model provider settings while minimising downtime.

## How Updates Work

After a model endpoint is enabled, you can adjust its compute configuration—such as workload size—to allocate more or fewer resources for serving the model. Until the new configuration is fully ready, the old configuration continues to serve prediction traffic, ensuring no interruption in service. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

Only one configuration update can be in progress at a time. While an update is ongoing, a second update request is rejected. In the Serving UI, you can cancel an in-progress configuration update by selecting **Cancel update** on the top right of the endpoint's details page. This cancellation feature is available only in the Serving UI. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Constraints When Using External Models

When an [External Model](/concepts/external-models.md) (a foundation model hosted outside Databricks) is part of the endpoint configuration, the endpoint’s served entities list can contain **only one** `served_entity` object. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

Two important restrictions apply to endpoints that include or exclude `external_model`:

- An endpoint that was created with an `external_model` **cannot** be updated to remove that external model (i.e., switch to a Databricks-hosted foundation or custom model).
- An endpoint that was created **without** an `external_model` **cannot** be updated to add one. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

These constraints mean that the decision to use external models must be made at endpoint creation time and cannot be changed later without creating a new endpoint.

## Methods for Updating

Updates can be performed through:

- **REST API** – Use the [Serving Endpoints update configuration API](https://docs.databricks.com/api/workspace/servingendpoints/updateconfig). The request body includes the endpoint name and the desired `served_entities` array. See the REST API documentation for full request and response schema details. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- **MLflow Deployments SDK** – Use the `mlflow.deployments` client to call the update methods programmatically. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

The Serving UI also supports updating the endpoint’s compute configuration and served entity selection interactively.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The platform that hosts and serves models.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Pre‑built endpoints for pay‑per‑token and provisioned throughput models.
- [External Models](/concepts/external-models.md) – Foundation models hosted outside Databricks.
- [Serving UI](/concepts/serving-ui.md) – Web interface for managing serving endpoints.
- REST API for Serving Endpoints – Programmatic control over endpoint lifecycle.
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) – Python SDK for deploying and managing endpoints.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
