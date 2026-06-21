---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe8ec6548a1ab05eae95f067049c3e50075ebafb07cb1d4938181b797c2ab185
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-audit-log-fields-for-pre-signed-url-queries
    - OALFFPUQ
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: OpenSharing Audit Log Fields for Pre-signed URL Queries
description: Provider audit logs for deltaSharingQueriedTable events contain fields like scannedAddFileSize, numRecords, tableVersion, limitHint, and userAgent to track what was shared.
tags:
  - databricks
  - audit-logging
  - delta-sharing
timestamp: "2026-06-19T17:37:01.747Z"
---

# OpenSharing Audit Log Fields for Pre-signed URL Queries

**OpenSharing Audit Log Fields for Pre-signed URL Queries** refers to the structured data written into the `response.result` field of provider audit logs when a data recipient performs a query that is served via pre-signed URLs. These fields give data providers visibility into what was shared, including file metadata, query hints, and recipient information.

## Overview

OpenSharing supports sharing asset types such as tables, views, materialized views, streaming tables, and volumes. For pre-signed URL‑based sharing, two audit log events are logged after a recipient’s query receives a response: `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`. The `response.result` field of these events contains a JSON object with detailed information about the query result. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

Providers can inspect these fields to monitor which files and versions were accessed, the size of the data returned, and the identity of the recipient (hashed). The list of fields below is representative but not exhaustive. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Common Fields in `response.result`

The following fields may appear in the `response.result` JSON for pre-signed URL queries:

| Field | Description |
|-------|-------------|
| `checkpointBytes` | Total bytes of checkpoint files involved in the query. |
| `earlyTermination` | Whether the query was terminated early (e.g., by a limit hint). |
| `maxRemoveFiles` | Maximum number of remove files considered. |
| `path` | File path to the `_delta_log` directory that was queried. |
| `deltaSharingPartitionFilteringAccessed` | Whether partition filtering was applied during the query. |
| `deltaSharingRecipientId` | Redacted recipient identifier. |
| `deltaSharingRecipientIdHash` | Hash of the recipient ID for non‑PII identification. |
| `jsonLogFileNum` | Number of JSON delta log files scanned. |
| `scannedJsonLogActionNum` | Number of actions (e.g., add, remove) scanned from JSON log files. |
| `numRecords` | Number of records returned in the query. |
| `deltaSharingRecipientMetastoreId` | Redacted [Metastore](/concepts/metastore.md) ID of the recipient. |
| `userAgent` | User‑agent string of the client that made the request. |
| `jsonLogFileBytes` | Total bytes of JSON delta log files scanned. |
| `checkpointFileNum` | Number of checkpoint files used. |
| `metastoreId` | [Metastore](/concepts/metastore.md) ID of the provider. |
| `limitHint` | Optional limit hint applied (e.g., `Some(1)`). |
| `tableName` | Name of the table being queried. |
| `tableId` | UUID of the table in Unity Catalog. |
| `activeAddFiles` | Number of `AddFile` entries that are active and were returned. |
| `numAddFiles` | Number of `AddFile` entries returned in the query. |
| `numAddCDCFiles` | Number of `AddCDCFile` entries returned in a CDF query. |
| `numRemoveFiles` | Number of `RemoveFile` entries returned. |
| `numSeenAddFiles` | Number of `AddFile` entries that were seen (including filtered ones). |
| `scannedAddFileSize` | File size (in bytes) for the `AddFile` entries returned. |
| `scannedAddCDCFileSize` | File size for `AddCDCFile` entries returned. |
| `scannedRemoveFileSize` | File size for `RemoveFile` entries returned. |
| `scannedCheckpointActionNum` | Number of actions scanned from checkpoint files. |
| `tableVersion` | Version of the table at the time of the query. |

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Comparison with STS‑Token Shares

For STS‑token‑based sharing, the audit log events are `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`, and the details are stored in the `request_params` column rather than `response.result`. Information such as recipient name, share name, table name, and storage credential are included. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Use Cases

- **Monitoring data access**: Track which tables and file sizes are being queried by recipients.
- **Billing and cost analysis**: Estimate the volume of data transferred based on `scannedAddFileSize` and related fields.
- **Troubleshooting**: Investigate unexpected query patterns or permissions issues using recipient hash and user‑agent fields.
- **Compliance auditing**: Verify that only authorized recipients access specific versions of shared data.

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The open protocol for Delta Sharing.
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) – The `system.access.audit` table where these logs are stored.
- [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) – Temporary read access via signed URLs.
- [STS Token Sharing](/concepts/sts-token-sharing.md) – Alternative sharing method using scoped‑down tokens.
- [Delta Sharing](/concepts/delta-sharing.md) – The cross‑platform data sharing protocol underlying OpenSharing.
- [Provider Audit Logs](/concepts/provider-audit-logs.md) – Logged events for actions taken by the data provider.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
