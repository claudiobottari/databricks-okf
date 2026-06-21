---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c4422ab8d346a6976dc32e9a555b1efe8cdd0a49a36270b1957c66193c45960
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-model-endpoint-constraints
    - EMEC
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: External Model Endpoint Constraints
description: "Restrictions on external model endpoints: only one served_entity per endpoint when external_model is present, and external_model cannot be added or removed after creation."
tags:
  - databricks
  - external-models
  - constraints
timestamp: "2026-06-18T11:24:12.230Z"
---

# External Model Endpoint Constraints

**External Model Endpoint Constraints** are the operational limits and configuration rules that apply when creating, updating, or managing model serving endpoints for [External Models](/concepts/external-models.md) — foundation models hosted outside of Databricks, such as OpenAI's GPT-4 or Anthropic's Claude. These constraints, enforced by the [Model Serving](/concepts/model-serving.md) system, govern the structure of endpoint configurations and how they can evolve over time. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Single Served Entity Constraint

When an endpoint configuration includes an `external_model`, the served entities list can contain only one `served_entity` object. This restriction exists because external models are served through a provider-specific gateway rather than through Databricks-hosted model replicas, and the system does not support multiplexing multiple external providers behind a single endpoint. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Immutability of External Model Presence

Two immutability rules apply to endpoints that use or have ever used an external model:

1. **Irreversibility**: If an endpoint is created with an `external_model` in its configuration, it cannot be updated to remove the `external_model`. Once an external model is part of an endpoint's served entities, that endpoint is permanently tied to an external model provider. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

2. **No retroactive addition**: If an endpoint is created *without* an `external_model` (for example, as a [custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md) for a traditional ML or Python model), it cannot later be updated to add an `external_model`. External model endpoints are created from the start as such; they cannot be converted from another endpoint type. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

These constraints mean that the decision to use an external model vs. a Databricks-hosted model must be made at endpoint creation time and cannot be changed afterward.

## Update Behavior Constraints

Until a new configuration is ready, the old configuration continues serving prediction traffic. While an update is in progress, another update cannot be made. In the [Serving UI](/concepts/serving-ui.md), you can cancel an in-progress configuration update by selecting **Cancel update** on the top right of the endpoint's details page. This functionality is only available in the Serving UI. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Endpoint Creation Options

Clients can create external model serving endpoints through:

- The **Serving UI** — where users select "Foundation models" under "External model providers" and provide configuration details such as the secret referencing the [personal access token](/concepts/databricks-personal-access-token-pat-authentication.md).
- The **REST API** — using the Serving Endpoints API with an `external_model` block in the request body.
- The **MLflow Deployments SDK** — requiring installation of the MLflow Deployment client (`pip install mlflow`; `mlflow.deployments.get_deploy_client("databricks")`).

Supported tasks for external model endpoints are `chat`, `completion`, and `embeddings`. The model provider and model name must be specified in the endpoint configuration. Available models are listed under [external model providers](/concepts/external-models.md). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [External Models](/concepts/external-models.md) — Foundation models hosted outside Databricks, governed by these constraints
- [Model Serving](/concepts/model-serving.md) — The system that enforces external model endpoint configuration rules
- Serving Endpoints API — The REST API used to create and update endpoints
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Performance-guaranteed serving for production workloads
- [Pay-per-Token](/concepts/pay-per-token-serving-mode.md) — Pricing model for base model API access
- Workload Size and Compute Configuration — The resource allocation that affects endpoint performance

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
