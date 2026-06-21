---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95b377de17928081119f1f03598a4eafd288509b6517e43fbf19cd471f0d0053
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sharing-tables-with-deletion-vectors-and-column-mapping
    - Column Mapping and Sharing Tables with Deletion Vectors
    - STWDVACM
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Sharing Tables with Deletion Vectors and Column Mapping
description: Sharing Delta tables that have storage optimizations like deletion vectors or column mapping enabled, requiring history sharing and specific recipient runtime versions.
tags:
  - delta-sharing
  - delta-lake
  - storage-optimization
timestamp: "2026-06-19T09:38:18.962Z"
---

# Sharing Tables with Deletion Vectors and Column Mapping

**Sharing Tables with Deletion Vectors and Column Mapping** refers to the practice of sharing [Delta Lake](/concepts/delta-lake.md) tables that have [Deletion Vectors](/concepts/deletion-vectors.md) or [column mapping](/concepts/column-mapping-in-delta-lake.md) enabled via [OpenSharing](/concepts/opensharing.md) (Delta Sharing) in Databricks. These storage‑optimization and schema‑evolution features require special handling to ensure recipients can query the data correctly.

## Overview

Deletion vectors allow Delta tables to mark rows as deleted without rewriting data files, improving write performance. Column mapping enables renaming and dropping columns without rewriting existing Parquet files. Both features are supported when sharing tables through OpenSharing, provided that the share is set up with history enabled and that recipients use a compatible compute engine. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

- **History sharing must be enabled** for the table. When adding a table to a share, you must select the option to share the table `WITH HISTORY` (full history from the beginning). This is necessary because deletion vectors and column mapping rely on the Delta transaction log, which is included in the history. ^[create-shares-for-opensharing-databricks-on-aws.md]
- The table must be a managed or external Delta table. Views, materialized views, and streaming tables are not subject to this requirement (though they cannot use deletion vectors or column mapping in the same way). ^[create-shares-for-opensharing-databricks-on-aws.md]

## How to Share a Table with Deletion Vectors or Column Mapping

The process is the same as adding any table to a share, but with history enabled. Use [Catalog Explorer](/concepts/catalog-explorer.md), SQL commands, or the Databricks CLI.

### Step‑by‑step (Catalog Explorer)

1. In your Databricks workspace, open **Catalog** and click the gear icon → **OpenSharing**.
2. On the **Shared by me** tab, select the share you want to modify (or create a new share).
3. Click **Manage assets > Edit assets**.
4. Browse to the Delta table you want to share and select it.
5. Enable **History** (toggle the **History** option). This ensures the Delta transaction log, including deletion vectors and column mapping metadata, is shared.
6. (Optional) Add an **Alias** or **Partition**.
7. Click **Save**.

After saving, the table is shared with full history, and recipients can query it. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Using SQL

```sql
ALTER SHARE share_name
ADD TABLE catalog.schema.table_name
WITH HISTORY;
```

## Recipient Requirements

For a recipient to successfully query a shared table that has deletion vectors or column mapping enabled, they must use one of the following compute engines:

- A SQL warehouse in Databricks
- A compute resource running Databricks Runtime 14.1 or above
- An open‑source client running `delta-sharing-spark` 3.1 or above

If the recipient uses an older compute engine, queries against the shared table may fail or return incorrect results. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Cloud Token Eligibility

When a table with deletion vectors or column mapping is shared with history and no partition filter, it may qualify for cloud token‑based direct file access (for Databricks‑to‑Databricks shares) or directory‑based access mode (for Databricks‑to‑Open shares). This provides recipients with direct read access to the underlying Delta files, improving performance. Cloud tokens are exchanged directly between metastores without long‑lived bearer tokens. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Deletion Vectors](/concepts/deletion-vectors.md) – Storage optimization for faster deletes
- [Column mapping](/concepts/column-mapping-in-delta-lake.md) – Schema evolution without rewriting data
- [Delta Sharing](/concepts/delta-sharing.md) – Open protocol for sharing data across platforms
- [History sharing](/concepts/table-history-sharing.md) – Sharing the Delta transaction log for time travel and consistency
- [OpenSharing](/concepts/opensharing.md) – Databricks implementation of Delta Sharing
- SQL warehouse – Compute engine that supports shared tables with these features
- Databricks Runtime 14.1 – Minimum runtime version for recipients

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
