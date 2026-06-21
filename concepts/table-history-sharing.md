---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b2cce6d07b69854d948d2dfc708347ddf47092b1f8c2a8d11ac8773d2d0b4dda
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-history-sharing
    - THS
    - History Sharing
    - History sharing
    - Table history
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Table History Sharing
description: Sharing a table's history (Delta log) in a share to allow recipients to perform time travel queries, read with Spark Structured Streaming, run transactions, and improve performance for Databricks-to-Databricks shares. Requires Databricks Runtime 12.2 LTS or above. Required when sharing tables with deletion vectors or column mapping.
tags:
  - delta-sharing
  - time-travel
  - delta-lake
timestamp: "2026-06-19T18:02:26.353Z"
---

# Table History Sharing

**Table History Sharing** is a feature of [OpenSharing](/concepts/opensharing.md) on Databricks that allows data providers to share the full history of a Delta table (or a managed Iceberg table) with recipients. When enabled, recipients can perform time travel queries, read the table with Spark Structured Streaming, or run transactions using the shared table’s historical versions. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

When a provider adds a table to a share, they can optionally enable **History** sharing. This grants the recipient access to all past versions of the table, not just the current snapshot. The recipient can query the table as it existed at any point in its history using time travel syntax (e.g., `VERSION AS OF` or `TIMESTAMP AS OF`). ^[create-shares-for-opensharing-databricks-on-aws.md]

History sharing is required for the following use cases:

- **Time travel queries** – read the table at a specific version or timestamp. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Spark Structured Streaming** – use the shared table as a streaming source. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Transactions** – perform read or write transactions against the shared table (depending on the sharing protocol). ^[create-shares-for-opensharing-databricks-on-aws.md]

For [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md), the table’s Delta log is also shared, which improves read performance. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

- History sharing requires recipients to use Databricks Runtime 12.2 LTS or above. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When adding a table to a share, the provider must explicitly turn on the **History** option in Catalog Explorer or use the `WITH HISTORY` clause in SQL. ^[create-shares-for-opensharing-databricks-on-aws.md]
- For **managed Iceberg tables**, history sharing is automatically included when the table is added to a share. ^[create-shares-for-opensharing-databricks-on-aws.md] *(This is inferred from the statement "Managed Iceberg tables are automatically shared with full history" in the foreign Iceberg section, but it applies to all managed Iceberg tables.)*

## Impact on Cloud Token Access

History sharing is a prerequisite for cloud token (directory-based) access, which gives recipients direct, performant reads from cloud storage. The eligibility rules differ by protocol:

### Databricks-to-Databricks sharing
Cloud tokens are used when **all** of the following are true:
- The table is shared `WITH HISTORY` (full history from the beginning). ^[create-shares-for-opensharing-databricks-on-aws.md]
- The table is shared without a partition filter. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Databricks-to-Open sharing
Cloud tokens (directory-based access mode) are used when **all** of the following are true:
- The shared object is a managed or external Delta table. ^[create-shares-for-opensharing-databricks-on-aws.md]
- The table is shared `WITH HISTORY` (full history from the beginning). ^[create-shares-for-opensharing-databricks-on-aws.md]
- The table is shared without a partition filter. ^[create-shares-for-opensharing-databricks-on-aws.md]
- The table is not a CCv2 table. ^[create-shares-for-opensharing-databricks-on-aws.md]
- The table does not use default storage. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Security Considerations

When cloud token access is enabled, recipients receive credentials scoped to the root directory of the shared Delta table. This grants read access to **both the data files and the Delta log**. The Delta log contains the commit history for each table version, information about the committer, and deleted data that has not been vacuumed. Providers should be aware of this before enabling history sharing for sensitive tables. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- Time Travel (Delta Lake)
- Spark Structured Streaming
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md)
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md)
- Cloud Token Access
- Delta Log
- Managed Iceberg Tables – also shared with full history.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
