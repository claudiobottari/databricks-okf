---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2ff46594c89f7dc59828586bbb34d0f9e4ce17270088edf2bfddf091bef9f72
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-models-on-model-serving
    - CMOMS
    - Custom Models in Model Serving
    - Custom model serving
    - Custom models overview
    - Custom models|Custom models
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: Custom Models on Model Serving
description: Python MLflow-packaged models (scikit-learn, PyTorch, Hugging Face, etc.) registered in Unity Catalog or Workspace Model Registry that can be deployed on Databricks for real-time and batch inference, including agent serving.
tags:
  - custom-models
  - mlflow
  - databricks
timestamp: "2026-06-18T15:26:30.119Z"
---

---
title: Custom Models on Model Serving
summary: Deployment of Python models packaged in MLflow format (e.g., scikit-learn, PyTorch, Hugging Face) as scalable REST API endpoints on Databricks.
sources:
  - deploy-models-using-model-serving-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:59:27.849Z"
updatedAt: "2026-06-18T11:59:27.849Z"
tags:
  - mlflow
  - custom-models
  - deployment
aliases:
  - custom-models-on-model-serving
  - CMOMS
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Custom Models on Model Serving

**Custom models** are user-created machine learning models deployed on [Model Serving](/concepts/model-serving.md) for real-time inference and batch inference. Model Serving provides a unified REST API to deploy, govern, and query these models, with automatic scaling to meet demand. This functionality uses [serverless compute](/concepts/serverless-gpu-compute.md).^[deploy-models-using-model-serving-databricks-on-aws.md]

## What Are Custom Models?

Custom models are Python models packaged in the MLflow format. They can be registered either in [Unity Catalog](/concepts/unity-catalog.md) or in the [Workspace Model Registry](/concepts/workspace-model-registry.md). Common examples include models built with scikit-learn, XGBoost, PyTorch, and Hugging Face transformers. Agent serving is also supported as a custom model.^[deploy-models-using-model-serving-databricks-on-aws.md]

Each deployed custom model is available as a REST API that you can integrate into your web or client application. The service automatically scales up or down to meet changes in demand, optimizing latency while reducing infrastructure costs.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Requirements

To deploy a custom model on Model Serving, you must meet the following prerequisites:^[deploy-models-using-model-serving-databricks-on-aws.md]

- A registered model in Unity Catalog or the Workspace Model Registry.
- Appropriate permissions on the registered models (see [Serving Endpoint ACLs](/concepts/serving-endpoint-acls.md)).
- MLflow 1.29 or higher.
- Workspace entitlements configured (see [Manage entitlements](/concepts/manage-privilege.md)).

## Enable Model Serving for Your Workspace

To use Model Serving, an account admin must accept the terms and conditions for enabling serverless compute in the account console. If your account was created after March 28, 2022, serverless compute is enabled by default. Once accepted, no additional workspace-level steps are required.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Deploying and Querying Custom Models

You can deploy custom models through the Serving UI or the MLflow Deployment API. For an introductory tutorial, see Tutorial: Deploy and query a custom model. Model Serving also provides the [AI Gateway](/concepts/ai-gateway.md) for managing permissions, usage limits, and monitoring across all endpoint types, including custom models.^[deploy-models-using-model-serving-databricks-on-aws.md]

For batch inference, you can use [AI Functions](/concepts/ai-functions.md) (such as `ai_query`) with custom models deployed on Model Serving. This allows direct SQL integration into analytics workflows.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Limitations and Region Availability

Model Serving imposes default limits to ensure reliable performance. For details, see Model Serving limits and regions. If you have feedback on these limits or need support in an unsupported region, contact your Databricks account team.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Data Protection

Model Serving encrypts all data at rest (AES-256) and in transit (TLS 1.2+). Every customer request is logically isolated, authenticated, and authorized. For all paid accounts, Databricks does not use user inputs or outputs to train models or improve services. Container build logs are retained for up to 30 days, and metrics data for up to 14 days.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks-hosted foundation models for pay-per-token or provisioned throughput
- [External Models](/concepts/external-models.md) — Foundation models hosted outside Databricks (e.g., OpenAI, Anthropic) accessible through Model Serving
- [AI Playground](/concepts/ai-playground.md) — A chat-like environment to test and compare LLMs
- [Serving Endpoint ACLs](/concepts/serving-endpoint-acls.md) — Access control for serving endpoints
- Optimize Model Serving endpoints for production — Strategies for latency-sensitive and high-throughput workloads
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring of agent-based custom models

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
