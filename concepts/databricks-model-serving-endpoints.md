---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee1d55167d41d44d467cfcc4be2c98d80309ed39aada8ed0f029e5e12b00c70b
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
    - query-with-the-google-gemini-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-model-serving-endpoints
    - DMSE
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
    - file: query-with-the-google-gemini-api-databricks-on-aws.md
title: Databricks Model Serving Endpoints
description: The underlying serving infrastructure on Databricks that hosts Foundation Model APIs, supporting both pay-per-token and provisioned throughput endpoint modes.
tags:
  - model-serving
  - infrastructure
  - endpoints
timestamp: "2026-06-19T18:12:58.192Z"
---

# Databricks Model Serving Endpoints

**Databricks Model Serving Endpoints** provide a managed infrastructure for deploying, querying, and monitoring machine learning models on Databricks. They enable you to serve both custom models and foundation models through scalable endpoints without managing underlying infrastructure.

## Overview

Model Serving Endpoints allow you to deploy models as REST API endpoints that can be queried in real-time or used for batch inference. The platform supports multiple serving modes, including pay-per-token, provisioned throughput, and AI Functions for batch workloads. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Foundation Model APIs

Foundation Model APIs are a key feature of Model Serving Endpoints that provide access to state-of-the-art open models hosted by Databricks. These APIs allow you to build applications using pre-trained models without maintaining your own model deployment infrastructure. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Serving Modes

Foundation Model APIs are available in three modes:

- **Pay-per-token**: The easiest way to start accessing foundation models. Recommended for beginning your journey with Foundation Model APIs. While not designed for high-throughput applications, it can be used for production workloads. ^[databricks-foundation-model-apis-databricks-on-aws.md]

- **Provisioned throughput**: Recommended for all production workloads, especially those requiring high throughput, performance guarantees, fine-tuned models, or additional security requirements. Provisioned throughput endpoints are available with compliance certifications like HIPAA. ^[databricks-foundation-model-apis-databricks-on-aws.md]

- **AI Functions optimized models**: Recommended for batch inference workloads. You can run batch inference using any generative AI or ML model using AI Functions. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Use Cases

Foundation Model APIs support a variety of applications:

- Querying a generalized LLM to verify a project's validity before investing more resources
- Creating quick proof-of-concepts for LLM-based applications before training and deploying custom models
- Building chatbots using retrieval augmented generation (RAG) with foundation models and vector indexes
- Replacing proprietary models with open alternatives to optimize for cost and performance
- Comparing LLMs to find the best candidate for a use case
- Building production LLM applications on a scalable, SLA-backed serving solution ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Requirements

To use Foundation Model APIs, you need:

- A Databricks API token to authenticate endpoint requests
- Serverless compute (for provisioned throughput models)
- A workspace in a supported region (pay-per-token or provisioned throughput regions) ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Querying Endpoints

The Foundation Model APIs are compatible with OpenAI, so you can use the OpenAI client for querying. You can also use the UI, the Foundation Models APIs Python SDK, the MLflow Deployments SDK, or the REST API. Databricks recommends using the OpenAI client SDK or API for extended interactions and the UI for trying out the feature. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Querying with the Google Gemini API

You can query Gemini models through Databricks Model Serving Endpoints using the Google Generative AI client library. The following example demonstrates how to configure the client to route requests through a Databricks serving endpoint: ^[query-with-the-google-gemini-api-databricks-on-aws.md]

```python
from google import genai
from google.genai import types
import os

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')

client = genai.Client(
    api_key="databricks",
    http_options=types.HttpOptions(
        base_url="https://example.staging.cloud.databricks.com/serving-endpoints/gemini",
        headers={
            "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        },
    ),
)

response = client.models.generate_content(
    model="databricks-gemini-2-5-pro",
    contents=[
        types.Content(
            role="user",
            parts=[types.Part(text="What is a mixture of experts model?")],
        ),
    ],
    config=types.GenerateContentConfig(
        max_output_tokens=256,
    ),
)

print(response.text)
```

## Pay-per-Token Endpoints

Preconfigured endpoints that serve pay-per-token models are accessible in your Databricks workspace. To access them, navigate to the **Serving** tab in the left sidebar. The Foundation Model APIs are located at the top of the Endpoints list view. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Provisioned Throughput Endpoints

Provisioned throughput provides endpoints with optimized inference for foundation model workloads that require performance guarantees. Support includes:

- Base models of all sizes, accessible via the Databricks Marketplace or downloaded from Hugging Face and registered in Unity Catalog
- Fine-tuned variants of base models, such as models fine-tuned on proprietary data
- Fully custom weights and tokenizers, including models trained from scratch or continued pre-trained
- Other variations using the base model architecture (for example, CodeLlama) ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Limitations

Foundation Model APIs have specific limits that apply to usage. See the Foundation Model APIs limits documentation for details. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The broader infrastructure for deploying models on Databricks
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Access to state-of-the-art open models hosted by Databricks
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Optimized inference for production workloads
- [AI Functions](/concepts/ai-functions.md) — Batch inference capabilities for generative AI and ML models
- [Unity Catalog](/concepts/unity-catalog.md) — Model registry for managing and deploying models
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) — SDK for querying deployed models
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Pattern for building chatbots with foundation models
- Serverless Compute — Compute infrastructure required for provisioned throughput models

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md
- query-with-the-google-gemini-api-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
2. [query-with-the-google-gemini-api-databricks-on-aws.md](/references/query-with-the-google-gemini-api-databricks-on-aws-8dbd37cc.md)
