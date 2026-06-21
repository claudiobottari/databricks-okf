---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb67b36f682d27451f345f290cf2c613ea645521246039bbb9853f7f785f0831
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sts-token-sharing-audit-details
    - STSAD
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: STS Token Sharing Audit Details
description: Audit log fields for STS token-based sharing, including generateTemporaryTableCredentials and generateTemporaryVolumeCredentials events with credential and table metadata.
tags:
  - audit-logging
  - delta-sharing
  - sts-tokens
  - data-access
timestamp: "2026-06-19T22:09:04.456Z"
---

# STS Token Sharing Audit Details

**STS Token Sharing Audit Details** describes the audit log events and fields captured when a data provider shares data via scoped-down AWS STS tokens through [OpenSharing](/concepts/opensharing.md) ([Delta Sharing](/concepts/delta-sharing.md)). These audit logs give providers full visibility into what was shared and who accessed it.

## Requirements

To view STS token sharing audit logs, an account admin must enable the [audit log system table](/concepts/audit-log-system-table-requirements.md) for your Databricks account. Audit events are then stored in the `system.access.audit` table. If your account uses an alternative audit log delivery setup, you need to know the delivery bucket and path. If you are not an account admin or [metastore admin](/concepts/metastore-admin-role.md), you must be granted access to `system.access.audit`.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

For STS-token-based sharing, two audit events are logged after a data recipient's query receives a response:

- `generateTemporaryTableCredentials` – generated when temporary credentials are issued for a table, view, or other relational asset.
- `generateTemporaryVolumeCredentials` – generated when temporary credentials are issued for a Unity Catalog volume.

These events appear in the provider's audit logs.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Details Available in `request_params`

Providers can inspect the `request_params` column of the audit log to see detailed information about the credentials request. The field may include the following values (list not exhaustive):^[audit-and-monitor-data-sharing-databricks-on-aws.md]

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

Key fields in the `request_params` object:^[audit-and-monitor-data-sharing-databricks-on-aws.md]

| Field | Description |
|---|---|
| `recipient_name` | Name of the recipient as defined in the share. |
| `share_name` | Name of the share accessed. |
| `share_id` | UUID of the share. |
| `recipient_id` | UUID of the recipient. |
| `share_owner` | Owner of the share. |
| `table_full_name` | Fully qualified name of the shared table (e.g., `catalog.schema.table`). |
| `table_id` | UUID of the shared table. |
| `table_url` | Storage location (e.g., S3 path) of the table's data. |
| `credential_type` | Type of credential issued (typically `StorageCredential`). |
| `operation` | The access operation (e.g., `READ`). |
| `metastore_id` | UUID of the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). |

## Differences from Pre-Signed URL Shares

For pre-signed URL sharing, the provider logs events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`, with details in the `response.result` field. For STS-token sharing, the relevant events are `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`, with details in the `request_params` field.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Logging

Failed STS token requests are also logged. The `response.error_message` field contains the error description. For example, an attempted access to a share without sufficient permissions logs:^[audit-and-monitor-data-sharing-databricks-on-aws.md]

```
DatabricksServiceException: PERMISSION_DENIED:User does not have SELECT on Share <share-name>
```

Other common errors include missing recipients, non-existent shares, or disabled Delta Sharing.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The Delta Sharing protocol used for cross-platform data sharing.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for secure data sharing across platforms.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages shares and recipients.
- [Audit log system table](/concepts/audit-log-system-table-requirements.md) – The system table (`system.access.audit`) that stores audit events.
- AWS STS – The AWS service providing temporary credentials used in STS token sharing.
- [Pre-signed URL Sharing Audit Details](/concepts/pre-signed-url-sharing-audit-events.md) – The equivalent audit details for pre-signed URL sharing.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
