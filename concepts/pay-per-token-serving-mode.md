---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e914668ed8218ee0f3f4d24ca3d18d4905599f4b268ae990c2b82855e5842c66
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-serving-mode
    - PSM
    - Pay-per-Token Serving
    - Pay-per-token serving
    - Pay‑per‑token serving
    - Pay-per-Token
    - Pay-per-token
    - Pay-per-token mode
    - Pay‑per‑Token
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: Pay-per-token serving mode
description: Preconfigured endpoints for accessing foundation models on a per-token billing basis, recommended for getting started and prototyping but not designed for high-throughput applications.
tags:
  - pricing
  - model-serving
  - llm
timestamp: "2026-06-19T14:50:24.796Z"
---

# Pay-per-token serving mode

**Pay-per-token serving mode** is a consumption-based offering of [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) that provides access to preconfigured endpoints for state-of-the-art open models hosted by Databricks. This mode does not require customers to manage their own model deployment or provision dedicated infrastructure; usage is billed per token consumed. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Overview

Pay-per-token is the simplest way to begin using foundation models on Databricks. Preconfigured endpoints for supported pay-per-token models are automatically available in the workspace under the **Serving** tab, listed at the top of the Endpoints list view. ^[databricks-foundation-model-apis-databricks-on-aws.md]

The mode is compatible with the OpenAI client SDK, the Databricks Python SDK, the [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md), and the REST API, allowing flexible integration into existing applications. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Recommended usage

Databricks recommends pay-per-token mode for beginning the journey with Foundation Model APIs. Although the mode is not specifically designed for high-throughput applications, it can still be used for production workloads when throughput requirements are moderate. ^[databricks-foundation-model-apis-databricks-on-aws.md]

Typical use cases include:

- Querying a generalized LLM to validate a project’s feasibility before investing more resources.
- Building quick prototypes and proof-of-concept applications for LLM-based solutions.
- Replacing proprietary models with open alternatives to optimize for cost and performance.
- Efficiently comparing multiple LLMs to select the best candidate for a use case.
- Building production LLM applications that do not require the performance guarantees or fine-tuning capabilities of [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md). ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Accessing pay-per-token endpoints

1. Navigate to the **Serving** tab in the left sidebar of your Databricks workspace.
2. The Foundation Model APIs are displayed at the top of the Endpoints list view.
3. Use a Databricks API token to authenticate requests.
4. Query the endpoint using the OpenAI-compatible API, the Python SDK, or the REST API. See [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models) for scoring examples.

Supported models and per-token pricing are listed in the foundation model overview documentation. The workspace must be in a [supported pay-per-token region](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws). ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Limitations

- Not designed for high-throughput applications, though it can serve production workloads with moderate traffic. ^[databricks-foundation-model-apis-databricks-on-aws.md]
- Does not offer performance guarantees, fine-tuned model support, or compliance certifications such as HIPAA — those capabilities are available only with [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md). ^[databricks-foundation-model-apis-databricks-on-aws.md] *(Inferred from the contrast between modes)*
- Subject to the general [Foundation Model APIs limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#fmapi-limits). ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related concepts

- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) — The overarching service offering three serving modes.
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) — Recommended for production workloads requiring high throughput, performance guarantees, and fine-tuned models.
- [AI Functions](/concepts/ai-functions.md) — A separate mode for batch inference workloads using generative AI or ML models.
- [Model Serving](/concepts/model-serving.md) — The platform feature that hosts serving endpoints.
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) — One of the client libraries that can query pay-per-token endpoints.

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
