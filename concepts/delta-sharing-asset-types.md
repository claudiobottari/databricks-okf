---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57914fae5b5cca9ef8a7bddd7bd8a8e22787833779a258b5b6ecdcf4feba053d
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-sharing-asset-types
    - DSAT
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Delta Sharing Asset Types
description: Types of assets that can be shared via OpenSharing including tables, views, materialized views, streaming tables, and volumes
tags:
  - delta-sharing
  - data-assets
  - unity-catalog
timestamp: "2026-06-19T14:05:54.181Z"
---

# Delta Sharing Asset Types

**Delta Sharing Asset Types** refers to the categories of data objects that can be shared between data providers and recipients using the [OpenSharing](/concepts/opensharing.md) protocol (the Databricks implementation of [Delta Sharing](/concepts/delta-sharing.md)). OpenSharing supports sharing several types of assets, each with specific characteristics and access patterns.

## Supported Asset Types

OpenSharing supports sharing the following asset types: tables, views, materialized views, streaming tables, and volumes. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Tables

Standard Delta tables can be shared with recipients. OpenSharing provides temporary read access to the underlying data. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Views

Views, including logical views defined over underlying tables, are supported as shareable assets. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Materialized Views

Materialized views, which store precomputed results, can be shared through OpenSharing. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Streaming Tables

Streaming tables that capture incremental data changes are supported as shareable asset types. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Volumes

Non-tabular data stored in Unity Catalog volumes can also be shared using OpenSharing. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Access Mechanisms

OpenSharing provides temporary read access to the underlying data through two mechanisms: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Pre-signed URLs

For pre-signed URL-based sharing, the provider's audit logs record events such as `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` after a recipient's query receives a response. Providers can inspect the `response.result` field to view details about what was shared, including the number of AddFiles, RemoveFiles, scanned file sizes, table version, and other metadata. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### STS Tokens

For STS-token-based sharing, the provider's audit logs record events such as `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`. Providers can view the `request_params` column to see details including the recipient name, share name, table name, credential type, and operation. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Audit Log Events by Asset Type

The following table outlines how the sharing type corresponds to the logged audit log events: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

| Sharing Mechanism | Audit Log Events | Relevant Fields |
|-------------------|------------------|-----------------|
| Pre-signed URLs | `deltaSharingQueriedTableChanges`, `deltaSharingQueriedTable` | `response.result` |
| STS Tokens | `generateTemporaryTableCredentials`, `generateTemporaryVolumeCredentials` | `request_params` |

## Limitations

Only managed tables or external tables on [Unity Catalog](/concepts/unity-catalog.md) can be added to a share. If a user attempts to share a table that is not in a Unity Catalog [Metastore](/concepts/metastore.md), the operation fails with an `INVALID_PARAMETER_VALUE` error. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The Databricks protocol implementing Delta Sharing
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer for Databricks
- [Audit Logs for Data Sharing](/concepts/delta-sharing.md) — Monitoring shared data access
- [Delta Sharing Recipients](/concepts/delta-sharing-recipient-object.md) — Entities that receive shared data
- [Delta Sharing Providers](/concepts/delta-sharing.md) — Entities that share data

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
