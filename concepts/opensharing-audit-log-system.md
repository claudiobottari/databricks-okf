---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3904c5e006a5d685c7a95a6631d977bad4508dfe88397c1261d3867289c7dbb
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-audit-log-system
    - OALS
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: OpenSharing Audit Log System
description: The system for auditing and monitoring data sharing events in Databricks Delta Sharing, capturing provider and recipient actions via system tables or audit log delivery.
tags:
  - audit-logging
  - delta-sharing
  - databricks
  - data-governance
timestamp: "2026-06-19T22:10:44.618Z"
---

# OpenSharing Audit Log System

The **OpenSharing Audit Log System** records events related to data sharing between providers and recipients in Databricks Delta Sharing. It enables both data providers and recipients to monitor actions taken on shared data, including queries, credential generation, and management operations. Provider audit logs record actions taken by the provider and actions taken by recipients on the provider's shared data. Recipient audit logs record events related to the accessing of shares and the management of provider objects. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access OpenSharing audit logs, an account admin must enable the audit log system table for the Databricks account. Audit logs are stored in `system.access.audit` when system tables are enabled. Alternatively, if the account has an audit log delivery setup, logs are delivered to a configured bucket and path. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

Users who are not account admins or [Metastore](/concepts/metastore.md) admins must be granted access to `system.access.audit` to read audit logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

OpenSharing supports sharing asset types including tables, views, materialized views, streaming tables, and volumes. The sharing type determines how audit log events are recorded. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Pre-signed URL Shares

For pre-signed URL-based sharing, the provider logs record the events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` after a data recipient's query receives a response. Providers can examine the `response.result` field of these logs to see details about what was shared. The field may include values such as: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `checkpointBytes` — Size of checkpoint data in bytes
- `earlyTermination` — Whether the query terminated early
- `maxRemoveFiles` — Maximum number of remove files
- `path` — File path to the Delta log
- `deltaSharingPartitionFilteringAccessed` — Whether partition filtering was used
- `deltaSharingRecipientId` — Recipient identifier (redacted)
- `deltaSharingRecipientIdHash` — Hashed recipient identifier
- `jsonLogFileNum` — Number of JSON log files
- `scannedJsonLogActionNum` — Number of scanned JSON log actions
- `numRecords` — Number of records returned
- `deltaSharingRecipientMetastoreId` — Recipient [Metastore](/concepts/metastore.md) identifier (redacted)
- `userAgent` — Client user agent string
- `jsonLogFileBytes` — Size of JSON log files in bytes
- `checkpointFileNum` — Number of checkpoint files
- `metastoreId` — [Metastore](/concepts/metastore.md) identifier (redacted)
- `limitHint` — Optional limit hint
- `tableName` — Name of the queried table
- `tableId` — Unique table identifier
- `activeAddFiles` — Number of AddFiles returned in the query
- `numAddFiles` — Number of AddFiles returned in the query
- `numAddCDCFiles` — Number of AddFiles returned in a CDF query
- `numRemoveFiles` — Number of RemoveFiles returned in the query
- `numSeenAddFiles` — Number of AddFiles seen
- `scannedAddFileSize` — File size in bytes for AddFiles returned
- `scannedAddCDCFileSize` — File size in bytes for AddCDCFile returned in CDF query
- `scannedRemoveFileSize` — File size in bytes for RemoveFiles returned
- `scannedCheckpointActionNum` — Number of scanned checkpoint actions
- `tableVersion` — Version of the table queried

### STS-token Shares

For STS-token-based sharing, the provider logs record the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` after a data recipient's query receives a response. Providers can examine the `request_params` column of these logs to see details about what was shared. The field may include values such as: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `recipient_name` — Name of the recipient
- `share_id` — Unique share identifier
- `credential_type` — Type of credential (e.g., `StorageCredential`)
- `is_permissions_enforcing_client` — Whether the client enforces permissions
- `table_full_name` — Full name of the table
- `operation` — Operation performed (e.g., `READ`)
- `share_name` — Name of the share
- `table_id` — Unique table identifier
- `share_owner` — Owner of the share
- `recipient_id` — Unique recipient identifier
- `table_url` — URL to the table's storage location
- `metastore_id` — [Metastore](/concepts/metastore.md) identifier

## Logged Errors

If an attempted OpenSharing action fails, the action is logged with the error message in the `response.error_message` field of the log. Items between `<` and `>` characters represent placeholder text. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Error Messages in Provider Logs

OpenSharing logs the following errors for data providers: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `FEATURE_DISABLED:Delta Sharing is not enabled` — OpenSharing is not enabled on the selected [Metastore](/concepts/metastore.md).
- `CATALOG_DOES_NOT_EXIST:Catalog '<catalog>' does not exist.` — An operation was attempted on a catalog that does not exist.
- `PERMISSION_DENIED:Only administrators can <operation-name> <operation-target>` — A non-admin user attempted a privileged operation.
- `INVALID_STATE:Workspace <workspace-name> is no longer assigned to this metastore` — An operation was attempted from a workspace not assigned to the [Metastore](/concepts/metastore.md).
- `INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare Missing required field: <recipient-name>/<share-name>` — A request was missing the recipient name or share name.
- `INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare <recipient-name>/<share-name> is not a valid name` — An invalid recipient or share name was provided.
- `INVALID_PARAMETER_VALUE: Only managed or external table on Unity Catalog can be added to a share` — An attempt was made to share a table not in Unity Catalog.
- `INVALID_PARAMETER_VALUE: There are already two active tokens for recipient <recipient-name>` — A user attempted to rotate a recipient that was already in a rotated state with two active tokens.
- `RECIPIENT_ALREADY_EXISTS/SHARE_ALREADY_EXISTS: Recipient/Share <name> already exists` — An attempt was made to create a duplicate recipient or share.
- `RECIPIENT_DOES_NOT_EXIST/SHARE_DOES_NOT_EXIST: Recipient/Share '<name>' does not exist` — An operation referenced a non-existent recipient or share.
- `RESOURCE_ALREADY_EXISTS: Shared Table '<name>' already exists` — An attempt was made to add a table already in the share.
- `TABLE_DOES_NOT_EXIST: Table '<name>' does not exist` — An operation referenced a non-existent table.
- `SCHEMA_DOES_NOT_EXIST: Schema '<name>' does not exist` — An operation referenced a non-existent schema.
- `SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` — An attempt was made to access a non-existent share.

### Error Messages in Recipient Logs

OpenSharing logs the following errors for data recipients: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `PERMISSION_DENIED:User does not have SELECT on Share <share-name>` — The user attempted to access a share without proper permissions.
- `SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` — The user attempted to access a non-existent share.
- `TABLE_DOES_NOT_EXIST: <table-name> does not exist` — The user attempted to access a table that does not exist in the share.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing across platforms
- [OpenSharing](/concepts/opensharing.md) — The Databricks implementation of the Delta Sharing protocol
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages access control for OpenSharing
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — The system table (`system.access.audit`) that stores audit log events
- [Metastore Admin](/concepts/metastore-admin-role.md) — Role with privileges to manage metastore-level settings and grant audit log access
- [Account Admin](/concepts/account-admin-unity-catalog.md) — Role responsible for enabling system tables and audit log delivery
- [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) — Sharing method using temporary URLs for data access
- [STS Token Sharing](/concepts/sts-token-sharing.md) — Sharing method using scoped-down security tokens for data access

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
