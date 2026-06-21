---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 49bba711f844da4f249311837619a47f6024f5e2a7c4a4e1c393370e50e28420
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-audit-log-events
    - PALE
    - Data Provider Audit Log Events
    - Data provider audit events
    - Data Provider Audit Monitoring
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Provider Audit Log Events
description: Audit events recorded for data providers in OpenSharing, including query response details, error messages, and actions taken by recipients on shared data.
tags:
  - audit-logging
  - delta-sharing
  - data-providers
timestamp: "2026-06-19T22:09:32.296Z"
---

# Provider Audit Log Events

**Provider Audit Log Events** are a subset of [OpenSharing audit log events](/concepts/opensharing-audit-logs.md) that record actions taken by a data provider and actions taken by recipients on the provider's shared data in [Delta Sharing](/concepts/delta-sharing.md). These logs enable data providers to monitor how their shared data is being accessed and queried. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Overview

When system tables are enabled for a Databricks account, audit logs are stored in `system.access.audit`. For accounts with an alternative audit log delivery setup, logs are delivered to a configured bucket and path. To access these logs, an account admin must first enable the audit log system table. Users who are not account admins or [Metastore](/concepts/metastore.md) admins must be granted access to `system.access.audit`. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Query Events

Provider audit logs record two categories of events depending on the sharing mechanism used: pre-signed URL shares and STS-token-based shares. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Pre-Signed URL Shares

For pre-signed URL-based sharing, the events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` are logged after a data recipient's query receives a response. Providers can inspect the `response.result` field of these logs for detailed information about what was shared. The field may include values such as: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `numRecords` — Number of records returned
- `tableName` — Name of the table accessed
- `tableId` — Identifier of the table
- `numAddFiles` — Number of AddFiles returned in the query
- `scannedAddFileSize` — File size in bytes for AddFiles returned
- `activeAddFiles` — Number of active AddFiles returned
- `deltaSharingRecipientIdHash` — Hash identifier of the recipient
- `userAgent` — Client software making the request
- `tableVersion` — Version of the table accessed

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### STS-Token Shares

For STS-token-based sharing, the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` are logged after a data recipient's query receives a response. Providers can inspect the `request_params` column for details, which may include: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `recipient_name` — Name of the recipient
- `share_name` — Name of the share accessed
- `table_full_name` — Fully qualified table name
- `table_url` — Storage path of the table
- `operation` — Type of operation (e.g., `READ`)
- `credential_type` — Type of credential used (e.g., `StorageCredential`)
- `is_permissions_enforcing_client` — Whether the client enforces permissions
- `metastore_id` — Identifier of the [Metastore](/concepts/metastore.md)

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Error Events

When an OpenSharing action fails, the error is logged in the `response.error_message` field. Provider logs capture errors such as: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- **Feature not enabled**: `FEATURE_DISABLED:Delta Sharing is not enabled`
- **Catalog does not exist**: `CATALOG_DOES_NOT_EXIST:Catalog '<catalog>' does not exist.`
- **Permission denied**: `PERMISSION_DENIED:Only administrators can <operation-name> <operation-target>`
- **Invalid recipient or share name**: `INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare Missing required field: <recipient-name>/<share-name>`
- **Duplicate resource**: `RECIPIENT_ALREADY_EXISTS/SHARE_ALREADY_EXISTS: Recipient/Share <name> already exists` and `RESOURCE_ALREADY_EXISTS: Shared Table '<name>' already exists`
- **Rotating a recipient with two active tokens**: `INVALID_PARAMETER_VALUE: There are already two active tokens for recipient <recipient-name>`
- **Table not in Unity Catalog**: `INVALID_PARAMETER_VALUE: Only managed or external table on Unity Catalog can be added to a share`
- **Non-existent resource**: `RECIPIENT_DOES_NOT_EXIST/SHARE_DOES_NOT_EXIST`, `TABLE_DOES_NOT_EXIST`, or `SCHEMA_DOES_NOT_EXIST`

## Related Concepts

- Audit and Monitor Data Sharing
- [Delta Sharing](/concepts/delta-sharing.md)
- [Recipient Audit Log Events](/concepts/recipient-audit-log-events.md)
- OpenSharing Events
- [Unity Catalog](/concepts/unity-catalog.md)
- System Tables

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
