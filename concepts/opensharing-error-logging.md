---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8657b0d6fbb015d8df0d1cd074e7279e8d669e3eae758a9266b88527f2d9186a
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-error-logging
    - OEL
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: OpenSharing Error Logging
description: Standardized error messages logged for failed OpenSharing operations in both provider and recipient audit logs, including errors for missing entities, permission denials, and configuration issues
tags:
  - delta-sharing
  - error-handling
  - debugging
timestamp: "2026-06-19T14:05:29.722Z"
---

---

title: OpenSharing Error Logging
summary: Comprehensive catalog of error messages logged when OpenSharing actions fail, covering provider errors (permissions, missing resources, duplication) and recipient errors (access denied, missing shares/tables).
sources:
  - audit-and-monitor-data-sharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:49:32.429Z"
updatedAt: "2026-06-19T09:04:50.644Z"
tags:
  - delta-sharing
  - error-handling
  - troubleshooting
aliases:
  - opensharing-error-logging
  - OEL
confidence: 0.97
provenanceState: extracted
inferredParagraphs: 3
---

# OpenSharing Error Logging

**OpenSharing Error Logging** captures failed actions during data sharing operations. When an OpenSharing action fails, the event is logged in the [audit log system table](/concepts/audit-log-system-table-requirements.md) (`system.access.audit`) with an error message in the `response.error_message` field. Both data providers and data recipients can inspect these logged errors to diagnose access, configuration, or permission issues. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Messages in Provider Logs

Data providers encounter the following logged errors when managing shares and recipients. In each case, items between `<` and `>` represent placeholder text that is replaced with actual values in the log. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

- **OpenSharing not enabled on the metastore**:  
  `DatabricksServiceException: FEATURE_DISABLED:Delta Sharing is not enabled`

- **Operation on a catalog that does not exist**:  
  `DatabricksServiceException: CATALOG_DOES_NOT_EXIST:Catalog '<catalog>' does not exist.`

- **Permission denied – non-admin user attempted a privileged operation**:  
  `DatabricksServiceException: PERMISSION_DENIED:Only administrators can <operation-name> <operation-target>`

- **Metastore not assigned to the workspace**:  
  `DatabricksServiceException: INVALID_STATE:Workspace <workspace-name> is no longer assigned to this metastore`

- **Missing required field (recipient name or share name)**:  
  `DatabricksServiceException: INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare Missing required field: <recipient-name>/<share-name>`

- **Invalid recipient name or share name**:  
  `DatabricksServiceException: INVALID

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
