---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b688a9fa0807511006f0c1e63a83782a47ee08aaf083955ce05cedc3fdfac22
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-feature-computation-and-serving
    - Serving and Online Feature Computation
    - OFCAS
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Online Feature Computation and Serving
description: On-demand computation of features for real-time applications with millisecond-latency serving endpoints.
tags:
  - real-time
  - feature-serving
  - machine-learning
timestamp: "2026-06-19T18:11:51.336Z"
---

# Online Feature Computation and Serving

**Online Feature Computation and Serving** refers to the ability to compute and retrieve feature values in real time for machine learning inference. In the context of Databricks Feature Store, this capability is built into the platform, enabling low-latency feature lookups and on-demand feature computation without requiring client-side engineering. ^[databricks-feature-store-databricks-on-aws.md]

## On-Demand Feature Computation

Databricks Feature Store provides on-demand computation of features for real-time applications. When a model is trained using features from the Feature Store, the system automatically handles all feature computation tasks at inference time. The model automatically looks up the latest feature values from the online store, and if a feature requires computation (e.g., a transformation or aggregation), that computation is performed on demand. ^[databricks-feature-store-databricks-on-aws.md]

This eliminates training/serving skew — the discrepancy between how features are computed during training versus inference — because the same feature definitions used during training are used at serving time. ^[databricks-feature-store-databricks-on-aws.md]

## Online Serving and Endpoints

Databricks provides model and feature serving endpoints that are available with a single click and that deliver millisecond‑level latency. These endpoints expose the feature values stored in online stores (e.g., in a key‑value database) so that production applications can retrieve them with minimal overhead. When feature tables are published to online stores, complex data types such as `ArrayType` and `MapType` are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## Benefits

- **Simplified client‑side code**: Because all feature lookups and computation are handled by Databricks Feature Store, the inference client does not need to implement feature engineering logic. ^[databricks-feature-store-databricks-on-aws.md]
- **Consistency**: The same feature computation runs at training and inference time, eliminating a common source of production errors. ^[databricks-feature-store-databricks-on-aws.md]
- **End‑to‑end platform**: The entire workflow — from data pipelines that create feature tables, to model training, to batch and real‑time serving — takes place on a single platform. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — Central registry for features used in ML models.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that provides lineage and discovery for feature tables.
- Feature Serving — The practice of exposing feature values to production models.
- [Online Store](/concepts/online-feature-store.md) — The low‑latency store (e.g., Redis or DynamoDB) that holds feature values for real‑time serving.
- Training/Serving Skew — A misalignment between training and inference feature computations.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of transforming raw data into model‑ready features.

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
