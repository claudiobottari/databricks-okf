---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 031aaa5b3c1ed9d02666221534b249e9cd35ab7dc9ded7c0d78bdbc7d1a803d3
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - system-tables-for-unity-catalog-audit
    - STFUCA
    - System tables (Unity Catalog)
    - System catalog
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: System Tables for Unity Catalog Audit
description: The system.access.audit system table requirement for accessing OpenSharing audit logs, requiring account admin enablement and appropriate permissions for non-admin users.
tags:
  - system-tables
  - databricks
  - audit-logging
timestamp: "2026-06-18T14:29:21.785Z"
---

# System Tables for Unity Catalog Audit

**System tables for Unity Catalog audit** provide a standardized, queryable repository of operational and governance events within [Unity Catalog](/concepts/unity-catalog.md) on Databricks. These tables enable data providers and recipients to monitor data sharing activities, access patterns, and errors across [Delta Sharing](/concepts/delta-sharing.md) and [OpenSharing](/concepts/opensharing.md) workloads.

## Overview

System tables are Databricks-managed schemas that store metadata and audit records for various Unity Catalog operations. The primary audit-related system table is `system.access.audit`, which captures audit log events for actions taken within the Unity Catalog [Metastore](/concepts/metastore.md). ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

To access audit logs through system tables, an account admin must first enable the audit log system table for your Databricks account. Once enabled, the audit data is stored in the `system.access.audit` table. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

If you are not an account admin or [Metastore](/concepts/metastore.md) admin, you must be granted explicit access to `system.access.audit` to read audit logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Events

The audit log records events related to [OpenSharing](/concepts/opensharing.md) activities. Audit logs are stored in `system.access.audit` when system tables are enabled for your account. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Pre-signed URL Shares

For pre-signed URL-based sharing, the provider logs record the following events after a data recipient's query receives a response:

- `deltaSharingQueriedTableChanges` — Logged when table changes are queried
- `deltaSharingQueriedTable` — Logged when table data is queried

Providers can view the `response.result` field of these logs to see details about what was shared with the recipient. The `response.result` field can include values such as `checkpointBytes`, `earlyTermination`, `maxRemoveFiles`, `path`, `deltaSharingPartitionFilteringAccessed`, `deltaSharingRecipientId`, `deltaSharingRecipientIdHash`, `jsonLogFileNum`, `scannedJsonLogActionNum`, `numRecords`, `deltaSharingRecipientMetastoreId`, `userAgent`, and `jsonLogFileBytes`. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### STS-token Shares

For [STS-token](/concepts/sts-token-sharing.md)-based sharing, the provider logs record the following events:

- `generateTemporaryTableCredentials` — Logged when temporary table credentials are generated
- `generateTemporaryVolumeCredentials` — Logged when temporary volume credentials are generated

Providers can view the `request_params` column of these logs to see details about what was shared with the recipient. The `request_params` field can include values such as `recipient_name`, `share_id`, `credential_type`, `is_permissions_enforcing_client`, `table_full_name`, `operation`, `share_name`, `table_id`, `share_owner`, `recipient_id`, `table_url`, and `metastore_id`. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Logged Errors

When an attempted OpenSharing action fails, the error is logged with the error message in the `response.error_message` field. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Error Messages in Provider Logs

Provider-side logs record the following error conditions:

- `FEATURE_DISABLED:Delta Sharing is not enabled` — OpenSharing is not enabled on the selected [Metastore](/concepts/metastore.md)
- `CATALOG_DOES_NOT_EXIST:Catalog '<catalog>' does not exist.` — An operation was attempted on a catalog that does not exist
- `PERMISSION_DENIED:Only administrators can <operation-name> <operation-target>` — A non-admin user attempted a privileged operation
- `INVALID_STATE:Workspace <workspace-name> is no longer assigned to this metastore` — An operation was attempted on a [Metastore](/concepts/metastore.md) from a workspace to which it is not assigned
- `INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare Missing required field: <recipient-name>/<share-name>` — A request was missing the recipient name or share name
- `INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare <recipient-name>/<share-name> is not a valid name` — A request included an invalid recipient or share name
- `INVALID_PARAMETER_VALUE: Only managed or external table on Unity Catalog can be added to a share` — A user attempted to share a table not in a Unity Catalog [Metastore](/concepts/metastore.md)
- `INVALID_PARAMETER_VALUE: There are already two active tokens for recipient <recipient-name>` — A user attempted to rotate a recipient with two active tokens
- `RECIPIENT_ALREADY_EXISTS/SHARE_ALREADY_EXISTS: Recipient/Share <name> already exists` — A duplicate recipient or share was created
- `RECIPIENT_DOES_NOT_EXIST/SHARE_DOES_NOT_EXIST: Recipient/Share '<name>' does not exist` — An operation referenced a non-existent recipient or share
- `RESOURCE_ALREADY_EXISTS: Shared Table '<name>' already exists` — A table was added to a share that already contained it
- `TABLE_DOES_NOT_EXIST: Table '<name>' does not exist` — A referenced table does not exist
- `SCHEMA_DOES_NOT_EXIST: Schema '<name>' does not exist` — A referenced schema does not exist
- `SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` — A recipient attempted to access a non-existent share

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Error Messages in Recipient Logs

Recipient-side logs record the following error conditions:

- `PERMISSION_DENIED:User does not have SELECT on Share <share-name>` — The user attempted to access a share they lack permission for
- `SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` — The user attempted to access a non-existent share
- `TABLE_DOES_NOT_EXIST: <table-name> does not exist.` — The user attempted to access a table that does not exist in the share

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- System Tables — Databricks-managed schemas for operational metadata
- Audit Logs — Historical record of actions performed in Unity Catalog
- [Delta Sharing](/concepts/delta-sharing.md) — Data sharing protocol for Unity Catalog
- [OpenSharing](/concepts/opensharing.md) — Open-standard data sharing capabilities
- Data Governance — Practices for managing data access and compliance
- [Account Admin](/concepts/account-admin-unity-catalog.md) — Role responsible for enabling system tables

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
