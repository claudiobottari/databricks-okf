---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10e6899220bfd3c7f12cc3e43eaf803ba47c6cf012ec41842bf8052a34c036d5
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-error-events-in-opensharing
    - PEEIO
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Provider Error Events in OpenSharing
description: OpenSharing logs specific error messages for providers, covering failures such as disabled features, missing catalogs, permission denials, invalid names, and duplicate resources.
tags:
  - databricks
  - error-handling
  - delta-sharing
timestamp: "2026-06-19T17:36:47.716Z"
---

# Provider Error Events in OpenSharing

**Provider Error Events in OpenSharing** are audit-log entries that record failed actions taken by a data provider or by a recipient interacting with the provider’s shared data. When an OpenSharing action fails, the error is logged in the `system.access.audit` table (or delivered via an audit log delivery setup) with the error message stored in the `response.error_message` field. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

These error events help providers diagnose configuration issues, permission problems, and resource availability. The following errors are specific to the provider’s audit logs; a separate set of errors appears in recipient logs.

## Common Provider Error Messages

OpenSharing logs the following error messages for data providers. Items between `<` and `>` characters represent placeholder text that should be replaced with actual values in the log. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

| Error Message | Likely Cause | Details |
|---------------|--------------|---------|
| `DatabricksServiceException: FEATURE_DISABLED:Delta Sharing is not enabled` | OpenSharing is not enabled on the selected [Metastore](/concepts/metastore.md). | The provider must enable Delta Sharing on the [Metastore](/concepts/metastore.md). |
| `DatabricksServiceException: CATALOG_DOES_NOT_EXIST:Catalog '<catalog>' does not exist.` | The referenced catalog does not exist. | Verify the catalog name. |
| `DatabricksServiceException: PERMISSION_DENIED:Only administrators can <operation-name> <operation-target>` | A user who is not an account admin or [Metastore](/concepts/metastore.md) admin attempted a privileged operation. | Only admins can perform the operation. |
| `DatabricksServiceException: INVALID_STATE:Workspace <workspace-name> is no longer assigned to this metastore` | The workspace is no longer assigned to the [Metastore](/concepts/metastore.md). | Reassign the [Metastore](/concepts/metastore.md) to the workspace. |
| `DatabricksServiceException: INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare Missing required field: <recipient-name>/<share-name>` | A required field was missing when creating a recipient or share. | Provide the missing field. |
| `DatabricksServiceException: INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare <recipient-name>/<share-name> is not a valid name` | The recipient or share name is invalid. | Use a valid naming convention. |
| `DatabricksServiceException: INVALID_PARAMETER_VALUE: Only managed or external table on Unity Catalog can be added to a share` | The table is not in a Unity Catalog [Metastore](/concepts/metastore.md). | Only Unity Catalog tables can be shared. |
| `DatabricksServiceException: INVALID_PARAMETER_VALUE: There are already two active tokens for recipient <recipient-name>` | Attempt to rotate a recipient that already has two active tokens. | Wait for one token to expire before rotating. |
| `DatabricksServiceException: RECIPIENT_ALREADY_EXISTS/SHARE_ALREADY_EXISTS: Recipient/Share <name> already exists` | Duplicate recipient or share name. | Use a unique name. |
| `DatabricksServiceException: RECIPIENT_DOES_NOT_EXIST/SHARE_DOES_NOT_EXIST: Recipient/Share '<name>' does not exist` | Attempt to operate on a non-existent recipient or share. | Check the name. |
| `DatabricksServiceException: RESOURCE_ALREADY_EXISTS: Shared Table '<name>' already exists` | Attempt to add a table that is already in the share. | The table is already shared. |
| `DatabricksServiceException: TABLE_DOES_NOT_EXIST: Table '<name>' does not exist` | The referenced table does not exist. | Verify the table name. |
| `DatabricksServiceException: SCHEMA_DOES_NOT_EXIST: Schema '<name>' does not exist` | The referenced schema does not exist. | Verify the schema name. |
| `DatabricksServiceException: SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` | Attempt to access a share that does not exist. | Check the share name. |

## How Errors Are Logged

When an OpenSharing action fails, the error is recorded in the provider’s audit log. The log entry includes the `response.error_message` field containing the exact exception string shown above. Providers can query `system.access.audit` or their audit log delivery bucket to monitor these failures. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Differentiating Provider and Recipient Error Events

Recipient errors (e.g., `PERMISSION_DENIED: User does not have SELECT on Share`) appear in the recipient’s audit logs, not the provider’s. Provider error events focus on provider-side actions such as creating shares, adding tables, rotating tokens, and configuring metastores. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing Audit Logs](/concepts/opensharing-audit-logs.md) – General overview of monitoring OpenSharing via audit logs.
- [Recipient Error Events in OpenSharing](/concepts/recipient-error-events-in-opensharing.md) – Errors logged on the recipient side.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying protocol for OpenSharing.
- System Tables – Where audit logs are stored.
- [Unity Catalog](/concepts/unity-catalog.md) – Required [Metastore](/concepts/metastore.md) for shared tables.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
