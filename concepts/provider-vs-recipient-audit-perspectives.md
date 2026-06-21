---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 89e0ecbb76fc28070099b61dcaecbeb10560f3cef2a08702628a335f5c9d9cc6
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-vs-recipient-audit-perspectives
    - PVRAP
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Provider vs Recipient Audit Perspectives
description: Distinction between provider audit logs (recording both provider and recipient actions on shared data) and recipient audit logs (recording share access and provider object management)
tags:
  - delta-sharing
  - audit-logging
  - data-governance
timestamp: "2026-06-19T14:05:19.591Z"
---

#Provider vs Recipient Audit Perspectives

**Provider vs Recipient Audit Perspectives** refers to the distinct sets of audit log events and error messages that data providers and data recipients can monitor when using OpenSharing (the Delta Sharing protocol on Databricks). Understanding the difference helps each party track compliance, troubleshoot access issues, and maintain governance over shared data.

## Overview

OpenSharing audit logs record actions taken by both the provider and the recipient. From the provider’s perspective, logs capture the provider’s own management actions as well as the recipient’s queries against the provider’s shared data. From the recipient’s perspective, logs capture events related to accessing shares and managing provider objects within the recipient’s environment. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access audit logs, an account admin must enable the audit log system table for the Databricks account. Logs are stored in `system.access.audit`. Users who are not account admins or [Metastore](/concepts/metastore.md) admins must be explicitly granted access to `system.access.audit` to read the logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Provider Audit Perspective

Provider audit logs record every action taken by the provider (such as creating shares, adding tables, managing recipients) and also every action taken by recipients when they query the provider’s shared data. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Logged Events

Key OpenSharing events visible in provider logs include:

- `deltaSharingQueriedTableChanges` – logged after a recipient’s query returns data via pre-signed URLs.
- `deltaSharingQueriedTable` – logged after a recipient’s query returns data via pre-signed URLs.
- `generateTemporaryTableCredentials` – logged after a recipient’s query returns data via STS tokens.
- `generateTemporaryVolumeCredentials` – logged after a recipient’s query returns data via STS tokens.

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Viewing Recipient Query Details

Providers can inspect what was shared with a recipient by examining the `response.result` field for pre-signed URL events. This field may contain the number of records returned, table name, table version, file sizes, and recipient identifiers. For STS-token events, providers can look at the `request_params` column, which includes the recipient name, share name, table full name, credential type, and operation. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Error Messages in Provider Logs

When an action fails, the error message is logged in the `response.error_message` field. Provider-specific error conditions include:

- Delta Sharing not enabled on the [Metastore](/concepts/metastore.md) (`FEATURE_DISABLED`)
- Catalog does not exist (`CATALOG_DOES_NOT_EXIST`)
- Permission denied for non-admin users (`PERMISSION_DENIED`)
- [Metastore](/concepts/metastore.md) not assigned to workspace (`INVALID_STATE`)
- Missing or invalid recipient/share name (`INVALID_PARAMETER_VALUE`)
- Attempt to share non-Unity Catalog tables
- Attempt to rotate a recipient with two active tokens
- Duplicate recipient/share name (`RECIPIENT_ALREADY_EXISTS`, `SHARE_ALREADY_EXISTS`)
- Non‑existent recipient/share (`RECIPIENT_DOES_NOT_EXIST`, `SHARE_DOES_NOT_EXIST`)
- Table already added to share (`RESOURCE_ALREADY_EXISTS`)
- Table, schema, or share does not exist (`TABLE_DOES_NOT_EXIST`, `SCHEMA_DOES_NOT_EXIST`, `SHARE_DOES_NOT_EXIST`)

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Recipient Audit Perspective

Recipient audit logs record events that happen within the recipient’s Databricks environment when they access shares or manage provider objects. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Logged Events

The source does not list a separate set of recipient-specific event types beyond the general OpenSharing events, but it does specify that recipient logs cover “events related to the accessing of shares and the management of provider objects.” ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Error Messages in Recipient Logs

When a recipient’s access attempt fails, the log records the error. Recipient-specific error conditions include:

- The user lacks `SELECT` permission on the share (`PERMISSION_DENIED: User does not have SELECT on Share <share-name>`)
- The share does not exist (`SHARE_DOES_NOT_EXIST`)
- The table does not exist within the share (`TABLE_DOES_NOT_EXIST`)

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Comparison at a Glance

| Aspect | Provider Perspective | Recipient Perspective |
|--------|---------------------|-----------------------|
| **What is logged** | Provider’s own management actions *and* recipient queries on shared data | Recipient’s access to shares and management of provider objects |
| **Query details** | Detailed fields (response payload, request params) showing what data was returned or credentials generated | Not detailed in the source |
| **Error categories** | Broad: configuration, permissions, missing entities, duplicate entries | Narrow: permission on share, missing share, missing table |
| **Error messages documented** | Twelve distinct error conditions | Three distinct error conditions |

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for cross-platform data sharing.
- OpenSharing Events – Full list of audit log event types for Delta Sharing.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) system that governs shared data.
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) – The `system.access.audit` table that stores all audit logs.
- Databricks System Tables – How to enable and query system tables.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
