---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 28825174be0a67b6d0d18833b68e4bf0e06ddba47f72d90f04cd0b1a20dda4d3
  pageDirectory: concepts
  sources:
    - query-vision-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-apis-databricks
    - FMA(
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
    - file: provisioned-throughput-foundation-model-apis-databricks-on-aws.md
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
    - file: query-vision-models-databricks-on-aws.md
title: Foundation Model APIs (Databricks)
description: Databricks-managed API infrastructure for hosting and querying foundation models including vision models via Model Serving.
tags:
  - databricks
  - api
  - foundation-models
timestamp: "2026-06-19T20:05:08.272Z"
---

# Foundation Model APIs (Databricks)

**Foundation Model APIs** are a managed inference service in Databricks that provides access to state-of-the-art foundation models with optimized deployment options. The APIs enable organizations to serve, govern, and consume foundation models — including both Databricks-hosted models and externally hosted models — through a unified serving infrastructure. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Overview

Foundation Model APIs offer two deployment modes: **pay-per-token** and **provisioned throughput**. Pay-per-token provides immediate access to curated foundation model architectures with usage-based pricing, while provisioned throughput allocates dedicated inference capacity with performance guarantees for production workloads. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

All foundation models are also available as pre-installed models in [Unity Catalog](/concepts/unity-catalog.md) under the `system.ai` schema, allowing organizations to discover, govern, and deploy models through Catalog Explorer. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Deployment Options

### Pay-per-Token

Pay-per-token endpoints are automatically provisioned in supported Databricks workspaces. These endpoints appear at the top of the **Serving** tab's Endpoints list view and are ready for immediate querying. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

This mode supports a curated set of foundation model architectures including models from OpenAI, Anthropic, and Meta. Regional availability varies — some models are restricted to US regions, while others are available in both EU and US regions. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Provisioned Throughput

Provisioned throughput provides dedicated inference capacity for foundation models with performance guarantees. Capacity is allocated in chunks of [Model Units](/concepts/model-units.md), and endpoints automatically scale between configurable minimum and maximum throughput levels. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

To create a provisioned throughput endpoint, users specify `min_provisioned_throughput` and `max_provisioned_throughput` fields in the API request. Databricks recommends using the model optimization information API (`GET api/2.0/serving-endpoints/get-model-optimization-info/{model_name}/{version}`) to identify the throughput chunk size for each model before configuring the endpoint. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

Provisioned throughput supports log probabilities (`logprobs`) for chat completion tasks, enabling use cases such as classification, model uncertainty assessment, and evaluation metrics. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### External Models

Foundation Model APIs also support **external models** — foundation models hosted outside of Databricks, such as OpenAI's GPT-4 and Anthropic's Claude. These endpoints can be centrally governed with rate limits and access control. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

External model endpoints are configured by selecting the model provider, specifying the task type (chat, completion, or embeddings), and providing authentication secrets (such as API keys). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Vision Model Support

Foundation Model APIs support multimodal capabilities through select Databricks-hosted models and external model endpoints. The Chat Completions API can accept image inputs encoded as base64 data URLs, enabling models to analyze and describe images. ^[query-vision-models-databricks-on-aws.md]

Multiple images can be included in a single request, allowing the model to analyze each image and synthesize information from all inputs to generate a response. ^[query-vision-models-databricks-on-aws.md]

Each image in a request to a foundation model adds to token usage. See the [pricing calculator](https://www.databricks.com/product/pricing/genai-pricing-calculator) to estimate image pricing based on token usage and the model being used. ^[query-vision-models-databricks-on-aws.md]

## Creating and Managing Endpoints

Endpoints can be created and managed through:

- **Serving UI** — Navigate to the Serving tab, select **Create serving endpoint**, and configure the entity, model, and throughput settings.
- **REST API** — Use the `/api/2.0/serving-endpoints` endpoint with `served_entities` configuration.
- **MLflow Deployments SDK** — Install the MLflow Deployment client and use `mlflow.deployments.get_deploy_client("databricks")`.

When updating endpoint configurations, the old configuration continues serving traffic until the new configuration is ready. In-progress updates can be canceled through the Serving UI. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Compliance and Security

### Compliance Standards

Compliance support varies by deployment mode: ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

| Standard | Pay-per-Token | Provisioned Throughput |
|----------|---------------|------------------------|
| HIPAA | Supported | Supported in all regions |
| PCI-DSS | Not supported | Supported in supported regions |
| FedRAMP | Not supported | Supported in supported regions |
| IRAP | Not supported | Supported in supported regions |
| CCCS | Not supported | Supported in supported regions |
| UK Cyber Essentials Plus | Not supported | Supported in supported regions |

For pay-per-token workloads with the Compliance Security Profile enabled, only HIPAA or "None" can be selected as the compliance standard. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Data Processing and Residency

Databricks may process Foundation Model API data outside the region and cloud provider where the data originated. Workspaces outside US or EU regions must be enabled for cross-Geo data processing to access certain models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Security Controls

Foundation Model API endpoints are protected by workspace-level access controls. Only workspace admins can modify governance settings. Endpoints respect IP allowlists, PrivateLink configurations, and networking-related ingress rules. Organizations can also restrict outbound network access by configuring network policies. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

To restrict which Databricks-hosted foundation models an organization can invoke, see [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md). ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Container Security

New model images created from new model versions contain the latest security patches, but Model Serving does not patch existing images to avoid destabilizing production deployments. Containers are automatically rebuilt every 30 days for compliance requirements. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Limitations

- Model deployment may fail due to GPU capacity issues, resulting in timeout during endpoint creation or update. Contact the Databricks account team to resolve capacity constraints. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]
- External model endpoints can only have one `served_entity` object when `external_model` is present. Existing endpoints with `external_model` cannot be updated to remove it. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- Meta Llama models deployed from Unity Catalog must use the **Instruct** version; base versions are not supported. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]
- Image understanding limitations apply to supported Databricks-hosted foundation models. For external models, refer to the provider's documentation. ^[query-vision-models-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The underlying infrastructure for serving models on Databricks
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for discovering and managing models
- [External Models](/concepts/external-models.md) — Foundation models hosted outside Databricks
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Dedicated inference capacity with performance guarantees
- [Pay-per-Token Pricing](/concepts/pay-per-token-pricing.md) — Usage-based pricing for foundation model inference
- [Model Units](/concepts/model-units.md) — Capacity units for provisioned throughput endpoints
- [AI Gateway](/concepts/ai-gateway.md) — Centralized governance for AI model access
- [Retired Models Policy](/concepts/partner-model-retirement-policy.md) — Lifecycle management for deprecated foundation models
- Query Vision Models — How to send image analysis requests to foundation models

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md
- foundation-model-apis-compliance-and-security-databricks-on-aws.md
- provisioned-throughput-foundation-model-apis-databricks-on-aws.md
- query-vision-models-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
2. [provisioned-throughput-foundation-model-apis-databricks-on-aws.md](/references/provisioned-throughput-foundation-model-apis-databricks-on-aws-0afb43fa.md)
3. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
4. [query-vision-models-databricks-on-aws.md](/references/query-vision-models-databricks-on-aws-afa9c021.md)
