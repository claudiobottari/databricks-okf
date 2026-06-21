---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e0c02d5908b9dc5213599a4f74afa82d1741ce85013c6988b623616fec54aa20
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-error-handling
    - OEH
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: OpenSharing Error Handling
description: Categorized error messages and error codes (e.g., PERMISSION_DENIED, SHARE_DOES_NOT_EXIST, TABLE_DOES_NOT_EXIST) logged for failed OpenSharing actions on both provider and recipient sides.
tags:
  - error-handling
  - delta-sharing
  - troubleshooting
timestamp: "2026-06-18T14:29:14.645Z"
---

# OpenSharing Error Handling

**OpenSharing Error Handling** refers to the mechanisms by which [OpenSharing](/concepts/opensharing.md) (the [Delta Sharing](/concepts/delta-sharing.md) protocol) logs and reports errors that occur during data sharing operations between providers and recipients. When an attempted OpenSharing action fails, the action is logged with the error message in the `response.error_message` field of the audit log. Items between `<` and `>` characters in error messages represent placeholder text. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Messages in Provider Logs

OpenSharing logs the following errors for data providers: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

| Error Type | Error Message | Description |
|------------|---------------|-------------|
| `FEATURE_DISABLED` | `Delta Sharing is not enabled` | OpenSharing is not enabled on the selected [Metastore](/concepts/metastore.md) |
| `CATALOG_DOES_NOT_EXIST` | `Catalog '<catalog>' does not exist.` | An operation was attempted on a catalog that does not exist |
| `PERMISSION_DENIED` | `Only administrators can <operation-name> <operation-target>` | A non-admin user attempted a privileged operation |
| `INVALID_STATE` | `Workspace <workspace-name> is no longer assigned to this metastore` | An operation was attempted on a [Metastore](/concepts/metastore.md) from a workspace to which the [Metastore](/concepts/metastore.md) is not assigned |
| `INVALID_PARAMETER_VALUE` | `CreateRecipient/CreateShare Missing required field: <recipient-name>/<share-name>` | A request was missing the recipient name or share name |
| `INVALID_PARAMETER_VALUE` | `CreateRecipient/CreateShare <recipient-name>/<share-name> is not a valid name` | An invalid recipient or share name was provided |
| `INVALID_PARAMETER_VALUE` | `Only managed or external table on Unity Catalog can be added to a share` | A user attempted to share a table not in a Unity Catalog [Metastore](/concepts/metastore.md) |
| `INVALID_PARAMETER_VALUE` | `There are already two active tokens for recipient <recipient-name>` | A user attempted to rotate a recipient with two active tokens |
| `RECIPIENT_ALREADY_EXISTS` / `SHARE_ALREADY_EXISTS` | `Recipient/Share <name> already exists` | A user attempted to create a recipient or share with an existing name |
| `RECIPIENT_DOES_NOT_EXIST` / `SHARE_DOES_NOT_EXIST` | `Recipient/Share '<name>' does not exist` | An operation was attempted on a non-existent recipient or share |
| `RESOURCE_ALREADY_EXISTS` | `Shared Table '<name>' already exists` | A table was already added to a share |
| `TABLE_DOES_NOT_EXIST` | `Table '<name>' does not exist` | A referenced table does not exist |
| `SCHEMA_DOES_NOT_EXIST` | `Schema '<name>' does not exist` | A referenced schema does not exist |
| `SHARE_DOES_NOT_EXIST` | `Share <share-name> does not exist.` | A user attempted to access a non-existent share |

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Messages in Recipient Logs

OpenSharing logs the following errors for data recipients: ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

| Error Type | Error Message | Description |
|------------|---------------|-------------|
| `PERMISSION_DENIED` | `User does not have SELECT on Share <share-name>` | The user lacks SELECT permission on the share |
| `SHARE_DOES_NOT_EXIST` | `Share <share-name> does not exist.` | The share does not exist |
| `TABLE_DOES_NOT_EXIST` | `<table-name> does not exist.` | The table does not exist in the share |

## Viewing Error Details in Audit Logs

### Pre-Signed URL Shares

In the provider logs, the events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` are logged after a data recipient's query gets a response for pre-signed URL-based sharing. Providers can view the `response.result` field to see details about what was shared. The field can include values such as `checkpointBytes`, `earlyTermination`, `maxRemoveFiles`, `path`, `deltaSharingPartitionFilteringAccessed`, `deltaSharingRecipientId`, `deltaSharingRecipientIdHash`, `jsonLogFileNum`, `scannedJsonLogActionNum`, `numRecords`, `deltaSharingRecipientMetastoreId`, `userAgent`, `jsonLogFileBytes`, `checkpointFileNum`, `metastoreId`, `limitHint`, `tableName`, `tableId`, `activeAddFiles`, `numAddFiles`, `numAddCDCFiles`, `numRemoveFiles`, `numSeenAddFiles`, `scannedAddFileSize`, `scannedAddCDCFileSize`, `scannedRemoveFileSize`, `scannedCheckpointActionNum`, and `tableVersion`. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### STS-Token Shares

In the provider logs, the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` are logged after a data recipient's query gets a response for STS-token-based sharing. Providers can view the `request_params` column to see details, which can include `recipient_name`, `share_id`, `credential_type`, `is_permissions_enforcing_client`, `table_full_name`, `operation`, `share_name`, `table_id`, `share_owner`, `recipient_id`, `table_url`, and `metastore_id`. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements for Accessing Audit Logs

To access audit logs, an account admin must enable the [audit log system table](/concepts/audit-log-system-table-requirements.md) for your Databricks account. See Enable system tables. For information on the audit log system table, see Audit log system table reference. If you are not an account admin or [Metastore](/concepts/metastore.md) admin, you must be given access to `system.access.audit` to read audit logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

If your account has system tables enabled, audit logs are stored in `system.access.audit`. If your account has an audit log delivery setup, you need to know the bucket and path where the logs are delivered. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for data sharing
- [OpenSharing](/concepts/opensharing.md) — The implementation of the Delta Sharing protocol
- [Audit Logging](/concepts/abac-policy-audit-logging.md) — The system for recording data sharing events
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance system for managing shares
- [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) — A sharing mechanism for temporary read access
- [STS Token Sharing](/concepts/sts-token-sharing.md) — A sharing mechanism using scoped-down tokens

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
