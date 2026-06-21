---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d250b44d01e522db0fa2c66a5055ecb76edddaafea33fe9645976170886b487
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - sharing-identifier
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: Sharing Identifier
description: A unique string identifying a Unity Catalog metastore, formatted as 'cloud:region:uuid', used by data providers to set up Databricks-to-Databricks sharing.
tags:
  - data-sharing
  - unity-catalog
  - identifier
timestamp: "2026-06-19T21:55:52.829Z"
---

# Sharing Identifier

A **sharing identifier** is a unique string that identifies a Unity Catalog [Metastore](/concepts/metastore.md), used to establish a secure Databricks-to-Databricks sharing connection between a data provider and a data recipient. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Format

The sharing identifier follows the format `<cloud>:<region>:<uuid>`, consisting of three parts:

- **Cloud**: The cloud provider where the [Metastore](/concepts/metastore.md) is hosted (e.g., `aws`, `gcp`, `azure`).
- **Region**: The cloud region where the [Metastore](/concepts/metastore.md) resides (e.g., `eu-west-1`, `us-west-2`).
- **UUID**: The unique identifier for the Unity Catalog [Metastore](/concepts/metastore.md).

For example: `aws:eu-west-1:b0c978c8-3e68-4cdf-94af-d05c120ed1ef` ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Purpose

In the Databricks-to-Databricks sharing model, a data provider creates a recipient object with an `authentication_type` of `DATABRICKS`. This recipient object represents a data recipient on a particular Unity Catalog [Metastore](/concepts/metastore.md), identified by the sharing identifier. Data shared with this recipient can only be accessed on that specific [Metastore](/concepts/metastore.md). The sharing identifier enables a secure connection managed by Databricks, eliminating the need for credential files or token-based authentication. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Obtaining the Sharing Identifier

A data recipient can obtain their sharing identifier using several methods:

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. On the **Shared with me** tab, select your Databricks sharing organization name in the upper right, and select **Copy sharing identifier**. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Using SQL

Use the default SQL function `CURRENT_METASTORE` in a Databricks notebook or Databricks SQL query:

```sql
SELECT CURRENT_METASTORE();
```

The query must run on a compute resource with standard or dedicated access mode in the workspace that will be used to access the shared data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Using the CLI

The sharing identifier can also be retrieved using the Databricks Unity Catalog CLI. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Relationship to Unity Catalog

Each [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) has exactly one sharing identifier. If multiple workspaces are attached to the same [Metastore](/concepts/metastore.md), they all share the same identifier. The sharing identifier is stable — it does not change unless the [Metastore](/concepts/metastore.md) itself is recreated in a different cloud or region. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Usage in Data Sharing

When creating a recipient for Databricks-to-Databricks sharing, the provider enters the full sharing identifier string. Once the recipient is created, the provider can grant access to one or more shares, making the data available in the recipient's workspace. The sharing identifier ensures that only the intended [Metastore](/concepts/metastore.md) can access the shared data. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open standard for secure data sharing that uses sharing identifiers
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) — The sharing model that requires sharing identifiers
- [Recipient](/concepts/data-recipient.md) — The named object representing a data consumer, created using the sharing identifier
- [Metastore](/concepts/metastore.md) — The Unity Catalog container that each sharing identifier uniquely identifies
- CURRENT_METASTORE SQL Function|CURRENT_METASTORE — The SQL function that returns the sharing identifier

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
2. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
