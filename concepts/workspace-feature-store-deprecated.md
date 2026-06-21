---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4242d6a2b00e36682bfe9b3abb9d3a76e10114e5d2e05f789f74921f1a6cfc6
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-feature-store-deprecated
    - WFS(
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Workspace Feature Store (Deprecated)
description: Legacy version of Databricks Feature Store for workspaces not enabled for Unity Catalog, now deprecated in favor of the Unity Catalog-backed Feature Store.
tags:
  - legacy
  - deprecated
  - databricks
timestamp: "2026-06-18T11:36:58.168Z"
---

# Workspace Feature Store (Deprecated)

The **Workspace Feature Store** is the legacy version of Databricks’ feature management system, available in workspaces that are not enabled for Unity Catalog. Databricks refers to it as deprecated, meaning that it is no longer the recommended solution and should be replaced by the Unity Catalog-based [Databricks Feature Store] for new and existing workloads. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

Databricks Feature Store — both the current Unity Catalog version and the Workspace Feature Store — provides a central registry for features used in AI and ML models. The Workspace Feature Store served the same core purpose but operated without Unity Catalog integration, meaning it lacked the built-in governance, lineage, point-in-time joins, and cross-workspace sharing that the Unity Catalog version offers. ^[databricks-feature-store-databricks-on-aws.md]

If your workspace is enabled for Unity Catalog, you should use the current Databricks Feature Store instead of the deprecated Workspace Feature Store. The documentation for the current version covers the full pipeline: data ingestion, feature table creation, model training, batch inference, serving endpoints, and monitoring. ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types

The Workspace Feature Store (deprecated) supports the same PySpark data types as the current Feature Store. These include:

- `IntegerType`
- `FloatType`
- `BooleanType`
- `StringType`
- `DoubleType`
- `LongType`
- `TimestampType`
- `DateType`
- `ShortType`
- `ArrayType`
- `BinaryType` (supported in Workspace Feature Store v0.3.5 or above)
- `DecimalType` (supported in v0.3.5 or above)
- `MapType` (supported in v0.3.5 or above)
- `StructType` (supported in Feature Engineering v0.6.0 or above, which applies to the legacy store as well)

^[databricks-feature-store-databricks-on-aws.md]

These data types support common machine learning feature representations: dense vectors, tensors, and embeddings can be stored as `ArrayType`; sparse vectors, tensors, and embeddings as `MapType`; and text as `StringType`. When published to online stores, `ArrayType` and `MapType` features are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## Deprecation and Migration

Databricks recommends migrating from the Workspace Feature Store to the Unity Catalog-based Databricks Feature Store. The deprecated version does not receive new features and is intended only for legacy workspaces that have not yet enabled Unity Catalog. To take advantage of full governance, lineage, and cross-workspace capabilities, administrators should enable Unity Catalog and transition workflows to the current Feature Store. ^[databricks-feature-store-databricks-on-aws.md]

For detailed migration guidance, refer to the documentation on [Databricks Feature Store].

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — The current, recommended feature store for Unity Catalog-enabled workspaces
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that underpins the current Feature Store
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The toolset for creating and managing features with Unity Catalog
- [Point-in-time Joins](/concepts/point-in-time-joins.md) — A capability available in the current Feature Store but not in the deprecated version
- [Supported Data Types in Feature Store](/concepts/supported-data-types-for-feature-stores.md) — Common data types for ML features

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
