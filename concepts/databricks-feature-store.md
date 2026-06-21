---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51d8f7821046b35195af21e012f87ad8c9f34e3da417579aa083ee3cf45adb23
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
    - databricks-feature-store-databricks-on-aws.md
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - use-features-in-online-workflows-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-feature-store
    - DFS
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
title: Databricks Feature Store
description: A managed feature store for batch and real-time serving of ML features with a single governed source of truth under Unity Catalog.
tags:
  - machine-learning
  - feature-engineering
  - mlops
timestamp: "2026-06-19T18:11:35.444Z"
---

```yaml
---
title: Databricks Feature Store
summary: A central registry on Databricks for managing, discovering, and serving features used in AI and ML models, integrated with Unity Catalog.
sources:
  - databricks-feature-store-databricks-on-aws.md
  - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T15:00:00.000Z"
updatedAt: "2026-06-20T15:00:00.000Z"
tags:
  - feature-store
  - machine-learning
  - databricks
aliases:
  - databricks-feature-store
  - DFS
confidence: 0.98
provenanceState: merged
inferredParagraphs: 0
---

# Databricks Feature Store

**Databricks Feature Store** is a central registry for the features used in your AI and ML models. When you register feature tables and models in [Unity Catalog](/concepts/unity-catalog.md), you get built-in governance, lineage, point-in-time joins, and cross-workspace feature sharing and discovery. ^[databricks-feature-store-databricks-on-aws.md]

The entire model training workflow takes place on a single platform, including data pipelines that ingest raw data, create feature tables, train models, and perform batch inference; model and feature serving endpoints that provide millisecond latency; and data and model monitoring. ^[databricks-feature-store-databricks-on-aws.md]

Features are managed in the Feature Store for both batch and real-time serving, providing a single, governed source of truth for features. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

When you use features from Databricks Feature Store to train models, the model automatically tracks lineage to the features used in training. At inference time, the model automatically looks up the latest feature values from the appropriate store (offline or online). Databricks Feature Store also provides on-demand computation of features for real-time applications, handling all feature computation tasks. This eliminates training/serving skew, ensuring that the feature computations used at inference are the same as those used during training. It also simplifies client-side code because all feature lookups and computation are handled by Feature Store. ^[databricks-feature-store-databricks-on-aws.md]

## How It Works

The typical machine learning workflow using feature engineering on Databricks follows this path: ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

1. Write code to convert raw data into features and create a Spark DataFrame containing the desired features.
2. Create a Delta table in Unity Catalog that has a primary key.
3. Train and log a model using the feature table. The model stores the specifications of the features used for training.
4. Register the model in the [Model Registry](/concepts/mlflow-model-registry.md).
5. For real-time serving use cases, publish the features to an [Online Feature Store](/concepts/online-feature-store.md).
6. At inference time, the model serving endpoint automatically uses the entity IDs in the request data to look up pre-computed features from the online store and score the model. The endpoint uses Unity Catalog to resolve lineage from the served model to the features used to train this model, and tracks lineage to the online feature store for real-time access.

## Key Concepts

### Feature Tables

Features are organized as **feature tables**. Each table must have a primary key and is backed by a [Delta table](/concepts/delta-lake-table.md) and additional metadata. Feature table metadata tracks the data sources from which a table was generated and the notebooks and jobs that created or wrote to the table. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

With Databricks Runtime 13.3 LTS and above, if your workspace is enabled for Unity Catalog, you can use any Delta table in Unity Catalog with a primary key as a feature table. Feature tables stored in the legacy Workspace Feature Store are called "Workspace feature tables." ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### FeatureLookup

A `FeatureLookup` specifies which features to use from a feature table and defines the keys used to join the feature table to the label data passed to `create_training_set`. You create one `FeatureLookup` per feature table you want to include in training. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### FeatureFunction

A `FeatureFunction` combines real-time inputs with feature values to compute up-to-date feature values when a feature depends on information only available at inference time. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Training Set

A **training set** consists of a list of features and a DataFrame containing raw training data, labels, and primary keys by which to look up features. You create the training set by specifying features to extract from Feature Store and provide it as input during model training. When you train and log a model using Feature Engineering in Unity Catalog, you can view the model's lineage in Catalog Explorer. Tables and functions used to create the model are automatically tracked and displayed. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### FeatureSpec

A `FeatureSpec` is a Unity Catalog entity that defines a reusable set of features and functions for serving. It combines `FeatureLookup`s from feature tables and `FeatureFunction`s into a single logical unit that can be used in model training or served using Feature Serving endpoints. `FeatureSpec`s are stored and managed by Unity Catalog, with full lineage tracking to their constituent offline feature tables and functions. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Time Series Feature Tables (Point-in-Time Lookups)

Time series feature tables include a timestamp column that ensures each row in the training dataset represents the latest known feature values as of that row's timestamp. You should use them whenever feature values change over time. The system performs an as-of timestamp join using the `timestamp_lookup_key` you specify. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Offline Store

The offline feature store is used for feature discovery, model training, and batch inference. It contains feature tables materialized as Delta tables. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Online Feature Store

The Databricks Online Feature Store is a high-performance, scalable solution for serving feature data to online applications and real-time ML models. Powered by Databricks Lakebase, it provides low-latency access to feature data while maintaining governance, lineage, and consistency with offline feature tables. You can provision online stores in the serverless Lakebase platform, and publish Unity Catalog tables into them using APIs. Databricks also supports [third-party online stores](/concepts/third-party-online-stores-for-feature-serving.md). ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Streaming

Databricks Feature Store supports streaming writes to feature tables from streaming sources. Feature computation code can utilize [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to transform raw data streams into features. You can also stream feature tables from the offline store to an online store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Model Packaging

When you train an ML model using Feature Engineering in Unity Catalog or Workspace Feature Store and log it using the client's `log_model()` method, the model retains references to the features it uses. At inference time, the model can optionally retrieve feature values automatically. In batch inference, values are retrieved from the offline store; in real-time inference, from the online store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Requirements

To use Databricks Feature Store, your workspace must be enabled for Unity Catalog. If your workspace is not enabled for Unity Catalog, see [Workspace Feature Store (Deprecated)](/concepts/workspace-feature-store-deprecated.md). ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types

Databricks Feature Store supports the following [PySpark data types](/concepts/supported-pyspark-data-types-for-features.md): `IntegerType`, `FloatType`, `BooleanType`, `StringType`, `DoubleType`, `LongType`, `TimestampType`, `DateType`, `ShortType`, `ArrayType`, `BinaryType` (from Feature Engineering v0.3.5+), `DecimalType` (v0.3.5+), `MapType` (v0.3.5+), and `StructType` (from Feature Engineering v0.6.0+). ^[databricks-feature-store-databricks-on-aws.md]

These data types support common ML feature types, such as dense vectors/tensors/embeddings as `ArrayType`, sparse vectors/tensors/embeddings as `MapType`, and text as `StringType`. When published to online stores, `ArrayType` and `MapType` features are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for features, models, and data
- [Delta table](/concepts/delta-lake-table.md) – Storage format for feature tables
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – Process of creating features
- [Model Registry](/concepts/mlflow-model-registry.md) – Manage model lifecycle
- [Online Feature Store](/concepts/online-feature-store.md) – Low-latency serving for real-time inference
- [Batch inference](/concepts/batch-inference-pipelines.md) – Scoring large datasets offline
- Real-time serving – Low-latency API endpoints
- [Feature Serving endpoints](/concepts/feature-serving-endpoint.md) – Serve features directly via REST API
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – Stream processing for feature computation
- [Workspace Feature Store (Deprecated)](/concepts/workspace-feature-store-deprecated.md) – Legacy feature store for non-Unity Catalog workspaces
- [Third-party online stores](/concepts/third-party-online-stores-for-feature-serving.md) – Alternative online stores for real-time serving

## Sources

- databricks-feature-store-databricks-on-aws.md
- databricks-feature-store-overview-and-glossary-databricks-on-aws.md
- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
2. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
3. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
