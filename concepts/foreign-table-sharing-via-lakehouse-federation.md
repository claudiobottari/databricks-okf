---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1aa3fe0caa9edcba66f71a8c6be3174d8bfc149ce64816428816249c42691c23
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foreign-table-sharing-via-lakehouse-federation
    - FTSVLF
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Foreign Table Sharing via Lakehouse Federation
description: Securely sharing data from external database systems through Lakehouse Federation without copying data, using on-demand query materialization on the provider side.
tags:
  - delta-sharing
  - lakehouse-federation
  - federation
timestamp: "2026-06-18T11:24:27.949Z"
---

# Foreign Table Sharing via Lakehouse Federation

**Foreign Table Sharing via Lakehouse Federation** enables Databricks users to securely share data from external systems — such as other databases or catalogs — without copying the data into Databricks, configuring complex network setups, or transferring credentials. The shared data is accessed through foreign schemas and tables that Unity Catalog connects to via [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md), with the data being queried and temporarily materialized on the provider side at query time. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Lakehouse Federation allows Databricks to run queries against external data sources. Foreign schemas and tables contain data and metadata managed by external systems, while Unity Catalog adds data governance to queries against these tables. OpenSharing extends this capability by allowing providers to add foreign schemas or tables to a share, making them available to recipients without physical data movement. ^[create-shares-for-opensharing-databricks-on-aws.md]

When sharing foreign schemas and tables, the data is queried and temporarily materialized on the provider’s side. By default, the materialized data is stored in a hidden schema using Databricks [default storage](https://docs.databricks.com/aws/en/storage/default-storage). The provider can opt out of using default storage and use their own storage for temporary materialization by opening a support case. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

To share foreign schemas or tables, you must meet the following prerequisites:

- **Lakehouse Federation Sharing preview**: You must enable this feature in your account-level Previews. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews). ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Serverless compute**: You must enable **Serverless compute for workflows, notebooks, and Lakeflow Spark Declarative Pipelines** in the account where foreign schema or foreign table sharing is set up. See [Connect to serverless compute](https://docs.databricks.com/aws/en/compute/serverless/). ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Default storage**: If you choose to use default storage for temporary materialization, you must enable the **OpenSharing for Default Storage – Expanded Access** preview at the account level. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews). Verify that you meet the requirements and observe the limitations for default storage. For details about default storage regional availability, see [Serverless availability](https://docs.databricks.com/aws/en/resources/feature-region-support#serverless-aws). ^[create-shares-for-opensharing-databricks-on-aws.md]
- **General share requirements**: You must meet the standard requirements for creating shares in OpenSharing. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

- **No predicate pushdown**: Shared foreign tables do not support `LIMIT` clauses or predicate pushdown. The system fully materializes all query results before returning them to the recipient, regardless of query filters. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Size limits**: Foreign tables that are too large to materialize cannot be shared. If materialization exceeds limits, the query fails. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Views referencing foreign tables**: You cannot share views that reference foreign tables, including foreign Iceberg tables. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Recommended Usage Patterns

Because query results are generated on-demand for each query, foreign table and schema sharing may be less cost-efficient compared to sharing regular tables or [materialized views](/concepts/materialized-views-in-databricks.md). Databricks recommends the following to improve performance:

- Keep the size of typical query results under 10 GB. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Use ad-hoc exploratory queries instead of frequent data dumps. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When using cloud-token sharing, consider sharing materialized views created on top of foreign tables for cost-efficiency and better performance. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Foreign Iceberg Tables

[Foreign Iceberg tables](/concepts/foreign-iceberg-table-sharing.md) are a specific type of foreign table — those federated from foreign Iceberg catalogs using Lakehouse Federation. These tables can be shared through OpenSharing, and recipients can also access them using external Iceberg clients if [Delta Uniform](/concepts/delta-uniform.md) is enabled on the table. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Additional Requirements for Foreign Iceberg Tables

- You must enable the **Lakehouse Federation Sharing** preview at the account level. ^[create-shares-for-opensharing-databricks-on-aws.md]
- If sharing with open recipients not using Iceberg clients, you must use default storage and enable the **OpenSharing for Default Storage – Expanded Access** preview. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Foreign Iceberg tables must have Delta Uniform enabled; otherwise, the table cannot be added to a share. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Limitations for Foreign Iceberg Tables

- Partitions are not supported. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When sharing with open recipients not using an Iceberg client, `LIMIT` clauses and predicate pushdown are not supported. The system fully materializes all query results. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Refreshing Data

To ensure recipients receive the freshest data, you should periodically refresh your foreign Iceberg tables. Any `SELECT` query or `REFRESH TABLE` command refreshes the table metadata. Databricks recommends setting up a scheduled job to keep the foreign Iceberg table in sync with the remote Iceberg source. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Adding Foreign Schemas or Tables to a Share

You can add foreign schemas or tables using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor. The process is similar to adding regular tables, with the same aliasing and partition options (though partitions are not supported for foreign Iceberg tables). ^[create-shares-for-opensharing-databricks-on-aws.md]

When adding a foreign schema, all supported data assets in that schema become available to recipients. Unsupported asset types (e.g., tables with liquid clustering and partition filtering, R2 tables with V2 checkpoint, tables with collations or row filters/column masks, `SHALLOW CLONE` tables, foreign key constraints) are filtered out and not shared. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) — The technology for connecting to external data sources
- [OpenSharing](/concepts/opensharing.md) — The Delta Sharing protocol used for sharing data
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer managing foreign objects
- Foreign Iceberg Tables — A specific type of foreign table for Iceberg catalogs
- [Delta Uniform](/concepts/delta-uniform.md) — Required for sharing foreign Iceberg tables to Iceberg clients
- [Default Storage](/concepts/workspace-default-storage-path.md) — Storage used for temporary materialization of shared foreign data
- Serverless Compute — Compute environment required for foreign table sharing
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Recommended alternative for cost-efficient sharing of foreign data
- [Shares, Providers, and Recipients](/concepts/recipient-and-share-concepts.md) — The sharing model in Delta Sharing
- Cloud Token Sharing — Directory-based access mode for performance improvements

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
