---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 272e4945363ae80cf01590bda91ee31af4945db86c85b019785b3da497aa30f6
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
    - deploy-models-using-model-serving-databricks-on-aws.md
    - migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - foundation-model-apis
    - FMA
    - FMAPI Foundation Model APIs
    - Foundation Model
    - Foundation Model API
    - Foundation Model APIs (FMAPI)
    - Foundation Model APIs regions
    - Foundation Model Types
    - Foundation Models
    - Foundation Models APIs
    - Foundation model types
    - Foundational Model APIs
    - Foundational Model APIs (FMAPI)
    - Use Foundation Models
    - Use foundation models
    - foundation model
    - foundation models
    - Foundation Model APIs overview
    - Foundation Model REST API Reference
    - available foundation models
    - scoring foundation models
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
    - file: deploy-models-using-model-serving-databricks-on-aws.md
    - file: migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
title: Foundation Model APIs
description: Databricks-curated set of state-of-the-art open foundation model architectures (e.g., Meta-Llama-3.3-70B-Instruct) supporting optimized inference with pay-per-token or provisioned throughput pricing.
tags:
  - model-serving
  - foundation-models
  - inference
timestamp: "2026-06-19T18:01:57.086Z"
---

# Foundation Model APIs

**Foundation Model APIs** is the Databricks offering that provides access to curated, optimized foundation models hosted on Databricks infrastructure. These models are based on state-of-the-art open architectures (e.g., Meta-Llama-3.3-70B-Instruct, GTE-Large) and support optimized inference for real-time and batch workloads. Foundation Model APIs are part of [Model Serving](/concepts/model-serving.md) and offer two primary pricing models: **pay-per-token** and **provisioned throughput**. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, deploy-models-using-model-serving-databricks-on-aws.md]

## Overview

Foundation Model APIs deliver curated foundation model architectures that support optimized inference. Base models such as Meta-Llama-3.3-70B-Instruct and GTE-Large are available for immediate use. The offering provides three consumption modes: pay-per-token for experimentation and low-volume workloads, provisioned throughput for production use cases with performance guarantees, and integration with [AI Functions](/concepts/ai-functions.md) for batch inference. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, deploy-models-using-model-serving-databricks-on-aws.md]

Databricks automatically creates pay-per-token endpoints for supported models in your workspace. These endpoints appear at the top of the Serving endpoints list and can be queried using a unified REST API that is OpenAI-compatible. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, deploy-models-using-model-serving-databricks-on-aws.md]

## Serving Options

### Pay-per-Token (Token-Based)

Pay-per-token endpoints let you query pre-configured Databricks-hosted foundation models without upfront infrastructure commitments. Databricks automatically creates these endpoints in your workspace. Billing is based on the number of tokens processed. You cannot modify the endpoint configuration; they are pre-provisioned by Databricks. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

### Provisioned Throughput

Provisioned throughput provides endpoints with performance guarantees for production workloads. It supports deployment of both base and fine-tuned models. You can create provisioned throughput endpoints via the Serving UI, REST API, or MLflow Deployments SDK. Provisioned throughput uses a simpler configuration where scale-out ranges are expressed in tokens per second rather than concurrency, and customers no longer need to select GPU workload types. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

### AI Functions (Batch Inference)

Model Serving integrates with [AI Functions](/concepts/ai-functions.md) for batch inference. You can use task-specific AI Functions or `ai_query` directly in SQL without configuring a dedicated serving endpoint. This integration allows you to apply AI to your data at scale using familiar SQL syntax. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## How to Use

### Prerequisites

- A Databricks workspace in a [supported region](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions).
- A Databricks API token for authenticating endpoint requests.
- Serverless compute (for provisioned throughput models).
- Workspace entitlements configured (serverless compute is enabled by default for accounts created after March 28, 2022). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, deploy-models-using-model-serving-databricks-on-aws.md]

### Querying Models

You can query foundation models using the OpenAI-compatible REST API, the MLflow Deployments SDK, or the Databricks API. Pay-per-token endpoints are available immediately without manual creation; provisioned throughput endpoints require explicit creation via the UI, REST API, or MLflow Deployments SDK. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, deploy-models-using-model-serving-databricks-on-aws.md]

For batch inference, you can use AI Functions like `ai_query` directly in SQL without provisioning a separate endpoint. See [Enrich data using AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions). ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Data Protection

Databricks encrypts all data at rest (AES-256) and in transit (TLS 1.2+) for Model Serving. For Foundation Model APIs specifically, Databricks may temporarily process and store inputs and outputs for abuse and harm detection. These inputs and outputs are isolated per customer, stored in the same region as the workspace for up to thirty days, and only accessible for security or abuse concerns. Partner model providers may retain data for safety purposes, with automated scanning prior to any limited human review. Foundation Model APIs is a [Databricks Designated Service](https://docs.databricks.com/aws/en/resources/designated-services) that adheres to data residency boundaries. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Limitations

- Foundation Model APIs are available only in [supported regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions).
- For pay-per-token endpoints, you cannot modify the endpoint configuration; they are pre-provisioned by Databricks.
- Provisioned throughput endpoints require manual creation and are subject to compute resource availability.
- Model Serving imposes default limits to ensure reliable performance. See [Model Serving limits and regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The overarching platform for deploying AI and ML models.
- [External Models](/concepts/external-models.md) – Access foundation models hosted outside Databricks (e.g., OpenAI, Anthropic).
- [AI Functions](/concepts/ai-functions.md) – SQL-based batch inference using foundation models.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Performance-guaranteed serving for production workloads.
- [AI Playground](/concepts/ai-playground.md) – Interactive chat environment for testing LLMs within the Databricks workspace.
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) – Programmatic way to create and manage serving endpoints.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md
- deploy-models-using-model-serving-databricks-on-aws.md
- migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
2. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
3. [migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md](/references/migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws-b1657ebd.md)
