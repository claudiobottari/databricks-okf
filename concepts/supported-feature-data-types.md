---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 624c2c0d4dc28d7ffafa510d5dc0baadecf28f47e03e325923f87d90d3888a72
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-feature-data-types
    - SFDT
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Supported Feature Data Types
description: The set of PySpark data types supported by Databricks Feature Store for storing features such as vectors, tensors, embeddings, and text.
tags:
  - data-types
  - feature-store
  - reference
timestamp: "2026-06-19T18:11:51.509Z"
---

# Supported Feature Data Types

**Supported Feature Data Types** refers to the set of [PySpark data types](/concepts/supported-pyspark-data-types-for-features.md) that can be used to store features in the [Databricks Feature Store](/concepts/databricks-feature-store.md) (both the Unity Catalog Feature Engineering version and the legacy Workspace Feature Store). These types cover common machine learning representations such as dense and sparse vectors, tensors, embeddings, and text. ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types

Feature Store and Workspace Feature Store support the following PySpark data types: ^[databricks-feature-store-databricks-on-aws.md]

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
- `BinaryType` ^[databricks-feature-store-databricks-on-aws.md]
- `DecimalType` ^[databricks-feature-store-databricks-on-aws.md]
- `MapType` ^[databricks-feature-store-databricks-on-aws.md]
- `StructType` ^[databricks-feature-store-databricks-on-aws.md]

### Version Availability

`BinaryType`, `DecimalType`, and `MapType` are supported in all versions of Feature Engineering in Unity Catalog and in Workspace Feature Store v0.3.5 or above. ^[databricks-feature-store-databricks-on-aws.md]

`StructType` is supported in Feature Engineering in Unity Catalog v0.6.0 or above. ^[databricks-feature-store-databricks-on-aws.md]

All other listed types are supported across all versions. ^[databricks-feature-store-databricks-on-aws.md]

## Typical Use Cases

The supported data types map to common feature representations: ^[databricks-feature-store-databricks-on-aws.md]

| Feature type | PySpark data type | Example |
|---|---|---|
| Dense vectors, tensors, embeddings | `ArrayType` | `[0.12, 0.87, 0.45]` |
| Sparse vectors, tensors, embeddings | `MapType` | `{"0":0.3, "5":0.8}` |
| Text | `StringType` | `"customer review"` |

## Storage in Online Stores

When features are published to online stores, `ArrayType` and `MapType` features are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## UI Display

The Feature Store UI displays metadata on feature data types, including complex types: ^[databricks-feature-store-databricks-on-aws.md]

![Complex data types example](https://docs.databricks.com/aws/en/assets/images/complex-data-type-example-18d4e615f2c7e61dffcce1f6358f23c0.png)

## Requirements

To use Databricks Feature Store, your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md). If it is not, refer to the legacy [Workspace Feature Store (Deprecated)](/concepts/workspace-feature-store-deprecated.md). ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md)
- Feature Store UI
- Online stores
- [PySpark data types](/concepts/supported-pyspark-data-types-for-features.md)
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
