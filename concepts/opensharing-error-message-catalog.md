---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e8bd55996f021fa267a254fff094d40a0b50eb1a096c7c575164dcb05b9c818
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-error-message-catalog
    - OEMC
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: OpenSharing Error Message Catalog
description: Standardized error messages logged in OpenSharing audit logs for both providers and recipients, covering permission, existence, and configuration failures.
tags:
  - error-messages
  - delta-sharing
  - troubleshooting
  - audit-logging
timestamp: "2026-06-19T22:09:27.012Z"
---

# OpenSharing Error Message Catalog

The **OpenSharing Error Message Catalog** documents the error messages that are logged when OpenSharing (Delta Sharing) operations fail. These errors are recorded in the `response.error_message` field of the audit log system table (`system.access.audit`) and help data providers and recipients diagnose failures in sharing operations. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Messages in Provider Logs

OpenSharing logs the following errors for data providers:

### Configuration and Feature Errors

- **OpenSharing not enabled**: `DatabricksServiceException: FEATURE_DISABLED:Delta Sharing is not enabled` — raised when OpenSharing is not enabled on the selected [Metastore](/concepts/metastore.md). ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Catalog and [Metastore](/concepts/metastore.md) Errors

- **Catalog does not exist**: `DatabricksServiceException: CATALOG_DOES_NOT_EXIST:Catalog '<catalog>' does not exist.` — an operation was attempted on a catalog that does not exist. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Metastore not assigned**: `DatabricksServiceException: INVALID_STATE:Workspace <workspace-name> is no longer assigned to this metastore` — an operation was attempted on a [Metastore](/concepts/metastore.md) from a workspace to which the [Metastore](/concepts/metastore.md) is not assigned. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Permission Errors

- **Non-admin operation**: `DatabricksServiceException: PERMISSION_DENIED:Only administrators can <operation-name> <operation-target>` — a user who is not an account admin or [Metastore](/concepts/metastore.md) admin attempted to perform a privileged operation. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Parameter Validation Errors

- **Missing recipient or share name**: `DatabricksServiceException: INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare Missing required field: <recipient-name>/<share-name>` — a request was missing the recipient name or share name. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Invalid recipient or share name**: `DatabricksServiceException: INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare <recipient-name>/<share-name> is not a valid name` — a request included an invalid recipient name or share name. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Non-Unity Catalog table**: `DatabricksServiceException: INVALID_PARAMETER_VALUE: Only managed or external table on Unity Catalog can be added to a share` — a user attempted to share a table that is not in a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Duplicate active tokens**: `DatabricksServiceException: INVALID_PARAMETER_VALUE: There are already two active tokens for recipient <recipient-name>` — a user attempted to rotate a recipient that was already in a rotated state and whose previous token had not yet expired. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Existence and Conflict Errors

- **Recipient or share already exists**: `DatabricksServiceException: RECIPIENT_ALREADY_EXISTS/SHARE_ALREADY_EXISTS: Recipient/Share <name> already exists` — a user attempted to create a new recipient or share with the same name as an existing one. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Recipient or share does not exist**: `DatabricksServiceException: RECIPIENT_DOES_NOT_EXIST/SHARE_DOES_NOT_EXIST: Recipient/Share '<name>' does not exist` — a user attempted to perform an operation on a recipient or share that does not exist. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Table already added to share**: `DatabricksServiceException: RESOURCE_ALREADY_EXISTS: Shared Table '<name>' already exists` — a user attempted to add a table to a share, but the table had already been added. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Table does not exist**: `DatabricksServiceException: TABLE_DOES_NOT_EXIST: Table '<name>' does not exist` — an operation referenced a table that does not exist. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Schema does not exist**: `DatabricksServiceException: SCHEMA_DOES_NOT_EXIST: Schema '<name>' does not exist` — an operation referenced a schema that did not exist. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Share does not exist (provider)**: `DatabricksServiceException: SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` — a user attempted to access a share that does not exist. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Messages in Recipient Logs

OpenSharing logs the following errors for data recipients:

- **Permission denied on share**: `DatabricksServiceException: PERMISSION_DENIED:User does not have SELECT on Share <share-name>` — the user attempted to access a share they do not have permission to access. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Share does not exist (recipient)**: `DatabricksServiceException: SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.` — the user attempted to access a share that does not exist. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- **Table does not exist in share**: `DatabricksServiceException: TABLE_DOES_NOT_EXIST: <table-name> does not exist.` — the user attempted to access a table that does not exist in the share. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Message Format

Error messages follow the pattern:

```
DatabricksServiceException: <ERROR_CODE>:<error message>
```

The `ERROR_CODE` is a machine-readable identifier (e.g., `FEATURE_DISABLED`, `PERMISSION_DENIED`, `INVALID_PARAMETER_VALUE`, `RECIPIENT_ALREADY_EXISTS`, `SHARE_DOES_NOT_EXIST`, `TABLE_DOES_NOT_EXIST`, `SCHEMA_DOES_NOT_EXIST`, `RESOURCE_ALREADY_EXISTS`, `INVALID_STATE`, `CATALOG_DOES_NOT_EXIST`). The error message provides a human-readable description of the failure. Items between `<` and `>` characters in the message represent placeholder text that is replaced with actual values in the log output. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Viewing Error Logs

Errors can be found in the `response.error_message` field of audit log entries. To access audit logs, an account admin must enable the [audit log system table](/concepts/audit-log-system-table-requirements.md) for your Databricks account. If you are not an account admin or [Metastore](/concepts/metastore.md) admin, you must be given access to `system.access.audit` to read audit logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- Audit and monitor data sharing — Overview of monitoring OpenSharing events
- OpenSharing event types — The events that trigger audit log entries
- [OpenSharing provider setup](/concepts/opensharing-provider-object.md) — Configuration for data providers
- [OpenSharing recipient setup](/concepts/opensharing-recipient.md) — Configuration for data recipients
- Pre-signed URL vs STS token sharing — Two sharing mechanisms with different audit event types

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
