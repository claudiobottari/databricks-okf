---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2fc92081f7bf1457d662a422d682b2b7341b2a76865344863dfe687f34bef2c
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - openai-client-compatibility
    - OCC
    - OpenAI Client
    - OpenAI Python client library
    - OpenAI client
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: OpenAI client compatibility
description: Foundation Model APIs are compatible with the OpenAI client SDK and API, allowing users to query Databricks-hosted models using familiar OpenAI tooling.
tags:
  - api
  - integration
  - openai
timestamp: "2026-06-19T14:50:35.838Z"
---

# OpenAI Client Compatibility

**OpenAI client compatibility** refers to the ability to use the standard OpenAI client SDK to query Databricks Foundation Model APIs. This compatibility allows developers to leverage familiar tools and code patterns when working with Databricks-hosted models, reducing the learning curve and enabling rapid prototyping.

## Overview

The Databricks Foundation Model APIs are designed to be compatible with the OpenAI client. This means you can use the OpenAI Python SDK, the OpenAI JavaScript/TypeScript SDK, or any other OpenAI-compatible client to send requests to Databricks serving endpoints. ^[databricks-foundation-model-apis-databricks-on-aws.md]

This compatibility extends to both chat completion and embedding endpoints, depending on the model being used. Databricks recommends using the OpenAI client SDK or REST API for extended interactions with foundation models. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## How It Works

To use the OpenAI client with Databricks Foundation Model APIs, you configure the client to point to the Databricks workspace endpoint instead of the OpenAI API endpoint. The client then sends requests that are structurally identical to standard OpenAI API calls. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Authentication

Requests to Databricks Foundation Model APIs require a Databricks API token for authentication. This token is passed in the same way as an OpenAI API key would be, typically through the `api_key` parameter in the OpenAI client. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Endpoint Configuration

When using the OpenAI client, you set the `base_url` (or equivalent configuration) to the Databricks workspace's serving endpoint URL. The exact URL format depends on your workspace configuration and the specific model endpoint you wish to query. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Use Cases

OpenAI client compatibility enables several workflows:

- **Rapid prototyping** – Developers can test Databricks-hosted models using existing OpenAI client code without significant modification.
- **Model comparison** – Teams can easily switch between OpenAI models and Databricks-hosted models to evaluate which performs best for their use case.
- **Migration flexibility** – Applications originally built against OpenAI can be adapted to use Databricks Foundation Model APIs with minimal code changes.
- **Hybrid deployments** – Applications can use the same client code to query both OpenAI endpoints and Databricks endpoints, selecting the appropriate model per request.

## Supported Querying Methods

The table below summarizes the querying options available for Foundation Model APIs:

| Method | Use Case | OpenAI Client Compatible |
|---|---|---|
| OpenAI client SDK | Extended interactions, production workloads | Yes |
| REST API | Direct HTTP requests | Yes (API-compatible) |
| UI (Serving tab) | Trying out features | No |
| Foundation Models APIs Python SDK | Python-specific workflows | No |
| MLflow Deployments SDK | MLflow integration | No |

Databricks recommends using the OpenAI client SDK or REST API for extended interactions and the UI for trying out the feature. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Available Modes

OpenAI client compatibility works with both payment modes of Foundation Model APIs:

- **Pay-per-token** – Preconfigured endpoints that are accessible in your workspace. Ideal for getting started and low-throughput applications.
- **Provisioned throughput** – Dedicated endpoints with performance guarantees. Recommended for production workloads.

## Limitations

While the APIs are compatible with OpenAI, there may be differences in:

- Available parameters and response formats for specific models
- Rate limits and throughput constraints
- Model availability across different Databricks workspace regions

See the [Foundation Model APIs limits](/concepts/foundation-model-apis-rate-limits.md) documentation for detailed constraints.

## Requirements

To use OpenAI client compatibility, you need:

- A Databricks API token for authentication
- A workspace in a [supported region](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws)
- For provisioned throughput endpoints: [Serverless compute](/concepts/serverless-gpu-compute.md) enabled

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of the Databricks-hosted model service
- [OpenAI SDK](/concepts/openai-api-compatibility-in-databricks.md) – The standard client library for OpenAI-compatible APIs
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) – The broader serving infrastructure
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) – Dedicated endpoints with performance guarantees
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) – Preconfigured endpoints for easy access

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
