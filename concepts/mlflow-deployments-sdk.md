---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30f7992aaea9c0797db9f9614ef8ef070a7b198f9f5496577ccdfebee7401443
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-deployments-sdk
    - MDS
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: MLflow Deployments SDK
description: A Python SDK (mlflow.deployments) for programmatically creating and managing model serving endpoints on Databricks.
tags:
  - model-serving
  - databricks
  - mlflow
  - sdk
timestamp: "2026-06-19T14:38:01.619Z"
---

# MLflow Deployments SDK

The **MLflow Deployments SDK** is a client library that allows programmatic creation and management of model serving endpoints on Databricks. It provides a unified interface for deploying both foundation models and external models through the Databricks Model Serving infrastructure.

## Overview

The MLflow Deployments SDK enables you to create, update, and manage model serving endpoints using Python code rather than the UI or REST API directly. It is part of the larger MLflow ecosystem and integrates with the Databricks deployment workflow. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Installation and Setup

To use the MLflow Deployments SDK, you must install the MLflow Deployment client and create a deployment client configured for Databricks:

```python
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")
```

^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Capabilities

### Creating Foundation Model Serving Endpoints

The SDK supports creating endpoints that serve foundation models, including both pay-per-token and provisioned throughput models available through Foundation Model APIs. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Creating External Model Serving Endpoints

You can create endpoints that query foundation models hosted outside of Databricks using the [External Models](/concepts/external-models.md) framework. This includes models from providers like OpenAI and Anthropic. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Updating Endpoint Configurations

The SDK allows you to update the compute configuration of existing endpoints. While a new configuration is being deployed, the old configuration continues serving prediction traffic. It is not possible to make another update while one is in progress. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Querying Endpoints

After creating endpoints, you can use the SDK to send inference requests and receive responses from the deployed models.

## Comparison with Other Methods

| Method | Description |
|--------|-------------|
| **Serving UI** | Create and manage endpoints through the Databricks workspace UI |
| **REST API** | Direct HTTP API calls for endpoint management |
| **MLflow Deployments SDK** | Python client abstraction over the REST API |

All three methods provide equivalent functionality for endpoint creation and management. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

- Use the SDK for automated deployment pipelines and CI/CD workflows.
- For endpoints with `external_model` configurations, the served entities list can only contain one `served_entity` object.
- Endpoints created without an `external_model` cannot be updated to add one, and vice versa.
- Consider using [AI Gateway-enabled inference tables](/concepts/ai-gateway-inference-tables.md) alongside the SDK for comprehensive governance and observability.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The underlying infrastructure that hosts and serves models
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Pre-configured endpoints for base models with pay-per-token pricing
- [External Models](/concepts/external-models.md) — Foundation models hosted outside Databricks, managed through the SDK
- [Create Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — For traditional ML or Python models
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Performance-guaranteed deployment for production workloads

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
