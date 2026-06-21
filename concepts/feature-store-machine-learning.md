---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66bcdf2d3cdb05a6d7afdd7d338dfcc0192bebe2423a72086723dff25cd8c4be
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-machine-learning
    - FS(L
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
title: Feature Store (Machine Learning)
description: A centralized repository that enables data scientists to find, share, and reuse features, ensuring the same feature computations are used during model training and inference.
tags:
  - machine-learning
  - feature-engineering
  - mlops
timestamp: "2026-06-19T09:52:22.953Z"
---

# Feature Store (Machine Learning)

A **feature store** is a centralized repository that enables data scientists to find and share features used in machine learning. Using a feature store ensures that the code used to compute feature values is the same during model training and when the model is used for inference, solving the problem of inconsistent feature engineering between development and production environments.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Overview

Machine learning uses existing data to build models that predict future outcomes. Raw data typically requires preprocessing and transformation before it can be used for model building — a process called feature engineering. The outputs of this process are called **features**, which are the building blocks of machine learning models.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

Developing features is complex and time-consuming. An additional complication is that feature calculations must be performed both during model training and when the model is used to make predictions. These implementations might not be done by the same team or using the same code environment, leading to delays and errors. Different teams within an organization often have similar feature needs but may not be aware of work other teams have done. A feature store addresses these problems by centralizing feature management.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Architecture

### Offline Store

The offline feature store is used for feature discovery, model training, and batch inference. It contains feature tables materialized as [Delta tables](/concepts/delta-lake-table.md). This store maintains the full historical record of feature values for training and batch scoring workflows.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Online Store

The online feature store is a high-performance, scalable solution for serving feature data to online applications and real-time machine learning models. It provides low-latency access to feature data at high scale while maintaining governance, lineage, and consistency with offline feature tables. For real-time serving, features are published from the offline store to the online store.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

At inference time, the [Model Serving](/concepts/model-serving.md) endpoint automatically uses entity IDs from the request data to look up pre-computed features from the online store to score the ML model. The system uses [Unity Catalog](/concepts/unity-catalog.md) to resolve lineage from the served model to the features used for training and tracks lineage to the online feature store for real-time access.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Key Concepts

### Feature Tables

Features are organized as **feature tables**. Each table must have a primary key and is backed by a Delta table with additional metadata. Feature table metadata tracks the data sources from which a table was generated and the notebooks and jobs that created or wrote to the table. In workspaces enabled for Unity Catalog, any Delta table with a primary key can serve as a feature table. Features in a feature table are typically computed and updated using a common computation function.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### FeatureLookup

A `FeatureLookup` specifies which features to use from a feature table and defines the key columns used to join the feature table to label data when creating a training set. Multiple models can use features from a single feature table, but not all models need every feature — the `FeatureLookup` selects only the relevant columns. When a training dataset is created, feature data is joined to the input DataFrame according to the specified lookup keys.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### FeatureFunction

A `FeatureFunction` combines real-time inputs with feature values to compute up-to-date feature values. This is useful when a feature depends on information only available at the time of inference. The function applies on-demand computation blending live input data with pre-computed features.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### FeatureSpec

A `FeatureSpec` is a Unity Catalog entity that defines a reusable set of features and functions for serving. It combines `FeatureLookup`s from feature tables and `FeatureFunction`s into a single logical unit that can be used in model training or served using Feature Serving endpoints. `FeatureSpec`s are stored and managed by Unity Catalog with full lineage tracking to their constituent offline feature tables and functions, enabling governance, discoverability, and reuse across different models and applications.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

A `FeatureSpec` always references offline feature tables, but those tables must be published to an online store for real-time serving scenarios. Feature Serving endpoints can be created using the Python API or REST API.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Training Set

A **training set** consists of a list of features and a DataFrame containing raw training data, labels, and primary keys by which to look up features. The training set is created by specifying features to extract from the feature store and is provided as input during model training.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Time Series Feature Tables

Time series feature tables include a timestamp column that ensures each row in the training dataset represents the latest known feature values as of the row's timestamp. They should be used whenever feature values change over time, such as with time series data, event-based data, or time-aggregated data. Time series columns are specified using the `timeseries_columns` argument, enabling point-in-time lookups during training set creation and batch scoring. The system performs an as-of timestamp join using the specified `timestamp_lookup_key`.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

If a time series column is designated only as a primary key column without the `timeseries_columns` argument, the feature store does not apply point-in-time logic — it matches only rows with an exact time match instead of matching all rows prior to the timestamp.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Model Packaging

When a machine learning model is trained using the feature store and logged using the client's `log_model()` method, the model retains references to the features used during training. At inference time, the model can optionally retrieve feature values automatically. The caller only needs to provide the primary key of the features (for example, `user_id`), and the model retrieves all required feature values. In batch inference, feature values are retrieved from the offline store. In real-time inference, feature values are retrieved from the online store.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### Streaming

In addition to batch writes, feature stores support streaming. Feature values can be written to a feature table from a streaming source, and feature computation code can utilize [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to transform raw data streams into features. Feature tables can also be streamed from the offline store to an online store.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Workflow

The typical machine learning workflow using feature engineering follows this path:^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

1. Write code to convert raw data into features and create a Spark DataFrame containing the desired features.
2. Create a Delta table in Unity Catalog that has a primary key.
3. Train and log a model using the feature table. The model stores the specifications of features used for training.
4. Register the model in the [Model Registry](/concepts/mlflow-model-registry.md).
5. For batch use cases, the model automatically retrieves the features it needs from the feature store.
6. For real-time serving, publish the features to an online feature store.

## Governance and Lineage

When a model is trained and logged using feature engineering in Unity Catalog, the model's lineage can be viewed in [Catalog Explorer](/concepts/catalog-explorer.md). Tables and functions used to create the model are automatically tracked and displayed. This provides governance, discoverability, and reuse across different models and applications.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Tables](/concepts/delta-lake-table.md)
- [Feature Engineering](/concepts/featureengineeringclient-api.md)
- [Model Registry](/concepts/mlflow-model-registry.md)
- [Model Serving](/concepts/model-serving.md)
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
