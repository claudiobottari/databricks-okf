---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 360c32ec0ee17349ec47cb72f30e23cc5fe77406597b0aa9447b43ea10e94657
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pre-signed-url-sharing-audit-events
    - PUSAE
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Pre-signed URL Sharing Audit Events
description: Audit events (deltaSharingQueriedTableChanges, deltaSharingQueriedTable) logged when data recipients query shared data via pre-signed URL-based sharing, with detailed response.result fields.
tags:
  - delta-sharing
  - pre-signed-url
  - audit-events
timestamp: "2026-06-19T09:04:39.403Z"
---

# Pre-signed URL Sharing Audit Events

**Pre-signed URL Sharing Audit Events** are audit log entries that record details about data shared via pre-signed URLs in [Delta Sharing](/concepts/delta-sharing.md) (OpenSharing). These events allow data providers to monitor what data recipients access when using pre-signed URL-based sharing, including file sizes, record counts, and table metadata.

## Overview

When a data recipient queries shared data using pre-signed URL-based sharing, the provider's audit logs record specific events that contain detailed information about the response. Providers can inspect these logs to understand what data was shared, how much data was scanned, and which tables were accessed. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

The following events are logged in provider audit logs after a data recipient's query receives a response for pre-signed URL-based sharing: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `deltaSharingQueriedTableChanges`
- `deltaSharingQueriedTable`

## Response Details

Providers can view the `response.result` field of these audit log events to see detailed information about what was shared with the recipient. The field can include the following values (this list is not exhaustive): ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

| Field | Description |
|-------|-------------|
| `activeAddFiles` | Number of AddFiles returned in the query |
| `checkpointBytes` | Size of checkpoint data in bytes |
| `checkpointFileNum` | Number of checkpoint files |
| `deltaSharingPartitionFilteringAccessed` | Whether partition filtering was used |
| `deltaSharingRecipientId` | Identifier of the recipient (redacted) |
| `deltaSharingRecipientIdHash` | Hashed recipient identifier |
| `deltaSharingRecipientMetastoreId` | Recipient's [Metastore](/concepts/metastore.md) ID (redacted) |
| `earlyTermination` | Whether the query terminated early |
| `jsonLogFileBytes` | Size of JSON log file in bytes |
| `jsonLogFileNum` | Number of JSON log files |
| `limitHint` | Optional limit hint applied to the query |
| `maxRemoveFiles` | Maximum number of remove files |
| `metastoreId` | Provider's [Metastore](/concepts/metastore.md) ID (redacted) |
| `numAddFiles` | Number of AddFiles returned |
| `numAddCDCFiles` | Number of AddFiles returned in CDF query |
| `numRecords` | Number of records returned |
| `numRemoveFiles` | Number of RemoveFiles returned |
| `numSeenAddFiles` | Number of AddFiles seen during scan |
| `path` | Path to the Delta log directory |
| `scannedAddFileSize` | File size in bytes for AddFiles returned |
| `scannedAddCDCFileSize` | File size in bytes for AddCDCFile returned in CDF query |
| `scannedCheckpointActionNum` | Number of checkpoint actions scanned |
| `scannedJsonLogActionNum` | Number of JSON log actions scanned |
| `scannedRemoveFileSize` | File size in bytes for RemoveFile returned |
| `tableId` | Unique identifier of the table |
| `tableName` | Name of the table accessed |
| `tableVersion` | Version of the table at query time |
| `userAgent` | Client software used by the recipient |

## Requirements

To access these audit logs, an account admin must enable the audit log system table for the Databricks account. The logs are stored in `system.access.audit`. Users who are not account admins or [Metastore](/concepts/metastore.md) admins must be granted access to `system.access.audit` to read the logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Comparison with STS-Token Shares

Pre-signed URL sharing differs from [STS Token Sharing Audit Events](/concepts/sts-token-sharing-audit-events.md) in how details are logged. For pre-signed URL shares, details are found in the `response.result` field of `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` events. For STS-token shares, details are found in the `request_params` column of `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` events. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing Audit Logs](/concepts/opensharing-audit-logs.md) — General overview of audit logging for data sharing
- OpenSharing Events — Complete list of OpenSharing audit log events
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — Reference for the `system.access.audit` table
- Data Provider Monitoring — Best practices for monitoring shared data access

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
