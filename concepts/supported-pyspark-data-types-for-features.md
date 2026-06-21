---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56535828bb1b65f5352c090e56f5c9f5626a8a03b94aefaf7493344d826845d7
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-pyspark-data-types-for-features
    - SPDTFF
    - PySpark Data Types
    - PySpark data types
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Supported PySpark Data Types for Features
description: The list of PySpark data types (IntegerType, FloatType, BooleanType, StringType, DoubleType, LongType, TimestampType, DateType, ShortType, ArrayType, BinaryType, DecimalType, MapType, StructType) supported by Databricks Feature Store for storing feature values.
tags:
  - data-types
  - pyspark
  - feature-engineering
timestamp: "2026-06-18T15:07:06.371Z"
---

# Supported PySpark Data Types for Features

**Supported PySpark Data Types for Features** refers to the set of [PySpark data types](https://spark.apache.org/docs/latest/sql-ref-datatypes.html) that can be used to store feature values in both Databricks Feature Store (Unity Catalog) and the legacy Workspace Feature Store. These types cover the range of common machine learning data formats, including numeric, categorical, text, and complex structured data. ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types

The following PySpark data types are supported across both Feature Store versions: ^[databricks-feature-store-databricks-on-aws.md]

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
- `BinaryType`
- `DecimalType`
- `MapType`
- `StructType`

### Version-Specific Support

Most types are supported in all versions of Feature Engineering in Unity Catalog and Workspace Feature Store. However, some types have version requirements: ^[databricks-feature-store-databricks-on-aws.md]

| Data Type | Minimum Version Requirement |
|-----------|-----------------------------|
| `BinaryType` | Feature Engineering in Unity Catalog (all versions) and Workspace Feature Store v0.3.5 or above |
| `DecimalType` | Feature Engineering in Unity Catalog (all versions) and Workspace Feature Store v0.3.5 or above |
| `MapType` | Feature Engineering in Unity Catalog (all versions) and Workspace Feature Store v0.3.5 or above |
| `StructType` | Feature Engineering in Unity Catalog v0.6.0 or above |

## Common Use Cases

The supported data types map to common machine learning feature types: ^[databricks-feature-store-databricks-on-aws.md]

- **Dense vectors, tensors, and embeddings** — store as `ArrayType`
- **Sparse vectors, tensors, and embeddings** — store as `MapType`
- **Text data** — store as `StringType`

When features are published to online stores, `ArrayType` and `MapType` features are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## UI Display

The Feature Store UI displays metadata about feature data types, including complex types such as arrays and maps. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — Central registry for ML features with governance and lineage
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The current generation of feature management
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — The legacy feature store for non-Unity Catalog workspaces

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
