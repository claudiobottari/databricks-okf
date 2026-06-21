---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16753fdf0b8583534a5a5e2a0a475b9adddb71d90096e6f00b5977d595e8cbb3
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-share-object
    - OSO
    - Share Object
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: OpenSharing Share Object
description: A securable object in Unity Catalog used to share data and AI assets (tables, views, volumes, notebooks, models, FeatureSpecs, Genie Spaces) with one or more recipients. Shares can contain assets from only one metastore and support dynamic addition/removal of assets.
tags:
  - delta-sharing
  - unity-catalog
  - data-sharing
timestamp: "2026-06-19T18:02:50.118Z"
---

# OpenSharing Share Object

An **OpenSharing Share Object** (or simply a **share**) is a [Unity Catalog](/concepts/unity-catalog.md) securable object that enables data providers to share data and AI assets with one or more recipients through the [OpenSharing](/concepts/opensharing.md) (Delta Sharing) protocol. Shares allow controlled, governed access to data without requiring recipients to have direct Databricks accounts or network access to the provider's storage. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

A share acts as a container for assets such as tables, views, volumes, notebooks, and AI models. All assets in a share must come from a single Unity Catalog [Metastore](/concepts/metastore.md). Providers can add or remove assets at any time, and recipients see only the current set of shared objects. Shares can also include entire schemas, which automatically propagate future assets added to that schema. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Shareable Assets

A share can contain any combination of the following asset types:

| Asset Type | Notes |
|------------|-------|
| **Tables and table partitions** | Regular Delta tables, optionally shared with partition filters or aliases |
| **Streaming tables** | Append-only tables for incremental processing; certain limitations apply for open recipients |
| **Managed Iceberg tables** | Iceberg tables managed in Unity Catalog (not shareable to external Iceberg clients) |
| **Foreign Iceberg tables** | Federated Iceberg tables from external catalogs; must have Delta Uniform enabled |
| **Foreign schemas and tables** | Tables from external data sources via [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md); data is materialized on the provider side |
| **Views** | Read-only query objects; cannot reference shared tables or foreign tables |
| **Dynamic views** | Use `CURRENT_RECIPIENT()` to restrict rows/columns per recipient |
| **Materialized views** | Precomputed views that improve query performance |
| **Volumes** | Non-tabular file-based data |
| **Python UDFs** | User-defined functions written in Python |
| **Notebooks** | Databricks notebooks |
| **AI models** | Registered models in Unity Catalog |
| **Genie Spaces** | Collaborative Genie workspaces |
| **`FeatureSpecs`** | Feature engineering specifications |

Sharing an entire schema includes all current and future tables, streaming tables, views, materialized views, models, and volumes in that schema. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Creating a Share

Shares can be created using **Catalog Explorer**, **SQL commands**, or the **Databricks Unity Catalog CLI**.

### Requirements

- Compute resources must run Databricks Runtime 11.3 LTS or above (standard or dedicated access mode) when using notebooks
- SQL warehouse or compute running Databricks Runtime 13.3 LTS or above is required for SQL operations involving schemas

### Using Catalog Explorer

1. In the Databricks workspace, click **Catalog** > gear icon > **OpenSharing**
2. On the **Shared by me** tab, click **Share data**
3. Provide a share name and optional comment
4. Add data assets, notebooks, and recipients as needed
5. Click **Share data** to finalize

### Using SQL

```sql
CREATE SHARE share_name [COMMENT 'optional comment'];
```

Then add assets using `ALTER SHARE ... ADD ...`. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Adding Assets to a Share

When adding tables, providers can:

- Specify **partitions** to share only a subset of data
- Set **aliases** to provide recipient-friendly names
- Enable **history sharing** to support time travel and streaming reads
- Use **recipient properties** (e.g., `CURRENT_RECIPIENT().country`) to dynamically filter partitions per recipient

### Cloud Token Eligibility

For Databricks-to-Databricks sharing, cloud tokens (temporary path-scoped credentials) are used when a table is shared `WITH HISTORY` and without partition filters. This gives recipients direct read access to Delta table files, improving performance. For Databricks-to-Open sharing, cloud tokens (directory-based access mode) require additional conditions: the shared object must be a managed or external Delta table, shared with full history, without partition filters, and not a CCv2 table or using default storage. ^[create-shares-for-opensharing-databricks-on-aws.md]

### ABAC Policies

Shares can include tables or schemas protected by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies. However, the share owner must be a **privileged user** (excluded from the policy) to ensure recipients gain full access to the shared asset. ABAC policies do not govern recipient access; they are applied only at the provider level. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Managing Shares

Providers can update shares at any time to:

- Add or remove assets
- Change partitions or aliases
- Revoke or grant access to recipients

Recipients must be created separately and assigned to shares. For detailed management workflows, see [Manage OpenSharing Data Shares](/concepts/opensharing-share.md). ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The overall data sharing framework on Databricks
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol underlying OpenSharing
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that secures shares
- [OpenSharing Recipient](/concepts/opensharing-recipient.md) – The entity that receives access to a share
- [OpenSharing Provider](/concepts/opensharing-provider-object.md) – The entity that creates and manages shares
- Dynamic Views with CURRENT_RECIPIENT()|Dynamic Views with CURRENT_RECIPIENT – Fine-grained row/column access control
- Cloud Token Access – Direct storage access for shared Delta tables

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
