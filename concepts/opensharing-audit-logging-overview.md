---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a2bcd7db9ef6b00207a9d732dc9f1d53d667ee839ff111ad274236ee510244e
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-audit-logging-overview
    - OALO
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: OpenSharing Audit Logging Overview
description: Audit logging infrastructure for monitoring Delta Sharing (OpenSharing) events, covering both provider and recipient perspectives with logged events and error messages.
tags:
  - delta-sharing
  - audit-logging
  - monitoring
timestamp: "2026-06-19T09:04:26.025Z"
---

# OpenSharing Audit Logging Overview

**OpenSharing Audit Logging** refers to the system of recording and monitoring events related to Delta Sharing data sharing activities within Databricks. Audit logs provide both data providers and data recipients with visibility into sharing operations, including queries executed against shared data, credential generation, and error events.

## Overview

Audit logs for OpenSharing capture actions taken by data providers and data recipients on shared datasets. These logs are essential for security monitoring, compliance reporting, and troubleshooting sharing-related issues. The audit logs are stored in the `system.access.audit` system table when enabled, or delivered to a configured storage location via audit log delivery. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access audit logs, an account admin must first enable the audit log system table for the Databricks account. Non-admin users must be granted access to `system.access.audit` to read audit logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

OpenSharing logs events for various sharing operations. For a complete list of events, see the OpenSharing events documentation. Each event captures details about the action performed, the user or recipient involved, and the resources affected. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Viewing Recipient Query Details

OpenSharing supports sharing asset types including tables, views, materialized views, streaming tables, and volumes. Data access is provided through temporary read access via pre-signed URLs or scoped-down STS tokens. The type of sharing determines how the audit log events are structured. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Pre-Signed URL Shares

For pre-signed URL-based sharing, the provider logs record events such as `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` after a recipient's query receives a response. Providers can examine the `response.result` field to see details about what was shared, including the table name, number of records returned, file sizes, and table version. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### STS-Token Shares

For STS-token-based sharing, the provider logs record events such as `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` when a recipient's query receives a response. Providers can examine the `request_params` field to see details including the recipient name, share name, table name, operation type, and storage path. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Errors

When an OpenSharing action fails, the action is logged with the error message in the `response.error_message` field of the audit log. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Provider Error Messages

Common errors logged for data providers include:
- `FEATURE_DISABLED`: Delta Sharing is not enabled on the selected [Metastore](/concepts/metastore.md).
- `CATALOG_DOES_NOT_EXIST`: Attempted operation on a catalog that does not exist.
- `PERMISSION_DENIED`: A non-admin user attempted a privileged operation.
- `INVALID_STATE`: The workspace is no longer assigned to the [Metastore](/concepts/metastore.md).
- `INVALID_PARAMETER_VALUE`: Missing or invalid recipient name, share name, or table type.
- `RECIPIENT_ALREADY_EXISTS` / `SHARE_ALREADY_EXISTS`: A recipient or share with the same name already exists.
- `RECIPIENT_DOES_NOT_EXIST` / `SHARE_DOES_NOT_EXIST`: Attempted operation on a non-existent recipient or share.
- `RESOURCE_ALREADY_EXISTS`: A table was already added to a share.
- `TABLE_DOES_NOT_EXIST` / `SCHEMA_DOES_NOT_EXIST`: Referenced table or schema does not exist.

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Recipient Error Messages

Common errors logged for data recipients include:
- `PERMISSION_DENIED`: The user does not have SELECT permission on the share.
- `SHARE_DOES_NOT_EXIST`: The share does not exist.
- `TABLE_DOES_NOT_EXIST`: The table does not exist in the share.

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The underlying protocol for data sharing.
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) – The `system.access.audit` table where logs are stored.
- OpenSharing Events – The full list of logged event types.
- System Tables – The system table infrastructure for Databricks accounts.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
