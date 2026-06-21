---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6489bd28523e8429bb57a0edb0e9a71164d0641b78df77ef751d0a08b45b115e
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-data-types-for-feature-stores
    - SDTFFS
    - Supported Data Types for Feature Tables
    - Supported Data Types in Feature Store
    - Supported Data Types for Feature Engineering
    - Supported data types for Feature Engineering
    - data types supported by Feature Store
    - supported-pyspark-data-types-in-feature-store
    - SPDTIFS
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Supported Data Types for Feature Stores
description: Databricks Feature Store supports PySpark data types including IntegerType, FloatType, ArrayType, MapType, StructType, and others, with specific version requirements for complex types.
tags:
  - feature-store
  - data-types
  - databricks
timestamp: "2026-06-19T14:48:37.192Z"
---

# Supported Data Types for Feature Stores

**Supported Data Types for Feature Stores** defines the set of [PySpark data types](https://spark.apache.org/docs/latest/sql-ref-datatypes.html) that can be used when creating and registering feature tables in Databricks Feature Store and the legacy Workspace Feature Store. These data types cover the common representations needed for machine learning features, including dense and sparse vectors, embeddings, text, and structured data.

## Supported PySpark Data Types

Databricks Feature Store and the legacy Workspace Feature Store support the following PySpark data types: ^[databricks-feature-store-databricks-on-aws.md]

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
- `BinaryType` [1]
- `DecimalType` [1]
- `MapType` [1]
- `StructType` [2]

[1] `BinaryType`, `DecimalType`, and `MapType` are supported in all versions of Feature Engineering in Unity Catalog and in Workspace Feature Store v0.3.5 or above. ^[databricks-feature-store-databricks-on-aws.md]

[2] `StructType` is supported in Feature Engineering v0.6.0 or above. ^[databricks-feature-store-databricks-on-aws.md]

## Common Feature Representations

The supported data types enable common machine learning feature representations: ^[databricks-feature-store-databricks-on-aws.md]

- **Dense vectors, tensors, and embeddings** can be stored as `ArrayType`.
- **Sparse vectors, tensors, and embeddings** can be stored as `MapType`.
- **Text** can be stored as `StringType`.

## Online Store Storage Format

When features are published to online stores, `ArrayType` and `MapType` features are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## UI Display

The Feature Store UI displays metadata on feature data types, including complex data types such as `ArrayType` and `MapType`. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — Central registry for features used in AI and ML models.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The Unity Catalog-based feature store implementation.
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — The legacy feature store for workspaces not enabled for Unity Catalog.
- [PySpark Data Types](/concepts/supported-pyspark-data-types-for-features.md) — The underlying type system used by Apache Spark.
- [Online Feature Store](/concepts/online-feature-store.md) — Low-latency storage for serving features in production.
- Training/Serving Skew — A common ML deployment problem that feature stores help eliminate.

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
