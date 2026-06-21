---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8e3e6bfb7c51fb1b624e41e69871a94acae02eb749f3e8019bb6bc6188c31c7
  pageDirectory: concepts
  sources:
    - share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-client-api-for-remote-operations
    - FSCAFRO
  citations:
    - file: share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
title: Feature Store Client API for Remote Operations
description: The set of FeatureStoreClient methods (create_table, read_table, write_table, publish_table, create_training_set, get_table) that operate on remote feature stores when configured with a feature_store_uri.
tags:
  - databricks
  - api
  - feature-store
timestamp: "2026-06-19T23:05:33.414Z"
---

# [Feature Store](/concepts/feature-store.md) Client API for Remote Operations

The **Feature Store Client API for Remote Operations** allows you to use the `FeatureStoreClient` to create, read, write, and manage [Feature Tables](/concepts/feature-table.md) across multiple Databricks workspaces. This is useful when teams share access to a centralized [Feature Store](/concepts/feature-store.md) or when your organization uses separate workspaces for different development stages. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

> **Deprecation note:** This documentation describes the legacy cross-workspace approach. Databricks now recommends using **[Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)** to share [Feature Tables](/concepts/feature-table.md) across workspaces. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Overview

In a multi-workspace setup, a single workspace (e.g., Workspace B) is designated as the centralized [Feature Store](/concepts/feature-store.md). All [Feature Store](/concepts/feature-store.md) metadata is stored there, and users from other workspaces access [Feature Tables](/concepts/feature-table.md) remotely. Access is controlled by [personal access tokens](/concepts/databricks-personal-access-token-pat-authentication.md) (PATs) created in the centralized workspace. Each user or script stores the token as a secret in the local workspace’s secret manager and passes it to the remote [Feature Store](/concepts/feature-store.md) client. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

As a security best practice, Databricks recommends using **OAuth tokens for M2M** or, if using PATs, tokens belonging to **service principals** instead of individual users. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Requirements

To use the remote [Feature Store](/concepts/feature-store.md) API you need:

- [Feature Store](/concepts/feature-store.md) client **v0.3.6** or later.
- Both workspaces must have access to the raw feature data via a shared **external Hive metastore** and **DBFS** storage.
- If **IP access lists** are enabled, the workspace IP addresses must be included in the lists. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Set Up the API Token for a Remote Registry

To connect a local workspace (Workspace A) to a remote [Feature Store](/concepts/feature-store.md) workspace (Workspace B):

1. **In Workspace B**, create a personal access token.
2. **In Workspace A**, create a secret scope and store three secrets under a chosen `<prefix>`:
   - `<prefix>-host`: the hostname of Workspace B.
   - `<prefix>-token`: the PAT from Workspace B.
   - `<prefix>-workspace-id`: the workspace ID of Workspace B (visible in the workspace URL).

These secrets are then used to construct a **remote registry URI**. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Specifying a Remote [Feature Store](/concepts/feature-store.md)

Build a `FeatureStoreClient` pointing to the remote workspace by passing a `feature_store_uri` of the form:

```python
feature_store_uri = f'databricks://<scope>:<prefix>'
fs = FeatureStoreClient(feature_store_uri=feature_store_uri)
```

Before creating [Feature Tables](/concepts/feature-table.md), you must create a database in the shared DBFS location. For example:

```sql
CREATE DATABASE IF NOT EXISTS recommender LOCATION '/mnt/shared'
```

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Creating and Reading [Feature Tables](/concepts/feature-table.md) Remotely

Once the client is configured with the remote URI, you can use standard `FeatureStoreClient` methods:

```python
# Create a [[feature-table|Feature Table]]
fs.create_table(
    name='recommender.customer_features',
    primary_keys='customer_id',
    schema=customer_features_df.schema,
    description='Customer-keyed features'
)

# Read a [[feature-table|Feature Table]]
customer_features_df = fs.read_table(name='recommender.customer_features')
```

Other supported methods include `get_table()`, `write_table()`, `publish_table()`, and `create_training_set()`. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Using a Remote Model Registry

You can also specify a **remote model registry** URI (for [MLflow](/concepts/mlflow.md) model logging and scoring) when instantiating the client:

```python
fs = FeatureStoreClient(
    feature_store_uri=f'databricks://<scope>:<prefix>',
    model_registry_uri=f'databricks://<scope>:<prefix>'
)
```

This allows you to train a model using features from any local or remote [Feature Table](/concepts/feature-table.md) and register the model in any local or remote [model registry](/concepts/mlflow-model-registry.md). ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – Centralized repository for machine learning features.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) – Recommended modern approach for sharing [Feature Tables](/concepts/feature-table.md).
- [MLflow](/concepts/mlflow.md) – Open-source platform for the [ML Lifecycle](/concepts/ml-lifecycle.md).
- [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md) – Authentication mechanism for Databricks APIs.
- Secret Manager – Stores sensitive credentials like PATs.
- [External Hive Metastore](/concepts/object-ownership-in-hive-metastore.md) – Shared [Metastore](/concepts/metastore.md) required for cross-workspace access.
- DBFS – Shared file system for datasets and [Feature Tables](/concepts/feature-table.md).
- [Model Registry](/concepts/mlflow-model-registry.md) – Centralized model store used with [MLflow](/concepts/mlflow.md).

## Sources

- share-feature-tables-across-workspaces-legacy-databricks-on-aws.md

# Citations

1. [share-feature-tables-across-workspaces-legacy-databricks-on-aws.md](/references/share-feature-tables-across-workspaces-legacy-databricks-on-aws-144855e9.md)
