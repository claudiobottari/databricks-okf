---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: afdf02c3be839c7b014d1e45c86566fafe2cae405e1fdfdd6f6d3e43446b59d1
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-opensharing-audit-log-system-table
    - DOALST
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Databricks OpenSharing Audit Log System Table
description: The system.access.audit table stores OpenSharing audit events, accessible to account admins and authorized users when system tables are enabled.
tags:
  - databricks
  - audit-logging
  - delta-sharing
timestamp: "2026-06-19T17:36:38.754Z"
---

Here is the wiki page for "Databricks OpenSharing Audit Log System Table", written based solely on the provided source material.

---

## Databricks OpenSharing Audit Log System Table

The **Databricks OpenSharing Audit Log System Table** (`system.access.audit`) stores a comprehensive record of all events related to [OpenSharing](/concepts/opensharing.md) on Databricks, enabling both data providers and recipients to monitor data sharing activity. The table captures actions taken by providers (such as creating shares and adding tables) as well as actions taken by recipients (such as querying shared data). ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Prerequisites

To access the audit log system table, an account admin must first enable system tables for the Databricks account. Non-admin users must be granted explicit access to `system.access.audit` to read audit logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Logged Events

The system table logs a wide range of OpenSharing events, including CRUD operations on recipients and shares. For a full list of event types, see the [OpenSharing audit log events reference](/concepts/opensharing-audit-logs.md). ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Viewing Details of Recipient Query Results

When a recipient queries shared data, the audit log records details about what was returned, with the format depending on the credential type used for access.

#### Pre-signed URL Shares

For shares accessed via pre-signed URLs, the events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` are logged after the provider responds. Providers can inspect the `response.result` column to see details such as the number of records returned, the table version, file sizes, and a recipient hash identifier. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

#### STS Token Shares

For shares accessed via scoped-down STS tokens, the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` are logged. Providers can view the `request_params` column to see recipient name, share name, table name, credential type, and operation (typically `READ`). ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Logged Errors

When an OpenSharing action fails, the error is recorded in the `response.error_message` field of the audit log. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

#### Provider-side Errors

Common provider errors logged include:

- **OpenSharing not enabled:** `FEATURE_DISABLED:Delta Sharing is not enabled`
- **Catalog does not exist:** `CATALOG_DOES_NOT_EXIST:Catalog '<name>' does not exist.`
- **Permission denied for non-admin:** `PERMISSION_DENIED:Only administrators can <operation> <target>`
- **Invalid or missing parameters:** `INVALID_PARAMETER_VALUE: ...`
- **Duplicate recipient/share:** `RECIPIENT_ALREADY_EXISTS / SHARE_ALREADY_EXISTS`
- **Recipient or share not found:** `RECIPIENT_DOES_NOT_EXIST / SHARE_DOES_NOT_EXIST`
- **Table already in share:** `RESOURCE_ALREADY_EXISTS: Shared Table '<name>' already exists`

#### Recipient-side Errors

Common recipient errors logged include:

- **No permission on share:** `PERMISSION_DENIED:User does not have SELECT on Share <share-name>`
- **Share not found:** `SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.`
- **Table not found in share:** `TABLE_DOES_NOT_EXIST: <table-name> does not exist.`

### Comparison with Audit Log Delivery

If the account uses Audit Log Delivery instead of system tables, the logs are delivered to a customer-managed bucket and path rather than stored in `system.access.audit`. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The underlying protocol for sharing data across Databricks workspaces.
- Audit Log System Table Reference — Schema and event documentation for `system.access.audit`.
- [OpenSharing Audit Log Events](/concepts/opensharing-audit-logs.md) — Full list of logged action types.
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) that governs shared assets.
- Data Provider — The entity that shares data.
- [Data Recipient](/concepts/data-recipient.md) — The entity that accesses shared data.

### Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
