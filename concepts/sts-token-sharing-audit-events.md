---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73b7d333e1d6e9e59abee5940839380dfee541f1c4751b01917ac62337c472c4
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sts-token-sharing-audit-events
    - STSAE
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: STS Token Sharing Audit Events
description: Audit events (generateTemporaryTableCredentials, generateTemporaryVolumeCredentials) logged when data recipients query shared data via scoped-down STS token-based sharing, with request_params details.
tags:
  - delta-sharing
  - sts-tokens
  - audit-events
timestamp: "2026-06-19T09:04:53.971Z"
---

## STS Token Sharing Audit Events

**STS Token Sharing Audit Events** are audit log entries generated when a data recipient queries shared data in [Delta Sharing](/concepts/delta-sharing.md) using scoped-down AWS Security Token Service (STS) credentials. These events appear in the provider's audit logs under the `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` actions, providing visibility into what data was accessed and by whom.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Overview

OpenSharing supports sharing asset types such as tables, views, materialized views, streaming tables, and volumes. For STS-token-based sharing, the provider issues temporary credentials that grant scoped-down read access to the underlying data. When a recipient uses these credentials to query shared data, the provider's audit logs record the event.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Logged Events

In the provider logs, the following events are logged after a data recipient's query receives a response for STS-token-based sharing:^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `generateTemporaryTableCredentials`
- `generateTemporaryVolumeCredentials`

### Request Details

Providers can view the `request_params` column of these logs to see details about what was shared with the recipient. This field can include the following values (list not exhaustive):^[audit-and-monitor-data-sharing-databricks-on-aws.md]

```json
{
  "recipient_name": "someRecipientName",
  "share_id": "ea7a4555-43d9-4cbd-a5df-f4f5193f297e",
  "credential_type": "StorageCredential",
  "is_permissions_enforcing_client": "true",
  "table_full_name": "someTableName",
  "operation": "READ",
  "share_name": "someShareName",
  "table_id": "someTableId",
  "share_owner": "someShareOwner",
  "recipient_id": "someRecipientId",
  "table_url": "s3://somePath",
  "metastore_id": "someMetastoreId"
}
```

### Requirements

To view STS token sharing audit events, the following requirements must be met:^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- An account admin must enable the [audit log system table](/concepts/audit-log-system-table-requirements.md) for the Databricks account.
- If you are not an account admin or [Metastore](/concepts/metastore.md) admin, you must be granted access to `system.access.audit` to read audit logs.

### Logged Errors

Error events related to STS token sharing are recorded in the `response.error_message` field of the log. Common error messages for data providers include:^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `FEATURE_DISABLED:Delta Sharing is not enabled` — OpenSharing is not enabled on the [Metastore](/concepts/metastore.md).
- `PERMISSION_DENIED:Only administrators can <operation> <target>` — A non-admin attempted a privileged operation.
- `SHARE_DOES_NOT_EXIST: Share <name> does not exist.` — The recipient attempted to access a non-existent share.

For recipients, logged errors include:^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- `PERMISSION_DENIED:User does not have SELECT on Share <share-name>` — The user lacks permission on the share.
- `SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` — The share does not exist.
- `TABLE_DOES_NOT_EXIST: <table-name> does not exist.` — The table does not exist in the share.

### Comparison with Pre-Signed URL Shares

STS token sharing events differ from [Pre-signed URL Sharing Audit Events](/concepts/pre-signed-url-sharing-audit-events.md). For pre-signed URL-based sharing, the logged events are `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`, with details in the `response.result` field. For STS token-based sharing, the events are `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`, with details in the `request_params` field.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing Audit Logs](/concepts/opensharing-audit-logs.md)
- [Pre-signed URL Sharing Audit Events](/concepts/pre-signed-url-sharing-audit-events.md)
- Audit Log System Table Reference
- OpenSharing Event Reference

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
