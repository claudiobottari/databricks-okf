---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7a5b715392f9feb132968dc5a353eabda7afdf2cc2f6ff41b3550673d35499c
  pageDirectory: concepts
  sources:
    - share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-workspace-feature-store-access-with-tokens
    - CFSAWT
  citations:
    - file: share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
title: Cross-workspace Feature Store Access with Tokens
description: Mechanism for accessing a centralized feature store from a local workspace using personal access tokens stored in the local workspace's secret manager, with each API request including the token.
tags:
  - databricks
  - authentication
  - security
timestamp: "2026-06-19T23:05:16.943Z"
---

#Cross-workspace [Feature Store](/concepts/feature-store.md) Access with Tokens

**Cross-workspace [Feature Store](/concepts/feature-store.md) Access with Tokens** refers to the legacy approach for sharing [Feature Tables](/concepts/feature-table.md) across multiple Databricks workspaces by using personal access tokens (or OAuth tokens) to authenticate requests to a centralized [Feature Store](/concepts/feature-store.md) workspace. This mechanism allows teams to create, write to, or read from [Feature Tables](/concepts/feature-table.md) stored in a remote workspace, enabling a [Centralized Feature Store Architecture](/concepts/centralized-feature-store-architecture.md). ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

> **Deprecation notice:** This documentation describes a deprecated method. Databricks recommends using [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) to share [Feature Tables](/concepts/feature-table.md) across workspaces instead. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Overview

In a multi-workspace setup, a single centralized workspace is designated to store all [Feature Store](/concepts/feature-store.md) metadata and [Feature Tables](/concepts/feature-table.md). Users in other (local) workspaces access those [Feature Tables](/concepts/feature-table.md) remotely. Access to the centralized [Feature Store](/concepts/feature-store.md) is controlled by tokens. Each user or script that needs access creates a personal access token in the centralized workspace and copies that token into the '''secret manager''' of their local workspace. Every API request sent to the centralized workspace must include the access token. The [Feature Store](/concepts/feature-store.md) client provides a simple mechanism to specify the secrets to be used when performing cross-workspace operations. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

If your teams are also sharing models across workspaces, you may choose to dedicate the same centralized workspace for both [Feature Tables](/concepts/feature-table.md) and models, or use different workspaces for each. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Authentication best practices

As a security best practice, Databricks recommends using OAuth tokens for authentication with automated tools, systems, scripts, and apps. If you use personal access tokens, Databricks recommends using tokens belonging to service principals instead of workspace users. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Requirements

Using a [Feature Store](/concepts/feature-store.md) across workspaces requires the following:

- **Feature Store client** v0.3.6 or above. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]
- **Shared data infrastructure:** Both workspaces must have access to the raw feature data. They must share the same External Hive Metastore|external Hive metastore and have access to the same DBFS storage. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]
- **Network access:** If IP access lists are enabled, workspace IP addresses must be on the access lists. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Setup: API token for a remote registry

In this section, "Workspace B" refers to the centralized (remote) [Feature Store](/concepts/feature-store.md) workspace.

1. **Create an access token** in Workspace B via the Token Management API. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]
2. **Store the token and workspace information in secrets** in the local workspace:
   - Create a secret scope: `databricks secrets create-scope --scope <scope>`.
   - Choose a unique prefix for Workspace B (shown as `<prefix>`).
   - Create three secrets with the following key names:
     - **`<prefix>-host`** – the hostname of Workspace B. You can retrieve it with the Python code:
       ```python
       import [[mlflow|MLflow]]
       host_url = [[mlflow|MLflow]].utils.databricks_utils.get_webapp_url()
       host_url
       ```
     - **`<prefix>-token`** – the access token from Workspace B.
     - **`<prefix>-workspace-id`** – the workspace ID of Workspace B (found in the URL of any page in that workspace). ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Specify a remote [Feature Store](/concepts/feature-store.md)

After storing the secrets, construct a [Feature Store](/concepts/feature-store.md) URI of the form:

```python
feature_store_uri = f'databricks://<scope>:<prefix>'
```

Then specify this URI when instantiating a `FeatureStoreClient`:

```python
from databricks.feature_store import FeatureStoreClient

fs = FeatureStoreClient(feature_store_uri=feature_store_uri)
```

All subsequent operations on this client (e.g., `create_table`, `read_table`, `write_table`) will be directed to the remote [Feature Store](/concepts/feature-store.md) workspace. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

Before you create [Feature Tables](/concepts/feature-table.md) in the remote [Feature Store](/concepts/feature-store.md), you must create a database to store them. The database must exist in the shared DBFS location. For example, to create a database `recommender` in the shared location `/mnt/shared`, run:

```sql
CREATE DATABASE IF NOT EXISTS recommender LOCATION '/mnt/shared'
```

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Create and use [Feature Tables](/concepts/feature-table.md) in the remote [Feature Store](/concepts/feature-store.md)

### Creating a [Feature Table](/concepts/feature-table.md)

```python
fs = FeatureStoreClient(feature_store_uri=f'databricks://<scope>:<prefix>')
fs.create_table(
    name='recommender.customer_features',
    primary_keys='customer_id',
    schema=customer_features_df.schema,
    description='Customer-keyed features'
)
```

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Reading a [Feature Table](/concepts/feature-table.md)

```python
customer_features_df = fs.read_table(
    name='recommender.customer_features',
)
```

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Other supported operations

The following helper methods are also supported on a `FeatureStoreClient` configured with a remote `feature_store_uri`:

- `fs.read_table()`
- `fs.get_table()` (v0.3.6 and above; equivalent to `fs.get_feature_table()` in v0.3.5 and below)
- `fs.write_table()`
- `fs.publish_table()`
- `fs.create_training_set()`

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Using a remote model registry

In addition to a remote [Feature Store](/concepts/feature-store.md), you may also specify a remote [Model Registry](/concepts/mlflow-model-registry.md) URI to share models across workspaces. You can combine both URIs when constructing the `FeatureStoreClient`:

```python
fs = FeatureStoreClient(
    feature_store_uri=f'databricks://<scope>:<prefix>',
    model_registry_uri=f'databricks://<scope>:<prefix>'
)
```

Then you can log and register models using [Feature Tables](/concepts/feature-table.md) from any local or remote [Feature Store](/concepts/feature-store.md):

```python
fs.log_model(
    model,
    "recommendation_model",
    flavor=mlflow.sklearn,
    training_set=training_set,
    registered_model_name="recommendation_model"
)
```

^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Example notebook

The source includes a notebook example titled "Centralized [Feature Store](/concepts/feature-store.md) example notebook" that demonstrates the complete workflow. Users are encouraged to consult that notebook for practical implementation details. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Related concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) – The recommended approach for sharing [Feature Tables](/concepts/feature-table.md).
- Feature Store Client API – Programmatic interface for [Feature Store](/concepts/feature-store.md) operations.
- [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md) – Legacy authentication method for cross-workspace access.
- Service Principals – Recommended identity for token-based automation.
- Secrets Management – How to securely store tokens and workspace metadata.
- [Model Registry](/concepts/mlflow-model-registry.md) – Cross-workspace sharing of registered models.

## Sources

- share-feature-tables-across-workspaces-legacy-databricks-on-aws.md

# Citations

1. [share-feature-tables-across-workspaces-legacy-databricks-on-aws.md](/references/share-feature-tables-across-workspaces-legacy-databricks-on-aws-144855e9.md)
