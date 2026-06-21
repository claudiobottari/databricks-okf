---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22728f067e0347590dbbf5449710811b19d09782171cfc7b6f13366e3e7f5d32
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pre-signed-url-sharing-audit-details
    - PUSAD
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Pre-signed URL Sharing Audit Details
description: Audit log fields for pre-signed URL-based sharing, including deltaSharingQueriedTableChanges and deltaSharingQueriedTable events with detailed metadata about shared files.
tags:
  - audit-logging
  - delta-sharing
  - pre-signed-urls
  - data-access
timestamp: "2026-06-19T22:09:04.597Z"
---

# Pre-signed URL Sharing Audit Details

**Pre-signed URL Sharing Audit Details** refers to the specific information captured in provider‑side audit logs when a data recipient accesses shared data via pre‑signed URL‑based sharing in [OpenSharing](/concepts/opensharing.md). Providers can inspect the `response.result` field of logged events to obtain detailed metadata about what was shared with each recipient, including file counts, sizes, and table versioning information.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access these audit details, an account admin must first enable the audit log system table for the Databricks account. The audit logs are stored in `system.access.audit`. Users who are not account admins or [Metastore](/concepts/metastore.md) admins must be granted access to `system.access.audit` to read the logs. Alternatively, if an account has an audit log delivery setup configured, the logs are delivered to a designated bucket and path.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Triggering Events

In the provider logs, the events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` are logged after a data recipient’s query receives a response for pre‑signed URL‑based sharing. These events contain the `response.result` field that providers can examine.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Response Result Fields

The `response.result` field can include the following values (this list is not exhaustive):

| Field | Description |
|---|---|
| `checkpointBytes` | Size of checkpoint data in bytes |
| `earlyTermination` | Whether the query terminated early (`true`/`false`) |
| `maxRemoveFiles` | Maximum number of remove files |
| `path` | File path of the Delta log directory |
| `deltaSharingPartitionFilteringAccessed` | Whether partition filtering was used |
| `deltaSharingRecipientId` | Redacted recipient identifier |
| `deltaSharingRecipientIdHash` | Hash of the recipient identifier |
| `jsonLogFileNum` | Number of JSON log files scanned |
| `scannedJsonLogActionNum` | Number of JSON log actions scanned |
| `numRecords` | Number of records returned |
| `deltaSharingRecipientMetastoreId` | Redacted recipient [Metastore](/concepts/metastore.md) identifier |
| `userAgent` | Client user agent string |
| `jsonLogFileBytes` | Size of scanned JSON log files in bytes |
| `checkpointFileNum` | Number of checkpoint files scanned |
| `metastoreId` | Redacted [Metastore](/concepts/metastore.md) identifier |
| `limitHint` | Optional query limit hint |
| `tableName` | Name of the table queried |
| `tableId` | UUID of the table |
| `activeAddFiles` | Number of AddFiles returned in the query |
| `numAddFiles` | Number of AddFiles returned in the query |
| `numAddCDCFiles` | Number of AddFiles returned in a CDF query |
| `numRemoveFiles` | Number of RemoveFiles returned in the query |
| `numSeenAddFiles` | Total number of AddFiles seen during query |
| `scannedAddFileSize` | File size in bytes for AddFiles returned |
| `scannedAddCDCFileSize` | File size in bytes for AddCDCFile in CDF query |
| `scannedRemoveFileSize` | File size in bytes for RemoveFiles returned |
| `scannedCheckpointActionNum` | Number of checkpoint actions scanned |
| `tableVersion` | Version of the table at query time |

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Key Differences from STS Token Sharing

Pre‑signed URL sharing and [STS Token Sharing](/concepts/sts-token-sharing.md) produce different audit log events and fields:

- **Pre‑signed URL sharing**: Logged under events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`, with details in the `response.result` field.
- **STS token sharing**: Logged under events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`, with details in the `request_params` field.

This means providers must check different event types and fields depending on the sharing method used.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Supported Asset Types

OpenSharing supports sharing multiple asset types via pre‑signed URLs, including tables, views, materialized views, streaming tables, and volumes. All provide temporary read access to the underlying data.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Logging

If an attempted OpenSharing action fails, the error is logged in the `response.error_message` field. This applies to both pre‑signed URL and STS token sharing. Common error messages include permission denied errors, non‑existent share errors, and table not found errors.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing framework that uses pre‑signed URLs
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — The `system.access.audit` table storing audit events
- [STS Token Sharing](/concepts/sts-token-sharing.md) — Alternative sharing method with different audit event types
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for sharing data across platforms
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer managing metastores and permissions

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
