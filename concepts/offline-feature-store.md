---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46b3c576f7adbc72f98eb0ead2fc1df20244632bc5092d5b8694b5c01111c438
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - offline-feature-store
    - OFS
    - Offline Store
    - offline store
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
title: Offline Feature Store
description: The storage layer for feature tables materialized as Delta tables, used for feature discovery, model training, and batch inference.
tags:
  - feature-store
  - delta
  - batch
timestamp: "2026-06-19T18:12:45.319Z"
---

# Offline Feature Store

The **Offline Feature Store** is the component of a [Feature Store](/concepts/feature-store.md) used for feature discovery, model training, and batch inference. It stores feature data as materialized [Delta tables](/concepts/delta-lake-table.md) and serves as the authoritative source for historical and analytical feature computations. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Overview

In the [Databricks Feature Store](/concepts/databricks-feature-store.md) architecture, the offline store is the primary repository where feature tables are created, updated, and managed. Feature engineering code transforms raw data into features, which are then written to feature tables backed by Delta tables in the offline store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

The offline store supports both batch and streaming writes. You can write feature values from streaming sources, and feature computation code can leverage [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to transform raw data streams into features. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Use Cases

The offline feature store serves three primary use cases:

- **Feature discovery**: Data scientists can browse and find existing features for reuse across different models and teams.
- **Model training**: Training datasets are created by joining [FeatureLookup](/concepts/featurelookup.md) specifications with label data, pulling feature values from offline feature tables.
- **Batch inference**: When models are used for batch scoring, feature values are retrieved from the offline store and joined with new data prior to prediction. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Relationship to the Online Feature Store

While the offline store is the source of truth for training and batch workflows, the [Online Feature Store](/concepts/online-feature-store.md) provides low-latency access to feature data for real-time model serving. You can publish feature tables from the offline store to an online store for real-time inference scenarios. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

The offline store and online store remain consistent through publishing workflows. [FeatureSpec](/concepts/featurespec.md) entities always reference the offline feature tables, but must be published to an online store for real-time serving. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Implementation

In workspaces enabled for [Unity Catalog](/concepts/unity-catalog.md), any Delta table with a primary key constraint can serve as a feature table in the offline store. Feature table metadata tracks the data sources from which the table was generated and the notebooks and jobs that created or wrote to the table. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The centralized repository that includes both offline and online components
- [Online Feature Store](/concepts/online-feature-store.md) — The low-latency serving layer for real-time inference
- [Feature Tables](/concepts/feature-table.md) — Organized collections of features backed by Delta tables
- [FeatureLookup](/concepts/featurelookup.md) — Defines which features to use and how to join them during training
- [FeatureSpec](/concepts/featurespec.md) — A Unity Catalog entity combining feature lookups and functions
- [Model Packaging](/concepts/model-packaging.md) — How models retain references to offline features for inference
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables with point-in-time lookup support

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
