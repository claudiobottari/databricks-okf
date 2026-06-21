---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0e799743a0fbc0776abd0479cc643f74e7e8a3bfcbaebe83c2db917cb231940
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-model-configuration
    - EMC
    - External Model Integration
    - External Model Credentials
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
      start: 8
      end: 10
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
      start: 24
      end: 28
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
      start: 32
      end: 34
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
      start: 45
      end: 47
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
      start: 51
      end: 68
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
      start: 91
      end: 107
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
      start: 31
      end: 34
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
      start: 80
      end: 88
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
      start: 80
      end: 84
title: External Model Configuration
description: Configuration details required to set up an external model endpoint, including model provider selection, task type (chat/completion/embeddings), API keys via secrets, and model name selection.
tags:
  - model-serving
  - external-models
  - configuration
timestamp: "2026-06-19T18:02:02.487Z"
---

# External Model Configuration

**External Model Configuration** refers to the setup of a [|model serving endpoint](/concepts/model-serving.md) that connects to a foundation model hosted outside of Databricks. These endpoints enable centralized governance, rate limits, and access control for third-party models such as OpenAI’s GPT‑4 and Anthropic’s Claude. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md#L8-L10]

## Overview

External models are a category of foundation models that are not hosted on Databricks infrastructure. They are accessed through [External Models in Model Serving](/concepts/external-model-multi-serving.md), which provides a unified API layer with built-in security and monitoring. Creating an external model endpoint requires selecting a provider, configuring authentication (usually a personal access token stored as a secret), and choosing the task type (chat, completion, or embeddings). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Requirements

Before creating an external model endpoint, you must have:

- A Databricks workspace in a [supported region](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md#L24-L28]
- (For API or SDK creation) The MLflow Deployments client installed: `import mlflow.deployments; client = mlflow.deployments.get_deploy_client("databricks")`. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md#L32-L34]

## Creating an External Model Serving Endpoint

You can create an external model endpoint using the **Serving UI**, **REST API**, or **MLflow Deployments SDK**. The steps are essentially the same across methods. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md#L45-L47]

### Serving UI

1. Provide a **Name** for the endpoint.
2. In the **Served entities** section, click the **Entity** field.
3. Select **Foundation models**.
4. Under **Select a foundation model**, choose the provider from the **External model providers** list.
5. Confirm the selection.
6. Provide configuration details – typically a secret referencing the personal access token required to access that model.
7. Select the **task**: `chat`, `completion`, or `embeddings`.
8. Select the **name** of the external model (the list filters based on task).
9. Click **Create**.

The new endpoint appears with state **Not Ready** until it becomes operational. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md#L51-L68]

### REST API

Send a `POST` request to the serving endpoints API. The payload must include `name`, `served_entities` with an `external_model` object containing `name`, `provider`, `task`, and provider-specific configuration (e.g., `openai_config`). A typical example for OpenAI GPT‑4: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md#L91-L107]

```json
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

### MLflow Deployments SDK

Use the `client.create_endpoint()` method with the same configuration structure as the REST API. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md#L31-L34]

## Updating an External Model Endpoint

You can update the compute configuration or served entity details after creation. Restriction: if the endpoint already contains an `external_model`, you cannot update it to remove that `external_model`. Conversely, if the endpoint was created without an `external_model`, you cannot add one later. Only one served entity is allowed when an `external_model` is present. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md#L80-L88]

While an update is in progress, the old configuration continues to serve traffic. You can cancel an in‑progress update from the Serving UI by selecting **Cancel update**. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md#L80-L84]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Pay‑per‑token and provisioned throughput endpoints for Databricks‑hosted models.
- [Create Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) – For traditional ML or Python models.
- [AI Gateway Inference Tables](/concepts/ai-gateway-inference-tables.md) – Audit and monitor endpoint usage.
- Model Serving Limits – Region and quota constraints.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md:8-10](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
2. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
3. [create-foundation-model-serving-endpoints-databricks-on-aws.md:24-28](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
4. [create-foundation-model-serving-endpoints-databricks-on-aws.md:32-34](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
5. [create-foundation-model-serving-endpoints-databricks-on-aws.md:45-47](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
6. [create-foundation-model-serving-endpoints-databricks-on-aws.md:51-68](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
7. [create-foundation-model-serving-endpoints-databricks-on-aws.md:91-107](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
8. [create-foundation-model-serving-endpoints-databricks-on-aws.md:31-34](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
9. [create-foundation-model-serving-endpoints-databricks-on-aws.md:80-88](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
10. [create-foundation-model-serving-endpoints-databricks-on-aws.md:80-84](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
