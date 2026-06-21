---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 079c67a6c7aee340bdfe73e2e6049e1c31a4f4cd2dbf6d8dcec3adf9594a7fea
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-audit-logs
    - PAL
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Provider Audit Logs
description: Audit logs recording actions taken by the data provider and actions taken by recipients on the provider's shared data, including query result details and error messages.
tags:
  - delta-sharing
  - audit-logging
  - data-provider
timestamp: "2026-06-19T09:04:35.742Z"
---

```markdown
---
title: Provider Audit Logs
summary: Audit logs recorded for data providers capturing actions taken by the provider and actions taken by recipients on shared data.
sources:
  - audit-and-monitor-data-sharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:49:18.314Z"
updatedAt: "2026-06-18T10:49:18.314Z"
tags:
  - audit-logging
  - data-provider
  - databricks
aliases:
  - provider-audit-logs
  - PAL
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Provider Audit Logs

**Provider audit logs** record actions taken by the data provider and actions taken by recipients on the provider's shared data in [[Delta Sharing]] (OpenSharing) environments. These logs enable data providers to monitor how recipients are accessing shared assets and to troubleshoot access issues. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access provider audit logs, an account admin must enable the audit log system table for the Databricks account. See Enable System Tables. If you are not an account admin or [[Metastore Admin Role|metastore admin]], you must be granted access to `system.access.audit` to read the logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Viewing OpenSharing Events

When system tables are enabled, audit logs are stored in the `system.access.audit` table. You can query this table directly using SQL. Alternatively, if your account uses an audit log delivery setup, you must know the bucket and path where logs are delivered. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

For a complete list of OpenSharing audit log events, see the [OpenSharing events reference](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs#ds). ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

OpenSharing supports sharing the following asset types: tables, views, materialized views, streaming tables, and volumes. Access is provided via temporary read credentials using either **pre-signed URLs** or **scoped-down STS tokens**. The logged audit events differ based on the sharing type. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Pre-signed URL Shares

In provider logs, the events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` are logged after a recipient's query receives a response. Providers can examine the `response.result` field to see details about what was shared. The field can include values such as:

- `checkpointBytes`
- `earlyTermination`
- `maxRemoveFiles`
- `path` (e.g., the Delta log path)
- `deltaSharingPartitionFilteringAccessed`
- `deltaSharingRecipientId` (redacted)
- `deltaSharingRecipientIdHash`
- `jsonLogFileNum`, `scannedJsonLogActionNum`
- `numRecords`
- `deltaSharingRecipientMetastoreId` (redacted)
- `userAgent`
- `jsonLogFileBytes`, `checkpointFileNum`
- `metastoreId` (redacted)
- `limitHint`
- `tableName`, `tableId`
- `activeAddFiles`, `numAddFiles`, `numAddCDCFiles`, `numRemoveFiles`, `numSeenAddFiles`
- `scannedAddFileSize`, `scannedAddCDCFileSize`, `scannedRemoveFileSize`
- `scannedCheckpointActionNum`
- `tableVersion`

This list is not exhaustive. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### STS-Token Shares

For STS-token-based sharing, the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` are logged. Providers can view the `request_params` column, which may include:

- `recipient_name`
- `share_id`
- `credential_type` (e.g., `StorageCredential`)
- `is_permissions_enforcing_client`
- `table_full_name`
- `operation` (e.g., `READ`)
- `share_name`
- `table_id`
- `share_owner`
- `recipient_id`
- `table_url`
- `metastore_id`

This list is also not exhaustive. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Errors

If an OpenSharing action fails, the error message is recorded in the `response.error_message` field of the audit log. The following errors are logged specifically for data providers:

| Error | Description |
|---|---|
| `FEATURE_DISABLED:Delta Sharing is not enabled` | OpenSharing is not enabled on the selected [[metastore|Metastore]]. |
| `CATALOG_DOES_NOT_EXIST:Catalog '<catalog>' does not exist.` | Operation attempted on a non-existent catalog. |
| `PERMISSION_DENIED:Only administrators can <operation-name> <operation-target>` | Non-admin attempted a privileged operation. |
| `INVALID_STATE:Workspace <workspace-name> is no longer assigned to this metastore` | Operation on a workspace not assigned to the [[metastore|Metastore]]. |
| `INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare Missing required field: ...` | Missing recipient or share name in a request. |
| `INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare <name> is not a valid name` | Invalid recipient or share name. |
| `INVALID_PARAMETER_VALUE: Only managed or external table on Unity Catalog can be added to a share` | Attempt to share a table not in a Unity Catalog [[metastore|Metastore]]. |
| `INVALID_PARAMETER_VALUE: There are already two active tokens for recipient <name>` | Recipient already in rotated state with two active tokens. |
| `RECIPIENT_ALREADY_EXISTS/SHARE_ALREADY_EXISTS: Recipient/Share <name> already exists` | Duplicate recipient or share name. |
| `RECIPIENT_DOES_NOT_EXIST/SHARE_DOES_NOT_EXIST: Recipient/Share '<name>' does not exist` | Operation on a non-existent recipient or share. |
| `RESOURCE_ALREADY_EXISTS: Shared Table '<name>' already exists` | Table already added to the share. |
| `TABLE_DOES_NOT_EXIST: Table '<name>' does not exist` | Referenced table does not exist. |
| `SCHEMA_DOES_NOT_EXIST: Schema '<name>' does not exist` | Referenced schema does not exist. |
| `SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` | Recipient attempted to access a non-existent share. |

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [[Delta Sharing]] — The open protocol for sharing data across platforms
- [[Unity Catalog]] — The governance layer that manages Delta Sharing providers and recipients
- System Tables — Built-in tables that store account-level audit and usage data
- [[Audit Log System Table Requirements|Audit Log System Table]] — Reference for the `system.access.audit` schema
- [[Recipient Audit Logs]] — Logs recorded from the recipient’s perspective

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md
```

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
