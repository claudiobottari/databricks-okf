---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4a233941cf92597d0f3b494f6b96c5b38dcd62ab3abb2b74041c6d34cc9757b6
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-audit-log-events
    - RALE
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Recipient Audit Log Events
description: Audit events recorded for data recipients in OpenSharing, covering share access attempts and management of provider objects.
tags:
  - audit-logging
  - delta-sharing
  - data-recipients
timestamp: "2026-06-19T22:08:59.361Z"
---

# Recipient Audit Log Events

**Recipient Audit Log Events** are entries in the [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) that record actions taken by a data recipient when accessing shares shared by a provider, as well as management actions on provider objects. These logs are part of the [OpenSharing](/concepts/opensharing.md) audit infrastructure and are stored in `system.access.audit` when system tables are enabled. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access recipient audit logs, an account admin must first enable the audit log system table for the Databricks account. Users who are not account admins or [Metastore](/concepts/metastore.md) admins must be granted access to `system.access.audit` to read the logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

The audit log for recipients captures events related to the **accessing of shares** and the **management of provider objects**. These events include both successful operations and failed attempts. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

Specific event types for recipients are not listed in the source documentation; instead, the logged information includes error messages when an action fails. The `response.error_message` field of the log entry contains the error details. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Messages in Recipient Logs

When a recipient’s action fails, OpenSharing logs the following errors (items between `<` and `>` represent placeholder text):

| Error | Message |
|-------|---------|
| Permission Denied | `DatabricksServiceException: PERMISSION_DENIED:User does not have SELECT on Share <share-name>` |
| Share Does Not Exist | `DatabricksServiceException: SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` |
| Table Does Not Exist | `DatabricksServiceException: TABLE_DOES_NOT_EXIST: <table-name> does not exist.` |

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

These errors indicate that the recipient tried to access a share they are not authorized for, or tried to query a share or table that does not exist in the provider’s catalog. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [Data Provider Audit Log Events](/concepts/provider-audit-log-events.md) – Audit events recorded for the provider side of data sharing.
- [OpenSharing](/concepts/opensharing.md) – The protocol underlying Delta Sharing audit logging.
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) – The system table storing all audit events.
- [Delta Sharing](/concepts/delta-sharing.md) – The overall data sharing framework.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
