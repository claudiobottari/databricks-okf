---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d170e82f6934abee9776c8c079d47560783945fd6f98c1a0f7f904cec9821100
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-table-sharing
    - STS
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Streaming Table Sharing
description: Sharing streaming tables (append-only Delta tables with incremental processing) with restrictions on partition filters, CDF support for open recipients, and predicate pushdown.
tags:
  - delta-sharing
  - streaming
  - real-time
timestamp: "2026-06-19T14:38:38.400Z"
---

# Streaming Table Sharing

**Streaming Table Sharing** refers to the ability to share streaming tables from a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) with recipients using [OpenSharing](/concepts/opensharing.md) ([Delta Sharing](/concepts/delta-sharing.md)). Streaming tables are regular Delta tables that support streaming or incremental data processing; they are designed for append-only data sources and process inputs only once. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Streaming tables can be added to a share alongside other data assets such as regular tables, views, materialized views, and volumes. When a streaming table is included in a share, recipients can read the current snapshot of the table. For [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md), recipients may also perform time-travel queries, read the table with Spark Structured Streaming, or run transactions if history sharing is enabled. For [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) (open recipients), only the current snapshot is accessible; time travel, streaming reads, and change data feed (CDF) are not supported. ^[create-shares-for-opensharing-databricks-on-aws.md]

You can also share an entire schema that contains streaming tables. When you add a schema to a share, all streaming tables currently in the schema, as well as any streaming tables added to the schema in the future, are automatically shared. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

- Shareable streaming tables must be defined on [Delta tables](/concepts/delta-lake-table.md) or other shareable streaming tables or views. ^[create-shares-for-opensharing-databricks-on-aws.md]
- To add a streaming table to a share, you must use a SQL warehouse or a compute running Databricks Runtime 13.3 LTS or above. ^[create-shares-for-opensharing-databricks-on-aws.md]
- If your workspace has workspace-catalog bindings enabled, verify that the workspace has read and write access to the catalog containing the streaming table. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

- A shared streaming table **cannot** have row filters or column masks applied directly to it. However, the base table that the streaming table is built on *can* have row filters and column masks. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Partition filters** are not supported on streaming tables in a share. To achieve partitioned access, create a view on top of the streaming table and share the view instead. ^[create-shares-for-opensharing-databricks-on-aws.md]
- For open (non-Databricks) recipients, `LIMIT` clauses and predicate pushdown are **not supported** when the recipient does not have direct access to the underlying data. The system fully materializes all query results before returning them, regardless of query filters. ^[create-shares-for-opensharing-databricks-on-aws.md]
- General streaming table limitations (see Streaming table limitations) also apply. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Cloud tokens (directory-based access mode) are **not supported** for streaming tables. Only regular Delta tables shared with full history and without partition filters are eligible for cloud token access. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Adding a Streaming Table to a Share

You can add a streaming table to a share using Catalog Explorer, SQL commands, or the Databricks CLI. Below are the general steps for Catalog Explorer:

1. In your Databricks workspace, navigate to **Catalog** and click the gear icon to select **OpenSharing** (or click **Share > OpenSharing** in the upper-right corner).
2. On the **Shared by me** tab, find the share you want to modify and click its name.
3. Click **Manage assets > Edit assets**.
4. Search or browse for the streaming table you want to share and select it.
5. (Optional) Provide an **alias** – an alternate name that the recipient will see and use in queries. If an alias is specified, recipients cannot use the actual streaming table name.
6. Click **Save**.

^[create-shares-for-opensharing-databricks-on-aws.md]

To remove a streaming table from a share, see [Update shares](/concepts/delta-sharing.md).

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for data sharing across platforms.
- [OpenSharing](/concepts/opensharing.md) — Databricks’ implementation of the Delta Sharing protocol for Unity Catalog.
- Streaming Tables — Incremental processing tables in Databricks.
- [Unity Catalog](/concepts/unity-catalog.md) — The unified governance layer for data and AI assets.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Another type of shared asset that can be queried efficiently.
- [Schema Sharing](/concepts/schema-level-sharing.md) — Sharing entire schemas, which includes all current and future streaming tables.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
