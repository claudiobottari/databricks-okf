---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 242a6b1da7115ff7679eb009b83af8b3e01b7a87d493b1a19ca7360e4cb9cb69
  pageDirectory: concepts
  sources:
    - read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-limitations-and-constraints
    - Constraints and OpenSharing Limitations
    - OLAC
  citations:
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: OpenSharing Limitations and Constraints
description: A collection of known limitations across OpenSharing clients, including memory constraints, unsupported features for streaming tables and materialized views, column mapping/CDF limitations, and connector-specific restrictions.
tags:
  - limitations
  - delta-sharing
  - compatibility
timestamp: "2026-06-19T20:11:16.050Z"
---

# OpenSharing Limitations and Constraints

**OpenSharing Limitations and Constraints** covers the known restrictions that apply when reading data shared via the [OpenSharing](/concepts/opensharing.md) open protocol. These limitations vary by client (Spark, pandas, Power BI, Tableau, Iceberg clients) and by data asset type (streaming tables, materialized views). Providers and recipients should be aware of these constraints when designing data-sharing workflows.

## General Protocol Constraints

The OpenSharing protocol itself imposes a few structural limitations:

- **Iceberg REST Catalog**: When listing tables in a namespace, if the namespace contains more than 100 shared views, the response is limited to the first 100 views. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Iceberg Client Limitations (Snowflake, Trino, Flink, Spark, etc.)

These apply to any external client that reads OpenSharing data through the [Apache Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md):

- **Metadata staleness**: The metadata file does not automatically update with the latest snapshot. Clients must rely on auto-refresh or manual refreshes to see new data. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]
- **R2 storage not supported**: R2 (Cloudflare R2) is not supported as a storage backend. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]
- All Iceberg client limitations listed above apply cumulatively to each client integration. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Power BI OpenSharing Connector Limitations

When using the Power BI connector:

- The loaded data must fit entirely into the memory of the machine running Power BI Desktop.
- The connector enforces a configurable **Row Limit** (default 1 million rows) to control memory usage. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Tableau OpenSharing Connector Limitations

When using the Tableau connector:

- Data must fit into the memory of the machine running Tableau Desktop or Tableau Server. A configurable row limit is enforced to manage this.
- **All columns are returned as type `String`**, regardless of the source column’s type.
- **SQL Filters** work only if the OpenSharing server supports the `predicateHint` extension defined in the protocol.
- **Deletion vectors** are not supported.
- **Column mapping** is not supported. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## OpenSharing Python Connector Limitations

When using the `delta-sharing` Python connector (also used by pandas):

- Connector version 1.1.0 and later supports **snapshot** queries on tables with [Column Mapping](/concepts/delta-table-column-mapping.md), but **Change Data Feed (CDF) queries on tables with column mapping are not supported**.
- CDF queries with `use_delta_format=True` **fail if the schema changed** during the queried version range. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Apache Spark Structured Streaming Limitations

When reading shared tables via Apache Spark [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md):

- The `Trigger.availableNow` option is **not supported**.
- For tables with deletion vectors or column mapping enabled, you must set the additional option `responseFormat=delta` to perform CDF or streaming queries. Batch queries work automatically.
- Row tracking columns require the `responseFormat=delta` option and are only supported in the delta response format (dump connectors not supported). ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Streaming Table Limitations

For Streaming Tables shared via OpenSharing:

- Only the **current snapshot** can be read.
- The following operations are **not supported**:
  - Querying the table’s history data (versioned reads)
  - Querying the [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
  - Using the table as a source for Spark Structured Streaming ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Materialized View Limitations

For [Materialized Views](/concepts/materialized-views-in-databricks.md) shared via OpenSharing:

- Only the **current snapshot** can be read.
- Using the materialized view as a source for Spark Structured Streaming is **not supported**. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md)
- [Deletion Vectors](/concepts/deletion-vectors.md)
- [Column Mapping](/concepts/delta-table-column-mapping.md)
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- [OpenSharing Protocol](/concepts/opensharing-protocol.md)
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)

## Sources

- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
