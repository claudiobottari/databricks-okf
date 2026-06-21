---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5450fac6d83450c12240553cf594a7878b7a7681e364621bcf87d0e1f2940fc5
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-audit-log-fields-for-sts-token-queries
    - OALFFSTQ
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: OpenSharing Audit Log Fields for STS Token Queries
description: Provider audit logs for generateTemporaryTableCredentials events capture recipient_name, share_name, credential_type, operation, and table_url to track STS-token-based sharing.
tags:
  - databricks
  - audit-logging
  - delta-sharing
timestamp: "2026-06-19T17:36:56.552Z"
---

## OpenSharing Audit Log Fields for STS Token Queries

**OpenSharing Audit Log Fields for STS Token Queries** refers to the set of fields logged in the Databricks audit log when a data recipient’s query triggers an STS-token‑based sharing operation. These fields appear in the `request_params` column of the provider audit log events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`.

### Overview

OpenSharing supports two temporary credential mechanisms for granting read access to shared data: pre‑signed URLs and scoped‑down STS tokens. For STS‑token shares, the provider logs record the details of what was shared in the `request_params` column of the audit log. Providers can inspect these fields to understand which recipient, share, table, or volume was accessed, and which credential type was used. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Viewing STS Token Details in Provider Logs

When a data recipient’s query receives a response for STS‑token‑based sharing, the provider audit log records either:

- `generateTemporaryTableCredentials` for table, view, materialized view, or streaming table access, or
- `generateTemporaryVolumeCredentials` for volume access.

The `request_params` column of these log entries contains a JSON object with the fields described below. The list is not exhaustive. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Fields in the `request_params` Column

The following fields are documented in the source material:

| Field | Description |
|-------|-------------|
| `recipient_name` | Name of the recipient accessing the share. |
| `share_id` | Unique identifier of the share. |
| `credential_type` | Type of credential used; typically `StorageCredential`. |
| `is_permissions_enforcing_client` | Indicates whether the client enforces permissions. |
| `table_full_name` | Full name of the table being accessed (three‑level namespace). |
| `operation` | Operation performed; typically `READ`. |
| `share_name` | Name of the share. |
| `table_id` | Unique identifier of the table. |
| `share_owner` | Owner of the share. |
| `recipient_id` | Unique identifier of the recipient. |
| `table_url` | URL or path to the underlying storage location (e.g., `s3://somePath`). |
| `metastore_id` | Unique identifier of the Unity Catalog [Metastore](/concepts/metastore.md). |

^[audit-and-monitor-data-sharing-databricks-on-aws.md]

These fields allow a provider to trace which recipient queried which table, under which share, and which storage location was accessed via the temporary STS credential.

### Related Concepts

- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) – The `system.access.audit` table that stores audit logs.
- [OpenSharing](/concepts/opensharing.md) – Databricks' implementation of Delta Sharing for read‑only data sharing.
- STS Token – Temporary security credentials scoped to a specific storage location.
- [Pre‑signed URL Sharing](/concepts/pre-signed-url-sharing.md) – Alternative credential mechanism with different logged fields (`response.result`).
- [OpenSharing Audit Log Events](/concepts/opensharing-audit-logs.md) – Complete list of OpenSharing events, including `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials`.

### Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
