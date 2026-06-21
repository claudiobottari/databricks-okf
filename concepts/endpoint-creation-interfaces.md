---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 835217e2c648e7a9bd70e48fd052c85695461b21298c1f2ac3cc4a6b2c9a1cec
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-creation-interfaces
    - ECI
    - Endpoint Creation
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Creation Interfaces
description: "Three options for creating model serving endpoints: Serving UI (graphical), REST API, and MLflow Deployments SDK (programmatic)."
tags:
  - api
  - ui
  - mlflow
  - deployment
timestamp: "2026-06-19T09:37:22.351Z"
---

# Endpoint Creation Interfaces

**Endpoint Creation Interfaces** refer to the three methods provided by Databricks Model Serving for creating model serving endpoints that deploy and serve foundation models. Each interface offers a different level of abstraction and automation, allowing users to choose the approach that best fits their workflow.

## Overview

Model Serving supports serving foundation models via two categories: **external models** (hosted outside Databricks, e.g., OpenAI GPT-4, Anthropic Claude) and **Foundation Model APIs** (curated open models with pay-per-token or provisioned throughput). The creation interfaces apply to both categories, though the configuration details differ. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Creation Interfaces

Databricks provides the following three options for endpoint creation:

- **Serving UI** – A graphical interface within the Databricks workspace. Users navigate to the **Serving** tab, provide an endpoint name, select the entity (external model provider), configure provider‑specific secrets, choose a task (chat, completion, embeddings), and select the model name. After creation, the endpoint state appears as "Not Ready" until provisioning completes. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- **REST API** – Programmatic creation using the [Serving Endpoints API](https://docs.databricks.com/api/workspace/servingendpoints/updateconfig). Users send a JSON payload specifying the endpoint name and a `served_entities` list. For external models, the payload includes an `external_model` object with provider, task, and authentication secrets (e.g., OpenAI API key referenced via Databricks secrets). The REST API also supports updating endpoint configurations. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- **MLflow Deployments SDK** – A Python client library that simplifies endpoint management. To use it, install the MLflow Deployment client and instantiate a deploy client with `mlflow.deployments.get_deploy_client("databricks")`. The SDK abstracts the underlying REST API and can be used in notebooks and scripts. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Endpoint Types

The same interfaces can create endpoints for:

- **External model endpoints** – Serve models hosted outside Databricks, with centralized governance and rate limits. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- **Foundation Model API endpoints** – For pay-per-token models, Databricks auto‑creates endpoints; users access them via the Serving UI. For provisioned throughput (fine‑tuned variants), users create endpoints via the REST API. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- **Custom model serving endpoints** – For traditional ML or Python models; the process is documented separately. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Updating Endpoints

All three interfaces support updating an endpoint’s compute configuration. During an update, the old configuration continues serving traffic until the new one is ready. Only the Serving UI provides a **Cancel update** button to abort an in‑progress change. Additional update restrictions apply to endpoints with an `external_model` (cannot be removed once present). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [External Models](/concepts/external-models.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md)
- [AI Gateway-enabled inference tables](/concepts/ai-gateway-inference-tables.md)
- [Custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md)

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
