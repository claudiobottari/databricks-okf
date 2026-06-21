---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 405761a791b0669860b5930e394714246e91944e5262b573f23385b73c3f2da4
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - openai-compatible-api-databricks
    - OA(
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: OpenAI-compatible API (Databricks)
description: Databricks Foundation Model APIs are compatible with the OpenAI client SDK and API, allowing users to use familiar OpenAI tooling to query Databricks-hosted models.
tags:
  - databricks
  - openai
  - api
  - compatibility
timestamp: "2026-06-19T09:52:02.694Z"
---

---
title: OpenAI-compatible API (Databricks)
summary: Databricks Foundation Model APIs provide an OpenAI-compatible interface for querying hosted open models, allowing use of the OpenAI client SDK or REST API.
sources:
  - databricks-foundation-model-apis-databricks-on-aws.md
kind: concept
createdAt: "2026-07-07T12:00:00.000Z"
updatedAt: "2026-07-07T12:00:00.000Z"
tags:
  - databricks
  - openai
  - api
  - model-serving
aliases:
  - openai-compatible-api-databricks
  - OCAPI
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# OpenAI-compatible API (Databricks)

The **OpenAI-compatible API** on Databricks refers to the ability to query Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md) using the same client libraries and request format as OpenAI’s API. This compatibility allows developers to reuse existing code and tools designed for OpenAI models when working with state-of-the-art open models hosted by Databricks. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Overview

Foundation Model APIs provide access to Databricks-hosted open models through serving endpoints. The APIs are designed to be compatible with OpenAI, meaning you can use the standard OpenAI client SDK to make requests. Databricks recommends using the OpenAI client SDK or the direct REST API for extended interactions, while the Databricks workspace UI can be used for trying out the feature. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## How to Use

To query a foundation model using the OpenAI-compatible API, you need a Databricks API token for authentication and a workspace in a supported region. The endpoints are accessible under the **Serving** tab in the left sidebar of the workspace. The pay-per-token models are preconfigured and appear at the top of the Endpoints list. ^[databricks-foundation-model-apis-databricks-on-aws.md]

You can query the models using:
- The OpenAI client SDK (recommended for extended interactions)
- The Databricks Foundation Models Python SDK
- The MLflow Deployments SDK
- The direct REST API
- The workspace UI (for experimentation)

See [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models) for scoring examples. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Modes

The Foundation Model APIs offer three modes, each with OpenAI-compatible access:

- **Pay-per-token**: Preconfigured endpoints billed per token. Recommended for getting started and can be used for production workloads, though not designed for high-throughput. ^[databricks-foundation-model-apis-databricks-on-aws.md]
- **Provisioned throughput**: Provisioned endpoints with performance guarantees, recommended for production workloads. Supports fine-tuned models and compliance certifications like HIPAA. ^[databricks-foundation-model-apis-databricks-on-aws.md]
- **AI Functions (batch inference)**: Optimized for batch inference workloads, usable via AI Functions or batch inference pipelines. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Requirements

- A Databricks API token for authentication.
- Serverless compute (required only for provisioned throughput models).
- A workspace in a supported region (see [pay-per-token regions](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws) and [provisioned throughput regions](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws)). ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Limitations

Usage limits apply to the Foundation Model APIs; see [Foundation Model APIs limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#fmapi-limits). ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Model Serving (Databricks)](/concepts/model-serving-on-databricks.md)
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md)
- [Pay-per-token Foundation Model APIs](/concepts/pay-per-token-foundation-model-apis.md)
- [AI Functions for Batch Inference](/concepts/ai-functions-for-batch-inference.md)
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md)
- OpenAI client SDK

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
