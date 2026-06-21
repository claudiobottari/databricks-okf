---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7bcc60d8fa2c9446baa6bb77b9e266ab1a21480a3ddb7e946ded55a56d850245
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-store-workflow
    - DFSW
    - Databricks Feature Store publish workflow
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
title: Databricks Feature Store Workflow
description: The end-to-end pipeline from raw data transformation through feature table creation, model training with feature logging, model registration, to batch and real-time inference.
tags:
  - feature-store
  - workflow
  - mlops
  - pipeline
timestamp: "2026-06-18T11:37:50.393Z"
---

# Databricks Feature Store Workflow

The **Databricks Feature Store Workflow** describes the end-to-end process of using [Databricks Feature Store](/concepts/databricks-feature-store.md) to centralize feature engineering for machine learning. The workflow ensures that the same feature computations are used during model training and inference, eliminating training-serving skew and enabling feature reuse across teams. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Overview

The typical machine learning workflow using feature engineering on Databricks follows a sequence of steps: raw data transformation, feature table creation, model training with feature logging, model registration, and—for real-time serving—publication of features to an online store and automated feature lookup at inference time. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

The workflow applies both to workspaces enabled for Unity Catalog (where any Delta table with a primary key can serve as a feature table) and to legacy Workspace Feature Store workspaces. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Step 1: Transform Raw Data into Features

Write code to convert raw data into features and create a [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) containing the desired feature columns. Feature engineering transforms raw data into the building blocks used by machine learning models. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Step 2: Create a Feature Table

Create a [Feature Table](/concepts/feature-table.md) — a [Delta table](/concepts/delta-lake-table.md) in [Unity Catalog](/concepts/unity-catalog.md) that includes a primary key constraint. Feature table metadata tracks the data sources from which the table was generated and the notebooks or jobs that created or wrote to the table. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

For time-sensitive data, you can define [Time Series Feature Tables](/concepts/time-series-feature-tables.md) by specifying time-related columns in the primary keys using the `timeseries_columns` argument (Unity Catalog) or `timestamp_keys` argument (Workspace Feature Store). This enables point-in-time lookups when training or scoring. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Step 3: Train and Log a Model Using Feature Tables

To train a model, create one or more [FeatureLookup](/concepts/featurelookup.md) objects. Each `FeatureLookup` specifies which features (columns) to use from a feature table and which keys to use to join the table to the label data. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

You then call `create_training_set`, providing a DataFrame with raw training data, labels, and primary keys. The system joins features from the feature tables according to the lookup keys, producing a [Training Set](/concepts/training-set-feature-store.md). ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

When you train the model and log it using `FeatureEngineeringClient.log_model()` (Unity Catalog) or `FeatureStoreClient.log_model()` (Workspace Feature Store), the model stores the specifications of the features used for training. This metadata enables automatic feature retrieval at inference time. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

If a feature depends on data only available at inference time, you can use a [FeatureFunction](/concepts/featurefunction.md) that combines real-time inputs with stored feature values to compute up-to-date values. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Step 4: Register the Model

Register the trained model in the [Model Registry](/concepts/mlflow-model-registry.md). At this point, the model carries lineage to the feature tables and functions used during training. In Unity Catalog, tables and functions that were used to create the model are automatically tracked and visible in Catalog Explorer. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Step 5: Batch Inference — Automatic Feature Retrieval

For batch use cases, the model automatically retrieves the features it needs from the offline feature store (the underlying Delta tables) when scoring new data. The caller only needs to provide the primary key values (e.g., `user_id`), and the model fetches all required feature values from the offline store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Step 6: Real-Time Serving — Publish to Online Store

For real-time serving, publish the feature table to an [Online Feature Store](/concepts/online-feature-store.md). Databricks provides a serverless online store powered by Databricks Lakebase for low-latency access. You can also use Third-Party Online Stores. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Step 7: Inference — Online Feature Lookup

At inference time, the model serving endpoint automatically uses the entity IDs in the request data to look up pre-computed features from the online store. The endpoint uses Unity Catalog to resolve lineage from the served model to the features used to train the model, and tracks lineage to the online feature store for real-time access. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

The following diagram illustrates the flow:

![Feature Store flow for machine learning models that are served.](https://docs.databricks.com/aws/en/assets/images/feature-store-flow-with-online-store-031283c533262f17af5ccaa15b57d6ea.png)

^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Alternative: FeatureSpec for Serving

For scenarios where you want to define a reusable set of features and functions for serving without training a model, you can use a [FeatureSpec](/concepts/featurespec.md). FeatureSpecs are Unity Catalog entities that combine `FeatureLookup`s and `FeatureFunction`s into a single logical unit. You can create a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) directly from a `FeatureSpec` using the Python API or REST API. For high-performance applications, enable route optimization. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Related Concepts

- Feature Store Glossary — Definitions of feature table, training set, FeatureLookup, FeatureFunction, online store, offline store, streaming, and model packaging.
- [Delta Table](/concepts/delta-lake-table.md) — The underlying storage format for feature tables.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for feature tables and model lineage.
- [Model Registry](/concepts/mlflow-model-registry.md) — For managing model lifecycle.
- [Online Feature Store](/concepts/online-feature-store.md) — For real-time serving.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — How to work with feature tables in Unity Catalog.

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
