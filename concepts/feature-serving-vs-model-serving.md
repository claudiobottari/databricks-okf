---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8fda09e19b9a2d6a65854a5dc6e2c2d7f07f4c6e145ac861d9dda0e672d1bf7e
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - feature-serving-vs-model-serving
    - FSVMS
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: Feature Serving vs Model Serving
description: The distinction between serving raw features directly via Feature Serving versus serving ML models that autonomously look up features via Model Serving, as depicted in the document's decision diagram.
tags:
  - architecture
  - machine-learning
  - databricks
timestamp: "2026-06-19T10:30:14.141Z"
---

# Feature Serving vs Model Serving

**Feature Serving** and **Model Serving** are two distinct serving capabilities within the Databricks platform that serve different purposes in the machine learning lifecycle. While both provide low-latency, high-availability endpoints, Feature Serving serves structured data (features) directly, whereas Model Serving serves model predictions.

## Overview

Feature Serving makes data stored in the Databricks platform available to models or applications deployed outside of Databricks. It serves structured data for retrieval augmented generation (RAG) applications, as well as features required for models served outside of Databricks or any other application that requires features based on data in Unity Catalog. ^[feature-serving-endpoints-databricks-on-aws.md]

Model Serving, by contrast, serves machine learning models and returns predictions. When a model served through Model Serving was built using features from Databricks, the model automatically looks up and transforms features for inference requests. ^[feature-serving-endpoints-databricks-on-aws.md]

## Key Differences

| Aspect | Feature Serving | Model Serving |
|--------|----------------|---------------|
| **Purpose** | Serves structured feature data (e.g., customer profiles, spending metrics) | Serves model predictions (e.g., classification scores, generated text) |
| **Entity served** | A `FeatureSpec` — a user-defined set of features and functions stored in Unity Catalog | A trained model (e.g., MLflow model, custom model) |
| **Output** | Feature values (e.g., `average_yearly_spend`, `country`) | Model inference results (e.g., predicted class, probability) |
| **Use case** | Providing features to external models, RAG applications, or any application needing structured data from Unity Catalog | Real-time inference, batch scoring, or online model serving |
| **Integration** | Can be queried independently via REST API, MLflow Deployments SDK, or UI | Can be queried via REST API, MLflow Deployments SDK, or UI |

## When to Use Each

### Use Feature Serving when:
- You need to serve structured feature data to models deployed outside of Databricks. ^[feature-serving-endpoints-databricks-on-aws.md]
- You are building a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) application that requires feature lookups. ^[feature-serving-endpoints-databricks-on-aws.md]
- Any application requires features based on data in Unity Catalog but does not need model inference. ^[feature-serving-endpoints-databricks-on-aws.md]

### Use Model Serving when:
- You need to serve a trained model for real-time predictions.
- You want the model to automatically look up and transform features from Databricks during inference. ^[feature-serving-endpoints-databricks-on-aws.md]

## Combined Usage

The two services can be used together. When a model served via Model Serving was built using features from Databricks, the model automatically performs feature lookups and transformations for each inference request. Feature Serving provides a way to serve those same features independently to external systems that need the raw feature data rather than model predictions. ^[feature-serving-endpoints-databricks-on-aws.md]

## Infrastructure and Management

Both Feature Serving and Model Serving share common infrastructure characteristics:

- **Automatic scaling**: Endpoints automatically scale up and down to adjust to real-time traffic. ^[feature-serving-endpoints-databricks-on-aws.md]
- **High availability**: Both provide low-latency, high-availability serving. ^[feature-serving-endpoints-databricks-on-aws.md]
- **Security**: Endpoints are deployed in a secure network boundary using dedicated compute that terminates when the endpoint is deleted or scaled to zero. ^[feature-serving-endpoints-databricks-on-aws.md]
- **API access**: Both can be queried using the REST API, MLflow Deployments SDK, or the Serving UI. ^[feature-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — Detailed setup and management of Feature Serving endpoints
- [Model Serving](/concepts/model-serving.md) — Serving machine learning models for inference
- [FeatureSpec](/concepts/featurespec.md) — The user-defined set of features and functions served by Feature Serving
- [Online Feature Store](/concepts/online-feature-store.md) — The source of pre-materialized features for Feature Serving
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer for features and models
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — A common use case for Feature Serving

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
