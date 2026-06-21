---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a93cadf976627e62358855026f6be4a80d89901be72b84a117de01e9dd3bae3
  pageDirectory: concepts
  sources:
    - share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - centralized-feature-store-architecture
    - CFSA
  citations:
    - file: share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
title: Centralized Feature Store Architecture
description: Architectural pattern designating a single Databricks workspace to store all feature store metadata, with multiple workspaces accessing it for creating, writing to, or reading from feature tables.
tags:
  - databricks
  - architecture
  - feature-store
timestamp: "2026-06-19T23:05:10.499Z"
---

# Centralized [Feature Store](/concepts/feature-store.md) Architecture

A **Centralized [Feature Store](/concepts/feature-store.md) Architecture** enables multiple Databricks workspaces to share access to [Feature Tables](/concepts/feature-tables.md) from a single, designated [Feature Store](/concepts/feature-store.md) workspace. This architecture is useful when multiple teams need to reuse the same features or when an organization maintains separate workspaces for different development stages. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Overview

In a centralized setup, one workspace acts as the central repository for all [Feature Store](/concepts/feature-store.md) metadata and [Feature Table](/concepts/feature-table.md) data. Other workspaces (local workspaces) can create, write, and read [Feature Tables](/concepts/feature-tables.md) hosted in the central workspace. Access is controlled through tokens: each user or script creates a personal access token (or, as a security best practice, an OAuth token) in the central workspace and stores that token in the secret manager of their local workspace. Every API request to the centralized [Feature Store](/concepts/feature-store.md) must include the access token. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

If teams are also sharing models across workspaces, they may dedicate the same centralized workspace for both [Feature Tables](/concepts/feature-tables.md) and models, or use separate centralized workspaces for each. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

> **Deprecation notice:** The approach described on this page is legacy. Databricks now recommends using [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) to share [Feature Tables](/concepts/feature-tables.md) across workspaces. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Requirements

Cross-workspace [Feature Store](/concepts/feature-store.md) sharing requires:

- **Feature Store client v0.3.6 or above** in the local workspace.
- **Shared external Hive metastore** – both workspaces must use the same Hive [Metastore](/concepts/metastore.md) and have access to the same DBFS storage location.
- **IP access lists** – if IP access lists are enabled, the IP addresses of both workspaces must be included in the access lists. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Setup

### 1. Create an access token in the central workspace

In the centralized [Feature Store](/concepts/feature-store.md) workspace (referred to as “Workspace B”), create an access token. For automated processes, Databricks recommends using tokens belonging to service principals rather than individual users. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### 2. Store secrets in the local workspace

In the local workspace, create a [secret scope](/concepts/databricks-secret-scopes.md) and store three secrets that identify the central workspace:

| Secret Key             | Value                                                        |
|------------------------|--------------------------------------------------------------|
| `<prefix>`-host        | Hostname of the central workspace (e.g., from `mlflow.utils.databricks_utils.get_webapp_url()`) |
| `<prefix>`-token       | The access token created in the central workspace            |
| `<prefix>`-workspace-id | Workspace ID of the central workspace (found in the workspace URL) |

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

The `<prefix>` is a unique identifier chosen for the central workspace.

## Specifying a Remote [Feature Store](/concepts/feature-store.md)

Using the secret scope and prefix, construct a [Feature Store](/concepts/feature-store.md) URI in the format:

```python
feature_store_uri = 'databricks://<scope>:<prefix>'
```

Then pass this URI when instantiating a `FeatureStoreClient`:

```python
fs = FeatureStoreClient(feature_store_uri=feature_store_uri)
```

Before creating [Feature Tables](/concepts/feature-tables.md) in the remote [Feature Store](/concepts/feature-store.md), a database must exist in the shared DBFS location. For example:

```sql
CREATE DATABASE IF NOT EXISTS recommender LOCATION '/mnt/shared'
```

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Operations on Remote [Feature Tables](/concepts/feature-tables.md)

All standard [Feature Store](/concepts/feature-store.md) APIs are supported for the remote [Feature Store](/concepts/feature-store.md):

| Operation               | Method                  |
|-------------------------|-------------------------|
| Create a [Feature Table](/concepts/feature-table.md)  | `fs.create_table()`     |
| Read a [Feature Table](/concepts/feature-table.md)    | `fs.read_table()`       |
| Write to a feature table| `fs.write_table()`      |
| Publish a [Feature Table](/concepts/feature-table.md) | `fs.publish_table()`    |
| Get table metadata      | `fs.get_table()` (v0.3.6+) |
| Create a training set   | `fs.create_training_set()` |

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

Example (create a customer features table):

```python
fs = FeatureStoreClient(feature_store_uri='databricks://<scope>:<prefix>')
fs.create_table(
    name='recommender.customer_features',
    primary_keys='customer_id',
    schema=customer_features_df.schema,
    description='Customer-keyed features'
)
```

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Using a Remote Model Registry

The `FeatureStoreClient` can also be configured to use a remote [MLflow Model Registry](/concepts/mlflow-model-registry.md) for model logging and scoring:

```python
fs = FeatureStoreClient(
    feature_store_uri='databricks://<scope>:<prefix>',
    model_registry_uri='databricks://<scope>:<prefix>'
)
```

This allows you to train a model using any local or remote [Feature Table](/concepts/feature-table.md), and then register the model in any local or remote model registry. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) – The recommended replacement for the legacy cross-workspace approach
- [Feature Store](/concepts/feature-store.md) – Core concepts for managing machine learning features
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ unified governance solution
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Model management across workspaces
- [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md) and OAuth Tokens for cross-workspace authentication
- Secrets Management – Storing tokens securely
- Service Principals – Recommended identity for automated access

## Sources

- share-feature-tables-across-workspaces-legacy-databricks-on-aws.md

# Citations

1. [share-feature-tables-across-workspaces-legacy-databricks-on-aws.md](/references/share-feature-tables-across-workspaces-legacy-databricks-on-aws-144855e9.md)
