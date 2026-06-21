---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f16f6b2b0903fc75744ddb823f5d525928507925b6ca513019157e67d7ad7c33
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sts-token-sharing-in-opensharing
    - STSIO
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: STS Token Sharing in OpenSharing
description: A credential mechanism for OpenSharing that uses scoped-down STS tokens for temporary data access, logged through generateTemporaryTableCredentials and generateTemporaryVolumeCredentials events.
tags:
  - delta-sharing
  - credentials
  - sts-tokens
timestamp: "2026-06-18T14:28:47.744Z"
---

# STS Token Sharing in OpenSharing

**STS Token Sharing** is one of two mechanisms OpenSharing uses to provide temporary read access to shared data. Instead of issuing pre-signed URLs, the provider issues scoped-down AWS Security Token Service (STS) credentials that grant the recipient direct read access to the underlying cloud storage. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Overview

OpenSharing supports sharing asset types such as tables, views, materialized views, streaming tables, and volumes. For each query, the recipient can be given access via either [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) or scoped-down STS tokens. The choice affects which audit log events are emitted. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

When a data recipient’s query is answered using STS‑token sharing, the provider’s audit log records the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

Providers can inspect the `request_params` column of these log entries to see the details of what was shared. The field may include the following values (the list is not exhaustive): ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

| Field | Description |
|---|---|
| `recipient_name` | Name of the recipient |
| `share_id` | Unique identifier of the share |
| `share_name` | Name of the share |
| `credential_type` | Always `StorageCredential` for STS token sharing |
| `is_permissions_enforcing_client` | Whether the client enforces permissions |
| `table_full_name` | Fully qualified name of the table |
| `table_id` | Unique identifier of the table |
| `table_url` | Cloud storage URL (e.g., `s3://somePath`) |
| `operation` | The operation performed (e.g., `READ`) |
| `share_owner` | Owner of the share |
| `recipient_id` | Unique identifier of the recipient |
| `metastore_id` | Unique identifier of the [Metastore](/concepts/metastore.md) |

These fields help providers audit exactly which storage paths, tables, and recipients are involved in each STS‑backed access. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Comparison with Pre-Signed URL Sharing

STS Token Sharing and [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) are the two temporary read‑access methods in OpenSharing. The audit log entries differ: pre‑signed URL requests log `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`, while STS token requests log the `generateTemporary*Credentials` events described above. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- [Audit log system table](/concepts/audit-log-system-table-requirements.md) – Where OpenSharing events are logged
- [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) – The alternative temporary access method
- [Unity Catalog](/concepts/unity-catalog.md) – Underlying [Metastore](/concepts/metastore.md) for OpenSharing

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
