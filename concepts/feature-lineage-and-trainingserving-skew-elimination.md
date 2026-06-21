---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ba79d77572092a449053fd39ed7447ac77f6c32c65526d5628dccf8d778e81a
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-lineage-and-trainingserving-skew-elimination
    - Training/Serving Skew Elimination and Feature Lineage
    - FLATSE
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Feature Lineage and Training/Serving Skew Elimination
description: Models automatically track lineage to training features and look up latest values at inference, ensuring identical feature computations between training and serving.
tags:
  - machine-learning
  - mlops
  - lineage
timestamp: "2026-06-18T11:36:42.312Z"
---

# Feature Lineage and Training/Serving Skew Elimination

**Feature Lineage** records the connection between a trained model and the specific features (from [Databricks Feature Store](/concepts/databricks-feature-store.md)) that were used during model training. **Training/Serving Skew Elimination** ensures that the same feature computations applied during training are consistently applied at inference time, preventing discrepancies that degrade model performance. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

When a model is trained using features from the Databricks Feature Store, the Feature Store automatically captures lineage — a traceable link between the model and the feature tables, columns, and versions that were used. This lineage is stored in [Unity Catalog](/concepts/unity-catalog.md), providing built-in governance and discoverability. At inference time, the Feature Store automatically retrieves the latest feature values for the input data, using the same computation logic that was used during training. ^[databricks-feature-store-databricks-on-aws.md]

## How Feature Lineage Works

1. **Training**: A model is trained on a feature DataFrame constructed by joining feature tables from the Feature Store. The Feature Store records metadata about which features (e.g., table, column, version) were accessed.
2. **Registration**: The model and its lineage are registered in Unity Catalog, enabling cross-workspace sharing and audit trails.
3. **Lineage Tracking**: Any authorized user can inspect the lineage to see exactly which features influenced the model, ensuring reproducibility and compliance. ^[databricks-feature-store-databricks-on-aws.md]

## How Training/Serving Skew Is Eliminated

Training/serving skew occurs when the logic for computing features differs between model development and production inference. The Feature Store eliminates this skew through two mechanisms: ^[databricks-feature-store-databricks-on-aws.md]

- **Automatic Feature Lookup**: At inference time, the model uses the Feature Store to look up the latest feature values for the given input. No manual feature engineering or client-side logic is required.
- **On‑Demand Feature Computation**: For real‑time applications, the Feature Store performs all feature computation tasks — including joining, aggregating, and transforming — using the same code paths that were used during training. The Feature Store handles all feature computation tasks, so the client code only needs to pass the raw input identifiers.

Because the Feature Store manages both lookup and computation, the feature values served during inference are guaranteed to match the feature values used to train the model. ^[databricks-feature-store-databricks-on-aws.md]

## Benefits

- **Simplified Client Code**: The client does not need to implement feature engineering logic; it simply calls the Feature Store for the required features.
- **Consistency**: The same feature transformation code runs both offline (training) and online (inference).
- **Governance**: Lineage is automatically captured and stored in Unity Catalog, supporting audit compliance and reproducibility.
- **Low Latency**: The Feature Store provides single‑click model and feature serving endpoints with millisecond latency. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — Central registry for features used in AI/ML models
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that stores feature lineage
- [Online Store](/concepts/online-feature-store.md) — Serves features with low latency for real‑time inference
- Training/Serving Skew — The problem addressed by consistent computation
- [Point-in-time Joins](/concepts/point-in-time-joins.md) — Ensures temporal consistency when joining feature tables
- Feature Governance — Managing feature metadata, access, and lineage

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
