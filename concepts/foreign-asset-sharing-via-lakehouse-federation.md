---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c6184cb8d19492a40984c772ddc23d9a226d3393a745e154e0eab213abe3b0a
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foreign-asset-sharing-via-lakehouse-federation
    - FASVLF
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Foreign Asset Sharing via Lakehouse Federation
description: The ability to share foreign schemas and tables (data managed by external systems) through OpenSharing without copying data or transferring credentials. Data is queried and temporarily materialized on the provider's side. Requires Lakehouse Federation Sharing preview, serverless compute, and default storage. Recommended for ad-hoc exploratory queries with result sizes under 10 GB.
tags:
  - delta-sharing
  - lakehouse-federation
  - federation
timestamp: "2026-06-19T18:02:19.074Z"
---

# Foreign Asset Sharing via Lakehouse Federation

**Foreign Asset Sharing via Lakehouse Federation** enables Databricks OpenSharing providers to securely share data from external databases and catalogs with recipients, without copying data into Databricks, setting up complex network configurations, or transferring credentials. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Lakehouse Federation allows Databricks to connect to and query external data sources. Foreign schemas and tables contain data and metadata managed by external systems, with Unity Catalog adding data governance for querying these tables. OpenSharing extends this capability by allowing providers to share foreign data from its original location. ^[create-shares-for-opensharing-databricks-on-aws.md]

When sharing foreign schemas and tables, the data is queried and temporarily materialized on the provider's side. By default, the materialized data is stored in a hidden schema using Databricks [default storage](/concepts/workspace-default-storage-path.md). ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

Before sharing foreign assets, the following prerequisites must be met:

- **Lakehouse Federation Sharing** must be enabled in the account-level Previews. See Manage Databricks previews. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Serverless compute for workflows, notebooks, and Lakeflow Spark Declarative Pipelines** must be enabled in the account where foreign schema or foreign table sharing is set up. See [Connect to serverless compute](/concepts/databricks-connect-with-serverless-compute.md). ^[create-shares-for-opensharing-databricks-on-aws.md]
- If using default storage, the **OpenSharing for Default Storage – Expanded Access** preview must be enabled at the account level. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Default storage requirements and limitations must be observed. For details about default storage regional availability, see Serverless availability. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

- Shared foreign tables do not support `LIMIT` clauses or predicate pushdown. The system fully materializes all query results before returning them to the recipient, regardless of query filters. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Foreign tables that are too large to materialize cannot be shared. If materialization exceeds limits, the query fails. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Recommended Usage Patterns

Query results are generated on-demand for each query, so foreign table and schema sharing may not be as cost-efficient as sharing tables or materialized views. Databricks recommends the following to improve performance:

- Keep the size of typical query results less than 10 GB. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Use ad-hoc exploratory queries instead of frequent data dumps. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When using cloud-token sharing, consider sharing [materialized views](/concepts/materialized-views-in-databricks.md) created on top of foreign tables for cost-efficiency and better performance. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Adding Foreign Schemas or Tables to a Share

Foreign schemas and tables can be added to a share using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor. ^[create-shares-for-opensharing-databricks-on-aws.md]

When adding a foreign schema or table, an optional alias can be specified to make the name more readable for recipients. The alias is the name that the recipient sees and must use in queries — recipients cannot use the actual foreign schema or table name if an alias is specified. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Custom Storage for Materialization

To opt out of using Databricks default storage and use your own storage for temporary materialization, open a support case. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing framework that enables foreign asset sharing
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) — The underlying technology for connecting to external data sources
- [Unity Catalog](/concepts/unity-catalog.md) — Provides data governance for foreign tables
- [Default Storage](/concepts/workspace-default-storage-path.md) — Storage used for temporary materialization of shared foreign data
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Recommended alternative for cost-efficient sharing of foreign data
- Serverless Compute — Required compute infrastructure for foreign asset sharing
- Foreign Iceberg Tables — A specific type of foreign table that can be shared

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
