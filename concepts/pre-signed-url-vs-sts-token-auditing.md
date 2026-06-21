---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21fb50bbe348c9e2f0491b98435e6098f65de4f046ef5a3ea1b58d24fd6ffde8
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pre-signed-url-vs-sts-token-auditing
    - PUVSTA
    - Pre-signed URL vs STS token sharing
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Pre-signed URL vs STS Token Auditing
description: OpenSharing supports two credential types for temporary data access — pre-signed URLs and scoped-down STS tokens — each producing distinct audit log fields in provider logs.
tags:
  - databricks
  - audit-logging
  - delta-sharing
  - security
timestamp: "2026-06-19T17:36:31.971Z"
---

# Pre-signed URL vs STS Token Auditing

**Pre-signed URL vs STS Token Auditing** refers to the differences in how data sharing access events are logged in Databricks OpenSharing depending on the credential mechanism used—pre-signed URLs or scoped-down STS tokens. The auditing approach and the fields available for monitoring vary between the two methods.

## Overview

OpenSharing supports sharing asset types such as tables, views, materialized views, streaming tables, and volumes. It provides temporary read access to the underlying data from either pre-signed URLs or from scoped-down STS tokens. The sharing type determines which audit log events are generated and where the relevant details appear. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Pre-signed URL Auditing

When a data recipient's query receives a response for pre-signed URL-based sharing, the provider logs record the events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`. Providers can view the `response.result` field of these logs to see details about what was shared with the recipient. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

The `response.result` field can include values such as `numRecords`, `numAddFiles`, `tableVersion`, `scannedAddFileSize`, `tableName`, `tableId`, `limitHint`, and `userAgent`, among others. This provides visibility into the volume and nature of data returned to the recipient. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## STS Token Auditing

When a data recipient's query receives a response for STS-token-based sharing, the provider logs record the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`. Providers can view the `request_params` column of these logs to see details about what was shared with the recipient. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

The `request_params` field can include values such as `recipient_name`, `share_name`, `table_full_name`, `operation`, `credential_type`, `metastore_id`, `share_owner`, `recipient_id`, and `table_url`. This provides visibility into the identity, scope, and permissions context of the credential request. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Comparison Summary

| Aspect | Pre-signed URL | STS Token |
|--------|---------------|-----------|
| **Logged events** | `deltaSharingQueriedTableChanges`, `deltaSharingQueriedTable` | `generateTemporaryTableCredentials`, `generateTemporaryVolumeCredentials` |
| **Key field for details** | `response.result` | `request_params` |
| **Typical detail fields** | `numRecords`, `numAddFiles`, `tableVersion`, `scannedAddFileSize` | `recipient_name`, `share_name`, `table_full_name`, `operation`, `credential_type` |
| **Focus** | Data volume and query result metadata | Identity, permissions, and credential context |

## Related Concepts

- [Delta Sharing Audit Logs](/concepts/opensharing-audit-logs.md) – General audit logging for OpenSharing events.
- OpenSharing Events – Full list of audit log event types for data sharing.
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) – System table reference for `system.access.audit`.
- [Data Provider Audit Monitoring](/concepts/provider-audit-logs.md) – Best practices for providers monitoring shared data access.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
