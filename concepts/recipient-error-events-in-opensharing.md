---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e40f3223efff26a49bda4b91d9eee4764dd1d9c4020a3683f408393c5c59dd2
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-error-events-in-opensharing
    - REEIO
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Recipient Error Events in OpenSharing
description: OpenSharing logs specific error messages for recipients, including permission denied on shares, missing shares, and missing tables within shares.
tags:
  - databricks
  - error-handling
  - delta-sharing
timestamp: "2026-06-19T17:36:46.086Z"
---

# Recipient Error Events in OpenSharing

**Recipient Error Events in OpenSharing** are logged errors that occur on the recipient side when a user attempts to access shared data through [OpenSharing](/concepts/opensharing.md). These events are recorded in the recipient’s audit logs and help recipients diagnose permission or availability issues when querying shared assets.

## Overview

When an OpenSharing action initiated by a recipient fails, the error message is stored in the `response.error_message` field of the audit log entry. Recipients can review these logs to identify the cause of access failures. The following errors are specific to data recipients. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Error Messages in Recipient Logs

OpenSharing logs the following errors for data recipients:

- **Permission denied on a share** – The user attempted to access a share they do not have permission to access.  
  `DatabricksServiceException: PERMISSION_DENIED:User does not have SELECT on Share <share-name>`

- **Share does not exist** – The user attempted to access a share that does not exist.  
  `DatabricksServiceException: SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.`

- **Table does not exist in the share** – The user attempted to access a table that does not exist in the share.  
  `DatabricksServiceException: TABLE_DOES_NOT_EXIST: <table-name> does not exist.`

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

These errors may appear when a recipient tries to read from a share that was revoked, renamed, or never granted. They are distinct from provider-side errors, which cover issues like [Metastore](/concepts/metastore.md) configuration, missing recipients, or duplicate resources.

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The data sharing protocol used.
- Audit Logs for OpenSharing – General overview of logged events for providers and recipients.
- [Provider Error Events in OpenSharing](/concepts/provider-error-events-in-opensharing.md) – Errors recorded on the data provider side.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying sharing technology.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
