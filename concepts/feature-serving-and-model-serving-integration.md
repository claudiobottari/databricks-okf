---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 294ca84e8cd74583fefceb46471948b87a5c4534188e9b11cf7bf7cbfd1f7337
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-serving-and-model-serving-integration
    - Model Serving Integration and Feature Serving
    - FSAMSI
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Feature Serving and Model Serving Integration
description: Online feature stores integrate with Feature Serving Endpoints and Model Serving Endpoints to automatically look up and serve features for real-time inference and applications.
tags:
  - inference
  - serving
  - real-time-ml
timestamp: "2026-06-19T14:51:44.606Z"
---

# Feature Serving and Model Serving Integration

**Feature Serving and Model Serving Integration** refers to the ability of deployed machine learning models to automatically retrieve the correct feature values from an [Online Feature Store](/concepts/online-feature-store.md) at inference time, without requiring custom lookup code. On Databricks, this integration is achieved through Unity Catalog lineage and dedicated serving endpoints.

## How the Integration Works

Models that are trained using features from Databricks automatically track lineage to the features they were trained on. When a model is deployed as a model serving endpoint, the endpoint uses Unity Catalog to look up the appropriate feature values from an online store. ^[databricks-online-feature-stores-databricks-on-aws.md]

For use cases that do not involve a pre-trained model (e.g., real-time applications such as recommendation systems, fraud detection, or personalization engines), you can create a dedicated [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) that serves feature data directly from the online store using [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md). ^[databricks-online-feature-stores-databricks-on-aws.md]

## Automatic Feature Lookup for Real-Time Inference

When a model serving endpoint is configured to use features from Databricks, it performs automatic feature lookup during real-time inference. The endpoint resolves features to the oldest online table based on creation timestamp if a feature table is published to multiple online tables. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations and Considerations

- **Multiple online stores**: Feature Serving and Model Serving endpoints that look up features from **multiple** online feature stores cannot use [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) instances. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Deleting online tables**: Deleting an online published table can cause unexpected failures in downstream dependencies. Ensure that the online features are no longer used by any model serving or feature serving endpoint before deletion. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Feature table resolution**: Specifying a specific online table is not supported; the system always resolves to the oldest online table based on creation timestamp. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Store](/concepts/online-feature-store.md) – High-performance store for serving feature data to real-time applications.
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) – Endpoints that expose feature data directly for real-time use.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – Endpoints that host trained models and can perform automatic feature lookup.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ governance layer that tracks lineage and resolves feature references.
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) – Backend infrastructure for online stores, with specific constraints for multi-store serving.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
