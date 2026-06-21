---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00f568e3f1266788998802ba8d0a5b6541ac5424d1f151695d70aecb5c2c81f1
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-workspace-feature-sharing
    - CFS
    - Cross-workspace model sharing
    - Multi-workspace data sharing
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Cross-Workspace Feature Sharing
description: The ability to discover and share feature tables across different Databricks workspaces through Unity Catalog integration.
tags:
  - collaboration
  - unity-catalog
  - feature-discovery
timestamp: "2026-06-19T09:50:53.717Z"
---

# Cross-Workspace Feature Sharing

**Cross-Workspace Feature Sharing** is a capability of [Databricks Feature Store](/concepts/databricks-feature-store.md) that allows feature tables and their associated metadata to be discovered and reused across multiple Databricks workspaces. When feature tables are registered in [Unity Catalog](/concepts/unity-catalog.md), they gain built-in governance, lineage, point-in-time joins, and cross-workspace sharing and discovery capabilities.^[databricks-feature-store-databricks-on-aws.md]

## Overview

Cross-workspace feature sharing enables organizations to centralize feature engineering efforts and promote reuse of feature definitions across teams and projects that operate in different workspaces. This eliminates redundant feature computation and ensures consistency in how features are defined and applied across models.^[databricks-feature-store-databricks-on-aws.md]

## Prerequisites

To use cross-workspace feature sharing, your workspace must be enabled for Unity Catalog. If your workspace is not enabled for Unity Catalog, see [Workspace Feature Store (Deprecated)](/concepts/workspace-feature-store-deprecated.md).^[databricks-feature-store-databricks-on-aws.md]

## How It Works

When feature tables are registered in Unity Catalog, they become accessible across workspaces through the catalog's namespace. The governance and access controls provided by Unity Catalog manage which users and service principals in other workspaces can discover and use shared features.^[databricks-feature-store-databricks-on-aws.md]

## Benefits

### Governance and Lineage

Cross-workspace feature sharing provides built-in governance and lineage tracking through Unity Catalog. When models are trained using features from shared feature tables, the system automatically tracks the relationship between features and the models that consume them. This provides a complete audit trail of feature usage across an organization.^[databricks-feature-store-databricks-on-aws.md]

### Consistency and Reusability

By sharing features across workspaces, organizations reduce the risk of training-serving skew, ensuring that feature computations used at inference are identical to those used during model training. Teams can reuse proven feature definitions rather than reimplementing them from scratch in each workspace.^[databricks-feature-store-databricks-on-aws.md]

### Point-in-Time Joins

Shared features maintain the ability to perform point-in-time joins, which is critical for time-series models and applications where feature values must reflect the state of the system at specific historical moments.^[databricks-feature-store-databricks-on-aws.md]

## Use Cases

- **Centralized feature engineering**: A data science team develops features once and shares them across multiple workspaces for different modeling projects.
- **Cross-team collaboration**: Different teams working on related problems can leverage shared feature definitions without duplicating work.
- **Enterprise-wide feature catalogs**: Organizations can maintain a single catalog of feature definitions that can be accessed by all model development projects across the company.

## Discovery

Feature tables registered in Unity Catalog are automatically discoverable in other workspaces that have access to the same Unity Catalog. This enables teams to find and reuse features that have already been defined and validated by other groups.^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — The central registry for features used in AI and ML models
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance layer that enables cross-workspace sharing
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of creating and transforming raw data into features
- [Training-serving skew](/concepts/trainingserving-skew-elimination.md) — The discrepancy between feature values at training time and inference time
- [Point-in-time Joins](/concepts/point-in-time-joins.md) — Joining features based on timestamp accuracy

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
