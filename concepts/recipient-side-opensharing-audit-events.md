---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 855d3da9c2277b580904e45ca92a0f33c14e572c673d86013bd2360e0abc83ac
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-side-opensharing-audit-events
    - ROAE
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Recipient-side OpenSharing Audit Events
description: Audit events visible to data recipients in OpenSharing, focused on accessing shares and managing provider objects, with specific error messages for permission and existence failures.
tags:
  - audit-logging
  - recipients
  - delta-sharing
timestamp: "2026-06-18T14:28:57.529Z"
---

# Recipient-side OpenSharing Audit Events

**Recipient-side OpenSharing Audit Events** are audit log entries that record actions taken by a data recipient in the context of [Delta Sharing](/concepts/delta-sharing.md) (OpenSharing). These events cover the recipient’s access to shared data and their management of provider objects, such as shares and recipients, within their own Databricks environment. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access recipient audit logs, an account admin must enable the audit log system table for the Databricks account (see Enable system tables). If the user is not an account admin or [Metastore](/concepts/metastore.md) admin, they must be granted access to `system.access.audit` to read the logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Viewing OpenSharing Events

If system tables are enabled, audit logs are stored in `system.access.audit`. Alternatively, if the account has an audit log delivery setup configured, the logs are delivered to a specified bucket and path. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

Recipient audit logs record events related to:

- Accessing shares (e.g., querying a shared table)
- Managing provider objects (e.g., creating or modifying recipients)

For a full list of OpenSharing events, see the [OpenSharing events](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs#ds) documentation. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Messages in Recipient Logs

When an OpenSharing action fails on the recipient side, the error is logged in the `response.error_message` field. The following error messages are specifically logged for data recipients. Items between `<` and `>` represent placeholder text.

- **Permission denied** – The user attempted to access a share they do not have `SELECT` permission on.
  ```
  DatabricksServiceException: PERMISSION_DENIED:User does not have SELECT on Share <share-name>
  ```

- **Share does not exist** – The user attempted to access a share that does not exist.
  ```
  DatabricksServiceException: SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.
  ```

- **Table does not exist** – The user attempted to access a table that does not exist in the share.
  ```
  DatabricksServiceException: TABLE_DOES_NOT_EXIST: <table-name> does not exist.
  ```

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for sharing data across Databricks workspaces
- [OpenSharing](/concepts/opensharing.md) – Databricks’ implementation of Delta Sharing
- [Audit log system table](/concepts/audit-log-system-table-requirements.md) – The `system.access.audit` table that stores audit logs
- [Data provider audit events](/concepts/provider-audit-logs.md) – Audit events logged by the data provider side
- Troubleshooting Delta Sharing errors – Guidance for resolving common sharing issues

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
