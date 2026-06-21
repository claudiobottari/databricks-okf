---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5625f4f8deb778621d14df5ca9ef7e2b68c131a842cb7e87ea7545c264221fae
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-feature-lineage
    - AFL
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Automatic Feature Lineage
description: Models trained using Databricks Feature Store automatically track lineage to the features used during training, enabling reproducibility and governance.
tags:
  - machine-learning
  - governance
  - lineage
timestamp: "2026-06-19T14:48:37.566Z"
---

# Automatic Feature Lineage

**Automatic Feature Lineage** is a capability of [Databricks Feature Store](/concepts/databricks-feature-store.md) that automatically tracks which features from registered feature tables are used during model training. This lineage information is stored alongside the model metadata, enabling transparent governance, reproducibility, and consistent inference. ^[databricks-feature-store-databricks-on-aws.md]

## How It Works

When a model is trained using features from Databricks Feature Store, the framework automatically captures the relationship between the model and the specific feature tables (and versions) that were used. This lineage is recorded without requiring any manual instrumentation from the data scientist. ^[databricks-feature-store-databricks-on-aws.md]

At inference time, the model automatically looks up the latest feature values based on the stored lineage. Databricks Feature Store handles all feature computation tasks, including on-demand computation for real-time applications, so the client code does not need to perform any feature lookups or computations. ^[databricks-feature-store-databricks-on-aws.md]

## Benefits

- **Eliminates training/serving skew** – Because the same feature definitions and computation logic are used for both training and inference, inconsistencies between the two environments are avoided. ^[databricks-feature-store-databricks-on-aws.md]
- **Simplifies client‑side code** – All feature lookups and computation are handled server‑side by Databricks Feature Store. ^[databricks-feature-store-databricks-on-aws.md]
- **Built‑in governance** – Lineage is stored in [Unity Catalog](/concepts/unity-catalog.md), providing a single source of truth for feature provenance across the ML lifecycle. ^[databricks-feature-store-databricks-on-aws.md]
- **Automatic discovery** – Registered feature tables and their lineage are visible in the Feature Store UI, supporting cross‑workspace sharing and discovery. ^[databricks-feature-store-databricks-on-aws.md]

## Requirements

- The workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md). (Workspace‑based Feature Store does not support Unity Catalog lineage features.) ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) – Central registry for ML features.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for data and AI assets.
- Training-Serving Skew – The inconsistency that automatic lineage helps eliminate.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – The process of creating features stored in feature tables.
- Model Inference – The stage where lineage is used to retrieve correct feature values.
- [Point-in-time Joins](/concepts/point-in-time-joins.md) – A technique that ensures feature values are consistent at a given timestamp.

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
