---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2e929862d832b233b1a95c469004ed05f985d0ee59c3fd64ae4672cd2fbb5fa
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foreign-schema-and-table-sharing-lakehouse-federation
    - Table Sharing (Lakehouse Federation) and Foreign Schema
    - FSATS(F
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Foreign Schema and Table Sharing (Lakehouse Federation)
description: Sharing data from external systems (foreign tables/schemas) via Lakehouse Federation without copying data into Databricks, using on-demand materialization on the provider side.
tags:
  - delta-sharing
  - lakehouse-federation
  - foreign-tables
timestamp: "2026-06-19T09:38:02.539Z"
---

# Foreign Schema and Table Sharing (Lakehouse Federation)

**Foreign Schema and Table Sharing** (also known as **Lakehouse Federation Sharing**) allows you to securely share data from external systems — such as databases or catalogs outside Databricks — without copying the data into Databricks, setting up complex network configurations, or transferring credentials. The data remains in its original location and is queried on demand through [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md). ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Lakehouse Federation enables you to create **foreign schemas** and **foreign tables** that represent data and metadata managed by external systems, with [Unity Catalog](/concepts/unity-catalog.md) adding data governance and access control. OpenSharing extends this capability by letting you share foreign schemas and tables with [Recipients](/concepts/data-recipient.md) through the same secure sharing infrastructure used for managed Delta tables. ^[create-shares-for-opensharing-databricks-on-aws.md]

When a recipient queries a shared foreign schema or table, the provider’s side queries the external source, filters the data, and temporarily materializes the results in a hidden schema. By default, this materialized data is stored in Databricks’ [Default Storage](/concepts/workspace-default-storage-path.md). You can opt out of default storage and provide your own storage by opening a support case. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

Before sharing foreign schemas or tables, you must meet the following requirements:

- **Lakehouse Federation Sharing preview** must be enabled at the account level. See Manage Databricks previews. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Serverless compute** must be enabled for workflows, notebooks, and Lakeflow Spark Declarative Pipelines in the account where the sharing is set up. See [Connect to serverless compute](/concepts/databricks-connect-with-serverless-compute.md). ^[create-shares-for-opensharing-databricks-on-aws.md]
- If you plan to use default storage for temporary materialization, enable the **OpenSharing for Default Storage – Expanded Access** preview at the account level. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Default storage must meet its own requirements and limitations. See Default storage requirements and Default storage limitations. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

- **No `LIMIT` clause or predicate pushdown** — the system fully materializes all query results before returning them to the recipient, regardless of query filters. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Size limits** — foreign tables that are too large to materialize cannot be shared. If materialization exceeds system limits, the query fails. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Recommended Usage Patterns

Because results are generated on-demand for each query, sharing foreign schemas and tables may be less cost-efficient than sharing regular tables or materialized views. Databricks recommends: ^[create-shares-for-opensharing-databricks-on-aws.md]

- Keep the size of typical query results **under 10 GB**.
- Use foreign sharing for **ad-hoc exploratory queries** rather than frequent data dumps.
- When using cloud-token sharing, consider sharing **materialized views created on top of foreign tables** for better performance and cost efficiency.

## Adding Foreign Schemas and Tables to a Share

You can add foreign schemas or tables to an existing share using **Catalog Explorer**, **SQL commands**, or the **Databricks Unity Catalog CLI**. ^[create-shares-for-opensharing-databricks-on-aws.md]

When adding a foreign table, you may optionally specify an **alias** (alternate name) that recipients will see and must use in queries. If no alias is set, recipients use the original table name. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Via Catalog Explorer

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, find the share you want to add a foreign table or schema to and click its name.
4. Click **Manage assets > Edit assets**.
5. Search or browse for the foreign table or schema you want to share and select it.
6. (Optional) Click the speech-bubble icon under the **Alias** column to specify an alias.
7. Click **Save**. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) — The underlying technology for connecting to external data sources.
- [OpenSharing](/concepts/opensharing.md) — The secure sharing mechanism that enables foreign table sharing.
- [Default Storage](/concepts/workspace-default-storage-path.md) — Where temporary materialized data is stored by default.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Can be created on top of foreign tables for better performance.
- Foreign Iceberg Tables — Sharing Iceberg tables federated from external Iceberg catalogs.
- Serverless Compute — Required for foreign table sharing.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
