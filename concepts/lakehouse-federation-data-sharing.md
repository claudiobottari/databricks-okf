---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac5a126c6135523eb8bb01851ddf6f941764c53bc6109dc4e07340c4ad16c37a
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakehouse-federation-data-sharing
    - LFDS
    - Lakehouse Federation
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Lakehouse Federation Data Sharing
description: Sharing foreign schemas and tables from external data sources via Lakehouse Federation without copying data, using on-demand query materialization on the provider side.
tags:
  - delta-sharing
  - lakehouse-federation
  - foreign-tables
timestamp: "2026-06-18T14:55:34.183Z"
---

#Lakehouse Federation Data Sharing

**Lakehouse Federation Data Sharing** refers to the ability to securely share data from external sources—without copying that data into Databricks—by combining [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) with [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md). Using this feature, providers can share foreign schemas and tables (data that resides in external systems managed by Unity Catalog via Lakehouse Federation) directly from their original location, eliminating the need for complex network setups or credential transfers. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Lakehouse Federation allows you to run queries against external data sources by creating foreign schemas and tables in [Unity Catalog](/concepts/unity-catalog.md). OpenSharing then enables you to add those foreign objects to a share, granting recipients read access to the data without moving it. Unity Catalog applies its data governance layer (including row filters, column masks, and ABAC) on top of the foreign data, and the shared material is presented to the recipient as if it were a native Delta table. ^[create-shares-for-opensharing-databricks-on-aws.md]

There are two primary categories of foreign objects that can be shared:

- **Foreign schemas and tables** – standard federated objects from external databases.
- **Foreign Iceberg tables** – tables federated from external Iceberg catalogs that also have Delta Uniform enabled. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

### General prerequisites (all foreign sharing)

- The **Lakehouse Federation Sharing** preview must be enabled at the account level. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Serverless compute for workflows, notebooks, and Lakeflow Spark Declarative Pipelines** must be enabled in the account where the sharing is set up. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When sharing foreign data, the provider’s side queries and temporarily materializes the results. By default, the materialized data is stored in a hidden schema using Databricks [default storage](https://docs.databricks.com/aws/en/storage/default-storage). The provider must meet the [requirements](https://docs.databricks.com/aws/en/storage/default-storage#requirements) and observe the [limitations](https://docs.databricks.com/aws/en/storage/default-storage#limitations) for default storage. ^[create-shares-for-opensharing-databricks-on-aws.md]
- To use custom storage instead of Databricks default storage for temporary materialization, the provider must open a support case. ^[create-shares-for-opensharing-databricks-on-aws.md]
- If default storage is used, the **OpenSharing for Default Storage – Expanded Access** preview must be enabled. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Additional requirements for foreign Iceberg tables

- The foreign Iceberg table must have **Delta Uniform** enabled. Without Uniform, the table cannot be added to a share. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When sharing foreign Iceberg tables with open recipients who are **not** using Iceberg clients, the data is filtered and materialized using the provider’s compute and storage, potentially incurring additional costs. ^[create-shares-for-opensharing-databricks-on-aws.md]
- To keep the shared data fresh, providers should periodically refresh the foreign Iceberg table metadata (e.g., with a `SELECT` query, `REFRESH TABLE`, or a scheduled job). ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

### Foreign schemas and tables

- Shared foreign tables do **not** support `LIMIT` clauses or predicate pushdown. The system fully materializes all query results before returning them to the recipient, regardless of query filters. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Foreign tables that are too large to materialize cannot be shared; if materialization exceeds limits, the query fails. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Foreign Iceberg tables

- Partitions are **not** supported when sharing foreign Iceberg tables. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When sharing with open recipients who are not using an Iceberg client, the same full-materialization limitation applies: `LIMIT` clauses and predicate pushdown are unsupported. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Foreign Iceberg tables are always shared **with full history**. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Recommended usage patterns

Because query results are generated on-demand for each query, foreign table and schema sharing may not be as cost-efficient as sharing native Delta tables or materialized views. Databricks recommends the following: ^[create-shares-for-opensharing-databricks-on-aws.md]

- Keep the size of typical query results under **10 GB**. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Use foreign sharing for **ad-hoc exploratory queries** rather than frequent, high-volume data dumps. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When using cloud-token sharing (direct credential access), consider sharing materialized views built on top of the foreign tables for better cost efficiency and performance. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Adding foreign objects to a share

Foreign schemas and tables (including foreign Iceberg tables) can be added to a share using Catalog Explorer, SQL commands, or the Databricks Unity Catalog CLI. The procedure is identical to adding any other table (see Create shares for OpenSharing). When adding, you can optionally specify an alias for the foreign object; the alias becomes the name that recipients must use in queries. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related concepts

- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) – the foundation for querying external data sources.
- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) – the sharing protocol used to distribute foreign data.
- Foreign Tables – the Unity Catalog objects that represent external data.
- Foreign Iceberg Tables – Iceberg tables federated via Lakehouse Federation.
- [Unity Catalog](/concepts/unity-catalog.md) – the governance layer that controls access to shared foreign data.
- [Delta Sharing](/concepts/delta-sharing.md) – the open standard underlying OpenSharing.
- Serverless Compute – required for the provider’s materialization step.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
