---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fca60c4a0966145692b6cc3efe1155e86e9d1cbc8aff925c0a9cacd590ab7144
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pre-signed-url-sharing
    - PUS
    - Pre‑signed URL Sharing
    - Pre-signed URLs
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Pre-signed URL Sharing
description: A Delta Sharing mechanism that provides temporary read access via pre-signed URLs, logged as deltaSharingQueriedTable and deltaSharingQueriedTableChanges events
tags:
  - delta-sharing
  - data-access
  - security
timestamp: "2026-06-19T14:04:58.026Z"
---

# Pre-signed URL Sharing

**Pre-signed URL Sharing** is a data access mechanism used by [Delta Sharing](/concepts/delta-sharing.md) (OpenSharing) to provide temporary read access to shared assets such as tables, views, materialized views, streaming tables, and volumes. When a data recipient queries a share, the provider generates pre-signed URLs that grant short-lived, direct access to the underlying data files. This method contrasts with [STS token-based sharing](/concepts/sts-token-sharing.md), which uses scoped-down security tokens for credential-based access.

## Overview

In pre-signed URL sharing, the provider’s system creates time-limited URLs that the recipient can use to download data directly from cloud storage (for example, Amazon S3). This approach avoids the need for the recipient to have its own cloud credentials. Each pre-signed URL is tied to a specific object (such as a Parquet file) and expires after a short interval. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

Providers can monitor pre-signed URL sharing activity through audit logs. The audit log events that record pre-signed URL queries are `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`. These events are logged after the recipient’s query receives a response. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Auditing Pre-signed URL Shares

To view details about what was shared via pre-signed URLs, a provider examines the `response.result` field of the two logged events (`deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`). This field contains a JSON object with metadata about the query response. The following is an example of the `response.result` structure (this list is not exhaustive): ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

```json
{
  "checkpointBytes": "0",
  "earlyTermination": "false",
  "maxRemoveFiles": "0",
  "path": "file: example/s3/path/golden/snapshot-data0/_delta_log",
  "deltaSharingPartitionFilteringAccessed": "false",
  "deltaSharingRecipientId": "<redacted>",
  "deltaSharingRecipientIdHash": "<recipient-hash-id>",
  "jsonLogFileNum": "1",
  "scannedJsonLogActionNum": "5",
  "numRecords": "3",
  "deltaSharingRecipientMetastoreId": "<redacted>",
  "userAgent": "Delta-Sharing-Unity-Catalog-Databricks-Auth/1.0 ...",
  "jsonLogFileBytes": "2846",
  "checkpointFileNum": "0",
  "metastoreId": "<redacted>",
  "limitHint": "Some(1)",
  "tableName": "cookie_ingredients",
  "tableId": "1234567c-6d8b-45fd-9565-32e9fc23f8f3",
  "activeAddFiles": "2",
  "numAddFiles": "2",
  "numAddCDCFiles": "2",
  "numRemoveFiles": "2",
  "numSeenAddFiles": "3",
  "scannedAddFileSize": "1300",
  "scannedAddCDCFileSize": "1300",
  "scannedRemoveFileSize": "1300",
  "scannedCheckpointActionNum": "0",
  "tableVersion": "0"
}
```

The logged fields provide information such as the number of files returned (`numAddFiles`, `numRemoveFiles`), scanned file sizes, table identity (`tableName`, `tableId`), and query characteristics (e.g., `limitHint`). The recipient’s identity is recorded in a hashed form (`deltaSharingRecipientIdHash`) for privacy. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements for Audit Log Access

To access audit logs containing pre-signed URL events, an account admin must enable the [audit log system table](/concepts/audit-log-system-table-requirements.md) for the Databricks account. The logs are stored in `system.access.audit`. Alternatively, if an audit log delivery setup is configured, the logs are delivered to a specified bucket and path. If you are not an account admin or [Metastore](/concepts/metastore.md) admin, you must be granted access to `system.access.audit` to read the logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Logging

When a pre-signed URL sharing operation fails, the error is logged in the `response.error_message` field of the audit log. Common errors include `PERMISSION_DENIED`, `SHARE_DOES_NOT_EXIST`, and `TABLE_DOES_NOT_EXIST`. These error messages are common to all OpenSharing operations and are not specific to pre-signed URL sharing. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for data sharing.
- [OpenSharing](/concepts/opensharing.md) – Databricks’ implementation of Delta Sharing.
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) – The system table (`system.access.audit`) that stores audit logs.
- [STS Token Sharing](/concepts/sts-token-sharing.md) – Alternative credential-based sharing mechanism.
- Audit and Monitor Data Sharing – Overall guidance on monitoring data sharing activity.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
