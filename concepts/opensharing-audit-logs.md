---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba23b865c05ff2c83b43d17abb491717c20f61768ddcb419fb6196b8a9bfb79a
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-audit-logs
    - OAL
    - Goal
    - OpenSharing Audit Log Events
    - OpenSharing audit log events
    - goal
    - Delta Sharing Audit Logs
    - OpenSharing audit log events reference
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: OpenSharing Audit Logs
description: Audit logs that record actions taken by data providers and recipients in Delta Sharing, stored in system.access.audit or delivered to an S3 bucket
tags:
  - delta-sharing
  - audit-logging
  - monitoring
timestamp: "2026-06-19T14:05:12.294Z"
---

# OpenSharing Audit Logs

**OpenSharing Audit Logs** record events related to [Delta Sharing](/concepts/delta-sharing.md) data sharing activities, enabling both data providers and recipients to monitor access, queries, and management operations on shared data assets. Audit logs capture actions taken by the provider, actions taken by recipients on the provider's shared data, and recipient-side events related to share access and provider object management. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access audit logs, an account admin must enable the audit log system table for your Databricks account. Audit logs are stored in `system.access.audit` when system tables are enabled. If an account has an audit log delivery setup instead, you need to know the bucket and path where the logs are delivered. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

Users who are not account admins or [Metastore](/concepts/metastore.md) admins must be granted access to `system.access.audit` to read audit logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Viewing OpenSharing Events

OpenSharing supports sharing asset types including tables, views, materialized views, streaming tables, and volumes. The platform provides temporary read access to underlying data through either pre-signed URLs or scoped-down STS tokens, and the sharing type determines which audit log events are recorded. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Pre-Signed URL Shares

In the provider logs, the events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` are logged after a data recipient's query receives a response for pre-signed URL-based sharing. Providers can view the `response.result` field of these logs to see additional details about what was shared with the recipient. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

The `response.result` field may include values such as:
- `numRecords` — the number of records returned
- `numAddFiles` — the number of AddFile entries returned in the query
- `scannedAddFileSize` — the file size in bytes for the AddFile returned
- `tableName` — the name of the queried table
- `tableVersion` — the version of the table
- `userAgent` — the client user agent string
- `deltaSharingRecipientIdHash` — a hashed identifier for the recipient

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### STS Token Shares

In the provider logs, the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` are logged after a data recipient's query receives a response for STS-token-based sharing. Providers can view the `request_params` column of these logs to see additional details about what was shared. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

The `request_params` field may include values such as:
- `recipient_name` — the name of the recipient
- `share_name` — the name of the share
- `table_full_name` — the fully qualified table name
- `table_url` — the storage path for the table
- `operation` — the operation performed (e.g., `READ`)
- `credential_type` — the type of credential used

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

For the complete list of OpenSharing audit log events, see the Databricks documentation on OpenSharing events. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Errors

If an attempted OpenSharing action fails, the action is logged with the error message in the `response.error_message` field of the log. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Error Messages in Provider Logs

OpenSharing logs the following errors for data providers:

- **Feature disabled:** `FEATURE_DISABLED:Delta Sharing is not enabled`
- **Catalog not found:** `CATALOG_DOES_NOT_EXIST:Catalog '<catalog>' does not exist.`
- **Permission denied:** `PERMISSION_DENIED:Only administrators can <operation-name> <operation-target>`
- **Invalid [Metastore](/concepts/metastore.md) assignment:** `INVALID_STATE:Workspace <workspace-name> is no longer assigned to this metastore`
- **Missing required field:** `INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare Missing required field: <recipient-name>/<share-name>`
- **Invalid name:** `INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare <recipient-name>/<share-name> is not a valid name`
- **Non-Unity Catalog table:** `INVALID_PARAMETER_VALUE: Only managed or external table on Unity Catalog can be added to a share`
- **Duplicate active tokens:** `INVALID_PARAMETER_VALUE: There are already two active tokens for recipient <recipient-name>`
- **Duplicate recipient or share:** `RECIPIENT_ALREADY_EXISTS/SHARE_ALREADY_EXISTS: Recipient/Share <name> already exists`
- **Recipient or share not found:** `RECIPIENT_DOES_NOT_EXIST/SHARE_DOES_NOT_EXIST: Recipient/Share '<name>' does not exist`
- **Duplicate table in share:** `RESOURCE_ALREADY_EXISTS: Shared Table '<name>' already exists`
- **Table not found:** `TABLE_DOES_NOT_EXIST: Table '<name>' does not exist`
- **Schema not found:** `SCHEMA_DOES_NOT_EXIST: Schema '<name>' does not exist`
- **Share not found:** `SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.`

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Error Messages in Recipient Logs

OpenSharing logs the following errors for data recipients:

- **No SELECT permission:** `PERMISSION_DENIED:User does not have SELECT on Share <share-name>`
- **Share not found:** `SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.`
- **Table not found in share:** `TABLE_DOES_NOT_EXIST: <table-name> does not exist.`

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The framework for secure data sharing across platforms
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — The `system.access.audit` table that stores audit events
- System Tables — The system table infrastructure that enables audit logging
- [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) — A sharing method that uses temporary signed URLs
- [STS Token Sharing](/concepts/sts-token-sharing.md) — A sharing method that uses scoped-down security tokens
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) and catalog system that governs OpenSharing

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
