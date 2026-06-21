---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44a8adb011e81b114138de147483bc7065a2eddd545a84db661bd703f9ebf9ae
  pageDirectory: concepts
  sources:
    - query-an-embedding-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-models-apis-on-databricks
    - FMAOD
    - Foundation Model APIs on Databricks
    - Foundation Models Hosted on Databricks
    - Foundation Models on Databricks
    - Foundation models hosted on Databricks
    - Foundation Model REST API Reference (Databricks APIs)
    - Foundation Models on Databricks|Databricks Foundation Model
  citations:
    - file: query-an-embedding-model-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Foundation Models APIs on Databricks
description: Databricks-hosted foundation models available via pay-per-token APIs for embedding tasks, also called Databricks-hosted foundation models.
tags:
  - foundation-models
  - databricks
  - model-serving
  - API
timestamp: "2026-06-19T20:01:31.508Z"
---

# Foundation Models APIs on Databricks

**Foundation Models APIs on Databricks** provide a serverless interface for querying pre-trained foundation models hosted directly on the Databricks platform. These APIs enable users to access state-of-the-art AI models for tasks such as text generation, embeddings, chat, reasoning, and vision processing without managing underlying infrastructure.

## Overview

Foundation Models APIs allow users to query Databricks-hosted foundation models through a simple API endpoint. These models are made available as **Databricks-hosted foundation models** via the Foundation Models APIs, as opposed to [External Models](/concepts/external-models.md) which are hosted outside of Databricks.^[query-an-embedding-model-databricks-on-aws.md]

The APIs support pay-per-token pricing for certain models, enabling cost-effective access to powerful AI capabilities. Users can interact with these models using various client options including the OpenAI-compatible client, REST API, MLflow Deployments SDK, Databricks Python SDK, and LangChain.^[query-an-embedding-model-databricks-on-aws.md]

## Supported Model Types

Foundation Models APIs support multiple model types for different tasks:

### Embedding Models
Embedding models convert text into numerical vector representations. For example, the `databricks-gte-large-en` model is available through the pay-per-token offering. Embedding requests take a JSON payload with an `input` field containing the text to embed.^[query-an-embedding-model-databricks-on-aws.md]

Example response format:
```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": []
    }
  ],
  "model": "text-embedding-ada-002-v2",
  "usage": {
    "prompt_tokens": 2,
    "total_tokens": 2
  }
}
```

### Chat, Reasoning, and Vision Models
The Databricks platform also supports Query a Chat Model|chat models, [Query Reasoning Models|reasoning models](/concepts/reasoning-models-foundation-model-api.md), and [Query Vision Models|vision models](/concepts/querying-vision-models-on-databricks-model-serving.md) through the Foundation Models APIs.^[query-an-embedding-model-databricks-on-aws.md]

## Querying Foundation Models

### Client Options

Users can query foundation models using several client approaches:

- **OpenAI-compatible client**: Use the `DatabricksOpenAI` client from `databricks_openai` package, specifying the model serving endpoint name as the `model` parameter.^[query-an-embedding-model-databricks-on-aws.md]
- **REST API**: Send direct HTTP requests to the model serving endpoint.^[query-an-embedding-model-databricks-on-aws.md]
- **MLflow Deployments SDK**: Use MLflow's deployment tools for programmatic access.^[query-an-embedding-model-databricks-on-aws.md]
- **Databricks Python SDK**: Leverage the official Databricks SDK for Python.^[query-an-embedding-model-databricks-on-aws.md]
- **LangChain**: Integrate with the LangChain framework for building LLM applications.^[query-an-embedding-model-databricks-on-aws.md]

### Authentication

To query foundation models from outside the Databricks workspace, users must authenticate using a Databricks API token. The OpenAI client can be configured with the token and workspace instance URL:

```python
client = OpenAI(
    api_key="dapi-your-databricks-token",
    base_url="https://example.staging.cloud.databricks.com/serving-endpoints"
)
```

### Checking Embedding Normalization

For embedding models, users can verify whether the generated embeddings are normalized using a simple function:

```python
import numpy as np

def is_normalized(vector: list[float], tol=1e-3) -> bool:
    magnitude = np.linalg.norm(vector)
    return abs(magnitude - 1) < tol
```
^[query-an-embedding-model-databricks-on-aws.md]

## Serverless Budget Policies

When using [MLflow](/concepts/mlflow.md) to run serverless workloads against the Foundation Models APIs, a **serverless budget policy** must be configured. If the workspace disables the default budget policy without assigning an alternative, MLflow returns a `403 PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy` error.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

Affected workloads include:
- Scheduled scorers (production monitoring)
- Synthetic evaluation set generation
- Agent Evaluation|Agent evaluation

### Setting a Budget Policy

To resolve this error, set a serverless budget policy on the MLflow experiment:

1. **In the UI**: Open the experiment, navigate to the **Details** panel, and set the **Budget policy** to an available policy.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
2. **With the API**: Use `mlflow.set_experiment_tag()` to set the `mlflow.workload_creation_policy_id` tag.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

Users and service principals must have permission to use the budget policy they assign.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [External Models](/concepts/external-models.md) — Foundation models hosted outside of Databricks
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — Endpoints for serving models on Databricks
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for MLflow runs and evaluations
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controls serverless workload spending
- Query a Chat Model — Querying chat-based foundation models
- [Query Reasoning Models](/concepts/hybrid-reasoning-models.md) — Querying reasoning models
- Query Vision Models — Querying vision-capable models

## Sources

- query-an-embedding-model-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [query-an-embedding-model-databricks-on-aws.md](/references/query-an-embedding-model-databricks-on-aws-18956bab.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
