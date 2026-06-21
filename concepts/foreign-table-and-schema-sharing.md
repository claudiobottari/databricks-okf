---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b62e63b85e01b136a53930839a05c6dc14e3426119d0660ebf76a314198ac14c
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foreign-table-and-schema-sharing
    - Schema Sharing and Foreign Table
    - FTASS
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Foreign Table and Schema Sharing
description: Sharing data from external systems via Lakehouse Federation without copying data into Databricks, using serverless compute for on-demand materialization on the provider side.
tags:
  - delta-sharing
  - lakehouse-federation
  - federation
timestamp: "2026-06-19T14:38:23.616Z"
---

---
title: Foreign Table and Schema Sharing
summary: Sharing foreign tables and schemas from external data sources via OpenSharing, enabling secure access to data in its original location without copying.
sources:
  - create-shares-for-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - delta-sharing
  - opensharing
  - foreign-tables
  - lakehouse-federation
aliases:
  - foreign-table-and-schema-sharing
  - FTS
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Foreign Table and Schema Sharing

**Foreign Table and Schema Sharing** refers to the ability to share data that is managed by external systems — such as other databases or catalogs — through [OpenSharing](/concepts/opensharing.md) without physically copying the data into Databricks. This capability builds on [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md), which allows Databricks to connect to external data sources and expose them as foreign schemas and tables in Unity Catalog. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Lakehouse Federation enables you to use Databricks to run queries against external data sources. You can create foreign schemas and tables, which contain data and metadata managed by external systems, with Unity Catalog adding data governance to query these tables. OpenSharing extends this by letting you securely share foreign data from its original location, without copying data into Databricks, complex network setups, or credential transfers. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

Before sharing foreign schemas or tables, the following prerequisites must be met:

- **Lakehouse Federation Sharing** must be enabled in your account-level Previews. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews). ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Serverless compute for workflows, notebooks, and Lakeflow Spark Declarative Pipelines** must be enabled in the account where foreign sharing is set up. See [Connect to serverless compute](https://docs.databricks.com/aws/en/compute/serverless/). ^[create-shares-for-opensharing-databricks-on-aws.md]
- When sharing foreign schemas and tables, the data is queried and temporarily materialized on the provider's side. By default, the materialized data is stored in a hidden schema using Databricks [default storage](/concepts/workspace-default-storage-path.md). Verify that you meet the requirements and observe the limitations for default storage. ^[create-shares-for-opensharing-databricks-on-aws.md]
- If you choose to use default storage, you must enable the **OpenSharing for Default Storage – Expanded Access** preview at the account level. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

- Shared foreign tables do **not** support `LIMIT` clauses or predicate pushdown. The system fully materializes all query results before returning them to the recipient, regardless of query filters. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Foreign tables that are too large to materialize cannot be shared. If materialization exceeds limits, the query fails. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Recommended Usage Patterns

Query results are generated on-demand for each query, so foreign table and schema sharing may not be as cost-efficient as sharing tables or materialized views. Databricks recommends the following: ^[create-shares-for-opensharing-databricks-on-aws.md]

- Keep the size of typical query results less than 10 GB. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Use ad-hoc exploratory queries instead of frequent data dumps. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When using cloud-token sharing, consider sharing [materialized views](/concepts/materialized-views-in-databricks.md) created on top of foreign tables for cost-efficiency and better performance. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Adding Foreign Schemas or Tables to a Share

You can add foreign schemas or tables to a share using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Using Catalog Explorer

1. Navigate to **Catalog** and open **OpenSharing**.
2. On the **Shared by me** tab, select the share you want to update.
3. Click **Manage assets > Edit assets**.
4. Search or browse for the foreign table or schema and select it.
5. (Optional) Add an **alias** to provide a more readable name that recipients will see and must use in queries. Recipients cannot use the actual foreign name if an alias is specified.
6. Click **Save**.

^[create-shares-for-opensharing-databricks-on-aws.md]

## Foreign Iceberg Tables

Foreign Iceberg tables are tables federated from foreign Iceberg catalogs using Lakehouse Federation. To share them, the table must have [Delta Uniform](/concepts/delta-uniform.md) enabled. Foreign Iceberg tables are automatically shared with full history. Partitions are not supported. ^[create-shares-for-opensharing-databricks-on-aws.md]

Additional requirements for foreign Iceberg sharing include enabling the **Lakehouse Federation Sharing** preview and — when sharing with open recipients not using Iceberg clients — enabling the **OpenSharing for Default Storage – Expanded Access** preview. ^[create-shares-for-opensharing-databricks-on-aws.md]

As with other foreign table sharing, `LIMIT` clauses and predicate pushdown are not supported for open recipients not using an Iceberg client; the system fully materializes query results. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Default Storage](/concepts/workspace-default-storage-path.md)
- [Materialized Views](/concepts/materialized-views-in-databricks.md)
- Foreign Iceberg Tables
- Serverless Compute

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
