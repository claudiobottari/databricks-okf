---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7d057aae959b8f2dacc048f9567a7f305c673dbe333725cf267e4264701c7ae
  pageDirectory: concepts
  sources:
    - model-serving-with-automatic-feature-lookup-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-data-types-for-feature-lookup
    - SDTFFL
  citations:
    - file: model-serving-with-automatic-feature-lookup-databricks-on-aws.md
title: Supported Data Types for Feature Lookup
description: Automatic feature lookup supports IntegerType, FloatType, BooleanType, StringType, DoubleType, LongType, TimestampType, DateType, ShortType, ArrayType, and MapType.
tags:
  - data-types
  - feature-store
  - model-serving
timestamp: "2026-06-19T19:44:33.621Z"
---

# Supported Data Types for Feature Lookup

**Supported Data Types for Feature Lookup** defines the set of Apache Spark data types that Databricks Model Serving can automatically retrieve from online feature stores during model scoring. When a model is logged with feature metadata, Databricks automatically looks up the required feature values from the configured online store and returns them alongside the model prediction.

## Supported Data Types

Automatic feature lookup is supported for the following data types: ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

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
- `MapType`

These data types are supported when looking up features from a [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) or from Amazon DynamoDB (v0.3.8 and above). ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Override Feature Values

When scoring a model using a REST API, you can override automatically looked-up feature values by including the new values in the API payload. The new feature values must conform to the feature's data type as expected by the underlying model. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Requirements

To use automatic feature lookup, the model must have been logged with `FeatureEngineeringClient.log_model` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient.log_model` (for legacy Workspace Feature Store), requiring version 0.3.5 and above. For third-party online stores, the online store must be published with read-only credentials. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The serving infrastructure that performs automatic feature lookup
- [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) — Recommended online store for real-time feature serving
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — Modern feature store approach using `FeatureEngineeringClient`
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — Legacy feature store approach using `FeatureStoreClient`
- [Inference Tables](/concepts/inference-tables.md) — Logging augmented DataFrames containing looked-up feature values

## Sources

- model-serving-with-automatic-feature-lookup-databricks-on-aws.md

# Citations

1. [model-serving-with-automatic-feature-lookup-databricks-on-aws.md](/references/model-serving-with-automatic-feature-lookup-databricks-on-aws-7e249d4a.md)
