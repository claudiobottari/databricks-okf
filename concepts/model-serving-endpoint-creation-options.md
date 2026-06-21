---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb1e0fcd1b1331e3e8d85fafc137523ad38df932dd9c9b5fc9e4b59dd574d18c
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-creation-options
    - MSECO
    - Model Serving Endpoint Creation
    - model-serving-endpoint-creation-methods
    - MSECM
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Creation Options
description: "Three methods to create model serving endpoints: Serving UI, REST API, and MLflow Deployments SDK."
tags:
  - databricks
  - api
  - ui
  - mlflow
timestamp: "2026-06-18T11:23:38.172Z"
---

# Model Serving Endpoint Creation Options

**Model Serving Endpoint Creation Options** refers to the three distinct interfaces available in Databricks for creating and deploying model serving endpoints: the Serving UI, the REST API, and the MLflow Deployments SDK. These options support both foundation models (including external models hosted outside Databricks and models available through Foundation Model APIs) and custom machine learning models.

## Overview

Model Serving in Databricks provides three methods for creating model serving endpoints, each suited to different use cases and user preferences: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- **The Serving UI** — A graphical interface in the Databricks workspace for creating and managing endpoints.
- **REST API** — A programmatic interface for creating and updating endpoints via HTTP requests.
- **MLflow Deployments SDK** — A Python SDK for creating endpoints programmatically within MLflow workflows.

## Supported Model Types

Model Serving supports two categories of models: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

1. **Foundation models** — State-of-the-art models available through Foundation Model APIs, including both pay-per-token and provisioned throughput options.
2. **External models** — Foundation models hosted outside Databricks, such as OpenAI's GPT-4 and Anthropic's Claude, which can be centrally governed with rate limits and access control.

For traditional ML or Python models, see [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Requirements

All endpoint creation methods require: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- A Databricks workspace in a supported region.
- For MLflow Deployments SDK: installation of the MLflow Deployment client.

## Creating Endpoints

### Using the REST API

The REST API provides a programmatic interface for creating and updating serving endpoints. It supports JSON payloads for endpoint configuration. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Using the MLflow Deployments SDK

The MLflow Deployments SDK provides a Python-based approach for creating endpoints, requiring `mlflow.deployments.get_deploy_client("databricks")`. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Foundation Model API Endpoints

For foundation models available through Foundation Model APIs with pay-per-per-token pricing, Databricks automatically provides specific endpoints. These can be accessed through the **Serving** tab in the workspace sidebar. For provisioned throughput endpoints, see [Create provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## External Model Endpoints

### Creating External Model Endpoints

When creating an external model endpoint: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

1. Provide a name for the endpoint.
2. In the Served entities section, select **Foundation models**.
3. Select the model provider from **External model providers**.
4. Configure access details (typically a [personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) secret).
5. Select the task (chat, completion, or embeddings).
6. Select the external model name based on task selection.

The endpoint state initially shows as **Not Ready**. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Update Constraints

When an `external_model` is present in an endpoint configuration: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- The served entities list can only contain one entity.
- Existing endpoints with `external_model` cannot be updated to remove it.
- Endpoints created without `external_model` cannot be updated to add one.

## Update Process

While a configuration update is in progress: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- The old configuration continues serving prediction traffic.
- No other update can be made until the current one completes.
- In the Serving UI, updates can be cancelled.

## Related Concepts

- [Model Serving Architecture](/concepts/model-serving-patterns.md) — The underlying infrastructure for model deployment
- Serving Endpoint State Management — How endpoints transition between states
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Pre-built API endpoints for foundation models
- External Model Governance — Rate limiting and access control for external models
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Performance guarantees for production workloads
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Cost control for serverless model serving

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
