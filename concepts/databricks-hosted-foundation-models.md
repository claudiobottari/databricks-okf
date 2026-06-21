---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33a042244ca0ad3c0585ea8338674d2aa074fb2c1255524fe3870fd733ace6e2
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-foundation-models
    - DFM
    - Databricks-hosted foundation model
    - DatabricksHosted Foundation Models
    - Databricks‑hosted foundation models
    - Databricks-Hosted Foundation Models Available in Foundation Model APIs
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: Databricks-hosted foundation models
description: State-of-the-art open models hosted and managed by Databricks, available as preconfigured endpoints through Foundation Model APIs for pay-per-token and provisioned throughput modes.
tags:
  - databricks
  - models
  - llm
timestamp: "2026-06-19T09:52:00.095Z"
---

# Databricks-hosted Foundation Models

**Databricks-hosted foundation models** are state-of-the-art open models served from [Model Serving](/concepts/model-serving.md) endpoints in Databricks, eliminating the need for users to maintain their own model deployment infrastructure. These models are hosted and managed by Databricks as part of the Foundation Model APIs offering. The service is a [Databricks Designated Service](/concepts/databricks-designated-service-with-geos.md), meaning it uses Databricks Geos to manage data residency when processing customer content. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Modes of Access

Foundation Model APIs are provided in three modes: pay-per-token, provisioned throughput, and AI Functions for batch inference. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Pay-per-token

The pay-per-token mode is the easiest way to start accessing foundation models on Databricks and is recommended for beginning your journey with Foundation Model APIs. This mode is not designed for high-throughput applications, but it can be used for production workloads. Preconfigured endpoints for pay-per-token models are automatically available in the Databricks workspace under the **Serving** tab. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Provisioned Throughput

Provisioned throughput mode is recommended for all production workloads, especially those requiring high throughput, performance guarantees, fine-tuned models, or additional security requirements such as HIPAA compliance. Provisioned throughput endpoints support: ^[databricks-foundation-model-apis-databricks-on-aws.md]

- Base models of all sizes, accessible via the Databricks Marketplace, Hugging Face, or other external sources registered in [Unity Catalog](/concepts/unity-catalog.md).
- Fine-tuned variants of base models (e.g., models fine-tuned on proprietary data).
- Fully custom weights and tokenizers (e.g., models trained from scratch or continued pre-trained) and other variations using the base model architecture (for example, CodeLlama). ^[databricks-foundation-model-apis-databricks-on-aws.md]

### AI Functions for Batch Inference

The AI Functions mode is recommended for batch inference workloads. Users can run batch inference using any generative AI or ML model using AI Functions. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Use Cases

With Foundation Model APIs you can: ^[databricks-foundation-model-apis-databricks-on-aws.md]

- Query a generalized LLM to verify a project's validity before investing more resources.
- Create a quick proof-of-concept for an LLM-based application before investing in training and deploying a custom model.
- Build a chatbot using retrieval augmented generation ([RAG](/concepts/retrieval-augmented-generation-rag.md)) by combining a foundation model with a vector index.
- Replace proprietary models with open alternatives to optimize for cost and performance.
- Efficiently compare LLMs to find the best candidate for a use case, or swap a production model with a better-performing one.
- Build an LLM application for development or production on top of a scalable, SLA-backed serving solution.

## Requirements

- A Databricks API token to authenticate endpoint requests.
- Serverless compute (for provisioned throughput models).
- A workspace in one of the [supported regions](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws) for pay-per-token or provisioned throughput. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## How to Use

The APIs are compatible with OpenAI, so you can use the OpenAI client SDK for querying. Other options include the UI, the Foundation Models APIs Python SDK, the [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md), and the REST API. Databricks recommends using the OpenAI client SDK or API for extended interactions and the UI for trying out the feature. ^[databricks-foundation-model-apis-databricks-on-aws.md]

For scoring examples, see Use foundation models. For REST API syntax and parameters, see Foundation model REST API reference. For deploying provisioned throughput endpoints, see [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md). For batch inference, see [Deploy batch inference pipelines](/concepts/batch-inference-pipelines.md). ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Limitations

See the [Foundation Model APIs limits](/concepts/foundation-model-apis-rate-limits.md) page for details on rate limits and other constraints. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Additional Resources

- Supported pay-per-token models
- Provisioned throughput supported model architectures
- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md)
- Enrich data using AI Functions

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
