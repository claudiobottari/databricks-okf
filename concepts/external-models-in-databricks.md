---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7bca95fb316e10218d21c8af2eae51f58d4ba95d975d0a327b0452f31575dc18
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-models-in-databricks
    - EMID
    - External Tables in Databricks
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: External Models in Databricks
description: Foundation models hosted outside Databricks (e.g., GPT-4, Claude) served through centrally governed endpoints with rate limits and access control.
tags:
  - model-serving
  - external-models
  - governance
timestamp: "2026-06-19T09:37:13.100Z"
---

# External Models in Databricks

**External Models** in Databricks refer to foundation models that are hosted outside of the Databricks platform, such as OpenAI's GPT-4 and Anthropic's Claude. These models are served through Databricks Model Serving endpoints, allowing organizations to centrally govern access, establish rate limits, and control usage while benefiting from models hosted by third-party providers. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Overview

External models enable organizations to integrate third-party AI models into their Databricks workflows without hosting those models on Databricks infrastructure. Databricks acts as a gateway, providing a unified serving interface, governance controls, and monitoring capabilities for models that run externally. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Creating an External Model Serving Endpoint

External model serving endpoints can be created through three interfaces:

- **Serving UI** – The web interface in the Databricks workspace
- **REST API** – Programmatic endpoint creation
- **MLflow Deployments SDK** – Python SDK for managing endpoints

### Requirements

- A Databricks workspace in a supported region. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Configuration Steps

1. **Name the endpoint** – Provide a unique name in the **Name** field.
2. **Select served entity** – Under **Served entities**, click into the **Entity** field to open the selection form. Choose **Foundation models**, then select the model provider under **External model providers**. The form dynamically updates based on the provider selection. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
3. **Provide credentials** – Configure access to the selected provider, typically using a secret that references a personal access token for the external service. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
4. **Select task and model** – Choose the task type (chat, completion, or embeddings) and the specific external model name. The list of available models updates based on the selected task. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
5. **Click Create** – The **Serving endpoints** page appears with the state shown as **Not Ready** until initialization completes. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Using REST API (Example)

```bash
{
  "name": "openai_endpoint",
  "served_entities": [
    {
      "name": "openai_chat",
      "external_model": {
        "name": "gpt-4",
        "provider": "openai",
        "task": "llm/v1/chat",
        "openai_config": {
          "openai_api_key": "{{secrets/my_scope/my_openai_api_key}}"
        }
      }
    }
  ]
}
```

^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Updating External Model Endpoints

When an `external_model` is present in an endpoint configuration, the served entities list can only contain one served entity object. Existing endpoints with an `external_model` cannot be updated to remove it. Conversely, endpoints created without an `external_model` cannot be updated to add one. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

During an update, the old configuration continues serving prediction traffic until the new configuration is ready. Only one update can occur at a time. In the Serving UI, you can cancel an in-progress configuration update. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Key Considerations

- **Centralized governance** – All external model usage flows through Databricks, enabling consistent access control and rate limiting. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- **Rate limits** – Administrators can set usage quotas on external model endpoints. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- **Single entity limitation** – Endpoints serving external models can only have one served entity object. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Comparison with Foundation Model APIs

Databricks offers two categories of model serving:

| Feature | External Models | Foundation Model APIs |
|---------|----------------|----------------------|
| Model location | Hosted outside Databricks | Models curated by Databricks |
| Examples | OpenAI GPT-4, Anthropic Claude | Meta-Llama-3.3-70B-Instruct, GTE-Large |
| Pricing | Provider's pricing applies | Pay-per-token or provisioned throughput |
| Governance | Rate limits and access control | Built-in Databricks governance |

^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The core Databricks ML inference platform
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Databricks-hosted foundation models
- [AI Gateway-enabled inference tables](/concepts/ai-gateway-inference-tables.md) – Logging and monitoring for model serving
- [Serving endpoints](/concepts/serving-endpoint-acls.md) – General endpoint management and configuration
- [Rate limits for model serving](/concepts/rate-limits-and-timeouts-in-model-serving.md) – Controlling usage of served models
- Secrets in Databricks – Managing API keys securely

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
