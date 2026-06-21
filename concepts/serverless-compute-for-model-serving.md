---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51253e0ec32b2f28c91c3b470c449f57ce02c777af64076fc52c6d6fac4685e2
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-for-model-serving
    - SCFMS
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: Serverless Compute for Model Serving
description: The underlying serverless compute architecture that powers Model Serving, enabling automatic scaling, cost savings, and high availability without manual infrastructure management.
tags:
  - serverless
  - compute
  - scaling
  - infrastructure
timestamp: "2026-06-19T18:30:25.785Z"
---

# Serverless Compute for Model Serving

**Serverless Compute for Model Serving** is the underlying infrastructure that powers [Model Serving](/concepts/model-serving.md) on Databricks. It enables real-time and batch inference for AI and ML models without requiring users to provision or manage any compute clusters. The service automatically handles scaling, resource allocation, and infrastructure maintenance. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## How It Works

Serverless compute provides a highly available, low-latency service that dynamically scales up or down in response to demand changes. This automatic scaling reduces infrastructure costs while maintaining optimal latency performance. Each deployed model is exposed as a REST API that can be integrated into web or client applications. ^[deploy-models-using-model-serving-databricks-on-aws.md]

Model Serving endpoints can support over 25,000 queries per second with overhead latency of less than 50 milliseconds. The infrastructure is designed for production reliability and includes multiple layers of security. Network access to serving endpoints can be controlled by configuring network policies for serverless egress control. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Requirements and Enablement

To use serverless compute for Model Serving, the account admin must read and accept the terms and conditions for enabling serverless compute in the account console. For workspaces created after March 28, 2022, serverless compute is enabled by default. If the workspace was created before that date, the admin must manually enable it from the feature enablement tab in the account console settings. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Data Protection

Databricks implements strong security controls to protect data processed through serverless compute:

- Every customer request is logically isolated, authenticated, and authorized.
- All data at rest is encrypted with AES-256, and all data in transit is encrypted with TLS 1.2 or higher.
- For paid accounts, user inputs and outputs are never used to train models or improve Databricks services.

Container build logs are retained for up to 30 days, and metrics data for up to 14 days. ^[deploy-models-using-model-serving-databricks-on-aws.md]

For [Foundation Model APIs](/concepts/foundation-model-apis.md) served via serverless compute, Databricks may temporarily process and store inputs and outputs to detect and mitigate abuse. These artifacts are isolated per customer, stored in the same region as the workspace for up to 30 days, and accessed only for security or abuse concerns. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Models You Can Deploy

Serverless compute supports the following model types on Model Serving:

- **Custom models** packaged in MLflow format (scikit‑learn, XGBoost, PyTorch, Hugging Face, etc.), including agents built with the Databricks Agent Framework.
- **Databricks-hosted foundation models** (e.g., Meta Llama, Mistral) available through Foundation Model APIs with pay‑per‑token or provisioned throughput pricing.
- **Externally hosted foundation models** (e.g., GPT‑4 from OpenAI) accessed via [External Models](/concepts/external-models.md), with centralized governance from Databricks.

^[deploy-models-using-model-serving-databricks-on-aws.md]

## Limitations and Region Availability

Serverless compute for Model Serving imposes default limits to ensure reliable performance. Users should review Model Serving limits and regions for specific constraints. If an endpoint is needed in an unsupported region, contact the Databricks account team. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The unified deployment interface that uses serverless compute.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Optimized serving for curated foundation models.
- [External Models](/concepts/external-models.md) — Governance and query layer for third‑party LLM providers.
- [AI Functions](/concepts/ai-functions.md) — SQL‑based batch inference integration.
- [AI Gateway](/concepts/ai-gateway.md) — Usage limits, monitoring, and guardrails for serving endpoints.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Cost controls for serverless workloads.

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
