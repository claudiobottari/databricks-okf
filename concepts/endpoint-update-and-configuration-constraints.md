---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43b1faa4e7488da07396a303a35808977c6d2d405f11c20e6474d39cb9899c12
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-update-and-configuration-constraints
    - Configuration Constraints and Endpoint Update
    - EUACC
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Update and Configuration Constraints
description: Rules governing updates to model serving endpoints, including compute configuration changes, the inability to add/remove external_model from an endpoint, and cancellation of in-progress updates.
tags:
  - model-serving
  - configuration
  - operations
timestamp: "2026-06-18T14:55:11.203Z"
---

# Endpoint Update and Configuration Constraints

**Endpoint Update and Configuration Constraints** refers to the rules and limitations that govern how a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) can be modified after creation, particularly regarding the presence or absence of an `external_model` in its served entity list. These constraints ensure safe transitions and prevent invalid configurations.

## Update Process

After a foundation model serving endpoint has been created, you can adjust its compute configuration (e.g., workload size) to allocate more or fewer resources for serving the model. The update is performed gradually: the old configuration continues to serve prediction traffic until the new configuration is ready.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

Only one configuration update can be in progress at a time. If an update is already underway, a subsequent update attempt will be rejected until the current one completes or is cancelled.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

Updates can be initiated via:

- The **Serving UI** (manual configuration change)
- The **REST API** (using the [update configuration](https://docs.databricks.com/api/workspace/servingendpoints/updateconfig) endpoint)
- The **MLflow Deployments SDK** (via `mlflow.deployments` client)^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Configuration Constraints

The most important constraints relate to the `external_model` property within the endpoint’s `served_entities` list:

1. **Single served entity when using `external_model`**: If an endpoint’s configuration includes an `external_model` (i.e., a model hosted outside Databricks such as OpenAI GPT-4 or Anthropic Claude), the `served_entities` list can contain at most one object. You cannot add additional served entities alongside an external model.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

2. **Immutability of `external_model` presence**:  
   - An endpoint created *with* an `external_model` cannot later be updated to remove that `external_model`. The external model type cannot be replaced by a Databricks-hosted or custom model.  
   - Conversely, an endpoint created *without* an `external_model` (e.g., serving a custom Python model or a foundation model via provisioned throughput) cannot be updated to *add* an `external_model` later.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

These constraints are enforced to maintain clarity of endpoint semantics and avoid runtime mismatch between the endpoint’s routing logic and the model provider.

## Canceling Updates

If an update is in progress and you wish to abort it, the **Serving UI** provides a **Cancel update** button on the endpoint’s details page (top right). This functionality is only available through the UI—there is no REST API or SDK method to cancel an update programmatically.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Overview of the model serving platform on Databricks.
- [External Models](/concepts/external-models.md) – Foundation models hosted outside Databricks.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Pay-per-token and provisioned throughput endpoints for curated models.
- Create Foundation Model Serving Endpoints – The creation process that precedes any update.
- [Serving UI](/concepts/serving-ui.md) – The web interface for managing endpoints.
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) – Python SDK for deploying and updating endpoints.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
