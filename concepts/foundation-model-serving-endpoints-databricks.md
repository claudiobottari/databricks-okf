---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92a81b8e5809a96335618ce19c00abe89ffa7e038185b5bfa9363d9df04e2565
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-serving-endpoints-databricks
    - FMSE(
    - Foundation Model Serving on Databricks
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Foundation Model Serving Endpoints (Databricks)
description: Managed endpoints on Databricks that deploy and serve foundation models, supporting both externally-hosted and Databricks-curated models.
tags:
  - databricks
  - model-serving
  - foundation-models
timestamp: "2026-06-18T11:23:26.334Z"
---

# Foundation Model Serving Endpoints (Databricks)

**Foundation Model Serving Endpoints** allow you to deploy and serve foundation models (large language models, embedding models, and others) through [Databricks Model Serving](/concepts/databricks-model-serving.md). Endpoints can serve models hosted externally (e.g., OpenAI, Anthropic) or Databricks-provided models via the [Foundation Model APIs](/concepts/foundation-model-apis.md). Databricks Model Serving manages the infrastructure, scaling, and governance of these endpoints. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Supported Models

Model Serving supports two categories of foundation models: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- **External models** – Foundation models hosted outside Databricks, such as OpenAI’s GPT‑4 and Anthropic’s Claude. Endpoints for external models can be centrally governed, with rate limits and access control enforced by Databricks.
- **Foundation Model APIs** – State-of-the-art open foundation models curated by Databricks (e.g., Meta-Llama-3.3-70B-Instruct, GTE-Large). These are available in two pricing tiers:
  - **Pay-per-token** – Immediate use with billing per token consumed.
  - **Provisioned throughput** – For production workloads, using base or fine‑tuned models, with performance guarantees.

## Requirements

- The Databricks workspace must be in a supported region for either [Foundation Model APIs](/concepts/foundation-model-apis.md) or [External Models](/concepts/external-models.md). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- To create endpoints via the [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md), install the MLflow Deployment client:

  ```python
  import mlflow.deployments
  client = mlflow.deployments.get_deploy_client("databricks")
  ```

  ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Creating a Foundation Model Serving Endpoint

You can create endpoints using any of the following methods: the **Serving UI**, the **REST API**, or the **MLflow Deployments SDK**. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Using the Serving UI

1. In the workspace sidebar, click **Serving**.
2. Click **Create serving endpoint**.
3. Provide a **Name**.
4. In **Served entities**, select the model type and configure provider details.
5. Click **Create**.

The endpoint’s state initially appears as **Not Ready**. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Using the REST API

Use the Serving Endpoints API to create an endpoint programmatically. For details, see the [API reference](https://docs.databricks.com/api/workspace/servingendpoints). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Using the MLflow Deployments SDK

```python
client.create_endpoint(
    name="my-endpoint",
    config={
        "served_entities": [
            {
                "name": "openai_chat",
                "external_model": {
                    "provider": "openai",
                    "name": "gpt-4",
                    "task": "llm/v1/chat",
                    "openai_config": {
                        "openai_api_key": "{{secrets/my_scope/my_key}}"
                    }
                }
            }
        ]
    }
)
```

^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Provisioned Throughput Endpoints

For fine‑tuned variants of Foundation Model APIs models using **provisioned throughput**, follow the [Provisioned Throughput API](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis#provisioned-throughput-api). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Creating an External Model Serving Endpoint

External model endpoints require configuring the provider and authentication. Steps using the **Serving UI**, **REST API**, and **MLflow Deployments SDK** are described in the source. The key points: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- Select **Foundation models** as the entity type, then choose an **External model provider**.
- Provide authentication credentials (typically a secret referencing a personal access token).
- Select the **task** (chat, completion, or embeddings) and the **model name**.
- An endpoint configuration can contain only one `external_model` served entity.

## Updating Endpoints

After creation, you can adjust the compute configuration (e.g., workload size). During an update, the old configuration continues serving traffic until the new one is ready. Concurrent updates are not allowed. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

- In the **Serving UI**, you can cancel an in‑progress update by clicking **Cancel update**.
- If an endpoint was created with an `external_model`, you cannot later remove the `external_model` (and vice‑versa — endpoints without an `external_model` cannot be updated to add one).
- The update configuration via REST API is documented in the [update configuration reference](https://docs.databricks.com/api/workspace/servingendpoints/updateconfig).

## Additional Resources

- [AI Gateway-enabled inference tables](/concepts/ai-gateway-inference-tables.md)
- Use foundation models – querying endpoints.
- [External models in Model Serving](/concepts/external-model-multi-serving.md)

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Pay-per-Token Pricing](/concepts/pay-per-token-pricing.md)
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md)
- Serving Endpoints API
- [External Models](/concepts/external-models.md)

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
