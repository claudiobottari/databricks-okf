---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffc507db8cb24f0e47fb31104e025dfeb0a14d5b7866f6fe07f983256f1c86f1
  pageDirectory: concepts
  sources:
    - share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shared-infrastructure-requirements-for-cross-workspace-feature-store
    - SIRFCFS
  citations:
    - file: share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
    - file: |-
        share-feature-tables-across-workspaces-legacy-databricks-on-aws.md>

        As a security best practice
    - file: Databricks recommends using OAuth tokens for authentication with automated tools
    - file: systems
    - file: scripts
    - file: and apps. If using personal access token authentication
    - file: Databricks recommends using tokens belonging to service principals instead of workspace users. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
title: Shared Infrastructure Requirements for Cross-workspace Feature Store
description: Prerequisite that both local and remote workspaces must share the same external Hive metastore and have access to the same DBFS storage for cross-workspace feature store operations.
tags:
  - databricks
  - infrastructure
  - configuration
timestamp: "2026-06-19T23:05:18.300Z"
---

# Shared Infrastructure Requirements for Cross-workspace [Feature Store](/concepts/feature-store.md)

**Shared Infrastructure Requirements for Cross-workspace Feature Store** refers to the common infrastructure dependencies that must be in place for two or more Databricks workspaces to share [Feature Tables](/concepts/feature-tables.md) through a centralized [Feature Store](/concepts/feature-store.md). When an organization designates a single workspace to store all [Feature Store](/concepts/feature-store.md) metadata — enabling multiple teams or development stages to access the same [Feature Tables](/concepts/feature-tables.md) — both the local workspace and the centralized workspace must meet specific infrastructure prerequisites. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Overview

Databricks supports sharing [Feature Tables](/concepts/feature-tables.md) across multiple workspaces. For example, from your own workspace, you can create, write to, or read from a [Feature Table](/concepts/feature-table.md) in a centralized [Feature Store](/concepts/feature-store.md). Databricks recommends designating a single workspace to store all [Feature Store](/concepts/feature-store.md) metadata and creating accounts for each user who needs access to the [Feature Store](/concepts/feature-store.md). If your teams are also sharing models across workspaces, you may choose to dedicate the same centralized workspace for both [Feature Tables](/concepts/feature-tables.md) and models, or specify different centralized workspaces for each. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Requirements

To use a [Feature Store](/concepts/feature-store.md) across workspaces, the following infrastructure requirements must be met: ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### [Feature Store](/concepts/feature-store.md) Client Version

Both workspaces must use [Feature Store](/concepts/feature-store.md) client v0.3.6 or above. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Shared External Hive [Metastore](/concepts/metastore.md)

Both workspaces must have access to the raw feature data. They must share the same external Hive metastore. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Shared DBFS Storage

Both workspaces must have access to the same DBFS storage location. This shared storage is used to persist the actual feature data and is referenced when creating databases for [Feature Tables](/concepts/feature-tables.md). Before creating [Feature Tables](/concepts/feature-tables.md) in the remote [Feature Store](/concepts/feature-store.md), you must create a database in the shared DBFS location. For example: ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

```sql
CREATE DATABASE IF NOT EXISTS recommender LOCATION '/mnt/shared'
```

### IP Access List Configuration

If IP access lists are enabled on either workspace, the workspace IP addresses must be on the access lists to allow cross-workspace communication. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Authentication and Token Setup

Access to the centralized [Feature Store](/concepts/feature-store.md) is controlled by tokens. Each user or script that needs access must create a personal access token in the centralized [Feature Store](/concepts/feature-store.md) and copy that token into the secret manager of their local workspace. Each API request sent to the centralized [Feature Store](/concepts/feature-store.md) workspace must include the access token. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md>

As a security best practice, Databricks recommends using OAuth tokens for authentication with automated tools, systems, scripts, and apps. If using personal access token authentication, Databricks recommends using tokens belonging to service principals instead of workspace users. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

### Secret Setup

To store the credentials for the remote [Feature Store](/concepts/feature-store.md) workspace, you must configure secrets in the local workspace: ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

1. Create a secret scope: `databricks secrets create-scope --scope <scope>`.
2. Pick a unique identifier (shown as `<prefix>`) for the centralized workspace. Then create three secrets with the specified key names:
   - `<prefix>-host`: The hostname of the centralized workspace.
   - `<prefix>-token`: The access token from the centralized workspace.
   - `<prefix>-workspace-id`: The workspace ID for the centralized workspace.

This secret setup enables the construction of a [Feature Store](/concepts/feature-store.md) URI of the form `databricks://<scope>:<prefix>` for use with the `FeatureStoreClient`. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Deprecation Note

This approach is deprecated. Databricks recommends using [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) to share [Feature Tables](/concepts/feature-tables.md) across workspaces instead of the legacy method described here. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Centralized repository for machine learning features
- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — Modern approach for [Cross-Workspace Feature Sharing](/concepts/cross-workspace-feature-sharing.md)
- [Model Registry](/concepts/mlflow-model-registry.md) — For sharing models alongside [Feature Tables](/concepts/feature-tables.md)
- [External Hive Metastore](/concepts/object-ownership-in-hive-metastore.md) — Shared [Metastore](/concepts/metastore.md) requirement
- DBFS — Shared storage requirement

## Sources

- share-feature-tables-across-workspaces-legacy-databricks-on-aws.md

# Citations

1. [share-feature-tables-across-workspaces-legacy-databricks-on-aws.md](/references/share-feature-tables-across-workspaces-legacy-databricks-on-aws-144855e9.md)
2. share-feature-tables-across-workspaces-legacy-databricks-on-aws.md>

As a security best practice
3. Databricks recommends using OAuth tokens for authentication with automated tools
4. systems
5. scripts
6. and apps. If using personal access token authentication
7. Databricks recommends using tokens belonging to service principals instead of workspace users. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
