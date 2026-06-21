---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aee81fd10ed509c19e298d5cb397fbf8f22d5b418470fdf91fe3ac89d385baa8
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple-served-entities-per-endpoint
    - MSEPE
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Multiple Served Entities per Endpoint
description: A single serving endpoint can serve multiple models or model versions with configurable traffic splits between them.
tags:
  - model-serving
  - traffic-routing
timestamp: "2026-06-18T11:22:40.538Z"
---

---
title: Multiple Served Entities per Endpoint
summary: Serving multiple models or model versions from a single serving endpoint with configurable traffic splits, compute, and environment settings per entity.
sources:
  - create-custom-model-serving-endpoints-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:00:00.000Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - model-serving
  - custom-models
  - deployment
aliases:
  - multiple-models-per-endpoint
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Multiple Served Entities per Endpoint

**Multiple Served Entities per Endpoint** is a feature of Databricks [Model Serving](/concepts/model-serving.md) that allows you to serve two or more [custom models](/concepts/custom-mlflow-pythonmodel.md) or model versions from a single serving endpoint. Each served entity can have its own compute configuration, traffic routing percentage, and advanced settings such as instance profiles and environment variables. This enables scenarios like canary deployments, A/B testing, or serving different model versions side‑by‑side.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Use Cases

- **Canary deployments**: Route a small percentage of traffic to a new model version while the majority continues to use the stable version.
- **A/B experimentation**: Compare the performance of two model variants on live traffic.
- **Multi‑purpose endpoints**: Serve different models (e.g., different task types) through a single endpoint, each with its own compute profile.

## Creating an Endpoint with Multiple Served Entities

### Using the Serving UI

When you create a custom model serving endpoint through the **Serving** UI:

1. Under **Served entities**, configure the first entity by selecting the model and model version, setting the traffic percentage, compute size, scale‑out, and advanced options.
2. Click **Add served entity** to add another entity.
3. Repeat the configuration steps for each additional entity.
4. The traffic percentages you assign must sum to 100% across all served entities.
5. Click **Create**.

This process is described in the endpoint creation workflow.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Using the REST API or MLflow Deployments SDK

Both the REST API and the MLflow Deployments SDK accept a list of served entities when creating or updating an endpoint. Each entry in the list specifies:
- `entity_name` (e.g., the registered model name and version in Unity Catalog or Workspace Model Registry)
- `workload_type` / `workload_size`
- `scale_to_zero_enabled`
- `traffic_percentage` (must sum to 100)
- Optional properties: `environment_vars`, `instance_profile_arn`, `name` (a friendly label)

The exact API payloads and SDK examples are documented in the REST API and SDK sections of the source.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Traffic Splitting

The endpoint routes requests to the served entities according to the defined traffic percentages. This is a weighted random split, not content‑based routing. The split is applied at inference time; each request is assigned to one entity.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Per‑Entity Configuration

Each served entity can be independently configured with:

- **Compute type**: CPU or GPU workload types.
- **Compute scale‑out**: Small (0–4 concurrent requests), Medium (8–16), or Large (16–64).
- **Scale to zero**: Whether the entity scales down to zero when idle (not recommended for production).
- **Instance profile**: An IAM role for accessing AWS resources.
- **Environment variables**: For connecting to resources or logging feature lookup DataFrames.
- **Custom name**: A label that appears in endpoint responses.

These settings are set per entity during creation or update.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Identity and Access Considerations

The endpoint's **recorded creator** (the identity that created the endpoint) must have the necessary Unity Catalog grants on *each* served entity. If you update the endpoint to add a new served entity, the creator must possess the required grants for that entity at the time of the update; otherwise the request fails with `PERMISSION_DENIED`. The same validation applies to configuration updates that modify existing entities.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

Because the creator identity cannot be changed after endpoint creation, it is recommended to use a long‑lived service principal that has all the grants needed for all served entities you plan to deploy.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Updating an Endpoint with Multiple Entities

You can modify the set of served entities, their configuration, and traffic splits after the endpoint is created. During an update:

- The existing configuration continues serving traffic until the new configuration is ready.
- Only one update can be in progress at a time (an in‑progress update can be cancelled from the UI).
- Update failures do not affect the current active configuration.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Custom Models in Model Serving](/concepts/custom-models-on-model-serving.md) – The types of models that can be served.
- [Create Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) – Full endpoint creation workflow.
- [Route Optimization for Serving Endpoints](/concepts/route-optimization-for-serving-endpoints.md) – Performance optimization for high QPS endpoints.
- [AI Gateway](/concepts/ai-gateway.md) – Governance features that can be applied to the endpoint.
- [Serving Endpoint Permissions](/concepts/serving-endpoint-acls.md) – Access control model for endpoints.
- Canary Deployment Strategies – Broader pattern of phased rollouts.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
