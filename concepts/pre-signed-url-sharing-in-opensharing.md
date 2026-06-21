---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 848e45514f89ae212c3a140e00514ce5e97f6ee92f32f40c889099c16502252c
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pre-signed-url-sharing-in-opensharing
    - PUSIO
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Pre-signed URL Sharing in OpenSharing
description: A credential mechanism for OpenSharing that provides temporary read access to shared data via pre-signed URLs, logged through deltaSharingQueriedTable and deltaSharingQueriedTableChanges events.
tags:
  - delta-sharing
  - credentials
  - pre-signed-urls
timestamp: "2026-06-18T14:28:50.443Z"
---

# Pre-signed URL Sharing in OpenSharing

**Pre-signed URL Sharing** is one of two methods used by [OpenSharing](/concepts/opensharing.md) to provide temporary read access to shared data. When a recipient queries a shared asset, the provider generates short-lived, pre-signed URLs that point to the underlying data files in cloud storage. The recipient’s query engine uses these URLs to read the data without requiring long-term credentials. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Overview

OpenSharing supports sharing a variety of asset types, including tables, views, materialized views, streaming tables, and volumes. For each query, temporary read access to the underlying data can be provided either through pre-signed URLs or through scoped-down STS tokens. The choice between the two mechanisms depends on the data source configuration and the access pattern. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

In a pre-signed URL–based share, the provider constructs a set of time-limited URLs that grant access to the physical files (for example, Parquet files in a [Delta Lake Table](/concepts/delta-lake-table.md)). The recipient’s client can then fetch the data directly from cloud storage using these URLs, which expire after a short window. This approach avoids the need to manage long-term credentials across organizations. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Audit Logging of Pre-signed URL Shares

For pre-signed URL–based sharing, the provider’s audit logs record two events after a data recipient’s query receives a response: `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

Providers can inspect the `response.result` field of these log entries to see detailed metadata about what was shared with the recipient. The field is a JSON object that may include (but is not limited to) the following values: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `checkpointBytes` – size of checkpoint data in bytes  
- `earlyTermination` – whether the query terminated early  
- `maxRemoveFiles` – maximum number of remove files  
- `path` – file path to the Delta log (for example, `file: example/s3/path/golden/snapshot-data0/_delta_log`)  
- `deltaSharingPartitionFilteringAccessed` – whether partition filtering was used  
- `deltaSharingRecipientId` – redacted recipient identifier  
- `deltaSharingRecipientIdHash` – hash of the recipient identifier  
- `jsonLogFileNum` – number of JSON log files scanned  
- `scannedJsonLogActionNum` – number of scanned JSON log actions  
- `numRecords` – number of records returned  
- `userAgent` – client user-agent string  
- `jsonLogFileBytes` – total bytes of JSON log files  
- `tableName` – name of the accessed table  
- `tableId` – UUID of the accessed table  
- `activeAddFiles` – number of AddFiles returned in the query  
- `numAddFiles` – number of AddFiles returned  
- `numAddCDCFiles` – number of AddFiles returned in a Change Data Feed query  
- `numRemoveFiles` – number of RemoveFiles returned  
- `numSeenAddFiles` – number of AddFiles seen during the scan  
- `scannedAddFileSize` – size in bytes of the returned AddFiles  
- `scannedAddCDCFileSize` – size in bytes of the returned CDC AddFiles  
- `scannedRemoveFileSize` – size in bytes of the returned RemoveFiles  
- `scannedCheckpointActionNum` – number of checkpoint actions scanned  
- `tableVersion` – version of the table at query time  

These fields allow providers to monitor which files and how many records are served to recipients, enabling usage tracking and auditing. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Comparison with STS-token Sharing

In contrast to pre-signed URL sharing, [STS Token Sharing in OpenSharing](/concepts/sts-token-sharing-in-opensharing.md) uses scoped-down temporary credentials (STS tokens) that give the recipient direct access to storage locations. The provider audit logs for STS‑token shares record different events: `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`. Both methods fulfill the same goal of temporary read access but differ in how the credential is delivered and how the access is logged. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – the overall framework for sharing data across Databricks workspaces  
- [STS Token Sharing in OpenSharing](/concepts/sts-token-sharing-in-opensharing.md) – the alternative temporary credential method  
- Audit logs for OpenSharing – how to monitor sharing activity with audit log system tables  
- [Delta Sharing](/concepts/delta-sharing.md) – the open protocol that OpenSharing is built on  

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
