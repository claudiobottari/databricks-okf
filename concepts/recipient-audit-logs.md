---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a2567ad63b64b718d1daa9f7a5b2780e1abee40442cc92346772c216bdf0629
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-audit-logs
    - RAL
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Recipient Audit Logs
description: Audit logs recording events related to accessing shares and managing provider objects from the data consumer side, including recipient-specific error messages.
tags:
  - delta-sharing
  - audit-logging
  - data-consumer
timestamp: "2026-06-19T09:04:34.462Z"
---

---
title: Recipient Audit Logs
summary: Audit logs recorded for data recipients capturing events related to accessing shares and managing provider objects in OpenSharing.
sources:
  - audit-and-monitor-data-sharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:49:17.666Z"
updatedAt: "2026-06-18T10:49:17.666Z"
tags:
  - audit-logging
  - data-recipient
  - databricks
aliases:
  - recipient-audit-logs
  - RAL
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Recipient Audit Logs

**Recipient audit logs** record events related to a data recipient’s access to shared data in OpenSharing ([Delta Sharing](/concepts/delta-sharing.md)). These logs capture actions such as querying shares, managing provider objects, and any errors that occur during those operations.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access recipient audit logs, an account admin must first enable the [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) for your Databricks account. The audit logs are then stored in `system.access.audit`. If you are not an account admin or [Metastore](/concepts/metastore.md) admin, you must be granted access to read the `system.access.audit` table.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Accessing recipient audit logs

If your account has system tables enabled, you can query recipient audit log events directly from the `system.access.audit` table. If your account uses an [audit log delivery setup](https://docs.databricks.com/aws/en/admin/account-settings/audit-log-delivery) instead, you need to know the bucket and path where the logs are delivered.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged events

Recipient audit logs record events related to the accessing of shares and the management of provider objects. For a full list of OpenSharing audit log events, see the [OpenSharing events](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs#ds) reference.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Viewing query result details

OpenSharing supports sharing asset types such as tables, views, materialized views, streaming tables, and volumes. The way query results are logged depends on the sharing type used for access.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Pre-signed URL shares

For shares that use pre-signed URLs, provider audit logs record `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` events after a recipient’s query receives a response. Providers can inspect the `response.result` field of these logs to see details such as the number of records returned, table version, and file size information.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### STS-token shares

For shares that use scoped-down STS tokens, provider audit logs record `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` events. Providers can inspect the `request_params` column of these logs to see details such as the recipient name, share name, table name, and credential type.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged errors

If an OpenSharing action attempted by a recipient fails, the event is logged with the error message in the `response.error_message` field. The following errors are specific to recipient actions:^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- **Permission denied**: The recipient user does not have `SELECT` on the share.  
  `DatabricksServiceException: PERMISSION_DENIED:User does not have SELECT on Share <share-name>`

- **Share does not exist**: The recipient attempted to access a share that does not exist.  
  `DatabricksServiceException: SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.`

- **Table does not exist**: The recipient attempted to access a table that does not exist in the share.  
  `DatabricksServiceException: TABLE_DOES_NOT_EXIST: <table-name> does not exist.`

## Related concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for data sharing that OpenSharing is built on
- [Provider Audit Logs](/concepts/provider-audit-logs.md) — Audit logs that record actions taken by the data provider and by recipients on shared data
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — The system table (`system.access.audit`) that stores audit log events
- [OpenSharing](/concepts/opensharing.md) — Databricks implementation of Delta Sharing with audit tracking

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
