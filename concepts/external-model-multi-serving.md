---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 116112455524baa4931802057383cc1dda1e0bde4739e3c90321ea9f74f78e88
  pageDirectory: concepts
  sources:
    - serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-model-multi-serving
    - EMM
    - External Model Serving
    - External Models in Model Serving
    - External models in Model Serving
  citations:
    - file: serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
title: External Model Multi-Serving
description: Serving multiple external (third-party provider) models such as OpenAI GPT-4 and Anthropic Claude on the same endpoint, provided they share the same task type.
tags:
  - model-serving
  - external-models
  - databricks
timestamp: "2026-06-19T23:03:34.196Z"
---

# External Model Multi-Serving

**External Model Multi-Serving** allows you to configure a single [Model Serving Endpoint](/concepts/model-serving-endpoint.md) to route traffic to multiple external models—such as OpenAI’s GPT‑4 or Anthropic’s Claude—hosted outside Databricks. This enables A/B testing, performance comparison, and gradual rollouts of new model versions without deploying separate endpoints for each provider. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

When serving multiple [External Models](/concepts/external-models.md), all models in the endpoint must:
- Share the same **task type** (e.g., `llm/v1/chat`).
- Have a **unique name** within the endpoint.

You **cannot** mix [External Models](/concepts/external-models.md) with custom models or [Foundation Model APIs](/concepts/foundation-model-apis.md) on the same endpoint. If you need to serve different model types (e.g., a custom model and an external model), you must use separate endpoints. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Creating an Endpoint with Multiple [External Models](/concepts/external-models.md)

Use the MLflow Deployments API (`mlflow.deployments.get_deploy_client("databricks")`) to create an endpoint. The configuration must include:
- A `served_entities` array with one entry per external model, each specifying the model name, provider, task, and provider-specific authentication (e.g., API keys stored in Databricks Secrets).
- A `traffic_config` with `routes` that define the percentage of traffic each served model receives.

The following Python example creates an endpoint named `mix-chat-endpoint` that routes 50% of traffic to OpenAI’s `gpt-4` and 50% to Anthropic’s `claude-3-opus-20240229`: ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

```python
import [[mlflow|MLflow]].deployments

client = [[mlflow|MLflow]].deployments.get_deploy_client("databricks")

client.create_endpoint(
    name="mix-chat-endpoint",
    config={
        "served_entities": [
            {
                "name": "served_model_name_1",
                "external_model": {
                    "name": "gpt-4",
                    "provider": "openai",
                    "task": "llm/v1/chat",
                    "openai_config": {
                        "openai_api_key": "{{secrets/my_openai_secret_scope/openai_api_key}}"
                    }
                }
            },
            {
                "name": "served_model_name_2",
                "external_model": {
                    "name": "claude-3-opus-20240229",
                    "provider": "anthropic",
                    "task": "llm/v1/chat",
                    "anthropic_config": {
                        "anthropic_api_key": "{{secrets/my_anthropic_secret_scope/anthropic_api_key}}"
                    }
                }
            }
        ],
        "traffic_config": {
            "routes": [
                {"served_model_name": "served_model_name_1", "traffic_percentage": 50},
                {"served_model_name": "served_model_name_2", "traffic_percentage": 50}
            ]
        },
    }
)
```

The `traffic_percentage` values for all routes must sum to 100. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Updating the Traffic Split

You can adjust the traffic split between served models using the **PUT /api/2.0/serving-endpoints/{name}/config** REST API or via the Databricks UI under the **Serving** tab using the **Edit configuration** button. The request body includes the full `served_entities` array and an updated `traffic_config`. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Querying Individual Models

To send requests directly to a specific served model (bypassing the traffic split), use the following endpoint:

```
POST /serving-endpoints/{endpoint-name}/served-models/{served-model-name}/invocations
```

The request format is the same as querying the endpoint. When you use this URL, the traffic configuration is ignored; all requests are served by the named model. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- External Model Serving – Overview of serving third-party model providers from Databricks.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The core entity for hosting models for inference.
- MLflow Deployments API – Programmatic interface for creating and managing endpoints.
- A/B Testing with Model Serving – Using traffic splits to compare model performance.
- Databricks Secrets – Recommended way to store provider API keys.

## Sources

- serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md](/references/serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws-64227d03.md)
