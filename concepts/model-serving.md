---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a2af24f1a6956214216490f61dfc8b37594e69f4a0491b51413d87f1502486a
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
    - machine-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-serving
    - Model Serving Logs
    - Debug Model Serving
    - Debugging Model Serving
    - LLM Serving
    - Model Serving with MLflow
    - real-time model serving
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
    - file: machine-learning-on-databricks-databricks-on-aws.md
title: Model Serving
description: Databricks' unified solution for deploying, governing, and querying AI/ML models via REST APIs for real-time and batch inference with automatic scaling.
tags:
  - machine-learning
  - deployment
  - model-serving
timestamp: "2026-06-18T11:59:10.611Z"
---

# Model Serving

**Model Serving** is the Databricks solution for deploying AI and machine learning models for real-time serving and batch inference. It provides a unified interface to deploy, govern, and query AI models as REST APIs that can be integrated into web applications, client applications, and analytics workflows.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Overview

Model Serving offers a highly available and low-latency service that automatically scales up or down to meet demand changes, reducing infrastructure costs while optimizing latency performance. The service uses serverless compute and supports over 25K queries per second with an overhead latency of less than 50 milliseconds.^[deploy-models-using-model-serving-databricks-on-aws.md]

The service provides a unified REST API and MLflow Deployment API for CRUD and querying tasks, along with a single UI to manage all models and their respective serving endpoints. Models can be accessed directly from SQL using [AI Functions](/concepts/ai-functions.md) for easy integration into analytics workflows.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Models You Can Deploy

Model Serving supports real-time and batch inference for three categories of models:^[deploy-models-using-model-serving-databricks-on-aws.md]

### Custom Models

Custom models are Python models packaged in the MLflow format, registered either in [Unity Catalog](/concepts/unity-catalog.md) or in the workspace model registry. Examples include scikit-learn, XGBoost, PyTorch, and Hugging Face transformer models. Agent serving is also supported as a custom model.^[deploy-models-using-model-serving-databricks-on-aws.md]

### Foundation Models

Foundation models include two subcategories:^[deploy-models-using-model-serving-databricks-on-aws.md]

- **Databricks-hosted foundation models** like Meta Llama and Mistral, available through Foundation Model APIs with pay-per-token pricing. Workloads requiring performance guarantees can use provisioned throughput.
- **Foundation models hosted outside of Databricks** like GPT-4 from OpenAI, accessible via [External Models](/concepts/external-models.md). These endpoints can be centrally governed from Databricks.

You can interact with supported large language models using the [AI Playground](/concepts/ai-playground.md), a chat-like environment for testing, prompting, and comparing LLMs.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Benefits

Model Serving provides several key advantages:^[deploy-models-using-model-serving-databricks-on-aws.md]

- **Unified model management**: Manage all models in one location and query them with a single API, regardless of whether they are hosted on Databricks or externally.
- **Secure customization with private data**: Integrate features and embeddings through native integration with the [Databricks Feature Store](/concepts/databricks-feature-store.md) and AI Search. Models can be fine-tuned with proprietary data.
- **Governance and monitoring**: The Serving UI enables centralized management of all model endpoints, including permissions, usage limits, and quality monitoring through [AI Gateway](/concepts/ai-gateway.md).
- **Cost optimization**: Endpoints automatically scale to meet demand, with optimized inference for large models.
- **Reliability and security**: Workloads are protected by multiple layers of security, with network policy controls for serverless egress.

## Data Protection

For all paid accounts, Model Serving does not use user inputs or outputs to train any models or improve Databricks services. Every customer request is logically isolated, authenticated, and authorized. All data is encrypted at rest (AES-256) and in transit (TLS 1.2+). Databricks retains container build logs for up to 30 days and metrics data for up to 14 days.^[deploy-models-using-model-serving-databricks-on-aws.md]

For Foundation Model APIs, Databricks may temporarily process inputs and outputs for abuse prevention. Partner model providers may retain data for safety purposes, with automated scanning prior to limited human review.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Requirements

To use Model Serving, you need:^[deploy-models-using-model-serving-databricks-on-aws.md]

- A registered model in Unity Catalog or the Workspace Model Registry
- Appropriate permissions on registered models (see [Serving Endpoint ACLs](/concepts/serving-endpoint-acls.md))
- MLflow 1.29 or higher
- Workspace entitlements configured

The account admin must accept the terms for enabling serverless compute in the account console. For accounts created after March 28, 2022, serverless compute is enabled by default.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Relationship to the Broader ML Platform

Model Serving is one component of the Databricks machine learning platform, which unifies the entire ML lifecycle from data preparation to production monitoring. The platform provides:^[machine-learning-on-databricks-databricks-on-aws.md]

- [Databricks Runtime for ML](/concepts/databricks-runtime-for-ml.md) — Pre-configured clusters with ML libraries
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking and model comparison
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — Feature creation, management, and serving
- [AI Gateway](/concepts/ai-gateway.md) — Governance and monitoring for served models
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Access to state-of-the-art open models

The platform also supports [External Models](/concepts/external-models.md) for integrating third-party model providers and [Unity Catalog](/concepts/unity-catalog.md) for governing data, features, models, and functions with unified access control.^[machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Model Endpoints](/concepts/model-serving-endpoint.md) — The specific serving endpoints created for each deployed model
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) — Deploying custom MLflow models
- [Foundation Model Serving](/concepts/foundation-model-serving-modes.md) — Deploying and querying foundation models
- External Model Endpoints — Connecting to third-party model providers
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Monitoring model quality in production
- [AI Functions](/concepts/ai-functions.md) — SQL-based batch inference integration
- Model Serving Limits — Default limits and region availability

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md
- machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
2. [machine-learning-on-databricks-databricks-on-aws.md](/references/machine-learning-on-databricks-databricks-on-aws-34650b43.md)
