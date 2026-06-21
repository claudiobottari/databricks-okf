---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 23c6dab797412ef7443078be11ad7a591d5895e467a7f3c1c481b57e934b873c
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - openai-api-compatibility-in-databricks
    - OACID
    - ACID
    - OpenAI API Compatibility (Databricks)
    - OpenAI API Compatibility (Databricks)|OpenAI's REST API format
    - OpenAI API Compatible Endpoints
    - OpenAI SDK
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: OpenAI API Compatibility in Databricks
description: Foundation Model APIs are compatible with the OpenAI client SDK and API, allowing users to use familiar OpenAI tooling to query models on Databricks.
tags:
  - openai
  - api-compatibility
  - integration
timestamp: "2026-06-19T18:13:07.978Z"
---

# OpenAI API Compatibility in Databricks

**OpenAI API Compatibility in Databricks** refers to the ability to use the OpenAI client SDK and API patterns to query Databricks Foundation Model APIs, providing a familiar interface for developers building applications with Databricks-hosted models. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Overview

The Databricks Foundation Model APIs are designed to be compatible with the OpenAI API, allowing you to use the OpenAI client library for querying supported models. Databricks recommends using the OpenAI client SDK or API for extended interactions, while the user interface is recommended for trying out the feature. ^[databricks-foundation-model-apis-databricks-on-aws.md]

This compatibility enables developers to:

- Use existing OpenAI client code with minimal modifications
- Leverage familiar API patterns for chat completion and other endpoints
- Switch between OpenAI and Databricks-hosted models without significant code changes

## Using the OpenAI-Compatible API

To use the OpenAI client with Databricks Foundation Model APIs, you need to configure the client with your Databricks workspace URL and authentication token:

```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["DATABRICKS_TOKEN"],
    base_url="https://<workspace-url>/serving-endpoints/<endpoint-name>/v1"
)

response = client.chat.completions.create(
    model="<model-endpoint-name>",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Authentication Requirements

API calls require a Databricks API token for authentication. The token must be included in the request headers when using the REST API directly or configured as the API key when using the OpenAI client SDK. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Supported API Endpoints

The OpenAI-compatible API supports the following endpoints:

- **Chat completions** (`POST /v1/chat/completions`) – Standard chat interface for conversational models
- **Embeddings** (`POST /v1/embeddings`) – Generate vector embeddings for text
- **Legacy completions** (`POST /v1/completions`) – For models that support traditional completion tasks

## Query Modes

### Pay-per-token

Preconfigured endpoints that serve pay-per-token models are accessible directly in your Databricks workspace. This mode supports OpenAI-compatible queries and is recommended for getting started with foundation models. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Provisioned Throughput

For production workloads requiring performance guarantees, provisioned throughput endpoints also support the OpenAI-compatible API. Databricks recommends this mode for production workloads with high throughput requirements. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### AI Functions for Batch Inference

For batch inference workloads, you can use [AI Functions](/concepts/ai-functions.md) with any generative AI or ML model. This mode is optimized for processing large datasets. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## SDK and API Options

Multiple options are available for querying Foundation Model APIs using the OpenAI-compatible interface:

| Option | Description |
|--------|-------------|
| **OpenAI client SDK** | Recommended for extended interactions and production applications |
| **Foundation Models APIs Python SDK** | Databricks-native Python library |
| **MLflow Deployments SDK** | For MLflow-integrated workflows |
| **REST API** | Direct HTTP requests to the serving endpoint |
| **UI** | For trying out features interactively |

^[databricks-foundation-model-apis-databricks-on-aws.md]

## Limitations

The OpenAI-compatible API is subject to the same [Foundation Model APIs limits](/concepts/foundation-model-apis-rate-limits.md) as the native Databricks API. These limits include rate limits, token limits, and other constraints specific to each model and service tier. ^[databricks-foundation-model-apis-databricks-on-aws.md]

For detailed information about specific limits, see the model serving limits documentation.

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of Databricks-hosted model serving
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) – Production-grade serving with performance guarantees
- [Pay-per-token Foundation Model APIs](/concepts/pay-per-token-foundation-model-apis.md) – Consumption-based pricing model
- [Model Serving](/concepts/model-serving.md) – General model deployment and serving infrastructure
- [Serving Endpoints](/concepts/serving-endpoint-acls.md) – How to create and manage serving endpoints
- Databricks API Token – Authentication for API access

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
