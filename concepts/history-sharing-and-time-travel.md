---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5801009d80aa14fbe816313a132b419664b1c96554491e889cd0d3e4cb00e18a
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - history-sharing-and-time-travel
    - Time Travel and History Sharing
    - HSATT
    - Delta Table History and Time Travel
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
    - file: abac-policy-audit-logging.md
title: History Sharing and Time Travel
description: Sharing the Delta transaction log history of a table to enable recipients to perform time travel queries, read with Spark Structured Streaming, and access Change Data Feed.
tags:
  - delta-sharing
  - time-travel
  - delta-lake
timestamp: "2026-06-18T11:24:54.801Z"
---

# History Sharing and Time Travel

**History sharing** is a feature in Databricks OpenSharing that allows providers to share the full historical record of a Delta table with recipients, enabling them to perform time travel queries, read the table with Spark Structured Streaming, or run transactions. When history is enabled, the table's Delta log is also shared to improve performance for Databricks-to-Databricks shares. ^[create-shares-for-opensharing-databricks-on-aws.md]

## How History Sharing Works

When a provider adds a table to a share with history, the recipient gains access to the table's complete version history from the beginning. This differs from sharing without history, where recipients only see the current snapshot of the table. History sharing is enabled by default when adding an entire schema to a share. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Requirements for History Sharing

- History sharing requires Databricks Runtime 12.2 LTS or above. ^[create-shares-for-opensharing-databricks-on-aws.md]
- For [Databricks-to-Databricks](/concepts/databricks-to-databricks-sharing.md) shares, the shared Delta log provides performance comparable to direct source table access. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Enabling History in the UI

When adding a table to a share using Catalog Explorer, the history option is controlled by a toggle under the **History** column. To enable history sharing: ^[create-shares-for-opensharing-databricks-on-aws.md]

1. Open the share in Catalog Explorer.
2. Click **Manage assets > Edit assets**.
3. Select the table and toggle the **History** option on.

If you select an entire schema instead of individual tables, history is included by default. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Time Travel for Recipients

When a table is shared with history, recipients can perform [time travel](/concepts/delta-lake-time-travel.md) queries against the shared table using the Delta table's version history. This allows recipients to: ^[create-shares-for-opensharing-databricks-on-aws.md]

- Query the table as it existed at any previous point in time.
- Read the table with Spark Structured Streaming for incremental processing.
- Run transactions on the shared data.

Time travel queries require Databricks Runtime 12.2 LTS or above on the recipient side. ^[create-shares-for-opensharing-databricks-on-aws.md]

### CDF Support with History Sharing

When a table is shared with history and [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) is enabled, recipients can use CDF to track changes to the table over time. This is useful for incremental processing and data synchronization workflows. ^[create-shares-for-opensharing-databricks-on-aws.md]

## History Sharing and Cloud Tokens

History sharing affects which access mechanism is used for the shared data. The use of cloud tokens (temporary, path-scoped cloud credentials) depends on whether history is shared: ^[create-shares-for-opensharing-databricks-on-aws.md]

### Databricks-to-Databricks Sharing

For [Databricks-to-Databricks](/concepts/databricks-to-databricks-sharing.md) shares, cloud tokens are used when:
- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared without a partition filter.

### Databricks-to-Open Sharing

For [Databricks-to-Open](/concepts/databricks-to-open-sharing.md) sharing, cloud tokens (directory-based access mode) are used when:
- The shared object is a managed or external Delta table.
- The table is shared `WITH HISTORY` (full history from the beginning).
- The table is shared without a partition filter.
- The table is not a CCv2 table.
- The table does not use [default storage](/concepts/workspace-default-storage-path.md).

When cloud token access is used, recipients receive credentials scoped to the root directory of the shared Delta table. This grants read access to both the data files and the Delta log, which contains the commit history, information about the committer, and deleted data that has not been vacuumed. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Security Considerations

When sharing history, providers should be aware that the Delta log contains: ^[create-shares-for-opensharing-databricks-on-aws.md]

- The commit history for each table version.
- Information about the committer.
- Deleted data that has not been vacuumed.

If you need to share only a subset of the data or restrict access to certain historical versions, consider using partition filtering or [Recipient Properties](/concepts/recipient-properties.md) to control what data is visible to each recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Best Practices

- **Share schemas for automatic history.** When you add an entire schema, history is included by default and all assets added to the schema in the future will also be shared with history. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Use history for CDF workflows.** If recipients need Change Data Feed (CDF), share a regular Delta table with history enabled rather than a streaming table, which only supports the current snapshot for open recipients. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Audit shared history.** Monitor which tables are shared with history using [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) to track changes to sharing configurations. ^[abac-policy-audit-logging.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The protocol for sharing data between Databricks workspaces
- [Time travel](/concepts/delta-lake-time-travel.md) — Querying historical versions of Delta tables
- Cloud tokens — Temporary credentials for direct data access
- Spark Structured Streaming — Streaming reads from shared tables
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — Tracking changes to shared tables
- Delta Log — The transaction log containing commit history
- [OpenSharing](/concepts/opensharing.md) — The Databricks sharing model

## Sources

- create-shares-for-opensharing-databricks-on-aws.md
- abac-policy-audit-logging.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
2. abac-policy-audit-logging.md
