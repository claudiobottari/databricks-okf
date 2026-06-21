---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4574a490dfa763ea0e9861cd41ffa872b6c21790df780ddc95899c44d52fef99
  pageDirectory: concepts
  sources:
    - machine-learning-lifecycle-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store
    - Feature Store UI
    - Feature Store URI
    - feature store APIs
    - feature stores
    - Feature Store Overview
    - Feature Store client
    - Feature Store data types
    - FeatureStoreClient
    - Features UI
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - file: machine-learning-lifecycle-databricks-on-aws.md
title: Feature Store
description: A governed system for defining, managing, and reusing ML features as assets, with the same feature definitions used for both training and serving, supporting batch and real-time ingestion.
tags:
  - machine-learning
  - feature-engineering
  - unity-catalog
timestamp: "2026-06-19T19:20:33.285Z"
---

# Feature Store

A **Feature Store** is a centralized repository for machine learning features that ensures consistent feature computation across model training and inference, addressing duplication and code-mismatch problems. It enables data scientists to find and share features while guaranteeing that the code used to compute feature values is identical during model training and when the model is used for inference, preventing training–serving skew. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Overview

Feature stores solve two common problems in machine learning: feature duplication across teams and code mismatch between training and serving pipelines. By providing a single source of truth for feature definitions, a feature store ensures that the same transformations applied during training are applied during inference, eliminating a major source of model degradation in production. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

On Databricks, the Feature Store integrates with [Unity Catalog](/concepts/unity-catalog.md) and [MLflow](/concepts/mlflow.md) to provide governance, lineage, and reproducibility. Features are organized as tables with primary keys, backed by [Delta Table](/concepts/delta-lake-table.md)s, and can be used for both batch and real-time serving. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## How Databricks Feature Store Works

The typical machine learning workflow using feature engineering on Databricks follows these steps:

1. Write code to convert raw data into features and create a Spark DataFrame containing the desired features.
2. Create a Delta table in Unity Catalog that has a primary key.
3. Train and log a model using the feature table. When you do this, the model stores the specifications of features used for training. When the model is used for inference, it automatically joins features from the appropriate feature tables.
4. Register the model in [Model Registry](/concepts/mlflow-model-registry.md).
5. For batch use cases, the model automatically retrieves the features it needs from Feature Store.
6. For real-time serving, publish the features to an [Online Feature Store](/concepts/online-feature-store.md).
7. At inference time, the model serving endpoint automatically uses the entity IDs in the request data to look up pre-computed features from the online store to score the ML model. The endpoint uses Unity Catalog to resolve lineage from the served model to the features used to train the model and tracks lineage to the online feature store for real-time access. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Key Concepts

### Feature Tables

Features are organized as feature tables. Each table must have a primary key and is backed by a [Delta Table](/concepts/delta-lake-table.md) and additional metadata. Feature table metadata tracks the data sources from which the table was generated and the notebooks and jobs that created or wrote to the table. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

With Databricks Runtime 13.3 LTS and above, if your workspace is enabled for Unity Catalog, you can use any Delta table with a primary key as a feature table. Features in a feature table are typically computed and updated using a common computation function. You can publish a feature table to an online store for real-time model inference. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### FeatureLookup

A `FeatureLookup` specifies which features to use from a feature table and defines the keys to join the feature table to the label data passed to `create_training_set`. Many different models might use features from the same table, and not all models will need every feature. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

When creating a training dataset, you create a `FeatureLookup` for each feature table, specifying the table name, the features (columns) to select, and the lookup key to use when joining features. The training data must contain columns corresponding to each primary key of the feature tables. The data in the feature tables is joined to the input DataFrame according to these keys. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### FeatureFunction

A feature might depend on information available only at inference time. You can specify a `FeatureFunction` that combines real-time inputs with feature values to compute up-to-date feature values. This enables on-demand feature computation. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Training Set

A training set consists of a list of features and a DataFrame containing raw training data, labels, and primary keys by which to look up features. You create the training set by specifying features to extract from Feature Store and provide the training set as input during model training. When you train and log a model using Feature Engineering in Unity Catalog, you can view the model's lineage in Catalog Explorer. Tables and functions used to create the model are automatically tracked and displayed. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### FeatureSpec

