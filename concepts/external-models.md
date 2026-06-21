---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0816621ba85a71323132a39e0592be40dbac9975196d600caf613a921a4143fe
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - external-models
    - External Model
    - external model
    - Databricks External Models
    - External models regions
    - LiteLLMModel
    - available external models
    - external model providers
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: External Models
description: Foundation models hosted outside Databricks (e.g., GPT-4, Claude) served through Databricks endpoints with centralized governance, rate limits, and access control.
tags:
  - model-serving
  - external-models
  - governance
timestamp: "2026-06-19T18:01:46.001Z"
---

---

title: External Models
summary: Foundation models hosted outside of Databricks (e.g., GPT-4, Claude) that can be centrally governed with rate limits and access control via Databricks serving endpoints.
sources:
  - create-foundation-model-serving-endpoints-databricks-on-aws.md
  - deploy-models-using-model-serving-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:59:06.312Z"
updatedAt: "2026-06-19T14:38:04.881Z"
tags:
  - model-serving
  - databricks
  - external-models
  - governance
aliases:
  - external-models
confidence: 1
provenanceState: merged
inferredParagraphs: 0
---

# External Models

**External Models** are foundation models hosted outside of Databricks—such as OpenAI's GPT‑4 and Anthropic's Claude—that are accessed through Databricks [Model Serving](/concepts/model-serving.md) endpoints. These endpoints enable centralized governance, rate‑limiting, and access control, allowing organizations to manage multiple LLM providers from a single platform. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Overview

External models are one of three serving options for foundation models on Databricks, alongside Databricks‑hosted models (via Foundation Model APIs) and custom MLflow models. Model Serving provides a unified REST API and MLflow Deployments client for creating and querying endpoints, simplifying experimentation and deployment across different clouds and providers. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, deploy-models-using-model-serving-databricks-on-aws.md]

## Supported Providers

Databricks supports external model providers including OpenAI, Anthropic, and others. As new model versions are released by a provider, they are typically supported without requiring configuration changes. Customers are responsible for ensuring compliance with applicable model licenses. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Governance and Security

External model endpoints are centrally governed from Databricks. You can manage permissions, track and set usage limits, and monitor costs using [AI Gateway](/concepts/ai-gateway.md). All data in transit is encrypted with TLS 1.2+, and all data at rest is encrypted with AES‑256. For all paid accounts, Databricks does not use inputs or outputs submitted to external models to train any models or improve any Databricks services. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Creating an External Model Endpoint

To query an external model, you first create a serving endpoint using the Databricks Serving UI, REST API, or MLflow Deployments SDK. During creation you specify the provider, the model name (e.g., `gpt‑4`), and authentication credentials—typically a secret containing the provider's API key. See Create foundation model serving endpoints for detailed instructions. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Endpoint Creation Options

- **Serving UI**: Navigate to the Serving tab, click **Create endpoint**, select **Foundation models**, then choose **External model providers**. Fill in the provider configuration including the secret for the API key, select the task (chat, completion, or embeddings), and choose the model name. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- **REST API**: Use the `POST /api/2.0/serving-endpoints` endpoint with a configuration that includes the `external_model` object specifying provider, task, model name, and API key secret. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- **MLflow Deployments SDK**: Use `mlflow.deployments.get_deploy_client("databricks")` to create an endpoint programmatically. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Querying External Models

After creation, you query the endpoint using the same OpenAI‑compatible API used for Databricks‑hosted foundation models. For example, you can use the OpenAI Python client by specifying the endpoint name as the `model` parameter. The REST API request format follows the standard chat completions schema. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, deploy-models-using-model-serving-databricks-on-aws.md]

## Update Considerations

When an `external_model` is present in an endpoint configuration, the served entities list can only have one served entity object. Existing endpoints with an `external_model` cannot be updated to remove it. If the endpoint was created without an `external_model`, you cannot later add one. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Use Cases

External models are suitable for:

- **Multi‑provider orchestration**: Access models from different providers through a single, centrally managed endpoint.
- **Production workloads**: Deploy foundation models with governance controls including rate limits and access policies.
- **Experimentation**: Quickly switch between different external models without changing infrastructure.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The unified deployment platform for AI and ML models
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks‑hosted foundation model endpoints
- [AI Gateway](/concepts/ai-gateway.md) — Governance, rate limiting, and cost tracking
- Create foundation model serving endpoints — Detailed creation guide
- [Serving Endpoint ACLs](/concepts/serving-endpoint-acls.md) — Permissions for endpoints
- [AI Functions](/concepts/ai-functions.md) — SQL functions for batch inference using models

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md
- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
2. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
