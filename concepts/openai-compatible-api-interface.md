---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca80bd3df448335a857711a153f61fbaa0fe76e150e4c413c7a8a9507b7592c7
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - openai-compatible-api-interface
    - OAI
    - OpenAI-Compatible API
    - OpenAI-compatible API
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: OpenAI-compatible API interface
description: Foundation Model APIs are compatible with the OpenAI client SDK and API, allowing users to use the OpenAI client for querying supported models.
tags:
  - api
  - compatibility
  - openai
  - databricks
timestamp: "2026-06-18T15:07:30.731Z"
---

# OpenAI-compatible API Interface

**OpenAI-compatible API interfaces** are REST API endpoints that implement the same request and response formats as the OpenAI API, allowing applications built for the OpenAI ecosystem to work with alternative providers like [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) without modifying client code.^[databricks-foundation-model-apis-databricks-on-aws.md]

## Overview

The Foundation Model APIs on Databricks are compatible with OpenAI, so you can use the OpenAI client SDK or API for querying supported models. In addition to the OpenAI client, you can also use the UI, the Foundation Models APIs Python SDK, the MLflow Deployments SDK, or the REST API directly. Databricks recommends using the OpenAI client SDK or API for extended interactions and the UI for trying out the feature.^[databricks-foundation-model-apis-databricks-on-aws.md]

## Using the OpenAI-Compatible Endpoint

To query an endpoint using the OpenAI Python client, provide Your Databricks workspace URL as the `base_url`, append the appropriate path (e.g. `/api/2.0/inference/chat/completions`), and authenticate with a Databricks API token. The request and response schemas follow OpenAI conventions.^[databricks-foundation-model-apis-databricks-on-aws.md]

### Supported Endpoints

The OpenAI-compatible interface supports the following common operations:

- **Chat completions** — `POST /api/2.0/inference/chat/completions`
- **Embeddings** — `POST /api/2.0/inference/embeddings`
- **Streaming** — Server-sent events for real-time token output

## Modes of Use

The Foundation Model APIs can be used in three modes, each accessible through the same OpenAI-compatible interface:

- **Pay-per-token** — Preconfigured endpoints serving popular models on a per-token billing basis. Recommended for getting started.^[databricks-foundation-model-apis-databricks-on-aws.md]
- **Provisioned throughput** — Endpoints with performance guarantees for production workloads. Supports base models, fine-tuned variants, and custom weights/tokenizers.^[databricks-foundation-model-apis-databricks-on-aws.md]
- **AI Functions for batch inference** — Recommended for batch processing using any generative AI or ML model.^[databricks-foundation-model-apis-databricks-on-aws.md]

## Requirements

- A Databricks API token for authentication.
- Serverless compute (for provisioned throughput models).
- A workspace in a supported region (see [region support](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws)).^[databricks-foundation-model-apis-databricks-on-aws.md]

## Benefits

The OpenAI-compatible interface allows you to use the same client libraries, tooling, and workflows you already know while taking advantage of Databricks' hosted foundation models, including open-source models from the Databricks Marketplace and Hugging Face. It also simplifies switching between providers or comparing models.^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- Foundation Model REST API reference — Detailed parameter and syntax documentation
- Use foundation models — Scoring examples and usage guidance
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) — Deployment guide for production workloads
- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) — Access control for foundation models
- [Model Serving](/concepts/model-serving.md) — Underlying infrastructure

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
