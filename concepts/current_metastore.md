---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8bdcc1f5a422178e0ed2efe9d564898987c0b8716b5c8a46991f656b8fec9482
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - current_metastore
    - CURRENT_METASTORE
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: CURRENT_METASTORE
description: A Databricks default SQL function that returns the sharing identifier of the attached Unity Catalog metastore
tags:
  - sql-function
  - delta-sharing
  - metastore
timestamp: "2026-06-18T14:54:11.195Z"
---

Here is the wiki page for "CURRENT_METASTORE".

---

## CURRENT_METASTORE

**CURRENT_METASTORE** is a SQL function in Databricks that returns the sharing identifier of the Unity Catalog [Metastore](/concepts/metastore.md) attached to the current workspace. This identifier uniquely represents the [Metastore](/concepts/metastore.md) across cloud providers and regions, and is the key piece of information exchanged between provider and recipient workspaces when setting up [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) via [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Format

The function returns a string in the format:

```
<cloud>:<region>:<uuid>
```

Where: ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

- `<cloud>` is the cloud provider (e.g., `aws`, `azure`, `gcp`).
- `<region>` is the cloud region (e.g., `us-west-2`).
- `<uuid>` is the unique identifier for the [Metastore](/concepts/metastore.md).

### Example

```
aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016
```

^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Purpose

In the [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) model, a data provider must create a [recipient](/concepts/data-recipient.md) object to represent the consumer. This recipient object requires the consumer's sharing identifier so that the provider can establish a secure connection managed by Databricks. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The `CURRENT_METASTORE` function is the primary way for a consumer to obtain their own sharing identifier. They can then send this identifier to the provider, who enters it when creating the recipient object with the authentication type set to `DATABRICKS`. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Usage

You can call `CURRENT_METASTORE` from: ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

- A Databricks notebook using SQL or Python (via `spark.sql`).
- The Databricks SQL query editor.
- Any compute resource that is attached to a workspace enabled for [Unity Catalog](/concepts/unity-catalog.md).

The function only returns data when run against a Unity Catalog-capable compute. Workspaces not attached to a Unity Catalog [Metastore](/concepts/metastore.md) will not return a valid result. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Alternative Method (Catalog Explorer)

A user can also retrieve their sharing identifier through the Databricks Catalog Explorer UI. From the **Catalog** pane, clicking the gear icon and selecting **OpenSharing** shows the organization name in the upper right of the **Shared with me** tab. Clicking the name reveals a **Copy sharing identifier** option. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Example Query

```sql
SELECT CURRENT_METASTORE() AS sharing_identifier;
```

**Result:**

| sharing_identifier |
|---------------------|
| aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016 |

## Related Concepts

- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) — The overall sharing framework
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) — The specific sharing mode requiring a sharing identifier
- [Recipient (Data Sharing)](/concepts/recipient-delta-sharing.md) — The object that stores the sharing identifier
- [Provider (Data Sharing)](/concepts/delta-sharing.md) — The entity that creates shares and grants access
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The [Metastore](/concepts/metastore.md) uniquely identified by this function

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
