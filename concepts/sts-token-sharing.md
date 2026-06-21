---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0713ae63c9a62979ac427c66e3460da8e3bbfe4714373cdca3c32f2415fa2658
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sts-token-sharing
    - STS
    - STS token-based sharing
    - STS (Security Token Service)
    - STS-token
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: STS Token Sharing
description: A Delta Sharing mechanism using scoped-down AWS STS tokens for temporary read access, logged as generateTemporaryTableCredentials and generateTemporaryVolumeCredentials events
tags:
  - delta-sharing
  - data-access
  - aws-sts
  - security
timestamp: "2026-06-19T14:04:49.590Z"
---

# STS Token Sharing

**STS Token Sharing** is one of two methods that [OpenSharing](/concepts/opensharing.md) (Databricks’ Delta Sharing protocol) uses to provide data recipients with temporary read access to shared assets. Instead of returning a pre-signed URL, the provider generates scoped-down AWS Security Token Service (STS) credentials that grant the recipient temporary read access to the underlying data files. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Audit Logging of STS Token Shares

When a data recipient submits a query that uses STS‑token‑based sharing, the provider’s audit logs record the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`. These events capture detailed information about what was shared. The `request_params` column of the log entry contains fields such as the recipient name, share name, table full name, operation type, credential type, and the S3 path (table URL) of the data. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

The following fields (non‑exhaustive list) appear in the `request_params` of an STS token event:

| Field | Description |
|-------|-------------|
| `recipient_name`       | Name of the data recipient |
| `share_id`             | UUID of the share |
| `credential_type`      | `StorageCredential` |
| `is_permissions_enforcing_client` | Whether the client enforces permissions |
| `table_full_name`      | Fully qualified name of the shared table |
| `operation`            | `READ` |
| `share_name`           | Name of the share |
| `table_id`             | UUID of the shared table |
| `share_owner`          | Owner of the share |
| `table_url`            | S3 path to the underlying data |
| `metastore_id`         | UUID of the [Metastore](/concepts/metastore.md) |

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Comparison with Pre-signed URL Sharing

OpenSharing supports two temporary access mechanisms: [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) and STS token sharing. The choice of mechanism depends on the asset type and configuration. For pre-signed URL shares, the provider logs `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` events, and details appear in the `response.result` field. For STS token shares, the provider logs `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` events, with details in the `request_params` field. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Scope and Supported Assets

STS token sharing provides temporary read access to tables, views, materialized views, streaming tables, and volumes. The access is scoped down to the minimum set of permissions needed, and the credentials are generated on a per‑query basis. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – Databricks’ implementation of the Delta Sharing protocol.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for secure data sharing across platforms.
- [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) – The alternative temporary access method using pre‑signed cloud storage URLs.
- [Audit Logs for Data Sharing](/concepts/delta-sharing.md) – How to monitor sharing events using Databricks audit logs.
- [Unity Catalog](/concepts/unity-catalog.md) – The underlying [Metastore](/concepts/metastore.md) and governance system for shared assets.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
