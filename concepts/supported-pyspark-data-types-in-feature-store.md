---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 041ff10fbb292e1ffe49363e5ad35fcaf9661e89565b8687f101f1ce8bc45f29
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-pyspark-data-types-in-feature-store
    - SPDTIFS
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Supported PySpark Data Types in Feature Store
description: Feature Store supports PySpark types including IntegerType, FloatType, ArrayType, MapType, StructType, and others, with ArrayType and MapType stored as JSON in online stores.
tags:
  - data-types
  - pyspark
  - databricks
timestamp: "2026-06-18T11:36:39.670Z"
---

# Supported PySpark Data Types in Feature Store

Databricks Feature Store and the legacy Workspace Feature Store support a specific set of [PySpark data types](/concepts/supported-pyspark-data-types-for-features.md) for features stored in feature tables. The supported types cover common machine learning use cases including dense and sparse vectors, embeddings, text, and structured data. ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types

The following table lists all supported PySpark data types, along with notes on version availability for types that were added after the initial release.

| PySpark Data Type | Notes |
|-------------------|-------|
| `IntegerType` | |
| `FloatType` | |
| `BooleanType` | |
| `StringType` | |
| `DoubleType` | |
| `LongType` | |
| `TimestampType` | |
| `DateType` | |
| `ShortType` | |
| `ArrayType` | |
| `BinaryType` | Supported in Feature Engineering in Unity Catalog (all versions) and Workspace Feature Store v0.3.5 or above |
| `DecimalType` | Supported in Feature Engineering in Unity Catalog (all versions) and Workspace Feature Store v0.3.5 or above |
| `MapType` | Supported in Feature Engineering in Unity Catalog (all versions) and Workspace Feature Store v0.3.5 or above |
| `StructType` | Supported in Feature Engineering v0.6.0 or above |

^[databricks-feature-store-databricks-on-aws.md]

## Usage Guidance

The supported data types enable a wide range of feature representations common in machine learning: ^[databricks-feature-store-databricks-on-aws.md]

- **Dense vectors, tensors, and embeddings** can be stored as `ArrayType`.
- **Sparse vectors, tensors, and embeddings** can be stored as `MapType`.
- **Text** can be stored as `StringType`.

When features are published to online stores, `ArrayType` and `MapType` are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## Version Compatibility

- All listed types are available in Feature Engineering in [Unity Catalog](/concepts/unity-catalog.md).
- Older Workspace Feature Store versions support the basic types (`IntegerType`, `FloatType`, etc.) but require v0.3.5 or above for `BinaryType`, `DecimalType`, and `MapType`.
- `StructType` requires Feature Engineering v0.6.0 or above. ^[databricks-feature-store-databricks-on-aws.md]

## Metadata in the UI

The Feature Store UI displays metadata about feature data types, including complex types such as `ArrayType`, `MapType`, and `StructType`. This helps users understand the structure of features when browsing the catalog. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — Central registry for features used in AI and ML models
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The current version of Databricks Feature Store
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — Legacy version (deprecated) for workspaces not enabled for Unity Catalog
- [PySpark Data Types](/concepts/supported-pyspark-data-types-for-features.md) — Official Apache Spark documentation on supported SQL data types
- [Online Store](/concepts/online-feature-store.md) — Low-latency storage for serving features in production
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for managing feature tables and models

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
