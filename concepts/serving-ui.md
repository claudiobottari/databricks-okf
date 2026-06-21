---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f103ad5693b4f42d1bd68f796751214c210974e1e209278a778b9f96561e97bf
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-ui
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Serving UI
description: The Databricks workspace interface for creating, viewing, and managing model serving endpoints, including canceling in-progress configuration updates.
tags:
  - model-serving
  - databricks
  - ui
timestamp: "2026-06-19T14:37:56.136Z"
---

# Serving UI

The **Serving UI** is the Databricks workspace interface for creating, viewing, and managing [model serving endpoints](/concepts/model-serving-endpoint.md). It is one of three options for endpoint creation, alongside the REST API and the [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Accessing the Serving UI

The Serving UI is located under the **Serving** tab in the left sidebar of the Databricks workspace. The main view lists all endpoints; for [Foundation Model APIs](/concepts/foundation-model-apis.md) with **pay-per-token** pricing, the automatically provided endpoints appear at the top of this list. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Creating Endpoints

### Foundation Model APIs (pay-per-token)

For models provided via Foundation Model APIs with pay-per-token pricing, Databricks creates the endpoints automatically. You can view and query them directly from the Serving UI without manual creation steps. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### External Models

To serve an external model (e.g., OpenAI GPT-4, Anthropic Claude), you use the **Create** or similar button in the Serving UI and configure the following: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

1. **Name** – Provide a name for the endpoint.
2. **Served entities** – Click into the **Entity** field, select **Foundation models**, then choose the model provider listed under **External model providers**.
3. **Configuration** – Provide the provider‑specific secrets (e.g., API key stored as a secret) and select the task (chat, completion, or embeddings).
4. **Model name** – Choose the specific external model to serve.

After creation, the **Serving endpoints** page displays and the endpoint state appears as **Not Ready** until the deployment completes. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Provisioned Throughput Endpoints

For fine‑tuned variants of foundation models using **provisioned throughput**, endpoints are created via the REST API; the Serving UI can then be used to manage those endpoints once created. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Updating Endpoints

The Serving UI only supports canceling a configuration update that is in progress (via the **Cancel update** button on the endpoint details page). All other updates (e.g., changing the served model, scaling settings) must be performed using the REST API or MLflow Deployments SDK. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The overall serving infrastructure.
- [External Models](/concepts/external-models.md) – Foundation models hosted outside Databricks.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Curated open models with pay‑per‑token or provisioned throughput.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Performance‑guaranteed serving for base or fine‑tuned models.
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) – Programmatic client for endpoint management.
- [AI Gateway-enabled inference tables](/concepts/ai-gateway-inference-tables.md) – Logging and governance for served models.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