A `FeatureSpec` is a Unity Catalog entity that defines a reusable set of features and functions for serving. `FeatureSpec`s combine `FeatureLookup`s from feature tables and `FeatureFunction`s into a single logical unit that can be used in model training or served using Feature Serving endpoints. `FeatureSpec`s are stored and managed by Unity Catalog, with full lineage tracking to their constituent offline feature tables and functions. This enables governance, discoverability, and reuse across different models and applications. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

You can use a `FeatureSpec` to create a Feature Serving endpoint using the Python API or REST API, or deploy directly using the Model Serving UI. For high-performance applications, enable route optimization. You can also use it in model training by referencing the `FeatureSpec` in `create_training_set`. A `FeatureSpec` always references the offline feature tables, but they must be published to an online store for real-time serving scenarios. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Time Series Feature Tables (Point-in-Time Lookups)

Data used to train a model often has time dependencies. When building the model, you must consider only feature values up until the time of the observed target value. If you train on features based on data measured after the timestamp of the target value, the model's performance may suffer. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

Time series feature tables include a timestamp column that ensures each row in the training dataset represents the latest known feature values as of the row's timestamp. Use them whenever feature values change over time, for example with time series data, event-based data, or time-aggregated data. When you create a time series feature table, you specify time-related columns in your primary keys using the `timeseries_columns` argument (for Feature Engineering in Unity Catalog) or the `timestamp_keys` argument (for Workspace Feature Store). This enables point-in-time lookups when using `create_training_set` or `score_batch`. The system performs an as-of timestamp join using the `timestamp_lookup_key` you specify. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

If you do not use the `timeseries_columns` or `timestamp_keys` argument and only designate a time series column as a primary key, Feature Store does not apply point-in-time logic during joins. Instead, it matches only rows with an exact time match instead of matching all rows prior to the timestamp. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Offline Store

The offline feature store is used for feature discovery, model training, and batch inference. It contains feature tables materialized as [Delta Table](/concepts/delta-lake-table.md)s. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Online Feature Store

The Databricks Online Feature Store is a high-performance, scalable solution for serving feature data to online applications and real-time machine learning models. It is powered by Databricks Lakebase and provides low-latency access to feature data at high scale while maintaining governance, lineage, and consistency with your offline feature tables. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

You can provision Online Stores in the serverless Lakebase platform. APIs allow you to manage instances and read-replicas and scale instances as needed. You can use convenient APIs to publish Unity Catalog tables into online stores. These tables are also Unity Catalog entities that natively track lineage to the source tables. Databricks also supports third-party online stores. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Streaming

In addition to batch writes, Databricks Feature Store supports streaming. You can write feature values to a feature table from a streaming source, and feature computation code can utilize [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to transform raw data streams into features. You can also stream feature tables from the offline store to an online store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Model Packaging

When you train a machine learning model using Feature Engineering in Unity Catalog or Workspace Feature Store and log it using the client's `log_model()` method, the model retains references to these features. At inference time, the model can optionally retrieve feature values automatically. The caller only needs to provide the primary key of the features used in the model (for example, `user_id`), and the model retrieves all required feature values. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

In batch inference, feature values are retrieved from the offline store and joined with new data prior to scoring. In real-time inference, feature values are retrieved from the online store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

To package a model with feature metadata, use `FeatureEngineeringClient.log_model` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient.log_model` (for Workspace Feature Store). ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Integration with the ML Lifecycle

The Feature Store plays a central role in the Machine Learning Lifecycle. During the data preparation and feature engineering phase, data scientists can discover existing features in Unity Catalog and reuse them across models, avoiding redundant work. The same feature definitions used during training are automatically applied during serving, eliminating training–serving skew. ^[machine-learning-lifecycle-databricks-on-aws.md]

When training models, features from the Feature Store are combined with label data to create training sets. The model artifact stores references to the features it uses, enabling automatic feature retrieval at inference time without manual coding of feature transformations. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Table](/concepts/delta-lake-table.md)
- [Model Registry](/concepts/mlflow-model-registry.md)
- [Feature Engineering](/concepts/featureengineeringclient-api.md)
- [Online Feature Store](/concepts/online-feature-store.md)
- Feature Serving
- [Point-in-Time Lookup](/concepts/point-in-time-lookups.md)
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- [MLflow](/concepts/mlflow.md)
- Machine Learning Lifecycle
- Training-Serving Skew

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md
- machine-learning-lifecycle-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
2. [machine-learning-lifecycle-databricks-on-aws.md](/references/machine-learning-lifecycle-databricks-on-aws-d195211f.md)
