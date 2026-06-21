---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f692546a493270ea33f55e4d56785f17523ef576db05eb2d0b05e6919b69a64
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-serving-endpoints
    - FMSE
    - Create Foundation Model Serving Endpoints
    - Create foundation model serving endpoints
    - Foundation Model Endpoint
    - Foundation Model Endpoints
    - Foundation Model Serving Endpoint
    - Scoring a model endpoint
    - scoring a model endpoint
    - foundation-model-serving-endpoints-databricks
    - FMSE(
    - Foundation Model Serving on Databricks
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Foundation Model Serving Endpoints
description: Databricks Model Serving endpoints that deploy and serve foundation models, supporting external models and Foundation Model APIs.
tags:
  - model-serving
  - databricks
  - foundation-models
timestamp: "2026-06-19T18:01:40.426Z"
---

```markdown
---
title: Foundation Model Serving Endpoints
summary: Databricks endpoints that deploy and serve foundation models, supporting both externally-hosted models and curated open foundation models.
sources:
  - create-foundation-model-serving-endpoints-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - model-serving
  - foundation-models
  - databricks
aliases:
  - foundation-model-serving-endpoints
  - FMSE
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Foundation Model Serving Endpoints

**Foundation Model Serving Endpoints** are [[Model Serving]] endpoints that deploy and serve foundation models. Databricks Model Serving supports two categories: external models hosted outside Databricks (e.g., OpenAI GPT-4, Anthropic Claude) and curated open foundation models made available via Foundation Model APIs (e.g., Meta-Llama-3.3-70B-Instruct, GTE-Large). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Overview

External model endpoints can be centrally governed, and administrators can set rate limits and access controls. For open foundation models, Databricks provides **pay-per-token** pricing for immediate use and **provisioned throughput** for production workloads (using base or fine-tuned models) with performance guarantees. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

Model Serving offers three ways to create endpoints: the Serving UI, the REST API, and the MLflow Deployments SDK. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- A Databricks workspace in a supported region. See Foundation Model APIs regions and [[External Models|External models regions]] for the list of supported regions. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- For creating endpoints with the MLflow Deployments SDK, install the MLflow Deployment client: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow.deployments
client = mlflow.deployments.get_deploy_client("databricks")
```

## Creating Endpoints

### Foundation Model APIs (Pay-per-Token)

For models available through Foundation Model APIs with pay-per-token pricing, Databricks automatically provides endpoints in your workspace. To see them, select the **Serving** tab in the left sidebar — the Foundation Model APIs are listed at the top of the Endpoints list view. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Provisioned Throughput Endpoints

To create an endpoint that serves fine-tuned variants of foundation models using provisioned throughput, see [[Provisioned Throughput Endpoint REST API|Create your provisioned throughput endpoint using the REST API]]. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### External Model Endpoints

To create an endpoint that queries a foundation model hosted by an external provider: ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

1. In the **Name** field, provide a name for your endpoint.
2. In the **Served entities** section:
   - Click into the **Entity** field to open the **Select served entity** form.
   - Select **Foundation models**.
   - In the **Select a foundation model** field, choose the model provider from those listed under **External model providers**. The form dynamically updates based on your selection.
   - Click **Confirm**.
   - Provide the configuration details for accessing the selected model provider — typically a secret that references the [[Databricks Personal Access Token (PAT) Authentication|personal access token]] the endpoint will use.
   - Select the task: `chat`, `completion`, or `embeddings`.
   - Select the name of the external model. The list dynamically updates based on your task selection. See the [[External Models|available external models]] for the full list.
3. Click **Create**. The **Serving endpoints** page appears with **Serving endpoint state** shown as Not Ready.

## Updating Endpoints

After enabling a model endpoint, you can adjust the compute configuration as needed. Workload size and compute configuration influence the resources allocated for serving your model. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

Until the new configuration is ready, the old configuration continues serving prediction traffic. While an update is in progress, another update cannot be made. In the Serving UI, you can cancel an in-progress configuration update by selecting **Cancel update** on the top right of the endpoint's details page. This functionality is only available in the Serving UI. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Constraints

- When an `external_model` is present in an endpoint configuration, the served entities list can only have one `served_entity` object. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- Existing endpoints with an `external_model` cannot be updated to remove the `external_model`. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- If the endpoint is created without an `external_model`, you cannot update it to add an `external_model`. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### REST API Update Example

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

## Querying Endpoints

For instructions on querying foundation model serving endpoints, see Use foundation models. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [[Model Serving]] — The underlying platform for deploying models.
- [[External Model Multi-Serving|External Models in Model Serving]] — Detailed guidance on external model configuration.
- [[Foundation Model APIs]] — Curated open models with optimized inference.
- [[AI Gateway Inference Tables|AI Gateway-enabled inference tables]] — Logging and monitoring for served models.
- [[Custom Model Serving Endpoint Support|Create custom model serving endpoints]] — For traditional ML or Python models.
- Rate limits and access control — Governance features for external model endpoints.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md
```

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
