---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6302f286df222da29949a275f4525ff713753e3e3a1b1e63a255c99275bbf7d1
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-store-feature-publishing
    - OSFP
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Online Store Feature Publishing
description: The mechanism by which feature values are published to online stores for low-latency serving, with ArrayType and MapType features stored in JSON format.
tags:
  - online-serving
  - feature-store
  - inference
timestamp: "2026-06-19T09:50:51.965Z"
---

# Online Store Feature Publishing

**Online Store Feature Publishing** is the process of making features from a [Databricks Feature Store](/concepts/databricks-feature-store.md) available for low-latency real-time serving in production applications. When features are published to an online store, they can be retrieved at inference time with millisecond latency, enabling use cases such as real-time recommendations, fraud detection, and personalization. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

Databricks Feature Store provides on-demand computation of features for real-time applications, handling all feature computation tasks automatically. This eliminates training/serving skew, ensuring that the feature computations used at inference are identical to those used during model training. It also significantly simplifies client-side code, as all feature lookups and computation are handled by Databricks Feature Store. ^[databricks-feature-store-databricks-on-aws.md]

## Data Type Considerations

When features are published to online stores, certain complex data types are serialized using JSON format:

- **`ArrayType`** – Used for dense vectors, tensors, and embeddings; stored as JSON arrays.
- **`MapType`** – Used for sparse vectors, tensors, and embeddings; stored as JSON objects.

Other supported data types (e.g., `IntegerType`, `FloatType`, `StringType`, `BooleanType`, `TimestampType`) do not require JSON serialization and are stored in their native format. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) – The central registry for features used in ML models.
- [Online Store](/concepts/online-feature-store.md) – The low-latency serving layer for features.
- Training/Serving Skew – A common problem that Databricks Feature Store helps eliminate.
- Feature Serving – Serving endpoints that provide millisecond latency.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer used with Databricks Feature Store for lineage and discovery.
- Publishing to Online Stores API – The API methods for publishing feature tables to online stores (see Databricks documentation for specifics).

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
