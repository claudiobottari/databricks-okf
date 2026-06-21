---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 043703501bdb2006363f0ed69c30859070cd4222a97384dee74db8f3593b36a5
  pageDirectory: concepts
  sources:
    - share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-client-uri-databricks
    - FSCU(
    - Feature Store in Databricks
  citations:
    - file: share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
title: Feature Store Client URI (databricks://)
description: A URI scheme of the form 'databricks://<scope>:<prefix>' used to specify a remote feature store or model registry when instantiating a FeatureStoreClient in Databricks.
tags:
  - databricks
  - api
  - configuration
timestamp: "2026-06-19T23:05:11.706Z"
---

## [Feature Store](/concepts/feature-store.md) Client URI (databricks://)

The **Feature Store Client URI** (`databricks://`) is a connection string used by the `FeatureStoreClient` to access a remote [Feature Store](/concepts/feature-store.md) workspace. It encodes the credentials needed to authenticate and communicate with the centralized [Feature Store](/concepts/feature-store.md) across workspace boundaries. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Legacy Status

> **Important:** This approach is **deprecated**. Databricks now recommends using [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) to share [Feature Tables](/concepts/feature-tables.md) across workspaces. The `databricks://` URI is part of the legacy cross-workspace [Feature Store](/concepts/feature-store.md) sharing mechanism. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Structure

The URI follows the format:

```
databricks://<scope>:<prefix>
```

- `<scope>` is the name of a Databricks secret scope that stores the remote workspace credentials.
- `<prefix>` is a unique identifier you choose for the remote workspace. It is used as a prefix for the secret keys within that scope. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Prerequisites

To use a `databricks://` URI, you must first set up secrets in the local workspace that contain the connection details for the remote [Feature Store](/concepts/feature-store.md) workspace:

| Secret Key | Value |
|---|---|
| `<prefix>-host` | The hostname (URL) of the remote workspace. Can be retrieved via `mlflow.utils.databricks_utils.get_webapp_url()` in Python. |
| `<prefix>-token` | A personal access token (or OAuth token) for the remote workspace. For security, use a service principal token. |
| `<prefix>-workspace-id` | The workspace ID of the remote workspace (found in the URL of any page). |

The secrets must be stored in a pre-created secret scope using the Databricks CLI. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Usage

Once the secrets are in place, construct the URI and pass it to `FeatureStoreClient`:

```python
from databricks.feature_store import FeatureStoreClient

feature_store_uri = "databricks://my_scope:my_prefix"
fs = FeatureStoreClient(feature_store_uri=feature_store_uri)
```

With this client, you can perform all standard [Feature Store](/concepts/feature-store.md) operations—such as `create_table`, `read_table`, `write_table`, `publish_table`, and `create_training_set`—on the remote workspace. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

You can also specify a separate `model_registry_uri` using the same URI format to share models across workspaces concurrently:

```python
fs = FeatureStoreClient(
    feature_store_uri="databricks://my_scope:my_prefix",
    model_registry_uri="databricks://my_scope:my_prefix"
)
```

This allows training a model using a remote [Feature Table](/concepts/feature-table.md) and registering it in a remote model registry. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Requirements

- [Feature Store](/concepts/feature-store.md) client v0.3.6 or above.
- Both workspaces must share the same external Hive metastore and have access to the same DBFS storage.
- If IP access lists are enabled, the local workspace's IP addresses must be on the remote workspace's allow list. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Related Concepts

- Feature Store Client — The Python client used to interact with [Feature Tables](/concepts/feature-tables.md).
- [Cross-workspace model sharing](/concepts/cross-workspace-feature-sharing.md) — Analogous pattern for sharing registered models across workspaces.
- [Secret scopes](/concepts/databricks-secret-scopes.md) — Databricks feature for securely storing credentials.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The modern, recommended alternative for sharing [Feature Tables](/concepts/feature-tables.md).
- Service principal authentication — Best practice for automated access tokens.

### Sources

- share-feature-tables-across-workspaces-legacy-databricks-on-aws.md

# Citations

1. [share-feature-tables-across-workspaces-legacy-databricks-on-aws.md](/references/share-feature-tables-across-workspaces-legacy-databricks-on-aws-144855e9.md)
