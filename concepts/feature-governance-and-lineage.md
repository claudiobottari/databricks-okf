---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50e2133794ea454a57c1a693742c9e02bbb083d50483fa030868a34c3830c94d
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-governance-and-lineage
    - Lineage and Feature Governance
    - FGAL
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Feature Governance and Lineage
description: Built-in tracking of the origin, transformations, and usage of features across model training and inference workflows, enabled by Unity Catalog.
tags:
  - governance
  - lineage
  - mlops
timestamp: "2026-06-18T15:06:32.920Z"
---

# Feature Governance and Lineage

**Feature Governance and Lineage** refers to the built-in capabilities in [Databricks Feature Store](/concepts/databricks-feature-store.md) that track the origin, transformation, and usage of features throughout the machine learning lifecycle. When feature tables and models are registered in [Unity Catalog](/concepts/unity-catalog.md), these capabilities provide automatic lineage tracking, centralized governance, and auditability for all feature assets. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

Databricks Feature Store serves as a central registry for features used in AI and ML models. By registering feature tables and models in Unity Catalog, organizations gain built-in governance, lineage, point-in-time joins, and cross-workspace feature sharing and discovery. The entire model training workflow takes place on a single platform, including data pipelines that ingest raw data, create feature tables, train models, and perform batch inference. ^[databricks-feature-store-databricks-on-aws.md]

## Automatic Lineage Tracking

When features from Databricks Feature Store are used to train models, the model automatically tracks lineage to the features that were used in training. This lineage information is captured and stored, providing a complete record of which features contributed to which model versions. ^[databricks-feature-store-databricks-on-aws.md]

### Benefits of Automatic Lineage

- **Reproducibility**: Teams can trace which feature versions were used in any given model training run.
- **Impact analysis**: When a feature changes, teams can identify all models that depend on that feature.
- **Compliance**: Lineage records support audit requirements and regulatory compliance.
- **Debugging**: When model performance degrades, lineage helps identify whether feature changes are the root cause.

## Inference-Time Feature Lookup

At inference time, the model automatically looks up the latest feature values from the Feature Store. This eliminates training/serving skew, ensuring that the feature computations used at inference are identical to those used during model training. The system handles all feature computation tasks, including on-demand computation for real-time applications. ^[databricks-feature-store-databricks-on-aws.md]

## Governance Features

### Unity Catalog Integration

Feature tables and models registered in Unity Catalog benefit from Unity Catalog's governance capabilities, including:

- **Access control**: Fine-grained permissions on feature tables and models.
- **Audit logging**: Tracking who accessed or modified feature assets.
- **Data discovery**: Searchable catalog of available features across workspaces.
- **Cross-workspace sharing**: Features can be shared and discovered across different workspaces. ^[databricks-feature-store-databricks-on-aws.md]

### Feature Metadata

The Feature Store UI displays metadata on feature data types, providing visibility into the structure and characteristics of registered features. Supported data types include `IntegerType`, `FloatType`, `BooleanType`, `StringType`, `DoubleType`, `LongType`, `TimestampType`, `DateType`, `ShortType`, `ArrayType`, `BinaryType`, `DecimalType`, `MapType`, and `StructType`. ^[databricks-feature-store-databricks-on-aws.md]

## Simplified Client-Side Code

Feature governance and lineage significantly simplify client-side code, as all feature lookups and computation are handled by Databricks Feature Store. Data scientists and engineers do not need to write custom code for feature retrieval or computation, reducing the risk of errors and inconsistencies. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that powers feature governance and lineage.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of creating and transforming features.
- Training/Serving Skew — A common ML deployment problem that Feature Store helps eliminate.
- Model Lineage — Tracking which data and features produced a given model.
- [Point-in-time Joins](/concepts/point-in-time-joins.md) — Ensuring feature values are historically accurate for training.
- Feature Serving — Real-time and batch serving of feature values.

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
