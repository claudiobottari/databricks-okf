---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85f03118ba6222fda0a929d4af1df84c1f1892287a99f2678c1bf4ab77026d5d
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - current_metastore-sql-function
    - CSF
    - CURRENT_METASTORE
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: CURRENT_METASTORE SQL Function
description: A Databricks SQL function that returns the sharing identifier of the current Unity Catalog metastore, used by recipients to discover their metastore identity for sharing.
tags:
  - sql-function
  - unity-catalog
  - sharing-identifier
timestamp: "2026-06-19T09:36:30.971Z"
---

# CURRENT_METASTORE SQL Function

The **CURRENT_METASTORE** SQL function is a built‑in function in Databricks SQL and notebooks that returns the identity of the Unity Catalog [Metastore](/concepts/metastore.md) attached to the current workspace. The output is a string in the format `<cloud>:<region>:<uuid>` and is primarily used during [OpenSharing] to share data with other Databricks workspaces. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Purpose

CURRENT_METASTORE provides the **sharing identifier** of a Unity Catalog [Metastore](/concepts/metastore.md). In [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md), the provider must know the recipient’s sharing identifier in order to create a [recipient](/concepts/data-recipient.md) object and grant access to shares. The function allows a recipient to retrieve their own [Metastore](/concepts/metastore.md) identifier quickly, without needing administrator assistance. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Usage

Call `CURRENT_METASTORE` in a Databricks notebook or in the Databricks SQL query editor. The compute resource must be Unity‑Catalog‑capable (standard or dedicated access mode). The function returns a single string value. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

```sql
SELECT CURRENT_METASTORE();
```

**Example output:**

```
aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016
```

^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Output Format

The returned string consists of three colon‑separated components:

| Component | Description |
|-----------|-------------|
| `<cloud>` | The cloud provider where the [Metastore](/concepts/metastore.md) is deployed, e.g. `aws`, `azure`, `gcp`. |
| `<region>` | The cloud region, e.g. `us-west-2`. |
| `<uuid>`  | The unique identifier for the Unity Catalog [Metastore](/concepts/metastore.md). |

Together, these components form the **sharing identifier** used in OpenSharing. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Related Concepts

- [Sharing Identifier](/concepts/sharing-identifier.md) – The [Metastore](/concepts/metastore.md) identity string used in Delta Sharing.
- [OpenSharing](/concepts/opensharing.md) – The Delta Sharing feature for cross‑workspace and cross‑platform data sharing.
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) – A sharing mode using this identifier for secure connections.
- [Recipient](/concepts/data-recipient.md) – The object that represents a consumer of shared data.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) service that manages the sharing identifier.
- CREATE RECIPIENT – The SQL command that requires the sharing identifier.

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
