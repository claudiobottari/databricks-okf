---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d07f4ed5e8096f0a9baf36e59b2b849bcf2285b364f48a6bc23ada039c5120a
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foreign-iceberg-table-sharing
    - FITS
    - Foreign Iceberg Table
    - Foreign Iceberg Tables
    - Foreign Iceberg tables
    - Foreign Iceberg Table|foreign Iceberg tables
    - Foreign catalog|Foreign
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Foreign Iceberg Table Sharing
description: Sharing Iceberg tables federated from foreign Iceberg catalogs via Lakehouse Federation, supporting both Databricks-to-Databricks and open Iceberg client recipients.
tags:
  - delta-sharing
  - iceberg
  - lakehouse-federation
timestamp: "2026-06-19T09:38:15.401Z"
---

---
title: Foreign Iceberg Table Sharing
summary: Sharing Iceberg tables federated from external Iceberg catalogs, requiring Delta Uniform and enabling sharing to external Iceberg clients.
sources:
  - create-shares-for-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:55:44.150Z"
updatedAt: "2026-06-18T14:55:44.150Z"
tags:
  - delta-sharing
  - iceberg
  - federation
aliases:
  - foreign-iceberg-table-sharing
  - FITS
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Foreign Iceberg Table Sharing

**Foreign Iceberg Table Sharing** refers to the ability to share Iceberg tables that have been federated from external Iceberg catalogs via [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) using [OpenSharing](/concepts/opensharing.md). This capability allows providers to make data stored in remote Iceberg sources available to recipients without copying the data into Databricks. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Foreign Iceberg tables are Unity Catalog tables that reference data managed by an external Iceberg catalog. When added to an [OpenSharing](/concepts/opensharing.md) share, the data is served to recipients on demand. The tables are always shared with full history. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

To share a foreign Iceberg table, the following must be in place:

- The **Lakehouse Federation Sharing** preview must be enabled at the account level. ^[create-shares-for-opensharing-databricks-on-aws.md]
- If the share recipients are open recipients who are **not using Iceberg clients**, the provider must configure [default storage](/concepts/workspace-default-storage-path.md) and enable the **OpenSharing for Default Storage – Expanded Access** preview at the account level. ^[create-shares-for-opensharing-databricks-on-aws.md]
- The foreign Iceberg table must have **Delta Uniform** enabled. If Uniform is not enabled, the table cannot be added to a share. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When sharing with open recipients who are not using Iceberg clients, the shared data is first filtered and materialized using the provider's compute and storage, which may incur additional costs. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

- **Partition filters** are not supported when sharing foreign Iceberg tables. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When sharing with open recipients who are **not using an Iceberg client**, `LIMIT` clauses and predicate pushdown are not supported. The system fully materializes all query results before returning them to the recipient, regardless of query filters. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Adding a Foreign Iceberg Table to a Share

Foreign Iceberg tables can be added to a share using Catalog Explorer, SQL, or the Databricks Unity Catalog CLI. The general workflow is:

1. Create a share if one does not already exist.
2. In the share's **Edit assets** page, browse or search for the foreign Iceberg table and select it.
3. Optionally, provide an **alias** — an alternate table name that recipients must use in queries. Recipients cannot use the actual table name if an alias is specified.
4. Save the share. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Sharing with External Iceberg Clients

In addition to standard OpenSharing recipients, foreign Iceberg tables can also be shared to recipients using external Iceberg clients. For details, see Enable sharing to external Iceberg clients. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Keeping Data Fresh

Because foreign Iceberg tables present data from an external source, the metadata on Databricks can become stale. Any `SELECT` query or `REFRESH TABLE` command refreshes the table metadata. Databricks recommends scheduling a recurring job (for example, using a Databricks SQL query schedule) to keep the table in sync with the remote Iceberg source. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The protocol for sharing data assets between Databricks workspaces and external recipients.
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) — The mechanism for querying external data sources without copying data.
- Managed Iceberg Tables — Native Unity Catalog Iceberg tables that can also be shared.
- [Delta Uniform](/concepts/delta-uniform.md) — The feature that enables Iceberg compatibility for Delta tables, required for foreign Iceberg table sharing.
- Foreign Schemas and Tables — More generally, sharing schemas or tables federated from external systems.
- [Default Storage](/concepts/workspace-default-storage-path.md) — Storage used for materialization during sharing workflows.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
