---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a8088bab9aa2a69d0e2a5594d4f25c3e67d91ab1b44f53cf27d2661a5054628
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - point-in-time-feature-joins
    - PFJ
    - Point-in-Time Features
    - Point-in-Time Queries
    - point-in-time correct features
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Point-in-Time Feature Joins
description: The ability to join feature values based on temporal alignment, ensuring historical consistency for training datasets.
tags:
  - feature-engineering
  - time-series
  - machine-learning
timestamp: "2026-06-19T18:12:05.559Z"
---

# Point-in-Time Feature Joins

**Point-in-Time Feature Joins** are a capability of the [Databricks Feature Store](/concepts/databricks-feature-store.md) that enables correct temporal joins between feature tables and training data, preventing data leakage from future feature values. When feature tables and models are registered in [Unity Catalog](/concepts/unity-catalog.md), the Databricks Feature Store provides built-in point-in-time joins, along with governance, lineage, and cross-workspace feature sharing and discovery. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

Point-in-time joins ensure that feature values used during model training are temporally consistent with the state of the data at a given point in time. This mechanism prevents data leakage by aligning features to the timestamp of the target label, avoiding the use of future information that would not be available at prediction time. ^[databricks-feature-store-databricks-on-aws.md]

## How Point-in-Time Joins Work

When training a model with features from the Databricks Feature Store, point-in-time joins automatically associate each training event with the feature values that were current at the event's timestamp. The join condition includes a timestamp field that restricts feature lookups to rows whose validity period precedes the event time. This ensures that the model never sees information from the future during training, which is critical for accurate offline evaluation and consistent online prediction. ^[databricks-feature-store-databricks-on-aws.md]

## Benefits

- **Eliminates training/serving skew**: The same temporal logic is applied during both training and inference, ensuring that feature computations used at inference are identical to those used during model training. ^[databricks-feature-store-databricks-on-aws.md]
- **Reduces data leakage risk**: Prevents models from learning patterns based on future information in time-series and sequential prediction tasks. ^[databricks-feature-store-databricks-on-aws.md]
- **Simplifies client-side code**: All temporal join logic is handled by the Feature Store, so users do not need to manually align timestamps or implement custom join logic. ^[databricks-feature-store-databricks-on-aws.md]

## Automatic Lineage Tracking

When you use features from Databricks Feature Store to train models, the model automatically tracks lineage to the features that were used in training. At inference time, the model automatically looks up the latest feature values. Databricks Feature Store also provides on-demand computation of features for real-time applications, handling all feature computation tasks. ^[databricks-feature-store-databricks-on-aws.md]

## Requirements

To use point-in-time feature joins with Databricks Feature Store, your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md). ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — The central registry for features with built-in point-in-time joins
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enables point-in-time joins alongside lineage and sharing
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of creating features that benefit from temporal joins
- Training/Serving Skew — The inconsistency that point-in-time joins help prevent
- Data Leakage — The problem that point-in-time joins address in time-series machine learning

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
