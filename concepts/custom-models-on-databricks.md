---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6d103a62ce8e110cd46c3b83f8d1a1d8b88f0c64b03e6c43e01e8299acaea93b
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-models-on-databricks
    - CMOD
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: Custom Models on Databricks
description: Python models packaged in MLflow format (scikit-learn, PyTorch, Hugging Face, etc.) registered in Unity Catalog or Workspace Model Registry for serving
tags:
  - mlflow
  - custom-models
  - unity-catalog
timestamp: "2026-06-19T10:12:34.369Z"
---

# Custom Models on Databricks

**Custom models on Databricks** are Python-based machine learning models packaged in the MLflow format that can be deployed for real-time serving and batch inference through the Model Serving platform. These models represent user-defined or organization-specific models that are not provided as pre-built foundation models by Databricks.

## Overview

Custom models on Databricks are machine learning models that you or your organization have developed and trained. They can be any MLflow-compatible Python model, including implementations using scikit-learn, XGBoost, PyTorch, and Hugging Face transformers. Custom models are registered either in [Unity Catalog](/concepts/unity-catalog.md) or in the [Workspace Model Registry](/concepts/workspace-model-registry.md).^[deploy-models-using-model-serving-databricks-on-aws.md]

## Supported Model Types

Custom models are distinct from foundation models (such as Meta Llama or Mistral-7B) which are hosted and managed by Databricks. While foundation models are available through [Foundation Model APIs](/concepts/foundation-model-apis.md) with pay-per-token pricing and optimized inference, custom models require you to provide the model artifact and deployment configuration.^[deploy-models-using-model-serving-databricks-on-aws.md]

### Custom Models Category

- **Python models packaged in MLflow format**: Any model that can be serialized using the MLflow model format is deployable as a custom model.
- **Examples include**: scikit-learn, XGBoost, PyTorch, and Hugging Face transformer models.
- **Agent support**: Agent serving is supported as a custom model, including deployment for generative AI applications.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Deployment Architecture

Custom models are served as REST API endpoints that you can integrate into web or client applications. The service provides a unified REST API and MLflow Deployment API for CRUD operations and querying tasks. Model Serving also provides a single UI to manage all your models and their respective serving endpoints.^[deploy-models-using-model-serving-databricks-on-aws.md]

### Serving Capabilities

- **Real-time and batch inference**: Custom models support both real-time serving and batch inference use cases.
- **Automatic scaling**: The service automatically scales up or down to meet demand changes, saving infrastructure costs while optimizing latency performance.
- **High availability**: The service is designed for production use, supporting over 25K queries per second with an overhead latency of less than 50 ms.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Requirements

To deploy custom models on Databricks, you must meet the following:

- **Registered model**: The model must be registered in Unity Catalog or the Workspace Model Registry.
- **Permissions**: Appropriate serving endpoint ACLs must be configured on the registered models.
- **MLflow version**: MLflow 1.29 or higher is required.
- **Workspace entitlements**: Workspace entitlements must be configured.
- **Serverless compute**: Model Serving uses serverless compute, which must be enabled for your workspace.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Integration with Other Services

Custom models on Databricks integrate with several other platform services:

- **Databricks Feature Store**: Native integration for incorporating features and embeddings into models.
- **AI Search**: Integration for improved accuracy and contextual understanding.
- **AI Functions**: Models can be accessed directly from SQL using AI Functions for easy integration into analytics workflows.
- **AI Gateway**: Central management of permissions, usage limits, and monitoring for all model types.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Security and Data Protection

Model Serving implements multiple layers of security for custom model workloads:

- **Data encryption**: All data is encrypted at rest (AES-256) and in transit (TLS 1.2+).
- **Logical isolation**: Every customer request is logically isolated, authenticated, and authorized.
- **Network policies**: You can control network access to model serving endpoints.
- **Data retention**: Container build logs are retained for up to 30 days and metrics data for up to 14 days.
- **No model training on user data**: For all paid accounts, Model Serving does not use user inputs or outputs to train models or improve services.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) - The platform for deploying and serving custom models
- [Unity Catalog](/concepts/unity-catalog.md) - Model registry for governed model management
- [Workspace Model Registry](/concepts/workspace-model-registry.md) - Alternative model registry location
- [Foundation Model APIs](/concepts/foundation-model-apis.md) - Pre-built model endpoints for quick use
- [AI Functions](/concepts/ai-functions.md) - SQL-based model access
- [MLflow](/concepts/mlflow.md) - Model packaging and deployment framework

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
