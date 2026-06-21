---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db4c3a3d7680a3f815394e164b48e11f30c23c85e2e494737c28357f3a787ff2
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - workspace-feature-store-deprecated-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - feature-table
    - Feature Table Metadata
    - Feature table metadata
    - Publish a Feature Table
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - file: workspace-feature-store-deprecated-databricks-on-aws.md
title: Feature Table
description: An organized collection of features backed by a Delta table with a primary key and additional metadata tracking data sources, notebooks, and jobs.
tags:
  - machine-learning
  - feature-store
  - data-engineering
timestamp: "2026-06-19T09:51:00.572Z"
---

# Feature Table

A **Feature Table** is a fundamental organizational unit in a [Feature Store](/concepts/feature-store.md) that groups related features together for use in machine learning workflows. Each feature table is backed by a [Delta table](/concepts/delta-lake-table.md) and includes additional metadata that tracks data sources, lineage, and computation history. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Overview

Feature tables centralize the storage and management of features — the transformed data inputs used to train machine learning models. By organizing features into tables with defined primary keys, the Feature Store ensures that the same feature computations are used during both model training and inference, preventing training-serving skew. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Key Characteristics

### Primary Key Requirement

Every feature table must have a primary key constraint. This key is used to join feature values with training data and inference requests. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Delta Table Backing

Feature tables are materialized as [Delta tables](/concepts/delta-lake-table.md), providing ACID transactions, schema enforcement, and time travel capabilities. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Metadata Tracking

Feature table metadata tracks:
- The data sources from which the table was generated
- The notebooks and jobs that created or wrote to the table
- Lineage information connecting features to models, notebooks, jobs, and endpoints ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Types of Feature Tables

### Unity Catalog Feature Tables

In workspaces enabled for [Unity Catalog](/concepts/unity-catalog.md), any Delta table with a primary key can serve as a feature table. This approach provides centralized governance, discoverability, and lineage tracking across the organization. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Workspace Feature Tables (Legacy)

Workspace Feature Store is available only for workspaces created before August 19, 2024, 4:00:00 PM (UTC). It is deprecated, and Databricks recommends using [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) instead. ^[workspace-feature-store-deprecated-databricks-on-aws.md]

### Time Series Feature Tables

Time series feature tables include a timestamp column that enables point-in-time lookups. These are essential when feature values change over time, such as with time series data, event-based data, or time-aggregated data. When you create a time series feature table, you specify time-related columns in your primary keys using the `timeseries_columns` argument (for Unity Catalog) or the `timestamp_keys` argument (for Workspace Feature Store). ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Working with Feature Tables

### Creating Feature Tables

Feature tables are created by writing a Spark DataFrame containing the desired features to a Delta table with a primary key constraint. The computation code that generates the features is typically reusable across training and inference. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Publishing to Online Stores

Feature tables can be published to an [Online Feature Store](/concepts/online-feature-store.md) for real-time model inference. This enables low-latency access to pre-computed features during model serving. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Streaming Support

Feature tables support both batch writes and streaming writes. Feature computation code can utilize [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to transform raw data streams into features, and feature tables can be streamed from the offline store to an online store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Feature Lookups

To train a model using features from a feature table, you create a `FeatureLookup` that specifies:
- The name of the feature table
- The features (columns) to select from the table
- The lookup key to use when joining features to create a training dataset

Multiple `FeatureLookup` objects from different feature tables can be combined to create a training set. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The centralized repository for managing features
- [FeatureLookup](/concepts/featurelookup.md) — Specifies which features to use from a feature table
- [FeatureSpec](/concepts/featurespec.md) — A Unity Catalog entity defining a reusable set of features and functions
- [Training Set](/concepts/training-set-feature-store.md) — A combination of features and raw training data
- [Online Feature Store](/concepts/online-feature-store.md) — Low-latency serving of feature data
- [Offline Store](/concepts/offline-feature-store.md) — Feature storage for discovery, training, and batch inference
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The recommended approach for managing features

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md
- workspace-feature-store-deprecated-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
2. [workspace-feature-store-deprecated-databricks-on-aws.md](/references/workspace-feature-store-deprecated-databricks-on-aws-a64a8491.md)
