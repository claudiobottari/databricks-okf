---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9997aa80270dbc64b4e29540a9bb423b4c9dc6ae92686147f72d38f410875307
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - point-in-time-joins
    - Point-in-time join
    - Point‑in‑Time Join
    - point-in-time join
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Point-in-time Joins
description: A feature of Databricks Feature Store that enables time-accurate feature lookups, ensuring features are joined to training or inference data at the correct historical timestamp.
tags:
  - feature-engineering
  - time-series
  - data-joins
timestamp: "2026-06-18T15:06:21.794Z"
---

# Point-in-time Joins

**Point-in-time Joins** are a technique used in feature engineering and machine learning pipelines to ensure that feature values used at inference time are computed from data that was available at the specific historical timestamp being evaluated. This prevents data leakage by ensuring predictions are never made using future information that wouldn't have been available in production.

## Overview

When training machine learning models, features are often computed from historical events — such as customer transactions, sensor readings, or user interactions. A point-in-time join aligns each training example with the feature values that were current at that example's timestamp, rather than using the latest available values or values from an arbitrary time. ^[databricks-feature-store-databricks-on-aws.md]

## Why Point-in-time Joins Matter

Without point-in-time joins, feature computations can introduce **data leakage** — information from the future leaking into training data. For example, if a model predicts customer churn at time *t*, using a feature that aggregates transactions that occurred after *t* would give the model access to information it wouldn't have in production, inflating evaluation metrics and degrading real-world performance. ^[databricks-feature-store-databricks-on-aws.md]

## Implementation in Feature Stores

Databricks Feature Store provides built-in point-in-time join capabilities as part of its feature engineering framework. When you register feature tables in Unity Catalog, the system tracks the timestamp associated with each feature value and automatically performs point-in-time lookups during training and inference. ^[databricks-feature-store-databricks-on-aws.md]

### Training Workflow

During model training, the Feature Store:

1. Identifies the timestamp for each training example (e.g., the date of the prediction event).
2. For each feature, retrieves the most recent value that was recorded **at or before** that timestamp.
3. Assembles the feature vector for training without including any future information.

This ensures that the training data reflects the same information that would be available at inference time. ^[databricks-feature-store-databricks-on-aws.md]

### Inference Workflow

At inference time, the model automatically looks up the latest feature values from the Feature Store, but with point-in-time semantics, the lookup still respects temporal ordering if the inference request includes a timestamp. For real-time serving, the system uses the current time as the reference point, ensuring consistency between training and serving. ^[databricks-feature-store-databricks-on-aws.md]

## Benefits

- **Eliminates training/serving skew** — Feature computations used at inference are guaranteed to be the same as those used during model training, preventing the common problem where production feature pipelines produce different results than training pipelines. ^[databricks-feature-store-databricks-on-aws.md]
- **Simplifies client-side code** — All feature lookups and temporal alignment are handled by the Feature Store, so application code doesn't need to manage timestamps or implement point-in-time logic. ^[databricks-feature-store-databricks-on-aws.md]
- **Built-in lineage** — When models are trained using features from the Feature Store, lineage is automatically tracked, showing which feature values were used and when they were computed. ^[databricks-feature-store-databricks-on-aws.md]

## Relationship to Feature Freshness

Point-in-time joins are related to the concept of feature freshness — how recently feature values were updated. While point-in-time joins ensure temporal correctness, feature freshness policies determine how often features are recomputed and how stale values are acceptable for different use cases.

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — The central registry for ML features with built-in point-in-time support
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The framework for developing and registering feature tables
- Training/Serving Skew — The problem that point-in-time joins help prevent
- Temporal Data Leakage — A type of data leakage caused by improper time-based feature computation
- [Feature Lineage](/concepts/feature-lineage-tracking.md) — Automatic tracking of which features were used in model training

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
