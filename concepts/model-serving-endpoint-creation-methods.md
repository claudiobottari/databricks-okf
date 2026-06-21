---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a62b461b3bdcc5e9e51d734e23ee9db5a8d46665c6393e75af19b5f5a5faea1d
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-creation-methods
    - MSECM
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Creation Methods
description: "Three ways to create model serving endpoints in Databricks: the Serving UI, REST API, and MLflow Deployments SDK."
tags:
  - model-serving
  - api
  - databricks
timestamp: "2026-06-19T18:01:43.441Z"
---

# Model Serving Endpoint Creation Methods

**Model Serving Endpoint Creation Methods** refers to the three options available on Databricks for creating and deploying model serving endpoints that serve foundation models, external models, and traditional ML or Python models. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Overview

Model Serving on Databricks supports three main categories of models: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- **External models**: Foundation models hosted outside of Databricks (e.g., OpenAI's GPT-4, Anthropic's Claude) that can be centrally governed with rate limits and access control.
- **Foundation Model APIs**: State-of-the-art open foundation models (e.g., Meta-Llama-3.3-70B-Instruct, GTE-Large) made available by Databricks with optimized inference. These offer **pay-per-token** pricing for base models and **provisioned throughput** for production workloads.
- **Custom ML/Python models**: Traditional machine learning or Python models served via [custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md).

## Creation Methods

Model Serving provides three options for endpoint creation: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

1. **The Serving UI** — A graphical interface in the Databricks workspace.
2. **REST API** — Programmatic creation via the Databricks API for both foundation model and external model endpoints.
3. **MLflow Deployments SDK** — Python SDK for creating and managing endpoints.

### Requirements

- A Databricks workspace must be in a supported region for both Foundation Model APIs and external models. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- For MLflow Deployments SDK usage, install the MLflow Deployment client: `import mlflow.deployments; client = mlflow.deployments.get_deploy_client("databricks")` ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Creating Foundation Model Serving Endpoints

### Via Foundation Model APIs

For **provisioned throughput** endpoints, create them using the [REST API for provisioned throughput](/concepts/provisioned-throughput.md). For **pay-per-token** endpoints, Databricks automatically provides pre-configured endpoints in the workspace under the **Serving** tab in the left sidebar. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Via External Models

When creating an endpoint for an external model (e.g., a provider like OpenAI), the process involves: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

1. Naming the endpoint.
2. In the **Served entities** section, select **Foundation models**, then choose the model provider from the **External model providers** list.
3. Provide configuration details — typically a secret referencing a [personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) for authentication.
4. Select the **task** (chat, completion, or embeddings) and the specific external model.
5. Click **Create**. The endpoint will initially show a state of **Not Ready**.

## Updating Endpoints

After enabling a model endpoint, you can adjust the compute configuration (workload size) as needed. Until the new configuration is ready, the old configuration continues serving prediction traffic. While an update is in progress, no other update can be made. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Restrictions

- If an `external_model` is present in the endpoint configuration, the served entities list can only contain one object. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- Existing endpoints with an `external_model` cannot be updated to remove it. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- Endpoints created without an `external_model` cannot be updated to add one. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — Core service for deploying and serving models.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Optimized inference for curated foundation models.
- [External Models](/concepts/external-models.md) — Third-party hosted foundation models.
- [Serving UI](/concepts/serving-ui.md) — Graphical interface for endpoint management.
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) — Python SDK for endpoint creation.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Performance guarantees for production workloads.
- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — Endpoints for traditional ML/Python models.
- Rate Limits and Access Control — Governance for external model endpoints.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
